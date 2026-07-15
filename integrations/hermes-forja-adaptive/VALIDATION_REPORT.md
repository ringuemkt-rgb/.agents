# Relatório de validação — Hermes FORJA 2.1

Data: 15 de julho de 2026.

## Testes executados

- Compilação Python de `forja_foundry` e `tests`: aprovada.
- 8 testes unitários: aprovados.
- Parsing YAML dos três perfis, distribuições e bundle: aprovado.
- Instalação isolada via `pip --no-build-isolation`: aprovada; versão importada `2.1.0`.
- Ciclo integral: fingerprint → candidata → avaliação → promoção → catálogo: aprovado.
- Avaliação integral: score `1.0`, verdict `auto-promote`, teste de regressão aprovado.
- Recuperação: skill sem backup foi colocada em quarentena após três falhas consecutivas.
- Scanner: execução remota por pipe foi bloqueada no teste.

## Limites

O ambiente de construção não possui PowerShell para executar o instalador Windows. Os scripts `.ps1` passaram por verificação estrutural de delimitadores, mas a instalação completa deve ser confirmada no PC alvo com `DIAGNOSTIC.ps1`.

A chamada real à NVIDIA não foi feita porque nenhuma chave secreta foi incluída no ambiente de teste. O cliente foi testado por construção de payload, multimodalidade e parsing interno; `DIAGNOSTIC.ps1` faz o teste online quando `NVIDIA_API_KEY` estiver configurada.
