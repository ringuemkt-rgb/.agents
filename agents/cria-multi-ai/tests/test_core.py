import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from cria_multi_ai.core import Memory, chunks, cosine, health, respond


class MultiAiTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.mem = Memory(str(Path(self.temp.name) / 'test.sqlite'))

    def tearDown(self):
        self.mem.close()
        self.temp.cleanup()

    def test_chunk_boundary_and_overlap(self):
        self.assertEqual(chunks('abcdef', size=4, overlap=1), ['abcd', 'def'])
        self.assertEqual(chunks(''), [])
        with self.assertRaises(ValueError):
            chunks('abc', size=2, overlap=2)

    def test_lexical_memory_and_source(self):
        self.mem.add('Boxe ensina disciplina e técnica.', 'publico.md')
        self.mem.add('Caderno de receitas culinárias.', 'cozinha.md')
        hits = self.mem.search('disciplina boxe')
        self.assertEqual(hits[0]['source'], 'publico.md')
        self.assertTrue(hits[0]['id'])

    def test_unicode_portuguese_and_dedupe(self):
        self.mem.add('Inclusão de crianças em projetos sociais.', 'abc.md')
        self.mem.add('Inclusão de crianças em projetos sociais.', 'abc.md')
        self.assertEqual(len(self.mem.search('inclusão')), 1)

    def test_file_restrictions(self):
        path = Path(self.temp.name) / 'private.pdf'
        path.write_text('private')
        with self.assertRaises(ValueError):
            self.mem.add_file(str(path))

    def test_embedding_ranking(self):
        self.mem.add('Lutas são atividade física.', 'luta.md', embed=lambda _: [1.0, 0.0])
        self.mem.add('Documento de outro tema.', 'outro.md', embed=lambda _: [0.0, 1.0])
        hits = self.mem.search('pergunta sem termo indexado', embed=lambda _: [1.0, 0.0])
        self.assertEqual(hits[0]['source'], 'luta.md')
        self.assertEqual(hits[0]['embedding_model'], 'BAAI/bge-m3')

    def test_empty_vectors(self):
        self.assertEqual(cosine([1], [1, 2]), 0.0)
        self.assertEqual(cosine([0.0], [1.0]), 0.0)

    def test_offline_refuses_to_invent(self):
        reply = respond('Qual o resultado?', [], provider='none')
        self.assertEqual(reply['status'], 'retrieval_only')
        self.assertIsNone(reply['answer'])

    def test_hf_requires_explicit_opt_in(self):
        with patch.dict(os.environ, {'CRIA_ENABLE_HF_INFERENCE': 'NO', 'HF_TOKEN': 'dummy'}):
            with self.assertRaises(PermissionError):
                respond('Oi', [], provider='hf')

    def test_hf_calls_correct_adapter_with_mock(self):
        with patch.dict(os.environ, {'CRIA_ENABLE_HF_INFERENCE': 'YES', 'HF_TOKEN': 'test-token'}):
            with patch('cria_multi_ai.core.request_json', return_value={'choices': [{'message': {'content': 'ok'}}]}) as mocked:
                result = respond('Pergunta', [{'id': 'abc', 'source': 'a.md', 'content': 'Evidência'}], 'hf')
        self.assertEqual(result['answer'], 'ok')
        self.assertEqual(result['model'], 'Qwen/Qwen3.5-4B')
        self.assertIn('router.huggingface.co', mocked.call_args.args[0])

    def test_health_has_zero_billed_calls(self):
        self.assertEqual(health()['status'], 'pass')
        self.assertEqual(health()['billed_calls'], 0)


if __name__ == '__main__':
    unittest.main()
