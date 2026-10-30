#!/usr/bin/env python3
"""Persistent, bounded, auditable mission queue for PUBLIC source checks.

This queue does NOT run a browser, perform login, submit forms, or store applicant
data. It persists public source identifiers and non-sensitive result summaries.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import sqlite3
import time
from typing import Callable

from scholarship_agent import read_json, scan_source, discover_page, official_url

VALID_ACTIONS = ("PUBLIC_SCAN", "PUBLIC_DISCOVER")
JOB_STATES = ("QUEUED", "RUNNING", "DONE", "RETRY", "WAITING_HUMAN", "DEAD_LETTER")
IDENTIFIER = re.compile(r"^[a-zA-Z0-9._:-]{1,100}$")


class MissionQueue:
    def __init__(self, path: str):
        self.path = Path(path).expanduser().resolve()
        if str(self.path).startswith(str(Path(__file__).resolve().parent) + os.sep):
            raise ValueError("Banco operacional deve ficar FORA do repositório Git")
        self.path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
        if os.name == "posix":
            os.chmod(self.path.parent, 0o700)
        self.db = sqlite3.connect(str(self.path), timeout=15)
        self.db.row_factory = sqlite3.Row
        self.db.execute("PRAGMA busy_timeout=15000")
        self.db.execute("PRAGMA journal_mode=WAL")
        self.db.executescript("""
            CREATE TABLE IF NOT EXISTS jobs (
              id TEXT PRIMARY KEY,
              action TEXT NOT NULL,
              source_id TEXT NOT NULL,
              state TEXT NOT NULL DEFAULT 'QUEUED',
              attempts INTEGER NOT NULL DEFAULT 0,
              max_attempts INTEGER NOT NULL DEFAULT 4,
              due_ts INTEGER NOT NULL,
              lease_until INTEGER,
              result_json TEXT,
              error_kind TEXT,
              created_ts INTEGER NOT NULL,
              updated_ts INTEGER NOT NULL
            );
            CREATE INDEX IF NOT EXISTS idx_jobs_due ON jobs(state,due_ts);
            CREATE TABLE IF NOT EXISTS audit (
              event_id INTEGER PRIMARY KEY AUTOINCREMENT,
              job_id TEXT NOT NULL,
              state TEXT NOT NULL,
              event TEXT NOT NULL,
              occurred_ts INTEGER NOT NULL
            );
        """)
        self.db.commit()
        if os.name == "posix" and self.path.exists():
            os.chmod(self.path, 0o600)

    def close(self):
        self.db.close()

    def enqueue(self, job_id: str, action: str, source_id: str,
                now: int | None = None, max_attempts: int = 4) -> bool:
        if not IDENTIFIER.fullmatch(job_id) or not IDENTIFIER.fullmatch(source_id):
            raise ValueError("Identificadores inválidos (sem dados pessoais)")
        if action not in VALID_ACTIONS:
            raise PermissionError("A fila executa apenas leitura de fontes públicas")
        if not 1 <= max_attempts <= 10:
            raise ValueError("max_attempts deve estar entre 1 e 10")
        now = int(time.time()) if now is None else int(now)
        with self.db:
            result = self.db.execute(
                """INSERT OR IGNORE INTO jobs
                (id,action,source_id,due_ts,created_ts,updated_ts,max_attempts)
                VALUES (?,?,?,?,?,?,?)""",
                (job_id, action, source_id, now, now, now, max_attempts))
            if result.rowcount:
                self._audit(job_id, "QUEUED", "enqueued", now)
            return bool(result.rowcount)

    def _audit(self, job_id: str, state: str, event: str, now: int):
        self.db.execute(
            "INSERT INTO audit(job_id,state,event,occurred_ts) VALUES(?,?,?,?)",
            (job_id, state, event, now))

    def claim(self, now: int | None = None, lease_seconds: int = 120):
        now = int(time.time()) if now is None else int(now)
        if not 10 <= lease_seconds <= 3600:
            raise ValueError("Lease fora dos limites")
        self.db.execute("BEGIN IMMEDIATE")
        try:
            row = self.db.execute(
                """SELECT * FROM jobs WHERE
                  (state IN ('QUEUED','RETRY') AND due_ts <= ?)
                  OR (state='RUNNING' AND lease_until <= ?)
                  ORDER BY due_ts ASC, created_ts ASC LIMIT 1""", (now,now)).fetchone()
            if row is None:
                self.db.commit()
                return None
            if row["attempts"] >= row["max_attempts"]:
                self.db.execute("UPDATE jobs SET state='DEAD_LETTER',updated_ts=? WHERE id=?",
                                (now,row["id"]))
                self._audit(row["id"],"DEAD_LETTER","retry budget exhausted",now)
                self.db.commit()
                return None
            self.db.execute(
                """UPDATE jobs SET state='RUNNING', attempts=attempts+1,
                lease_until=?,updated_ts=? WHERE id=?""",
                (now+lease_seconds, now, row["id"]))
            self._audit(row["id"],"RUNNING","claimed",now)
            self.db.commit()
            return dict(self.db.execute("SELECT * FROM jobs WHERE id=?",(row["id"],)).fetchone())
        except Exception:
            self.db.rollback()
            raise

    def complete(self, job_id: str, summary: dict, now: int | None = None):
        now = int(time.time()) if now is None else int(now)
        allowed = ("status","sha256","checked_at_utc","content_type","leads_count")
        filtered = {k:summary[k] for k in allowed if k in summary}
        with self.db:
            r = self.db.execute(
                """UPDATE jobs SET state='DONE', result_json=?, error_kind=NULL,
                lease_until=NULL,updated_ts=? WHERE id=? AND state='RUNNING'""",
                (json.dumps(filtered,ensure_ascii=False),now,job_id))
            if not r.rowcount:
                raise ValueError("Trabalho não estava em execução")
            self._audit(job_id,"DONE","completed",now)

    def fail(self, job_id: str, kind: str, now: int | None = None):
        """No exception content, identifiers or credentials are logged."""
        now = int(time.time()) if now is None else int(now)
        if kind not in ("TRANSIENT","AUTH_REQUIRED","CAPTCHA","ROBOTS",
                        "PORTAL_CHANGED","MANUAL_REVIEW","PERMANENT"):
            kind = "MANUAL_REVIEW"
        row = self.db.execute("SELECT * FROM jobs WHERE id=?",(job_id,)).fetchone()
        if row is None or row["state"] != "RUNNING":
            raise ValueError("Trabalho não estava em execução")
        if kind == "TRANSIENT" and row["attempts"] < row["max_attempts"]:
            state = "RETRY"
            wait = min(3600, 15 * (2 ** (row["attempts"] - 1)))
        elif kind in ("AUTH_REQUIRED","CAPTCHA","ROBOTS","PORTAL_CHANGED","MANUAL_REVIEW"):
            state, wait = "WAITING_HUMAN", 0
        else:
            state, wait = "DEAD_LETTER", 0
        with self.db:
            self.db.execute(
                """UPDATE jobs SET state=?,error_kind=?,due_ts=?,lease_until=NULL,
                updated_ts=? WHERE id=?""", (state,kind,now+wait,now,job_id))
            self._audit(job_id,state,kind,now)

    def get(self, job_id: str):
        row = self.db.execute("SELECT * FROM jobs WHERE id=?", (job_id,)).fetchone()
        return dict(row) if row else None

    def summary(self):
        return {r["state"]: r["count"] for r in self.db.execute(
            "SELECT state, COUNT(*) AS count FROM jobs GROUP BY state")}


def perform(job: dict, registry: dict, fetcher: Callable | None = None):
    hosts = registry["allowed_hosts"]
    sources = {x["label"]: x["url"] for x in registry["watch_urls"]}
    sources.update({x["id"]:x["official_url"] for x in registry["opportunities"]})
    if job["source_id"] not in sources:
        raise ValueError("Fonte desconhecida no registro autorizado")
    url = sources[job["source_id"]]
    if not official_url(url, hosts):
        raise PermissionError("URL fora dos domínios oficiais")
    if fetcher:
        result = fetcher(job["action"], url, hosts)
    elif job["action"] == "PUBLIC_SCAN":
        result = scan_source(url, hosts)
    elif job["action"] == "PUBLIC_DISCOVER":
        result = discover_page(url, hosts)
    else:
        raise PermissionError("Ação proibida")
    if result["status"] in ("ROBOTS_UNAVAILABLE","ROBOTS_DISALLOWED"):
        return {"error":"ROBOTS"}
    if result["status"] not in ("FETCHED","DISCOVERED_LEADS"):
        return {"error":"MANUAL_REVIEW"}
    return {"status":result["status"],"sha256":result.get("sha256"),
            "checked_at_utc":result.get("checked_at_utc"),
            "leads_count":len(result.get("leads",[])),
            "content_type":result.get("content_type")}


def process_one(queue: MissionQueue, registry: dict, fetcher: Callable | None = None,
                now: int | None = None):
    job = queue.claim(now=now)
    if not job:
        return None
    try:
        result = perform(job, registry, fetcher)
        if "error" in result:
            queue.fail(job["id"],result["error"],now=now)
        else:
            queue.complete(job["id"],result,now=now)
    except (TimeoutError, ConnectionError):
        queue.fail(job["id"],"TRANSIENT",now=now)
    except Exception:
        # No error message, URL, applicant data or source body in the audit log.
        queue.fail(job["id"],"MANUAL_REVIEW",now=now)
    row = queue.get(job["id"])
    return {"job_id":job["id"],"state":row["state"],"error_kind":row["error_kind"]}


def main(argv=None):
    p=argparse.ArgumentParser(description="Agente local persistente de fontes oficiais")
    p.add_argument("--db",required=True,help="Caminho privado FORA do repositório")
    p.add_argument("--registry",default=str(Path(__file__).with_name("sources.json")))
    sub=p.add_subparsers(dest="command",required=True)
    en=sub.add_parser("enqueue")
    en.add_argument("--source-id",required=True)
    en.add_argument("--action",choices=VALID_ACTIONS,default="PUBLIC_SCAN")
    sub.add_parser("run-once")
    sub.add_parser("status")
    args=p.parse_args(argv)
    registry=read_json(args.registry)
    queue=MissionQueue(args.db)
    try:
        if args.command=="enqueue":
            ids={x["label"] for x in registry["watch_urls"]}
            ids.update(x["id"] for x in registry["opportunities"])
            if args.source_id not in ids:
                p.error("Fonte não encontrada no registro")
            job_id=f"{args.action.lower()}:{args.source_id}"
            print(json.dumps({"job_id":job_id,
                              "created":queue.enqueue(job_id,args.action,args.source_id)},
                             ensure_ascii=False))
        elif args.command=="run-once":
            print(json.dumps(process_one(queue,registry),ensure_ascii=False))
        else:
            print(json.dumps(queue.summary(),ensure_ascii=False))
    finally:
        queue.close()

if __name__=="__main__":
    main()
