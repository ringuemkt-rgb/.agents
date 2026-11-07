# Ativação com ChatGPT
1. Abra o diretório `agents/boxe-de-cria-media-revenue/` do GitHub.
2. Disponibilize `SYSTEM_PROMPT.md`, `AGENT.md` e as skills necessárias na conversa/ambiente de trabalho.
3. Prompt curto: "Use o BDC MEDIA & REVENUE AGENT, com revisão factual e comercial. Verifique o site Lovable antes de alterar, registre testes reais, não invente conteúdo nem métricas e não publique automaticamente."
4. Para API OpenAI, defina `OPENAI_API_KEY` e `OPENAI_MODEL` em ambiente seguro e use `python runtime/bdc_media.py brief <id> --provider openai`. O ChatGPT não fornece automaticamente uma chave de API nem execução contínua ao runtime.
A instrução permanece portátil para outras IAs; adapters não podem enfraquecer as salvaguardas.