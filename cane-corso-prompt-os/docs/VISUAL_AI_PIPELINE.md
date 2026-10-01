# Visual AI Pipeline

Pipeline visual recomendado para transformar prompts da marca em imagens premium, consistentes e editáveis.

---

## 1. Objetivo

Produzir artes 2.5D premium com:

- identidade visual consistente;
- Cane Corso equilibrado;
- moldura da marca;
- layout editorial;
- menor erro de texto;
- arquivos prontos para Canva/Figma/Photoshop.

---

## 2. Princípio operacional

Para máxima qualidade, preferir:

```text
imagem sem texto → edição final do texto no Canva/Figma
```

Usar texto embutido somente quando:

- headline curta;
- poucos blocos;
- teste rápido;
- baixa exigência tipográfica.

---

## 3. Stack recomendado

### ComfyUI

Motor principal de workflow visual.

Uso:

- workflows por nó;
- lote de imagens;
- controle de etapas;
- versionamento visual.

### FLUX.1

Modelo de geração para:

- fundos premium;
- cenas;
- personagens;
- composição editorial;
- assets sem texto.

### ControlNet

Controle de:

- pose;
- profundidade;
- layout;
- bordas;
- composição.

### IP-Adapter

Consistência com:

- logo;
- mascote;
- cão de referência;
- paleta;
- estilo.

### SAM 2

Uso:

- recortar cão;
- remover fundo;
- separar mascote;
- preparar colagens.

---

## 4. Workflow recomendado

```text
prompt estratégico
→ layout base
→ geração sem texto
→ upscaling
→ recorte/ajustes
→ aplicação de texto no Canva/Figma
→ export 2160x2700
→ QA visual
```

---

## 5. Versão com texto

Usar quando o prompt exigir texto embutido.

Regras:

- poucas palavras;
- letras grandes;
- contraste alto;
- evitar parágrafos;
- não confiar em textos longos gerados por IA.

---

## 6. Versão sem texto

Todo prompt complexo deve gerar também versão sem texto:

Pedir:

- cards vazios;
- selos sem texto;
- barras sem texto;
- espaços reservados;
- molduras limpas;
- área segura;
- ícones sem palavras.

---

## 7. Layout base do carrossel

Cada slide deve conter:

- headline zone;
- visual central;
- blocos laterais;
- selo;
- rodapé;
- assinatura da marca.

No design sem texto, deixar espaços claros para:

- headline;
- subheadline;
- cards;
- CTA;
- rodapé técnico.

---

## 8. Controle de consistência

Usar referências:

- logo oficial;
- mascote tigre;
- Cane Corso preto/cinza;
- paleta;
- brasão;
- textura de couro;
- bronze envelhecido.

Ao usar IP-Adapter, manter:

- mesmo estilo;
- mesma iluminação;
- proporção coerente;
- sem distorção facial/corporal.

---

## 9. QA visual

Reprovar se:

- cão estiver raivoso;
- anatomia estiver errada;
- texto estiver errado;
- estilo parecer pet shop genérico;
- composição estiver poluída;
- fonte ilegível;
- houver arma, sangue ou briga;
- faltar identidade da marca.

---

## 10. Prompt visual mínimo

```text
Criar arte vertical 4:5, 2160x2700 px, ultra nítida, infográfico premium 2.5D, fundo preto fosco/azul-preto, couro, bronze envelhecido, brasão, Cane Corso calmo e vigilante, estética de guardião de família, composição editorial, sem texto ou com áreas reservadas para texto, sem cão raivoso, sem violência, sem aparência infantil.
```

---

## 11. Entrega ideal

Para cada slide:

- prompt com texto;
- prompt sem texto;
- texto final para aplicar manualmente;
- nota de composição;
- negative prompt;
- checklist de revisão.
