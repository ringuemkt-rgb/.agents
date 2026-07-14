# Cria Agent Hub

Repositório central de agentes, skills, workflows e integrações para os projetos do Mestre Satoshi.

Este é o **único repositório oficial de agentes**. Ele organiza o trabalho de planejamento, desenvolvimento, arte, sprites, lore, QA e release sem duplicar o código dos produtos.

## O que ele faz

- valida manifestos de agentes e ferramentas;
- monta planos de execução com dependências em ordem correta;
- instala ferramentas externas em `.vendor/` a partir de um catálogo controlado;
- mantém agentes especializados em arquivos claros e versionados;
- impede que um agente altere canon, segurança ou arquitetura sem passar pelos guardiões adequados;
- fornece CI para validar o hub antes de qualquer alteração.

## Início rápido

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install -e .

cria-agents validate
cria-agents list
cria-agents plan build-game
cria-agents tools sync
```

## Estrutura

```text
.agents/
├── agents/                      # contratos individuais dos agentes
├── config/
│   ├── agents.json              # registro dos agentes
│   ├── workflows.json           # DAGs de execução
│   └── tools.json               # integrações externas
├── src/cria_agents/             # CLI e orquestrador determinístico
├── tests/                       # testes do núcleo
├── scripts/                     # bootstrap portátil
├── docs/                        # arquitetura e operação
└── .vendor/                     # ferramentas clonadas; não versionadas
```

## Agentes oficiais

| Agente | Responsabilidade |
|---|---|
| Repository Guardian | mantém fonte única, estrutura e higiene Git |
| Product Architect | transforma objetivo em especificação executável |
| Game Studio Director | coordena gameplay, Godot, dados e produção |
| BJJ Combat Engineer | protege biomecânica e máquina de estados do grappling |
| Lore Guardian | protege canon, continuidade e identidade regional |
| Art & Sprite Director | coordena conceitos, sprites, mapas e handoff para engine |
| QA & Release Guardian | valida testes, builds, APK e critérios de conclusão |
| Security & Privacy Guardian | revisa segredos, dados pessoais e riscos operacionais |

## Princípio central

Agentes não substituem engenharia. Eles transformam intenção em tarefas verificáveis, executam dentro de limites claros e entregam evidência do que foi modificado e testado.

Consulte `docs/ARCHITECTURE.md` e `AGENTS.md` antes de acrescentar novas funções.
