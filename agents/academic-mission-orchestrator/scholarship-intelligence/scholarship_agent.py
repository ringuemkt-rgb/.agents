#!/usr/bin/env python3
"""Scholarship Intelligence v1 — auditable, privacy-first local CLI.

No real applicant data is included or transmitted. Source checks inspect public pages
only. Neither this CLI nor the browser companion submits an application.
"""
from __future__ import annotations

import argparse
from datetime import date, datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit
from urllib.request import Request, build_opener, HTTPRedirectHandler
from urllib.robotparser import RobotFileParser

VERSION = "0.1.0"
STATES = (
    "DISCOVERED", "VERIFIED_OFFICIAL", "APPLICATION_DRAFT",
    "SUBMITTED_CONFIRMED", "ADMITTED", "FUNDING_SELECTED",
    "FUNDING_IMPLEMENTED", "PAID", "EXPIRED", "REJECTED",
)
TRANSITIONS = {
    "DISCOVERED": {"VERIFIED_OFFICIAL", "EXPIRED", "REJECTED"},
    "VERIFIED_OFFICIAL": {"APPLICATION_DRAFT", "EXPIRED", "REJECTED"},
    "APPLICATION_DRAFT": {"SUBMITTED_CONFIRMED", "EXPIRED", "REJECTED"},
    "SUBMITTED_CONFIRMED": {"ADMITTED", "REJECTED"},
    "ADMITTED": {"FUNDING_SELECTED", "REJECTED"},
    "FUNDING_SELECTED": {"FUNDING_IMPLEMENTED", "REJECTED"},
    "FUNDING_IMPLEMENTED": {"PAID"},
    "PAID": set(),
    "EXPIRED": set(),
    "REJECTED": set(),
}
GATED = {"SUBMITTED_CONFIRMED", "ADMITTED", "FUNDING_SELECTED",
         "FUNDING_IMPLEMENTED", "PAID"}


def read_json(path: str | Path):
    with open(path, encoding="utf-8") as stream:
        return json.load(stream)


def write_json(path: str | Path, data):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as stream:
        json.dump(data, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


def official_url(url: str, allowed_hosts: list[str]) -> bool:
    parts = urlsplit(url)
    if parts.scheme != "https" or parts.username or parts.password:
        return False
    if parts.port not in (None, 443):
        return False
    host = (parts.hostname or "").lower().rstrip(".")
    return host in {h.lower().rstrip(".") for h in allowed_hosts}


def validate_record(item: dict, allowed_hosts: list[str]):
    required = ["id", "title", "official_url", "status", "application_actor"]
    missing = [x for x in required if not item.get(x)]
    if missing:
        raise ValueError(f"{item.get('id', '?')}: missing {missing}")
    if item["status"] not in STATES:
        raise ValueError(f"{item['id']}: invalid status")
    if item["application_actor"] not in ("candidate", "program", "other"):
        raise ValueError(f"{item['id']}: invalid application actor")
    if not official_url(item["official_url"], allowed_hosts):
        raise ValueError(f"{item['id']}: official_url outside allowlist")
    if item.get("deadline"):
        date.fromisoformat(item["deadline"])
    if item["status"] == "VERIFIED_OFFICIAL" and not item.get("evidence_date"):
        raise ValueError(f"{item['id']}: official status needs evidence_date")
    return True


def rank(item: dict, profile: dict, today: date) -> dict:
    """Transparent triage score, NOT admission likelihood or scholarship odds."""
    deadline = date.fromisoformat(item["deadline"]) if item.get("deadline") else None
    reasons: list[str] = []
    if deadline and deadline < today:
        return {"id": item["id"], "status": "PRAZO_ENCERRADO", "score": 0,
                "reasons": ["O prazo documentado é anterior à data consultada."]}
    if item["status"] not in ("VERIFIED_OFFICIAL", "APPLICATION_DRAFT"):
        reasons.append("Verificar novo edital primário antes de considerar elegível.")
    if item["application_actor"] != "candidate":
        reasons.append("O edital exige submissão institucional; não é inscrição direta.")
    interests = {s.lower() for s in profile.get("interests", [])}
    topics = {s.lower() for s in item.get("topics", [])}
    preferred = {s.lower() for s in profile.get("preferred_states", [])}
    state = str(item.get("state", "")).lower()
    overlap = sorted(interests & topics)
    score = min(50, len(overlap) * 15)
    if state and state in preferred:
        score += 20
        reasons.append("Estado dentro da região preferencial.")
    if overlap:
        reasons.append("Temas coincidentes: " + ", ".join(overlap))
    if deadline:
        remaining = (deadline - today).days
        if remaining <= 7:
            score += 20
            reasons.append(f"Prazo urgente: {remaining} dia(s).")
        elif remaining <= 30:
            score += 10
            reasons.append(f"Prazo em {remaining} dias.")
    if item["application_actor"] != "candidate":
        score = max(0, score - 20)
    if item["status"] not in ("VERIFIED_OFFICIAL", "APPLICATION_DRAFT"):
        score = max(0, score - 20)
    score = max(0, min(100, score))
    reasons.append("Pontuação = triagem operacional, não nota oficial ou chance de aprovação.")
    return {"id": item["id"], "status": "TRIAGEM", "score": score,
            "reasons": reasons, "source": item["official_url"],
            "deadline": item.get("deadline")}


def transition(current: str, target: str, evidence: str, approved: bool = False) -> dict:
    if current not in STATES or target not in STATES:
        raise ValueError("Estado desconhecido")
    if target not in TRANSITIONS[current]:
        raise ValueError(f"Transição inválida: {current} → {target}")
    if not evidence.strip():
        raise ValueError("Comprovante externo verificável obrigatório")
    if target in GATED and not approved:
        raise PermissionError("Confirmação humana obrigatória para estado consequencial")
    return {"previous": current, "current": target, "evidence": evidence,
            "human_approved": approved,
            "logged_at_utc": datetime.now(timezone.utc).isoformat()}


class SafeRedirect(HTTPRedirectHandler):
    def __init__(self, allowed_hosts):
        super().__init__()
        self.allowed_hosts = allowed_hosts

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if not official_url(newurl, self.allowed_hosts):
            raise ValueError("Redirect fora da allowlist")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def scan_source(url: str, allowed_hosts: list[str]) -> dict:
    """Low-volume public source monitor. No login, CAPTCHA, or form submission."""
    if not official_url(url, allowed_hosts):
        raise ValueError("URL não permitida")
    parsed = urlsplit(url)
    robots_url = f"https://{parsed.hostname}/robots.txt"
    robot = RobotFileParser()
    robot.set_url(robots_url)
    try:
        robot.read()
    except Exception:
        return {"url": url, "status": "ROBOTS_UNAVAILABLE", "requires_manual_check": True}
    if not robot.can_fetch("ScholarshipIntelligence/0.1", url):
        return {"url": url, "status": "ROBOTS_DISALLOWED", "requires_manual_check": True}
    opener = build_opener(SafeRedirect(allowed_hosts))
    req = Request(url, headers={"User-Agent": "ScholarshipIntelligence/0.1 (public academic source monitor)"})
    with opener.open(req, timeout=12) as response:
        data = response.read(2_000_001)
        if len(data) > 2_000_000:
            return {"url": url, "status": "TOO_LARGE", "requires_manual_check": True}
        kind = response.headers.get("Content-Type", "").split(";")[0].lower()
        digest = hashlib.sha256(data).hexdigest()
        title = ""
        if "html" in kind:
            raw = data.decode("utf-8", errors="replace")
            match = re.search(r"<title[^>]*>(.*?)</title>", raw, re.I | re.S)
            if match:
                title = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", match.group(1))).strip()[:150]
    return {"url": url, "status": "FETCHED", "sha256": digest,
            "content_type": kind, "page_title": title,
            "checked_at_utc": datetime.now(timezone.utc).isoformat(),
            "requires_manual_check": True}


def public_grok_review(item: dict, model: str | None = None) -> str:
    """Send ONLY public opportunity metadata to xAI; optional proprietary provider."""
    key = os.environ.get("XAI_API_KEY")
    if not key:
        raise RuntimeError("XAI_API_KEY ausente — nenhum dado foi transmitido")
    from urllib.request import urlopen
    payload = {
        "model": model or os.environ.get("XAI_MODEL", "grok-4.7"),
        "messages": [
            {"role": "system", "content":
             "Analise exclusivamente os metadados públicos. Não infira elegibilidade, "
             "datas ou bolsa sem edital primário. Liste lacunas e citações."},
            {"role": "user", "content": json.dumps({
                k: item.get(k) for k in (
                    "title", "official_url", "deadline", "application_actor",
                    "topics", "notes", "evidence_date")}, ensure_ascii=False)},
        ],
    }
    req = Request("https://api.x.ai/v1/chat/completions",
                  data=json.dumps(payload).encode("utf-8"),
                  headers={"Authorization": f"Bearer {key}",
                           "Content-Type": "application/json"},
                  method="POST")
    with urlopen(req, timeout=40) as response:
        result = json.load(response)
    return result["choices"][0]["message"]["content"]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Scholarship Intelligence — triagem auditável")
    parser.add_argument("--registry", default=str(Path(__file__).with_name("sources.json")))
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate")
    rank_p = sub.add_parser("rank")
    rank_p.add_argument("--profile", required=True, help="arquivo LOCAL, não versionado")
    rank_p.add_argument("--today", default=date.today().isoformat())
    scan_p = sub.add_parser("scan")
    scan_p.add_argument("--id", required=True)
    ai_p = sub.add_parser("grok-public")
    ai_p.add_argument("--id", required=True)
    args = parser.parse_args(argv)
    registry = read_json(args.registry)
    hosts = registry["allowed_hosts"]
    items = registry["opportunities"]
    for item in items:
        validate_record(item, hosts)
    if args.command == "validate":
        print(f"OK: {len(items)} registros, allowlist de {len(hosts)} domínios.")
    elif args.command == "rank":
        profile = read_json(args.profile)
        rows = [rank(item, profile, date.fromisoformat(args.today)) for item in items]
        print(json.dumps(sorted(rows, key=lambda row: -row["score"]),
                         indent=2, ensure_ascii=False))
    else:
        matching = [x for x in items if x["id"] == args.id]
        if not matching:
            parser.error("Identificador não encontrado")
        if args.command == "scan":
            print(json.dumps(scan_source(matching[0]["official_url"], hosts),
                             indent=2, ensure_ascii=False))
        elif args.command == "grok-public":
            print(public_grok_review(matching[0]))


if __name__ == "__main__":
    main()
