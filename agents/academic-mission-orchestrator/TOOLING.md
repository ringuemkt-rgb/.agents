# Tooling

These integrations are optional. The operating system must remain usable without them.

## Orchestration

### LangGraph

Use for durable state, checkpoints, explicit transitions, and human approval nodes.

Repository: `https://github.com/langchain-ai/langgraph`

### smolagents

Use for small, bounded specialist agents instead of uncontrolled swarms.

Repository: `https://github.com/huggingface/smolagents`

## Scientific evidence

### PaperQA2

Evidence-grounded scientific RAG and literature question answering.

Repository: `https://github.com/Future-House/paper-qa`

### ASReview

Active-learning screening for systematic/scoping review workflows.

Repository: `https://github.com/asreview/asreview`

### Consensus / Scite

Use when connected for scientific search and citation-context checking. Do not rely on any single engine as sole authority.

## Document intelligence

### Docling

PDF/DOCX/table/layout extraction.

Repository: `https://github.com/docling-project/docling`

## Privacy

### Microsoft Presidio

PII detection/anonymization before public release.

Repository: `https://github.com/microsoft/presidio`

## Browser automation

### Browser Use

Useful for robust browser workflows, but place a human approval gate before final submissions or sensitive communications.

Repository: `https://github.com/browser-use/browser-use`

## Retrieval

### BGE-M3

Multilingual retrieval model suitable for Portuguese/English/Chinese document collections.

Model: `BAAI/bge-m3`

### bge-reranker-v2-m3

Multilingual reranker for narrowing retrieved evidence.

Model: `BAAI/bge-reranker-v2-m3`

## GitHub

Use GitHub as the versioned source of agent prompts, checklists, schemas, and changelog. Do not put candidate private context in public Git.
