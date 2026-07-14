from __future__ import annotations

import json
import subprocess
from pathlib import Path

from .models import ConfigurationError, ToolSource


class ToolSyncError(RuntimeError):
    pass


def _run(args: list[str], cwd: Path | None = None) -> str:
    result = subprocess.run(
        args,
        cwd=cwd,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        command = " ".join(args)
        raise ToolSyncError(
            f"Command failed ({result.returncode}): {command}\n{result.stderr.strip()}"
        )
    return result.stdout.strip()


def _validate_tool(tool: ToolSource, root: Path) -> None:
    if not tool.repository.startswith("https://github.com/") or not tool.repository.endswith(".git"):
        raise ConfigurationError(
            f"Tool {tool.id} must use an explicit HTTPS GitHub .git URL"
        )
    vendor_root = (root / ".vendor").resolve()
    destination = tool.destination.resolve()
    if vendor_root not in destination.parents:
        raise ConfigurationError(
            f"Tool {tool.id} destination must be inside {vendor_root}: {destination}"
        )


def sync_tool(tool: ToolSource, root: Path) -> dict[str, str]:
    _validate_tool(tool, root)
    tool.destination.parent.mkdir(parents=True, exist_ok=True)

    if not (tool.destination / ".git").is_dir():
        _run(
            [
                "git",
                "clone",
                "--filter=blob:none",
                "--no-checkout",
                tool.repository,
                str(tool.destination),
            ]
        )
    else:
        current_origin = _run(
            ["git", "remote", "get-url", "origin"], cwd=tool.destination
        )
        if current_origin != tool.repository:
            raise ToolSyncError(
                f"Tool {tool.id} origin mismatch: {current_origin} != {tool.repository}"
            )

    _run(["git", "fetch", "--depth", "1", "origin", tool.ref], cwd=tool.destination)
    _run(["git", "checkout", "--detach", "FETCH_HEAD"], cwd=tool.destination)
    sha = _run(["git", "rev-parse", "HEAD"], cwd=tool.destination)

    return {
        "id": tool.id,
        "repository": tool.repository,
        "requested_ref": tool.ref,
        "resolved_sha": sha,
        "destination": str(tool.destination.relative_to(root)),
    }


def sync_tools(tools: dict[str, ToolSource], root: Path) -> list[dict[str, str]]:
    lock_entries = [
        sync_tool(tool, root)
        for tool in tools.values()
        if tool.enabled
    ]
    lock_path = root / "config" / "tools.lock.json"
    lock_path.write_text(
        json.dumps({"schema_version": 1, "tools": lock_entries}, indent=2) + "\n",
        encoding="utf-8",
    )
    return lock_entries
