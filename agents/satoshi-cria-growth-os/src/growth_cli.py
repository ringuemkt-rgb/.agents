#!/usr/bin/env python3
"""CRIA Growth OS: deterministic read-only CLI (Python standard library)."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def facts() -> dict:
    return json.loads((ROOT / "public_facts.json").read_text(encoding="utf-8"))


def validate_brief(brief: dict) -> dict:
    data = facts()
    errors: list[str] = []
    warnings: list[str] = []
    if not isinstance(brief, dict):
        return {"valid": False, "errors": ["brief must be a JSON object"], "warnings": []}
    class_id = brief.get("class_id")
    match = next((item for item in data["classes"] if item["id"] == class_id), None)
    if match is None:
        errors.append("Unknown or unconfirmed class_id")
    else:
        if brief.get("academy") != match["academy"]:
            errors.append("Academy does not match the confirmed class")
        if brief.get("start_time") != match["start_time"]:
            errors.append("Start time does not match the confirmed class")
        if brief.get("weekdays_iso") != match["weekday_iso"]:
            errors.append("Weekdays do not match the confirmed class")
    trainer = str(brief.get("trainer", ""))
    if trainer != data["professional_title"]:
        errors.append("The publication must identify 'Treinador Satoshi Nishiuchi'")
    copy = " ".join(str(brief.get(k, "")) for k in ("headline", "body", "cta"))
    if re.search(r"\bprofessor\s+satoshi\b", copy, flags=re.IGNORECASE):
        errors.append("Use Treinador, never Professor Satoshi")
    if not str(brief.get("headline", "")).strip():
        errors.append("Missing headline")
    if not str(brief.get("cta", "")).strip():
        errors.append("Missing CTA")
    if brief.get("redraw_official_logo") is True:
        errors.append("Official logos must not be redrawn")
    if brief.get("recreate_faces") is True:
        errors.append("Original facial features must not be reconstructed")
    for claim in ("vagas limitadas", "aula grátis", "grátis", "desconto", "100%", "garantido"):
        if claim in copy.lower() and claim not in brief.get("verified_claims", []):
            warnings.append("Review unverified promise: " + claim)
    if brief.get("price") is not None:
        warnings.append("Confirm price in private authorized source; public dataset intentionally omits it")
    return {"valid": not errors and not warnings, "errors": errors, "warnings": warnings, "class_id": class_id}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="CRIA Growth OS public tools")
    parser.add_argument("action", choices=["facts", "validate", "health", "manifest"])
    parser.add_argument("--input", type=Path, help="JSON brief path for validate")
    args = parser.parse_args(argv)
    if args.action == "facts":
        result = facts()
    elif args.action == "manifest":
        result = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    elif args.action == "health":
        result = {"status": "ok", "mode": "local_read_only", "classes": len(facts()["classes"])}
    else:
        if args.input is None:
            parser.error("validate requires --input")
        try:
            value = json.loads(args.input.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            print(json.dumps({"valid": False, "errors": [str(e)]}, ensure_ascii=False))
            return 2
        result = validate_brief(value)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("valid", True) else 2


if __name__ == "__main__":
    sys.exit(main())
