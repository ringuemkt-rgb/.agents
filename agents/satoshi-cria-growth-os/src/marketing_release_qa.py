#!/usr/bin/env python3
"""Prepublication QA for CRIA sports marketing creative briefs (offline, stdlib)."""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
FORMATS={"story":(1080,1920),"feed_portrait":(1080,1350),"square":(1080,1080)}
SUPPORTED_BRANDS={"FIT BOX","CTRK","BOXE DE CRIA","CB PRISCO TEAM","FISIOBOXE"}
FORMAL_TITLE="Treinador Satoshi Nishiuchi"
HIGH_RISK={"vagas_limitadas":["vagas limitadas","últimas vagas","ultimas vagas","poucas vagas"],
           "gratuidade":["grátis","gratis","gratuita","gratuito","sem custo"],
           "resultado":["resultado garantido","garantimos resultados","100% garantido"],
           "urgencia":["garanta sua vaga","reserve sua vaga","última chance","ultima chance"]}
def public_facts():
    return json.loads((ROOT/"public_facts.json").read_text(encoding="utf-8"))
def _has_verified_sha(asset):
    return bool(re.fullmatch(r"[a-f0-9]{64}", str((asset or {}).get("source_sha256") or "")))
def validate(brief,gate="draft"):
    errors=[];warnings=[];checks=[]
    if gate not in ("draft","publish"):
        raise ValueError("gate must be draft|publish")
    if not isinstance(brief,dict):
        return {"ok":False,"status":"BLOCKED","errors":["brief must be object"],"warnings":[]}
    brand=brief.get("brand")
    if brand not in SUPPORTED_BRANDS:errors.append("Brand is not a registered editorial context")
    copy=" ".join(str(brief.get(k) or "") for k in ("headline","body","cta","subtitle","footer"))
    lower=copy.lower()
    if re.search(r"\b(?:professor|professora|prof\.?)\s+satoshi\b",lower):
        errors.append("Incorrect coach title: use Treinador Satoshi Nishiuchi, never Prof./Professor")
    if brief.get("coach") and brief["coach"]!=FORMAL_TITLE and ("satoshi" in brief["coach"].lower()):
        errors.append("Wrong official professional title for Satoshi")
    if "satoshi" in lower and not re.search(r"treinador\s+satoshi\s+nishiuchi",lower):
        errors.append("Satoshi must be identified as Treinador Satoshi Nishiuchi")
    if brand=="FIT BOX" and re.search(r"\bfitbox\b",lower):
        errors.append("Academy spelling: FIT BOX, not FITBOX")
    if not str(brief.get("headline") or "").strip():errors.append("Missing headline")
    if not str(brief.get("cta") or "").strip():errors.append("Missing action CTA")
    channel=brief.get("cta_channel")
    if channel not in ("direct","whatsapp","reception","none"):
        errors.append("Must define one supported CTA channel")
    if channel=="direct" and not re.search(r"\bdirect\b",str(brief.get("cta") or ""),re.I):
        errors.append("Direct CTA must explicitly identify the Direct channel")
    if channel=="direct" and brand in {"FIT BOX","CTRK"} and brand.lower() not in str(brief.get("cta") or "").lower():
        errors.append("Direct CTA must name the account owner/academy")
    if channel=="whatsapp" and not re.search(r"whats\s?app|whatsapp",str(brief.get("cta") or ""),re.I):
        errors.append("WhatsApp CTA must identify WhatsApp")
    frame=brief.get("format")
    if frame not in FORMATS:errors.append("Unknown format")
    elif [brief.get("width"),brief.get("height")] != list(FORMATS[frame]):
        errors.append("Dimension mismatch for format "+frame)
    isclass=brief.get("campaign_type")=="class_signup"
    if isclass:
        entry=next((x for x in public_facts()["classes"] if x["id"]==brief.get("class_id")),None)
        if not entry:errors.append("Class not in publicly confirmed schedule")
        else:
            if entry["academy"]!=brand:errors.append("Venue does not match confirmed class")
            if entry["start_time"]!=brief.get("start_time"):errors.append("Class time does not match confirmed start")
            if entry["weekday_iso"]!=brief.get("weekdays_iso"):errors.append("Class weekdays are not confirmed")
            if brief.get("end_time") is not None and entry.get("end_time") is None:
                errors.append("Public end time has never been confirmed")
    if brief.get("price") is not None and brief.get("price_verified") is not True:
        errors.append("Public price lacks a confirmed source and explicit approval")
    verified=set(brief.get("verified_claims") or [])
    for claim,phrases in HIGH_RISK.items():
        if claim not in verified and any(s in lower for s in phrases):
            errors.append("Unverified marketing promise: "+claim)
    if re.search(r"(cura|previne todas? lesões|sem risco|garante proteção)",lower):
        errors.append("Unsupported absolute clinical/safety promise")
    assets=brief.get("assets") or {}
    logo=assets.get("logo") or {}
    photo=assets.get("photo") or {}
    if logo.get("mode") in {"generated","redrawn","stylized","reconstructed"}:
        errors.append("Logo must not be AI-redrawn, recreated or stylized")
    if photo.get("mode") in {"generated_fake_documentary","face_reconstruction","body_reconstruction"}:
        errors.append("Real photo must preserve identity and documentary context")
    if brief.get("contains_identifiable_minor") and not brief.get("minor_use_authorized"):
        errors.append("Images of identifiable minors require documented authorization")
    if brief.get("contains_private_leads") or brief.get("contains_unconsented_testimonial"):
        errors.append("No private leads or unconsented testimonial in publishable creative")
    if gate=="publish":
        if not logo.get("present") or logo.get("mode")!="original_overlay" or not _has_verified_sha(logo):
            errors.append("Publish gate needs official logo original overlaid with verified SHA-256")
        if not logo.get("owner_permission") or not logo.get("manual_visual_checked"):
            errors.append("Publish gate needs brand permission and human logo visual check")
        if photo.get("present"):
            if photo.get("mode")!="original_overlay" or not _has_verified_sha(photo) or not photo.get("manual_visual_checked"):
                errors.append("Publish gate needs original photograph provenance and visual check")
        if not brief.get("manual_text_checked"):
            errors.append("Publish gate requires human readable-text verification on final rendered image")
        if not brief.get("manual_layout_checked"):
            errors.append("Publish gate requires human crop, spacing and legibility inspection")
        if not brief.get("human_publication_approval"):
            errors.append("Publication requires explicit human approval")
    else:
        if logo.get("present") and not _has_verified_sha(logo):
            warnings.append("Draft only: original logo has not been byte-verified")
        if photo.get("present") and not _has_verified_sha(photo):
            warnings.append("Draft only: photograph source has not been byte-verified")
        warnings.append("Draft preflight does not inspect actual pixels/text in a rendered image")
    result={"ok":not errors, "status": "BLOCKED" if errors else
            ("APPROVAL_RECORDED_NOT_POSTED" if gate=="publish" else "DRAFT_REQUIRES_VISUAL_REVIEW"),
            "gate":gate, "errors":errors, "warnings":warnings,
            "manual_visual_required":True,"publication_performed":False}
    return result

def main(argv=None):
    p=argparse.ArgumentParser()
    p.add_argument("--input",required=True,type=Path)
    p.add_argument("--gate",choices=["draft","publish"],default="draft")
    args=p.parse_args(argv)
    b=json.loads(args.input.read_text(encoding="utf-8"))
    result=validate(b,args.gate)
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 0 if result["ok"] else 2
if __name__=="__main__":sys.exit(main())
