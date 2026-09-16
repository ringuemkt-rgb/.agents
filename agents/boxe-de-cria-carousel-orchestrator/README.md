# BOXE DE CRIA — Carousel Orchestrator

Sistema portátil para qualquer IA: perícia → Claim Lock → **prompts 22 blocos autónomos** → legenda no fim.
Imagens Gemini 4:5. Não gerar arte aqui a menos que peçam render.

**Versão: 4.1.0-portable.1**

## Acordar a IA (qualquer modelo)

1. Colar [`ACTIVATE.md`](./ACTIVATE.md) nas instruções / no primeiro mensagem.
2. Opcional: anexar [`PROMPT_PROTOCOL_FIXED.md`](./PROMPT_PROTOCOL_FIXED.md) + [`PROMPT_TEMPLATE.md`](./PROMPT_TEMPLATE.md).
3. Enviar:

```text
Ativa o BOXE DE CRIA Carousel Orchestrator v4.1.
Tema: [TEMA]
Slides: 8
Entrega: Claim Lock + Viral Brief + 8 fences de 22 blocos autônomos + legenda só no fim.
Não gerar imagem. Não encurtar prompt. Não escrever "mesmo do anterior".
```

Contrato visual: 4:5, 2160×2700 work, export 1080×1350, sRGB, Criago lock inteiro em cada fence mesmo OFF.

## Ficheiros que a IA deve carregar

| Ordem | Ficheiro | Função |
|---|---|---|
| 0 | `ACTIVATE.md` | acordar + contrato de entrega |
| 1 | `PROMPT_PROTOCOL_FIXED.md` | 22 blocos + HEX + caption |
| 2 | `PROMPT_TEMPLATE.md` | molde vazio |
| 3 | `CONTENT_PRODUCTION_OS.md` | pipeline + KPI hops |
| 4 | `AGENT.md` | perícia e disciplina |
| 5 | `EVIDENCE_SYNTHESIS.md` | motor forense |
| 6 | `STYLE_LOCK_EDITORIAL_BOXE.md` | cara |
| 7 | `CORRECTIONS_APPLIED.md` | unidades, voz |

## Entrega obrigatória

- Claim Lock antes do hook
- Um code fence por slide, 22 secções, autónomo
- Legenda PT-BR só depois do último slide
- Gate APROVADO / RESSALVAS / REPROVADO

## Repo

https://github.com/ringuemkt-rgb/.agents/tree/main/agents/boxe-de-cria-carousel-orchestrator

MIT no código/prompt. Marca BOXE DE CRIA™ / FISIOBOXE — ver NOTICE.md.
