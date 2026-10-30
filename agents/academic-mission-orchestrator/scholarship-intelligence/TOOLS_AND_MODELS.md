# Ferramentas e modelos avaliados — catálogo não instalado

Esta lista registra projetos e APIs **potencialmente úteis**. Nenhuma dependência
externa está embutida ou instalada neste repositório; examine versões, licenças,
cadeia de suprimento e política de processamento de dados antes de implantar.

| Camada | Ferramenta | Origem | Licença indicada / status | Uso proposto |
|---|---|---|---|---|
| Formulários e navegador | Playwright Python | https://github.com/microsoft/playwright-python | Apache-2.0 | Browser control local, seletores, testes em portais simulados |
| Navegação orientada por agente | browser-use | https://github.com/browser-use/browser-use | MIT, biblioteca aberta; nuvem paga | Planejar interações em sites complexos, SEM autoenvio |
| Coleta pública | Crawl4AI | https://github.com/unclecode/crawl4ai | Apache-2.0 | Páginas públicas → Markdown/JSON, respeitar robots/ToS |
| Editais PDF | Docling | https://github.com/docling-project/docling | MIT, verificar licença dos modelos | Tabelas, layout, barema, PDF estruturado |
| Estado, checkpoints | LangGraph | https://github.com/langchain-ai/langgraph | MIT | Processo retomável, HITL, máquina de estados |
| Saídas tipadas | PydanticAI | https://github.com/pydantic/pydantic-ai | MIT | Extração validada com schema em versão futura |
| Proteção de dados | Microsoft Presidio | https://github.com/microsoft/presidio | Verificar licença do componente | Detecção de dados identificáveis, sempre com revisão manual |
| LLM local | Qwen3-8B | https://huggingface.co/Qwen/Qwen3-8B | Apache-2.0 | Texto e triagem local; adequação depende de hardware |
| Busca multilíngue | BGE-M3 | https://huggingface.co/BAAI/bge-m3 | MIT | Busca semântica por programas, projetos, editais |
| LLM comercial opcional | xAI Grok | https://docs.x.ai/overview | Proprietário, API paga | Leitura de metadados públicos; nunca enviar perfil por padrão |

## Seleção de arquitetura

- Regras, prazos, elegibilidade e baremas: algoritmo determinístico e citações.
- PDFs de editais: Docling, preservando número da página e versão.
- Descoberta de links públicos: HTML/HTTP e Crawl4AI, com foco em domínios oficiais.
- Login e formulário: Playwright e, futuramente, browser-use atrás de confirmação humana.
- Interpretação ambígua: Grok ou Qwen, mas resposta exige prova independente.
- Banco persistente: SQLite privado ou PostgreSQL com RBAC; nunca SQLite de candidato em Git.
- Embeddings opcionais: BGE-M3 somente quando o volume justificar índice.

## Agentes especialistas propostos

`call-intelligence` descobre editais e retificações;
`eligibility-auditor` analisa requisitos, cotas e PcD somente em ambiente privado;
`barema-auditor` pontua títulos comprovados;
`research-fit` avalia aderência da linha e orientação sem solicitar favorecimentos;
`browser-operator` prepara rascunhos nos portais autorizados;
`scholarship-guardian` separa ingresso, concessão, implementação e pagamento;
`privacy-guardian` elimina vazamentos;
`red-team` tenta identificar rejeições administrativas antes do envio.

## Fontes primárias oficiais

- UEL PEF: https://pos.uel.br/pef/editais/
- UESB/UESC PPGEF: https://www2.uesb.br/ppg/ppgef/?page_id=40
- UESC: https://www.uesc.br/
- FAPES: https://fapes.es.gov.br/edital-aberto-forma%C3%A7%C3%A3o-cient%C3%ADfica
- CAPES: https://www.gov.br/capes/pt-br
- CNPq: https://www.gov.br/cnpq/pt-br
- FAPESB: https://www.fapesb.ba.gov.br/

Lembrete: a presença de URL no catálogo não prova edital aberto.

## MCP 2026 e Grok: implementação atual

- SDK MCP Python **v2**: https://github.com/modelcontextprotocol/python-sdk
  (`from mcp.server import MCPServer`). Atenção: `FastMCP` legado
  (`mcp.server.fastmcp`) pertence à API v1 e não é usado pelo novo módulo.
- xAI Grok: https://docs.x.ai/developers/model-capabilities/text/best-practices
  (Responses API `/v1/responses`, Chat Completions legado).
- Qwen3-8B (Apache-2.0): https://huggingface.co/Qwen/Qwen3-8B
- BGE-M3 (MIT): https://huggingface.co/BAAI/bge-m3
- Qwen3-Embedding-0.6B (Apache-2.0):
  https://huggingface.co/Qwen/Qwen3-Embedding-0.6B

**Não confundir catálogo com instalação.** MCP local é um servidor de
ferramentas restritas; modelos de texto podem produzir recomendações, mas
não recebem shell, credenciais, acesso irrestrito à web ou submissão.

Critérios de integração: manutenção ativa, licença, dados enviados,
armazenamento, gastos, capacidade offline, vulnerabilidades, escape de
prompt injection, compatibilidade, custo de inferência e testes em ambiente
controlado. Não executar código novo de terceiros sem revisar a versão.
