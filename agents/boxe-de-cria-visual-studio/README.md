# BDC Visual Identity & Creative Studio v1.0

Sistema portátil de identidade visual e produção de peças para o **portal BOXE DE CRIA**: notícias, perfis de lutadores, eventos, FISIOBOXE, guias, redes sociais e publicidade identificada.

**Estado:** design system e runtime determinístico de validação e templates; NÃO é um gerador de imagens completo nem substitui ferramentas gráficas/serviços de imagem. Não contém logotipos/fotos oficiais licenciados. Não modifica nem publica o site Lovable.

## Integração canônica
- Agente editorial existente: `agents/boxe-de-cria-media-revenue/` (não duplicar suas políticas de verificação).
- Agente Carousel: `agents/boxe-de-cria-carousel-orchestrator/` (usar para carrosséis educativos, não presumir que regras do carrossel servem para capas jornalísticas).
- Art & Sprite Director: reservado para jogos/sprites; não reutilizar como pipeline de site sem adaptar escopo.
- Site: Lovable BOXE DE CRIA Nexus (código do produto fica no repositório conectado pelo Git Sync).

## Ativar
- [ChatGPT](ACTIVATE_CHATGPT.md)
- [Grok](ACTIVATE_GROK.md)
- [System Prompt compartilhado](SYSTEM_PROMPT.md)
- [Manual de marca](BRAND_GUIDELINES.md)
- [Brand tokens em JSON](config/brand.tokens.json)
- [Presets de exportação](config/image-presets.json)
- [Handoff Lovable](docs/LOVABLE_HANDOFF.md)

## Uso local: apenas stdlib Python 3.11+
```bash
python runtime/visual_qa.py tokens
python runtime/visual_qa.py presets
python runtime/template_gen.py --preset news_hero --title "Manchete de exemplo" --section "BOXE" --output var/news_hero.svg
python -m unittest discover -s tests -v
```
O SVG é **layout editável com espaços reservados**, nunca notícia pronta nem foto documental. O logotipo deve entrar depois como arquivo oficial validado, sem redesenho. Ausência de foto autorizada => placeholder editorial honesto.

## Regras fundamentais
1. Não inventar atleta, luta, placar, uniforme, federação, fala ou evento; nunca simular foto documental com IA.
2. Não modificar rostos/corpos/tatuagens ou logotipos oficiais sem pedido e autorização explícitos.
3. Não usar imagem sem licença/consentimento comprovados.
4. Gráficos científicos e tabelas com texto/dados verificados; produzir texto determinístico quando exatidão for essencial.
5. Texto legível no celular, contraste adequado, safe areas e arquivo-mestre separados dos exports.
6. Separar patrocinado de editorial, preservar credibilidade e evitar anúncio que confunda com notícia.
7. Não publicar automaticamente: verificar fidelidade, direitos e dados antes do deploy.

## Limites
As skills são contratos reutilizáveis por modelos de IA; instalar apenas estes arquivos não disponibiliza motores de renderização, Adobe, Penpot ou acesso Lovable. Render, compressão WebP/AVIF, testes visuais com navegador e publicação exigem ferramentas e execução reais.


## CRIA APPAREL — Design de camisas e uniformes

A [skill de vestuário](skills/apparel-design/SKILL.md) define as linhas Alunos, Treinador e Premium, além de métodos de estampa, matriz visual e auditoria de produção. Manual: [APPAREL_MANUAL.md](docs/APPAREL_MANUAL.md); ficha para fornecedores: [PRODUCTION_BRIEF.md](templates/PRODUCTION_BRIEF.md).

Rodar QA sem bibliotecas externas:

```bash
python agents/boxe-de-cria-visual-studio/runtime/apparel_qa.py --input agents/boxe-de-cria-visual-studio/examples/student_training_tee.json --gate concept
python -m unittest discover -s agents/boxe-de-cria-visual-studio/tests -v
```

**Mockup != arte pronta de estamparia.** Somente produção autorizada com arquivo original rastreado e amostra física aprovada. Nunca salvar assets privados de marca no GitHub público.


### Referências enviadas — novembro de 2026

As dez páginas visuais de identidade e estampas foram auditadas sem inserir imagens privadas no GitHub: [perícia de versões](docs/APPAREL_REFERENCE_AUDIT_2026-11.md) • [manifesto JSON](config/apparel.reference-manual.json). São **referências em análise**, não uma atualização automática da paleta canônica nem arquivos de produção.
