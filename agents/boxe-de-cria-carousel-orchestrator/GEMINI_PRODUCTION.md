# Gemini Image Production — prompts 1:1 ultra-detalhados

Descarregar o carrossel BDC no Gemini (Gemini Image / Imagen via Gemini) sem depender do slide anterior.

## Contrato

1. Um bloco de código por slide.
2. Copiar UM bloco → colar no Gemini → gerar → só então o próximo.
3. Proibido: mesmo do anterior / continue a série / estilo canónico.
4. Cada bloco = 56 campos de SYSTEM_PROMPT.md.
5. 4:5, 2160×2700, sRGB.
6. Character Lock do Criago inteiro mesmo se VISIBILITY OFF.

## TASK lock (bloco 1 de cada prompt)

```text
TASK / OUTPUT LOCK:
Generate ONE single carousel slide image, not a grid, not a storyboard, not 4 variants.
Output: one 4:5 vertical image, 2160x2700 intent, print-sharp labels.
Do not ask follow-up questions. Do not reference any previous image.
Ignore chat history for style. This block is the only source of truth.
```

## Ordem do operador

Claim Lock → storyboard → GEMINI_SLIDE_01..N → colar 01 → QA → 02..N → legenda fora do Gemini.

## Negative mínimo (bloco 56)

```text
no photoreal skin pores, no 3D plastic CGI, no extra limbs, no extra fingers,
no unreadable microtext, no watermark, no Instagram UI chrome, no other gym brand,
no copied influencer layout, no medical gore, no childlike mascot,
no "same style as previous", no collage of multiple slides
```

Não mandar YAML GRADE / DOI / inventory para o Gemini. Só tese + Rigor Card + visual.
Se o chat recusar prompt longo: um slide por conversa nova.
