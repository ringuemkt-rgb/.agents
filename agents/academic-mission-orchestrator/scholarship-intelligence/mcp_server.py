"""Read-only MCP server for the scholarship intelligence public registry.

Requires MCP Python SDK v2. Exposes no password, private data, browser execution,
form submission, payment, arbitrary URL fetch or shell tool to LLM clients.
Launch locally using: mcp dev mcp_server.py
"""
from __future__ import annotations
from datetime import date
import json
import os
from pathlib import Path

from mcp.server import MCPServer
from scholarship_agent import read_json, rank, validate_record
from permission_guard import decision

mcp = MCPServer("Scholarship Intelligence (public and read-only)")
CATALOG = Path(__file__).with_name("sources.json")


def registry():
    data=read_json(CATALOG)
    for item in data["opportunities"]:
        validate_record(item, data["allowed_hosts"])
    return data


@mcp.tool()
def list_public_opportunities() -> list[dict]:
    """List public, dated opportunities. No claims of submission or actual scholarship."""
    return [{
        "id":x["id"],"title":x["title"],"institution":x.get("institution"),
        "status":x["status"],"deadline":x.get("deadline"),
        "application_actor":x["application_actor"],
        "source":x["official_url"],"reviewed":x.get("evidence_date")
    } for x in registry()["opportunities"]]


@mcp.tool()
def triage_public(interests: list[str], preferred_states: list[str],
                  today: str) -> list[dict]:
    """Estimate operational relevance only, not admission or scholarship probability."""
    if len(interests)>12 or len(preferred_states)>10:
        raise ValueError("Limite de filtros excedido")
    day=date.fromisoformat(today)
    profile={"interests":interests,"preferred_states":preferred_states}
    return sorted((rank(x,profile,day) for x in registry()["opportunities"]),
                  key=lambda x: -x["score"])


@mcp.tool()
def policy_for_action(action: str, url: str) -> str:
    """Return capability policy for the requested official action and site."""
    return decision(action,url,registry()["allowed_hosts"])


@mcp.tool()
def public_source_status() -> dict:
    """Check registry shape without triggering a network request."""
    data=registry()
    return {"registry_reviewed":data.get("reviewed_on"),
            "opportunity_count":len(data["opportunities"]),
            "watch_count":len(data["watch_urls"]),
            "note":"A data do registro não comprova que um prazo permanece aberto."}


@mcp.tool()
def grok_review_public_opportunity(opportunity_id: str) -> str:
    """Optional billed xAI review of PUBLIC metadata only; opt-in required."""
    if os.environ.get("SCHOLARSHIP_ALLOW_PAID_ANALYSIS") != "1":
        raise PermissionError("Integração paga desativada por padrão")
    from llm_gateway import grok_public_review
    data=registry()
    found=next((x for x in data["opportunities"] if x["id"]==opportunity_id),None)
    if found is None:
        raise ValueError("Oportunidade não cadastrada")
    return grok_public_review(found)
