import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class ManualReferenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT/"config"/"apparel.reference-manual.json").read_text(encoding="utf-8"))
        cls.tokens = json.loads((ROOT/"config"/"brand.tokens.json").read_text(encoding="utf-8"))
    def test_ten_sources_manifest(self):
        self.assertEqual(len(self.data["user_supplied_files"]),10)
        self.assertEqual(len(set(x["id"] for x in self.data["user_supplied_files"])),10)
    def test_sha256_form_and_dimensions(self):
        for x in self.data["user_supplied_files"]:
            self.assertRegex(x["sha256"],r"^[a-f0-9]{64}$")
            self.assertEqual(len(x["dimensions_px"]),2)
            self.assertTrue(all(v>0 for v in x["dimensions_px"]))
    def test_no_images_published(self):
        self.assertTrue(all(not x["original_bytes_in_public_repo"] for x in self.data["user_supplied_files"]))
    def test_pallettes_unapproved(self):
        self.assertEqual(len(self.data["palette_alternatives"]),2)
        self.assertTrue(all(x["status"]=="PENDENTE_HOMOLOGACAO" for x in self.data["palette_alternatives"]))
        self.assertEqual(self.tokens["colors"]["gold"],"#C9A24E")
    def test_two_textile_routes_not_merged(self):
        self.assertEqual({x["process"] for x in self.data["garment_routes"]},
                         {"sublimacao_total","serigrafia"})
        self.assertTrue(all(x["status"]=="EXEMPLO_NAO_VALIDADO" for x in self.data["garment_routes"]))
    def test_logo_versions_not_assumed_official(self):
        self.assertTrue(all(x["status"].endswith("PENDENTE") for x in self.data["logo_lockups"]))
    def test_print_locked(self):
        self.assertTrue(self.data["print_status"].startswith("BLOCKED"))
if __name__=="__main__":
    unittest.main()
