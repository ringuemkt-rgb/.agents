# BDC CONTENT GRAPH ENGINE v1.0

## Missão

Transformar uma pergunta em biblioteca editorial conectada, evitando posts soltos e pesquisa repetida.

---

## 1. Node types

- QUESTION
- PAIN
- DESIRE
- INTENT
- PERSONA
- CLAIM
- EVIDENCE
- MECHANISM
- TECHNIQUE
- MYTH
- RISK
- HISTORY
- PERSON
- RULESET
- EQUIPMENT
- LOCAL_CONTEXT
- FORMAT
- POST
- SERIES
- NEXT_QUESTION

---

## 2. Edge types

- ASKS
- EXPERIENCES
- WANTS
- EXPLAINS
- SUPPORTS
- CONTRADICTS
- MODERATES
- CAUSES? — only when causal evidence supports
- ASSOCIATED_WITH
- PRECEDES
- COMPARES_WITH
- APPLIES_TO
- LEADS_TO
- NEEDS_UPDATE
- DERIVES_FROM
- REPURPOSES_TO

Use “CAUSES?” apenas como edge provisório até Claim Lock.

---

## 3. Query expansion

Exemplo:

```text
QUESTION: “por que meu gás acaba?”
├─ PAIN: fadiga precoce
├─ MECHANISM: pacing
├─ MECHANISM: tensão excessiva
├─ MECHANISM: capacidade aeróbia
├─ MECHANISM: ansiedade
├─ TECHNIQUE: respiração
├─ RECOVERY: sono
├─ RECOVERY: intervalo
├─ MYTH: “é só correr mais”
└─ NEXT_QUESTION: “corrida longa melhora boxe?”
```

Cada nó pode virar conteúdo se passar Opportunity + Evidence Gate.

---

## 4. Series compiler

Do grafo, montar sequência:

1. pergunta ampla;
2. mito;
3. mecanismo;
4. evidência;
5. aplicação;
6. erro;
7. protocolo;
8. comparação;
9. história;
10. FAQ.

Não publicar 10 posts se só 3 têm valor real.

---

## 5. Research reuse

Uma investigação pode alimentar vários formatos, mas cada saída deve:
- preservar Claim Lock;
- adaptar copy;
- adaptar densidade;
- adaptar visual;
- atualizar freshness quando necessário.

Não duplicar texto.

---

## 6. Content moat clusters

Clusters preferenciais BDC:

### FISIOBOXE
boxe × fisioterapia × biomecânica × segurança.

### NEUROCOMBATE
boxe × percepção × aprendizagem motora × TEA.

### COMBAT HISTORY
boxe × luta livre × SAMBO × jiu-jitsu × escolas.

### COACH LAB
didática × estratégia × treinamento.

### BAIXO SUL / BAHIA
luta × cultura local × acesso × comunidade.

---

## 7. Gap coverage

O grafo deve marcar:
- EXISTS_BDC;
- NEEDS_UPDATE;
- MISSING;
- DUPLICATE;
- WEAK_EVIDENCE;
- HIGH_OPPORTUNITY.

Isso impede repetir pauta já resolvida sem novidade.

---

## 8. Content Graph output

```yaml
root_question:
cluster:
nodes:
edges:
existing_posts:
missing_nodes:
high_opportunity_nodes:
evidence_refresh_nodes:
recommended_series:
repurpose_targets:
```

---

## 9. Handoff

```text
AUDIENCE DEMAND
→ TOPIC OPPORTUNITY
→ CONTENT GRAPH
→ EVIDENCE INVESTIGATION
→ CAROUSEL
→ LEARNING ENGINE
→ GRAPH UPDATE
```
