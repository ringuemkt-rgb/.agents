from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


class ConfigurationError(ValueError):
    """Raised when a registry or workflow violates the hub contract."""


@dataclass(frozen=True, slots=True)
class Agent:
    id: str
    name: str
    role: str
    instructions: Path
    capabilities: tuple[str, ...] = ()
    forbidden: tuple[str, ...] = ()
    requires: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class WorkflowStep:
    id: str
    agent: str
    needs: tuple[str, ...] = ()
    deliverables: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class Workflow:
    id: str
    description: str
    steps: tuple[WorkflowStep, ...]


@dataclass(frozen=True, slots=True)
class ToolSource:
    id: str
    repository: str
    ref: str
    destination: Path
    install_commands: tuple[str, ...] = ()
    enabled: bool = True


@dataclass(slots=True)
class ExecutionPlan:
    workflow: Workflow
    ordered_steps: list[WorkflowStep]
    context: dict[str, Any] = field(default_factory=dict)

    def as_dict(self) -> dict[str, Any]:
        return {
            "workflow": self.workflow.id,
            "description": self.workflow.description,
            "context": self.context,
            "steps": [
                {
                    "id": step.id,
                    "agent": step.agent,
                    "needs": list(step.needs),
                    "deliverables": list(step.deliverables),
                }
                for step in self.ordered_steps
            ],
        }
