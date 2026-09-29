# BDC EDITORIAL LEARNING ENGINE v1.0

## Objetivo

Fechar o ciclo produção → publicação → medição → aprendizado sem transformar correlação em causalidade.

## 1. Learning loop

```text
DOSSIER
→ CAROUSEL
→ PUBLISH
→ METRICS SNAPSHOT
→ NORMALIZATION
→ FEATURE TAGGING
→ HYPOTHESIS
→ A/B TEST
→ LEARNING LEDGER
→ NEXT BRIEF
```

## 2. Metrics registry

Quando disponíveis, registrar:
- reach;
- impressions;
- likes;
- saves;
- shares;
- comments;
- profile visits;
- follows;
- slide completion / carousel advancement quando a plataforma fornecer;
- watch/hold proxy quando disponível;
- publication date/time.

Nunca inventar métrica ausente.

## 3. Normalize before learning

Comparações devem considerar:
- tamanho da audiência na data;
- paid vs organic;
- collab vs solo;
- recência;
- tema;
- formato;
- sazonalidade;
- distribuição anormal;
- alcance inicial.

Não concluir "ouro converte mais" a partir de 1 post.

## 4. Feature tagging

Cada post recebe tags:

HOOK:
contradição | mecanismo | mito | pergunta | dado | identidade | utilidade

VISUAL:
close | split | hub | path | anatomy | timeline | flat-chart | sequence | map

CRIAGO:
off | mentor | commentator | closing

PALETTE:
default | lab | ring | alert | terreiro | night

COPY:
short | medium | dense

CTA:
save | share | comment | follow | apply

CONTENT:
science | history | biomechanics | injury | TEA | boxing | BJJ | local

## 5. Creative memory

Registrar fingerprint do layout para evitar fadiga:
- hero placement;
- headline placement;
- frame grammar;
- card count;
- infographic grammar;
- accent pair;
- Criago position.

Regra:
- identidade deve repetir tokens;
- composição não deve repetir mecanicamente;
- evitar mesma capa 3 posts seguidos;
- variedade não pode quebrar FRAME/PALETTE/LOGO locks.

## 6. Hook tournament

Antes de escolher a capa:
1. gerar 16–24 hooks;
2. eliminar qualquer um acima do Claim Lock;
3. agrupar por família;
4. pontuar separadamente:
   - CLARITY;
   - CURIOSITY;
   - SPECIFICITY;
   - PROOFABILITY;
   - SHARE POTENTIAL;
5. selecionar 3 finalistas;
6. escolher o que maximiza STOP sem perder PROOFABILITY.

Não produzir score "científico"; é rubrica editorial explícita.

## 7. A/B experiments

Testar uma variável principal por vez quando possível:
- Hook A vs B;
- Criago ON vs OFF;
- close vs diagram;
- gold keyword vs white;
- utility CTA vs share CTA.

Definir antes:
- hypothesis;
- primary metric;
- comparison window;
- confounders known.

Sem randomização verdadeira, rotular resultado como OBSERVATIONAL, não causal.

## 8. Content graph

Cada dossiê gera nós:
- tema;
- subtema;
- mecanismo;
- mito;
- estudo;
- técnica;
- atleta/história;
- risco;
- aplicação;
- próximo post.

Exemplo:
BOXE SOVIÉTICO
→ origem
→ pedagogia
→ footwork
→ pontuação amateur
→ atletas
→ mito "um único estilo"
→ comparação Cuba/México
→ treino aplicável

O sistema deve reutilizar investigação, não copiar texto.

## 9. Repurposing

Do mesmo Claim Lock podem nascer:
- carousel;
- Reel 45 s;
- Reel 90 s;
- article;
- story quiz;
- infographic;
- caption short;
- coach checklist.

Cada formato recompila a narrativa; não cortar o carousel em pedaços sem adaptação.

## 10. Learning ledger schema

```yaml
post_id:
date:
topic:
claim_lock:
hook_family:
visual_grammar:
palette_mode:
criago:
cta:
metrics:
normalization_notes:
observed_pattern:
confidence: low|medium|high
next_test:
```

## 11. Rule promotion

Uma heurística só vira "regra BDC" quando:
- aparece repetidamente;
- sobrevive a temas diferentes;
- não depende de uma única campanha;
- não conflita com A11Y/evidence/brand.

Caso contrário permanece HYPOTHESIS.

## 12. No vanity optimization

Prioridade BDC:
1. factual trust;
2. shares/saves úteis;
3. comprehension;
4. retention;
5. reach;
6. likes.

Nunca sacrificar rigor por métrica.
