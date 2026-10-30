import sys
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import permission_guard as p

HOSTS=["portal.universidade.edu.br"]
URL="https://portal.universidade.edu.br/inscricao"

class PolicyTests(unittest.TestCase):
    def test_public_reads_are_automatic(self):
        self.assertEqual(p.decision("public.fetch",URL,HOSTS),"ALLOW_AUTONOMOUS")

    def test_submit_requires_single_use(self):
        self.assertEqual(p.decision("portal.submit",URL,HOSTS),"REQUIRE_ONE_TIME_APPROVAL")

    def test_authentication_never_delegated(self):
        for action in ("auth.password","auth.2fa","auth.biometric","captcha.solve"):
            self.assertEqual(p.decision(action,URL,HOSTS),"HUMAN_ONLY")

    def test_lookalikes_and_unknown_tools_denied(self):
        self.assertEqual(p.decision("portal.submit","https://portal.universidade.edu.br.evil.test/",HOSTS),"DENY_HOST")
        self.assertEqual(p.decision("shell.execute",URL,HOSTS),"DENY_UNRECOGNIZED")

    def test_approval_single_use_and_scope_locked(self):
        with tempfile.TemporaryDirectory() as tmp:
            ledger=p.ApprovalLedger(str(Path(tmp)/"auth.sqlite3"))
            try:
                with patch.object(sys.stdin,"isatty",return_value=True),patch("builtins.input",return_value="AUTORIZO portal.submit"):
                    token=ledger.issue_interactively("portal.submit",URL,HOSTS,artifact_sha256="a"*64)
                self.assertFalse(ledger.consume(token,"portal.submit",URL,HOSTS,artifact_sha256="b"*64))
                self.assertTrue(ledger.consume(token,"portal.submit",URL,HOSTS,artifact_sha256="a"*64))
                self.assertFalse(ledger.consume(token,"portal.submit",URL,HOSTS,artifact_sha256="a"*64))
            finally:
                ledger.close()

    def test_no_approval_from_noninteractive_bot(self):
        with tempfile.TemporaryDirectory() as tmp:
            ledger=p.ApprovalLedger(str(Path(tmp)/"auth.sqlite3"))
            try:
                with patch.object(sys.stdin,"isatty",return_value=False):
                    with self.assertRaises(PermissionError):
                        ledger.issue_interactively("portal.submit",URL,HOSTS)
            finally:
                ledger.close()

if __name__=="__main__":
    unittest.main()
