"""Unit tests for brand canon, safety gates, and editable graphic templates."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"runtime"))
from visual_qa import check_tokens, check_presets, check_asset_registry, contrast_ratio
from template_gen import render_template

class BrandCanonTests(unittest.TestCase):
    def test_canonical_tokens_and_wcag(self):
        result=check_tokens()
        self.assertTrue(result["ok"])
        self.assertGreaterEqual(result["paper_on_ink_contrast"],4.5)
        self.assertGreaterEqual(result["gold_on_ink_contrast"],4.5)
    def test_all_seven_presets(self):
        self.assertEqual(check_presets()["presets"],7)
    def test_reject_changed_brand_token(self):
        with tempfile.TemporaryDirectory() as tmp:
            data=json.loads((ROOT/"config"/"brand.tokens.json").read_text())
            data["colors"]["gold"]="#111111"
            f=Path(tmp)/"colors.json";f.write_text(json.dumps(data))
            with self.assertRaises(ValueError):check_tokens(f)
    def test_reject_contrast_hazard(self):
        self.assertLess(contrast_ratio("#111111","#101010"),4.5)
    def test_no_official_asset_assumed(self):
        self.assertEqual(check_asset_registry(ROOT/"config"/"asset-registry.example.json")["assets"],0)
    def test_reject_unauthorized_asset(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/"registry.json"
            path.write_text(json.dumps({"assets":[{"asset_id":"logo",
                  "type":"official_logo","origin":"no permission","rights_status":"unknown",
                  "usage_scope":"site","sha256":"a"*64,"reviewed_by":"editor",
                  "immutable_original":True}]}))
            with self.assertRaises(ValueError):check_asset_registry(path)
    def test_reject_ai_fake_documentary(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/"registry.json"
            path.write_text(json.dumps({"assets":[{"asset_id":"synthetic",
                 "type":"ai_illustration","origin":"model","rights_status":"approved",
                 "usage_scope":"article","sha256":"a"*64,"reviewed_by":"editor"}]}))
            with self.assertRaises(ValueError):check_asset_registry(path)
    def test_original_logo_sha_protection(self):
        with tempfile.TemporaryDirectory() as tmp:
            logo=Path(tmp)/"approved.png";logo.write_bytes(b"test sample, not a real logo")
            digest=hashlib.sha256(logo.read_bytes()).hexdigest()
            entry={"asset_id":"logo","type":"official_logo","origin":"authorized private master",
                   "rights_status":"approved","usage_scope":"site","sha256":digest,
                   "reviewed_by":"editor","immutable_original":True,
                   "local_original_path":str(logo)}
            path=Path(tmp)/"registry.json";path.write_text(json.dumps({"assets":[entry]}))
            self.assertTrue(check_asset_registry(path,strict_files=True)["ok"])
            logo.write_bytes(b"tampered")
            with self.assertRaises(ValueError):check_asset_registry(path,strict_files=True)
    def test_minor_review_required(self):
        with tempfile.TemporaryDirectory() as tmp:
            entry={"asset_id":"photo","type":"licensed_photo","origin":"rights owner",
                   "rights_status":"approved","usage_scope":"site","sha256":"b"*64,
                   "reviewed_by":"editor","identity_and_context_preserved":True,
                   "minor_subject":True}
            path=Path(tmp)/"registry.json";path.write_text(json.dumps({"assets":[entry]}))
            with self.assertRaises(ValueError):check_asset_registry(path)

class TemplateTests(unittest.TestCase):
    def test_svg_is_well_formed_and_placeholder_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/"hero.svg"
            rendered=render_template("news_hero","Uma manchete de exemplo para boxe","BOXE",path)
            self.assertFalse(rendered["publishable"])
            root=ET.fromstring(path.read_text())
            self.assertEqual(root.attrib["width"],"1600")
            self.assertIn("LOGO ORIGINAL AQUI",path.read_text())
            metadata=json.loads(path.with_suffix(".manifest.json").read_text())
            self.assertEqual(metadata["state"],"template_not_publishable")
            self.assertEqual(metadata["photo"],"not_included")
    def test_xml_escaping(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/"social.svg"
            render_template("social_portrait","Boxe & disciplina <treino>","ARTE",path)
            ET.parse(path)
            self.assertIn("Boxe &amp; disciplina &lt;treino&gt;",path.read_text())
    def test_reject_too_long_title(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                render_template("news_hero","palavra "*20,"BOXE",Path(tmp)/"bad.svg")
    def test_reject_unknown_preset(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                render_template("broken","Uma manchete relevante","BOXE",Path(tmp)/"bad.svg")

if __name__=="__main__":
    unittest.main()
