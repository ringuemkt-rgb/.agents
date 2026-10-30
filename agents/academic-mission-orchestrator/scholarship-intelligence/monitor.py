#!/usr/bin/env python3
"""Bounded official-source monitor for a scheduled or local execution.

A run emits only source IDs, statuses and timestamps; NO candidate details.
No automatic form, email, account or payment access.
"""
from __future__ import annotations
import argparse
from datetime import date, datetime, timezone
import json
import os
from pathlib import Path
import tempfile
import time

from mission_runtime import MissionQueue, process_one, source_index
from scholarship_agent import read_json

def monitor(registry: dict, db_path: str, *, max_sources: int = 6,
            day: date | None = None, sleep_seconds: float = 1.5) -> dict:
    if not 1 <= max_sources <= 30 or not 0 <= sleep_seconds <= 30:
        raise ValueError("Limites inválidos")
    day=day or date.today()
    jobs=[]
    index=source_index(registry)
    watch_ids=[name for name in index if name.startswith("watch-")][:max_sources]
    q=MissionQueue(db_path)
    try:
        for name in watch_ids:
            job_id=f"daily-{day.isoformat()}:{name}"
            q.enqueue(job_id,"PUBLIC_DISCOVER",name)
            jobs.append(job_id)
        results=[]
        for i in range(len(jobs)):
            if i: time.sleep(sleep_seconds)
            result=process_one(q,registry)
            if result is None:
                break
            results.append(result)
        return {
            "date":day.isoformat(),
            "checked_at_utc":datetime.now(timezone.utc).isoformat(),
            "workflows_processed":len(results),
            "jobs":[{"id":x["job_id"],"status":x["state"],
                    "error_kind":x["error_kind"]} for x in results],
            "note":"Resultado da consulta técnica, não certificação de edital aberto."
        }
    finally:
        q.close()

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--registry",default=str(Path(__file__).with_name("sources.json")))
    p.add_argument("--db",help="Path SQLite privado externo ao repo; sem argumento usa temporário")
    p.add_argument("--max-sources",type=int,default=6)
    p.add_argument("--out",help="JSON de status sem dados pessoais")
    args=p.parse_args()
    registry=read_json(args.registry)
    if args.db:
        result=monitor(registry,args.db,max_sources=args.max_sources)
    else:
        with tempfile.TemporaryDirectory(prefix="scholarship-public-") as d:
            result=monitor(registry,os.path.join(d,"jobs.sqlite3"),
                           max_sources=args.max_sources)
    report=json.dumps(result,indent=2,ensure_ascii=False)
    if args.out:
        Path(args.out).write_text(report+"\n",encoding="utf-8")
    else:
        print(report)

if __name__=="__main__":
    main()
