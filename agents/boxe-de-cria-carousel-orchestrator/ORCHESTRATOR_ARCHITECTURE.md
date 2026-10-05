# BOXE DE CRIA Carousel Orchestrator — Architecture v7.1

## Objetivo

Eliminar drift, duplicação conflitante e desperdício de contexto sem perder a exigência do usuário de prompts finais totalmente autônomos.

## Princípio estrutural

SOURCE MODULARITY → COMPILED REDUNDANCY

A fonte canônica existe uma vez.
A saída compilada repete tudo o que o gerador precisa.

## Camadas

### A — Control Plane
ACTIVATE.md
SKILL.md
MODULE_STATUS.md
MANIFEST.json

### B — Demand Plane
AUDIENCE_DEMAND_INTELLIGENCE_ENGINE.md
TOPIC_OPPORTUNITY_ENGINE.md
CONTENT_GRAPH_ENGINE.md

### C — Evidence Plane
INVESTIGATIVE_SYNTHESIS_INTELLIGENCE.md
EVIDENCE_SYNTHESIS.md
CROSS_STUDY_INTELLIGENCE.md
GRADE_RUBRIC.md
RED_TEAM_EVALUATION_ENGINE.md

Saída:
BEST CURRENT EXPLANATION + CLAIM LEDGER + GAP MAP.

### D — Editorial Plane
ATTENTION_NARRATIVE.md
VIRAL_ENGINE.md
NEUROMARKETING_PERCEPTION_ENGINE.md

Saída:
HOOK + SHARE/SAVE JOB + DIDACTIC ARC + PERCEPTION PLAN.

### E — Visual Plane
VISUAL_SYSTEM_PROFESSIONAL.md
INFOGRAPHIC_GRAMMAR.md
PALETTE_CANON.md
PALETTE_DECISION_ENGINE.md
COLOR_THEORY_BDC.md
ACCESSIBILITY_CONTRAST.md
RENDER_2_5D_LOCK.md
OFFICIAL_LOGO_LOCK.md

Saída:
VISUAL PROOF PLAN.

### F — Compiler Plane
PROMPT_PROTOCOL_FIXED.md
PROMPT_TEMPLATE.md
PROMPT_COMPILER_QA.md

Saída:
N autonomous 25-block fences.

### G — Model Adapter Plane
GEMINI_PRODUCTION.md ou outro adapter futuro.

O adapter nunca redefine Evidence, Brand ou A11Y.

### H — Finalization Plane
Text finalization when generative rendering is unreliable.
Official asset insertion.
Export/crop 1080×1350.

### I — Distribution Plane
Caption compiler.
SEO semântico.
CTA útil.
Originalidade e utilidade acima de “algoritmo hack”.

### J — Learning Plane
EDITORIAL_LEARNING_ENGINE.md

## Canonical pipeline

```text
REQUEST
↓
MODE ROUTER
↓
RISK TIER
↓
DEMAND if needed
↓
EVIDENCE
↓
RED TEAM
↓
CLAIM LEDGER
↓
HOOK / ARC
↓
VISUAL PROOF
↓
GRAMMAR
↓
25-BLOCK COMPILER
↓
MODEL ADAPTER
↓
PRE-QA
↓
RENDER
↓
POST-QA / REPAIR
↓
FINALIZATION
↓
CAPTION
↓
GATE
↓
LEARNING
```

## Claim-to-slide handoff

Cada claim material:
- claim_id;
- wording;
- status;
- certainty;
- directness;
- population;
- caveat;
- source_ids;
- expiry/freshness note.

Cada slide usa apenas claims necessários.

## Risk routers

### Forensic risk
T0 visual/creative sem claim factual.
T1 evergreen.
T2 performance/biomecânica/comparação.
T3 saúde/safety/criança/TEA/concussão/lesão/vulnerável.

### Generative risk
TEXT_RISK LOW/MED/HIGH.
ANATOMY_RISK LOW/MED/HIGH.
DATA_RISK LOW/MED/HIGH.
BRAND_RISK LOW/MED/HIGH.

HIGH exige simplificação ou finalização externa.

## Visual architecture

ONE THESIS → ONE GRAMMAR → ONE HERO → ONE VISUAL PROOF → ONE MEMORY LINE.

Core frame:
pill + counter + hairline + 4 L-corners + footer.
Rails são opcionais quando prejudicarem density/chrome budget.

Depth:
Z0–Z6.

Background:
L0–L9.

## No-conflict doctrine

- nenhum arquivo ativo pode declarar versão 5.x/6.x como current;
- contrato visual atual = 25 blocos;
- depth atual = Z0–Z6;
- narrative role do Criago = CR0–CR4;
- humor = H0–H3;
- caption prompt é obrigatório;
- Gemini native size e design grid são coisas diferentes.


## Runtime execution plane

### Canon plane
`canon/*.json` holds brand, palette, typography, A11Y, frame, background, render, Criago, evidence states, freshness, assets and caption rules.

### Compiler plane
`src/compiler/*` compiles canonical locks + slide-specific claims into autonomous 25-block prompts.

### Intelligence plane
`src/intelligence/forensic-ai.ts` orchestrates adversarial research roles. In interactive ChatGPT use, those roles are executed by the current assistant with available web/file tools; external automation may provide an `AiProvider`.

### Deterministic finalization plane
Exact charts, critical typography, source IDs and official assets must prefer deterministic SVG/finalization when generative risk is HIGH.

### Learning plane
Account metrics remain descriptive until sufficiently controlled experimentation justifies stronger inference.

### CI plane
`.github/workflows/bdc-orchestrator-ci.yml` runs typecheck, tests, example compilation and repository-contract checks.
