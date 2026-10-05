# PROTOCOLO FIXO — BDC Surgical Prompt Compiler v7.1

Todo prompt visual final é autônomo.
A fonte é modular; o fence compilado é redundante por design.

## Ordem

Audience/Demand when material
→ Perícia
→ Best Current Explanation
→ Claim Ledger
→ Red Team
→ Viral Brief
→ Didactic Arc
→ Visual Proof Plan
→ N fences de 25 blocos
→ Target Adapter
→ QA
→ Caption Prompt
→ Gate

## Autonomy Repetition Law

Todo fence final contém explicitamente:
format/target;
claim;
audience;
narrative;
exact copy;
color/A11Y;
type;
grid/zones;
frame;
background;
depth;
grammar;
hero;
diagram/data;
camera;
light;
materiality;
full Criago canon;
official assets;
source/data state;
negative;
compiler;
post-QA;
rejection.

Nunca:
“same as previous”
“mesmo background”
“seguir o slide anterior”.

## 25 blocos

### 01 TASK / TARGET / OUTPUT LOCK
- uma arte;
- 4:5;
- design grid conceitual 2160×2700;
- export final 1080×1350;
- sRGB;
- safe top 7%, left 7%, right 7%, bottom 6%;
- 12 cols;
- spacing ×8;
- baseline 24;
- negative space 22–28%, capa pode chegar a 35%;
- target model declarado;
- render 2.5D editorial only.

Importante:
2160×2700 é grid de design, não resolução física obrigatória do gerador.

### 02 BRAND / MODE / SÉRIE
Marca, submarca, série, tema, mode, tone e positioning.

### 03 EVIDENCE / CLAIM LOCK
Incluir somente claims usados no slide:
CLAIM IDS;
allowed wording;
blocked wording;
certainty;
directness;
population;
critical caveat.

### 04 AUDIENCE / JTBD / INTENT
Persona, awareness, real problem, intent, lexicon, JTBD, share reason, save reason.

### 05 NARRATIVE / ATTENTION / SHARE-SAVE
ROLE;
PRIMARY FOCAL;
ENTRY;
READING PATH;
PAYOFF NOW;
OPEN LOOP;
NEXT DESIRE;
SWIPE HANDOFF;
SHARE JOB;
SAVE JOB;
Gestalt/fluency;
no pseudo-neuromarketing.

### 06 EXACT TEXT / T0-T1-T2
T0 critical exact.
T1 secondary exact.
T2 finalization-eligible.
Do not paraphrase/translate/add copy.
Capa: zero parágrafo.

### 07 COLOR / A11Y / SEMANTIC COLOR
Usar palette canon.
Máx. 2 main accents.
Body ≥4.5:1.
Headline target ≥7:1.
Graphics ≥3:1.
No hue-only distinction.

### 08 TYPOGRAPHY / LEGIBILITY
Max 2 families.
Headline condensed only for short copy.
Body non-condensed.
No all-caps paragraph.
No critical microtext.

### 09 GRID / SAFE AREA / DENSITY / ZONES
12-col grid.
Safe area.
Density budget.
Define zones A–F when target generative:
A chrome;
B headline;
C hero;
D explanation;
E Criago/quote;
F source/footer.

### 10 FRAME / CHROME
Core:
charcoal/graphite;
bronze/gold hairline;
4 cyan L-corners;
top pill;
counter;
footer;
logo zone.

Rails optional.
Chrome attention budget ≤5%.

### 11 BACKGROUND L0–L9
L0 field.
L1 vignette.
L2 material.
L3 microgrid.
L4 environment ghost.
L5 blueprint.
L6 mechanism/evidence.
L7 cultural/documentary memory.
L8 focal halo.
L9 interface/frame integration.

### 12 DEPTH Z0–Z6
Z0 field.
Z1 environment/material.
Z2 grid/blueprint.
Z3 hero.
Z4 diagram/evidence.
Z5 copy.
Z6 frame/brand.

Depth only by layering, overlap, occlusion, contact shadow, selective blur, shallow perspective.

### 13 VISUAL GRAMMAR / METAPHOR
Choose one grammar.
Declare visual metaphor/proof.
No two competing grammars.

### 14 HERO / COMPOSITION / ANATOMY
Hero demonstrates claim.
Humans generic unless authorized reference flow.
Anatomy and sport technique plausible.
Declare placement, scale, pose and negative space.

### 15 DIAGRAM / DATA-VIZ / CLAIM TRACE
CLAIM → VISUAL → LABEL → SOURCE/CAVEAT.
For quantitative content:
variable, measure, unit, denominator, population, N, time, uncertainty, comparison, instrument, what-not-measured.
Charts flat/orthographic.
No perspective deception.

### 16 CAMERA / PERSPECTIVE
Declare lens-equivalent, angle, crop and fairness constraints.

### 17 LIGHTING
Editorial dramatic lighting, not cinematic CGI.
Controlled key/fill/rim.
No engine bloom.

### 18 MATERIALITY
Matte leather/canvas/gi/paper/metal/rubber.
2–3 cel levels.
Print grain 1.5–2%.
No ray-traced/plastic look.

### 19 CRIAGO FULL CANON / CR-ROLE / H-LEVEL
Repeat full species/anatomy/coat/wardrobe/flags/back/aviators/render lock.
CR0 witness; CR1 mentor; CR2 skeptic; CR3 curator; CR4 closer.
H0–H3 is humor intensity only.
Health/safety/TEA/children/injury = H0.

### 20 OFFICIAL ASSETS / REFERENCE HANDLING
Official BDC logo = immutable owner asset.
Canonical Criago image = identity reference when supplied.
Third-party references = function/hierarchy only.
If exact asset unavailable, reserve zone.

### 21 SOURCE / PROVENANCE / DATA STATE
List source IDs relevant to this slide.
Declare:
✓ confirmed;
≈ estimated;
△ indirect;
◇ didactic model;
? not investigated;
! conflicting.
Freshness note if time-sensitive.

### 22 NEGATIVE / DO-NOT-DRAW
Global negatives + slide-specific negatives.
No 3D/CGI, fake source/data/ranking, logo substitute, Criago drift, random HUD, pseudo-neuro, misleading arrow.

### 23 PRE-RENDER COMPILER
Pass:
STRUCTURE;
VERSION;
CLAIM;
EVIDENCE STATE;
CONTRADICTION;
CLAIM→VISUAL;
DENSITY;
THUMBNAIL;
A11Y;
COLOR-BLIND;
2.5D;
TEXT RISK;
ANATOMY RISK;
DATA RISK;
BRAND RISK.

### 24 POST-RENDER QA / REPAIR
Check exact copy, anatomy, brand, data, A11Y, 2.5D, logo, Criago, crop and visual meaning.
Repair only the failing cause.
Up to 2 generative repairs; then route to finalization or reject.

### 25 REJECTION CONDITIONS
Explicit slide-specific hard fails.
P0/P1 = do not ship.

## Caption contract

After final slide, always output:
PROMPT COMPLETO DA DESCRIÇÃO / LEGENDA — COPIAR E COLAR

Unless explicitly omitted by the user.


## Runtime compiler binding

The documentary contract is now executable.

- Canonical locks are loaded from `canon/*.json`.
- Slide-specific content is supplied as a structured `SlidePlan`.
- `src/compiler/compile-slide.ts` expands the 25 blocks.
- `src/qa/contract-linter.ts` blocks cross-slide dependency, blocked claims and ranking language over `NOT_INVESTIGATED` data.
- `src/routers/risk-router.ts` chooses `G1_IN_MODEL` or `G2_FINALIZATION_SAFE`.
- Exact charts/text may be produced with deterministic SVG helpers.

A manually written prompt is valid only if it satisfies the same contract.
