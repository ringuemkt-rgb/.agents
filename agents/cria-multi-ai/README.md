# CRIA Multi-AI Orchestrator · MVP 0.1

Módulo portátil do repositório oficial `ringuemkt-rgb/.agents`. Funciona com Python 3.11+, SQLite FTS5 e **nenhuma dependência obrigatória**. Não cria contas, Jobs pagos, endpoints, campanhas, commits ou deploys automaticamente.

## Executar sem custo

```bash
cd agents/cria-multi-ai
python -m cria_multi_ai health
python -m cria_multi_ai add docs/demo-publica.md
python -m cria_multi_ai search 'boxe inclusão'
python -m cria_multi_ai ask 'O que está documentado sobre inclusão?'
python -m unittest discover -s tests -v
```

A memória fica **fora do Git**, por padrão em `~/.local/share/cria-multi-ai/memory.sqlite`. Nenhuma memória pessoal é publicada no GitHub; há uma demonstração pública sintética. O modo `ask` padrão devolve `retrieval_only` e fontes, **não inventa uma resposta de IA**.

## Executar modelos abertos (opcional)

- **Qwen3.5-4B local:** instale Ollama e o modelo `qwen3.5:4b`; execute `python -m cria_multi_ai ask 'pergunta' --provider ollama`. Ele fala apenas com `127.0.0.1:11434`. Requer recursos locais; o nome/tag precisa existir no seu Ollama.
- **BGE-M3 local:** instale opcionalmente `pip install sentence-transformers` e execute `python -m cria_multi_ai add docs/demo-publica.md --embed-local` e `python -m cria_multi_ai search 'inclusão' --embed-local`. Isso baixa pesos públicos na primeira execução, sem pagar uma API; exige RAM e armazenamento. Índices sem embeddings continuam com FTS5.
- **Qwen3.5-4B na Hugging Face:** configure `HF_TOKEN` em ambiente **privado** com permissão Inference Providers e `CRIA_ENABLE_HF_INFERENCE=YES`, depois `python -m cria_multi_ai ask 'pergunta' --provider hf`. **Não faça isso na execução agendada nem em CI**. A plataforma pode cobrar ou consumir créditos. A configuração padrão nunca chama API paga.

O usuário deve conferir crédito disponível e desativar faturamento adicional antes de optar por inferência remota. `HF_TOKEN` nunca pertence ao repositório. O OAuth de leitura do MCP Hugging Face não é um token reutilizável pelo código.

## Agendamento e aprovação

`.github/workflows/cria-multi-ai.yml` executa testes e smoke test **offline** diariamente às 08:23 UTC, usando runners gratuitos conforme as cotas GitHub aplicáveis, e gera artefato de diagnóstico. Nenhum token ou custo de inferência é usado. O agendamento só passa a funcionar depois de o workflow estar no **branch padrão** (PR ainda não ativa o cron).

Mudanças externas e sensíveis dependem de revisão humana via PR. Os testes usam simuladores somente para verificar contratos de integração; não provam a execução real dos pesos de Qwen/BGE. Ver `docs/ARCHITECTURE.md`.
