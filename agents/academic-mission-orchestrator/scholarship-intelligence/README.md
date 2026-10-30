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

## Barema e conferência de documentos (sem inventar pontos)

Preencha o arquivo de critérios a partir do **edital real e de suas retificações**;
o `criteria.example.json` é didático, NÃO é o barema oficial da UEL.
O arquivo de evidências e os caminhos para comprovantes ficam apenas no seu
computador privado. Cada critério precisa do link da fonte primária e a evidência
precisa estar marcada `human_verified` com referência local.

```bash
python application_auditor.py \\
  --rules /CAMINHO-PRIVADO/criterios-oficiais.json \\
  --evidence /CAMINHO-PRIVADO/provas.json
```

Sem prova, a nota simulada é zero. Essa simulação não substitui homologação
pela banca e não deve ser usada sem revisar caps, unidades e pontuações reais.

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


## v0.3 — MCP, Grok Responses, autonomia persistente e supervisão

### MCP local (SDK Python v2)

```bash
# Ambiente virtual Python 3.11+:
python -m pip install "mcp[cli]>=2,<3"
cd agents/academic-mission-orchestrator/scholarship-intelligence
mcp dev mcp_server.py
```

A interface MCP expõe apenas leitura do registro público, triagem por preferências
de interesse, consulta de política e verificação de fontes. O comando opcional
`grok_review_public_opportunity` exige **duas opções privadas**:
`SCHOLARSHIP_ALLOW_PAID_ANALYSIS=1` e `XAI_API_KEY`.
Nenhum desses valores deve ir para o Git. O cliente MCP deve ser LOCAL,
não publicar um endpoint sem autenticação na internet.

### Grok via xAI Responses API

A integração agora usa `POST https://api.x.ai/v1/responses` (não o endpoint
legado de chat). O modelo padrão poderá ser atualizado pela variável
`XAI_MODEL`. Somente metadados estritamente permitidos da oportunidade pública
são transmitidos. Sem `XAI_API_KEY`, falha sem qualquer chamada.
Este adaptador não fornece ferramentas a Grok nem permite que texto remoto
conceda permissões; ele não acessa documentos do candidato. Limites de tokens
e orçamento de API devem ser monitorados na plataforma xAI.

### Fila persistente, falhas e retomada

```bash
# Execute fora do repositório; o caminho é privado.
python mission_runtime.py --db "$HOME/scholarship-private/jobs.sqlite3" \
  enqueue --source-id watch-000 --action PUBLIC_DISCOVER
python mission_runtime.py --db "$HOME/scholarship-private/jobs.sqlite3" run-once
python mission_runtime.py --db "$HOME/scholarship-private/jobs.sqlite3" status

# Rotina local: reusa SQLite, respeita orçamento de até 6 fontes por execução
python monitor.py --db "$HOME/scholarship-private/jobs.sqlite3"
```

Tarefas registradas usam IDs públicos sem dados pessoais e uma lease para
retomar tentativas interrompidas. Falhas transitórias têm **até quatro
tentativas** com backoff. CAPTCHA, pedido de autenticação, robots.txt, mudança
de portal e falha desconhecida passam a `WAITING_HUMAN`. Não há repetição sem
limite, evasão de controle anti-bot ou execução opaca.

### Política de capacidades

- `ALLOW_AUTONOMOUS`: apenas leitura pública, análise pública e elaboração local.
- `REQUIRE_ONE_TIME_APPROVAL`: preencher em portal, upload, submissão, envio
  externo, pagamentos, assinatura ou exportação de dados privados.
- `HUMAN_ONLY`: senha, segundo fator, biometria e CAPTCHA. Agente jamais
  pode tentar obter, contornar ou coletar esses fatores.
- `DENY_HOST` ou `DENY_UNRECOGNIZED`: bloqueado.

`permission_guard.py` emite permissões **únicas, com escopo e prazo**, só via
terminal interativo local; o mecanismo não está conectado a um executor de
submissão, que ainda não foi implementado. Não interpretar uma permissão como
confirmação de matrícula ou como autorização da universidade.

### Monitoramento GitHub Actions

A workflow `.github/workflows/scholarship-public-monitor.yml` inclui
`workflow_dispatch` e agendamento diário 08:17 na Bahia, com leitura pública,
artefato de status sem PII e permissões `contents: read`.
**O agendamento só terá efeito após merge na branch padrão** do repositório.
GitHub Actions usa máquina efêmera: o artefato guarda o status da execução,
mas não mantém uma fila SQLite entre runs. Para memória contínua usar servidor
privado ou cron local com disco persistente.

### Tratamento de alterações e bloqueios

Quando um edital é retificado, nenhuma inscrição deve ser considerada concluída
automaticamente. Valide novamente versão, prazo, formulário e anexos.
Quando um portal falha: classifique a falha, tente novamente apenas para erros
transitórios e preserve um checkpoint. Caso haja bloqueio institucional,
reconcilie manualmente com o suporte oficial. Não usar evasão de limites
de acesso, identidades falsas, proxies para driblar bloqueios ou engenharia
social para conseguir credenciais.

### Limites reais da entrega

Os módulos executáveis e testes são verificados em GitHub CI; a integração
MCP com cliente real, os portais universitários, o navegador guiado por agente
e a chamada faturável a Grok **não foram submetidos a testes E2E aqui**.
Nenhuma inscrição ou matrícula foi enviada; sem implantação contínua,
não existe um agente permanentemente online.

Documentos do candidato ficam em cofre privado com consentimento granular e
acesso mínimo; não conceda acesso indiscriminado a aplicações remotas.

## Cofre de documentos local (v0.3)

Usa criptografia autenticada AES-256-GCM com derivação de chave scrypt
(`cryptography>=46,<47`). A frase secreta é solicitada por `getpass`,
não é passada como parâmetro da linha de comando nem enviada a Grok ou ao MCP.

```bash
python -m pip install "cryptography>=46,<47"
python private_vault.py seal \
  --input "$HOME/documentos-privados/diploma.pdf" \
  --output "$HOME/scholarship-private/cofre/diploma.enc"

# Decriptação somente sob decisão do titular e em pasta privada:
python private_vault.py unseal \
  --input "$HOME/scholarship-private/cofre/diploma.enc" \
  --output "$HOME/scholarship-private/temp/diploma.pdf"
```

O arquivo de saída é criado com permissão `0600`, sem sobrescrever
arquivos existentes. A decriptação cria um ARQUIVO EM TEXTO CLARO; não a use
numa pasta sincronizada/publicada. Recomenda-se também criptografia do disco,
backup controlado e remoção segura dos temporários. Não existe recuperação
automática da frase secreta; perdê-la pode tornar os arquivos irrecuperáveis.
**O cofre não está conectado ao Google Drive nem aos formulários nesta versão.**
