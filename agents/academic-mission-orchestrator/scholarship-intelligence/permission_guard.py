#!/usr/bin/env python3
"""Least-privilege capability broker with one-time, scope-bound approvals.

A remote LLM cannot authorize itself by returning JSON. Approval is granted
only through an interactive local terminal prompt and then consumed once.
"""
from __future__ import annotations
from datetime import datetime, timezone
import hashlib
import os
import sqlite3
from pathlib import Path
import secrets
import sys
import time
from urllib.parse import urlsplit

AUTO = {"public.fetch", "public.discover", "public.analyze", "local.draft"}
REVIEW = {"portal.fill", "portal.upload", "portal.submit", "email.send",
          "private.export", "payment.pay", "legal.sign"}
HUMAN_ONLY = {"auth.password", "auth.2fa", "auth.biometric", "captcha.solve"}
ALLOWED = AUTO | REVIEW | HUMAN_ONLY
MAX_TTL = 900


def target_valid(url: str, host_allowlist: list[str]) -> bool:
    try:
        p=urlsplit(url)
        host=(p.hostname or "").lower().rstrip(".")
        return (p.scheme == "https" and host in {
            h.lower().rstrip(".") for h in host_allowlist}
            and p.username is None and p.password is None
            and p.port in (None,443) and not p.fragment)
    except ValueError:
        return False


def decision(action: str, url: str, host_allowlist: list[str]) -> str:
    if action not in ALLOWED:
        return "DENY_UNRECOGNIZED"
    if not target_valid(url,host_allowlist):
        return "DENY_HOST"
    if action in HUMAN_ONLY:
        return "HUMAN_ONLY"
    return "ALLOW_AUTONOMOUS" if action in AUTO else "REQUIRE_ONE_TIME_APPROVAL"


def _scope_hash(action: str, url: str, artifact_sha256: str) -> str:
    if action not in ALLOWED or not isinstance(artifact_sha256,str):
        raise ValueError("Ação ou resumo de artefato inválido")
    if artifact_sha256 and (len(artifact_sha256) != 64 or
                           any(c not in "0123456789abcdef" for c in artifact_sha256)):
        raise ValueError("SHA-256 inválido")
    return hashlib.sha256(
        (action+"\0"+url+"\0"+artifact_sha256).encode("utf-8")).hexdigest()


class ApprovalLedger:
    def __init__(self, path: str):
        p=Path(path).expanduser().resolve()
        if str(p).startswith(str(Path(__file__).resolve().parent)+os.sep):
            raise ValueError("Armazene autorizações fora do repositório")
        p.parent.mkdir(parents=True,exist_ok=True,mode=0o700)
        self.db=sqlite3.connect(str(p))
        self.db.execute("""CREATE TABLE IF NOT EXISTS grants(
            token_hash TEXT PRIMARY KEY, scope_hash TEXT NOT NULL,
            expires INTEGER NOT NULL, consumed INTEGER NOT NULL DEFAULT 0,
            issued INTEGER NOT NULL)""")
        self.db.commit()
        if os.name == "posix":
            os.chmod(p,0o600)

    def close(self):
        self.db.close()

    def issue_interactively(self, action: str, url: str, allowed_hosts: list[str],
                            *, artifact_sha256: str = "", ttl: int = 300) -> str:
        if decision(action,url,allowed_hosts) != "REQUIRE_ONE_TIME_APPROVAL":
            raise PermissionError("Ação não admite emissão automática de autorização")
        if not 30 <= ttl <= MAX_TTL:
            raise ValueError("TTL inválido")
        if not sys.stdin.isatty():
            raise PermissionError("Autorização exige terminal interativo local")
        label=f"AUTORIZO {action}"
        print("OPERAÇÃO EXTERNA; confirme o endereço no navegador antes de autorizar.")
        print("Ação:",action,"Destino:",url,"SHA256:",artifact_sha256 or "(sem anexo)")
        typed=input(f"Digite exatamente '{label}' para permitir UMA execução: ")
        if typed != label:
            raise PermissionError("Autorização recusada")
        token=secrets.token_urlsafe(32)
        now=int(time.time())
        with self.db:
            self.db.execute(
                "INSERT INTO grants VALUES (?,?,?,?,?)",
                (hashlib.sha256(token.encode()).hexdigest(),
                 _scope_hash(action,url,artifact_sha256),now+ttl,0,now))
        return token

    def consume(self, token: str, action: str, url: str,
                allowed_hosts: list[str], *, artifact_sha256: str = "",
                now: int | None = None) -> bool:
        if decision(action,url,allowed_hosts) != "REQUIRE_ONE_TIME_APPROVAL":
            raise PermissionError("Ação não permite aprovação delegada")
        now=int(time.time()) if now is None else int(now)
        token_hash=hashlib.sha256(token.encode()).hexdigest()
        expected=_scope_hash(action,url,artifact_sha256)
        with self.db:
            cur=self.db.execute(
                """UPDATE grants SET consumed=1 WHERE token_hash=? AND scope_hash=?
                AND consumed=0 AND expires>=?""",
                (token_hash,expected,now))
        return cur.rowcount==1
