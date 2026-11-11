# CRIA BOXE ACADEMY — planejamento pedagógico de Boxe (v1.0)

Módulo determinístico do [SATOSHI CRIA GROWTH OS](../). Usa fatos confirmados de `../public_facts.json` e converte um briefing com **duração informada** em plano minucioso de seis blocos, critérios de avaliação e material HTML ilustrado com SVGs **originais**, editáveis e prontos para impressão.

## Execução

```bash
python agents/satoshi-cria-growth-os/lesson_planning/src/lesson_planner.py \
  --input agents/satoshi-cria-growth-os/lesson_planning/examples/fitbox_06h.json \
  --output /tmp/aula
python -m unittest discover -s agents/satoshi-cria-growth-os/lesson_planning/tests -v
```

Saídas: `plan.json` e `plan.html`. Sem dependências, conexão à internet ou uso de LLM para o plano inicial. Cada sessão é um **rascunho supervisionado pelo treinador**.

## Campos de entrada
`class_id` (turma confirmada), `start_time`, `duration_min` (obrigatória; nunca presumir), `week` (1-12), `session` (1-2), `goal` (opcional), `population`, `equipment`, `contact` (aceita somente false).

**FIT BOX:** terça/quinta às 6h; exemplo de 40 minutos termina 6h40, mas o término é proposta de aula, não horário comercial confirmado. **CTRK:** terça/quinta às 12h; informar duração, não inventar.

## Estrutura pedagógica
1. Acolhimento, segurança e objetivo observável.
2. Aquecimento geral e específico.
3. Demonstração e ambiente previsível.
4. Prática orientada sem contato humano.
5. Variação de tarefa e tomada de decisão.
6. Desaceleração, avaliação e próximo passo.

Propor regressão e progressão com critério observável. Meta inicial `4/5` é rubrica didática **não validada cientificamente**. Adaptar volume e intensidade ao perfil e sinais da turma; não oferecer contato na cabeça, sparring, BFRT ou reabilitação automatizados.

## Governança e fontes
Esta pasta **não contém textos integrais, figuras ou marcas dos materiais do Google Drive**. Consulte o documento privado de Plano Mestre para o inventário e auditoria. Fontes-base: Mateus Alves (2020, Módulos I e II); Maykel Balmaseda (2009); CBBoxe, Manual para Treinadores (versão do acervo); USA Boxing Grassroots Training Manual; CONADE México, Academia Box; Boxing Science; BDC Science Map. Conferir regras atuais em órgãos oficiais.

Segurança: [CDC HEADS UP — resposta à suspeita de concussão, 2025](https://www.cdc.gov/heads-up/response/index.html). Retirada imediata da atividade e sem retorno no mesmo dia até avaliação e liberação.

## Ilustrações
SVGs esquemáticos originais (não extraídos dos livros) ilustram jab e footwork. Para fotos/logo dos parceiros, somente arquivos-mestres oficiais e permissões pertinentes. Não reconstruir rostos nem redesenhar marcas.

## Integração Grok e Manus
Ambos podem consumir o JSON gerado e a orientação em [SYSTEM_PROMPT.md](SYSTEM_PROMPT.md). Não há controle remoto da academia, das contas, do Google Drive nem publicação automática de aulas. Referências privadas não devem ser copiadas para prompts públicos.
