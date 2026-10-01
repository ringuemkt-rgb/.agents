# RAG Pipeline

Pipeline recomendado para transformar documentos da marca, PDFs técnicos, artigos, padrões da raça, insights e histórico de posts em uma base de conhecimento pesquisável.

---

## 1. Objetivo

Reduzir alucinação e aumentar rigor técnico.

O sistema deve responder com base em:

- padrão oficial da raça;
- artigos científicos;
- documentos veterinários;
- conteúdos aprovados da marca;
- métricas reais de performance;
- checklists internos;
- exemplos vencedores.

---

## 2. Estrutura de pastas sugerida

```text
knowledge/
├── breed-standard/
├── scientific-papers/
├── veterinary/
├── brand/
├── instagram-insights/
├── winning-posts/
└── rejected-patterns/
```

---

## 3. Ingestão

### MarkItDown

Use para conversão rápida e simples.

### Docling

Use para PDFs técnicos, tabelas e conteúdo estruturado.

### MinerU

Use para documentos complexos, longos ou com layout difícil.

Saída preferencial:

```text
Markdown + metadados + fonte + data + tipo de documento
```

---

## 4. Chunking

Cada documento deve ser dividido em blocos úteis:

- título;
- seção;
- trecho;
- página/linha quando possível;
- tipo de fonte;
- nível de evidência;
- data.

Evitar chunks grandes demais.

---

## 5. Embeddings e ranking

Recomendação:

- embeddings: BGE-M3;
- reranker: bge-reranker;
- busca: LlamaIndex ou RAGFlow.

Fluxo:

```text
query → retrieval → reranking → evidence pack → resposta/carrossel
```

---

## 6. Evidence pack

Antes de gerar conteúdo, criar um pacote de evidência:

```text
Tema:
Pergunta central:
Fontes recuperadas:
Trechos úteis:
Nível de evidência:
Riscos de exagero:
O que pode afirmar:
O que não pode afirmar:
```

---

## 7. Avaliação com Ragas

Avaliar:

- fidelidade;
- relevância da resposta;
- precisão do contexto;
- completude;
- risco de resposta sem fonte.

---

## 8. Separação obrigatória

Todo conteúdo deve diferenciar:

- fato documentado;
- inferência técnica;
- opinião editorial da marca;
- recomendação prática;
- hipótese.

---

## 9. Exemplo de uso

Tema: socialização do filhote Cane Corso.

Evidence pack:

- padrão da raça: guardião, ágil, obediente;
- comportamento: socialização controlada;
- risco: não prometer cão perfeito;
- afirmação permitida: socialização ajuda a formar estabilidade;
- afirmação proibida: socialização garante ausência de agressividade.

---

## 10. Regra final

Se a base não sustenta, não publique como fato.

Use linguagem prudente:

- “pode ajudar”;
- “tende a favorecer”;
- “é recomendado observar”;
- “não substitui avaliação profissional”.
