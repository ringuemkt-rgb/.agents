# Runbook — evidence-first carousel → Gemini

System version: 3.5.0-portable.1

1. Audience + problem
2. PICOT
3. Forensic tier 1/2/3
4. Unbounded search (OpenAlex/PubMed paginate) — OSS_FORENSIC_STACK.md
5. Inventory + atoms (schemas/finding-atom.schema.json)
6. Study families + GRADE by outcome (GRADE_RUBRIC.md)
7. Cross-study links + bridge + 3s/30s/3min
8. Completeness Ledger
9. Editorial Claim Lock
10. Hooks >=12 → winner
11. 6/8/10 slides + Retention Map
12. 56-block prompts, one fence per slide (GEMINI_PRODUCTION.md)
13. PT-BR caption
14. Gate APROVADO / RESSALVAS / REPROVADO
15. Paste into Gemini one slide at a time

Forbidden: invent source, page cap, hook before lock, prompt that depends on previous slide, send forensic YAML to Gemini.
