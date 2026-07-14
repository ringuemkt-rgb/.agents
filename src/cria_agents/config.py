from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .models import Agent, ConfigurationError, ToolSource, Workflow, WorkflowStep


DEFAULT_ROOT = Path(__file__).resolve().parents[2]


def _read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ConfigurationError(f"Missing configuration file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ConfigurationError(f"Invalid JSON in {path}: {exc}") from exc


def load_agents(root: Path = DEFAULT_ROOT) -> dict[str, Agent]:
    payload = _read_json(root / "config" / "agents.json")
    agents: dict[str, Agent] = {}
    for raw in payload.get("agents", []):
        agent = Agent(
            id=raw["id"],
            name=raw["name"],
            role=raw["role"],
            instructions=root / raw["instructions"],
            capabilities=tuple(raw.get("capabilities", [])),
            forbidden=tuple(raw.get("forbidden", [])),
            requires=tuple(raw.get("requires", [])),
        )
        if agent.id in agents:
            raise ConfigurationError(f"Duplicate agent id: {agent.id}")
        if not agent.instructions.is_file():
            raise ConfigurationError(
                f"Agent {agent.id} points to missing instructions: {agent.instructions}"
            )
        agents[agent.id] = agent

    for agent in agents.values():
        missing = [dependency for dependency in agent.requires if dependency not in agents]
        if missing:
            raise ConfigurationError(f"Agent {agent.id} requires unknown agents: {missing}")
    return agents


def load_workflows(root: Path = DEFAULT_ROOT) -> dict[str, Workflow]:
    payload = _read_json(root / "config" / "workflows.json")
    workflows: dict[str, Workflow] = {}
    for raw in payload.get("workflows", []):
        steps = tuple(
            WorkflowStep(
                id=step["id"],
                agent=step["agent"],
                needs=tuple(step.get("needs", [])),
                deliverables=tuple(step.get("deliverables", [])),
            )
            for step in raw.get("steps", [])
        )
        workflow = Workflow(
            id=raw["id"],
            description=raw["description"],
            steps=steps,
        )
        if workflow.id in workflows:
            raise ConfigurationError(f"Duplicate workflow id: {workflow.id}")
        workflows[workflow.id] = workflow
    return workflows


def load_tools(root: Path = DEFAULT_ROOT) -> dict[str, ToolSource]:
    payload = _read_json(root / "config" / "tools.json")
    tools: dict[str, ToolSource] = {}
    for raw in payload.get("tools", []):
        tool = ToolSource(
            id=raw["id"],
            repository=raw["repository"],
            ref=raw.get("ref", "main"),
            destination=root / raw["destination"],
            install_commands=tuple(raw.get("install_commands", [])),
            enabled=raw.get("enabled", True),
        )
        if tool.id in tools:
            raise ConfigurationError(f"Duplicate tool id: {tool.id}")
        tools[tool.id] = tool
    return tools


def validate_all(root: Path = DEFAULT_ROOT) -> tuple[dict[str, Agent], dict[str, Workflow], dict[str, ToolSource]]:
    agents = load_agents(root)
    workflows = load_workflows(root)
    tools = load_tools(root)

    for workflow in workflows.values():
        step_ids = {step.id for step in workflow.steps}
        if len(step_ids) != len(workflow.steps):
            raise ConfigurationError(f"Workflow {workflow.id} contains duplicate step ids")
        for step in workflow.steps:
            if step.agent not in agents:
                raise ConfigurationError(
                    f"Workflow {workflow.id} step {step.id} uses unknown agent {step.agent}"
                )
            unknown_needs = [need for need in step.needs if need not in step_ids]
            if unknown_needs:
                raise ConfigurationError(
                    f"Workflow {workflow.id} step {step.id} needs unknown steps {unknown_needs}"
                )

    return agents, workflows, tools
