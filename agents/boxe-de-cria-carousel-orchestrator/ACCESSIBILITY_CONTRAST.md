# Contraste acessível — WCAG 2.2 no slide BDC

Instagram não audita WCAG. O polegar e daltonismo sim.
Padrão de trabalho: **WCAG 2.2 nível AA** no texto da arte; AAA na headline.
eMAG (Brasil, setor público) aponta para WCAG — não é lei deste feed.

## Critérios

| ID | Nível | Regra |
|---|---|---|
| 1.4.3 | AA | texto normal ≥4.5:1; texto grande ≥3:1 |
| 1.4.6 | AAA | texto normal ≥7:1; grande ≥4.5:1 |
| 1.4.11 | AA | gráfico / ícone / eixo que *informa* ≥3:1 com o vizinho |

Texto grande WCAG: ≥18 pt (~24 px web) ou ≥14 pt bold. No 4:5 1080, trata headline Anton e cards 38px+ bold como *large*; micro 28–32 px como *normal* → exige 4.5:1.

Fórmula 2.x: (L1+0.05)/(L2+0.05). WCAG 3 / APCA ainda não é requisito.

Imagem-de-texto (todo o carrossel Gemini) cai em 1.4.3/1.4.6 na prática: o contraste *dentro* do PNG é o que o olho tem.

## Cânone BDC vs o padrão (já medido)

| Par | Razão | AA texto normal | AAA headline |
|---|---|---|---|
| `#F3F0EA` em `#0B0B0D` | 17.3 | passa | passa |
| `#3EC6C9` em `#0B0B0D` | 9.5 | passa | passa |
| `#D4A017` em `#0B0B0D` | 8.3 | passa | passa |
| `#C08F3C` em `#0B0B0D` | 6.8 | passa AA | falha AAA |
| `#C62828` em `#0B0B0D` | 3.5 | falha corpo | só large |
| ciano em P500 `#174957` | 4.8 | limite AA | não AAA |
| ouro em tan/terra | <2 | falha | falha |
| branco em placa ouro | 2.1 | falha | falha |

## Lei de produção

- Corpo e source footer: só `#F3F0EA` no carvão/graphite.
- Headline: branco, ouro ou ciano no carvão — não bronze se quiseres AAA.
- Vermelho: palavra ≥ large, nunca parágrafo.
- Node / seta / barra de gráfico: ≥3:1 com o fundo (1.4.11). Não distingas séries só por ouro vs terra.
- Ícone ALERT + label escrito (cor não é o único canal — 1.4.1 Use of Color).

## QA no fence 21/22

```text
A11Y: body text ≥4.5:1 | headline ≥7:1 | graphics ≥3:1
FAIL if gold on tan, red body text, gray #808080, legend hue-only
```
