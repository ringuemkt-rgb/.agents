import importlib.util
from pathlib import Path
from decimal import Decimal
import tempfile
import unittest
ROOT=Path(__file__).resolve().parents[1]/"runtime"
def mod(name):
    spec=importlib.util.spec_from_file_location(name,ROOT/(name+".py"))
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
ads=mod("adsense_report")
crm=mod("commercial")
class TestMonetization(unittest.TestCase):
    def test_adsense_requires_oauth(self):
        with self.assertRaises(ValueError):ads.report("bad-account","temporary-access-token")
        with self.assertRaises(ValueError):ads.report("accounts/123","")
        with self.assertRaises(ValueError):ads.report("accounts/123","temporary-access-token","NONSENSE")
    def test_crm_values_not_revenue(self):
        with tempfile.TemporaryDirectory() as tmp:
            with crm.connect(str(Path(tmp)/"sales.sqlite")) as c:
                r=crm.update(c,"L001","Academia Teste","Sponsorship","400","proposal")
                self.assertEqual(r["stage"],"proposal")
                self.assertEqual(crm.summary(c)["amounts_brl_by_stage"]["proposal"],"400")
                self.assertEqual(crm.summary(c)["amounts_brl_by_stage"]["paid"],"0")
                crm.update(c,"L001","Academia Teste","Sponsorship","400","contracted")
                self.assertEqual(crm.summary(c)["amounts_brl_by_stage"]["proposal"],"0")
                self.assertEqual(crm.summary(c)["counts"]["contracted"],1)
                self.assertEqual(c.execute("SELECT COUNT(*) FROM opportunity_history").fetchone()[0],2)
    def test_crm_negative_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            with crm.connect(str(Path(tmp)/"sales.sqlite")) as c:
                with self.assertRaises(ValueError):crm.update(c,"A","Test","Sponsor","-1","lead")
if __name__=="__main__":unittest.main()
