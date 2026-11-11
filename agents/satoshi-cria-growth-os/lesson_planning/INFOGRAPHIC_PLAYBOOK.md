# CRIA TECHNICAL INFOGRAPHIC SYSTEM v1.0
## Padrão de engenharia gráfica e revisão científica para BOXE DE CRIA, FISIOBOXE e CTRK
**Estado:** guia operacional — arte final depende de revisão humana
**Revisão:** 11/11/2026

### Princípio
A arte tem duas camadas independentes: (1) informação auditada, redigida e diagramada em texto vetorial; (2) ilustrações originais 2D, 2.5D ou 3D. Nunca permitir que um gerador de imagens seja a fonte final dos textos, números, logotipos, proporções anatômicas, citações ou regras de competição. Imagem publicitária não é validação científica.

### Quatro modelos
1. **Anatomia de ambiente/equipamento:** render isométrico de ringue com perspectivas consistentes; setas de chamada apontam exatamente para o elemento real; quadro de medidas contextualizado ao regulamento; oficiais e funções em área separada.
2. **Anatomia e regras:** vistas anterior, lateral e quando necessário posterior; cores + hachuras para zonas legais/ilegais, com exemplos de golpe válido; versão normativa e data no rodapé.
3. **Biomecânica e drill de manoplas:** três quadros (posição inicial, ação, recuperação), vetores com legenda, defesa e erros mecânicos observáveis; não desenhar articulações impossíveis nem afirmar que cotovelo rígido previne lesão em porcentagem fixa.
4. **Tática condicional:** matriz situação → leitura → decisão → consequência. A alternativa recomendada depende de distância, guarda, eixo, espaço e resposta; evitar regras universais do tipo "sempre" ou "nunca" sem base específica.

### Tratamento das quatro referências do briefing
- Ringue: a referência original mistura dimensões de regras distintas, inclusive boxe profissional. Não copiar medidas sem definir organização/ano.
- Zonas: não afirmar que capacete é obrigatório em todo o boxe amador; na World Boxing v5.0 é obrigatório para U17, U19 e elite feminino, e não permitido para elite masculino.
- Manoplas: referência apresenta letras corrompidas, sobreposições e visual confuso; refazer composição com ilustração sem texto, texto sobreposto em camada tipográfica separada.
- Canhotos: revisar absolutos; estratégia de pé externo e circular é contextual, não mandamento universal.

### Contexto normativo validado
Fonte: World Boxing Competition Rules v5.0, em vigor em março/2026, disponível em https://worldboxing.org/wp-content/uploads/2026/10/World-Boxing-Competition-Rules-March-2026-v5.0.pdf (consultado 11/11/2026). Conferir atualização antes de publicar.
- 13.12: dentro das cordas mínimo 6,10 m por lado; plataforma a 100 cm; quatro cordas a 40, 70, 100 e 130 cm.
- 6.1.1: árbitro controla e não pontua; cinco juízes pontuam.
- 7.2: alvo válido é frente/lados da cabeça e tronco, segundo os limites especificados; punch clean, superfície dos nós da luva e demais critérios.
- 13.3: headguard U17/U19 e elite feminino obrigatório; elite masculino proibido.
Contexto CBBoxe: https://cbboxe.org.br/transparencia/11/regras-oficiais. Para campeonato específico, conferir edital/regulamento local, não generalizar World Boxing para boxe profissional.

### Grade editorial
| Destino | Tamanho | Conteúdo sugerido |
|---|---|---|
| Feed Instagram | 1080×1350 (4:5) | uma tese central, 3–5 chamadas, footer curto |
| Story | 1080×1920 | uma ideia forte, 1–3 passos legíveis, CTA |
| PDF A4 | 2480×3508 a 300 dpi ou PDF vetorial | detalhamento técnico e referências completas |
| Apresentação | 1920×1080 | uma figura + um conceito por slide |

Usar área segura ~8% da largura para elementos principais e verificar prévia de recorte no Instagram. Para 4:5: título 72–108 px, subtítulo 36–54 px, rótulos 30–38 px, corpo preferencialmente 28–34 px; são parâmetros iniciais, ajustar pelo teste de leitura real. Para A4, texto diagramado vetor e fonte corporal pelo menos ~10 pt se destinado a impressão próxima.
Grid 12 colunas, espaçamento em múltiplos de 8, linhas-guia de 1.5–2 px quando 1080 px e contraste visual suficiente. Sem excesso de setas cruzadas, texto sobre imagem complexa ou texto menor que possa ser lido no telefone.

### Identidade sem inventar ativos
- BOXE DE CRIA: preto #0B0B0B, ouro #C9A24E, vermelho #B33939, branco #F3F3F3.
- CTRK: preto, branco e vermelho preservando os códigos/arte do arquivo oficial recebido.
- FISIOBOXE: base clínica (azul profundo, branco, acentos ciano); definir tokens do projeto antes de produzir lote.
- Logotipos: inserir apenas PNG/SVG original, sem gerar de novo, sem estilizar ou modificar letras.
- Pessoas reais: preservar rosto, corpo, roupa e proporções; não usar recriação generativa quando o briefing exige exatidão.
Tipografia: títulos fortes como Anton/Oswald/Bebas; subtítulos Manrope/Inter; corpo Inter. Evitar 3+ famílias e all-caps em parágrafos.

### Princípios perceptivos com aplicação prática
- Hierarquia por escala e localização: ver primeiro a ideia, depois a figura, depois detalhes.
- Proximidade e continuidade: rótulos ao lado do elemento, linhas não cruzadas.
- Redundância: diferença não deve depender somente de vermelho/verde; acrescentar ícone, texto ou padrão.
- Contraste para leitura: WCAG AA como referência de contraste 4,5:1 para texto comum, 3:1 para texto grande; 3:1 para gráficos essenciais. Fonte: https://www.w3.org/TR/WCAG22/.
- Psicologia das cores é contextual/cultural: vermelho pode comunicar alerta e ação, azul organização técnica, ouro tradição/premium, mas nenhuma cor garante conversões ou resultados pedagógicos.

### Pipeline obrigatório
1. Definir público, modalidade, instituição, faixa etária, objetivo e formato.
2. Escolher contexto normativo e auditar fontes primárias (organização, versão, data, link, seções).
3. Escrever todo o texto final em PT-BR, com revisão ortográfica e terminologia técnica; limitar chamadas à capacidade do formato.
4. Fazer wireframe (hierarquia, grids, bounding boxes, espaços de rótulos e fontes).
5. Criar ilustração técnica separada, **sem texto**, por desenho vetorial, 3D ou geração seguida de revisão anatômica.
6. Diagramar texto editável com SVG/PDF/Figma/Canva sobre a imagem; posicionar linhas-guia com revisão visual.
7. Inserir marca original como overlay intacto e assinatura editorial correta.
8. Rodar 4 auditorias: factual/segurança; anatomia/biomecânica; ortografia; legibilidade e recortes.
9. Exportar matriz vetorial ou PNG de alta resolução, PDF de referência e preview reduzido; testar tamanho real em Android.
10. Aprovação final antes de publicar.

### Escala QA 100 pontos
- Correção factual e fontes (25)
- Anatomia/biomecânica e diagramas (20)
- Legibilidade e hierarquia (20)
- Fidelidade às marcas e fotografias (15)
- Terminologia e português (10)
- Composição, acabamento e exportação (10)
*Falha crítica bloqueante:* regra de competição errada, segmento anatômico impossível, rosto alterado, logo redesenhado, texto ilegível/gibberish, referência científica fabricada ou estratégia perigosamente categórica. Nota alta não desbloqueia falha crítica.

### Exemplo de briefs aprováveis
**Ringue:** "Anatomia do ringue de Boxe Olímpico sob World Boxing v5.0 — março 2026": vista isométrica com postes, 4 cordas, padding, canto vermelho/azul/branco, árbitro, oficiais; mostrar apenas medidas validadas.
**Zonas:** "Onde um golpe limpo pode pontuar?": mapas frente e lateral, exemplo de jab com guarda e nota sobre regras.
**Manoplas:** "Três decisões para uma manopla mais segura": apoio, orientação do alvo, retorno defensivo; sem prometer prevenção absoluta.
**Canhotos:** "Pé de fora: quando ajuda e quando atrapalha": decisão contextual com cenários de leitura.

### Segurança editorial
"Saúde" e "prevenção" jamais implicam que existe proteção absoluta. Protetor craniano não garante prevenção de concussões. Nunca prescrever contato na cabeça para crianças em infográfico educativo. Diferenciar prática recreativa sem contato da competição. Qualquer claim de força, velocidade, lesão, TEA ou desenvolvimento requer fonte concreta, população e limites. Sinalizar [VERIFICAR] se falta fonte.

### Prompt operacional para assistentes
"Atue como diretor de arte editorial, treinador de Boxe, revisor científico e técnico de pré-impressão. Gere primeiro o roteiro e o wireframe, depois a ilustração sem texto e finalmente o texto como camada editável. Preserve logos originais e identidades fotográficas. Verifique fontes e regulamento atualizado. Use PT-BR com revisão ortográfica, hierarquia legível e rodapé de fontes. Liste problemas detectados e não publique sem checagem. Para tática, escreva opções condicionais, sem absolutos. Entregue 4:5 e A4 quando necessário."
