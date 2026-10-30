#!/usr/bin/env python3
"""Auditor determinístico de documentos e baremas declarados a partir de edital oficial.

Uma avaliação automática não valida a autenticidade do comprovante. A coluna
'human_verified' é uma declaração local de revisão, não uma verificação técnica.
"""
from __future__ import annotations
import argparse
from decimal import Decimal, InvalidOperation
import json
from pathlib import Path
from urllib.parse import urlsplit

def valid_source(url, hosts):
    parsed = urlsplit(url or "")
    return (parsed.scheme == "https"
            and (parsed.hostname or "").lower() in {h.lower() for h in hosts}
            and not parsed.username and not parsed.password and parsed.port in (None,443))

def compute_barema(rules, evidence, official_hosts):
    seen = set()
    total = Decimal("0")
    rows = []
    for rule in rules:
        rid = str(rule["id"])
        if rid in seen:
            raise ValueError("Regra duplicada: " + rid)
        seen.add(rid)
        if not valid_source(rule.get("official_source_url"), official_hosts):
            raise ValueError("Regra sem fonte oficial permitida: " + rid)
        try:
            rate = Decimal(str(rule["points_per_unit"]))
            ceiling = Decimal(str(rule["cap_points"]))
        except (InvalidOperation, KeyError):
            raise ValueError("Pontos inválidos: " + rid)
        if not rate.is_finite() or not ceiling.is_finite() or rate < 0 or ceiling < 0:
            raise ValueError("Pontos negativos ou infinitos não são permitidos")
        proof = evidence.get(rid, {})
        units = proof.get("units", 0)
        if not isinstance(units,int) or isinstance(units,bool) or units < 0:
            raise ValueError("Quantidade inválida: " + rid)
        approved = proof.get("human_verified") is True
        documented = bool(str(proof.get("local_proof_reference","")).strip())
        counted = min(rate * units, ceiling) if (approved and documented) else Decimal("0")
        total += counted
        rows.append({
            "id": rid, "points": str(counted), "max": str(ceiling),
            "units": units, "status": ("PROVA_DECLARADA_E_REVISADA"
                         if approved and documented else "PENDENTE_COMPROVANTE"),
            "official_source_url": rule["official_source_url"],
            "warning": "Validação do colegiado/da banca ainda é necessária"
        })
    return {"declared_defensible_points":str(total),
            "warning":"SIMULAÇÃO LOCAL; NÃO equivale à pontuação homologada do edital.",
            "items":rows}

def check_documents(requirements, evidence, official_hosts):
    report=[]
    for requirement in requirements:
        if not valid_source(requirement.get("official_source_url"), official_hosts):
            raise ValueError("Documento sem origem oficial")
        rid=requirement["id"]
        proof=evidence.get(rid, {})
        ok = proof.get("human_verified") is True and bool(
            str(proof.get("local_proof_reference","")).strip())
        report.append({"id":rid,"mandatory":bool(requirement.get("mandatory",True)),
                       "status":"CONFERIDO_LOCALMENTE" if ok else "PENDENTE",
                       "official_source_url":requirement["official_source_url"]})
    return {"documents":report,"blocking_missing":[r["id"] for r in report
                    if r["mandatory"] and r["status"]=="PENDENTE"]}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--rules",required=True,help="JSON de critérios extraídos e revisados do edital")
    parser.add_argument("--evidence",required=True,help="JSON PRIVADO de evidências, não versionado")
    args=parser.parse_args()
    public=json.loads(Path(args.rules).read_text(encoding="utf-8"))
    private=json.loads(Path(args.evidence).read_text(encoding="utf-8"))
    hosts=public["official_hosts"]
    result={"barema":compute_barema(public.get("barema_rules",[]),
                                      private.get("barema",{}),hosts),
            "documents":check_documents(public.get("documents",[]),
                                      private.get("documents",{}),hosts)}
    print(json.dumps(result,indent=2,ensure_ascii=False))

if __name__=="__main__":
    main()
