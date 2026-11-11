# Manus — integração opcional API v2

Este módulo inclui integrations/manus_v2.py. Sem argumentos, **não envia requisição**: apenas mostra payload de prévia. Para enviar, é preciso configurar MANUS_API_KEY e executar explicitamente com --send, sujeito a custos e autorização.

~~~bash
python agents/satoshi-cria-growth-os/integrations/manus_v2.py
# Somente após autorização:
MANUS_API_KEY=... python agents/satoshi-cria-growth-os/integrations/manus_v2.py --send
~~~

O payload pede a leitura do módulo público e a preparação de campanha sem publicar, cobrar ou acessar dados privados.

Referência oficial v2: https://open.manus.ai/docs/v2/introduction

**Estado:** payload e prévia local; execução remota não testada.
