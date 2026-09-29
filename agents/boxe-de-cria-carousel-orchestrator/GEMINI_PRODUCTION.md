# Gemini Image Production — BDC v5.1

Use este módulo quando o destino final de imagem for Gemini Image.

A investigação, Audience/Demand Intelligence, Claim Lock, narrativa e Prompt Compiler rodam ANTES desta etapa.

## 1. Produção padrão

```text
AUDIENCE/DEMAND
→ OPPORTUNITY
→ EVIDENCE
→ CLAIM LOCK
→ STORYBOARD
→ 22-BLOCK AUTONOMOUS FENCE
→ GEMINI ADAPTER
→ GENERATE ONE SLIDE
→ POST-RENDER QA
→ REPAIR IF NEEDED
→ NEXT SLIDE
```

Nunca pedir ao Gemini para gerar o carrossel inteiro numa única imagem.

---

## 2. Gemini Output Contract

Para cada slide:

- UMA imagem;
- proporção 4:5;
- uma única composição vertical;
- sem grid de 8 slides;
- sem storyboard;
- sem variantes lado a lado;
- sem mockup;
- sem smartphone;
- sRGB intent;
- 2.5D editorial only.

Quando a interface/API permitir configuração explícita:
- solicitar `aspect_ratio: 4:5`;
- preferir 2K para iteração e 4K para master final quando custo/tempo permitirem;
- nunca depender do aspect ratio implícito de uma referência.

O working canvas conceitual BDC continua 2160×2700; a resolução física real gerada pode seguir os tamanhos suportados pelo modelo. O layout deve ser pensado para crop/export final 1080×1350 sem perda de elementos.

---

## 3. Gemini Task Lock — inserir no bloco 01

```text
GEMINI IMAGE TASK LOCK:
Generate ONE single final carousel slide image.
Aspect ratio: 4:5 vertical.
One composition only — NOT a grid, NOT a storyboard, NOT multiple variants.
This prompt is fully autonomous; do not rely on prior chat images or previous slides.
Preserve all exact-text strings verbatim.
RENDER: premium 2.5D graphic editorial semi-vector only.
2–3 cel-shading levels, matte surfaces, contact shadows, restrained depth, print grain 1.5–2%.
NO 3D render, NO CGI, NO Blender/Unreal/Octane look, NO photoreal skin/fur, NO plastic shader, NO game-engine aesthetic.
```

---

## 4. Reference Asset Strategy

### Official logo
If the owner-supplied BDC logo is provided as an input image:
- treat it as immutable brand asset;
- preserve proportions/colors/wordmark;
- place it, do not reinterpret it.

If the logo is NOT supplied:
- reserve the exact logo zone;
- render textual placeholder only if the production workflow requests it;
- never invent a substitute mascot/logo.

### Criago reference
If a canonical Criago image is provided:
- use it as character-identity reference;
- preserve species, coat pattern, jacket, aviator, patches and adult proportions;
- do not copy accidental pose/background unless requested.

### Visual reference from another page
Use only for:
- functional reference;
- information hierarchy;
- type of composition.

Do NOT copy:
- brand;
- distinctive layout;
- wording;
- palette;
- logo;
- character.

---

## 5. Exact Text Reliability

Gemini must receive text in explicit priority tiers.

### T0 — must be exact
- headline;
- slide counter;
- key number;
- pill/category;
- critical warning.

### T1 — exact, secondary
- subheadline;
- card titles;
- labels;
- CTA.

### T2 — exact but may be moved to finalization if image render corrupts it
- body paragraph;
- source line;
- footer microcopy.

Prompt block 06 must mark:

```text
TEXT RENDER POLICY:
Do not paraphrase.
Do not translate.
Do not add copy.
Do not correct brand wording.
Render every quoted string exactly in Brazilian Portuguese.
If a text area cannot be rendered legibly, keep clean reserved space rather than hallucinating extra words.
```

If T0/T1 has spelling error in the image: REJECT and regenerate/repair.
If T2 repeatedly fails: preserve layout and apply text during finalization outside the generative render.

---

## 6. Typography for Gemini

To reduce text failure:

- maximum 2 type families;
- headline short;
- no dense paragraph on cover;
- body split into short lines;
- no extreme tracking;
- no ultra-thin fonts;
- avoid tiny superscripts;
- avoid curving essential text;
- keep critical text horizontal;
- use high-contrast opaque panels behind body when background is active.

The visual prompt should describe function first:
“large condensed display headline” + font reference.

Do not depend on Gemini reproducing a licensed font perfectly. Visual equivalence is acceptable unless the exact font is supplied in a separate design-finalization stage.

---

## 7. Layout Reliability

Gemini tends to follow strong spatial instructions better when the fence specifies explicit zones.

Every slide should define:

```text
ZONE A — top chrome / category / counter
ZONE B — primary headline
ZONE C — hero visual
ZONE D — explanatory content
ZONE E — Criago / quote if ON
ZONE F — footer / source / brand
```

Use percentages or relative position, not pixel-perfect coordinates unless necessary.

Example:
- A: top 7–13%;
- B: 15–33%;
- C: 28–72%;
- D: 55–82%;
- F: bottom 88–96%.

Zones may overlap intentionally only when specified.

---

## 8. 2.5D Style Lock

Always repeat:

```text
2.5D GRAPHIC EDITORIAL ONLY.
Semi-vector anatomy and props.
Matte surfaces.
2–3 cel-shading levels.
Layering, overlap, contact shadow, shallow perspective and selective blur create depth.
No 3D mesh, no CGI, no engine lighting, no glossy plastic.
```

Gemini should not interpret “cinematic” as photoreal/3D unless the prompt explicitly redefines it as editorial lighting.

Prefer “editorial dramatic lighting” over “cinematic 3D”.

---

## 9. Background/Frame Repetition

Every Gemini fence MUST restate the complete:
- FRAME LOCK;
- BACKGROUND L0–L9;
- DEPTH Z0–Z5;
- COLOR/A11Y;
- TYPOGRAPHY;
- CRIAGO;
- LOGO handling;
- NEGATIVE;
- QA.

Never:
- “same style as slide 1”;
- “same background”;
- “same mascot as before”.

Reference images are support, not a substitute for autonomy.

---

## 10. Content Density

For Gemini generation reliability:

### Cover
- 1 headline;
- 0–1 sub;
- 1 hero;
- 1 swipe cue;
- no paragraph.

### Explanation
- 1 headline;
- 2–4 information units;
- ≤3 major cards.

### Comparison
- 2 columns;
- ≤3 main comparison axes per frame.

### Data
- one main chart;
- one takeaway;
- one caveat/source.

If the editorial dossier contains more, split into another slide rather than shrink type.

---

## 11. Negative Block

Every fence:

```text
NO 3D render.
NO CGI.
NO game-engine aesthetic.
NO photoreal skin/fur.
NO glossy plastic.
NO multiple slides in one image.
NO storyboard contact sheet.
NO duplicate heads/limbs.
NO malformed hands.
NO invented source/data/percentage.
NO third-party logo.
NO unofficial BOXE DE CRIA logo substitute.
NO childlike Criago.
NO puzzle-piece autism symbol.
NO tiny unreadable body text.
NO fake scientific HUD.
NO arbitrary neon.
NO same-as-previous dependency.
NO copied influencer layout.
```

---

## 12. Post-render Gemini QA

After each generation:

### Text
- T0 exact?
- T1 exact?
- Portuguese correct?
- no hallucinated words?

### Composition
- one slide?
- 4:5?
- headline priority correct?
- negative space preserved?
- no crop of critical content?

### Character
- Criago still ratel?
- coat correct?
- jacket/aviator/patches correct?

### Brand
- owner logo intact if provided?
- no fake substitute?

### Technical
- anatomy plausible?
- diagram truthful?
- chart values unchanged?
- arrows do not imply unsupported causality?

### Style
- truly 2.5D?
- matte?
- no CGI/3D drift?

### A11Y
- body contrast?
- headline?
- color-blind backup?

P0/P1 failure:
repair/regenerate before next slide.

---

## 13. Sequential Consistency

Generate 01 → QA → 02 → QA → … → N.

Consistency comes from:
- canonical tokens;
- complete repeated prompt;
- reference assets;
- frame/background contracts;
- character lock.

Not from “remember what you did before”.

---

## 14. API/Interface Note

Google's current image-generation interfaces support explicit image aspect-ratio control including 4:5 and multiple output size tiers. Use explicit 4:5 when available rather than relying on defaults.

Generated images may carry platform provenance/watermarking such as SynthID; do not instruct the model to remove provenance.

---

## 15. Final Export Handoff

After QA:
- crop/fit master to 4:5 without moving critical content;
- target delivery 1080×1350 for Instagram;
- preserve higher-resolution master when available;
- keep sRGB;
- no sharpening halos;
- no fake upscaling detail;
- apply official logo/text finalization if required.

Caption remains outside Gemini image generation.
