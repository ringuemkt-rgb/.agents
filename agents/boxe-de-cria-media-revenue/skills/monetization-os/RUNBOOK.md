# RUNBOOK — ativação progressiva do negócio de mídia BOXE DE CRIA

Data de elaboração: 2026-11-11. Este arquivo é orientação operacional; não comprova aprovação do Google nem instalação no site.

## Gate zero — prova de propriedade e ambiente
- [ ] Confirmar se o portal canônico é **BOXE DE CRIA Nexus** e se a publicação real usa domínio próprio; não tratar outro site de treinamento como substituto.
- [ ] Inspecionar no Lovable `project_id` e workspace acessíveis; exportar status de publicação/deploy e checar vínculo Git Sync. Não tentar outro projeto ao acaso.
- [ ] Verificar domínio, DNS, HTTPS, canonical e versões `www`/raiz, redirects.
- [ ] Confirmar conta AdSense existente/status na interface do proprietário; nunca registrar segunda conta por tentativa.
- [ ] Confirmar Search Console e GA4 em conectores autorizados; conexão bloqueada => “sem dados”, não zero.
- [ ] Inventariar artigos, imagens, vídeos incorporados, dados de atletas, produtos, checkout, CRM e dashboards existentes.

## Auditoria técnica (sem credenciais)
1. Inspecionar homepage e 5 artigos por fetch/render; status, titles, description, H1, canonical, hreflang se aplicável.
2. Ver `robots.txt`, `sitemap.xml` e status de cada URL; não publicar URLs 404/redirect/noindex em sitemap.
3. Conferir renderização no HTML obtido pelo crawler, não apenas React montado no browser; considerar prerender/SSR quando necessário.
4. Verificar links internos, páginas órfãs, alt de imagens, idioma pt-BR, breadcrumbs, schema coerente (Article, NewsArticle, Person, Event, FAQ somente com conteúdo real).
5. Aferir PageSpeed mobile e CWV de dados de campo quando houver; metas técnicas baseadas em documentação atual.
6. Registrar todos os achados com `url`, `evidência`, `gravidade`, `owner`, `correção`, `teste`, `status`.

## Prontidão para AdSense (site, não YouTube)
1. Editorial substancial e original, site terminado e funcional, menus e páginas de confiança, conteúdo próprio e permissões sobre mídia.
2. Política de privacidade precisa refletir cookies, parceiros publicitários, base legal, direitos dos titulares e eventuais transferências internacionais; revisão jurídica pertinente.
3. Acesso legítimo ao HTML, verificação de domínio, política editorial e decisão de anúncios para páginas sensíveis.
4. Na interface do Google, adicionar domínio e seguir a verificação e avaliação de site. **Não** marcar aprovado até confirmação direta.
5. Após aprovação, colocar ID de publisher verdadeiro no código e `ads.txt`, somente no site certo; não guardar IDs privados em templates genéricos.
6. Começar com poucos anúncios em artigos substanciais; comparar velocidade mobile/receita/engajamento. Não ativar em login, checkout, páginas vazias ou layout enganoso.
7. Monitorar alertas de política, tráfego inválido e cobertura. Em qualquer alerta, reduzir anúncios/suspender ação comercial arriscada e investigar antes de continuar.

## SEO editorial / pipeline
1. Escolher uma query real e o público: iniciante, fã da competição, atleta ou família.
2. Mapear SERP e fontes oficiais; assunto precisa de diferencial prático e atualidade verificável.
3. Rascunhar artigo com autoria real, exemplos originais, fontes e links internos úteis.
4. Para perfis/cartéis, listar fonte exata de cada resultado; não inferir cartel com dados de terceiros incompletos.
5. Para saúde/TEA, checar revisão científica, DOI quando verificável e evidência/limitações.
6. Revisão humana aprova reportagem, imagens e claims; somente então publicar.
7. Adicionar ou atualizar sitemap, verificar URLs canônicas, medir indexação e resultados depois de janela suficiente.

## Produtos, afiliados e patrocínios
- Catálogo piloto: guia `Boxe do Zero`, análise técnica individual de treino e pacotes presenciais com valores confirmados antes de vender.
- Oferta: página dedicada, qualificação para quem serve, entregáveis, preço e moeda, contato, regras de reembolso e privacidade.
- Afiliados: escolher somente marcas/produtos compatíveis e autorizados, informar eventual comissão; reviews de primeira mão, não fingir uso.
- B2B: patrocínios de reportagem/programa claramente rotulados, contratos com escopo/cotas/impressões medidas, sem garantir audiência/posição esportiva.
- Checagem financeira mensal: valores efetivamente recebidos, custos, impostos, comissão, margem, reembolsos.

## Experimentos com hipóteses
- Ex.: artigo `como limpar luvas`: adicionar um guia original comparando rotina de manutenção e vídeo demonstrativo. Métrica primária: cliques orgânicos na URL em 28 dias completos; secundária: cliques para produto com consentimento. Não contar a flutuação natural como efeito causal sem controle.
- Ex.: placement AdSense: comparar cobertura, page RPM e CLS/engajamento entre configurações, com volumes significativos.
- Ex.: patrocinador: testar proposta com inventário comprovado e medir resposta/proposta/contrato, não apenas envios.

## Resumo mensal obrigatório
```
MÊS:
TRÁFEGO: sessões / pageviews / Google clicks / URLs indexadas (datas e fontes)
ADSENSE: status real / page RPM real / receita real
PRODUTOS: visitas ofertas / leads / checkout / vendas pagas / devoluções
PATROCÍNIOS: prospectados / propostas / contratos / recebido
CUSTOS: domínio / hospedagem / taxas / mídia / ferramentas / impostos / trabalho
RESULTADO: receita bruta / contribuição / resultado operacional
QUALIDADE: atualizações aprovadas / alertas Google / fontes / copyright
TOP 3 AÇÕES: priorizadas com proprietário, evidência e teste
```

## Modos de falha e fallback
- Lovable indisponível: gerar PR de especificação no repo de agentes, sem alegar aplicação no site.
- GSC Wizard sem assinatura: usar interface gratuita do Google Search Console do proprietário, ou exportações CSV fornecidas; não exigir pagamento.
- AdSense sem API/status: pedir print da seção Sites ou integração autorizada; nunca deduzir aceitação pela presença de script.
- Sem site publicado: focar em lançamento e qualidade editorial, não inserir anúncios fictícios.
- Sem vendas: demonstrar hipótese de oferta e validar primeiro cliente antes de extrapolar LTV/receita.

## Definição de pronto
Ver `ACCEPTANCE.md`. Nenhum item de prontidão substitui a revisão e decisão do Google.
