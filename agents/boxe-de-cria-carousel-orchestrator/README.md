# BOXE DE CRIA — Carousel Orchestrator v7.1

Sistema portátil para produção editorial baseada em evidência:

Audience/Demand → Evidence → Claim Ledger → Red Team → Hook/Arc → Visual Proof → 25-block Compiler → Gemini/target adapter → QA → Caption → Learning.

## Principal mudança v7

SOURCE MODULARITY → COMPILED REDUNDANCY.

O repositório mantém cada lock canônico em um único lugar.
O prompt entregue ao usuário continua totalmente autônomo e repete todos os locks necessários.

## Visual doctrine

Evidence × Metaphor × Memory.

ONE THESIS
→ ONE GRAMMAR
→ ONE HERO
→ ONE VISUAL PROOF
→ ONE MEMORY LINE.

## Prompt contract

25 blocos por slide.
Depth Z0–Z6.
Background L0–L9.
2.5D editorial only.
Criago role CR0–CR4.
Humor H0–H3.

## Gemini

- uma imagem por slide;
- 4:5 quando suportado;
- 2K/4K conforme capacidade atual do modelo/interface;
- design grid 2160×2700 é conceitual;
- T0/T1/T2 exact text;
- G1 all-in-one;
- G2 finalization-safe quando o texto/dado/marca for de alto risco.

## Caption

Todo carrossel termina com:
PROMPT COMPLETO DA DESCRIÇÃO / LEGENDA — COPIAR E COLAR

salvo pedido explícito para omitir.

## Wake phrase

```text
Ativa o BOXE DE CRIA Carousel Orchestrator v7.1.
Tema: [TEMA]
Slides: 8
Destino: Gemini Image.
Entrega: perícia + Claim Ledger + Viral Brief + arco + 8 prompts autônomos de 25 blocos + QA + prompt completo da legenda + Gate.
```


## Runtime executável

A v7.1 deixa de ser somente um framework documental.

Principais componentes:
- `canon/*.json` — Single Source of Truth;
- `src/compiler/*` — compiler de 25 blocos;
- `src/intelligence/forensic-ai.ts` — conselho pericial adversarial;
- `src/routers/*` — risco, complexidade, domínio, freshness e gramática;
- `src/dataviz/*` + `src/finalization/*` — camadas determinísticas;
- `src/qa/*` — lint, visual QA e regressão;
- `src/learning/*` + `src/experiments/*` — feedback real;
- GitHub Actions — typecheck, testes, schemas e regressão de contrato.

### Uso local

```bash
cd agents/boxe-de-cria-carousel-orchestrator
npm install
npm run ci
npm run build:fixture
```

### AI Forensic Council

Em ChatGPT, a camada pericial é executada por esta própria IA com as ferramentas disponíveis. Para automação externa, o runtime expõe `AiProvider` sem amarrar o sistema a um único fornecedor.
