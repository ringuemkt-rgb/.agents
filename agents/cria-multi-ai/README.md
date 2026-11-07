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

## Armazenamento persistente em nuvem (Google Drive, opcional)

Em 2026-11-07 foi criada uma pasta privada do usuário no Google Drive:
[CRIA Multi-AI - Memoria Privada](https://drive.google.com/drive/folders/1NUb7z_YK3ZBd6fKTOWXm-oVZ1t95fQgR).
O arquivo de demonstração `cria-multi-ai-DEMO-2026-11-07.enc` foi enviado ao Drive,
baixado e restaurado com sucesso, comparando SHA-256. Contém **apenas dados fictícios**.

**Nenhum token OAuth do conector ChatGPT é repassado para o código.** Para sincronização
programática entre dispositivos, cada máquina precisa de seu próprio token Google Drive
com escopo mínimo de acesso à pasta, e a mesma chave Fernet. Tokens não são incluídos na CI.

### Criar um backup local cifrado

Instale a dependência opcional: `python -m pip install cryptography`.

```bash
cd agents/cria-multi-ai
python -m cria_multi_ai keygen  # Copie a chave somente para um gerenciador de senhas
# Configure CRIA_MEMORY_ENCRYPTION_KEY no seu terminal, sem escrever no repositório.
python -m cria_multi_ai add docs/demo-publica.md
python -m cria_multi_ai snapshot backup-2026-11-07.enc
python -m cria_multi_ai restore backup-2026-11-07.enc --db /tmp/cria-restored.sqlite
```

A chave é indispensável para restaurar os documentos. **Se perdê-la, não há
recuperação do backup.** O exemplo de chave é apenas gerado localmente, nunca gravado
no GitHub ou no Drive. O programa se recusa a sobrescrever backups antigos.

### Sincronização via Google Drive API, somente sob opção explícita

```bash
# Configure GOOGLE_DRIVE_ACCESS_TOKEN de forma privada no dispositivo.
# Use apenas uma pasta própria e sem compartilhamento público.
export CRIA_DRIVE_FOLDER_ID=1NUb7z_YK3ZBd6fKTOWXm-oVZ1t95fQgR
export CRIA_ENABLE_DRIVE_SYNC=YES
python -m cria_multi_ai cloud-upload backup-2026-11-07.enc
python -m cria_multi_ai cloud-list
python -m cria_multi_ai cloud-download 'FILE_ID:download-2026-11-07.enc'
python -m cria_multi_ai restore download-2026-11-07.enc
```

As operações são manuais e explícitas. Nunca há backup remoto automático nem
consumo de API paga na CI. O token deve ser obtido pelo usuário em um fluxo OAuth
aprovado; **não copie tokens MCP ou credenciais de terceiros**. A pasta foi criada
pelo conector Google Drive e é acessível pelo próprio ChatGPT, mas isso não
concede uma sessão OAuth ao script ou ao GitHub Actions.

### Verificação dos modelos e instalação local

```bash
python -m cria_multi_ai model-status
bash scripts/setup-local-models.sh  # modo informativo, SEM downloads
# Em máquina própria, somente se quiser baixar pesos grandes:
CRIA_ENABLE_MODEL_DOWNLOAD=YES bash scripts/setup-local-models.sh
```

A tag `qwen3.5:4b` está publicada no Ollama e ocupa aproximadamente 3,3–4,0 GB
em disco; seu uso precisa de memória RAM adicional. BGE-M3 requer baixar pesos
e instalar `sentence-transformers`. Modelos **não** são instalados, carregados ou
executados automaticamente na CI nem no servidor desta conversa.
