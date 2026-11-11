# Cria Agent Hub

Repositório central de agentes, skills, workflows e integrações para os projetos do Mestre Satoshi.

Este é o **único repositório oficial de agentes**. Ele organiza o trabalho de planejamento, desenvolvimento, arte, sprites, lore, QA, conteúdo editorial e release sem duplicar o código dos produtos.

## O que ele faz

- valida manifestos de agentes e ferramentas;
- monta planos de execução com dependências em ordem correta;
- instala ferramentas externas em `.vendor/` a partir de um catálogo controlado;
- mantém agentes especializados em arquivos claros e versionados;
- impede que um agente altere canon, segurança ou arquitetura sem passar pelos guardiões adequados;
- fornece CI para validar o hub antes de qualquer alteração;
- disponibiliza agentes portáteis que podem ser carregados em diferentes IAs por arquivos Markdown/JSON.

## Início rápido

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install -e .

cria-agents validate
cria-agents list
cria-agents plan build-game
cria-agents plan build-bdc-carousel
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
| BOXE DE CRIA Carousel Orchestrator | transforma temas em carrosséis evidence-first, didáticos, 2.5D e prompts autônomos portáteis entre IAs |
| Academic Mission Orchestrator | conduz missões acadêmicas longas com gates, evidência, ética, bolsa, finanças e relocação |

## BOXE DE CRIA Carousel Orchestrator

O pacote portátil vive em:

`agents/boxe-de-cria-carousel-orchestrator/`

Use `SYSTEM_PROMPT.md` como instrução principal em ChatGPT, Claude, Gemini ou qualquer LLM que aceite instruções personalizadas. O arquivo `PORTABILITY.md` descreve os modos de uso por plataforma.

## Princípio central

Agentes não substituem engenharia. Eles transformam intenção em tarefas verificáveis, executam dentro de limites claros e entregam evidência do que foi modificado e testado.

Consulte `docs/ARCHITECTURE.md` e `AGENTS.md` antes de acrescentar novas funções.


## Academic Mission Orchestrator

O pacote portátil vive em:

`agents/academic-mission-orchestrator/`

Use `SYSTEM_PROMPT.md` para ativação completa em outra plataforma, `ACTIVATE.md` para ativação compacta e `PRIVATE_CONTEXT_TEMPLATE.md` para fornecer dados do candidato **somente em ambiente privado**.

O pacote público não contém documentos pessoais, dados de saúde, credenciais, proposta viva de seleção ou outros dados sensíveis.

## BDC Media & Revenue Agent

O agente editorial e comercial portátil para ChatGPT, Grok e outras IAs está em [`agents/boxe-de-cria-media-revenue/`](agents/boxe-de-cria-media-revenue/). Inclui skills de jornalismo, dados de atletas, SEO, AdSense, vendas, integrações e runtime Python testável. Nenhuma publicação ou campanha publicitária é acionada automaticamente.

## BDC Visual Identity & Creative Studio

Módulo oficial de identidade e produção gráfica do portal BOXE DE CRIA: [`agents/boxe-de-cria-visual-studio/`](agents/boxe-de-cria-visual-studio/). Inclui 10 skills, tokens de marca, sete presets responsivos, governança de logomarcas/fotografia, template SVG editável, checklist Lovable e testes de contraste/proveniência. Prompt portátil para ChatGPT e Grok. **Não inclui fotos ou logomarcas oficiais e não faz deploy do site.**


## SATOSHI CRIA Growth OS

Agente portátil de marketing e captação de alunos de artes marciais em Guarapari: [agents/satoshi-cria-growth-os/](agents/satoshi-cria-growth-os/). Inclui validação determinística de horários e assinatura profissional, regras de privacidade e contratos opcionais de integração com Grok e Manus. **Sem credenciais, dados reais de alunos ou arquivos-mestres de marcas no repositório público.**
