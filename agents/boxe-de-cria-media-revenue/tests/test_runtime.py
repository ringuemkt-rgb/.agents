import importlib.util
from pathlib import Path
from decimal import Decimal
import tempfile
import unittest

spec=importlib.util.spec_from_file_location("bdc_media",Path(__file__).resolve().parents[1]/"runtime"/"bdc_media.py")
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

class TestAgent(unittest.TestCase):
    def test_canonical(self):
        self.assertEqual(m.canonical("https://example.org/f?utm_source=x&id=2#bio"),
                         "https://example.org/f?id=2")
        with self.assertRaises(ValueError):m.canonical("http://example.org")
        with self.assertRaises(ValueError):m.canonical("https://user:pass@example.org")
    def test_rss(self):
        xml=b"<rss><channel><item><title>Campeonato de boxe do Brasil</title><link>https://example.org/a</link></item></channel></rss>"
        self.assertEqual(m.parse_feed(xml)[0]["url"],"https://example.org/a")
    def test_atom(self):
        xml=b'<feed xmlns="http://www.w3.org/2005/Atom"><entry><title>Competicao de kickboxing regional</title><link href="https://example.org/b"/></entry></feed>'
        self.assertEqual(len(m.parse_feed(xml)),1)
    def test_xxe(self):
        with self.assertRaises(ValueError):m.parse_feed(b"<!DOCTYPE foo><rss/>")
    def test_financial(self):
        d=m.project(100000,Decimal("0.75"),Decimal("5"),Decimal("350"),3,Decimal("400"))
        self.assertEqual(d["adsense_hypothesis"],"375.00")
        self.assertEqual(d["gross_hypothesis"],"1575.00")
        self.assertEqual(d["after_reported_costs"],"1225.00")
        with self.assertRaises(ValueError):m.project(-1,Decimal("1"),Decimal("5"),Decimal("1"))
    def test_gate_and_audit(self):
        with tempfile.TemporaryDirectory() as tmp:
            with m.connect(str(Path(tmp)/"test.sqlite")) as c:
                u="https://example.org/test"
                cid=m.hashlib.sha256(u.encode()).hexdigest()
                c.execute("INSERT INTO candidates(id,source,title,url,discovered_at) VALUES(?,?,?,?,?)",
                          (cid,"Font","Competicao a confirmar",u,m.utc()))
                self.assertEqual(m.brief(c,cid,"offline")["status"],"needs_review")
                with self.assertRaises(ValueError):m.review(c,cid,"X","https://example.org/oficial","curta",True)
                self.assertEqual(m.review(c,cid,"Editor Jose","https://example.org/oficial",
                      "Confirmei os documentos e escrevi uma analise independente original.",True)["status"],"approved")
                self.assertEqual(c.execute("SELECT COUNT(*) FROM audit").fetchone()[0],2)
    def test_records_separated(self):
        with tempfile.TemporaryDirectory() as tmp:
            with m.connect(str(Path(tmp)/"test.sqlite")) as c:
                c.execute("INSERT INTO fighters(id,display_name) VALUES(?,?)",("f1","Atleta de teste"))
                for id,mode,cls,result,verified in [
                    ("1","boxing","professional","W",1),
                    ("2","boxing","amateur","L",1),
                    ("3","muay_thai","professional","D",1),
                    ("4","boxing","professional","L",0)
                ]:
                    c.execute("INSERT INTO bouts(id,fighter_id,discipline,class,result,evidence_url,verified) VALUES(?,?,?,?,?,?,?)",
                        (id,"f1",mode,cls,result,"https://example.org/evidencia",verified))
                data=m.record(c,"f1")["records"]
                self.assertEqual(data["boxing:professional"]["W"],1)
                self.assertEqual(data["boxing:professional"]["L"],0)
                self.assertEqual(data["boxing:amateur"]["L"],1)
    def test_output_text(self):
        self.assertEqual(m.response_text({"output":[{"content":[{"type":"output_text","text":"ok"}]}]}),"ok")

if __name__=="__main__":unittest.main()
