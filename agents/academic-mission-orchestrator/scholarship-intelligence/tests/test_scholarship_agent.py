import importlib.util
from datetime import date
from pathlib import Path
import unittest

MODULE_PATH = Path(__file__).resolve().parents[1] / "scholarship_agent.py"
spec = importlib.util.spec_from_file_location("scholarship_agent", MODULE_PATH)
agent = importlib.util.module_from_spec(spec)
spec.loader.exec_module(agent)

class ScholarshipTests(unittest.TestCase):
    def setUp(self):
        self.item = {"id":"a","title":"Mestrado","official_url":"https://www.uesb.br/",
                     "status":"VERIFIED_OFFICIAL","application_actor":"candidate",
                     "evidence_date":"2026-10-15","deadline":"2026-11-02",
                     "topics":["educação física"],"state":"BA"}
        self.hosts = ["www.uesb.br"]

    def test_url_allowlist_rejects_http_and_lookalikes(self):
        for u in ("http://www.uesb.br/", "https://www.uesb.br.evil.test/",
                  "https://www.uesb.br:8080/", "https://user@www.uesb.br/"):
            self.assertFalse(agent.official_url(u,self.hosts))
        self.assertTrue(agent.official_url(self.item["official_url"],self.hosts))

    def test_verified_requires_date(self):
        broken = dict(self.item)
        broken.pop("evidence_date")
        with self.assertRaises(ValueError):
            agent.validate_record(broken, self.hosts)

    def test_expired_is_never_top_rank(self):
        row = agent.rank(self.item,{"interests":["educação física"],"preferred_states":["BA"]},date(2026,11,3))
        self.assertEqual(row["status"],"PRAZO_ENCERRADO")
        self.assertEqual(row["score"],0)

    def test_funding_notice_not_direct_application(self):
        row = agent.rank({**self.item,"application_actor":"program"},
                         {"interests":["educação física"]},date(2026,10,30))
        self.assertTrue(any("institucional" in s for s in row["reasons"]))

    def test_link_collector_rejects_non_official_targets(self):
        from urllib.parse import urljoin
        parser = agent.LinkCollector()
        parser.feed('<a href="/editais/bolsas">Bolsas</a><a href="https://evil.test/bolsa">Bolsa falsa</a>')
        urls = [urljoin(self.item["official_url"], href) for href, label in parser.links
                if "bolsa" in (label + href).lower()]
        allowed = [u for u in urls if agent.official_url(u, self.hosts)]
        self.assertEqual(allowed, ["https://www.uesb.br/editais/bolsas"])

    def test_requires_human_and_evidence(self):
        with self.assertRaises(PermissionError):
            agent.transition("APPLICATION_DRAFT","SUBMITTED_CONFIRMED","receipt-123")
        with self.assertRaises(ValueError):
            agent.transition("APPLICATION_DRAFT","SUBMITTED_CONFIRMED","",approved=True)
        self.assertEqual(agent.transition("APPLICATION_DRAFT","SUBMITTED_CONFIRMED",
                                          "receipt-123",approved=True)["current"],"SUBMITTED_CONFIRMED")
        with self.assertRaises(ValueError):
            agent.transition("VERIFIED_OFFICIAL","PAID","receipt",approved=True)

if __name__ == "__main__":
    unittest.main()
