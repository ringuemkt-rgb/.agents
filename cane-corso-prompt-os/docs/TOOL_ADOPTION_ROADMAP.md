# Tool Adoption Roadmap

Roteiro de adoção progressiva das ferramentas recomendadas para o Cane Corso Prompt OS.

---

## Fase 0 — Uso portátil imediato

Objetivo: usar o sistema em qualquer IA.

Ações:

- copiar `SYSTEM_PROMPT.md`;
- usar templates manuais;
- gerar prompts individuais;
- registrar resultados em planilha.

Ferramentas:

- IA conversacional;
- `templates/insights_log.csv`;
- `templates/ip_viral_scorecard.md`.

Critério de sucesso:

- carrosséis completos com prompts autônomos;
- legenda pronta;
- CTA;
- próximos temas com IPV.

---

## Fase 1 — QA de prompts

Objetivo: impedir regressões e erros recorrentes.

Ações:

- ativar `configs/promptfoo.yaml`;
- criar casos de teste;
- validar negative prompt;
- validar presença de legenda, CTA, Reels e IPV.

Ferramentas:

- promptfoo.

Critério de sucesso:

- prompts não passam se romantizarem agressividade;
- prompts não passam se não forem autônomos;
- prompts não passam se omitirem CTA.

---

## Fase 2 — Ingestão de documentos

Objetivo: transformar PDFs e materiais técnicos em base consultável.

Ações:

- converter documentos com MarkItDown, Docling ou MinerU;
- salvar Markdown em `knowledge/`;
- preservar fonte e metadados.

Ferramentas:

- MarkItDown;
- Docling;
- MinerU.

Critério de sucesso:

- documentos técnicos convertidos;
- trechos pesquisáveis;
- base pronta para RAG.

---

## Fase 3 — RAG e evidência

Objetivo: respostas e posts fundamentados.

Ações:

- indexar documentos;
- usar embeddings multilíngues;
- reordenar trechos;
- avaliar fidelidade factual.

Ferramentas:

- LlamaIndex ou RAGFlow;
- BGE-M3;
- bge-reranker;
- Ragas.

Critério de sucesso:

- cada afirmação importante aponta para fonte;
- menos inferência sem base;
- menos alucinação.

---

## Fase 4 — Observabilidade

Objetivo: transformar uso em aprendizado acumulado.

Ações:

- registrar prompt, tema, versão, saída e resultado;
- associar cada publicação a métricas reais;
- criar score por post.

Ferramentas:

- Langfuse;
- `templates/insights_log.csv`.

Critério de sucesso:

- saber qual gancho performou;
- saber qual CTA gerou direct;
- saber qual tema merece parte 2.

---

## Fase 5 — Pipeline visual premium

Objetivo: controle avançado de imagem e consistência.

Ações:

- criar workflows ComfyUI;
- usar FLUX para backgrounds e assets;
- usar ControlNet para layout;
- usar IP-Adapter para estilo/mascote;
- usar SAM 2 para recortes.

Ferramentas:

- ComfyUI;
- FLUX;
- ControlNet;
- IP-Adapter;
- SAM 2.

Critério de sucesso:

- identidade visual consistente;
- menor erro de texto;
- artes sem texto prontas para Canva/Figma.

---

## Fase 6 — Autoaperfeiçoamento programático

Objetivo: otimizar o sistema por métrica, não por feeling.

Ações:

- modularizar ganchos, roteiros e prompts;
- criar métricas internas;
- testar variações;
- selecionar melhores exemplos;
- otimizar instruções.

Ferramentas:

- DSPy;
- promptfoo;
- Langfuse.

Critério de sucesso:

- prompts vencedores viram exemplos;
- erros viram asserts;
- dados reais ajustam o próximo pacote.

---

## Regra de adoção

Não adotar ferramenta por vaidade técnica.

Adotar somente se resolver uma das dores:

- melhorar evidência;
- reduzir erro;
- aumentar consistência visual;
- aumentar velocidade;
- medir performance;
- melhorar conversão;
- preservar identidade.
