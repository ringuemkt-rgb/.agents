# PALETTE MODES — BOXE DE CRIA v4.2

This file lists the named modes. Selection logic lives in `PALETTE_DECISION_ENGINE.md`; exact tokens live in `PALETTE_CANON.md`.

Field/chrome never changes identity:

- CHARCOAL `#0B0B0D`
- GRAPHITE `#121317`
- TECHNICAL GRAY `#23252B`
- WARM WHITE `#F3F0EA`
- GLOVE TAN `#C4A574`

Petroleum (`P900–P500`) is the preferred scientific atmosphere, not a replacement for BDC chrome.

## Modes

| MODE | Primary | Secondary | Typical use |
|---|---|---|---|
| EDITORIAL_DEFAULT | GOLD `#D4A017` | CYAN SIGNAL `#3EC6C9` | balanced explanation / mechanism |
| RING_LIGHT | GOLD RING `#E8B84A` | cyan only in one technical chip | hook / identity / close |
| LAB | CYAN SIGNAL `#3EC6C9` | gold only for brand/key identity | evidence / number / GRADE / data-viz |
| ALERT | BDC RED `#C62828` ≤8% | GOLD `#D4A017` | myth / risk / blocked claim |
| TERREIRO | TERRA `#B85C38` | GOLD `#D4A017` | Bahia / place / community |
| NIGHT | NIGHT BLUE `#1E3A5F` | low gold | recovery / sleep / volume |

Optional field tokens:

- P900 `#020A0E`
- P850 `#04131A`
- P800 `#06191F`
- NIGHT FIELD `#07080C`

## Mode router

Do not choose by taste alone.

Use:

```text
CONTENT JOB
+ EMOTION
+ INFOGRAPHIC GRAMMAR
+ CLAIM ROLE
+ ACCESSIBILITY
→ PALETTE MODE
```

See `PALETTE_DECISION_ENGINE.md`.

## Accent law

- max 2 active accent families per slide;
- red ≤8% and semantically justified;
- bronze is metal/evidence support, not primary headline;
- no neon RGB;
- no third accent for decoration;
- flags on canonical Criago are allowed to use their real colors.

## A11Y

Inherit `ACCESSIBILITY_CONTRAST.md`:

```text
body ≥4.5:1
headline target ≥7:1
graphics ≥3:1
no hue-only distinction
```

## Typical 8-slide modulation

Not mandatory, but useful default:

1. RING_LIGHT / DEFAULT
2. ALERT / DEFAULT
3. LAB
4. LAB
5. DEFAULT / TERREIRO
6. ALERT / DEFAULT
7. DEFAULT
8. RING_LIGHT

The arc may change if the content job or visual grammar demands it.
