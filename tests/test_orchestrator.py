import unittest

from cria_agents.models import ConfigurationError, Workflow, WorkflowStep
from cria_agents.orchestrator import order_workflow


class WorkflowOrderingTests(unittest.TestCase):
    def test_orders_dependencies_before_dependents(self) -> None:
        workflow = Workflow(
            id="example",
            description="example",
            steps=(
                WorkflowStep(id="release", agent="qa", needs=("build",)),
                WorkflowStep(id="audit", agent="repo"),
                WorkflowStep(id="build", agent="game", needs=("audit",)),
            ),
        )

        ordered = [step.id for step in order_workflow(workflow)]
        self.assertEqual(ordered, ["audit", "build", "release"])

    def test_rejects_cycle(self) -> None:
        workflow = Workflow(
            id="cycle",
            description="cycle",
            steps=(
                WorkflowStep(id="a", agent="one", needs=("b",)),
                WorkflowStep(id="b", agent="two", needs=("a",)),
            ),
        )

        with self.assertRaises(ConfigurationError):
            order_workflow(workflow)


if __name__ == "__main__":
    unittest.main()
