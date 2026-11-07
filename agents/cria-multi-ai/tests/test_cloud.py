import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from cria_multi_ai.core import Memory, model_status
from cria_multi_ai.cloud import snapshot, restore, keygen, drive_upload, drive_list, drive_download


class CloudMemoryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Path(self.tmp.name) / 'memory.sqlite'
        self.backup = Path(self.tmp.name) / 'snapshot.enc'
        self.mem = Memory(str(self.db))
        self.mem.add('Boxe e inclusão social: exemplo sintético de teste.', 'demo-publica.md')
        self.mem.close()

    def tearDown(self):
        self.tmp.cleanup()

    def test_requires_encryption_key(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaises(PermissionError):
                snapshot(self.db, self.backup)

    def test_roundtrip_encrypted_and_source(self):
        k = keygen()
        with patch.dict(os.environ, {'CRIA_MEMORY_ENCRYPTION_KEY': k}):
            result = snapshot(self.db, self.backup)
            self.assertEqual(result['chunks'], 1)
            self.assertNotIn(b'Boxe', self.backup.read_bytes())
            restored = Path(self.tmp.name) / 'new.sqlite'
            self.assertEqual(restore(restored, self.backup)['restored'], 1)
            self.assertEqual(restore(restored, self.backup)['already_present'], 1)
            m = Memory(str(restored))
            self.assertEqual(m.search('inclusão')[0]['source'], 'demo-publica.md')
            m.close()

    def test_wrong_key_refuses(self):
        with patch.dict(os.environ, {'CRIA_MEMORY_ENCRYPTION_KEY': keygen()}):
            snapshot(self.db, self.backup)
        with patch.dict(os.environ, {'CRIA_MEMORY_ENCRYPTION_KEY': keygen()}):
            with self.assertRaises(ValueError):
                restore(Path(self.tmp.name) / 'bad.sqlite', self.backup)

    def test_backups_cannot_be_overwritten(self):
        with patch.dict(os.environ, {'CRIA_MEMORY_ENCRYPTION_KEY': keygen()}):
            snapshot(self.db, self.backup)
            with self.assertRaises(FileExistsError):
                snapshot(self.db, self.backup)

    def test_drive_upload_off_by_default(self):
        self.backup.write_bytes(b'not-a-real-secret')
        with patch.dict(os.environ, {'CRIA_ENABLE_DRIVE_SYNC':'NO'}):
            with self.assertRaises(PermissionError):
                drive_upload(self.backup, '123456', 'dummy')

    def test_drive_upload_with_explicit_optin(self):
        k = keygen()
        with patch.dict(os.environ, {'CRIA_MEMORY_ENCRYPTION_KEY':k}):
            snapshot(self.db, self.backup)
        with patch.dict(os.environ, {'CRIA_ENABLE_DRIVE_SYNC':'YES', 'CRIA_MEMORY_ENCRYPTION_KEY':k}):
            with patch('cria_multi_ai.cloud._request', return_value={'id':'remote42','name':'snapshot.enc'}) as x:
                out = drive_upload(self.backup, 'folder_id', 'token')
                self.assertTrue(out['uploaded'])
                self.assertIn(self.backup.read_bytes(), x.call_args.args[3])

    def test_drive_listing(self):
        with patch('cria_multi_ai.cloud._request', return_value={'files':[{'id':'abc', 'name':'snapshot.enc'}]}) as x:
            out = drive_list('folderid', 'token')
        self.assertEqual(out[0]['name'], 'snapshot.enc')
        self.assertIn('folderid', x.call_args.args[0])

    def test_model_status_does_not_call_remote_inference(self):
        with patch('urllib.request.urlopen', side_effect=OSError('not installed')) as mocked:
            result = model_status()
        self.assertFalse(result['ollama']['server'])
        self.assertEqual(result['billed_calls'], 0)
        self.assertFalse(result['all_models_running'])
        self.assertEqual(mocked.call_count, 1)

    def test_invalid_drive_identifiers(self):
        with self.assertRaises(ValueError):
            drive_list('invalid id!', 'token')
        with self.assertRaises(ValueError):
            drive_download('bad?', 'token', self.backup)

if __name__ == '__main__':
    unittest.main()
