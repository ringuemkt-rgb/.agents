# BDC AUDIENCE & DEMAND INTELLIGENCE ENGINE v1.0

## Missão

Descobrir **o que vale a pena explicar agora**, antes da perícia científica.

O sistema não deve começar por “qual tema parece interessante?”. Deve começar por:

```text
QUEM ESTÁ PERGUNTANDO?
→ O QUE ESTÁ PERGUNTANDO?
→ COMO FORMULA A DÚVIDA?
→ QUAL DOR / DESEJO EXISTE?
→ QUAL TAREFA ELA ESTÁ TENTANDO RESOLVER?
→ QUAL INTENÇÃO?
→ QUAL DEMANDA / RECORRÊNCIA?
→ QUAL GAP DE CONTEÚDO?
→ ONDE A BOXE DE CRIA TEM VANTAGEM REAL?
```

A camada de audiência NÃO substitui Evidence. Ela decide qual pergunta merece investigação.

---

## 1. Princípio

Separar:

- **demand truth** = existe procura, dúvida ou dor real;
- **evidence truth** = a resposta é sustentada por evidência;
- **editorial fit** = BDC é a marca certa para responder;
- **timing** = vale responder agora.

Nunca usar demanda para validar uma afirmação científica.

---

## 2. Audience Map — segmentação por problema, não demografia rasa

### Persona operacional mínima

```yaml
persona_id:
role: iniciante|intermediario|competidor|treinador|pai_mae|profissional_saude|pessoa_autista|fan|comprador
combat_context:
experience_level:
primary_problem:
desired_outcome:
fear_or_objection:
language_examples:
knowledge_level:
decision_stage:
content_jobs:
```

### Segmentos padrão BDC

#### INICIANTE
Perguntas típicas:
- como começar;
- medo de apanhar;
- condicionamento inicial;
- equipamento;
- vergonha;
- primeira aula;
- técnica básica.

#### INTERMEDIÁRIO
- gás;
- timing;
- base;
- jab;
- potência;
- sparring;
- defesa;
- recuperação;
- platô.

#### COMPETIDOR
- periodização;
- peso;
- recuperação;
- estratégia;
- adversário;
- potência;
- concussão;
- carga;
- performance.

#### TREINADOR
- progressão;
- didática;
- correção de erro;
- segurança;
- periodização;
- iniciante;
- criança;
- TEA;
- feedback.

#### PAIS / RESPONSÁVEIS
- segurança;
- agressividade;
- idade;
- TEA;
- benefícios;
- lesão;
- ambiente.

#### PESSOA AUTISTA
- sensorial;
- rotina;
- previsibilidade;
- comunicação;
- interação social;
- coordenação;
- ambiente;
- fadiga.

#### FISIO / PROFISSIONAL
- lesão;
- retorno;
- carga;
- avaliação;
- biomecânica;
- prevenção;
- evidência.

---

## 3. Query Mining Engine

Fontes possíveis quando tecnicamente acessíveis:

### Search
- autocomplete;
- People Also Ask;
- related searches;
- Trends;
- Search Console;
- consultas do site.

### Social
- YouTube autocomplete;
- YouTube comments;
- Instagram comments;
- TikTok comments;
- Reddit/forums;
- perguntas em lives;
- DMs autorizadas;
- comentários no próprio BDC.

### Competitor surface
- comentários perguntando algo que o post não respondeu;
- claims repetidos sem fonte;
- dúvidas recorrentes;
- conteúdos desatualizados;
- temas tratados de forma superficial.

Nunca coletar dado privado sem autorização.

---

## 4. Query Atom

Toda pergunta real deve virar um átomo estruturado:

```yaml
query_id:
raw_query:
normalized_query:
source_surface:
date_observed:
language_variant:
persona_guess:
intent:
pain:
desire:
jtbd:
topic:
subtopic:
freshness:
evidence_needed:
privacy_status:
notes:
```

Preservar `raw_query` do jeito que a pessoa escreveu.

Exemplo:

```yaml
raw_query: "pq meu braço fica pesado no boxe"
normalized_query: "por que o braço fica pesado durante o boxe?"
intent: FIX
pain: fadiga percebida no membro superior
jtbd: sustentar combinações sem quebrar técnica
```

---

## 4.1 Query Family Resolver

Antes de contar recorrência, agrupar variantes semanticamente equivalentes.

Exemplo:

```text
"meu gás acaba"
"canso rápido no boxe"
"fico sem ar no sparring"
"não aguento 3 rounds"
```

podem pertencer ao cluster:

`FADIGA / PACING / RESPIRAÇÃO`

Mas não fundir prematuramente perguntas com soluções diferentes.

Guardar:
- canonical_question;
- variants;
- surface_count;
- unique_surface_count;
- first_seen;
- last_seen;
- geography quando explícita;
- persona distribution;
- intent distribution.

### Duplicate-demand rule

Não contar:
- mesma pergunta copiada por bots;
- reposts automáticos;
- um único vídeo viral replicado como “múltiplas fontes”;
- resultados de busca que apenas citam a mesma origem.

Demanda independente é mais informativa que repetição algorítmica.

---

## 4.2 Signal Quality

Cada sinal recebe qualidade descritiva:

- SOURCE OWNED / PLATFORM / OPEN WEB / FORUM / COMPETITOR;
- timestamp;
- sample bias;
- whether count is known;
- whether audience identity is known;
- whether signal is independent.

Nunca converter um comentário popular em “mercado inteiro”.

---

## 4.3 Geography Layer

Quando relevante, separar:

- BRASIL;
- NORDESTE;
- BAHIA;
- BAIXO SUL;
- município;
- global/lusófono.

Não localizar artificialmente todo tema.

Uma query local pode ter alto valor estratégico mesmo com baixo volume absoluto.

---

## 4.4 Awareness / Decision Stage

Classificar quando útil:

- UNAWARE;
- PROBLEM_AWARE;
- SOLUTION_AWARE;
- OPTION_AWARE;
- DECISION_READY;
- POST_PURCHASE / PRACTITIONER.

Isso muda:
- profundidade;
- CTA;
- vocabulário;
- necessidade de comparação;
- necessidade de prova.

---

## 5. Search Intent Classifier

Classificar uma intenção principal e, quando útil, uma secundária:

- LEARN
- UNDERSTAND
- FIX
- PREVENT
- START
- IMPROVE
- COMPARE
- DECIDE
- BUY
- BELONG
- VERIFY
- FOLLOW_EVENT
- FIND_LOCAL

Exemplos:

“boxe ou jiu-jitsu para autista?”
→ COMPARE + DECIDE

“como respirar no sparring?”
→ FIX + IMPROVE

“luva 14 ou 16 oz?”
→ BUY + DECIDE

---

## 6. Pain & Desire Ontology

Distinguir cinco níveis:

```text
SURFACE QUESTION
→ DECLARED PAIN
→ FUNCTIONAL PROBLEM
→ USER THEORY
→ POSSIBLE CAUSES
→ DESIRED OUTCOME
```

Exemplo:

```text
Q: "por que meu gás acaba?"
PAIN: cansaço precoce
FUNCTIONAL: não sustenta ritmo
USER THEORY: "meu cardio é ruim"
POSSIBLE CAUSES: pacing, tensão, técnica, ansiedade, capacidade aeróbia, descanso
DESIRED: manter ritmo sem desmontar
```

O hook pode explorar a diferença entre USER THEORY e POSSIBLE CAUSES, mas a resposta só entra após investigação.

---

## 7. Jobs To Be Done

Para cada query:

```text
WHEN [contexto]
I WANT TO [tarefa]
SO I CAN [resultado funcional/identitário]
WITHOUT [medo/custo]
```

Exemplo:
“qual luva comprar?”
→ Quando começo boxe, quero escolher a luva certa para treinar com segurança e não gastar errado, sem parecer completamente perdido.

Isso melhora CTA, vocabulário e utilidade.

---

## 8. Audience Lexicon

Guardar linguagem real em três colunas:

| Público fala | Termo técnico | Copy BDC |
|---|---|---|
| “meu braço pesa” | fadiga local/percepção de esforço | “Por que seu braço pesa no 2º round?” |
| “fico duro no sparring” | co-contração/tensão excessiva | “Você está lutando ou travando?” |
| “não consigo entrar” | gestão de distância/entry | “Seu problema pode começar antes do soco.” |

Regra:
não corrigir o público com arrogância.
Traduzir sem ridicularizar.

---

## 9. Comment Mining

Separar comentário em:

- QUESTION;
- CONFUSION;
- OBJECTION;
- PERSONAL EXPERIENCE;
- REQUEST;
- MYTH;
- EQUIPMENT;
- LOCAL;
- SAFETY;
- EMOTION;
- META.

Não tratar experiência pessoal como evidência causal.

Uma alta recorrência de comentário = sinal de demanda, não prova de verdade.

---

## 10. Competitor Gap Mining

Objetivo não é copiar.

Procurar:

- claim sem fonte;
- explicação rasa;
- pergunta não respondida;
- comentário recorrente;
- material desatualizado;
- ausência de contexto brasileiro;
- ausência de aplicação prática;
- excesso de jargão;
- mito repetido;
- formato visual confuso.

Saída:

```yaml
gap_type:
competitor_claim:
audience_question:
what_is_missing:
bdc_advantage:
original_angle:
copy_risk:
```

---

## 11. BDC Expertise Moat

Prioridade aumenta quando o tema cruza duas ou mais competências proprietárias:

- boxe;
- fisioterapia;
- biomecânica;
- ciência do esporte;
- autismo;
- didática;
- história das lutas;
- Bahia / realidade local;
- cultura de academia.

Moat não significa exclusividade jurídica. Significa espaço editorial onde BDC pode entregar mais nuance que conteúdo genérico.

---

## 12. Demand Evidence Levels

Não inventar volume.

Classificar:

### D0 — ANECDOTAL
Uma pergunta isolada.

### D1 — REPEATED
A mesma dúvida aparece repetidamente em comentários/consultas.

### D2 — CROSS-SURFACE
Aparece em ≥2 superfícies independentes.

### D3 — PLATFORM SIGNAL
Há dado de Trends/Search Console/analytics ou tendência observável da plataforma.

### D4 — OWNED AUDIENCE SIGNAL
Dados reais do próprio BDC: comentários, search, DMs autorizadas, site, analytics.

Nunca converter D0–D4 em volume absoluto sem dado.

---

## 13. Freshness Class

- F0 EVERGREEN — muda lentamente.
- F1 PERIODIC — regras/estudos podem mudar em meses/anos.
- F2 ACTIVE — evento/atleta/regulamento atual.
- F3 BREAKING — notícia/polêmica/resultado recente.

F2/F3 exigem busca atual no momento da produção.

---

## 13.1 Question Coverage Matrix

Cruzar clusters de pergunta com cobertura BDC:

| Cluster | Demand | BDC content | Evidence freshness | Gap |
|---|---|---|---|---|
| gás | D? | strong/weak/none | current/stale | yes/no |
| sparring | D? | ... | ... | ... |

Status:
- COVERED_STRONG;
- COVERED_STALE;
- COVERED_WEAK;
- MISSING;
- HIGH_OPPORTUNITY.

Usar para dominar um território por cobertura de dúvidas, não por quantidade de posts.

---

## 14. Audience-Demand Output

Antes da perícia, produzir internamente:

```yaml
audience:
persona:
raw_queries:
primary_intent:
secondary_intent:
declared_pain:
functional_problem:
desire:
jtbd:
lexicon:
demand_level:
freshness:
competitor_gap:
bdc_moat:
candidate_question:
why_now:
query_family:
unique_surface_count:
awareness_stage:
geography:
coverage_status:
signal_quality_notes:
```

---

## 15. Guardrails

Proibido:
- inventar Google Trends/search volume;
- dizer “milhares buscam” sem fonte;
- usar dado privado;
- inferir diagnóstico de comentário;
- usar medo de saúde como exploração;
- transformar popularidade em evidência;
- copiar concorrente;
- inferir preferência política/religiosa/saúde sensível para targeting.

---

## 16. Handoff

Saída desta camada alimenta:

```text
TOPIC_OPPORTUNITY_ENGINE
→ FORENSIC TIER ROUTER
→ INVESTIGATIVE SYNTHESIS
```

Se a demanda for alta mas a evidência for fraca, o conteúdo pode virar:
“o que sabemos / o que não sabemos” — nunca uma resposta inventada.
