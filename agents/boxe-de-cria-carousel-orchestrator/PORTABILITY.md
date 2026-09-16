# Portability Guide — Use in Any AI

The system is vendor-neutral. The only hard requirement is that the target model can receive a long instruction block or repository context.

## Generic LLM

Load, in order:

1. `SYSTEM_PROMPT.md` as system/custom instructions.
2. `AGENT.md` as execution contract.
3. `MANIFEST.json` if the platform supports machine-readable agent metadata.

Then send the theme normally.

## ChatGPT

- Projects/Work: add `SYSTEM_PROMPT.md`, `AGENT.md` and this directory as project knowledge/instructions.
- Custom GPT: use `SYSTEM_PROMPT.md` as the main instruction set and upload supporting files as knowledge.
- Normal chat: paste `SYSTEM_PROMPT.md` once, then send themes.
- For current/scientific topics, use web/research tools when available.
- Preserve the default: prompts first; images only on explicit render request.

## Claude / Claude Code

- Claude Projects: place `SYSTEM_PROMPT.md` in Project Instructions and add the directory as project knowledge.
- Claude Code: read repository `AGENTS.md`, then this directory's `AGENT.md` and `SYSTEM_PROMPT.md` before executing carousel work.
- Do not let concise mode drop evidence, data-viz, brand or safety gates.

## Gemini

- Put `SYSTEM_PROMPT.md` into Gem/custom instructions.
- Attach `AGENT.md` and supporting files when supported.
- Require every slide prompt to remain autonomous even if the model wants to abbreviate repeated design instructions.

## Grok / DeepSeek / Mistral / Copilot / other assistants

Use the Generic LLM procedure. If context is limited, prioritize:

1. `AGENT.md`;
2. sections 4–8, 11–20 and 22–24 of `SYSTEM_PROMPT.md`;
3. the full Criago Character Lock;
4. evidence/safety/data-viz rules.

Never shorten by removing evidence gates or the full slide autonomy requirement.

## Starter command

```text
Tema: [TEMA]
Modo: carrossel completo.
Idioma: português brasileiro.
Faça perícia investigativa, pesquise evidência atual se houver ferramentas, gere hooks concorrentes, construa roteiro didático, depois entregue prompts ultra detalhados slide por slide, todos autônomos. Finalize com legenda pronta para copiar e colar em bloco de código, emojis semânticos, 3–5 hashtags e Guardião.
```
