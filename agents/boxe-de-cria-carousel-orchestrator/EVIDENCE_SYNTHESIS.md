# BDC Evidence Fusion & Forensic Synthesis Engine v1.0.0

This module is the deep-research layer for the BOXE DE CRIA Carousel Orchestrator. It is used before hook generation whenever a topic depends on scientific, clinical, biomechanical, epidemiological, historical or otherwise contested evidence.

## Mission

Do not search for papers that support a desired sentence.

Build the evidence map first, then allow the sentence to emerge from that map.

Core question:

> What is the strongest conclusion the total body of evidence allows for this question, population, context and date?

## Core principles

1. Research is not PDF counting.
2. One paper is not one unit of truth.
3. Several papers may come from the same cohort.
4. A meta-analysis does not erase bias, heterogeneity or indirectness.
5. A weak systematic review does not automatically outrank a strong primary study.
6. Mechanistic plausibility does not prove a clinical or sport-performance outcome.
7. Independent convergence across methods is more informative than repetition of the same bias.
8. Absence of evidence is not automatically evidence of absence.
9. Certainty is assessed by outcome, not as one global score for the topic.
10. Every conclusion must state its limits and what evidence could change it.

## Methodological anchors

Use these frameworks when applicable and available:

- PRISMA 2020 for transparent identification, selection and synthesis reporting;
- Cochrane Handbook principles for evidence synthesis, heterogeneity, sensitivity and interpretation;
- GRADE for certainty of evidence by outcome;
- RoB 2 for randomized trials;
- ROBINS-I / current appropriate ROBINS version for non-randomized intervention studies;
- ROBINS-E when appropriate for observational exposure studies;
- AMSTAR 2 for systematic-review methodology;
- JBI critical-appraisal tools for additional study designs;
- CINeMA for network meta-analysis confidence;
- design-specific validated tools when the question is diagnostic, prognostic, qualitative or measurement-focused.

Never turn these tools into one universal numeric quality score.

## 1. Question Decomposition

Before searching, create:

```yaml
central_question:
claim_target:
population:
subpopulations:
intervention_or_exposure:
comparator:
outcomes:
critical_outcomes:
secondary_outcomes:
harms:
setting:
time_horizon:
dose:
sport_or_rule_context:
study_designs_expected:
directness_target:
decision_context:
date_cut:
```

If a critical field is ambiguous, preserve that ambiguity explicitly rather than guessing.

## 2. Forensic Tier Router

### TIER 1 — RAPID FORENSIC
Use for simple, low-risk evergreen content.

Minimum:
- one or two recent high-quality syntheses;
- critical primary sources;
- contradiction search;
- Fact Lock.

### TIER 2 — DEEP SYNTHESIS
Use for important sports-science, biomechanics, performance and evidence-heavy topics.

Add:
- study-family resolution;
- multiple reviews and key primaries;
- risk-of-bias reasoning;
- Evidence Graph;
- heterogeneity;
- applicability;
- certainty by outcome.

### TIER 3 — FULL INVESTIGATIVE DOSSIER
Use for clinical, safety, children, neurodevelopment, concussion, injury, vulnerable populations, major controversies or high-impact claims.

Add all available layers:
- overlap control;
- missing evidence;
- causal map/DAG;
- sensitivity reasoning;
- replication independence;
- benefit-harm balance;
- temporal evidence history;
- what-would-change-the-conclusion analysis.

## 3. Source Universe Map

Choose sources for their fitness to the question, not by a rigid pyramid.

### Primary evidence
- randomized trials;
- cohort studies;
- case-control;
- cross-sectional studies;
- registries/surveillance;
- biomechanical experiments;
- physiological experiments;
- qualitative studies;
- archival documents;
- official rules/results/records.

### Secondary evidence
- systematic reviews;
- pairwise meta-analyses;
- network meta-analyses;
- umbrella reviews;
- evidence maps;
- guidelines/consensus documents.

### Verification evidence
- trial registries;
- protocols;
- statistical analysis plans;
- supplementary files;
- corrections/retractions;
- DOI/PubMed/Crossref metadata;
- official federation or institutional records.

### Contextual evidence
- high-quality narrative reviews;
- textbooks/handbooks;
- institutional educational material;
- expert commentary.

Contextual evidence should not replace a better primary source when that source is available.

## 4. Search Mesh

Use several search passes.

### Pass A — Anchor
Find the newest relevant synthesis, guideline/consensus, foundational study and official source.

### Pass B — Forward
Find important studies published after the anchor synthesis.

### Pass C — Backward
Trace foundational and repeatedly cited primary studies.

### Pass D — Contradiction
Deliberately search for:
- null results;
- opposite effects;
- failed replication;
- subgroup reversal;
- methodological criticism;
- harms;
- letters/corrections.

### Pass E — Missing evidence
Look for:
- registered but unpublished studies;
- protocols without results;
- selective outcome reporting;
- abstract-only positive results;
- publication lag.

### Pass F — Population/context mismatch
Search for evidence closer to the actual age, sport, rules, dose, skill level or clinical population.

### Pass G — Fresh Research Delta
Look specifically at the last 24–36 months when the field could have materially changed.

## 5. Study Identity Resolution

Before saying “X studies”, determine whether publications are independent.

For each study family record:

```yaml
study_family_id:
publication_id:
trial_registration:
cohort_name:
recruitment_site:
recruitment_dates:
sample_n:
population_signature:
intervention_signature:
outcome_signature:
followup:
primary_or_secondary_analysis:
overlap_probability:
notes:
```

Detect:
- protocol + final paper;
- conference abstract + full article;
- subanalysis;
- follow-up of same participants;
- partially overlapping samples;
- reused pooled datasets;
- multiple papers from the same cohort.

P0 failure: counting the same participants as independent replication.

## 6. Outcome Ontology & Harmonization

Do not combine outcomes just because the labels sound similar.

For each outcome record:

```yaml
outcome_id:
construct:
instrument:
scale_direction:
timepoint:
minimal_important_difference:
objective_or_subjective:
validated_for_population:
conversion_required:
harmonization_confidence:
```

Do not automatically merge:
- executive function with inhibitory control;
- pain with disability;
- impact force with fight performance;
- social communication with quality of life;
- bone mineral density with bone strength.

## 7. Study-Design Lens

The design determines the inference.

### Randomized trial
Can support causal intervention inference when conduct, adherence, missing data and analysis are adequate.

### Cohort
Can support temporal association and risk estimates; confounding remains central.

### Cross-sectional
Supports contemporaneous association only; temporal direction is unresolved.

### Case-control
Useful for uncommon outcomes; selection and recall bias require attention.

### Mechanistic / biomechanical
Supports plausibility and process, not long-term clinical benefit on its own.

### Qualitative
Supports experience, acceptability, barriers and meaning, not population prevalence or treatment-effect size.

### Registry/database/ecological
Useful for real-world patterns; avoid individual-level causal inference when design does not support it.

## 8. Risk-of-Bias Router

Route appraisal by design and use the most appropriate current validated tool available.

Typical mapping:
- RCT → RoB 2;
- non-randomized intervention → ROBINS-I / appropriate current version;
- observational exposure → ROBINS-E when applicable;
- systematic review → AMSTAR 2;
- network meta-analysis → CINeMA plus missing-evidence assessment;
- additional designs → relevant JBI or design-specific instrument.

Record judgments by domain. Do not reduce methodological quality to a simplistic total score.

## 9. Evidence Graph

Represent the body of evidence as a graph, not just a table.

### Node types
QUESTION, CLAIM, STUDY_FAMILY, PUBLICATION, POPULATION, INTERVENTION, EXPOSURE, OUTCOME, MECHANISM, MODERATOR, CONFOUNDER, SOURCE, GUIDELINE, REVIEW, HARM, UNCERTAINTY.

### Edge types
SUPPORTS, CONTRADICTS, PARTIALLY_SUPPORTS, INDIRECTLY_SUPPORTS, DOES_NOT_ADDRESS, SAME_COHORT, SUPERSEDES, REANALYZES, MEDIATES, MODERATES, CONFOUNDS, MEASURES, REPORTS, DUPLICATES, EXTENDS_FOLLOWUP, LOWERS_CERTAINTY, INCREASES_PLAUSIBILITY.

Strong convergence should ideally include independent teams, independent samples, different methods and coherent outcomes.

## 10. Causal Map / DAG Layer

When causality matters, map conceptually:

```text
INTERVENTION / EXPOSURE
        ↓
MEDIATOR(S)
        ↓
OUTCOME

CONFOUNDER → exposure + outcome
MODERATOR → changes effect magnitude/direction
COLLIDER → do not condition casually
```

Ask:
1. Is temporality established?
2. Is there dose-response evidence?
3. Are objective outcomes consistent?
4. Could confounders explain the association?
5. Is the proposed mechanism coherent?
6. Is there experimental convergence?
7. Is there reversibility/dechallenge evidence when relevant?
8. Do independent methods converge?

Do not label this checklist as proof of causality.

## 11. Mechanism–Outcome Bridge

Keep three levels separate:

1. MECHANISM EXISTS;
2. MECHANISM CHANGES AN INTERMEDIATE OUTCOME;
3. ATHLETE/PATIENT-IMPORTANT OUTCOME CHANGES.

Never automatically jump from level 1 to level 3.

Example: greater muscle activation does not by itself prove fewer injuries or better fight performance.

## 12. Effect Normalization

Record:

```yaml
effect_type:
raw_effect:
relative_effect:
absolute_effect:
standardized_effect:
confidence_interval:
prediction_interval:
p_value:
baseline_risk:
direction_beneficial:
clinical_importance:
```

Rules:
- standardized effect size is not a percentage;
- OR is not RR;
- statistical significance is not clinical importance;
- non-significance is not proof of no effect;
- an estimate without uncertainty is incomplete;
- prefer absolute effect when the decision depends on baseline risk.

## 13. Heterogeneity Intelligence

Separate:

### Clinical heterogeneity
Age, sex, severity, experience, modality, rules, dose, comorbidity, baseline.

### Methodological heterogeneity
Design, measurement instrument, comparator, follow-up, case definition, analysis.

### Statistical heterogeneity
Direction, I², tau², prediction intervals, outliers, small-study effects when available.

If heterogeneity is large and not adequately explained, do not hide it behind one pooled average. Prefer stratified or narrative synthesis when appropriate.

## 14. Synthesis Router

Choose the synthesis that matches the evidence:

- narrative synthesis;
- pairwise meta-analysis;
- network meta-analysis;
- dose-response;
- diagnostic synthesis;
- prognostic synthesis;
- qualitative synthesis;
- mechanistic triangulation;
- umbrella synthesis.

Never fabricate a meta-analysis from insufficient or incompatible data.

## 15. Umbrella Overlap Control

When several reviews cover the same topic:

- map which primary studies occur in each review;
- identify duplicated cohorts;
- do not add review sample sizes as if unique participants;
- compare review recency, completeness and methodology;
- use AMSTAR 2 reasoning;
- estimate overlap/CCA when it materially helps.

“Twenty reviews” does not mean twenty independent confirmations.

## 16. Contradiction Engine

For every critical claim create:

```yaml
claim:
supporting_evidence:
contradicting_evidence:
difference_in_population:
difference_in_dose:
difference_in_outcome:
difference_in_time:
difference_in_method:
risk_of_bias_difference:
possible_effect_modifier:
possible_explanation:
unresolved_conflict:
```

Potential explanations:
1. not actually the same outcome;
2. different population;
3. different dose;
4. different follow-up;
5. risk-of-bias difference;
6. imprecision;
7. real effect heterogeneity;
8. selective publication;
9. extraction/interpretation error.

Try to explain the disagreement before voting by majority.

## 17. Triangulation Matrix

Cross-check six evidence lines when relevant:

- experimental;
- observational;
- mechanistic;
- real-world/surveillance;
- qualitative/acceptability;
- guideline/consensus.

Classify convergence as:
- CONVERGENT;
- PARTIALLY_CONVERGENT;
- DIVERGENT;
- NOT_COMPARABLE;
- INSUFFICIENT.

Triangulation is not vote counting.

## 18. External Validity / Applicability

Ask whether the evidence applies to the actual content question.

Map:
- age;
- sex;
- skill level;
- sport/modality;
- rules;
- amateur/pro;
- contact/non-contact;
- equipment;
- setting;
- country;
- time period;
- baseline health;
- neurodevelopmental/clinical profile;
- dose/frequency;
- supervision.

Output:
- DIRECT;
- CLOSE;
- PARTIALLY_INDIRECT;
- VERY_INDIRECT.

## 19. Certainty by Outcome

Use GRADE-style reasoning when appropriate:
- risk of bias;
- inconsistency;
- indirectness;
- imprecision;
- publication/missing-evidence bias.

Potential upgrades when valid may include large magnitude, dose-response or residual confounding likely to reduce rather than create the observed effect.

Output by outcome:
- HIGH;
- MODERATE;
- LOW;
- VERY_LOW.

Do not issue one global certainty label when outcomes differ.

## 20. Missing Evidence / Publication Bias

Investigate when material:
- trial registries without results;
- selective reporting;
- outcome switching;
- small-study effects;
- publication lag;
- positive conference abstracts without full publication;
- missing harms.

Published evidence can look consistent while important evidence is missing.

## 21. Replication & Independence

Classify:
- SAME_TEAM;
- PARTIALLY_INDEPENDENT;
- INDEPENDENT;
- MULTICENTER;
- EXTERNAL_REPLICATION.

Repeated reports by one group in correlated samples do not carry the same epistemic weight as independent replication.

## 22. Benefit–Harm Pairing

For any intervention or practice map:

```yaml
benefits:
harms:
burden:
feasibility:
adherence:
acceptability:
opportunity_cost:
uncertainty:
```

Do not celebrate a benefit while suppressing a relevant harm or burden.

## 23. Temporal Intelligence

Build an evidence timeline when useful:
- initial hypothesis;
- foundational study;
- replications;
- first review;
- meta-analyses;
- higher-quality later evidence;
- corrections/retractions;
- current state.

Look for declining effects as samples/methods improve and for outdated claims that survived after the evidence changed.

## 24. Integrated Conclusion Engine

Do not finish with a single “yes/no”.

Produce:

### WHAT WE KNOW
Well-supported findings.

### WHAT IS PROBABLY TRUE
Consistent but not definitive findings.

### WHAT IS PLAUSIBLE
Mechanistic or indirect evidence.

### WHAT WE DO NOT KNOW
Real uncertainty/gaps.

### WHAT THE EVIDENCE CONTRADICTS
Claims not supported or contradicted.

### WHO IT APPLIES TO
Population/context/directness.

### UNDER WHAT CONDITIONS
Dose, supervision, rules, environment or relevant modifiers.

### WHAT WOULD CHANGE THE CONCLUSION
Specify the type of future evidence that would meaningfully update the verdict.

## 25. Verdict Language Compiler

Translate methodological rigor into clear Brazilian Portuguese.

Examples:

High/moderate confidence:
> “Os estudos indicam de forma consistente que…”

Low confidence:
> “Há sinais de benefício, mas ainda não dá para afirmar com segurança…”

Indirect evidence:
> “Isso torna a hipótese plausível, mas não prova que o mesmo efeito aconteça no boxe.”

Conflict:
> “Os resultados não apontam todos na mesma direção.”

Insufficient evidence:
> “Não encontramos evidência suficiente para concluir.”

Avoid “a ciência provou” unless the evidence and wording truly justify an unusually strong statement.

## 26. Evidence Synthesis Ledger

Master structure:

```yaml
question:
date_cut:
search_domains:
source_map:
study_families:
outcome_ontology:
risk_of_bias:
effect_table:
heterogeneity:
contradictions:
triangulation:
applicability:
certainty_by_outcome:
benefit_harm:
missing_evidence:
research_delta:
current_consensus:
unknowns:
what_would_change_conclusion:
editorial_claims_allowed:
editorial_claims_forbidden:
visualization_rules:
```

## 27. Evidence-to-Visual Outputs

The evidence dossier may generate:
- Evidence Ladder;
- Causal Chain;
- Direct vs Indirect Map;
- Study Family Map;
- Outcome Matrix;
- Contradiction Matrix;
- Timeline of Evidence;
- Forest Plot;
- Risk-of-Bias Grid;
- Applicability Map;
- Benefit–Harm Balance;
- What We Know / Do Not Know split;
- Mechanism–Outcome Bridge.

Every visual must state whether it is quantitative, qualitative or conceptual.

## 28. P0 Forensic Failures

Block publication when the system:

1. counts duplicate publications as independent studies;
2. sums overlapping samples;
3. trusts a review without evaluating its methodology;
4. treats indirect evidence as direct;
5. ignores a critical contradictory outcome;
6. hides important heterogeneity;
7. uses mechanism as proof of clinical benefit;
8. treats statistical significance as clinical importance;
9. converts SMD to percent without a valid transformation;
10. mixes prevalence and incidence;
11. treats OR, RR and HR as interchangeable;
12. treats cross-sectional association as causal;
13. ignores retraction/correction;
14. ignores relevant adverse effects;
15. claims superiority from a network-meta-analysis ranking without uncertainty;
16. says “X studies” without resolving study families;
17. treats a guideline as primary research;
18. claims consensus where unresolved conflict exists;
19. extrapolates to another population without declaring indirectness;
20. invents a pooled estimate or meta-analysis.

## 29. Integration with Carousel Production

The forensic layer runs before hook generation:

```text
QUESTION
→ FORENSIC TIER
→ SEARCH MESH
→ STUDY IDENTITY RESOLUTION
→ OUTCOME ONTOLOGY
→ RISK OF BIAS
→ EVIDENCE GRAPH
→ CAUSAL / MECHANISTIC MAP
→ EFFECT NORMALIZATION
→ HETEROGENEITY
→ CONTRADICTION ENGINE
→ TRIANGULATION
→ APPLICABILITY
→ CERTAINTY BY OUTCOME
→ BENEFIT × HARM
→ MISSING EVIDENCE
→ INTEGRATED CONCLUSION
→ EDITORIAL CLAIM LOCK
════════════════════════
ONLY THEN:
→ ANGLE
→ HOOK
→ STORY
→ DESIGN
→ AUTONOMOUS PROMPTS
```

No hook may be selected before Editorial Claim Lock.

## 30. Efficiency rule

Deeper evidence synthesis must improve the reasoning **upstream**. It must not bloat every visual prompt with invisible methodology.

The slide prompt should receive only what it needs:
- approved factual thesis;
- evidence state;
- direct vs indirect status;
- relevant certainty/applicability;
- exact verified numbers;
- caveat;
- allowed/prohibited visualization;
- source footer;
- Rigor Card.

Final rule:

> **Do not search for a sentence to prove. Build the evidence map and let the sentence emerge from it.**
