# Viral Engine — o que faltava para o prompt ser mais forte no feed

Viral não se garante. Este módulo sobe probabilidade de **parar o dedo / salvar / mandar no grupo da academia** sem mentir evidência.

Hierarquia: Claim Lock > STYLE LOCK > este motor > humor.

## 1. Física da plataforma (Instagram carrossel 4:5)

- Slide 1 tem ~1,5–3 s. Se a tese não cabe em 7 palavras, morreu.
- Grelha do perfil corta o topo e a base: headline no terço médio-alto, não na safe só de arte.
- Som off. Texto é o áudio.
- Métrica que importa para este brand: **salvamentos + compartilhar no directo**, não só like.
- Slide 1 ≠ capa de Reels. Se fores recortar 1:1 depois, testa o centro.

No fence 1:
`STOP TEST: 7 words readable at grid thumbnail`

## 2. Objecto social (porque é que alguém manda)

Um carrossel viral neste nicho é quase sempre UM destes:

| Objecto | Frase que o viewer encaminha |
|---|---|
| Utilidade | “toma o protocolo” |
| Identidade | “isso é a gente” |
| Status de quem sabe | “vê, não é o que o influencer disse” |
| Correção de mito | “te falei que isso frita o ombro” |
| Pertencer ao lugar | “Bahia não é laboratório” |

Obrigatório no dossiê, antes dos fences:
`SHARE_LINE: "[frase de 8–14 palavras que cabe no WhatsApp]"`
`SHARE_JOB: utility | identity | status | mythbust | place`

Sem SHARE_LINE o prompt é bonito e mudo.

## 3. Emoção única

Um carrossel, uma temperatura:
ORGULHO | RAIVA_ÚTIL (mito) | CURIOSIDADE | CALMA_DE_MESTRE | URGENCIA_DE_CORPO

Misturar raiva + fofo + aula no mesmo 8-pack dilui.
Criago H-level casa com a temperatura: H0 calma/dano · H1 orgulho · H2 mito · H3 raro.

## 4. Voz (o sistema ainda estava visual demais)

Léxico BDC — preferir: cria, ringue, saco, guarda, volume, recuperação, amador, calor, chão, professor.
Banir no Exact Text Lock: otimizar, performar, mindset, jornada, hack, secreto, comprovado pela ciência, game changer, unlock.

Ritmo de headline: sujeito + verbo + corte. Não gerúndio corporativo.
Certo: “A Bahia não virou Cuba.”
Errado: “Descubra como otimizar sua performance com método científico.”

## 5. Distinctiveness (por que este post não é mais um de boxe)

Antes do hook, uma linha:
`CATEGORY DENIAL: o feed já está cheio de [X]; este post recusa [X] e oferece [Y].`

X típico: fisiculturista, cardápio de hotel, número sem unidade, pose onlyfans, “disciplina” vazia.
Y típico: limite do estudo + chão da Bahia + Criago.

## 6. Dual gate (viral vs rigor)

| Gate | Reprova se |
|---|---|
| RIGOR | tese fora do Claim Lock; número órfão; mecanismo vendido como luta |
| STOP | slide 1 ilegível na grelha; 7+ palavras fracas; sem SHARE_LINE |
| VOZ | palavra banida; tom de curso americano |
| SOMBRA | humilha o amador; xenofobia; medo de morte |

Pode ser APROVADO rigor e FRACO stop — aí reescreve só o Exact Text Lock do slide 1. Não mexer na evidência.

## 7. Sequência entre posts (não só 8 slides)

Viral de marca é série: mito → mecanismo → protocolo → lugar.
Cada carrossel fecha um arco e deixa 1 fio para o próximo post (não para o slide 2 só).
`SERIES_THREAD: [fio de 6 palavras]`

## 8. Bloco extra obrigatório em TODO fence 1

```text
VIRAL LOCK
STOP TEST: [7 words]
SHARE_LINE: "..."
SHARE_JOB: identity|utility|mythbust|status|place
EMOTION: ORGULHO|... 
CATEGORY DENIAL: feed=X / nós=Y
SERIES_THREAD: ...
```
