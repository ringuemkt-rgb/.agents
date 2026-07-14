# Arquitetura do Cria Agent Hub

## Visão geral

O hub é dividido em quatro camadas:

```text
objetivo do usuário
      ↓
workflow determinístico
      ↓
agentes especializados
      ↓
ferramentas externas + repositório do produto
      ↓
evidência, testes e decisão de gate
```

## 1. Registro

`config/agents.json` descreve agentes, capacidades, dependências e limites.

`config/workflows.json` descreve DAGs. O orquestrador apenas ordena passos e rejeita ciclos; ele não inventa dependências durante a execução.

`config/tools.json` contém fontes externas explícitas. Ferramentas são clonadas em `.vendor/`, nunca misturadas automaticamente ao código do hub.

## 2. Núcleo determinístico

O pacote `cria_agents` usa somente a biblioteca padrão do Python para:

- carregar e validar registros;
- verificar referências entre agentes e workflows;
- ordenar passos por dependência;
- sincronizar repositórios externos em diretório confinado;
- produzir `tools.lock.json` com os commits resolvidos.

O núcleo não chama LLM e não executa comandos de instalação definidos no catálogo. Essa separação reduz risco de supply chain e comportamento implícito.

## 3. Agentes

Cada agente possui um `AGENT.md` com:

- missão;
- procedimento;
- limites;
- entregáveis;
- gates relevantes.

Um agente é um contrato operacional, não uma personalidade solta. Workflows podem reutilizar o mesmo agente em etapas diferentes.

## 4. Ferramentas externas

As integrações são dependências de desenvolvimento opcionais. `cria-agents tools sync`:

1. valida URL e destino;
2. clona ou atualiza a ferramenta;
3. faz checkout destacado do `ref` solicitado;
4. registra o SHA real em `config/tools.lock.json`.

Instalação de dependências permanece explícita. Consulte `install_commands` e revise antes de executar.

## 5. Repositórios de produto

O hub não guarda o código do Cria do Tatame nem do MotoJá. Ele atua sobre os repositórios oficiais e respeita seus próprios `AGENTS.md`, CI, canon e contratos.

## Modelo de confiança

- Configuração local do hub: confiável após CI.
- Repositórios externos: não confiáveis até revisão e lock.
- Texto gerado por IA: proposta, não evidência.
- Testes e builds: evidência apenas quando realmente executados.
- Deleção: permitida somente depois de migração e gate de QA.

## Evolução

Novos agentes só devem ser criados quando houver responsabilidade, entradas, limites e entregáveis distintos. Caso contrário, amplie um agente existente em vez de multiplicar nomes e burocracia.
