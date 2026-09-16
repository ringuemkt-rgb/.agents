# Portability Guide — Use in Any AI

The system is vendor-neutral. The only hard requirement is that the target model can receive a long instruction block or repository context. Web/research access is strongly recommended for current, scientific or contested topics.

## Generic LLM

Load, in order:

1. `SYSTEM_PROMPT.md` as system/custom instructions.
2. `AGENT.md` as execution contract.
3. `EVIDENCE_SYNTHESIS.md` for scientific/clinical/biomechanical/epidemiological or controversial themes.
4. `MANIFEST.json` if the platform supports machine-readable agent metadata.
5. JSON schemas when structured evidence output is useful.

Then send the theme normally.

## ChatGPT

- Projects/Work: add `SYSTEM_PROMPT.md`, `AGENT.md`, `EVIDENCE_SYNTHESIS.md` and the `schemas/` directory as project knowledge/instructions.
- Custom GPT: use `SYSTEM_PROMPT.md` as the main instruction set and upload the supporting files as knowledge.
- Normal chat: paste `SYSTEM_PROMPT.md`; for deep science questions also attach/paste `EVIDENCE_SYNTHESIS.md`.
- For current/scientific topics, use web/research tools when available.
- Preserve the default: prompts first; images only on explicit render request.

## Claude / Claude Code

- Claude Projects: place `SYSTEM_PROMPT.md` in Project Instructions and add `AGENT.md`, `EVIDENCE_SYNTHESIS.md` and schemas as project knowledge.
- Claude Code: read repository `AGENTS.md`, then this directory's `AGENT.md`, `SYSTEM_PROMPT.md` and evidence module before scientific carousel work.
- Do not let concise mode drop evidence, data-viz, overlap, applicability, brand or safety gates.

## Gemini

- Put `SYSTEM_PROMPT.md` into Gem/custom instructions.
- Attach `AGENT.md`, `EVIDENCE_SYNTHESIS.md` and schemas when supported.
- Require every slide prompt to remain autonomous even if the model wants to abbreviate repeated design instructions.

## Grok / DeepSeek / Mistral / Copilot / other assistants

Use the Generic LLM procedure.

If context is constrained, prioritize:

1. `AGENT.md`;
2. `EVIDENCE_SYNTHESIS.md` for evidence-heavy topics;
3. pipeline, evidence, hook, retention, design, data-viz and prompt-contract sections of `SYSTEM_PROMPT.md`;
4. full Criago Character Lock;
5. clinical/safety rules.

Never shorten by removing:
- Editorial Claim Lock before Hook Forge;
- direct vs indirect evidence;
- duplicate/overlap resolution when relevant;
- heterogeneity/contradiction/applicability gates;
- data-viz integrity;
- full slide autonomy requirement.

## Structured evidence workflows

When the AI/platform supports JSON or tools, use:

- `schemas/claim-ledger.schema.json` — atomic claims and evidence state;
- `schemas/study-family-ledger.schema.json` — cohort/publication identity and overlap;
- `schemas/evidence-graph.schema.json` — support, contradiction, indirectness, mechanism and uncertainty graph.

## Starter command — complete carousel

```text
Tema: [TEMA]
Modo: carrossel completo.
Idioma: português brasileiro.

Defina a audiência e o problema.
Escolha o nível de perícia necessário.
Pesquise evidência atual se houver ferramentas.
Resolva publicações duplicadas/coortes sobrepostas antes de contar estudos.
Separe outcomes diferentes.
Procure evidência contraditória, heterogeneidade e limitações de aplicabilidade.
Construa a conclusão integrada antes de selecionar o hook.
Depois gere hooks concorrentes, roteiro didático, retenção slide a slide e Visual Claim Map.
Entregue prompts ultra detalhados, slide por slide, totalmente autônomos e seguindo integralmente o estilo de design solicitado.
Finalize com legenda pronta para copiar e colar, emojis semânticos, 3–5 hashtags, fontes e Guardião.
```

## Starter command — full forensic dossier

```text
Tema: [TEMA]
Modo: FULL INVESTIGATIVE DOSSIER.

Antes de produzir conteúdo:
1. decomponha a pergunta;
2. faça Source Map;
3. resolva Study Families e amostras sobrepostas;
4. construa Outcome Ontology;
5. avalie risco de viés por desenho;
6. construa Evidence Graph;
7. investigue causalidade/mecanismo quando aplicável;
8. normalize efeitos sem conversões falsas;
9. explique heterogeneidade e contradições;
10. faça triangulação;
11. avalie aplicabilidade e certeza por outcome;
12. pareie benefícios/danos;
13. procure evidência ausente;
14. conclua em: sabemos / provavelmente / plausível / não sabemos / contradito / o que mudaria a conclusão.

Só depois libere claims editoriais e hooks.
```
