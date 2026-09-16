# External AI stack — GitHub + Hugging Face

Usar estrutura e tools. Nunca copiar estilo visual de bibliotecas genéricas.
Identidade = STYLE_LOCK_EDITORIAL_BOXE.md + PALETTE_MODES.md.

## A. Montar o prompt de imagem (Gemini)

| Recurso | URL | O que roubar |
|---|---|---|
| Gemini Image Prompting Handbook (JSON schema) | https://github.com/pauhu/gemini-image-prompting-handbook | validar campos core/style/technical |
| SCHEMA paper Gemini 3 Pro Image | https://arxiv.org/abs/2602.18903 | BASE/MEDIO/AVANZATO; info-design >95% com estrutura |
| PromptCrates SAT | https://github.com/promptcrates/prompt-frameworks | Subject · Atmosphere · Technical; mudar 1 camada por revisão |
| FLUX skills JSON | https://github.com/black-forest-labs/skills | JSON → prosa; HEX de marca |
| AI Image Bible | https://github.com/AI-BrandFactory/ai-image-bible | payload Gemini vs GPT-Image vs MJ; hex brand |
| awesome-nano-banana-pro-prompts | https://github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts | só estudar géneros (infographic, poster). NÃO colar o prompt |

Gramática: Gemini/FLUX leem **frase**. SDXL/MJ leem tags. O fence BDC é prosa estruturada em 56 blocos, não tag soup.

## B. Perícia / papers (GitHub)

ASReview, pyalex, MetaScreener, ReviewAid, EvidenceEngine, RobotReviewer, Critiplot, robvis, research-pipeline (OpenAlex+S2+HF daily papers).
Detalhe em OSS_FORENSIC_STACK.md.

## C. Hugging Face — útil de verdade

| Recurso | Uso BDC |
|---|---|
| Dataset **EBM-NLP / EBM-PICO** | treino/ref de extração PICO; não gerar slide com ele |
| **SPECTER2** / sentence-transformers científicos | similaridade entre papers (família / living review) |
| **SciBERT** / BiomedNLP | NER biomédico se extraíres PDF local |
| HF Daily Papers | fonte extra no Unbounded Search, não teto |
| Models de imagem HF (FLUX, SD) | **off** no fluxo oficial — alvo é Gemini 4:5 |

## D. Ordem de montagem do material completo

1. Perícia (OpenAlex/PubMed ± ASReview ± átomos ± GRADE) → Claim Lock
2. SAT: Subject (herói+Criago+cards) / Atmosphere (PALETTE MODE + luz) / Technical (4:5 2160×2700)
3. Injetar STYLE LOCK inteiro + Exact Text Lock
4. Um fence por slide → Gemini
5. Revisão: mudar SÓ Subject OU Atmosphere, nunca os dois + Technical
