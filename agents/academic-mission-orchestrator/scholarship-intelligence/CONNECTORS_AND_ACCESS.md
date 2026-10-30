# Conexões MCP, fontes pessoais e autonomia operacional

## Estado atual (30/10/2026)

Durante o desenvolvimento pelo ChatGPT, foram consultados:
- **GitHub conectado:** leitura de regras do hub, escrita de módulos e PR #8.
- **Hugging Face conectado:** metadados dos modelos Qwen3-8B, BGE-M3 e Qwen3-Embedding-0.6B.
- **Google Drive conectado:** descoberta por metadados de documentos de mestrado, Lattes e NeuroJitsu;
  nenhum arquivo pessoal foi enviado ao GitHub nem a Grok.

**Acesso do ChatGPT aos conectores NÃO equivale a delegar tokens ou sessão à aplicação
independente.** Cada implantação deve solicitar consentimento e OAuth próprios;
não tente copiar cookies, tokens MCP, credenciais ou dados internos das conexões
da conta ChatGPT.

## Matriz de integração recomendada

| Conector | Atuação | Escopo inicial | Escrita | Condição |
|---|---|---|---|---|
| GitHub | Versionamento de código, questões e PRs | Repositório específico | Branch/PR autorizado | Sem arquivos pessoais |
| Hugging Face | Ler metadados/modelos e baixar versões aprovadas | Público | Não | Licença, SHA, custo GPU |
| Google Drive | Descobrir diplomas, históricos e certificados | `drive.metadata.readonly`, depois `drive.readonly` | Não | OAuth por conta do candidato |
| Gmail | Ler notificações de PPGs e identificar protocolos | `gmail.readonly` | Não | Consentimento e filtro de remetentes |
| Google Calendar | Consultar prazos | `calendar.readonly` | Separado | Criar evento somente se autorizado |
| xAI Grok | Analisar texto e metadados públicos | API em `/v1/responses` | Sem ferramentas | Chave privada, limite de gastos |
| Portais universitários | Preparar rascunho em sessão local | Site exato e aprovação local | Rascunho | Playwright + validação de campos |
| gov.br | Dados de serviços oficiais do próprio titular | Autenticação presencial do titular | Não delegada | Não contornar 2FA/CAPTCHA |
| CAPES/CNPq/FAPs | Editais e regras públicos | Consulta de portais oficiais | Não | Respeitar robots e limites |

## Separação dos ambientes

1. **GitHub público:** código, testes, normas, conectores sem credenciais e exemplos fictícios.
2. **Servidor privado:** banco de candidaturas, documentos, histórico, política de retenção,
   criptografia em repouso e backups, acesso autenticado e registro por pessoa.
3. **Navegador assistido:** sessão real autenticada pelo titular, controle de domínio,
   rascunho sem submissão automática.
4. **LLM remoto:** por padrão apenas metadados públicos. Para qualquer dado pessoal
   seria necessária política de consentimento específica e revisão de LGPD.
5. **MCP local:** expõe ferramentas específicas, não acesso ao sistema operacional.

## Barreiras que não podem ser contornadas

- Login do titular, 2FA e biometria: execução humana, nunca solicitar segredo ao modelo.
- CAPTCHA e bloqueios anti-bot: não burlar; interromper e usar caminho permitido.
- Inscrição ou matrícula concluída: apenas com confirmação do sistema e comprovante.
- E-mail a orientador/avaliador: verificar integridade acadêmica e autorização antes.
- Dados PcD ou médicos: nunca transmitir por padrão; usar apenas quando exigidos no edital.
- Prazos vencidos: atualizar a fonte, procurar retificação; não inventar prorrogação.
- Falha por indisponibilidade do portal: capturar status, aplicar backoff legal e
  encaminhar ao atendimento administrativo se persistir.

## Plano de operação com permissões mínimas

**AUTO:** pesquisar fontes públicas, identificar links, comparar instituições,
resumir editais e criar rascunhos locais.

**AUTORIZAÇÃO ESPECÍFICA:** ler documentos particulares, anexar arquivos ao portal,
enviar mensagens, efetivar inscrição, aceitar termos, requerer bolsa e solicitar dados
financeiros quando o documento exigir.

**SOMENTE TITULAR:** autenticação gov.br, fornecimento de senha, verificação em
duas etapas, biometria e outras etapas de verificação pessoal.

A política em `permission_guard.py` é uma base técnica para um executor futuro.
O código atual não realiza essas operações sensíveis por conta própria.

## Fonte de verdade e evidência

Cada decisão deve registrar: URL oficial, instituição, número do edital, versão
e retificação, prazo com fuso local, regra/citação e página, status documental,
protocolo, responsável pela etapa e o próximo gate. Havendo dúvida, classificar
como `EVIDENCE_GAP`, não como concluído.
