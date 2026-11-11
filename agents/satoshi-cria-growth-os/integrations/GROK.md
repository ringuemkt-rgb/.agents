# Grok / xAI — ponte de function calling

A API xAI permite que o Grok peça chamadas de funções que **um runtime controlado pelo usuário** executa e retorna ao modelo. Este repositório fornece um validador determinístico e um schema adaptável em integrations/grok_tools.json.

1. Configure Grok com SYSTEM_PROMPT.md e AGENT.md.
2. Registre validate_marketing_brief, conforme o endpoint xAI escolhido.
3. Ao receber chamada, execute src/growth_cli.py validate com JSON do briefing e devolva resposta ao Grok.
4. Não habilite automação de postagens, gastos nem mensagens sem autorização específica.
5. Mantenha XAI_API_KEY fora do Git; APIs podem custar créditos.

Documentação oficial: https://docs.x.ai/developers/tools/function-calling

**Estado:** ferramenta e contrato locais testáveis; API xAI não testada com credencial real.
