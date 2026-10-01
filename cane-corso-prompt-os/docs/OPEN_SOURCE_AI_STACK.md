# Open Source AI Stack — Cane Corso Prompt OS

Este documento define a pilha open-source recomendada para transformar o sistema de prompts em uma fábrica de conteúdo com pesquisa, avaliação, observabilidade, RAG, visual premium e melhoria contínua.

> Regra: não afirmar que uma ferramenta está instalada sem confirmação. Trate cada item como módulo adotável.

---

## 1. Camada de prompt optimization

### DSPy

Função:

- transformar prompts em módulos programáveis;
- otimizar instruções e exemplos;
- medir qualidade por métricas;
- criar pipeline de geração com avaliação.

Aplicação:

- `HookGenerator`;
- `CarouselStrategist`;
- `SlidePromptBuilder`;
- `CaptionOptimizer`;
- `IPVScorer`;
- `EvidenceChecker`;
- `VisualConsistencyJudge`.

Prioridade: máxima.

---

## 2. Camada de QA e red team

### promptfoo

Função:

- testar prompts;
- comparar modelos;
- criar assertions;
- evitar regressão;
- validar segurança editorial.

Aplicação:

- impedir glamourização de agressividade;
- exigir CTA e legenda;
- garantir prompts autônomos;
- verificar negative prompt;
- comparar capas A/B/C.

Prioridade: máxima.

---

## 3. Camada de observabilidade

### Langfuse

Função:

- versionar prompts;
- registrar entradas e saídas;
- armazenar avaliações;
- conectar resultado real do Instagram com o prompt usado;
- manter histórico de melhoria.

Campos recomendados:

- tema;
- gancho;
- versão do prompt;
- IPV estimado;
- legenda;
- CTA;
- alcance;
- salvamentos;
- compartilhamentos;
- comentários;
- directs;
- diagnóstico.

Prioridade: máxima.

---

## 4. Camada de documentos

### MarkItDown

Uso:

- converter PDFs, DOCX, PPTX, XLSX, HTML e outros materiais em Markdown.

Quando usar:

- ingestão rápida;
- material simples;
- documentação leve.

### Docling

Uso:

- conversão estruturada para RAG;
- documentos técnicos;
- chunking;
- tabelas e layouts.

Quando usar:

- padrões oficiais;
- artigos científicos;
- material veterinário;
- PDFs com estrutura importante.

### MinerU

Uso:

- documentos complexos;
- PDF pesado;
- tabelas;
- fórmulas;
- material visual.

Quando usar:

- perícia profunda;
- PDFs longos;
- conteúdo técnico com layout difícil.

---

## 5. Camada RAG

### LlamaIndex

Uso:

- arquitetura RAG customizada;
- conectores;
- índices;
- busca em documentos internos.

### RAGFlow

Uso:

- RAG com interface pronta;
- respostas com citações;
- operação por usuário não técnico.

### BGE-M3

Uso:

- embeddings multilíngues;
- português;
- documentos longos;
- busca semântica.

### bge-reranker

Uso:

- reordenar documentos recuperados;
- melhorar precisão da fonte usada.

### Ragas

Uso:

- avaliar fidelidade factual;
- contexto recuperado;
- relevância da resposta;
- risco de alucinação.

---

## 6. Camada visual IA

### ComfyUI

Uso:

- criar workflows visuais;
- gerar slides em lote;
- preservar identidade visual;
- automatizar background, moldura e assets.

### FLUX.1

Uso:

- imagem open-weight;
- fundos premium;
- ilustrações;
- assets sem texto.

### ControlNet

Uso:

- controlar layout;
- pose;
- profundidade;
- bordas;
- composição.

### IP-Adapter

Uso:

- usar referência visual;
- manter mascote/cão/estilo consistente.

### SAM 2

Uso:

- recortar cão, mascote, produto ou pessoa;
- segmentar imagens;
- preparar assets para design.

---

## 7. Camada de modelos abertos

### Qwen3

Uso:

- raciocínio;
- português;
- texto;
- automação;
- análise estratégica.

### Qwen2.5-VL

Uso:

- leitura visual;
- análise de layout;
- documentos;
- gráficos;
- auditoria de artes.

### llama.cpp

Uso:

- rodar modelos quantizados localmente;
- notebook limitado;
- baixa infraestrutura.

### vLLM / SGLang

Uso:

- serving em GPU/cloud;
- alto volume;
- baixa latência.

### PEFT / TRL

Uso futuro:

- adaptação de modelos;
- fine-tuning de tom da marca;
- avaliador próprio.

---

## 8. Stack recomendado mínimo

Para começar sem complexidade:

```text
promptfoo + insights_log.csv + SYSTEM_PROMPT.md
```

Próximo nível:

```text
MarkItDown/Docling + LlamaIndex + BGE-M3 + Ragas
```

Nível profissional visual:

```text
ComfyUI + FLUX + ControlNet + IP-Adapter + SAM 2
```

Nível autoaperfeiçoamento:

```text
DSPy + promptfoo + Langfuse + dados reais de performance
```
