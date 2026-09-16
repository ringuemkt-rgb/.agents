# BDC Cross-Study Intelligence & Unbounded Evidence Mapper v1.0.0

Módulo irmão de `EVIDENCE_SYNTHESIS.md`. Entra **antes** do Editorial Claim Lock.

Missão: mapear o corpo de evidência sem teto artificial de páginas, ligar achados entre estudos independentes e escrever uma conclusão coerente em português claro.

## Lei de busca sem teto

A IA que executar este pacote **não pode** impor limite próprio de:

- número de páginas de resultado;
- “top 10” / “primeiros 20 hits”;
- uma única base (só PubMed, só Google, só memória do modelo);
- uma única língua;
- uma única passagem de busca.

Parar só é lícito quando o **critério de saturação** for atingido e registrado — nunca porque “já deu”.

Isto não é milagre: o host ainda tem teto de ferramenta, cota e tempo. O contrato obriga a **não inventar um teto editorial** e a **continuar em lotes** até saturação ou até documentar o que restou sem varrer.

## 1. Unbounded Search Mandate

```yaml
search_policy: UNBOUNDED_UNTIL_SATURATION
forbidden:
  - max_pages: any_self_imposed
  - max_results: any_self_imposed_without_saturation
  - stop_after_first_page
  - stop_after_nice_quote
required:
  - multi_source
  - multi_language
  - multi_pass
  - contradiction_pass
  - missing_evidence_pass
  - continuation_batches
```

Fontes mínimas quando a ferramenta existir:

- PubMed / MEDLINE
- PMC full text
- Cochrane Library
- Epistemonikos
- OpenAlex / Semantic Scholar
- Crossref / DOI
- ClinicalTrials.gov + registros WHO ICTRP
- Scopus/Web of Science se existirem
- guidelines (IOC, AMSSM, ACSM, ISSN, NICE, WHO, federações)
- errata / retraction watch / PubPeer quando material
- literatura PT-ES-EN (não só inglês)

Cada lote de busca deve registrar:

```yaml
batch_id:
query:
source:
date_cut:
hits_seen:
new_unique_study_families:
new_contradictions:
new_harms:
stop_or_continue: CONTINUE | SATURATED | TOOL_LIMIT
residual_queries:
```

Se a ferramenta paginar, a regra é: **pedir a página seguinte** até saturação. Se a ferramenta recusar, declarar `TOOL_LIMIT` e o espaço residual — não fingir que o tema acabou.

## 2. Saturação (quando pode parar)

Saturação = as três últimas passagens **não** acrescentaram:

1. nova study family independente relevante;
2. novo outcome crítico;
3. nova contradição material;
4. novo dano/burden relevante;
5. evidência mais direta para a população-alvo.

Marcas de **não-saturação** (obrigam continuar):

- só reviews citando os mesmos primários;
- só abstracts;
- só uma língua;
- nenhum pass D (contradição);
- nenhum registro de trial;
- população-alvo (boxe amador, idade, sexo, regra) ainda sem busca dedicada.

## 3. Evidence Inventory (mapa de tudo que entrou)

Antes de concluir, inventariar:

```yaml
inventory_id:
question:
date_cut:
n_hits_screened:
n_publications_examined:
n_study_families:
n_independent_samples:
n_reviews:
n_guidelines:
n_trials_registered_unpublished:
languages:
excluded_with_reason:
coverage_gaps:
```

P0: dizer “a literatura mostra” sem inventory.

## 4. Finding Atomizer

Quebrar cada paper em átomos, não em “o estudo concluiu que”:

```yaml
finding_id:
study_family_id:
publication_id:
population:
design:
exposure_or_intervention:
comparator:
outcome_id:
timepoint:
effect:
ci:
direction:
mechanism_level: 1 | 2 | 3
directness:
rob_domain_notes:
what_it_actually_measured:
what_it_did_not_measure:
```

Um paper pode gerar vários átomos. Um átomo nunca mistura dois outcomes.

## 5. Cross-Study Linkage (constelação)

A inteligência do sistema é **ligar átomos**, não empilhar resumos.

Relações entre findings:

| Relação | Uso |
|---|---|
| REPLICATES | mesma pergunta, amostra independente, mesma direção |
| EXTENDS | follow-up / dose / subgrupo novo |
| MECHANISTICALLY_EXPLAINS | biomecânica/fisio explica um desfecho |
| CONVERGES_INDIRECTLY | métodos diferentes, mesma tese fraca |
| CONTRADICTS_DIRECTLY | mesmo construto, direção oposta |
| CONTRADICTS_APPARENTLY | labels iguais, construtos diferentes |
| MODERATES | efeito muda com idade/sexo/dose/regra |
| CONFOUNDS | terceira variável explica associação |
| SUPERSEDES | evidência mais nova/melhor anula leitura antiga |
| HARMS_OFFSETS_BENEFIT | dano material contra o benefício celebrado |
| APPLIES_CLOSER | evidência mais próxima do boxe/público-alvo |
| DOES_NOT_TRANSFER | salto de população sem declaração de indireção |

Cada ligação:

```yaml
link_id:
from_finding:
to_finding:
relation:
shared_construct:
independence: INDEPENDENT | SAME_TEAM | SAME_COHORT | UNCLEAR
why_the_link_is_valid:
why_it_could_be_spurious:
weight: HIGH | MODERATE | LOW
plain_pt: "em uma frase o que essa ligação muda na leitura"
```

Proibido: “vários estudos confirmam” sem pelo menos uma ligação classificada.

## 6. Bridge Narrative (conclusão que costura)

Ordem obrigatória da costura:

1. O que a pergunta pedia.
2. Quais átomos são **diretos** para boxe / público.
3. Quais átomos só sustentam **mecanismo**.
4. Onde estudos independentes **convergem**.
5. Onde divergem e **por que** (população, dose, instrumento, viés).
6. O que isso permite dizer em uma frase honesta.
7. O que um professor/aluno pode aplicar amanhã sem distorcer.
8. O que mudaria a frase.

Modelo de parágrafo (PT-BR fácil):

> Os estudos que medem [outcome X] em [população] apontam [direção], com certeza [GRADE].  
> Isso **não** é o mesmo que [outcome Y], medido por [estudo B].  
> O estudo C ajuda a entender o **como** (mecanismo), mas sozinho não prova o resultado no ringue.  
> O estudo D parece contradizer A; a diferença está em [dose/idade/instrumento], não em “a ciência brigou”.  
> Por isso a frase segura é: [Claim Lock].  
> Se aparecer um RCT em boxe com [N/desfecho], essa frase sobe ou cai.

## 7. Easy Explanation Compiler

Toda conclusão integrada gera **três camadas de fala**, sem mudar o conteúdo:

- **3 segundos:** uma frase que um aluno cansaço entende.
- **30 segundos:** mecanismo + ressalva.
- **3 minutos:** costura entre estudos + o que não sabemos.

Regras de clareza:

- verbo concreto; sem “impacta positivamente o paradigma”;
- número só com unidade, população e incerteza;
- analogia de academia/ringue permitida se não virar prova;
- nunca traduzir SMD em “X% mais forte” sem transformação válida.

## 8. Completeness Ledger

```yaml
question:
saturation_status: SATURATED | PARTIAL | TOOL_LIMIT | INSUFFICIENT_HOST
pages_traversed: unbounded_batches
self_imposed_page_cap_used: false
languages_covered:
contradiction_pass_done: true
registry_pass_done:
cross_study_links_n:
unresolved_queries:
what_was_not_opened:
honesty_note:
```

`self_imposed_page_cap_used: true` é falha P0.

## 9. Falhas P0 deste módulo

1. Parar na primeira página “porque já achou um review”.
2. Impor teto de páginas/resultados sem saturação.
3. Resumir papers em silos sem ligações.
4. Tratar citação compartilhada como replicação.
5. Costurar mecanismo de um esporte no desfecho de outro sem marcar indireção.
6. Escrever conclusão difícil quando a evidência cabe em frase curta honesta.
7. Omitir o lote residual quando a ferramenta cortou.
8. Usar “a literatura é unânime” com links DIVERGENT ou APPARENTLY contraditórios sem explicar.

## 10. Onde isso entra no pipeline

```text
SEARCH MESH (UNBOUNDED)
→ INVENTORY
→ FINDING ATOMS
→ STUDY FAMILIES
→ CROSS-STUDY LINKS
→ BRIDGE NARRATIVE
→ EASY EXPLANATION (3s / 30s / 3min)
→ INTEGRATED CONCLUSION
→ EDITORIAL CLAIM LOCK
```

O prompt do slide recebe só: tese costurada, certeza, aplicabilidade, ressalva, e a frase de 3 segundos.
