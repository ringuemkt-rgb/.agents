# BDC PROMPT COMPILER & QA v2.0

## Missão

Tratar prompt e render como artefatos compiláveis.
Autonomia na saída, modularidade na fonte.

## Compile order

```text
CLAIM LEDGER
→ SLIDE JOB
→ EXACT COPY
→ VISUAL PROOF
→ GRAMMAR
→ COLOR/TYPE
→ GRID/ZONES
→ FRAME/BACKGROUND/DEPTH
→ HERO/DIAGRAM
→ CRIAGO/ASSETS
→ SOURCE/DATA STATE
→ NEGATIVES
→ RISK ROUTER
→ PRE-LINT
→ RENDER
→ POST-QA
→ REPAIR/FINALIZATION
```

## Structural linter — hard fail

Todo fence novo precisa dos 25 blocos em ordem.

Falhar se:
- versão não for v7 no cabeçalho ativo;
- aparecer “same as previous” ou equivalente;
- faltar Claim Lock, A11Y, Frame, Background L0–L9, Depth Z0–Z6, full Criago, official assets, provenance, negative, QA ou rejection;
- existir 3D/CGI como instrução positiva;
- existir claim não presente no ledger;
- existir número sem contexto/source;
- existir data state que contradiga o texto;
- “não apurado” coexistir com ranking/afirmação volumétrica;
- role H0-H4 antigo não for convertido para CR0-CR4;
- body crítico depender de fonte condensada ou microtexto.

## Contradiction linter

Detectar:
photoreal + 2.5D;
neon bloom + matte editorial;
Criago OFF + pose visível;
logo inventado + official asset lock;
T0/T1 “exact” + instrução de paraphrase;
headline > density budget;
causal arrow sem causal claim;
equal visual weights sugerindo equal quantitative contribution sem evidência.

## Claim-to-visual table

Internamente:
Claim ID | Claim | Evidence | Visual proof | Label | Caveat | Data state

Todo elemento grande deve justificar sua existência.

## Visual-proof classes

DIRECT_PHYSICAL
DOCUMENTARY
MECHANISTIC
COMPARATIVE
CONCEPTUAL
DATA

Se CONCEPTUAL ou MECHANISTIC não diretamente medido:
rotular ◇ MODELO DIDÁTICO ou △ INDIRETO.

## Density gates

Cover:
1 thesis;
1 hero;
0 paragraph;
0–1 short sub;
max 3 micro elements.

Internal:
1 thesis;
2–4 info units;
max 3 equivalent cards.

Comparison:
2 sides;
max 3 primary axes each unless type remains comfortably readable.

Data:
1 chart;
1 takeaway;
1 caveat/source.

## Generative risk router

TEXT_RISK HIGH when:
- critical exact copy is long;
- many labels;
- sources/DOI must be legible;
- mixed symbols/superscripts.

ANATOMY_RISK HIGH when:
- 3+ interacting people;
- complex grappling entanglement;
- close hands/feet;
- mirrored poses.

DATA_RISK HIGH when:
- exact numbers/axes;
- multiple units;
- ratios or error bars;
- small source text.

BRAND_RISK HIGH when:
- exact logo;
- flags;
- Criago close-up;
- multiple patches.

Routing:
LOW → all-in-one render allowed.
MED → simplify + explicit zones.
HIGH → reserve critical zones or use immutable reference/finalization layer.

## Text reliability

T0/T1 failure:
repair up to 2 generations.
Persistent failure:
do not keep regenerating blindly.
Preserve layout and route exact typography to finalization.

## Thumbnail gate

At ~150 px:
- headline readable;
- hero recognizable;
- one idea dominates;
- accent highlights correct concept;
- chrome tertiary.

## A11Y gate

body ≥4.5:1;
headline target ≥7:1;
graphics ≥3:1;
color + label/shape/position.

## Post-render QA

TEXT:
literal T0/T1, pt-BR, no hallucinated copy.

ANATOMY:
hands, limbs, joints, neck, sport technique.

BRAND:
Criago species/coat/wardrobe/flags;
logo immutable;
2.5D.

DATA:
values, units, denominators, axis, ordering, caveat.

MEANING:
visual does not overclaim.

## Repair loop

1 identify failing layer;
2 patch only cause;
3 recompile affected blocks;
4 rerender;
5 inspect again.

Max 2 generative repair attempts before FINALIZATION_ROUTE or REPROVADO.

## Severity

P0 factual/safety/data/source/brand integrity — blocks.
P1 autonomy/A11Y/anatomy/2.5D/text-critical — blocks.
P2 density/hierarchy/narrative — fix before deliver.
P3 polish — may ship with note.

## Compiler output status

COMPILED_PASS
FINALIZATION_REQUIRED
REPROVADO
