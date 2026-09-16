# BOXE DE CRIA — Carousel Orchestrator

Portable, model-agnostic system for building **evidence-first, visually didactic, premium 2.5D combat-sports carousels** for BOXE DE CRIA™ / FISIOBOXE.

This package is designed to run in **any capable LLM** that accepts custom/system instructions, project files, agent rules, or repository context.

## What it does

Given a raw theme, study, news item, screenshot or visual reference, the orchestrator:

1. audits the topic before scripting;
2. searches for current and primary evidence when tools are available;
3. identifies myths, contradictions, gaps and recent research deltas;
4. generates and stress-tests multiple hooks;
5. builds a simple Brazilian-Portuguese didactic arc;
6. maps every important claim to a useful visual explanation;
7. compiles fully autonomous, ultra-detailed slide prompts;
8. enforces BOXE DE CRIA visual continuity and Criago canon;
9. produces a copy/paste-ready caption with controlled emojis, one CTA and 3–5 hashtags;
10. runs pre/post-render QA.

## Universal entry point

Use [`SYSTEM_PROMPT.md`](./SYSTEM_PROMPT.md) as the primary instruction block.

For tools that support repository-aware agents, also load [`AGENT.md`](./AGENT.md) and [`MANIFEST.json`](./MANIFEST.json).

## Quick start — any AI

Paste the contents of `SYSTEM_PROMPT.md` into the model's **System / Custom Instructions / Project Instructions** field, then send:

```text
Tema: [seu tema]
Modo: carrossel completo
Idioma: português brasileiro
Pesquisar evidência atual quando houver acesso à web.
Entregar os prompts slide por slide, todos integralmente autônomos.
```

## Portability

See [`PORTABILITY.md`](./PORTABILITY.md) for ChatGPT, Claude, Gemini and generic LLM usage.

## Repository contract

The portable system follows these invariants:

- **Prompts by default, images only on explicit render request.**
- **Theme-only rebuild** for references: extract the topic, never copy the third-party design.
- **Research before hook** for factual/current/technical topics.
- **No invented data, sources, percentages, scores or “secret algorithm” claims.**
- **One dominant thesis per slide.**
- **Every major claim must have a visual job.**
- **Every slide prompt must be self-contained.**
- **Criago full character lock repeats even when hidden.**
- **No promise of virality; optimize legitimate stop-power, saves, shares, clarity and authority.**

## Structure

```text
boxe-de-cria-carousel-orchestrator/
├── AGENT.md
├── SYSTEM_PROMPT.md
├── MANIFEST.json
├── PORTABILITY.md
├── LICENSE
├── NOTICE.md
└── schemas/
    └── claim-ledger.schema.json
```

## Version

`3.1.0-portable.1`

## License

MIT for the portable prompt/agent implementation in this directory. See `NOTICE.md` for brand/trademark boundaries.
