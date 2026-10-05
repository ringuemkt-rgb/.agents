# BDC AI Forensic Intelligence Manager v1.0

## Purpose
Adversarial AI orchestration for difficult themes. It does not replace sources, statistics or professional judgment. It decomposes research into independent roles and forces an Evidence Governor to reconcile them.

## Council
1. SOURCE SCOUT — primary/high-authority discovery.
2. IDENTITY AUDITOR — study families, duplicate cohorts, document editions and records.
3. METHODS AUDITOR — design, population, outcome, denominator, bias, what-not-measured.
4. CONTRADICTION HUNTER — rival hypotheses, nulls, counterexamples.
5. MECHANISM BRIDGE AUDITOR — mechanism vs observed outcome vs didactic model.
6. SAFETY REVIEWER — T3 only.
7. VISUAL EVIDENCE AUDITOR — visual proof that cannot overclaim.
8. EDITORIAL TRANSLATOR — audience language only after claims are locked.
9. EVIDENCE GOVERNOR — adjudicates conflicts and produces Best Current Explanation + Claim Ledger.

## Execution in ChatGPT
When this skill is active, ChatGPT itself can perform these roles sequentially using available research/file tools. No second model is required merely to claim the council is active.

For external automation, src/intelligence/forensic-ai.ts exposes an AiProvider interface so an approved LLM provider can be plugged in later.

## Governor cannot
- invent a citation;
- convert absence into zero;
- convert mechanism into outcome;
- count overlapping reviews as independent confirmation;
- accept a visual that says more than the claim.

## Required output
BEST CURRENT EXPLANATION
CLAIM LEDGER
SOURCE / STUDY-FAMILY LEDGER
CONTRADICTION MAP
EVIDENCE GAPS
BLOCKED CLAIMS
VISUAL PROOF MAP
FRESHNESS / RECHECK DATE
FINAL GATE
