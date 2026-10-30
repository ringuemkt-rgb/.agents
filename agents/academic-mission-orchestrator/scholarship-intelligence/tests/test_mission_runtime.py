import sys
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import mission_runtime as m

REGISTRY={
    "allowed_hosts":["example.edu.br"],
    "watch_urls":[{"label":"Bolsas edital","url":"https://example.edu.br/edital"}],
    "opportunities":[{"id":"mestrado-x","official_url":"https://example.edu.br/mestrado"}],
}

class QueueTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.db=Path(self.tmp.name)/"private"/"jobs.sqlite3"
        self.q=m.MissionQueue(str(self.db))

    def tearDown(self):
        self.q.close()
        self.tmp.cleanup()

    def test_idempotency_and_public_only(self):
        self.assertTrue(self.q.enqueue("job-x","PUBLIC_SCAN","mestrado-x",now=1000))
        self.assertFalse(self.q.enqueue("job-x","PUBLIC_SCAN","mestrado-x",now=1000))
        with self.assertRaises(PermissionError):
            self.q.enqueue("untrusted","PORTAL_SUBMIT","mestrado-x",now=1000)
        with self.assertRaises(ValueError):
            self.q.enqueue("cpf 123.456","PUBLIC_SCAN","mestrado-x",now=1000)

    def test_claim_and_resume_after_stale_lease(self):
        self.q.enqueue("job-y","PUBLIC_SCAN","mestrado-x",now=1000)
        job=self.q.claim(now=1000,lease_seconds=10)
        self.assertEqual(job["state"],"RUNNING")
        self.assertIsNone(self.q.claim(now=1005,lease_seconds=10))
        again=self.q.claim(now=1011,lease_seconds=10)
        self.assertEqual(again["attempts"],2)
        self.q.complete("job-y",{"status":"FETCHED","secret":"NEVER","sha256":"abc"},now=1012)
        self.assertEqual(self.q.get("job-y")["state"],"DONE")
        self.assertNotIn("NEVER",self.q.get("job-y")["result_json"])

    def test_retry_budget_and_manual_stop(self):
        self.q.enqueue("job-z","PUBLIC_DISCOVER","watch-000",now=2000,max_attempts=2)
        self.q.claim(now=2000)
        self.q.fail("job-z","TRANSIENT",now=2000)
        self.assertEqual(self.q.get("job-z")["state"],"RETRY")
        self.assertIsNone(self.q.claim(now=2014))
        self.q.claim(now=2015)
        self.q.fail("job-z","TRANSIENT",now=2015)
        self.assertEqual(self.q.get("job-z")["state"],"DEAD_LETTER")

    def test_no_network_stub_and_unknown_source(self):
        self.q.enqueue("job-ok","PUBLIC_DISCOVER","watch-000",now=1000)
        calls=[]
        def stub(action,url,hosts):
            calls.append((action,url))
            return {"status":"DISCOVERED_LEADS","leads":[{"url":url}]}
        result=m.process_one(self.q,REGISTRY,fetcher=stub,now=1000)
        self.assertEqual(result["state"],"DONE")
        self.assertEqual(self.q.summary()["DONE"],1)
        self.assertEqual(len(calls),1)
        self.q.enqueue("job-bad","PUBLIC_SCAN","unknown",now=1000)
        result=m.process_one(self.q,REGISTRY,fetcher=stub,now=1000)
        self.assertEqual(result["state"],"WAITING_HUMAN")
        self.assertEqual(len(calls),1)

    def test_login_or_captcha_never_retried(self):
        self.q.enqueue("job-auth","PUBLIC_SCAN","watch-000",now=1000)
        self.q.claim(now=1000)
        self.q.fail("job-auth","CAPTCHA",now=1000)
        self.assertEqual(self.q.get("job-auth")["state"],"WAITING_HUMAN")
        self.assertIsNone(self.q.claim(now=99999))

if __name__=="__main__":
    unittest.main()
