#!/usr/bin/env python3
"""Deterministic apparel concept & print-release QA, no external dependencies."""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_PRODUCTS = {"camiseta", "regata", "rashguard", "short", "polo", "jaqueta"}
ALLOWED_AUDIENCE = {"alunos", "treinadores", "premium", "competicao"}
PRINT_METHODS = {"a_confirmar", "dtf", "serigrafia", "sublimacao_total", "bordado", "dtg"}

def check(spec: dict, gate="concept") -> dict:
    errors, warnings = [], []
    if not isinstance(spec, dict):
        return {"ok": False, "errors": ["Spec must be an object"], "warnings": [], "gate": gate}
    tokens = json.loads((ROOT / "config" / "brand.tokens.json").read_text(encoding="utf-8"))
    keys = set(tokens["colors"])
    if spec.get("brand") != "BOXE DE CRIA":
        errors.append("Brand must match BOXE DE CRIA")
    if spec.get("audience") not in ALLOWED_AUDIENCE:
        errors.append("Invalid audience")
    if spec.get("product") not in ALLOWED_PRODUCTS:
        errors.append("Invalid product")
    visual = spec.get("visual") or {}
    if visual.get("logo_mode") != "original_unmodified":
        errors.append("The logo must be the original unmodified asset")
    if visual.get("base_color") not in keys:
        errors.append("Unknown canonical base color")
    if any(c not in keys for c in visual.get("accent_colors", [])):
        errors.append("Unknown canonical accent color")
    if spec.get("third_party_brands"):
        allowed = set(spec.get("third_party_approvals") or [])
        missing = set(spec["third_party_brands"]) - allowed
        if missing:
            errors.append("Third-party branding without explicit approval: " + ", ".join(sorted(missing)))
    if spec.get("claims"):
        errors.append("Marketing claims require separate evidence approval: do not put in manufacturing spec")
    manufacture = spec.get("manufacturing") or {}
    method = manufacture.get("printing_method")
    if method not in PRINT_METHODS:
        errors.append("Unknown printing process")
    if method == "sublimacao_total":
        textile = (manufacture.get("fabric_composition") or "").lower()
        if "poli" not in textile:
            errors.append("Sublimation on fabric requires verified compatible polyester textile")
    master = visual.get("logo_master") or {}
    if gate == "print":
        if not master.get("approved_for_use"):
            errors.append("Original logo is not approved for production")
        if master.get("status") != "verificado" or not re.fullmatch(r"[a-f0-9]{64}", str(master.get("sha256") or "")):
            errors.append("Missing verified SHA-256 for original master file")
        for k in ("fabric_composition", "fabric_gsm", "supplier"):
            if not manufacture.get(k):
                errors.append(f"Production requires {k}")
        if method == "a_confirmar":
            errors.append("Supplier must confirm print method")
        for k in ("color_proof_approved", "size_chart_approved", "physical_sample_approved"):
            if manufacture.get(k) is not True:
                errors.append(f"Production approval missing: {k}")
        if spec.get("status") != "PRODUCAO_AUTORIZADA":
            errors.append("Production gate requires authorized status")
    else:
        if master.get("status") != "verificado":
            warnings.append("CONCEPT ONLY: logo master pending approval")
        if method == "a_confirmar":
            warnings.append("CONCEPT ONLY: print method and fabric pending supplier")
    return {"ok": not errors, "gate": gate, "errors": errors, "warnings": warnings, "status": "READY_TO_PRINT" if gate=="print" and not errors else ("CONCEPT_REVIEW" if not errors else "BLOCKED")}

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", type=Path, required=True)
    p.add_argument("--gate", choices=["concept", "print"], default="concept")
    p.add_argument("--output", type=Path)
    args = p.parse_args()
    try:
        spec = json.loads(args.input.read_text(encoding="utf-8"))
        result = check(spec, args.gate)
    except (OSError, ValueError) as exc:
        result = {"ok": False, "errors": [str(exc)], "warnings": []}
    encoded = json.dumps(result, ensure_ascii=False, indent=2)
    print(encoded)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded + "\n", encoding="utf-8")
    return 0 if result["ok"] else 2

if __name__ == "__main__":
    sys.exit(main())
