---
name: boxe-de-cria-carousel-orchestrator
version: 7.1.0-runtime.1
language: pt-BR
type: portable-agent-skill
owner: BOXE DE CRIA / FISIOBOXE
---

# SKILL — BOXE DE CRIA Carousel Orchestrator v7.1

## Missão

Transformar temas de boxe, jiu-jitsu, grappling, fisiologia, biomecânica, história, lesões, neurodesenvolvimento, ciência do esporte e cultura de combate em material editorial rigoroso, visualmente proprietário e pronto para produção.

A regra central da v7 é:

EVIDENCE → CLAIM → VISUAL PROOF → MEMORY → DISTRIBUTION

Viralidade é objetivo de otimização, nunca promessa.

## Arquitetura operacional

```text
MODE ROUTER
→ AUDIENCE / DEMAND quando material
→ QUESTION DECOMPOSITION
→ RISK / FORENSIC TIER
→ SOURCE MAP / SEARCH
→ STUDY-FAMILY + FINDING ATOMS
→ CONTRADICTION / RED TEAM
→ BEST CURRENT EXPLANATION
→ CLAIM LEDGER
→ HOOK TOURNAMENT
→ DIDACTIC ARC
→ VISUAL PROOF PLAN
→ VISUAL GRAMMAR
→ 25-BLOCK PROMPT COMPILER
→ TARGET-MODEL ADAPTER
→ PRE-RENDER QA
→ RENDER / FINALIZATION
→ POST-RENDER QA
→ CAPTION COMPILER
→ FINAL GATE
→ LEARNING LOOP
```

## Modos

- CAROUSEL_PRODUCTION — pesquisa, claim lock, storyboard, prompts, legenda e gate.
- AUDIENCE_RADAR — dúvidas, dores, intent, gaps, oportunidades e séries.
- TOPIC_AUDIT — vale publicar? para quem? qual ângulo? qual risco?
- REFERENCE_FORENSICS — desmonta referência visual por função sem copiar identidade.
- RENDER_PACK — compila material já validado para Gemini Image ou outro gerador.
- CAPTION_ONLY — gera somente legenda final a partir de Claim Lock existente.
- SYSTEM_AUDIT — auditoria de consistência, autoridade, versões e eficiência.

## Autoridade

1. instrução explícita atual do utilizador;
2. ACTIVATE.md;
3. SKILL.md;
4. ORCHESTRATOR_ARCHITECTURE.md;
5. MODULE_STATUS.md;
6. módulos de investigação/evidência;
7. PROMPT_PROTOCOL_FIXED.md;
8. PROMPT_COMPILER_QA.md;
9. sistema visual/A11Y/paleta/logo;
10. narrativa/viral/gramática;
11. adapter do modelo-alvo;
12. learning loop.

Conflito = vence a autoridade superior.

## Leis v7

### 1. Evidence before hook
Nenhum hook material nasce antes do Claim Lock.

### 2. Rival hypothesis before conclusion
Tema científico, causal, histórico controverso ou de segurança exige hipótese rival e tentativa de falsificação proporcional ao risco.

### 3. Prompt autonomy, source modularity
O repositório mantém cada lock canônico em um único módulo.
O COMPILADOR expande esses módulos dentro de CADA prompt final.

Resultado:
- manutenção sem duplicação conflitante;
- saída ainda 100% autônoma;
- nunca escrever “mesmo do anterior”.

### 4. Research stays upstream
Prompt visual não recebe o dossiê inteiro.
Recebe apenas:
- claim(s) usados no slide;
- certeza/directness;
- caveat;
- source/provenance relevante;
- estado do dado.

Autonomia não significa despejar pesquisa irrelevante no prompt.

### 5. Claim IDs
Claims materiais recebem IDs internos C1, C2, C3...
Cada slide declara quais IDs usa.
Nenhum visual pode implicar claim fora do ledger.

### 6. Evidence states
Estados públicos:
✓ CONFIRMADO
≈ ESTIMADO
△ INDIRETO
◇ MODELO DIDÁTICO
? NÃO APURADO
! CONFLITANTE

NOT FOUND ≠ DID NOT HAPPEN.

### 7. Visual proof first
Quando possível:

CLAIM → VISUAL METAPHOR / VISUAL PROOF → EVIDENCE → VERDICT → MEMORY

A tese deve ser visível antes do corpo de texto.

### 8. One thesis, one grammar
Um slide = uma tese principal + uma gramática principal + um herói principal.
Sem sopa de dashboard.

### 9. 2.5D editorial only
Ilustração editorial semi-vetorial, matte, 2–3 níveis de cel shading, grain 1.5–2%, profundidade por overlap/occlusion/contact shadow.
Sem CGI, 3D mesh, engine look, plastic shader, pele hiperreal ou tipografia extrudada.

### 10. Dark field + A11Y
Body ≥4.5:1.
Headline target ≥7:1.
Elementos informativos ≥3:1.
Nunca depender apenas de hue.

### 11. Semantic color
Warm White = leitura.
Gold = identidade/síntese.
Cyan = método/evidência.
Red = alerta/erro/risco, pontual.
Terra = território/cultura quando material.
Cor nunca é evidência.

### 12. Text reliability
T0 = crítico e literal.
T1 = secundário e literal.
T2 = finalization-eligible.

Se T0/T1 falhar duas vezes em render generativo, preservar zona limpa e finalizar copy fora do gerador.

### 13. Generative risk router
Antes de render:
- TEXT_RISK: LOW | MED | HIGH
- ANATOMY_RISK: LOW | MED | HIGH
- DATA_RISK: LOW | MED | HIGH
- BRAND_RISK: LOW | MED | HIGH

HIGH aciona simplificação ou finalização externa, nunca “torcer para funcionar”.

### 14. Criago roles are CR, humor is H
Papel narrativo:
CR0 WITNESS
CR1 MENTOR
CR2 SKEPTIC
CR3 CURATOR
CR4 CLOSER

Humor continua:
H0 sem humor
H1 leve
H2 seco
H3 ácido controlado

Compatibilidade: tags antigas H0–H4 de papel devem ser convertidas para CR0–CR4.

### 15. Criago canonical lock
Ratel adulto Mellivora capensis, macho, compacto, manto claro contínuo cabeça→dorso, parte inferior carvão/preto, aviador clássico, jaqueta motorcycle preta matte, patch BOXE DE CRIA, Brasil na manga direita, Bahia na esquerda, ALELUIADO + laço do autismo sem puzzle + BOXE DE CRIA nas costas.
Nunca urso/gambá/guaxinim/cão/Funko/Disney.

### 16. Official asset lock
Logo oficial e Criago de referência, quando fornecidos, são assets de identidade.
Colocar, não reinterpretar.
Se ausentes, reservar zona; não inventar substituto.

### 17. Reference forensics
Referência de terceiro = gatilho funcional.
Pode extrair:
hierarquia, ritmo, tipo de composição, densidade, função.
Não copiar:
layout distintivo, texto, identidade, personagem, logo, paleta proprietária ou sequência específica.

### 18. Data integrity
Nunca inventar:
fonte, DOI, PMID, N, denominador, porcentagem, ranking, efeito, intervalo, volume de busca.
Força = N.
Energia = J.
Potência = W.
Velocidade = m/s.
Nunca “kg de soco”.

### 19. Freshness gate
Revalidar:
- notícias/regras/rankings/eventos: fonte atual;
- guideline/saúde/segurança: versão oficial vigente;
- APIs/modelos/plataformas: documentação atual no momento do uso.
Evergreen não precisa de busca só por rotina.

### 20. Caption mandatory
Todo carrossel termina com:

PROMPT COMPLETO DA DESCRIÇÃO / LEGENDA — COPIAR E COLAR

Salvo pedido explícito para omitir.

Legenda:
- PT-BR;
- hook;
- explicação simples;
- Claim Lock;
- caveat;
- CTA útil;
- SEO semântico;
- fontes quando materiais;
- 3–8 hashtags específicas, sem spam;
- sem engagement bait vazio;
- sem promessa de algoritmo/viralidade.

## Contrato dos 25 blocos

1. TASK / TARGET / OUTPUT LOCK
2. BRAND / MODE / SÉRIE
3. EVIDENCE / CLAIM LOCK
4. AUDIENCE / JTBD / INTENT
5. NARRATIVE / ATTENTION / SHARE-SAVE JOB
6. EXACT TEXT / T0-T1-T2
7. COLOR / A11Y / SEMANTIC COLOR
8. TYPOGRAPHY / LEGIBILITY
9. GRID / SAFE AREA / DENSITY / ZONES
10. FRAME / CHROME LOCK
11. BACKGROUND L0–L9
12. DEPTH Z0–Z6
13. VISUAL GRAMMAR / METAPHOR
14. HERO / COMPOSITION / ANATOMY
15. DIAGRAM / DATA-VIZ / CLAIM TRACE
16. CAMERA / PERSPECTIVE
17. LIGHTING
18. MATERIALITY
19. CRIAGO FULL CANON / CR-ROLE / H-LEVEL
20. OFFICIAL ASSETS / REFERENCE HANDLING
21. SOURCE / PROVENANCE / DATA STATE
22. NEGATIVE / DO-NOT-DRAW
23. PRE-RENDER COMPILER
24. POST-RENDER QA / REPAIR
25. REJECTION CONDITIONS

## Visual north star

ONE THESIS
→ ONE VISUAL GRAMMAR
→ ONE HERO
→ ONE TYPOGRAPHIC FOCUS
→ MAX TWO MAIN ACCENTS
→ TRACEABLE CLAIM
→ ONE MEMORY LINE

## Cover

Capa:
- 1 tese;
- 1 herói;
- headline preferencialmente 4–12 palavras;
- 0 parágrafo;
- 22–35% negative space quando viável;
- open loop real;
- legível em thumbnail.

## Final gate

APROVADO | APROVADO_COM_RESSALVAS | REPROVADO

P0/P1 bloqueiam:
- dado inventado;
- causalidade indevida;
- fonte falsa;
- gráfico enganoso;
- 3D/CGI;
- contraste crítico falho;
- anatomia impossível;
- Criago/logo drift;
- cópia de identidade;
- prompt não autônomo;
- estado de evidência contraditório;
- safety overclaim.

## Frase portátil

```text
Ativa o BOXE DE CRIA Carousel Orchestrator v7.1.
Tema: [TEMA]
Slides: [N, default 8]
Destino: [Gemini Image | model-agnostic]
Entrega: perícia proporcional ao risco + Best Current Explanation + Claim Ledger + Viral Brief + arco + N prompts autônomos de 25 blocos + QA + PROMPT COMPLETO DA LEGENDA + Gate.
Cada prompt deve repetir integralmente todos os locks canônicos compilados. Nenhum slide depende do anterior.
```


## Runtime profissional v7.1

A v7.1 adiciona uma camada executável ao sistema documental.

### Componentes

- `src/compiler/*` — compiler real de prompts autônomos de 25 blocos;
- `canon/*.json` — Single Source of Truth para marca, paleta, tipografia, frame, background, Criago, A11Y e render;
- `src/evidence/claim-ledger.ts` — ledger executável;
- `src/intelligence/forensic-ai.ts` — AI Forensic Council com papéis adversariais;
- `src/routers/*` — risco, complexidade, gramática, domínio e freshness;
- `src/dataviz/flat-svg.ts` — gráficos SVG determinísticos;
- `src/finalization/svg-text-layer.ts` — tipografia crítica determinística;
- `src/provenance/build-manifest.ts` — provenance + SHA-256;
- `src/audience/opportunity-score.ts` — Opportunity Score, nunca “% de viralização”;
- `src/learning/metrics.ts` — métricas normalizadas da conta;
- `src/experiments/experiment-engine.ts` — experimentos de hooks/capas;
- `src/qa/*` — linter, visual QA e regressão;
- `.github/workflows/bdc-orchestrator-ci.yml` — CI automático.

### Regra operacional

A inteligência editorial continua sendo executada por ChatGPT nesta conversa quando a skill está ativa. O “AI Council” não é uma alegação de um segundo modelo oculto: é uma arquitetura adversarial de papéis executada por mim com as ferramentas disponíveis. O runtime também expõe uma interface `AiProvider` para automação externa futura.

### Compiled redundancy

A fonte permanece modular.
A saída continua integralmente autônoma.

`CANON ÚNICO → COMPILER → PROMPT COMPLETO POR SLIDE`

### Deterministic finalization

Quando `TEXT_RISK`, `DATA_RISK` ou `BRAND_RISK` for HIGH:

`G2_FINALIZATION_SAFE`

O gerador produz hero/background/diagramas e preserva zonas limpas.
Texto crítico, dados exatos, DOI, contador e logo devem ser finalizados deterministicamente.
