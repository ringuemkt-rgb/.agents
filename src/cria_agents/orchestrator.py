from __future__ import annotations

from collections import defaultdict, deque
from typing import Any

from .models import ConfigurationError, ExecutionPlan, Workflow, WorkflowStep


def order_workflow(workflow: Workflow) -> list[WorkflowStep]:
    """Return workflow steps in dependency order and reject cycles."""

    steps = {step.id: step for step in workflow.steps}
    indegree = {step.id: 0 for step in workflow.steps}
    dependents: dict[str, list[str]] = defaultdict(list)

    for step in workflow.steps:
        for dependency in step.needs:
            if dependency not in steps:
                raise ConfigurationError(
                    f"Workflow {workflow.id}: step {step.id} needs unknown step {dependency}"
                )
            indegree[step.id] += 1
            dependents[dependency].append(step.id)

    ready = deque(step.id for step in workflow.steps if indegree[step.id] == 0)
    ordered: list[WorkflowStep] = []

    while ready:
        step_id = ready.popleft()
        ordered.append(steps[step_id])
        for dependent in dependents[step_id]:
            indegree[dependent] -= 1
            if indegree[dependent] == 0:
                ready.append(dependent)

    if len(ordered) != len(workflow.steps):
        unresolved = [step_id for step_id, degree in indegree.items() if degree > 0]
        raise ConfigurationError(
            f"Workflow {workflow.id} contains a dependency cycle: {unresolved}"
        )

    return ordered


def build_plan(workflow: Workflow, context: dict[str, Any] | None = None) -> ExecutionPlan:
    return ExecutionPlan(
        workflow=workflow,
        ordered_steps=order_workflow(workflow),
        context=context or {},
    )
