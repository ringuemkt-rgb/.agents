# BDC RED TEAM & EVALUATION ENGINE v1.0

## Missão

Um agente cria. Outro tenta reprovar.

O Red Team não reescreve a tese para ficar mais bonita; procura o ponto em que ela quebra.

## 1. Red Team questions

EVIDENCE
- Qual claim é mais forte que o desenho do estudo?
- População do estudo corresponde ao público?
- Existe confundimento?
- O mecanismo foi medido ou inferido?
- Há estudos negativos?
- O efeito é clínico/prático ou apenas estatístico?
- A fonte é independente?

HISTORY
- A narrativa comprime escolas diferentes numa só?
- Há mito repetido por mídia sem fonte primária?
- O termo existia na época?
- Estamos projetando categorias atuais no passado?

COMBAT
- A nomenclatura é usada no Brasil?
- A técnica é plausível?
- A regra da modalidade muda a conclusão?
- Confundimos estilo individual com escola?

VISUAL
- A imagem sugere causalidade não suportada?
- Um gráfico decorativo parece dado real?
- Seta, heatmap ou anatomia parecem medição?
- A comparação parece ranking sem base?

COPY
- O hook promete mais do que o slide entrega?
- Existe clickbait?
- Existe humilhação?
- Existe certeza falsa?

## 2. Source provenance ledger

Para cada claim material:

```text
CLAIM_ID
claim_text
source_type
source_id / DOI / PMID / archive
population
design
date
directness
risk_of_bias
independence
what_measured
what_not_measured
applicability
certainty
allowed_wording
blocked_wording
```

Esse ledger pode ficar interno; não encher o slide.

## 3. Evaluation card — dimensões separadas

Nunca produzir "nota científica total" misturando tudo.

Avaliar 0–3 por dimensão operacional:
- evidence integrity;
- claim discipline;
- didactic clarity;
- visual hierarchy;
- mobile legibility;
- A11Y;
- 2.5D compliance;
- brand fidelity;
- originality;
- share utility;
- save utility;
- caption alignment.

0 = fail
1 = weak
2 = acceptable
3 = strong

A nota é QA editorial, não medida científica de qualidade.

## 4. Originality guard

Referência externa pode fornecer:
- função;
- tipo de narrativa;
- categoria de diagrama;
- problema de design.

Não copiar:
- grid específico;
- tipografia distintiva;
- paleta distintiva;
- composição 1:1;
- frase;
- marca;
- personagem;
- sequência única.

Teste:
"Se removermos a logo BDC, isto ainda parece claramente a peça de outra página?"
Se sim, reprovar e reconstruir.

## 5. Falsification gate

Antes da tese final:
- o que faria esta tese ser falsa?
- existe evidência desse cenário?
- qual interpretação rival explica os mesmos dados?
- qual evidência falta para decidir?

Se não houver resposta, o sistema está defendendo narrativa, não investigando.

## 6. Pre-publication adversarial review

Simular quatro leitores:
- pesquisador cético;
- treinador experiente;
- fisioterapeuta;
- iniciante.

Para cada um: "qual erro você apontaria primeiro?"

Corrigir o erro que for factual, de clareza ou técnica. Não diluir verdade só para agradar todos.

## 7. Gate

APROVADO:
- zero P0/P1;
- Claim Lock preservado;
- visual não exagera;
- autonomia completa.

APROVADO_COM_RESSALVAS:
- incerteza real explicitada;
- P2/P3 documentado;
- sem risco factual.

REPROVADO:
- dado inventado;
- overclaim;
- técnica/anatomia inválida;
- logo/Criago drift;
- 3D;
- A11Y grave;
- prompt não autônomo.
