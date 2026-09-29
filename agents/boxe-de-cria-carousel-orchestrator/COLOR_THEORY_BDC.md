# Teoria das cores BOXE DE CRIA v2.0

Não é chakra. Não é “cor que vende”. É **contraste + hierarquia + semântica de marca + acessibilidade + teste**.

HEX somente de PALETTE_CANON.md.

## 1. O que a cor deve fazer

1. Separar figura e fundo.
2. Priorizar a informação principal.
3. Agrupar classes visuais.
4. Sinalizar papel editorial.
5. Manter reconhecimento BDC.
6. Sobreviver ao telemóvel, compressão e daltonismo.

Se a cor não faz uma dessas coisas, é decoração.

## 2. Anti-folclore

A literatura de psicologia da cor mostra efeitos dependentes de contexto, cultura, tarefa, saturação e valor.

Portanto:
- NÃO “azul = confiança universal”;
- NÃO “vermelho = compra/urgência automática”;
- NÃO “verde acalma o sistema nervoso”;
- NÃO “ouro ativa status no cérebro”.

BDC usa associações aprendidas dentro da própria marca.

## 3. Campo = silêncio visual

CHARCOAL #0B0B0D
GRAPHITE #121317
TECH GRAY #23252B

Petroleum P900–P500 = ambiente científico.
Chrome da marca continua charcoal/graphite.

WARM WHITE #F3F0EA = texto-base.

## 4. Semântica BDC

| Cor | Papel da marca | Uso |
|---|---|---|
| Gold #D4A017 | identidade/ownership | keyword, wordmark, rail |
| Cyan #3EC6C9 | método/evidência | node, blueprint, chip |
| Bronze #C08F3C | metal/prova | hairline/chip |
| Red #C62828 | alerta/blocked claim | 1 palavra/card |
| Terra #B85C38 | lugar/Bahia | Terreiro/local |
| Amber #E0A259 | transição/luz | edge/handoff |
| Warm white | voz | body/sub |

Isto é convenção BDC, não lei universal de psicologia.

## 5. Acorde principal

Gold × Cyan sobre dark neutral.

Máximo 2 acentos principais.

## 6. Accent budget

- dark neutrals: 80–88%;
- accent 1: 8–12%;
- accent 2: 4–6%;
- red: ≤8%.

## 7. Isolation

Uma palavra ou número pode receber acento para isolamento visual.

Não destacar 5 coisas.
Se tudo é destaque, nada é.

## 8. Data-viz

Cor nunca é o único canal.
Adicionar:
label, shape, dash, position ou icon.

No 3D charts.

## 9. Criago

Não recolorir pelagem.
Jaqueta preta.
Óculos âmbar.
Patch ouro.
Bandeiras em cores reais.

## 10. Modes

EDITORIAL_DEFAULT — gold + cyan.
RING_LIGHT — more gold.
LAB — petroleum + cyan.
ALERT — red controlled.
TERREIRO — terra + gold.
NIGHT — night blue + restrained gold/cyan.

Um mode por slide.

## 11. A11Y

Herdar ACCESSIBILITY_CONTRAST.md:

body ≥4.5:1
headline target ≥7:1
meaningful graphics ≥3:1

Evitar:
- gray #808080 body;
- red body;
- gold on tan/terra;
- white on gold plate;
- hue-only comparisons.

## 12. Grayscale test

Se A vs B desaparece em grayscale, adicionar outro canal.

## 13. Fence block

```text
COLOR THEORY BDC:
dark field;
gold=identity;
cyan=method;
red=alert;
bronze=metal;
max 2 accents;
red ≤8%;
one isolated keyword;
A11Y verified;
grayscale backup;
NO universal color psychology;
NO brain-color claims.
```
