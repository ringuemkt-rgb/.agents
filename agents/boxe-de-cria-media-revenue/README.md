# BOXE DE CRIA — Media & Revenue Agent v1
Agente portátil para **ChatGPT e Grok**, focado em portal de notícias, atletas brasileiros (boxe, Muay Thai, kickboxing), SEO, AdSense e patrocínios.

**Situação:** branch de desenvolvimento no hub oficial. Código-base testado localmente; integração com site, contas AdSense e publicação ainda não ativadas. Nenhuma notícia é publicada automaticamente.

## Ativação
- ChatGPT: [ACTIVATE_CHATGPT.md](ACTIVATE_CHATGPT.md).
- Grok: [ACTIVATE_GROK.md](ACTIVATE_GROK.md).
- Modelo comum: [SYSTEM_PROMPT.md](SYSTEM_PROMPT.md).
- Operação e limites: [AGENT.md](AGENT.md) e [docs/OPERATIONS.md](docs/OPERATIONS.md).
- Competências modulares: [skills](skills/).

## Runtime (Python 3.11+, stdlib)
```bash
python runtime/bdc_media.py --db var/bdc.sqlite3 list
python runtime/bdc_media.py --db var/bdc.sqlite3 finance --views 100000 --eligible 0.75 --rpm 5 --cost 350
python -m unittest discover -s tests -v
```
Fontes de feeds começam vazias por segurança. Com fontes revisadas, use `collect --sources config/sources.json` e `brief <id> --provider offline|openai|xai`. As APIs OpenAI/xAI exigem chaves e modelo definidos via ambiente. O agente só produz briefing de apuração, não matéria factual automática.

## Integrações e honestidade
Site canônico: https://lovable.dev/projects/a63e471f-f034-481c-a75c-8dd9978de7e7 .
O site precisa de Git Sync próprio; a mera presença do agente no hub não o modifica. AdSense OAuth, Search Console, GA4 e infraestrutura de agendamento não estão conectados. Não usar notícias para criar tráfego artificial nem resultados fictícios.

## Licenças
Código original MIT; marcas e logotipos BOXE DE CRIA não são licenciados a terceiros.