# BDC PALETTE DECISION ENGINE — DARK FIELD v1.0

Purpose: choose a coherent dark palette for each slide based on **content job, evidence role, emotion, infographic grammar and accessibility**, while preserving BOXE DE CRIA identity.

This engine does not invent new brand colors. It selects and combines tokens from `PALETTE_CANON.md`.

## 1. Base doctrine

The user preference is dark visual fields, especially **azul-petróleo**, charcoal and deep navy.

BDC identity must still read immediately:

- charcoal/graphite = structural chrome / house;
- warm white = truth/readability;
- gold = identity / ownership / hero emphasis;
- cyan = method / science / information;
- bronze = evidence metal / hairline, not primary headline;
- red = stop / risk / blocked claim, never decoration;
- petroleum = atmosphere / scientific depth;
- terra = place / Bahia;
- night blue = recovery / volume / nocturnal mood.

## 2. Field architecture

Default dark field stack:

```text
L0 ATMOSPHERE: P900 #020A0E or P850 #04131A
L1 VIGNETTE: CHARCOAL #0B0B0D
L2 STRUCTURE: GRAPHITE #121317
L3 CARDS: TECHNICAL GRAY #23252B with dark transparency equivalent
L4 TEXT: WARM WHITE #F3F0EA
L5 ACCENT 1: selected by mode
L6 ACCENT 2: selected by mode
```

Petroleum is allowed to dominate the atmosphere, but the frame/chrome should retain BDC charcoal/graphite so the carousel does not look like a generic science app.

## 3. Mode selection by editorial job

### EDITORIAL_DEFAULT
Use when: explanation, mechanism, balanced authority.

- field: P900/P850 + charcoal chrome;
- accent 1: GOLD #D4A017;
- accent 2: CYAN SIGNAL #3EC6C9;
- mood: calm authority.

### LAB
Use when: evidence, measurement, study, uncertainty, data-viz.

- field: P900 → P800 petroleum;
- accent 1: CYAN SIGNAL #3EC6C9;
- accent 2: GOLD only for wordmark/key identity;
- bronze: evidence chip/hairline only;
- mood: precision.

### RING_LIGHT
Use when: cover, identity, final synthesis, hero quote.

- field: charcoal + very dark petroleum depth;
- accent 1: GOLD RING #E8B84A;
- accent 2: cyan only in one technical chip;
- mood: pride / authority.

### ALERT
Use when: myth, risk, blocked claim, correction.

- field: charcoal / P900;
- accent 1: BDC RED #C62828, ≤8% of area;
- accent 2: GOLD #D4A017 for brand rail;
- warm white carries most copy;
- mood: controlled warning, never panic.

### TERREIRO
Use when: Bahia, place, community, local application.

- field: charcoal + P900;
- accent 1: TERRA #B85C38;
- accent 2: GOLD #D4A017;
- optional MATA #2D5016 on one prop only;
- mood: rooted / local.

### NIGHT
Use when: recovery, sleep, training volume, quiet reflection.

- field: NIGHT FIELD #07080C + NIGHT BLUE #1E3A5F;
- accent 1: low GOLD #C9971C/#D4A017 family according to canon;
- accent 2: restrained cyan chip;
- mood: quiet technical.

## 4. Mode selection by infographic grammar

| Grammar | Preferred mode | Reason |
|---|---|---|
| CINE_COVER | RING_LIGHT / DEFAULT | stop + identity |
| HUB | LAB / DEFAULT | mechanism / nodes |
| SPLIT | LAB vs ALERT or cyan vs gold | comparison |
| PATH | DEFAULT / TERREIRO | temporal ribbon / journey without cliché |
| FLAT_CHART | LAB | data integrity |
| STACK_STEPS | DEFAULT | protocol/saveability |
| CLIPBOARD | LAB / DEFAULT | evidence/system |
| ISO_FLOW | DEFAULT / LAB | process, but always 2.5D not engine |

Never choose palette only because it “looks cool”. The palette must reinforce the claim role.

## 5. Emotion × color map

This is brand semantics, not universal color psychology.

```text
CALMA_DE_MESTRE → petroleum + warm white + cyan
CURIOSIDADE → petroleum + cyan + one gold keyword
ORGULHO → charcoal + gold + warm white
RAIVA_UTIL → charcoal + restrained red + warm white
URGENCIA_DE_CORPO → charcoal/petroleum + amber + red micro-alert
PERTENCIMENTO/BAHIA → charcoal + terra + gold
```

## 6. Accent budget

Default visual area:

- dark neutrals/environment: 80–88%;
- accent 1: 8–12%;
- accent 2: 4–6%;
- red: ≤8%, only when semantically justified.

No third accent unless it is a real flag color inside the canonical Criago patch/flag.

## 7. Headline color logic

Primary headline defaults:

- WARM WHITE #F3F0EA;
- one keyword may be GOLD #D4A017 or CYAN SIGNAL #3EC6C9;
- never bronze as the main AAA headline;
- red only for one large warning word;
- max two colored lines/keywords total.

## 8. Data-viz palette

Quantitative graphics remain flat/orthographic.

Use:

- primary series: cyan + shape/label;
- comparator: warm white / gold + different shape/line style;
- risk/blocked threshold: red with symbol/label;
- uncertainty: line/hatch/opacity + textual cue, never color alone.

Never use 3D bars, gradients as magnitude, perspective or hue-only legends.

## 9. Accessibility gate

Inherit `ACCESSIBILITY_CONTRAST.md`.

Required:

```text
body ≥4.5:1
headline target ≥7:1
meaningful graphics ≥3:1
no hue-only distinction
```

Known safe/high-performing dark-field pairings:

- warm white on charcoal;
- cyan on charcoal;
- gold on charcoal.

Known caution/fail-prone:

- bronze as AAA headline;
- red body text;
- gold on tan/terra;
- white on gold plate;
- cyan on lighter petroleum without verification.

## 10. Viral-design principle

Color does not create virality. It improves:

- stop power;
- recognition;
- readability;
- semantic memory;
- screenshot/share legibility.

The palette may amplify a strong idea, but it must never replace Claim Lock, SHARE_LINE or useful information.

## 11. Fence insertion

Every block 07 should contain:

```text
PALETTE DECISION:
CONTENT JOB: [job]
EMOTION: [emotion]
GRAMMAR: [grammar]
MODE: [mode]
FIELD: [HEX]
ACCENT 1: [HEX + semantic role]
ACCENT 2: [HEX + semantic role]
ACCENT BUDGET: [area rules]
A11Y: body ≥4.5:1 | headline target ≥7:1 | graphics ≥3:1
NO hue-only legend. NO third accent. NO neon RGB.
```

## 12. QA fail

Reject if:

- the slide looks like another brand because petroleum replaced all BDC chrome;
- 3+ accent families compete;
- cyan glow becomes neon sci-fi;
- gold is used on tan/terra without adequate contrast;
- red is decorative rather than semantic;
- a chart depends only on color;
- headline readability degrades for mood;
- palette contradicts content role (e.g. ALERT red on a calm neutral evidence slide without risk claim).
