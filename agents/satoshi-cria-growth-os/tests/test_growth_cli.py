import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("growth_cli", ROOT / "src" / "growth_cli.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class GrowthTests(unittest.TestCase):
    def setUp(self):
        self.brief = json.loads((ROOT / "examples" / "brief.json").read_text(encoding="utf-8"))

    def test_two_confirmed_classes(self):
        self.assertEqual(len(mod.facts()["classes"]), 2)

    def test_valid_brief(self):
        self.assertTrue(mod.validate_brief(self.brief)["valid"])

    def test_wrong_hour(self):
        self.brief["start_time"] = "18:30"
        self.assertFalse(mod.validate_brief(self.brief)["valid"])

    def test_professor_not_allowed(self):
        self.brief["trainer"] = "Professor Satoshi"
        self.assertFalse(mod.validate_brief(self.brief)["valid"])

    def test_logo_and_face_guards(self):
        self.brief["redraw_official_logo"] = True
        self.brief["recreate_faces"] = True
        result = mod.validate_brief(self.brief)
        self.assertFalse(result["valid"])
        self.assertEqual(len(result["errors"]), 2)

    def test_unverified_claim_warns(self):
        self.brief["cta"] = "Vagas limitadas. Aula grátis!"
        self.assertFalse(mod.validate_brief(self.brief)["valid"])

    def test_crm_not_present(self):
        self.assertFalse(list(ROOT.rglob("*.sqlite")))
        self.assertFalse(list(ROOT.rglob("*.xlsx")))


if __name__ == "__main__":
    unittest.main()
