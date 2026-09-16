# Casta de campos escuros — petróleo primeiro

O operador prefere fundo azul-petróleo. O símbolo oficial continua preto+branco+ouro.
Nos slides, o L0 é a **casta petróleo**. Chrome (trilhos, logo) pode ficar carvão/preto para o PNG oficial contrastar.

## Campo (L0) — escolher UM por slide

| Grau | HEX centro → borda | Quando |
|---|---|---|
| PETRO_DEEP | `#020A0E` → `#000000` | capa RING, fecho, logo no canto |
| PETRO_LAB | `#06191F` → `#020A0E` | mecanismo, número, TEA |
| PETRO_MID | `#0A232A` → `#04131A` | protocolo, split frio |
| PETRO_NIGHT | `#07080C` + `#1E3A5F` 12% | sono, volume, recuperação |
| CHARCOAL | `#0B0B0D` → `#000000` | se o petróleo comer o ouro |

Vinheta 10–15%. Grain 1.5%. Sem glow de órgão.

## Combinações coerentes (casta)

Cada linha = campo + acento 1 + acento 2 + texto. Máx. 2 acentos.

| Nome da casta | Campo | Acento 1 | Acento 2 | Texto | Tema / hop |
|---|---|---|---|---|---|
| MARCA | PETRO_DEEP | ouro `#D4A017` | — | `#FFFFFF` no símbolo; `#F3F0EA` no pack | capa, merch, Public |
| MÉTODO | PETRO_LAB | ciano `#3EC6C9` | ouro no wordmark | `#F3F0EA` | ciência, save |
| CORTE | PETRO_LAB esq / PETRO_DEEP dir | ciano | vermelho `#C62828` | branco | mito vs conta (SPLIT) |
| CHÃO | PETRO_DEEP | terra `#B85C38` | ouro | `#F3F0EA` | Bahia, cria |
| ALARME | PETRO_DEEP | vermelho palavra | ouro trilhos | `#F3F0EA` | correção |
| NOITE | PETRO_NIGHT | ouro baixo `#C9971C` | ciano 4% | `#F3F0EA` | recuperação |

Não existe casta “neon” nem “fundo claro”.

## Logo no campo petróleo

O PNG oficial é preto. Em petróleo: colocar o símbolo **sem o rectângulo preto** (versão knockout: cabeça branca + wordmark + ouro) OU um selo preto circular/quadrado pequeno atrás do PNG completo.
Nunca recortar a cabeça e pintar de ciano.

## Rota rápida (alinha ao THEME_PALETTE_ROUTER)

- Família A mito → MARCA, ALARME, MÉTODO, MÉTODO, ALARME, CHÃO, MÉTODO, MARCA
- Família B ciência → MARCA, MÉTODO×5, CHÃO, MARCA
- Família C lugar → MARCA, CHÃO, MÉTODO, CHÃO, CHÃO, MÉTODO, MARCA

## Bloco 07 extra

```text
FIELD CASTE: PETRO_LAB
COMBO: MÉTODO
LOGO: official knockout white+gold OR official PNG on black seal
NO recolor of the ratel mark
```
