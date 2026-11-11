# Critérios de aceitação e segurança — BDC Monetization OS

## Aceitação de skill
- [ ] Frontmatter tem name `bdc-site-monetization-os`.
- [ ] Nenhum segredo, ID de AdSense, CPF, chave OAuth ou dado de cliente real.
- [ ] Caminhos das skills existentes do agente resolvem corretamente.
- [ ] Contrato separa análise, implementação, revisão, deploy e aprovação por terceiros.
- [ ] Modelagem financeira executa com matemáticas reproduzíveis e status de hipótese.
- [ ] Documentação para SEO, AdSense, LGPD, B2B, e-books, GA4/GSC e QA está presente.
- [ ] Branch + PR de revisão, sem merge direto em produção.

## Aceitação do site (bloqueante para AdSense)
- [ ] URL/domínio final e titular identificados.
- [ ] Páginas públicas funcionais, navegação e conteúdo original substancial.
- [ ] Sem conteúdo placeholder/matéria gerada em massa sem valor editorial.
- [ ] Política de privacidade/cookies e demais disclosures jurídicos adequados.
- [ ] Artigos com autor, verificações, licença de imagens e fontes quando pertinentes.
- [ ] Testes técnicos mobile, status, renderização, canonical, robots, sitemap e velocidade.
- [ ] Consentimento e direitos de usuários/menores tratados.
- [ ] Propriedade do site e status Google AdSense conferidos em fonte oficial.
- [ ] Publisher ID real e ads.txt configurados somente após verificação e autorização.
- [ ] Ausência de tráfego artificial, incentivo a clicar e ad placements enganosos.
- [ ] Publicação/alteração de anúncio em produção aprovada e documentada.

## Teste de regressão econômico
Exemplo: 10.000 pageviews × 80% elegíveis × R$ 5 RPM / 1.000 = R$ 40 (hipotético). Com 0 elegíveis = R$ 0. Com conta não aprovada = R$ 0 realizado independentemente de visitas.

## Entrega obrigatória
`IMPLEMENTADO`: arquivos/commit/PR; `VALIDADO`: evidência executada; `PENDENTE`: credenciais/autorização/site/revisão; `RISCOS`: políticas, privacidade e receitas; `PRÓXIMA AÇÃO`: pequena e verificável.
