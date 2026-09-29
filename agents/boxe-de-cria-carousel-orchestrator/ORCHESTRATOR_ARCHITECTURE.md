# BOXE DE CRIA Carousel Orchestrator — Architecture v4.3

## Objetivo

Este documento organiza o sistema em camadas para impedir conflito entre módulos, duplicação de autoridade e regressões de protocolo.

## Single Source of Truth

```text
USER REQUEST
   ↓
ACTIVATE.md
   ↓
SKILL.md
   ↓
AGENT.md / SYSTEM_PROMPT.md
   ↓
INVESTIGATIVE LAYER
   ↓
EDITORIAL LAYER
   ↓
VISUAL COMPILER
   ↓
QA / GATE
```

## Camada A — Controle

### ACTIVATE.md
Contrato de ativação e precedência.

### SKILL.md
Comportamento portátil da skill e leis operacionais.

### AGENT.md
Missão, responsabilidades, inferência, segurança editorial e limites do agente.

### SYSTEM_PROMPT.md
Raiz model-agnostic para implementação em outras IAs.

## Camada B — Investigação

### INVESTIGATIVE_SYNTHESIS_INTELLIGENCE.md
Hipóteses rivais, ACH, causalidade, falsificação, sensibilidade e Best Current Explanation.

### EVIDENCE_SYNTHESIS.md
Inventário, famílias de estudo, risco de viés, heterogeneidade, aplicabilidade e certainty.

### CROSS_STUDY_INTELLIGENCE.md
Finding atoms, saturação, ligação entre estudos e independência de replicação.

### GRADE_RUBRIC.md
Certeza por outcome.

Saída desta camada:
`BEST CURRENT EXPLANATION + CLAIM LOCK`.

## Camada C — Estratégia editorial

### CONTENT_PRODUCTION_OS.md
Pipeline completo de produção.

### ATTENTION_NARRATIVE.md
Payoff, open loop, next-slide desire e handoff.

### VIRAL_ENGINE.md
Hook, share line, save reason e distribuição sem romper Claim Lock.

Saída:
`VIRAL BRIEF + DIDACTIC ARC`.

## Camada D — Compilador visual

### PROMPT_PROTOCOL_FIXED.md
Contrato final dos 22 blocos.

### PROMPT_TEMPLATE.md
Molde operacional.

### INFOGRAPHIC_GRAMMAR.md
Escolha de gráfico/diagrama/estrutura didática.

### PALETTE_CANON.md
Tokens oficiais.

### PALETTE_DECISION_ENGINE.md
Seleção de modo por conteúdo, emoção e gramática.

### COLOR_THEORY_BDC.md
Semântica e coerência cromática.

### ACCESSIBILITY_CONTRAST.md
WCAG 2.2.

### RENDER_2_5D_LOCK.md
Lei visual 2.5D.

### OFFICIAL_LOGO_LOCK.md
Logo oficial como asset externo.

Saída:
`N FENCES AUTÔNOMOS`.

## Camada E — Brand character

Mestre Criago é compilado dentro do bloco 18 de CADA fence.

A descrição canônica nunca depende de outro slide.

O personagem pode estar `VISIBILITY: OFF`, mas o FULL LOCK continua presente para evitar identity drift em modelos que processam prompts isoladamente.

## Autonomy Repetition Law

Para cada slide, os seguintes componentes nunca podem ser abreviados por referência:

```text
FORMAT
PALETTE
A11Y
FRAME
BACKGROUND
DEPTH
CRIAGO
LOGO
NEGATIVE
QA
```

A repetição deliberada garante portabilidade ChatGPT ↔ Gemini ↔ Claude ↔ Grok ↔ DeepSeek ↔ modelos locais.

## Visual architecture

### Frame
BDC chrome = charcoal/graphite matte.

### Environment
Preferência por campo escuro:
- petroleum;
- deep navy;
- charcoal.

### Accent policy
No máximo 2 famílias principais por slide.

### Depth
Apenas 2.5D:
- overlap;
- occlusion;
- contact shadow;
- selective blur;
- shallow perspective.

### No-go
- 3D;
- CGI;
- game engine;
- glossy plastic;
- photoreal skin/fur;
- generic sci-fi HUD.

## Cover architecture

```text
BRAND / CATEGORY
      ↓
HOOK ≤ 1 ideia central
      ↓
HERO VISUAL QUE PROVA O HOOK
      ↓
OPEN LOOP
      ↓
SWIPE CUE DISCRETO
```

A capa não deve parecer infográfico cheio. Ela vende a pergunta/tese; os slides seguintes entregam a prova.

## QA stack

### Evidence QA
Claim ≤ evidence.

### Editorial QA
Hook ≤ Claim Lock.

### Didactic QA
Elemento visual deve ensinar algo.

### Visual QA
2.5D + hierarchy + negative space + frame.

### Accessibility QA
WCAG 2.2.

### Brand QA
Logo e Criago canônicos.

### Safety QA
Sem humor contra vulneráveis; sem promessas clínicas indevidas.

### Final Gate
`APROVADO | APROVADO_COM_RESSALVAS | REPROVADO`.

## Versão

`4.3.0-portable.1`
