# BOXE DE CRIA — Manual de identidade digital v1.0

## Posicionamento
**Um portal esportivo e uma base de dados confiável, não uma página de promoções.** Força visual sem sensacionalismo; tradição do boxe aliada a tecnologia e jornalismo verificável.
Slogan institucional: **De Cria pra Cria**. Valores: disciplina, honra, respeito, inclusão, integridade. Lema: **Ser forte é ser gentil.**

## Canon visual
- Preto `#0B0B0B`: superfícies primárias e dramaticidade.
- Dourado `#C9A24E`: marca e destaque de autoridade, não todas as linhas.
- Vermelho `#B33939`: elementos de ação e urgência, nunca indicador falso de perigo.
- Branco `#F3F3F3`: texto, áreas claras e legibilidade.
- Grafite `#242424`: planos secundários.
Cores exatas em `config/brand.tokens.json`. Não inferir propriedades psicológicas universais dessas cores.

## Tipografia
Para editorial digital: Oswald em títulos; Inter no corpo, menus e estatísticas, se licenciadas e disponíveis. Fallbacks seguros: Arial Narrow, Arial, sans-serif. Bebas Neue é alternativa de títulos, não corpo. Não versionar arquivos de fonte sem licença.

## Linguagem de imagem
- Notícia: foto real autorizada, data, local e crédito; edição cromática moderada.
- Editorial conceitual: imagem autoral ou gerada, identificada como ilustração quando possa ser confundida com registro factual.
- Fichas de atletas: foto real com permissão ou avatar neutro; cartel e bandeiras sem dados inventados.
- Evento: card, data e local verificados; publicidade explicitamente rotulada.
- FISIOBOXE: diagramas anatomicamente revisados, valores e unidades corretas, fontes auditáveis; evitar imagens médicas falsas.
- UI: fundo neutro e hierarquia limpa. Textura/metal/fumaça discretos em capas, nunca sobre tabelas.
- Segurança editorial: imagens de ferimentos explícitos exigem avaliação de política de anúncios e contexto.

## Asset oficial e fidelidade
Logo oficial deve entrar COMO ARQUIVO ORIGINAL com hash SHA-256 e proveniência, sem geração, redesenho, estilização automática, deformação, troca de cor ou sobreposição não aprovada. Se o arquivo não estiver disponível, não simular sua aparência. Usar placeholder com instruções de inserção.
Fotos reais: preservar identidade, feições, expressão, corpo, tatuagens, uniforme, contexto factual e crédito. Só alterar pessoas e cenário mediante instrução explícita e editorialmente admissível; restauração é conservadora.
CTRK, CB Prisco Team e quaisquer marcas de terceiros devem ser tratadas como assets independentes, com direitos e autorização próprios. Não fundi-las ao logotipo BOXE DE CRIA.

## Diretrizes de layout
- Grid web 12 colunas; mobile-first; títulos não cobrem rostos.
- Margem interna para social 4:5 de pelo menos 7%, além de considerar áreas de interface no aplicativo de destino.
- Tabelas e números renderizados por HTML/SVG determinístico, não gerados como texto em fotografias por IA.
- Texto corrido do site deve ser HTML acessível; texto embutido na capa não substitui título HTML.
- Contraste alvo WCAG AA: pelo menos 4.5:1 para texto normal e 3:1 para texto grande. Teste manual e automatizado.

## Presets
Ver `config/image-presets.json`; exportação online deve usar WebP/AVIF/JPEG com dimensões responsivas; preservar master PNG/SVG/TIFF conforme caso. SVGs do runtime são bases editáveis, não imagens finais.

## Regras de rejeição
REPROVAR se houver logo aproximada, rosto alterado, cartel inventado, texto impossível de ler no celular, direitos incertos, corte destrutivo, foto fabricada de evento real, selo de verificação falso ou conteúdo de saúde sem revisão.
