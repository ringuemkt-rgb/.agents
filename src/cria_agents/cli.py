from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .config import DEFAULT_ROOT, load_tools, validate_all
from .models import ConfigurationError
from .orchestrator import build_plan
from .tools import ToolSyncError, sync_tools


def _json_context(raw: str | None) -> dict[str, object]:
    if not raw:
        return {}
    value = json.loads(raw)
    if not isinstance(value, dict):
        raise ValueError("--context must contain a JSON object")
    return value


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="cria-agents",
        description="Validate and plan work with the Cria Agent Hub.",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=DEFAULT_ROOT,
        help="Agent Hub root directory.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("validate", help="Validate all registries and workflows.")
    subparsers.add_parser("list", help="List registered agents and workflows.")

    plan = subparsers.add_parser("plan", help="Build a dependency-ordered execution plan.")
    plan.add_argument("workflow", help="Workflow id from config/workflows.json")
    plan.add_argument("--context", help="Optional JSON object passed to the plan.")

    tools = subparsers.add_parser("tools", help="Manage external tool integrations.")
    tools_subparsers = tools.add_subparsers(dest="tools_command", required=True)
    tools_subparsers.add_parser("list", help="List configured tools.")
    tools_subparsers.add_parser("sync", help="Clone/update enabled tools and write a lock file.")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    root = args.root.resolve()

    try:
        if args.command == "validate":
            agents, workflows, tools = validate_all(root)
            print(
                f"Valid hub: {len(agents)} agents, {len(workflows)} workflows, "
                f"{len(tools)} tools."
            )
            return 0

        if args.command == "list":
            agents, workflows, _ = validate_all(root)
            print("Agents:")
            for agent in agents.values():
                print(f"- {agent.id}: {agent.name} — {agent.role}")
            print("\nWorkflows:")
            for workflow in workflows.values():
                print(f"- {workflow.id}: {workflow.description}")
            return 0

        if args.command == "plan":
            _, workflows, _ = validate_all(root)
            try:
                workflow = workflows[args.workflow]
            except KeyError as exc:
                raise ConfigurationError(f"Unknown workflow: {args.workflow}") from exc
            plan = build_plan(workflow, _json_context(args.context))
            print(json.dumps(plan.as_dict(), indent=2, ensure_ascii=False))
            return 0

        if args.command == "tools":
            tools = load_tools(root)
            if args.tools_command == "list":
                for tool in tools.values():
                    state = "enabled" if tool.enabled else "disabled"
                    print(f"- {tool.id}: {tool.repository}@{tool.ref} [{state}]")
                return 0
            if args.tools_command == "sync":
                entries = sync_tools(tools, root)
                print(json.dumps({"synced": entries}, indent=2))
                return 0

        parser.error("unsupported command")
        return 2
    except (ConfigurationError, ToolSyncError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
