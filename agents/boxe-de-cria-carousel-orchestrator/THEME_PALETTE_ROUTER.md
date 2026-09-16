# Router tema → paleta

Uma marca. Seis climas. O tema escolhe a **sequência de modos**, não uma paleta nova.
HEX só PALETTE_CANON.md. Viral = STOP + SHARE no nicho cria, não “cor que o algoritmo ama”.

## Os 6 climas (não inventar o 7.º)

| MODE | Par | Sensibilidade no feed |
|---|---|---|
| RING_LIGHT | ouro alto | capa, ícone, fecho — currency |
| EDITORIAL_DEFAULT | ouro + ciano | tese mista |
| LAB | ciano + petroleum | método, número, GRADE |
| ALERT | vermelho pontual | mito, correção, unidade errada |
| TERREIRO | terra + ouro | Bahia, cria, chão |
| NIGHT | azul baixo + ouro baixo | volume, sono, recuperação |

## Famílias de tema → rota de 8 slides

### A — MITO / CORREÇÃO (soco kg, “autismo leve”, biohack)
Job: mythbust. Emoção: RAIVA_ÚTIL.
`1 RING · 2 ALERT · 3 LAB · 4 LAB · 5 ALERT · 6 TERREIRO · 7 LAB · 8 RING`
Porquê: vermelho no 2 e 5 (o erro). Ciano no meio (a conta). Ouro no 1 e 8 (ainda somos nós).

### B — MECANISMO / CIÊNCIA (pressão, jab, TEA com ressalva)
Job: authority. Emoção: CURIOSIDADE.
`1 RING · 2 DEFAULT · 3 LAB · 4 LAB · 5 LAB · 6 TERREIRO · 7 LAB · 8 RING`
Sem ALERT a menos que haja frase proibida a desmontar. TEA: zero vermelho de “doença”.

### C — LUGAR / IDENTIDADE (Bahia×Cuba, Criago, autismo do criador)
Job: identity. Emoção: ORGULHO.
`1 RING · 2 TERREIRO · 3 DEFAULT · 4 LAB · 5 TERREIRO · 6 TERREIRO · 7 DEFAULT · 8 RING`
Terra no 2/5/6. Ciano só quando entra método.

### D — PROTOCOLO / UTILIDADE (3 rounds, 7 dias no saco)
Job: utility. Emoção: CALMA_DE_MESTRE.
`1 RING · 2 LAB · 3 LAB · 4 LAB · 5 DEFAULT · 6 TERREIRO · 7 LAB · 8 RING`
Save vive no 7 LAB (número + passo).

### E — DANO / VOLUME / CALOR / RECUPERAÇÃO
Job: utility + mythbust leve. Emoção: URGÊNCIA_DE_CORPO.
`1 RING · 2 ALERT · 3 LAB · 4 NIGHT · 5 NIGHT · 6 TERREIRO · 7 LAB · 8 RING`
NIGHT no pico fisiológico. ALERT só no mito (“mais round = mais duro”).

### F — ÍCONE / HISTÓRIA (Popó, 110 rounds, escola)
Job: identity + story. Emoção: ORGULHO ou CURIOSIDADE.
`1 RING · 2 DEFAULT · 3 DEFAULT · 4 LAB · 5 TERREIRO · 6 DEFAULT · 7 LAB · 8 RING`
Sem NIGHT. Sem órgão neon.

### G — COMPARAÇÃO A vs B (cuba vs bahia, kg vs N, hotel vs cria)
Job: mythbust ou status. Gramática SPLIT no 2 ou 4.
`1 RING · 2 SPLIT(LAB|ALERT) · 3 LAB · 4 SPLIT ou LAB · 5 ALERT · 6 TERREIRO · 7 LAB · 8 RING`

### H — PRODUTO / FIGHTWEAR
Só 1/10 dos posts. `1 RING · resto DEFAULT` · ouro no objeto, ciano se houver tese técnica. Sem ALERT de desconto.

## Como a IA escolhe

1. Classificar o tema numa letra A–H.
2. Copiar a rota de 8.
3. Se o slide 2 não for mito, não forçar ALERT.
4. Sempre 1 e 8 RING — Public + fecho ouro (peak-end).
5. Nunca 8 slides ALERT. Nunca 8 slides NIGHT.
6. SPLIT usa dois climas *no mesmo frame*; não conta como 7.º modo.

## O que sobe hop (não é magia)

- Mito: ALERT no 2 aumenta activação (Berger) *se* o 4 LAB entregar a conta.
- Identidade: TERREIRO no 5–6 dá trigger de lugar.
- Save: LAB no 7.
- Reconhecimento no print: RING no 1 e 8 + ciano nalgum chip.

Paleta nova “porque o tema é água / fogo / chakras” = REPROVA.

## Bloco no Viral Brief

```yaml
theme_family: A|B|C|D|E|F|G|H
palette_route: [RING, ALERT, LAB, LAB, ALERT, TERREIRO, LAB, RING]
slide_modes: {1: RING_LIGHT, 2: ALERT, ...}
```
