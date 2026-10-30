import sys
from pathlib import Path
import io
import json
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import llm_gateway as g

RECORD={"id":"edital-1","title":"Edital PPG",
        "official_url":"https://universidade.edu.br/edital",
        "deadline":"2026-11-02","topics":["educação física"],
        "application_actor":"candidate",
        "email":"privado@example.com", "cpf":"123.456.789-00",
        "notes":"NUNCA ENVIAR: dado sensível"}

class DummyResponse:
    def __init__(self,body):
        self.buffer=io.BytesIO(json.dumps(body).encode("utf-8"))
    def __enter__(self): return self
    def __exit__(self,*args): self.buffer.close()
    def read(self,*args): return self.buffer.read(*args)

class GatewayTests(unittest.TestCase):
    def test_private_keys_not_present_in_payload(self):
        sent={}
        def stub(req,timeout):
            sent["body"]=req.data.decode()
            sent["url"]=req.full_url
            return DummyResponse({"output":[{"type":"message",
                     "content":[{"type":"output_text","text":"Itens a verificar"}]}]})
        result=g.grok_public_review(RECORD,opener=stub,api_key="TEST-FAKE")
        self.assertEqual(result,"Itens a verificar")
        self.assertEqual(sent["url"],g.ENDPOINT)
        self.assertNotIn("123.456.789-00",sent["body"])
        self.assertNotIn("privado@example.com",sent["body"])
        self.assertNotIn("NUNCA ENVIAR",sent["body"])
        self.assertNotIn("TEST-FAKE",sent["body"])
        self.assertNotIn("tools",sent["body"])
        self.assertIn("instructions",sent["body"])

    def test_reject_pii_in_whitelisted_field(self):
        with self.assertRaises(PermissionError):
            g.public_metadata({**RECORD,"title":"CPF 123.456.789-00"})

    def test_missing_key_does_not_call_network(self):
        def blocked(*a,**kw):
            self.fail("network called")
        with patch.dict("os.environ",{},clear=True):
            with self.assertRaises(RuntimeError):
                g.grok_public_review(RECORD,opener=blocked)

    def test_empty_reply_is_not_success(self):
        with self.assertRaises(ValueError):
            g.extract_text({"output":[]})

if __name__=="__main__":
    unittest.main()
