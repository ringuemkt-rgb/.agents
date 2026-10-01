# Cane Corso do Cangaço — Prompt Production OS

Sistema profissional, público e portátil para produzir **posts, carrosséis, prompts de imagem, legendas, Reels derivados, Stories, temas com potencial viral e fluxos de melhoria contínua** para a marca **Cane Corso do Cangaço**.

> Filosofia central: **força sob controle, guarda equilibrada, criação responsável e autoridade visual premium.**

Este repositório foi pensado para funcionar em qualquer chat de IA. Basta copiar o conteúdo de `SYSTEM_PROMPT.md` para o chat ou usar `AGENTS.md` como instrução de projeto/agente.

---

## O que este sistema faz

- Estrutura carrosséis com pesquisa, tese, gancho, roteiro e prompts individuais.
- Gera prompts autônomos por slide para Gemini, ChatGPT, Midjourney, ComfyUI/Flux ou outro gerador visual.
- Mantém identidade visual premium 2.5D da marca.
- Separa fato, evidência, inferência e opinião editorial.
- Cria legenda otimizada para Instagram com CTA, emojis e palavras-chave.
- Produz variações de capa A/B/C.
- Gera Reels e Stories derivados.
- Calcula o **IPV — Índice de Potencial Viral**, uma estimativa estratégica baseada em dor do público, salvamento, compartilhamento, gancho, aderência à marca e segurança de recomendação.
- Adiciona uma arquitetura open-source opcional para RAG, avaliação, observabilidade, prompt optimization e pipeline visual.

---

## Novo em v4.0

O sistema agora inclui uma camada profissional de ferramentas open-source para tornar o fluxo mais completo:

- **DSPy** para otimização programática de prompts e módulos.
- **promptfoo** para testes, regressão, comparação e red team de prompts.
- **Langfuse** para observabilidade, logs, versões e gestão de prompts.
- **Docling / MarkItDown / MinerU** para converter documentos em Markdown/RAG.
- **LlamaIndex / RAGFlow** para base de conhecimento pesquisável.
- **BGE-M3 + reranker** para busca semântica multilíngue.
- **Ragas** para avaliação de fidelidade factual em RAG.
- **ComfyUI + FLUX + ControlNet + IP-Adapter + SAM 2** para pipeline visual premium e consistente.
- **Qwen / vLLM / SGLang / llama.cpp / PEFT / TRL** como rotas de modelos abertos e evolução futura.

> Importante: estes componentes são **módulos recomendados**. O sistema não afirma que todos estão instalados. Eles devem ser adotados conforme ambiente, orçamento, máquina e objetivo.

---

## Estrutura

```text
cane-corso-prompt-os/
├── README.md
├── AGENTS.md
├── SYSTEM_PROMPT.md
├── CHANGELOG.md
├── data/
│   └── brand_config.json
├── docs/
│   ├── OPEN_SOURCE_AI_STACK.md
│   ├── TOOL_ADOPTION_ROADMAP.md
│   ├── EVAL_PROTOCOL.md
│   ├── RAG_PIPELINE.md
│   └── VISUAL_AI_PIPELINE.md
├── configs/
│   ├── promptfoo.yaml
│   ├── langfuse_schema.json
│   ├── dspy_modules.md
│   └── rag_models.md
├── templates/
│   ├── carousel_request_template.md
│   ├── slide_prompt_template.md
│   ├── instagram_caption_template.md
│   ├── ip_viral_scorecard.md
│   ├── eval_cases.csv
│   └── insights_log.csv
├── scripts/
│   └── prompt_pack_generator.py
└── examples/
    └── jiu-jitsu-cane-corso-carousel.md
```

---

## Como usar em qualquer IA

1. Abra `SYSTEM_PROMPT.md`.
2. Copie o conteúdo completo.
3. Cole no início de um novo chat.
4. Depois peça algo como:

```text
Faça um carrossel sobre socialização do filhote Cane Corso usando o sistema completo.
```

---

## Como usar como agente/projeto

Use `AGENTS.md` como instrução do agente.

Ele define:

- tom de voz;
- identidade visual;
- pipeline de pesquisa;
- prompt engineering;
- QA;
- IPV;
- próximos temas;
- regras éticas;
- módulos open-source opcionais.

---

## Como usar o gerador simples

```bash
python3 scripts/prompt_pack_generator.py "Socialização do filhote Cane Corso"
```

O script cria um esqueleto de pacote de carrossel com:

- tema;
- tese;
- crença errada;
- prompts individuais;
- legenda;
- CTA;
- IPV;
- próximos temas.

---

## Ordem recomendada de adoção técnica

### Fase 1 — Sem custo alto

- Usar `SYSTEM_PROMPT.md` manualmente.
- Registrar resultados em `templates/insights_log.csv`.
- Rodar avaliações com `configs/promptfoo.yaml`.
- Usar `docs/EVAL_PROTOCOL.md` para QA.

### Fase 2 — Pesquisa e RAG

- Converter documentos com MarkItDown, Docling ou MinerU.
- Indexar com LlamaIndex ou RAGFlow.
- Usar BGE-M3 e reranker.
- Validar com Ragas.

### Fase 3 — Visual premium

- Criar workflows no ComfyUI.
- Gerar com FLUX.1.
- Controlar layout com ControlNet.
- Manter identidade com IP-Adapter.
- Recortar assets com SAM 2.

### Fase 4 — Autoaperfeiçoamento

- Modularizar o sistema com DSPy.
- Testar prompts com promptfoo.
- Registrar execuções com Langfuse.
- Otimizar com base em resultados reais.

---

## Regra operacional

Não publicar conteúdo que:

- romantize agressividade;
- venda cão bravo como virtude;
- prometa saúde/longevidade sem prova;
- promova cor rara como qualidade;
- use violência gratuita;
- gere desinformação cinotécnica ou veterinária;
- pareça panfleto genérico de pet shop.

---

## Filosofia final

O sistema existe para transformar conteúdo em ativo estratégico:

```text
pesquisa → tese → prompt → arte → legenda → publicação → insight → melhoria
```

Cada post deve ensinar, filtrar, atrair tutor sério, fortalecer a marca e aumentar a qualidade da próxima produção.
