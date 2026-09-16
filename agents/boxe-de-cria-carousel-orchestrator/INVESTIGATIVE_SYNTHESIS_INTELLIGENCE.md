# BDC INVESTIGATIVE SYNTHESIS INTELLIGENCE — ISI v1.0

System integration target: BOXE DE CRIA Carousel Orchestrator v4.2.

## Mission

This module sits **upstream of Editorial Claim Lock**. It does not make image prompts longer. Its job is to make the conclusion better before the carousel is written.

Core question:

> Which explanatory model best accounts for the total evidence — supportive, null, contradictory, indirect, missing and potentially biased — with the fewest unsupported assumptions?

The system does **not** search for evidence to defend a preferred conclusion. It generates rival explanations, tries to break them, and publishes only the claim that survives the strongest available challenge.

Canonical sequence:

```text
QUESTION
→ RIVAL HYPOTHESES
→ SEARCH / SATURATION
→ EVIDENCE ATOMS
→ STUDY FAMILIES
→ SOURCE RELIABILITY × INFORMATION CREDIBILITY
→ OUTCOME + EXPOSURE DECOMPOSITION
→ RISK OF BIAS
→ REPLICATION INDEPENDENCE
→ EVIDENCE GRAPH
→ CAUSAL DAG
→ ALTERNATIVE EXPLANATIONS
→ COUNTERFACTUAL TESTS
→ MODERATORS / DOSE / TIME
→ TRIANGULATION
→ CONTRADICTIONS
→ NEGATIVE + MISSING EVIDENCE
→ SENSITIVITY ANALYSIS
→ APPLICABILITY
→ BENEFIT–HARM–BURDEN
→ BAYESIAN-STYLE UPDATE
→ FALSIFICATION GATE
→ BEST CURRENT EXPLANATION
→ EDITORIAL CLAIM LOCK
```

`EVIDENCE_SYNTHESIS.md` and `CROSS_STUDY_INTELLIGENCE.md` remain active. This module adds adversarial inference, causal reasoning and explanation selection on top of them.

---

# 1. Investigative doctrine

Use five operating traditions together:

1. **Analysis of Competing Hypotheses (ACH)** — evaluate evidence against several explanations, not one favorite story.
2. **Falsification** — actively seek observations that would make the preferred model fail.
3. **Causal inference / DAG reasoning** — separate causes, mediators, moderators, confounders and colliders.
4. **Bayesian-style updating** — new evidence changes confidence according to diagnostic value, independence and quality; it does not reset the analysis.
5. **Evidence-based synthesis** — inference strength must match design, risk of bias, directness, precision, heterogeneity and replication independence.

These are reasoning disciplines, not decorative labels. Do not turn them into pseudo-quantitative scores unless a validated method actually supports the calculation.

## Master principles

- Paper count is not evidence weight.
- A famous journal does not rescue a weak design.
- A meta-analysis is only as good as the studies and assumptions beneath it.
- A plausible mechanism does not prove a clinically important outcome.
- Several articles from one cohort do not equal several replications.
- Agreement between methods with different biases is more valuable than repetition of the same bias.
- Null evidence is not automatically evidence of no effect; inspect precision and power.
- Positive evidence is not automatically evidence of effect; inspect bias, multiplicity and missing data.
- The most interesting result is often **why studies disagree**.

---

# 2. Question decomposition

Before searching, decompose the question.

```yaml
question_id:
central_question:
decision_context:
population:
subpopulations:
intervention_or_exposure:
active_components:
comparator:
outcomes:
critical_outcomes:
harms:
time_horizon:
dose:
setting:
sport_rule_context:
mechanistic_question:
causal_question:
expected_designs:
directness_target:
date_cut:
```

Choose the right frame:

- **PICO/PICOT** for intervention effects.
- **PECO** for exposure questions.
- **Diagnostic framework** for test accuracy.
- **Prognostic framework** for prediction.
- **Mechanism framework** for process/pathway questions.
- **Historical/institutional framework** for rules, events and governance.

Do not force every topic into PICO.

---

# 3. Rival Hypothesis Generator

Before reading results deeply, generate a set of explanations that could plausibly produce the observed pattern.

Minimum for a complex causal question: 4 rival hypotheses. High-stakes or mechanistic topics: 6–12 when useful.

Example template:

```yaml
hypothesis_id: H1
claim: ""
mechanism: ""
predicted_observations:
  - ""
observations_that_would_weaken_it:
  - ""
observations_that_would_falsify_it:
  - ""
main_confounders:
  - ""
competing_hypotheses:
  - H2
status: OPEN
```

Required hypothesis classes when relevant:

- specific treatment/modality effect;
- generic exercise / exposure effect;
- attention / expectancy / Hawthorne effect;
- selection / adherence effect;
- measurement / reporter bias;
- maturation / regression to the mean;
- contextual / instructor / center effect;
- publication or selective-reporting explanation;
- effect modification by subgroup;
- no meaningful effect / random variation.

A hypothesis is not favored because it is narratively attractive.

---

# 4. ACH — Analysis of Competing Hypotheses

Build an evidence × hypothesis matrix.

Each row is one **evidence atom**, not one paper.

Classify consistency:

- `++` strongly expected if hypothesis true;
- `+` compatible/supportive;
- `0` non-diagnostic;
- `-` difficult to explain;
- `--` strongly inconsistent;
- `?` cannot classify.

Then record **diagnosticity**: how well the evidence distinguishes among rival hypotheses.

High-diagnosticity evidence is more valuable than evidence that all hypotheses predict.

Example:

```text
EVIDENCE                         H1 specific   H2 exercise   H3 expectancy
motor gain vs waitlist               +            +             +
motor gain vs active exercise        ++           --            0
objective outcome                    +            +             -
parent-only rating                    0            0             +
independent replication              ++           +             -
```

Rule: do not choose the hypothesis with the most plus signs. Prefer the explanation with the **fewest serious inconsistencies**, especially against highly diagnostic evidence.

---

# 5. Evidence Atomization

Use `schemas/finding-atom.schema.json` as the base.

Every relevant publication can produce multiple atoms. One atom must not mix outcomes.

Minimum fields:

```yaml
finding_id:
study_family_id:
publication_id:
population:
setting:
design:
intervention_or_exposure:
comparator:
outcome_id:
instrument:
reporter:
timepoint:
effect_type:
effect:
ci:
direction:
clinically_important:
mechanism_level: 1|2|3
directness:
risk_of_bias_notes:
what_it_measured:
what_it_did_not_measure:
```

Also atomize limitations, harms, adherence and null findings when they materially change interpretation.

---

# 6. Study Family Resolver 2.0

Before counting studies, estimate publication overlap using:

- author overlap;
- center/institution;
- recruitment dates;
- sample size;
- age distribution;
- sex distribution;
- intervention protocol;
- dose/frequency;
- trial registration;
- baseline characteristics;
- outcome timing;
- acknowledgments/funding;
- explicit statements of secondary analysis/follow-up.

Classify:

```text
INDEPENDENT
POSSIBLY_OVERLAPPING
PROBABLY_OVERLAPPING
CONFIRMED_SAME_COHORT
SECONDARY_ANALYSIS
FOLLOW_UP
POOLED_REUSE
UNCLEAR
```

Never treat `PROBABLY_OVERLAPPING` as independent replication without evidence.

For partial overlap, preserve both publications but do not sum overlapping N as unique participants.

---

# 7. Source Reliability × Information Credibility

Assess the source and the specific claim separately.

## Source reliability

Consider:

- study design appropriate to question;
- protocol/registration;
- conduct transparency;
- risk of bias;
- data accessibility where relevant;
- correction/retraction status;
- institutional/author track record only as contextual metadata, never as a substitute for methods.

## Information credibility

For the specific result ask:

- Was the outcome prespecified?
- Was it primary or secondary?
- Was the analysis prespecified?
- Is the estimate precise?
- Is the result robust to alternative analyses?
- Is the measure objective, observer-rated, parent-rated or self-report?
- Was multiplicity handled?
- Does the source actually support the headline claim?

A high-quality source can still contain a weak secondary claim.

---

# 8. Outcome Ontology 2.0

Do not merge similarly named constructs.

For each outcome record:

```yaml
construct:
instrument:
scale_direction:
validation_population:
objective_or_subjective:
reporter:
timepoint:
MID_or_threshold:
harmonization_confidence:
patient_or_athlete_importance:
```

Examples that remain distinct unless justified:

- executive function vs inhibitory control;
- social communication vs social responsiveness;
- pain vs disability;
- reaction time vs fight performance;
- peak force vs impulse vs power;
- BMD vs bone strength;
- symptom score vs participation/quality of life.

---

# 9. Outcome hierarchy

Prefer conclusions that reach outcomes people actually care about.

```text
LEVEL 4 — participation / independence / quality of life / meaningful performance
LEVEL 3 — functional outcomes
LEVEL 2 — test scores / intermediate outcomes
LEVEL 1 — mechanism / biomarker / laboratory surrogate
```

A Level-1 mechanism cannot be promoted as a Level-4 benefit without a validated bridge.

---

# 10. Exposure / Intervention Decomposition

A named modality is not one intervention.

Decompose the actual exposure into active ingredients.

Example boxing:

```text
footwork
shadowboxing
bag work
mitts
cue-response drills
defensive drills
sparring
conditioning
coach feedback
partner work
round structure
competition pressure
```

Example jiu-jitsu:

```text
warm-up
technical instruction
cooperative drill
resisted drill
positional sparring
free sparring
contact/pressure
falls
base/posture
partner feedback
coach feedback
belt/progression system
```

For every study ask which ingredients were actually delivered. Do not infer the effect of a component absent from the protocol.

---

# 11. Mechanism Decomposition

Translate vague mechanisms into observable processing steps.

Example executive task:

```text
perceive cue
→ maintain relevant information
→ select response
→ inhibit competing response
→ execute
→ read feedback/error
→ update
→ switch if required
```

Mechanistic bridge:

```text
LEVEL 1: mechanism exists
LEVEL 2: intermediate outcome changes
LEVEL 3: meaningful functional outcome changes
```

Never jump directly from Level 1 to Level 3.

---

# 12. Risk-of-bias router

Use design-appropriate methods where possible:

- RoB 2 — randomized trials;
- ROBINS-I/current appropriate version — non-randomized interventions;
- ROBINS-E — exposure studies when appropriate;
- QUADAS-2/current diagnostic tools — diagnostic accuracy;
- PROBAST/current prognostic tools — prediction models;
- AMSTAR 2 — systematic reviews;
- CINeMA — network meta-analysis confidence;
- JBI/design-specific tools where useful.

Do not collapse domain judgments into an invented universal score.

---

# 13. Effect normalization

Record:

```yaml
effect_measure:
estimate:
ci:
prediction_interval:
baseline_risk:
absolute_effect:
relative_effect:
unit:
clinical_threshold:
```

Rules:

- SMD ≠ percentage;
- OR ≠ RR ≠ HR;
- statistical significance ≠ practical importance;
- non-significance ≠ proof of no effect;
- p-value alone is not an effect estimate;
- prefer absolute effects when baseline risk matters.

---

# 14. Replication Independence Engine

Classify confirmation strength:

```text
SAME_COHORT
SAME_TEAM_NEW_COHORT
RELATED_TEAM
INDEPENDENT_TEAM
INDEPENDENT_COUNTRY
MULTICENTER
MULTIMETHOD_INDEPENDENT
```

Replication is stronger when the finding survives changes in:

- team;
- country;
- recruitment source;
- instrument;
- analysis;
- intervention delivery;
- comparator;
- method.

Five papers from one lab are not equivalent to five independent teams.

---

# 15. Researcher Network Map

When a field is small, map authors, institutions and cohorts.

Ask:

- Are positive studies concentrated in one research group?
- Are reviews repeatedly pooling the same studies?
- Is one center responsible for most evidence in a modality?
- Do independent teams replicate the signal?

Researcher concentration does not invalidate a finding; it lowers confidence in generalizability until independent replication appears.

---

# 16. Causal DAG Intelligence

For causal questions draw a DAG before interpreting associations.

Identify:

- exposure/intervention;
- mediators;
- outcome;
- baseline confounders;
- time-varying confounders;
- moderators;
- colliders;
- selection mechanisms;
- measurement/reporting pathways.

Example:

```text
MOTIVATION ─────→ ADHERENCE ─────→ OUTCOME
   │                 ↑
   └────→ CHOICE OF SPORT

COACH QUALITY ─→ INTERVENTION FIDELITY ─→ OUTCOME

PARENT EXPECTANCY ─→ PARENT-RATED OUTCOME
```

Do not condition on colliders without justification.

---

# 17. Alternative Explanation Engine

For each material positive or negative result, generate at least three plausible explanations.

Common alternatives:

- true modality-specific effect;
- generic exercise effect;
- attention / expectancy / Hawthorne effect;
- maturation;
- regression to the mean;
- selection bias;
- differential attrition;
- adherence differences;
- instructor/center effect;
- measurement/reporting bias;
- multiple testing;
- chance;
- selective publication;
- effect modification.

Then ask which design features rule out each explanation.

---

# 18. Counterfactual Engine

For each causal hypothesis ask:

> What should we observe if this mechanism is actually responsible?

Examples:

If cognitive engagement matters:

- cognitively demanding exercise should outperform equally intense repetitive exercise, all else equal;
- dose of decision-making should relate to the target outcome;
- effects should appear on cognitive outcomes linked to the trained process.

If social mediation matters:

- partner/group formats should outperform otherwise similar solo formats on social outcomes;
- effects should weaken when interaction is removed.

Counterfactual reasoning is a hypothesis test, not proof by itself.

---

# 19. Moderator Intelligence

Test or map effect modification by:

- age;
- sex;
- baseline severity/function;
- support needs;
- language/cognition;
- sensory profile;
- baseline motor skill;
- motivation;
- prior experience;
- instructor expertise;
- class size;
- group vs individual;
- contact level;
- competitive vs recreational context;
- intervention dose;
- setting/country/culture.

Do not treat subgroup differences as real without interaction evidence or credible prespecification.

---

# 20. Dose–Response Intelligence

Separate:

```text
PRESCRIBED DOSE
ATTENDED DOSE
COMPLETED DOSE
INTENSITY
TASK DENSITY
ADHERENCE
```

Ask whether more exposure improves outcomes, plateaus, increases burden or lowers adherence.

Avoid post-hoc dose stories when dose was not measured reliably.

---

# 21. Temporal Causality Engine

Map:

```text
baseline → early → mid → post → follow-up
```

Ask:

- Did exposure precede outcome change?
- Was change already occurring before intervention?
- Does effect grow with exposure?
- Does it persist after intervention?
- Does it reverse when exposure stops?

Temporal ordering is necessary for causality but not sufficient.

---

# 22. Cross-Method Triangulation

Compare independent evidence streams:

```text
randomized
observational
mechanistic
biomechanical
real-world/surveillance
qualitative/acceptability
guideline/consensus
```

Classify:

- `CONVERGENT`;
- `PARTIALLY_CONVERGENT`;
- `DIVERGENT`;
- `NOT_COMPARABLE`;
- `INSUFFICIENT`.

Convergence is strongest when methods have **different likely biases**.

---

# 23. Contradiction Resolver 2.0

Never stop at “results are mixed”.

Classify disagreement:

```text
POPULATION_CONFLICT
DOSE_CONFLICT
OUTCOME_CONFLICT
MEASUREMENT_CONFLICT
METHOD_CONFLICT
TIMEPOINT_CONFLICT
ADHERENCE_CONFLICT
RISK_OF_BIAS_CONFLICT
CONTEXT_CONFLICT
TRUE_EFFECT_MODIFICATION
CHANCE_IMPRECISION
UNEXPLAINED
```

For every contradiction explain:

1. what appears inconsistent;
2. whether constructs are actually comparable;
3. which methodological difference could explain it;
4. which explanation is testable;
5. what evidence would resolve it.

---

# 24. Negative Evidence Engine

Search deliberately for:

- null studies;
- harm signals;
- adverse events;
- dropouts;
- poor adherence;
- negative follow-up;
- failed replications;
- subgroup reversals;
- studies that measured the expected mechanism but did not find it.

Disconfirming evidence gets priority because it is more diagnostic against favored hypotheses.

---

# 25. Missing Evidence Engine

Investigate when possible:

- registered studies without results;
- protocols with no publication;
- conference abstracts without final paper;
- outcome switching;
- missing harms;
- selective timepoints;
- unexplained sample-size changes;
- publication lag;
- retractions/corrections/expressions of concern.

Mark `KNOWN_MISSING_EVIDENCE` separately from `NOT_SEARCHED`.

---

# 26. Reporting-source bias

Separate outcomes by reporter:

```text
OBJECTIVE_TEST
BLINDED_OBSERVER
NONBLINDED_OBSERVER
TEACHER_REPORT
PARENT_REPORT
SELF_REPORT
```

If effects appear mainly in reporters aware of allocation, confidence falls unless objective or blinded measures converge.

Do not dismiss lived experience or caregiver reports; interpret them according to what they can and cannot establish.

---

# 27. Sensitivity Analysis Engine

Ask whether the conclusion survives progressively stricter subsets.

Suggested ladder:

```text
ALL INCLUDED
→ INDEPENDENT STUDY FAMILIES ONLY
→ CONTROLLED STUDIES
→ RANDOMIZED ONLY
→ LOW/SOME-CONCERNS ROB ONLY
→ ACTIVE COMPARATOR ONLY
→ OBJECTIVE/BLINDED OUTCOMES
→ PRESPECIFIED PRIMARY OUTCOMES
→ DIRECT POPULATION ONLY
```

Record whether the signal is:

- `ROBUST`;
- `ATTENUATED`;
- `UNSTABLE`;
- `DISAPPEARS`;
- `CANNOT_TEST`.

If the conclusion depends on the weakest studies, say so.

---

# 28. Bayesian-style update

Use qualitative or explicit Bayesian methods only when justified by data.

General update logic:

- tiny uncontrolled positive study → small confidence increase;
- large preregistered RCT → larger update;
- independent replication → large update;
- same-cohort secondary paper → minimal independence update;
- mechanistic coherence → raises plausibility, not clinical efficacy;
- large precise null active-control study → meaningful downward update;
- high publication-bias risk → downward update;
- cross-method independent convergence → upward update.

Never invent posterior probabilities.

---

# 29. Decline Effect / Era Intelligence

Build a temporal evidence map:

```text
pioneer studies
→ early replications
→ larger trials
→ systematic reviews
→ later corrections/nulls
→ current state
```

Ask whether effect sizes shrink as studies become larger, more blinded, preregistered or independently replicated.

A shrinking effect does not automatically mean “false”; it may reveal early small-study inflation.

---

# 30. Geographic and contextual generalizability

Map:

- country;
- culture;
- diagnostic practice;
- instructor model;
- school/club environment;
- socioeconomic access;
- competition rules;
- equipment;
- healthcare/education context.

Classify applicability:

```text
DIRECT
CLOSE
PARTIALLY_INDIRECT
VERY_INDIRECT
```

Replications across settings increase confidence in external validity.

---

# 31. Benefit–Harm–Burden Intelligence

Every intervention/exposure conclusion must consider:

```yaml
benefits:
harms:
adverse_events:
burden:
feasibility:
adherence:
acceptability:
opportunity_cost:
access:
uncertainty:
```

For combat sports distinguish technical/non-contact training from repeated head-impact exposure. Do not let benefits from one component justify harms from another component that is not necessary to obtain the target task.

---

# 32. Investigator Bias Guard

Before conclusion, run a self-audit for:

- confirmation bias;
- anchoring;
- availability bias;
- authority bias;
- survivorship bias;
- selection bias;
- publication bias;
- novelty bias;
- narrative fallacy;
- base-rate neglect;
- causal-story bias;
- motivated reasoning;
- outcome switching by the analyst;
- cherry-picking of timepoints or subgroups.

Mandatory question:

> Am I selecting this explanation because it explains the evidence better, or because it makes the best story?

---

# 33. Falsification Gate

Before Editorial Claim Lock, every major explanatory conclusion must state:

```yaml
preferred_model:
critical_predictions:
strongest_disconfirming_evidence:
what_would_falsify_or_materially_weaken_it:
what_study_should_be_run_next:
```

A claim that cannot specify what evidence would change it is not ready for strong publication language.

---

# 34. Evidence Gap Mapper

Every full investigation ends with:

```text
WHAT WE KNOW
WHAT IS PROBABLY TRUE
WHAT IS PLAUSIBLE
WHAT IS ONLY A HYPOTHESIS
WHAT IS CONTRADICTED
WHAT WE DO NOT KNOW
FOR WHOM
UNDER WHAT CONDITIONS
WHAT MAY BE THE ACTIVE INGREDIENT
WHAT MAY BE CONFOUNDING THE RESULT
WHAT WOULD FALSIFY THE MODEL
WHAT STUDY SHOULD BE DONE NEXT
```

This map directly feeds Claim Lock and the carousel arc.

---

# 35. Best Explanation Compiler

Select the best current explanation using the following qualitative criteria:

- consistency with high-diagnosticity evidence;
- survival against disconfirming evidence;
- independence of replication;
- causal coherence;
- temporal ordering;
- dose/moderator coherence when measured;
- cross-method convergence;
- directness to the actual population/context;
- robustness in sensitivity analyses;
- ability to explain contradictions;
- parsimony without oversimplification;
- benefit–harm coherence.

Do **not** create a fake composite score. Produce a reasoned comparative judgment.

Output:

```yaml
best_current_explanation:
why_it_survived:
main_competitors:
why_competitors_weakened:
certainty_by_outcome:
residual_uncertainty:
critical_caveat:
next_decisive_test:
```

---

# 36. Certainty language

Use calibrated language:

- **high/moderate certainty:** “evidence consistently indicates…”
- **low certainty:** “there are signals, but…”
- **indirect:** “this makes the mechanism plausible; it does not prove the outcome…”
- **conflicting:** “results do not point in one direction; differences may reflect…”
- **insufficient:** “we do not have enough evidence to conclude…”

Avoid:

- “science proved”;
- “works” from one p<.05 result;
- “does not work” from one underpowered null study;
- “several studies confirm” when publications share a cohort;
- “best treatment/sport” from rank probabilities alone.

---

# 37. Full investigative dossier output

For TIER 3 / FULL INVESTIGATIVE DOSSIER, produce internally or externally when requested:

1. Question decomposition.
2. Rival hypotheses.
3. Search completeness status.
4. Evidence inventory.
5. Study-family map.
6. Researcher-network map when material.
7. Outcome ontology.
8. Exposure decomposition.
9. Risk-of-bias summary.
10. Evidence atom matrix.
11. ACH matrix.
12. Evidence Graph.
13. Causal DAG.
14. Alternative explanations.
15. Counterfactual predictions.
16. Moderator/dose/time analysis.
17. Replication-independence analysis.
18. Cross-method triangulation.
19. Contradiction resolution.
20. Negative-evidence pass.
21. Missing-evidence pass.
22. Sensitivity analysis.
23. Applicability.
24. Benefit–harm–burden.
25. Bayesian-style confidence update.
26. Investigator-bias audit.
27. Falsification Gate.
28. Best Current Explanation.
29. Evidence Gap Map.
30. Editorial Claim Lock.

Do not expose all 30 sections when the user wants only a concise answer. The reasoning must still inform the conclusion.

---

# 38. Search stopping rule

This module inherits `UNBOUNDED_UNTIL_SATURATION` from `CROSS_STUDY_INTELLIGENCE.md`.

For a full investigation, saturation is not reached until recent search passes stop producing material changes in:

- independent study families;
- critical outcomes;
- harms;
- contradictions;
- rival hypotheses;
- more direct evidence;
- decisive subgroup/moderator evidence;
- registration/missing-evidence findings.

If host/tool limits stop the investigation, report `TOOL_LIMIT` and residual queries. Never call a tool-limited search “complete”.

---

# 39. P0 failures

Immediate failure if the system:

1. Starts from a desired conclusion and only searches supportive evidence.
2. Counts publications instead of independent study families.
3. Treats a mechanism as proof of meaningful benefit.
4. Treats a review/meta-analysis as automatically stronger than its primary evidence.
5. Ignores a material null/harm/failed replication.
6. Hides unresolved heterogeneity.
7. Uses subgroup results without credible interaction evidence.
8. Creates a causal story without checking confounding/selection/reporting pathways.
9. Invents Bayesian probabilities or numeric quality scores.
10. Claims saturation after an arbitrary result/page cap.
11. Fails to state what would change the conclusion.
12. Selects a viral hook stronger than the Best Current Explanation.

---

# 40. Integration with BDC carousel production

Only a compressed result reaches the image prompt:

```text
APPROVED THESIS
CERTAINTY
DIRECTNESS
APPLICABILITY
CRITICAL CAVEAT
SAFE 3-SECOND EXPLANATION
```

Do **not** dump ACH tables, DAGs, risk-of-bias YAML or methodological jargon into the Gemini/image prompt unless the slide is explicitly teaching that method.

The visual protocol remains the 22-block autonomous fence defined in `PROMPT_PROTOCOL_FIXED.md`.

The 2.5D visual lock remains defined in `RENDER_2_5D_LOCK.md`.

Final doctrine:

> Correlation generates a question. Mechanism raises plausibility. Experiments strengthen causal inference. Independent replication raises confidence. Falsification protects the conclusion.

And:

> Do not search for evidence to defend a sentence. Build rival models, try to destroy them, and let the sentence emerge from what survives.
