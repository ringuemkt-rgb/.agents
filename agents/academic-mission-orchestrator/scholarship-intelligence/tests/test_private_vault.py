import sys
from pathlib import Path
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import private_vault as v

class VaultTests(unittest.TestCase):
    def test_encrypt_decrypt_and_no_plaintext(self):
        msg=b"Documento privado de teste, nao real"
        pw="frase-de-teste-robusta-1234"
        blob=v.seal_bytes(msg,pw)
        self.assertNotIn(msg,blob)
        self.assertEqual(v.open_bytes(blob,pw),msg)

    def test_tampering_fails(self):
        pw="frase-de-teste-robusta-1234"
        blob=bytearray(v.seal_bytes(b"documento",pw))
        blob[-1] ^= 1
        with self.assertRaises(Exception):
            v.open_bytes(bytes(blob),pw)

    def test_short_password_rejected(self):
        with self.assertRaises(ValueError):
            v.seal_bytes(b"test", "1234")

    def test_exclusive_write_refuses_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            target=str(Path(tmp)/"private"/"vault.bin")
            v.write_exclusive(target,b"encrypted")
            with self.assertRaises(FileExistsError):
                v.write_exclusive(target,b"override")
            self.assertEqual(Path(target).read_bytes(),b"encrypted")

    def test_reject_repo_destination(self):
        with self.assertRaises(ValueError):
            v.safe_destination(str(ROOT/"confidential.json"))

if __name__=="__main__":
    unittest.main()
