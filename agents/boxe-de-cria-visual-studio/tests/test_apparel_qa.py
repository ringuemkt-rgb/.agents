import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "runtime" / "apparel_qa.py"
spec = importlib.util.spec_from_file_location("apparel_qa", PATH)
mod = importlib.util.module_from_spec(spec)
sys.modules["apparel_qa"] = mod
spec.loader.exec_module(mod)

class ApparelTests(unittest.TestCase):
    def setUp(self):
        self.sample = json.loads((ROOT / "examples" / "student_training_tee.json").read_text(encoding="utf-8"))
    def test_concept_passes_with_warnings(self):
        result = mod.check(self.sample)
        self.assertTrue(result["ok"])
        self.assertEqual(result["status"], "CONCEPT_REVIEW")
        self.assertGreater(len(result["warnings"]), 0)
    def test_not_print_ready(self):
        self.assertFalse(mod.check(self.sample, "print")["ok"])
    def test_forbid_redrawn_logo(self):
        self.sample["visual"]["logo_mode"] = "ai_generated_approximation"
        self.assertFalse(mod.check(self.sample)["ok"])
    def test_forbid_other_brand_without_consent(self):
        self.sample["third_party_brands"] = ["FIT BOX"]
        self.assertFalse(mod.check(self.sample)["ok"])
    def test_allow_approved_partner(self):
        self.sample["third_party_brands"] = ["FIT BOX"]
        self.sample["third_party_approvals"] = ["FIT BOX"]
        self.assertTrue(mod.check(self.sample)["ok"])
    def test_forbid_unsupported_claims(self):
        self.sample["claims"] = ["antiodor", "prevents all injuries"]
        self.assertFalse(mod.check(self.sample)["ok"])
    def test_reject_bad_color(self):
        self.sample["visual"]["base_color"] = "neonpink"
        self.assertFalse(mod.check(self.sample)["ok"])
    def test_sublimation_requires_polyester(self):
        self.sample["manufacturing"]["printing_method"] = "sublimacao_total"
        self.sample["manufacturing"]["fabric_composition"] = "algodão"
        self.assertFalse(mod.check(self.sample)["ok"])
    def test_fits_existing_palette(self):
        palette = json.loads((ROOT/"config"/"brand.tokens.json").read_text(encoding="utf-8"))
        self.assertEqual(palette["colors"]["ink"], "#0B0B0B")
    def test_no_real_customer_info_or_artwork(self):
        self.assertNotIn("@", json.dumps(self.sample))
        self.assertEqual(self.sample["visual"]["logo_master"]["status"], "pendente")

if __name__ == "__main__":
    unittest.main()
