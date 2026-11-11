---
name: bdc-site-monetization-os
description: Orquestra monetização auditável do portal e blog BOXE DE CRIA: AdSense, SEO, analytics, patrocínios, afiliados, produtos, leads, LGPD, QA e métricas financeiras.
---

# BDC SITE MONETIZATION OS — v1.0 (2026-11-11)

## Quando ativar
Acionar em toda tarefa sobre monetização, tráfego orgânico, conteúdo comercial, AdSense, patrocinadores, produtos, afiliados, analytics, funil de conversão, readiness de publicação ou auditoria de receita do site/blog BOXE DE CRIA. Não substituir as skills filhas; **orquestrar** as existentes:
- `../adsense/SKILL.md`
- `../seo-search/SKILL.md`
- `../finance/SKILL.md`
- `../commercial/SKILL.md`
- `../editorial-qa/SKILL.md`
- `../fact-checking/SKILL.md`
- `../legal-privacy/SKILL.md`
- `../fighter-records/SKILL.md`
- `../lovable-engineering/SKILL.md`
- `../../AGENT.md` e `../../../boxe-de-cria-visual-studio/AGENT.md`

## Missão
Desenvolver um portal brasileiro de boxe e artes marciais com editorial verificável, audiência própria, vendas úteis e anúncios não intrusivos. Priorizar originalidade, experiência de treinador/fisioterapeuta e interesse do leitor. A decisão comercial **nunca** altera fatos esportivos, vereditos científicos ou direitos de imagem.

## Fonte oficial / separação de responsabilidades
- Agentes, prompts e critérios: `ringuemkt-rgb/.agents` (este repositório).
- Código de produto: repositório vinculado **comprovadamente** ao projeto oficial; verificar Git Sync antes de alterar.
- Projeto Lovable candidato: BOXE DE CRIA Nexus; **não presumir publicação, conexão ou domínio** sem inspeção.
- Site e propriedade Search Console: identificar domínio canônico, CNAME/DNS, permissões e status; não alegar conexão ou aprovação.
- GitHub/Codex/Grok/ChatGPT: leem a mesma skill. Estar versionada NÃO significa que execução agendada, MCP, propriedade Google ou site estão conectados.

## Pipeline operacional — gates de execução
**G0 Inventário (read-only)**: identificar site exato e domínio, branches e deploys, CMS/renderização, sitemap/robots, analytics, GSC, AdSense, meios de pagamento, autoria, fontes e permissões. Se desconhecidos: marcar PENDENTE, nunca inventar.
**G1 Saúde técnica**: HTTPS; conteúdo HTML rastreável; status 200; canonical; robots; sitemap contendo URLs canônicas; navegação; responsividade; noindex correto; 404 e redirecionamentos; CWV, LCP/INP/CLS e performance real em dispositivos móveis.
**G2 Qualidade editorial**: cada peça deve ter intenção do leitor, resposta própria, expertise demonstrável, título factual, autor real, data de publicação e atualização substantiva, fontes primárias, direito de mídia, diferencial original e revisão humana quando exigida. Em saúde/TEA: evidência científica rastreável, DOI quando disponível, revisão especializada e limites; nunca prometer cura ou resultados.
**G3 SEO/Search Console**: mapear clusters de intenção, termos e canibalização; otimizar title/meta/H1, interlink contextual, URLs, schema apenas quando representarem o conteúdo real; verificar indexação e consultas por URL. Não fingir rich results.
**G4 AdSense**: verificar elegibilidade, propriedade do site, páginas substanciais, compliance, anúncios e consentimento. Só depois de aprovação configurar código do publisher **real**, ads.txt validado e Auto Ads com densidade prudente; monitorar políticas, tráfego inválido e page RPM.
**G5 Receita direta**: catálogo com preços confirmados, páginas claras de ofertas, rastreio de leads (sem expor dados), campanhas de patrocínio identificadas, afiliados com disclosure, loja/produtos e políticas de reembolso/contratos.
**G6 Instrumentação**: GA4/GSC/AdSense ou ferramentas gratuitas equivalentes somente com autorização; eventos de page_view, article_view, video_click, lead_start, lead_submit, offer_view, checkout_start, purchase VERIFIED; UTMs sem PII.
**G7 Experimentos**: um teste por vez, hipótese e KPI de decisão pré-definidos; comparar períodos/consultas com base equivalente; alterações de anúncios sob controle; jamais otimizar clique artificial.
**G8 Validação & entrega**: testes e URLs verificáveis, fontes e datas, riscos, alterações realizadas, guardrails, rollback, próximos passos. Nenhum deploy/pagamento/publicação em produção sem permissão explícita e revisão prévia.

## 12 competências acionáveis
1. **SEO técnico**: rendering, indexação, canônicos, sitemap, structured data, CWV.
2. **SEO editorial**: intenção, SERP, clusters, brief, atualização legítima, E-E-A-T como conceito (não score oficial).
3. **Jornalismo esportivo**: notícias originais, agenda, cartéis, atletas, fonte oficial e correções auditáveis.
4. **Ciência/FisioBoxe**: literatura primária, método, DOI/limitações; proteção a alegações médicas.
5. **AdSense**: elegibilidade, setup, ads.txt, políticas, UX, invalid traffic, experimentos controlados.
6. **Analytics/atribuição**: GSC, GA4, funil, consentimento, relatórios segmentados.
7. **CRO e UX**: propostas, CTAs honestas, acessibilidade, velocidade, confiança.
8. **Patrocínios B2B**: mídia kit, inventário, pacotes, proposta, contratos e entregáveis.
9. **Afiliados**: reviews testados e realmente úteis, disclosure de comissão, rastreamento.
10. **Produtos digitais**: guia, videoaulas e serviços com pré-venda controlada e validação de demanda.
11. **Financeiro**: receita observada vs. prevista, margem de contribuição, CAC, RPM, coortes, custos e impostos.
12. **Automação segura**: coleta legal de fontes, deduplicação, drafts, QA, alertas; publicação só com autorização editorial.

## Política de dados e de negócios
- NUNCA pedir para clicar em anúncios, testar clique próprio, comprar tráfego não qualificado, simular conversões ou alterar CSS para criar cliques acidentais.
- Nunca divulgar IDs de conta, tokens, segredos, credenciais, emails pessoais, IDs de beneficiários ou dados de clientes em repo público. `ads.txt` exige ID real, obtido via proprietário.
- Não criar rankings pagos como se fossem mérito esportivo; patrocinado sempre identificado.
- Não reproduzir imagens de campeonatos sem licença; citações e referências não garantem direitos de uso.
- Não publicar automaticamente notícias copiadas, artigos em escala sem valor ou estatísticas inventadas.
- LGPD: finalidade e minimização, consentimento quando exigido, segurança, retenção e direitos do titular. Revisão jurídica para casos materiais.
- Produto/cadastro: venda só com checkout autorizado, descrição correta, recibo e política aplicável.
- Receita, posição de busca e aprovação AdSense nunca são garantidas.

## Estimativas financeiras e indicadores (separar claramente)
`page_RPM = receita_ads_real / pageviews_monetizadas * 1000`.
`receita_ads_simulada = pageviews_monetizadas_estimadas * RPM_assumido / 1000`.
`ticket_medio = receita_vendas / número_vendas`.
`CVR_lead = leads_qualificados / sessões_atribuídas`.
`CVR_venda = compras / leads_qualificados` (usar janela e atribuição documentadas).
`margem_contribuicao = receita_recebida - taxas_checkout - comissão - custos_variáveis - impostos_variáveis`.
Não confundir usuários, sessões, impressões, páginas visualizadas, pageviews monetizáveis, cliques, receita bruta e lucro. Moeda BRL por padrão.

### KPIs de decisão
- **Tráfego**: impressões/clicks GSC, CTR por query, indexação real, sessões GA4, pageviews por formato/rota.
- **Qualidade**: engajamento por landing page, leitura e scroll estimados com instrumentação, retorno, Core Web Vitals.
- **Negócio**: leads consentidos, vendas pagas, taxa de conversão, GMV vs receita líquida, contratos ativos e recebimento.
- **AdSense**: aprovação/status, page RPM observado, pageviews com anúncio, política/invalid traffic, cobertura.
- **Produção**: posts publicados com aprovação, custo por artigo, tempo de revisão e uso de fontes.

## Portfólio de conteúdo proposto, sujeito a validação de intenção
Pilares: `/tecnica/`, `/historia/`, `/boxe-brasileiro/`, `/eventos/`, `/atletas/`, `/equipamentos/`, `/ciencia/`, `/fisioboxe/`, `/produtos/`. Não criar rotas vazias nem disputar a mesma query com páginas similares. Atenção redobrada a dados de atletas menores.

## Rotinas que podem ser executadas sem publicação
- **Semanal**: auditoria Search Console/analytics quando conectados, top 10 URLs, páginas em queda, oportunidade de título, backlog de correções, qualidade das fontes.
- **Mensal**: resultado financeiro conciliado, contratos e propostas, custo/conversão, SEO e AdSense, backlog priorizado por impacto × custo × risco.
- **Trimestral**: auditoria jurídica editorial, segurança, receita por canal, estratégia de produtos e UX mobile.
Rotina não constitui agendamento persistente; agendar apenas via ferramenta autorizada.

## Rotas de execução
- `auditar o blog` → G0-G4 + lista priorizada de falhas e evidências.
- `preparar AdSense` → checklist de prontidão + lacunas, sem declarar aprovado.
- `monetizar artigo` → intenção, oferta útil e placement compatível com UX/políticas.
- `criar calendário` → pesquisar demanda, lacunas e esforço; saída priorizada por potencial e evidência.
- `montar mídia kit` → utilizar só números medidos e escopo da campanha.
- `receita mensal` → anexar fonte de cada valor; separar realizado, contratado, simulado.
- `desenvolver site` → trabalhar na base de código oficial com PR, CI e aprovação para deploy.

## Contrato de saída obrigatória
1. Situação do ativo (identidade e acesso confirmados, últimas datas observadas);
2. Oportunidade, seu grau de evidência e resultado esperado;
3. O que foi **IMPLEMENTADO**, **VALIDADO**, **PENDENTE**;
4. Métricas/cálculos reproduzíveis, com fontes e período;
5. Riscos técnicos, legais e comerciais;
6. Próximo passo de maior retorno e teste de aceitação.

## Documentos auxiliares
- `RUNBOOK.md`: execução passo a passo sem serviços pagos obrigatórios.
- `REVENUE_MODEL.json`: cenários estritamente hipotéticos, editáveis e sem falsa precisão.
- `ACCEPTANCE.md`: contrato de aceitação/QA antes de ativar anúncios e comercial.
- Fontes normativas: https://support.google.com/adsense/answer/91205?hl=pt-BR ; https://support.google.com/adsense/answer/48182?hl=pt-BR ; https://support.google.com/adsense/answer/9261307?hl=pt-BR ; https://developers.google.com/search/docs/fundamentals/creating-helpful-content?hl=pt-br ; https://developers.google.com/search/docs/essentials/spam-policies?hl=pt-br ; https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap?hl=pt-br .
