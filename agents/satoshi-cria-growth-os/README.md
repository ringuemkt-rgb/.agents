# SATOSHI CRIA GROWTH OS — agente público interoperável

Módulo do [Cria Agent Hub](https://github.com/ringuemkt-rgb/.agents) para marketing de academias de luta, captação responsável de alunos e construção de autoridade em Guarapari–ES.

**Este diretório público contém apenas código, instruções e dados aprovados para divulgação.** O CRM, os repasses financeiros internos, fotografias privadas e arquivos-mestres de logos permanecem fora do GitHub.

## Execução local (Python 3.10+, sem dependências)
~~~bash
python agents/satoshi-cria-growth-os/src/growth_cli.py facts
python agents/satoshi-cria-growth-os/src/growth_cli.py validate --input agents/satoshi-cria-growth-os/examples/brief.json
python -m unittest discover -s agents/satoshi-cria-growth-os/tests -v
python agents/satoshi-cria-growth-os/integrations/manus_v2.py
~~~

Leia AGENT.md, SYSTEM_PROMPT.md e public_facts.json antes de produzir qualquer campanha.

## Grok e Manus
- **Grok:** integração por function calling, com schema em integrations/grok_tools.json, validador em src/growth_cli.py e orientação em integrations/GROK.md.
- **Manus:** adaptador de API v2 em integrations/manus_v2.py. Funciona em **prévia por padrão**, e só envia com --send e MANUS_API_KEY configurada externamente. Consulte integrations/MANUS.md.
- **Qualquer IA:** pode ler o repositório público e usar as regras portáteis; acesso à leitura não dá permissão de publicação.

## Limitações
Não há conexão automática ativa com Grok, Manus, Instagram, WhatsApp ou campanhas pagas. As APIs dos provedores exigem conta, chave, permissões e eventualmente créditos; testes locais não equivalem a teste remoto.

## Política de dados
Não subir cadastros de alunos, contatos, contratos, planilhas financeiras, credenciais ou imagens de menores. Consulte PRIVACY.md.


## CRIA BOXE ACADEMY — Planejamento de aulas

Módulo de geração de planos e esquemas vetoriais originais: [`lesson_planning/`](lesson_planning/). **Sem redistribuir livros ou PDFs do Google Drive.**
