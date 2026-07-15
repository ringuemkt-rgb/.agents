# Hermes FORJA Adaptive NVIDIA 2.1

Pacote instalável do agente local/híbrido FORJA para Windows, baseado no Hermes Agent.

## Capacidades

- perfil local com Ollama e Qwen 3.5 selecionado pela RAM;
- perfil rápido com NVIDIA `minimaxai/minimax-m3`;
- perfil especialista com Mixture of Agents, Hugging Face, OpenRouter e fallback local;
- programação autônoma com Git, testes e build;
- criação de skill candidata ao detectar bloqueios repetidos;
- pesquisa em fontes primárias, teste de regressão, scanner, score e promoção;
- rollback ou quarentena depois de três falhas consecutivas;
- aprovação inteligente, cron perigoso bloqueado e avaliação Docker sem rede.

## Instalação

1. Baixe `releases/Hermes_FORJA_Adaptive_NVIDIA_v2.1.zip`.
2. Confirme o SHA-256 publicado nesta pasta.
3. Extraia o ZIP e execute no PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\VERIFY_PACKAGE.ps1
.\INSTALL_WINDOWS.ps1
.\CONFIGURE_KEYS.ps1
.\DIAGNOSTIC.ps1
```

## Validação

O pacote passou por 8 testes unitários, parsing dos YAML, instalação isolada do pacote Python e ciclo integral de fingerprint, candidata, avaliação e promoção. O teste online NVIDIA e a execução integral do instalador PowerShell dependem do PC Windows e das chaves do operador; consulte `VALIDATION_REPORT.md`.

## Segurança

Nenhuma chave está no arquivo. Segredos são gravados somente nos `.env` locais dos perfis. A promoção de uma skill exige score mínimo de 0,85, hash correspondente, fonte primária e regressão verde.
