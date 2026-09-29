# BDC PALETTE DECISION ENGINE — DARK FIELD v2.0

Purpose: choose a coherent dark palette by content job, evidence role, emotion, infographic grammar, accessibility and perceptual hierarchy.

This engine selects tokens from PALETTE_CANON.md. It does not invent "brain colors".

## 1. Doctrine

Preference:
azul-petróleo + charcoal + deep navy.

Identity:
- charcoal/graphite = house/chrome;
- warm white = truth/readability;
- gold = identity/ownership;
- cyan = method/evidence;
- bronze = metal/hairline;
- red = alert/blocked claim;
- petroleum = scientific depth;
- terra = place/Bahia.

Color semantics are BDC conventions, not universal psychological laws.

## 2. Field stack

```text
L0 ATMOSPHERE: P900 #020A0E or P850 #04131A
L1 VIGNETTE: CHARCOAL #0B0B0D
L2 STRUCTURE: GRAPHITE #121317
L3 CARDS: TECHNICAL GRAY #23252B
L4 TEXT: WARM WHITE #F3F0EA
L5 ACCENT 1
L6 ACCENT 2
```

## 3. Modes

EDITORIAL_DEFAULT
- P900/P850 + charcoal;
- gold + cyan;
- calm authority.

LAB
- P900→P800;
- cyan primary;
- gold only identity;
- measurement/evidence.

RING_LIGHT
- charcoal + dark petroleum;
- gold ring primary;
- one cyan chip;
- cover/identity.

ALERT
- charcoal/P900;
- red ≤8%;
- gold rail;
- warning/correction.

TERREIRO
- charcoal/P900;
- terra + gold;
- place/community.

NIGHT
- #07080C + #1E3A5F;
- restrained gold/cyan;
- recovery/quiet.

## 4. Perceptual selection rule

Choose palette by:
`CONTENT JOB + GRAMMAR + HIERARCHY + CONTRAST + BRAND`.

Do NOT choose by:
- “red sells”;
- “blue creates trust”;
- “green calms the brain”.

Color psychology is context-dependent; contrast and learned brand semantics have priority.

## 5. Accent budget

- neutral/environment: 80–88%;
- accent 1: 8–12%;
- accent 2: 4–6%;
- red: ≤8%.

No third accent unless real flag color in canonical asset.

## 6. Headline

Default:
- #F3F0EA;
- one keyword gold or cyan;
- red only one large alert word;
- bronze not AAA headline.

## 7. Data-viz

Use multiple channels:
- hue + label;
- hue + shape;
- hue + dash;
- position.

Never hue-only.

No 3D bars, perspective magnitude or decorative gradients.

## 8. Accessibility

Inherit ACCESSIBILITY_CONTRAST.md.

```text
body ≥4.5:1
headline target ≥7:1
meaningful graphics ≥3:1
```

## 9. Sunlight/mobile robustness

Prefer luminance contrast strong enough to survive:
- phone brightness variation;
- outdoor viewing;
- compressed screenshots.

If a distinction disappears in grayscale, add label/shape.

## 10. Fence insertion

```text
PALETTE DECISION:
CONTENT JOB:
EMOTION:
GRAMMAR:
MODE:
FIELD:
ACCENT 1:
ACCENT 2:
COLOR SEMANTICS:
ACCENT BUDGET:
A11Y:
GRAYSCALE/COLOR-BLIND BACKUP:
NO universal-color psychology.
```

## 11. Fail

Reject if:
- petroleum erases BDC chrome;
- 3+ accents compete;
- cyan becomes sci-fi neon;
- red decorative;
- gold on tan/terra without verified contrast;
- chart depends only on hue;
- color claim is presented as neuroscience;
- headline readability is sacrificed for mood.
