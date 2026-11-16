import copy
import importlib.util
import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/"src"/"marketing_release_qa.py"
spec=importlib.util.spec_from_file_location("marketing_release_qa",SRC)
mod=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=mod
spec.loader.exec_module(mod)

class CampaignQATests(unittest.TestCase):
    def setUp(self):
        self.b=json.loads((ROOT/"examples"/"fitbox_story_campaign.json").read_text(encoding="utf-8"))
    def test_valid_draft(self):
        x=mod.validate(self.b)
        self.assertTrue(x["ok"])
        self.assertEqual(x["status"],"DRAFT_REQUIRES_VISUAL_REVIEW")
    def test_wrong_title_prohibited(self):
        self.b["body"]="Aulas com Prof. Satoshi Nishiuchi."
        self.assertFalse(mod.validate(self.b)["ok"])
    def test_wrong_brand_spelling(self):
        self.b["body"]="Aulas na FITBOX"
        self.assertFalse(mod.validate(self.b)["ok"])
    def test_wrong_schedule(self):
        self.b["start_time"]="18:30"
        self.assertFalse(mod.validate(self.b)["ok"])
    def test_unconfirmed_end_time(self):
        self.b["end_time"]="06:40"
        self.assertFalse(mod.validate(self.b)["ok"])
    def test_unsupported_free_trial(self):
        self.b["body"]="Aula experimental grátis"
        self.assertFalse(mod.validate(self.b)["ok"])
    def test_false_scarcity(self):
        self.b["cta"]="Garanta sua vaga pelo Direct da FIT BOX"
        self.assertFalse(mod.validate(self.b)["ok"])
    def test_story_dimensions(self):
        self.b["width"]=1080; self.b["height"]=1350
        self.assertFalse(mod.validate(self.b)["ok"])
    def test_wrong_venue(self):
        self.b["brand"]="CTRK"
        self.assertFalse(mod.validate(self.b)["ok"])
    def test_no_dubious_logo(self):
        self.b["assets"]["logo"]["mode"]="redrawn"
        self.assertFalse(mod.validate(self.b)["ok"])
    def test_no_face_reconstruction(self):
        self.b["assets"]["photo"]["mode"]="face_reconstruction"
        self.assertFalse(mod.validate(self.b)["ok"])
    def test_no_publishing_without_original(self):
        self.assertFalse(mod.validate(self.b,gate="publish")["ok"])
    def test_no_autopost_even_with_manual_approval(self):
        self.b["assets"]["logo"].update({"source_sha256":"a"*64,"owner_permission":True,
                                           "manual_visual_checked":True})
        self.b["assets"]["photo"].update({"source_sha256":"b"*64,"manual_visual_checked":True})
        self.b["manual_text_checked"]=True
        self.b["manual_layout_checked"]=True
        self.b["human_publication_approval"]=True
        result=mod.validate(self.b,gate="publish")
        self.assertTrue(result["ok"])
        self.assertFalse(result["publication_performed"])
    def test_minors_protected(self):
        self.b["contains_identifiable_minor"]=True
        self.assertFalse(mod.validate(self.b)["ok"])
    def test_unverified_price(self):
        self.b["price"]=120
        self.assertFalse(mod.validate(self.b)["ok"])
    def test_wrong_coach(self):
        self.b["coach"]="Prof. Satoshi Nishiuchi"
        self.assertFalse(mod.validate(self.b)["ok"])
    def test_private_leads_guard(self):
        self.b["contains_private_leads"]=True
        self.assertFalse(mod.validate(self.b)["ok"])
if __name__=="__main__":unittest.main()
