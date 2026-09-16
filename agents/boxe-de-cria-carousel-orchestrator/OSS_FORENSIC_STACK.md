# OSS Forensic Stack — BOXE DE CRIA Carousel Orchestrator v3.5

Catálogo oficial de software **open-source** para perícia. Não substitui Claim Lock. Acelera busca, triagem, extração e RoB. A IA-host continua responsável por não inventar DOI e por saturar a busca.

Fonte-mãe: [evidencesynthesis-tools/awesome-evidence-synthesis](https://github.com/evidencesynthesis-tools/awesome-evidence-synthesis).

## Lei de uso

1. Ferramenta sugere. Humano ou agente BDC decide inclusão.
2. Nunca auto-excluir paper só porque o screener marcou irrelevante.
3. Extração LLM exige trecho citado (anti-alucinação).
4. RoB automático é hipótese, não nota final.
5. Meta-análise só com dados extraídos compatíveis — nunca fabricar pooled.

## Stack por etapa

| Etapa BDC | OSS | Repo | Papel |
|---|---|---|---|
| Busca / IDs | OpenAlex (`pyalex`), Crossref, PubMed | https://github.com/J535D165/pyalex | paginar sem teto editorial |
| Dedup | ASReview duplicate hide | https://github.com/asreview/asreview | não contar o mesmo título 4 vezes |
| Screening TA | ASReview LAB (Apache 2.0) | https://github.com/asreview/asreview | active learning; Nature Mach Intell 2021 |
| Screening ensemble | MetaScreener | https://github.com/ChaokunHong/MetaScreener | vários LLMs + incerteza |
| Full-text + PICO | ReviewAid | https://github.com/aurumz-rgb/ReviewAid | PDF → campos |
| Extração Cochrane-like | EvidenceEngine | https://github.com/saulmcphd/EvidenceEngine | 2º revisor AI + log |
| RCT filter | RobotSearch | https://github.com/ijmarshall/robotsearch | filtrar o que não é RCT |
| RoB RCT | RobotReviewer | https://github.com/ijmarshall/robotreviewer | input do Risk-of-Bias Router |
| Tabelas PDF | Tabula | https://github.com/tabulapdf/tabula | números fora do PDF |
| Living review | living-review-updater | https://github.com/mattebso/living-review-updater | re-rank; nunca auto-exclude |
| Catálogo | awesome-evidence-synthesis | https://github.com/evidencesynthesis-tools/awesome-evidence-synthesis | descobrir tool nova |

P0 TIER 2/3: OpenAlex/PubMed paginado → triagem → átomos → RobotReviewer se RCT → GRADE por outcome.

Não clonar ASReview no hub por default (`enabled: false` em `config/tools.json`).

OSS de perícia termina no Claim Lock. Gemini só recebe o prompt de 56 blocos.
