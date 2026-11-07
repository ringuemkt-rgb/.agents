# Ativação com Grok
1. Abra este diretório no GitHub.
2. Forneça ao Grok `SYSTEM_PROMPT.md`, `AGENT.md` e skills da tarefa. Apenas colar uma URL não garante que o Grok tenha lido os arquivos.
3. Prompt curto: "Atue como BDC MEDIA & REVENUE AGENT, respeitando a política do repositório. Auditoria antes de ações, fatos rastreáveis, estatísticas por modalidade e AdSense legítimo. Apresente evidências do que realmente executou."
4. Com runtime próprio: defina `XAI_API_KEY` e `XAI_MODEL` em variáveis de ambiente, então execute `python runtime/bdc_media.py brief <id> --provider xai`.
Documentação xAI: https://docs.x.ai/developers/rest-api-reference/inference/responses . O modo API é independente do chat e gera briefing não publicado.