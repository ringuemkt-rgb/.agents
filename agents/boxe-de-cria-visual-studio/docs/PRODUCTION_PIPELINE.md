# Pipeline de produção visual BDC

1. **Entrada:** ID do artigo, título aprovado, editoria, audiência, foto aprovada (ou indicação de ilustração), permissão de uso, autor, data e destino.
2. **Roteamento:**
   - `real_photo`: retouch conservador, nunca inventar lutador/evento.
   - `illustrative`: brief de arte, indicar claramente "Ilustração" quando couber.
   - `data_viz`: gráfico determinístico, dados verificados.
   - `UI`: design tokens HTML/CSS, não screenshot de foto gerada.
3. **Composição:** escolher preset, grid, safe area, título HTML, linha de crédito, alt text, crop não destrutivo, contraste.
4. **QA:** direitos, integridade da marca/pessoa, presença de caracteres corretos, legibilidade em 320px, sensibilidade de violência e qualidade de imagem. Para eventos envolvendo menores, revisão reforçada.
5. **Exports:** arquivo-mestre + variantes mobile/desktop; metadados manifest para raster; não embutir segredos.
6. **Publicação:** revisão editorial e autorização comercial distintas. Nenhum ad deve parecer botão de navegação ou resultado esportivo.
7. **Medição:** Core Web Vitals e posição de títulos, cliques em matérias, layout shift, sem prometer tráfego/receita.

A automação começa vazia de fotos/logos até receber os masters autorizados. Não usar imagem de busca como se estivesse licenciada.
