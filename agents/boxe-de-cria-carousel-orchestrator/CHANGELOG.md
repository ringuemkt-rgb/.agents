# Changelog — BOXE DE CRIA Carousel Orchestrator

## 3.4.0-portable.1 — 2026-09-16

### Cross-Study Intelligence & Unbounded Search
- Added `CROSS_STUDY_INTELLIGENCE.md`.
- Forbade self-imposed page/result caps. Search continues in batches until saturation or a documented tool limit.
- Added Evidence Inventory, Finding Atomizer and Cross-Study Linkage (constellation).
- Added Bridge Narrative that stitches independent findings before the headline.
- Added Easy Explanation Compiler: 3s / 30s / 3min in Brazilian Portuguese.
- Added Completeness Ledger (`self_imposed_page_cap_used` is a P0 failure).
- Added schemas `cross-study-link.schema.json` and `search-completeness.schema.json`.
- Hook Forge remains after Editorial Claim Lock. 56-block prompt contract unchanged.

## 3.3.0-portable.1 — 2026-09-16

### Evidence Fusion & Forensic Synthesis
- Added `EVIDENCE_SYNTHESIS.md` as the canonical deep-research protocol.
- Added three forensic depth tiers: Rapid Forensic, Deep Synthesis and Full Investigative Dossier.
- Added Study Family Resolution to detect duplicate publications and overlapping cohorts.
- Added Outcome Ontology & Harmonization to avoid mixing different constructs.
- Added study-design-specific Risk-of-Bias routing.
- Added Evidence Graph for support, contradiction, indirectness, cohort identity, mechanism, moderation and confounding.
- Added causal-map/DAG layer for causal questions.
- Added effect-normalization safeguards for OR/RR/HR/SMD/absolute effects.
- Added clinical, methodological and statistical Heterogeneity Intelligence.
- Added Contradiction Engine and Triangulation Matrix.
- Added External Validity / Applicability mapping.
- Added certainty assessment by outcome rather than one global science score.
- Added Benefit–Harm Pairing and Missing-Evidence checks.
- Added Integrated Conclusion Engine: known / likely / plausible / unknown / contradicted / what would change.
- Hook Forge now runs only after Editorial Claim Lock.

### Schemas
- Added `schemas/evidence-graph.schema.json`.
- Added `schemas/study-family-ledger.schema.json`.
- Expanded `schemas/claim-ledger.schema.json` with study identity, effect, uncertainty, heterogeneity, applicability, certainty and missing-evidence fields.

### Prompt compiler
- Preserved the **56-block autonomous prompt contract**.
- Evidence intelligence grows upstream instead of bloating each visual prompt with invisible methodology.

### Preserved
- Audience Intelligence and Problem–Audience Fit.
- Fresh Research/Fresh Attention.
- Hook Forge and Retention Engine.
- Design Style Resolver + Magnificent Science 2.5D fallback.
- Mestre Criago archetypes and Sarcasm Dial.
- Copy/paste Brazilian Portuguese caption with controlled emojis.
- Prompts by default; images only on explicit render request.

## 3.2.0-portable.1 — 2026-09-16

### Growth intelligence
- Added Audience Intelligence and Problem–Audience Fit.
- Added Fresh Attention Delta, Social Search Intelligence and Competitive Gap Miner.
- Added Topic Opportunity Matrix and Content Job Router.
- Added Content Portfolio Router and Distribution Multiplier.
- Added Experiment Ledger for account-relative learning.

### Retention
- Every slide defines `PAYOFF_NOW`, `OPEN_LOOP`, `NEXT_SLIDE_DESIRE`, `ATTENTION_RESET` and `SWIPE_HANDOFF`.
- Empty cliffhangers are rejected.
- Saveability is treated as recurring utility rather than recurring CTA decoration.

### Design
- Added Design Style Resolver.
- Explicit user-requested style is compiled into a full autonomous STYLE LOCK repeated on every slide.
- Theme-only rebuild remains mandatory for third-party references.

### Mestre Criago
- Added formal Mestre Criago voice and contextual archetype mixes.
- Added Sarcasm Dial H0–H3.
- Acid humor targets myths, ego and pseudoscience — never vulnerable people or beginners.
- Clinical/safety content defaults to H0.

### Prompt compiler
- Autonomous contract expanded from 48 to 56 blocks.
- Added audience, content job, style authority, retention and Mestre Criago mindset fields.

### Safety / integrity
- Added explicit blocks against invented trend/search-volume claims.
- Virality remains an optimization goal, never a promise.
