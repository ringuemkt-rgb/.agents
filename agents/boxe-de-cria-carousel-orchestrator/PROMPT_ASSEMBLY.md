# PROMPT ASSEMBLY — v4.2 compatibility note

The old 12-group assembly has been superseded by `PROMPT_PROTOCOL_FIXED.md`.

Current rule:

> **One slide = one autonomous fence = 22 blocks.**

Do not use this file to shorten the prompt or collapse required locks.

## Current assembly order

```text
01 TASK / OUTPUT LOCK
02 PROJECT IDENTITY
03 EVIDENCE / CLAIM LOCK
04 CONTENT JOB / AUDIENCE
05 NARRATIVE / RETENTION
06 EXACT TEXT LOCK
07 COLOR SYSTEM
08 TYPOGRAPHY
09 FRAME LOCK
10 BACKGROUND L0–L9
11 DEPTH Z0–Z5
12 HERO / COMPOSITION
13 BIOMECHANICS and/or INFOGRAPHIC
14 VISUAL CLAIM MAP
15 CAMERA
16 LIGHTING
17 MATERIALITY
18 MESTRE CRIAGO FULL LOCK
19 OFFICIAL BRAND ASSET
20 NEGATIVE PROMPT
21 PRE-RENDER QA
22 POST-RENDER QA
```

## Upstream inputs

Before assembly, the compiler receives only the compressed editorial outputs of the investigative system:

```text
BEST CURRENT EXPLANATION
APPROVED THESIS
CERTAINTY
DIRECTNESS
APPLICABILITY
CRITICAL CAVEAT
SAFE 3-SECOND EXPLANATION
```

Do not send ACH matrix, raw DAG, GRADE worksheet, study-family ledger or search inventory to the image model unless the slide is explicitly about that method.

## Mandatory locks

- `RENDER_2_5D_LOCK.md` — no 3D/CGI/game-engine.
- `ACCESSIBILITY_CONTRAST.md` — body ≥4.5:1, headline target ≥7:1, graphics ≥3:1.
- `PALETTE_CANON.md` + `PALETTE_DECISION_ENGINE.md` — dark-field/petroleum-aware palette selection.
- `OFFICIAL_LOGO_LOCK.md` — external master asset by default.
- full Criago lock even when OFF.

## Legacy mapping

Any previous 56-field or 12-group structure is only a completeness memory for upstream reasoning. It does not define current user-visible prompt output.
