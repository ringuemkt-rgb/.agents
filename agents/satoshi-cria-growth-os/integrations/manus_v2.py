#!/usr/bin/env python3
"""Manus v2 opt-in task client. No network or cost unless --send is used."""
from __future__ import annotations
import argparse
import json
import os
from urllib import request

REPO = "https://github.com/ringuemkt-rgb/.agents/tree/main/agents/satoshi-cria-growth-os"
ENDPOINT = "https://api.manus.ai/v2/task.create"


def make_payload():
    return {"message": {"content": (
        "Consulte o agente público CRIA Growth OS em " + REPO + ". "
        "Leia AGENT.md, SYSTEM_PROMPT.md, public_facts.json e PRIVACY.md. "
        "Produza uma proposta de campanha de Boxe em Guarapari sem dados privados, "
        "sem publicar em redes sociais ou fazer gastos. Cite fatos e pendências."
    )}}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--send", action="store_true",
                        help="Requires MANUS_API_KEY and explicit approval; may incur charges")
    args = parser.parse_args()
    payload = make_payload()
    if not args.send:
        print(json.dumps({"mode": "dry-run", "endpoint": ENDPOINT,
                          "payload": payload}, ensure_ascii=False, indent=2))
        return
    key = os.getenv("MANUS_API_KEY")
    if not key:
        parser.error("MANUS_API_KEY is required; secrets must stay outside Git")
    data = json.dumps(payload).encode("utf-8")
    req = request.Request(ENDPOINT, data=data,
        headers={"Content-Type": "application/json", "x-manus-api-key": key}, method="POST")
    with request.urlopen(req, timeout=30) as response:
        print(response.read().decode("utf-8"))


if __name__ == "__main__":
    main()
