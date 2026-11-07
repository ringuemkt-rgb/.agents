#!/usr/bin/env bash
# Setup opcional para uma máquina própria; nunca é executado na CI.
set -euo pipefail
if [[ "${CRIA_ENABLE_MODEL_DOWNLOAD:-NO}" != "YES" ]]; then
  echo 'Somente instruções. Para instalar os pesos localmente, defina CRIA_ENABLE_MODEL_DOWNLOAD=YES.'
  echo 'Ollama: https://ollama.com  /  modelo: ollama pull qwen3.5:4b'
  echo 'BGE-M3: python -m pip install sentence-transformers; o primeiro --embed-local baixa o modelo.'
  exit 0
fi
if ! command -v ollama >/dev/null 2>&1; then
  echo 'Ollama ausente. Instale manualmente em https://ollama.com e repita.' >&2
  exit 2
fi
ollama pull qwen3.5:4b
python -m pip show sentence-transformers >/dev/null || {
  echo 'BGE-M3 requer a dependência opcional sentence-transformers. Instale manualmente.' >&2
  exit 3
}
python - <<'PY'
from sentence_transformers import SentenceTransformer
model=SentenceTransformer('BAAI/bge-m3', trust_remote_code=False)
vector=model.encode(['O boxe trabalha movimentos técnicos.'], normalize_embeddings=True)
print('Teste real do BGE-M3: forma=',vector.shape)
PY
python -m cria_multi_ai model-status
