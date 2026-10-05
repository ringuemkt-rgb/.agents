# Gemini Image Production — BDC v7.0

Use quando o destino final for Gemini Image.

## Capability rule

Capacidades do modelo mudam.
No momento da execução, verificar documentação/controles disponíveis.
Não hardcode capacidade futura como lei editorial.

Canonical intent:
- aspect ratio 4:5;
- image size 2K para iteração quando disponível;
- 4K para master quando disponível;
- final crop/export editorial 1080×1350.

O design grid BDC 2160×2700 é referência de layout, não exigência de resolução nativa.

## Production loop

```text
CLAIM LOCK
→ 25-BLOCK FENCE
→ GEMINI ADAPTER
→ GENERATIVE RISK ROUTER
→ ONE SLIDE
→ POST-RENDER QA
→ REPAIR OR FINALIZE
→ NEXT SLIDE
```

## Gemini Task Lock

```text
GEMINI IMAGE TASK LOCK:
Generate ONE single final carousel slide image.
Aspect ratio: 4:5 vertical.
One composition only — NOT a grid, NOT a storyboard, NOT multiple variants.
This prompt is fully autonomous.
Preserve T0/T1 quoted text verbatim.
Premium 2.5D graphic editorial semi-vector only.
2–3 cel-shading levels, matte surfaces, contact shadows, restrained depth, print grain 1.5–2%.
NO 3D render, NO CGI, NO Blender/Unreal/Octane look, NO photoreal skin/fur, NO plastic shader, NO game-engine aesthetic.
```

## Reference assets

Official logo:
if supplied, immutable.
Place; do not reinterpret.

Criago:
if supplied, identity reference.
Preserve species, coat, jacket, aviators, flags and adult proportions.

Third-party visual:
use only for functional composition/hierarchy clues.
Do not copy identity or distinctive layout.

Reference counts and fidelity vary by Gemini model; use the capability actually exposed by the selected model.

## Text routes

### G1 — In-model typography
Use when TEXT_RISK LOW/MED.
T0/T1 exact.
T2 may be finalization-eligible.

### G2 — Finalization-safe
Use when TEXT_RISK HIGH or exact copy failed twice.
Gemini renders:
hero, frame, background, diagrams and clean text zones.
Final exact text/source/logo are applied in a deterministic design/finalization stage.

G2 is not a failure; it is the preferred reliability route for dense scientific slides.

## Tiers

T0:
headline, counter, critical number/warning, category.

T1:
subhead, card titles, labels, CTA.

T2:
body, source, DOI, micro-footer.

If a text zone cannot be rendered accurately:
keep it blank/clean.
Never hallucinate replacement copy.

## Zones

A top chrome.
B headline.
C hero.
D evidence/explanation.
E Criago/quote.
F footer/source.

Use relative percentages; do not obsess over unsupported pixel placement.

## Density

Cover:
1 headline, 0–1 sub, 1 hero, 1 swipe cue.

Internal:
1 headline, 2–4 information units.

Comparison:
2 sides, ≤3 main axes each.

Data:
1 main chart, 1 takeaway, 1 caveat/source.

## 2.5D lock

Depth by layering, overlap, occlusion, contact shadow, shallow perspective and selective blur.
No 3D mesh, glossy engine lighting or photoreal skin.

## Render risk

Before generation declare:
TEXT_RISK
ANATOMY_RISK
DATA_RISK
BRAND_RISK

If HIGH:
simplify composition or use G2.

## Sequential consistency

Do not rely on chat memory for style.
Each slide repeats the canon.
Use reference assets where supported.

## Post-render Gemini QA

Reject or repair:
- wrong text;
- wrong language;
- extra copy;
- wrong slide count;
- wrong aspect ratio;
- anatomy failure;
- Criago drift;
- logo mutation;
- flags wrong;
- data mutation;
- 3D/CGI drift;
- visual overclaim;
- density failure.

Never move to next slide with unresolved P0/P1.
