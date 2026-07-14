# AGENTS.md — Contrato Global

Estas regras se aplicam a todos os agentes, workflows e integrações deste repositório.

## Fonte única

- Agentes vivem em `ringuemkt-rgb/.agents`.
- Código de produto vive no repositório oficial de cada produto.
- Não criar repositórios paralelos para protótipos, prompts, builds ou versões alternativas.
- Experimentos usam branches, feature flags ou diretórios temporários claramente marcados.

## Ordem de trabalho

1. Ler o objetivo e o contexto do repositório-alvo.
2. Auditar o que já existe antes de criar novos arquivos.
3. Declarar suposições materiais.
4. Produzir um plano com critérios de aceitação.
5. Alterar o mínimo necessário para entregar valor verificável.
6. Executar validações disponíveis.
7. Relatar arquivos, testes, falhas, riscos e próximo passo.

## Proibições

- Não inventar resultado de teste, build, deploy ou instalação.
- Não apagar conteúdo antes de confirmar migração e recuperação.
- Não versionar tokens, chaves, senhas, keystores ou dados pessoais reais.
- Não introduzir dependência ou serviço sem justificar manutenção, licença e risco.
- Não alterar canon, regra financeira ou contrato de segurança silenciosamente.
- Não usar código ou arte sem verificar licença e atribuição.
- Não colocar LLM no caminho crítico quando uma regra determinística resolve melhor.

## Evidência mínima

Toda execução deve produzir, quando aplicável:

- objetivo e escopo;
- arquivos criados e modificados;
- comandos ou testes executados;
- resultado real das validações;
- limitações e pendências;
- decisão de concluir, bloquear ou reverter.

## Deleção de repositórios

Um repositório só pode ser removido depois de:

1. inventário de conteúdo exclusivo;
2. migração do conteúdo aprovado;
3. verificação no repositório canônico;
4. backup ou referência de recuperação;
5. lista explícita de repositórios autorizados para exclusão.

## Filosofia

Autonomia não é agir no escuro. É avançar com disciplina, rastreabilidade e responsabilidade.
