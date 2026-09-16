# Gemini Image Production — BDC v4.2

Use this file when the final image model is Gemini/Imagen. The research/investigative engine runs before this stage.

## Contract

1. One code fence per slide.
2. One slide image per generation.
3. Each fence = **22 autonomous blocks** from `PROMPT_PROTOCOL_FIXED.md`.
4. Do not depend on prior images/chat history.
5. 4:5, 2160×2700 working intent, sRGB.
6. RENDER = editorial semi-vector **2.5D only**.
7. Full Criago lock even when `VISIBILITY: OFF`.
8. Apply `ACCESSIBILITY_CONTRAST.md`, `PALETTE_CANON.md`, `PALETTE_DECISION_ENGINE.md` and `OFFICIAL_LOGO_LOCK.md`.
9. Do not send ACH tables, DAGs, GRADE YAML or evidence inventory to Gemini unless the slide explicitly teaches those methods.

## TASK lock

```text
TASK / OUTPUT LOCK:
Generate ONE single carousel slide image, not a grid, not a storyboard, not variants.
Output: one 4:5 vertical image, 2160x2700 intent, sRGB, mobile-first, print-sharp labels.
Do not reference any previous image. This fence is fully autonomous.
RENDER LOCK: 2.5D GRAPHIC EDITORIAL ONLY.
All figures, Criago, gym, cards, nodes, gloves and props: premium semi-vector illustration.
2–3 cel-shading levels. Matte. Print grain 1.5–2%. Contact shadow.
NO 3D render, NO CGI, NO Blender, NO Unreal, NO photoreal skin/fur, NO plastic shader, NO game-engine aesthetic.
```

## Order

`Best Current Explanation → Claim Lock → storyboard → GEMINI_SLIDE_01..N → generate 01 → QA → 02..N → caption outside Gemini`.

## Minimum negative block

```text
NO 3D render, CGI, game-engine, photoreal skin/fur, plastic shader,
NO extra limbs/fingers, unreadable microtext, watermark, Instagram UI chrome,
NO third-party brand, copied influencer layout, medical gore, childlike mascot,
NO puzzle-piece autism cliché, fake study/data, invented percentages,
NO same-as-previous dependency, NO collage of multiple slides,
NO unofficial BOXE DE CRIA logo substitute.
```

## Accessibility

Every fence must carry:

```text
A11Y: body text ≥4.5:1 | headline target ≥7:1 | meaningful graphics ≥3:1.
No hue-only legend. Body defaults to #F3F0EA on dark field.
```

## Official logo

Normal production:

```text
Use the owner-supplied BOXE DE CRIA official logo asset in finalization.
Do not generate, redesign or restyle it.
If unavailable, reserve space rather than inventing a substitute unless the user explicitly requests reconstruction under OFFICIAL_LOGO_LOCK.md.
```

## Long-prompt handling

If the image model truncates or ignores a long fence, use a new generation context for each slide rather than deleting mandatory locks. Never solve context pressure by writing “same as previous”.
