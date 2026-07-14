import unittest
from pathlib import Path

from cria_agents.config import validate_all


class RegistryTests(unittest.TestCase):
    def test_repository_configuration_is_valid(self) -> None:
        root = Path(__file__).resolve().parents[1]
        agents, workflows, tools = validate_all(root)

        self.assertGreaterEqual(len(agents), 8)
        self.assertIn("build-game", workflows)
        self.assertIn("agent-sprite-forge", tools)


if __name__ == "__main__":
    unittest.main()
