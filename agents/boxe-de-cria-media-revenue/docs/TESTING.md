# Testes
Execute a partir deste diretório:
```bash
python -m unittest discover -s tests -v
python runtime/bdc_media.py finance --views 100000 --eligible 0.75 --rpm 5 --cost 350
python runtime/bdc_media.py list
```
Testes unitários cobrem URLs, RSS/Atom, XML inseguro, fórmula econômica, revisão editorial, registros por modalidade/classe e leitura do retorno das APIs. Não cobrem tráfego de rede real, tokens OpenAI/xAI, OAuth AdSense, produção Lovable ou deploy.

O CI do GitHub executa o mesmo conjunto de testes. Nunca trocar uma falha real por uma alegação de sucesso.
