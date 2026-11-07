# Handoff para o Lovable — BOXE DE CRIA Nexus

Projeto: https://lovable.dev/projects/a63e471f-f034-481c-a75c-8dd9978de7e7
Repositório do site (Git Sync): definir/confirmar no Lovable. O Cria Agent Hub NÃO é o repositório do produto.

## Contrato de implementação
1. Ler os tokens JSON do studio; mapear cores/fontes e espaçamentos em CSS variables sem sobrescrever silenciosamente designs existentes.
2. Construir componentes: `ArticleHero`, `FighterCard`, `EventPoster`, `SourceCredit`, `EditorialBadge`, `SponsoredLabel`, `ResponsivePicture`.
3. Usar `<picture>` com `srcset`, `sizes`, `width` e `height`; lazy-load imagens não críticas e priorizar a imagem LCP. Títulos importantes em HTML.
4. Imagens editoriais oficiais só depois de autorização/manifest. Sem arquivo? exibir placeholder neutro, não atleta inventado.
5. Criar template OG por notícia, mas a URL pública deve refletir conteúdo rastreável e imagens com direitos aprovados.
6. Validar captura em 320px, 390px, 768px e desktop; aferir contraste (axe-core) e screenshot diff (Playwright).
7. Guardar arquivo mestre e derivados em mídia permitida; não subir fotos de menores nem consentimentos ao GitHub.
8. Não deployar sem aprovação; não habilitar AdSense automaticamente.

## Integração sugerida
Penpot (design), Sharp (derivados raster), SVGO (SVG estático), Playwright (regressão visual), axe-core (acessibilidade). Suas licenças devem ser verificadas; nenhuma dependência externa é instalada automaticamente por este agente.

## Smoke checklist
Rotas principais; nav mobile; alt text; fallback de retrato; não esconder cartel; performance em rede móvel; indicação de ilustrativa/patrocinada; sem pixels de logo reconstruídos.
