# Integrações Externas

As ferramentas abaixo são sincronizadas a partir dos repositórios originais. Elas não precisam permanecer como forks separados no perfil `ringuemkt-rgb`.

| ID | Fonte | Uso |
|---|---|---|
| `agent-sprite-forge` | `0x0funky/agent-sprite-forge` | planejamento e processamento de sprites e mapas |
| `sprite-gen` | `aldegad/sprite-gen` | extração, alpha, atlas, manifesto e curadoria |
| `spec-kit` | `github/spec-kit` | desenvolvimento orientado por especificação |
| `game-master` | `Sstobo/Claude-Code-Game-Master` | referência de coordenação para produção de jogos |
| `game-development-reference` | `HermeticOrmus/claude-code-game-development` | padrões e referências de desenvolvimento |
| `agent-game-forge` | `0x0funky/agent-game-forge` | workflows de construção de jogos |
| `character-animation-creator` | `tachikomared/character-animation-creator-skill` | apoio à criação de animação de personagens |
| `image-cockpit` | `dreiachse-cyber/image-cockpit-for-codex-workflows` | cockpit visual opcional; desativado por padrão pelo tamanho |

## Sincronização

```bash
cria-agents tools list
cria-agents tools sync
```

O sync faz checkout destacado do `ref` configurado e grava o SHA resolvido em `config/tools.lock.json`. O arquivo de lock é local por padrão, permitindo atualização consciente sem inflar o repositório central.

## Instalação

O catálogo registra comandos sugeridos, mas o hub não os executa automaticamente. Revise licença, código e dependências antes de instalar qualquer ferramenta.

## Política para forks antigos

Depois que este hub estiver validado, os forks pessoais usados apenas como cópia podem ser excluídos. O hub continuará apontando para as fontes originais e não dependerá dos repositórios antigos do perfil.
