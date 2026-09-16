# BOXE DE CRIA — Carousel Orchestrator

Portable, model-agnostic system for building **forensically researched, evidence-synthesized, audience-aware, retention-engineered and visually didactic combat-sports carousels** for BOXE DE CRIA™ / FISIOBOXE.

This package is designed to run in **any capable LLM** that accepts custom/system instructions, project files, agent rules or repository context.

## What v3.3 adds

v3.3 upgrades the research layer from “find studies and summarize them” into a **Forensic Evidence Fusion system**.

The orchestrator can now:

- detect multiple publications from the same cohort;
- prevent double-counting overlapping samples;
- separate different outcomes before synthesis;
- route risk-of-bias appraisal by study design;
- build an Evidence Graph linking claims, studies, populations, outcomes, mechanisms, moderators and contradictions;
- create causal/mechanistic maps when causality is relevant;
- normalize effect measures without fake conversions;
- analyze clinical, methodological and statistical heterogeneity;
- actively search for null/contradictory findings;
- triangulate experimental, observational, mechanistic, real-world and qualitative evidence;
- assess applicability to the real audience/population;
- estimate certainty **by outcome**, not with one global “science score”;
- pair benefits with harms, burden and feasibility;
- inspect missing/unpublished evidence when material;
- produce an integrated conclusion: **known / likely / plausible / unknown / contradicted / what would change the conclusion**.

The 56-block visual prompt contract remains unchanged. The extra intelligence happens **before** prompt compilation, so prompts stay detailed and reconstructible without becoming bloated systematic-review documents.

## Canonical workflow

Given a raw theme, study, news item, screenshot or reference, the orchestrator:

1. identifies the primary audience and problem;
2. audits the theme before scripting;
3. selects a forensic depth tier;
4. searches current and primary evidence when tools exist;
5. separates scientific novelty from current attention/trend context;
6. maps Brazilian-Portuguese search language;
7. mines competitive editorial gaps without copying;
8. builds Claim Ledger;
9. resolves duplicated/overlapping study families;
10. builds Outcome Ontology;
11. routes risk-of-bias appraisal;
12. builds Evidence Matrix + Evidence Graph;
13. builds causal/mechanistic map when relevant;
14. analyzes effect measures, heterogeneity and contradictions;
15. triangulates independent evidence lines;
16. checks applicability and certainty by outcome;
17. pairs benefits/harms and checks missing evidence;
18. produces the integrated evidence conclusion;
19. locks editorial claims;
20. only then generates/stress-tests >=12 hooks;
21. assigns one primary Content Job;
22. builds didactic + retention arc;
23. maps every claim to a useful visual explanation;
24. resolves the requested design into a complete STYLE LOCK;
25. selects Mestre Criago archetypes/humor mode when relevant;
26. compiles autonomous **56-block slide prompts**;
27. produces copy/paste-ready caption with controlled emojis, one CTA and 3–5 hashtags;
28. proposes distribution derivatives when useful;
29. records an experiment hypothesis when growth is measurable;
30. runs pre/post-render QA and learns from real analytics.

## Forensic tiers

### Tier 1 — Rapid Forensic
For simple, low-risk evergreen content.

### Tier 2 — Deep Synthesis
For sports science, performance, biomechanics and evidence-heavy topics.

### Tier 3 — Full Investigative Dossier
For clinical/safety topics, children, neurodevelopment, concussion, injury, vulnerable populations, major controversies or high-impact claims.

Full methodology: [`EVIDENCE_SYNTHESIS.md`](./EVIDENCE_SYNTHESIS.md)

## Evidence schemas

The package includes structured schemas for agents/workflows:

- [`schemas/claim-ledger.schema.json`](./schemas/claim-ledger.schema.json)
- [`schemas/evidence-graph.schema.json`](./schemas/evidence-graph.schema.json)
- [`schemas/study-family-ledger.schema.json`](./schemas/study-family-ledger.schema.json)

## Mestre Criago

Criago is formally treated as **Mestre Criago** when he speaks: an old-school, evidence-literate master who protects the student and uses dry/acid humor against bad ideas, ego and pseudoscience — never against beginners, bodies, disability, injury or vulnerable people.

Default archetype blend:

- Sage 35%
- Mentor/Caregiver 25%
- Warrior/Hero 20%
- Trickster/Jester 15%
- Ruler/Guardian 5%

Sarcasm modes range from `H0` neutral to `H3` cutting, with sensitive clinical/safety topics defaulting to `H0`.

## Universal entry point

Use [`SYSTEM_PROMPT.md`](./SYSTEM_PROMPT.md) as the primary instruction block.

For repository-aware tools, also load:

1. [`AGENT.md`](./AGENT.md)
2. [`EVIDENCE_SYNTHESIS.md`](./EVIDENCE_SYNTHESIS.md)
3. [`MANIFEST.json`](./MANIFEST.json)

## Quick start — any AI

Paste `SYSTEM_PROMPT.md` into the model's **System / Custom Instructions / Project Instructions** field, then send:

```text
Tema: [seu tema]
Modo: carrossel completo
Idioma: português brasileiro

Defina audiência e problema antes do roteiro.
Escolha o nível de perícia necessário.
Pesquise evidência atual quando houver acesso à web.
Resolva estudos duplicados/coortes sobrepostas antes de contar estudos.
Separe outcomes diferentes.
Procure evidência contraditória e avalie aplicabilidade.
Construa uma conclusão integrada antes de escolher o hook.
Escolha o melhor ângulo sem ultrapassar a evidência.
Construa retenção slide a slide.
Use o estilo visual que eu especificar e repita o STYLE LOCK integralmente em cada prompt.
Entregue prompts ultra detalhados, totalmente autônomos, slide por slide.
Finalize com legenda pronta para copiar e colar.
```

## Repository contract

- **Prompts by default; images only on explicit render request.**
- **Theme-only rebuild** for references; never copy third-party identity.
- **Evidence synthesis before hook** for factual/current/technical themes.
- **No duplicate study counting.**
- **No outcome conflation.**
- **No mechanism → clinical benefit leap.**
- **No hiding important heterogeneity.**
- **No invented data, sources, trends, search volumes, scores or secret-algorithm claims.**
- **Audience/problem fit before storyboard.**
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
├── EVIDENCE_SYNTHESIS.md
├── MANIFEST.json
├── PORTABILITY.md
├── CHANGELOG.md
├── LICENSE
├── NOTICE.md
└── schemas/
    ├── claim-ledger.schema.json
    ├── evidence-graph.schema.json
    └── study-family-ledger.schema.json
```

## Version

`3.3.0-portable.1`

## License

MIT for the portable prompt/agent implementation in this directory. See `NOTICE.md` for brand/trademark boundaries.
