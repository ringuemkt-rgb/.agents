# Scholarship Intelligence — módulo operacional do Academic Mission Orchestrator

**Status: MVP funcional de triagem e preparo; NÃO é robô de inscrição autônoma em produção.**
Data de revisão das fontes: 2026-10-30. Código aberto, perfil do candidato privado.

## Objetivo

Aumentar a chance legítima de ingresso e bolsa de mestrado por meio de:
1. monitoramento de fontes institucionais oficiais, com evidência e data;
2. triagem por prazo, áreas de pesquisa, região e ator apto a se inscrever;
3. máquina de estados que distingue inscrição, aprovação e implementação da bolsa;
4. preparação local dos formulários em navegador sob supervisão;
5. revisão opcional com Grok via API somente de METADADOS PÚBLICOS;
6. ampliação futura para ETL de editais em PDF, extração de baremas e RAG;
7. isolamento de dados pessoais e provas do candidato.

O módulo estende o `academic-mission-orchestrator` já registrado no hub. Não substitui
as regras do `SYSTEM_PROMPT.md`, `AGENTS.md` e `PRIVACY_SECURITY.md` superiores.

## Rodar agora (Python 3.11+, sem dependências para o núcleo)

```bash
cd agents/academic-mission-orchestrator/scholarship-intelligence
python scholarship_agent.py validate
python scholarship_agent.py discover --max-pages 3  # somente links candidatos; não comprova edital aberto
python -m unittest discover -s tests -v

# Fora do repositório: copiar profile.example.json para um diretório privado e ajustar
python scholarship_agent.py rank --profile /CAMINHO-PRIVADO/perfil.json --today 2026-10-30

# Uma página oficial por vez: só retorna metadados de fetch e hash (não determina elegibilidade)
python scholarship_agent.py scan --id ppgef-uesb-uesc-2027
```

## Navegador local — rascunho sem envio

```bash
pip install playwright
python -m playwright install chromium
python browser_assist.py --url https://portal-oficial.exemplo.br/inscricao \
  --allowed-host portal-oficial.exemplo.br --draft /CAMINHO-PRIVADO/campos.json
```

O arquivo local `campos.json` usa rótulos exatos dos campos: `{"Nome completo":"..."}`.
Apenas campos localizados de forma inequívoca serão preenchidos. Login, autenticação
gov.br, 2FA, CAPTCHA, assinatura, declaração, finalização, pagamento e protocolo final
são etapas humanas. **O código NÃO clica em Enviar.** Prefira APIs autorizadas,
respeite as condições dos portais, limites de acesso e LGPD.

## Grok (modelo proprietário; integração opcional)

```bash
export XAI_API_KEY="defina-no-seu-gerenciador-de-segredos"
python scholarship_agent.py grok-public --id ppgef-uesb-uesc-2027
```

O comando acima transmite à xAI apenas `title, official_url, deadline, application_actor,
topics, notes, evidence_date` de uma chamada PÚBLICA, nunca o perfil local. Uso de API
pode gerar custos. A resposta da IA não substitui edital vigente nem validação humana.
Uma futura integração com Qwen local pode evitar enviar dados de documentos a provedores.

## Estrutura

- `sources.json`: registros de oportunidades oficiais e URLs a monitorar;
- `scholarship_agent.py`: validador, ranking auditável, leitura pública, Grok e estados;
- `browser_assist.py`: navegador Playwright local, formulário como rascunho;
- `TOOLS_AND_MODELS.md`: catálogo técnico com opções de instalação;
- `profile.example.json`: APENAS dados fictícios e estrutura exemplar;
- `tests/`: testes sem rede e sem dados de candidato.

## Regras críticas

- Uma seleção de MESTRADO NÃO é automaticamente uma seleção de BOLSA.
- `program` em `application_actor`: candidatura é do PPG, não do estudante.
- Uma oportunidade é verificada somente quando a fonte oficial informa os termos.
- Pontuação calculada é de TRIAGEM OPERACIONAL, não probabilidade de aprovação.
- Data vencida implica prazo encerrado até nova retificação documental verificável.
- `FUNDING_SELECTED` não é `FUNDING_IMPLEMENTED`, muito menos `PAID`.
- `SUBMITTED_CONFIRMED` exige comprovante oficial e aprovação humana.
- Não há coleta automática de conta gov.br, CPF, laudos, credenciais ou autenticação.
- O Github público não é cofre: mesmo histórico Git de arquivos posteriormente apagados
  pode conservar material confidencial. Não publique documentos pessoais.
- `scan` respeita robots, allowlist e limite de bytes; resultado não é análise do edital.
- Analisar automaticamente TODOS os editais no Brasil exige conectores homologados por
  universidade/agência, regras locais e testes extensivos; este MVP ainda não cobre isso.

## Próximos incrementos técnicos necessários

1. Ampliar a descoberta inicial de links oficiais já incluída no CLI com crawling incremental, cache, deduplicação, comparação histórica e conectores por agência.
2. Ingestão PDF com Docling, captura de seções de requisitos/prazos/bolsas e citações por página.
3. Baremas determinísticos com comprovantes privados e bloqueio de itens não pontuáveis.
4. Integração autenticada opt-in com Google Drive/Gmail e cofre privado com controle de acesso.
5. Perfis de portais, testes E2E com páginas-simulacro e revisão visual antes de enviar.
6. Fila persistente de candidaturas e alertas de prazo com logs, prazos e evidência.
7. Política de privacidade, retenção, exclusão e avaliação de ameaças antes de hospedagem.

**Não declarar uma inscrição realizada sem comprovante oficial.**
