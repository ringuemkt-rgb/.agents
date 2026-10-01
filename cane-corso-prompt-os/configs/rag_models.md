# RAG Models and Retrieval Config

Configuração recomendada para busca semântica e recuperação de evidência em português.

---

## 1. Embeddings

### BGE-M3

Uso recomendado:

- base multilíngue;
- português;
- documentos longos;
- dense retrieval;
- sparse retrieval;
- multi-vector retrieval.

Configuração conceitual:

```yaml
embedding_model: BAAI/bge-m3
chunk_size: 600-1200 tokens
chunk_overlap: 100-200 tokens
language: pt-BR
```

---

## 2. Reranker

### bge-reranker-v2-m3

Uso:

- reordenar top-k documentos recuperados;
- reduzir ruído;
- priorizar fontes técnicas.

Configuração conceitual:

```yaml
reranker_model: BAAI/bge-reranker-v2-m3
retrieval_top_k: 20
rerank_top_k: 5
```

---

## 3. RAG Framework

Escolher conforme necessidade:

### LlamaIndex

Use se quiser controle customizado.

### RAGFlow

Use se quiser painel mais pronto e operação visual.

---

## 4. Metadados obrigatórios

Cada chunk deve manter:

```json
{
  "source_title": "string",
  "source_type": "breed_standard|paper|veterinary|brand|insight|other",
  "evidence_level": "strong|moderate|weak|editorial",
  "date": "string",
  "page": "string|null",
  "section": "string|null",
  "language": "pt-BR|en|other",
  "claim_scope": "what this chunk supports"
}
```

---

## 5. Tipos de documento e prioridade

1. Padrão oficial da raça.
2. Artigos científicos.
3. Documentos veterinários.
4. Guias de comportamento.
5. Dados próprios de performance.
6. Conteúdo aprovado da marca.
7. Conteúdo de mercado.

---

## 6. Regras de resposta

Ao usar RAG:

- não citar fonte que não sustenta a afirmação;
- não extrapolar estudo pequeno para promessa geral;
- separar evidência de opinião;
- usar linguagem prudente;
- registrar lacunas.

---

## 7. Avaliação com Ragas

Métricas sugeridas:

- faithfulness;
- answer relevancy;
- context precision;
- context recall;
- factual consistency.

---

## 8. Exemplo de query

```text
Quais pontos do padrão oficial sustentam que o Cane Corso deve ser apresentado como guardião equilibrado, não como cão agressivo?
```

Resposta esperada:

- recuperar trechos sobre utilização, temperamento, guarda, obediência e faltas comportamentais;
- gerar conteúdo editorial sem exagero;
- marcar inferências como inferências.
