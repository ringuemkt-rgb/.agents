import importlib.util
from pathlib import Path
import unittest

path=Path(__file__).resolve().parents[1]/"application_auditor.py"
spec=importlib.util.spec_from_file_location("application_auditor",path)
a=importlib.util.module_from_spec(spec)
spec.loader.exec_module(a)

class BaremaTests(unittest.TestCase):
    def setUp(self):
        self.rules=[{"id":"exp","points_per_unit":15,"cap_points":30,
                     "official_source_url":"https://pos.uel.br/pef/editais/"}]
        self.hosts=["pos.uel.br"]

    def test_no_proof_no_score(self):
        r=a.compute_barema(self.rules,{"exp":{"units":2,"human_verified":True}},self.hosts)
        self.assertEqual(r["declared_defensible_points"],"0")

    def test_human_review_and_cap(self):
        r=a.compute_barema(self.rules,{"exp":{"units":5,"human_verified":True,
                        "local_proof_reference":"arquivo-local"}},self.hosts)
        self.assertEqual(r["declared_defensible_points"],"30")

    def test_reject_fake_official_domain(self):
        r=[{**self.rules[0],"official_source_url":"https://pos.uel.br.evil.test/"}]
        with self.assertRaises(ValueError):
            a.compute_barema(r,{},self.hosts)

    def test_reject_negative_units(self):
        with self.assertRaises(ValueError):
            a.compute_barema(self.rules,{"exp":{"units":-1}},self.hosts)

    def test_mandatory_documents(self):
        requirements=[{"id":"diploma","mandatory":True,
                        "official_source_url":"https://pos.uel.br/pef/editais/"}]
        r=a.check_documents(requirements,{},self.hosts)
        self.assertEqual(r["blocking_missing"],["diploma"])

if __name__=="__main__":
    unittest.main()
