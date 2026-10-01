# DSPy Module Design

Design conceitual para transformar o sistema de prompts em módulos avaliáveis e otimizáveis.

---

## 1. Objetivo

Migrar de prompt manual para pipeline modular:

```text
brief → pesquisa → tese → gancho → roteiro → prompts → legenda → QA → IPV
```

---

## 2. Módulos recomendados

### AudienceResearcher

Entrada:

- tema;
- público;
- dados de insight quando disponíveis.

Saída:

- dor real;
- crença errada;
- objeções;
- tipo de métrica esperada.

### EvidencePlanner

Entrada:

- tema;
- fontes recuperadas;
- documentos internos.

Saída:

- evidence pack;
- nível de evidência;
- afirmações permitidas;
- afirmações proibidas.

### HookGenerator

Entrada:

- dor;
- crença errada;
- objetivo.

Saída:

- capa A direta;
- capa B provocativa;
- capa C checklist;
- justificativa.

### CarouselStrategist

Entrada:

- tese;
- público;
- gancho escolhido.

Saída:

- roteiro card por card;
- texto exato dos slides;
- retenção slide a slide.

### SlidePromptBuilder

Entrada:

- slide;
- texto;
- objetivo visual;
- brand config.

Saída:

- prompt com texto;
- prompt sem texto;
- negative prompt.

### CaptionOptimizer

Entrada:

- tema;
- tese;
- CTA;
- tom.

Saída:

- legenda final;
- hashtags;
- CTA;
- frase salvável.

### IPVScorer

Entrada:

- tema;
- dor;
- gancho;
- evidência;
- aderência à marca.

Saída:

- IPV estimado;
- métrica principal;
- justificativa;
- prioridade.

### QualityJudge

Entrada:

- pacote completo.

Saída:

- QA score;
- red flags;
- correções exigidas.

---

## 3. Métricas DSPy sugeridas

- `has_autonomous_prompts`;
- `has_clear_cta`;
- `has_evidence_level`;
- `no_aggression_romanticization`;
- `visual_consistency_score`;
- `mobile_legibility_score`;
- `saveability_score`;
- `shareability_score`;
- `brand_fit_score`.

---

## 4. Exemplos de treinamento

Usar exemplos aprovados pelo usuário como few-shot.

Campos por exemplo:

```json
{
  "theme": "Socialização do filhote Cane Corso",
  "approved_hook": "Socializar não é soltar no mundo",
  "winning_cta": "Comente SOCIALIZAÇÃO para receber o checklist",
  "visual_notes": "2.5D premium, couro, bronze, cão calmo",
  "performance": {
    "saves": 0,
    "shares": 0,
    "comments": 0
  }
}
```

---

## 5. Regra

DSPy deve otimizar para qualidade e coerência, não para sensacionalismo.
