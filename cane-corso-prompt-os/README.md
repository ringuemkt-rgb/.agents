# Cane Corso do Cangaço — Prompt Production OS

Sistema profissional, portátil e operacional para produzir **posts, carrosséis, prompts de imagem, legendas, Reels derivados e temas com potencial viral** para a marca **Cane Corso do Cangaço**.

> Filosofia central: **força sob controle, guarda equilibrada, criação responsável e autoridade visual premium.**

Este repositório foi pensado para funcionar em qualquer chat de IA. Basta copiar o conteúdo de `SYSTEM_PROMPT.md` para o chat ou usar `AGENTS.md` como instrução de projeto em ambientes que suportam agentes.

---

## O que este sistema faz

- Estrutura carrosséis com pesquisa, tese, gancho, roteiro e prompts individuais.
- Gera prompts autônomos por slide para Gemini, ChatGPT, Midjourney ou outro gerador visual.
- Mantém identidade visual premium 2.5D da marca.
- Separa fato, evidência, inferência e opinião editorial.
- Cria legenda otimizada para Instagram com CTA, emojis e palavras-chave.
- Produz variações de capa A/B/C.
- Gera Reels e Stories derivados.
- Calcula o **IPV — Índice de Potencial Viral**, uma estimativa estratégica baseada em dor do público, salvamento, compartilhamento, gancho, aderência à marca e segurança de recomendação.
- Mantém um ciclo de autoaperfeiçoamento com base em feedback e métricas reais.

---

## Como usar em qualquer IA

### Opção 1 — Uso rápido

1. Abra `SYSTEM_PROMPT.md`.
2. Copie tudo.
3. Cole no começo de um novo chat de IA.
4. Depois peça:

```text
Faça um carrossel sobre: socialização do filhote Cane Corso.
Siga rigorosamente o Cane Corso do Cangaço Prompt Production OS.
```

### Opção 2 — Uso em agente/projeto

1. Copie `AGENTS.md` para a raiz do seu projeto.
2. Use como instrução permanente do agente.
3. Coloque os templates de `/templates` como arquivos auxiliares.

### Opção 3 — Gerar esqueleto por terminal

```bash
python3 scripts/prompt_pack_generator.py "Socialização do filhote Cane Corso"
```

O script gera um esqueleto de pacote com roteiro, prompts individuais, legenda, CTA e bloco IPV.

---

## Estrutura do repositório

```text
cane-corso-prompt-os/
├── README.md
├── AGENTS.md
├── SYSTEM_PROMPT.md
├── CHANGELOG.md
├── data/
│   └── brand_config.json
├── examples/
│   └── jiu-jitsu-cane-corso-carousel.md
├── scripts/
│   └── prompt_pack_generator.py
└── templates/
    ├── carousel_request_template.md
    ├── instagram_caption_template.md
    ├── ip_viral_scorecard.md
    └── slide_prompt_template.md
```

---

## Princípios rígidos da marca

### O Cane Corso nunca será vendido como

- cão de briga;
- cão raivoso;
- arma de intimidação;
- troféu de status;
- animal demonizado;
- produto de compra impulsiva;
- promessa de cor rara.

### O Cane Corso será comunicado como

- guardião equilibrado;
- cão funcional;
- cão de família;
- animal que exige origem, saúde, temperamento e condução;
- força sob controle;
- compromisso sério.

---

## Fórmula de performance

Todo conteúdo deve buscar pelo menos um destes sinais:

1. Salvamento.
2. Compartilhamento.
3. Comentário qualificado.
4. Direct.
5. Lead.
6. Aumento de autoridade.

A fórmula-base:

```text
gancho forte + verdade técnica + visual premium + frase salvável + CTA filtradora + análise de métrica
```

---

## Observação importante

O sistema não promete viralização matemática. O **IPV** é uma pontuação estratégica, não garantia. Ele serve para priorizar temas com maior probabilidade de gerar sinais positivos de alcance e engajamento.

---

## Status

Versão: `v3.0.0`

Status: **operacional**
