# BOXE DE CRIA — Carousel Orchestrator

Portable, model-agnostic system for building **evidence-first, audience-aware, retention-engineered and visually didactic combat-sports carousels** for BOXE DE CRIA™ / FISIOBOXE.

This package is designed to run in **any capable LLM** that accepts custom/system instructions, project files, agent rules or repository context.

## What v3.2 adds

The orchestrator no longer starts from “make slides about this topic”. It now starts by deciding **who needs the topic, what real problem it solves, what evidence is current, what angle is underexplored, why the reader should keep swiping, why the post is worth saving/sharing, and what the system should learn after publication**.

New strategic layers:

- Audience Intelligence;
- Problem–Audience Fit;
- Fresh Attention Delta;
- Social Search Intelligence;
- Competitive Gap Miner;
- Topic Opportunity Matrix;
- Content Job Router;
- Retention Engine;
- Saveability Engineering;
- Design Style Resolver;
- Distribution Multiplier;
- Experiment Ledger;
- Content Portfolio Router;
- Mestre Criago Mindset & Archetype Engine.

## Canonical workflow

Given a raw theme, study, news item, screenshot or reference, the orchestrator:

1. identifies the primary audience and problem;
2. audits the theme before scripting;
3. searches current and primary evidence when tools exist;
4. separates scientific novelty from current attention/trend context;
5. maps social-search language in Brazilian Portuguese;
6. looks for competitive editorial gaps without copying competitors;
7. builds Claim Ledger, Evidence Matrix, contradictions and Fact Lock;
8. evaluates angle opportunity;
9. generates and stress-tests at least 12 hooks;
10. assigns one primary Content Job;
11. builds a didactic and retention arc;
12. maps every important claim to a useful visual explanation;
13. resolves the user-requested design style into a complete STYLE LOCK;
14. selects Mestre Criago archetypes/humor mode when relevant;
15. compiles fully autonomous **56-block slide prompts**;
16. produces a copy/paste-ready caption with controlled emojis, one CTA and 3–5 hashtags;
17. proposes distribution derivatives when useful;
18. records an experiment hypothesis when growth is measurable;
19. runs pre/post-render QA and learns from real analytics.

## Mestre Criago

Criago is now formally treated as **Mestre Criago** when he speaks: an old-school, evidence-literate master who protects the student and uses dry/acid humor against bad ideas, ego and pseudoscience — never against beginners, bodies, disability, injury or vulnerable people.

Default archetype blend:

- Sage 35%
- Mentor/Caregiver 25%
- Warrior/Hero 20%
- Trickster/Jester 15%
- Ruler/Guardian 5%

Sarcasm modes range from `H0` neutral to `H3` cutting, with sensitive clinical/safety topics defaulting to `H0`.

## Universal entry point

Use [`SYSTEM_PROMPT.md`](./SYSTEM_PROMPT.md) as the primary instruction block.

For repository-aware tools, also load [`AGENT.md`](./AGENT.md) and [`MANIFEST.json`](./MANIFEST.json).

## Quick start — any AI

Paste `SYSTEM_PROMPT.md` into the model's **System / Custom Instructions / Project Instructions** field, then send:

```text
Tema: [seu tema]
Modo: carrossel completo
Idioma: português brasileiro

Defina a audiência e o problema antes do roteiro.
Pesquise evidência atual quando houver acesso à web.
Procure novidade científica real e atenção recente sem inventar tendências.
Escolha o melhor ângulo e hook sem ultrapassar a evidência.
Construa retenção slide a slide.
Use o estilo visual que eu especificar e repita o STYLE LOCK integralmente em cada prompt.
Entregue prompts ultra detalhados, totalmente autônomos, slide por slide.
Finalize com legenda pronta para copiar e colar.
```

## Repository contract

- **Prompts by default; images only on explicit render request.**
- **Theme-only rebuild** for references; never copy third-party identity.
- **Research before hook** for factual/current/technical themes.
- **Audience/problem fit before storyboard.**
- **No invented data, sources, trends, search volumes, scores or secret-algorithm claims.**
- **One dominant thesis per slide.**
- **Every slide delivers a payoff and a legitimate reason to continue.**
- **Every major claim has a visual job.**
- **Every slide prompt is self-contained.**
- **The full selected design style is repeated in every prompt.**
- **Criago full visual lock repeats even when hidden.**
- **Mestre Criago humor attacks ideas, never vulnerable people.**
- **No promise of virality; optimize legitimate discovery, retention, saves, shares, authority and conversion.**

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

`3.2.0-portable.1`

## License

MIT for the portable prompt/agent implementation in this directory. See `NOTICE.md` for brand/trademark boundaries.
