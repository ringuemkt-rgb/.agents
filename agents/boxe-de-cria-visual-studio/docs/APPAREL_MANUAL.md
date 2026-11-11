# BOXE DE CRIA — Manual mestre de vestuário v1.0

## 1. Linguagem e personalidade
**Herói + Guerreiro + Sábio**. Marca brasileira de Boxe com disciplina, respeito, pertencimento e excelência técnica. A roupa é uniforme de treino, vestuário de marca e embaixador visual — nunca somente outdoor de logotipo.

Frases institucionais selecionáveis: **De Cria pra Cria.**; **Ser forte é ser gentil.**; **O boxe não é pra parecer. É pra se tornar.** Não empilhar os três no mesmo uniforme. A camisa da turma deve ser sóbria e fácil de reconhecer no treino.

## 2. Matriz visual
- Preto: fundo predominante; acabamento fosco ou levemente texturizado, sem ruído gráfico que esconda a arte.
- Branco: legibilidade da assinatura e logotipo.
- Dourado: linhas, detalhes, status visual e assinatura; em peças comuns, evitar excesso de degradês metálicos.
- Vermelho: acento secundário, quando o modelo pedir; evitar misturar vermelho forte com muitas faixas douradas.
- **Tokens canônicos:** `../config/brand.tokens.json` — não há outra fonte de cores no módulo.
- Títulos: Oswald/Bebas Neue, corpo: Inter; sempre conferir licença, aplicação comercial e fornecedor.

## 3. Identidade gráfica obrigatória
A amostra recebida apresenta símbolo branco estilizado de animal, lettering branco "BOXE DE CRIA" e traços/coroa dourados sobre fundo preto. O animal NÃO deve ser reinterpretado, classificado como outra mascote nem reilustrado por aproximação. A versão JPG 1536×1536 é uma amostra visual, não o master de impressão. Solicitar arquivo original em vetor (SVG, EPS, AI, PDF) ou PNG com transparência e resolução apropriada, e registrar sua proveniência e SHA-256.

A marca deve manter as proporções originais. A redução excessiva da tipografia/coroa inviabiliza certos processos e precisa de amostra física. Não extrair "somente o símbolo" da logo sem uma versão oficialmente aprovada.

## 4. Coleções e padrões
### A — CRIA TRAINING (alunos)
- Base preta; logo completo no peito, centrado e com respiro.
- Faixas douradas sutis nos recortes laterais ou no ombro (elementos independentes, fora da marca).
- Costas: escolha entre `TURMA DE BOXE`, um slogan curto ou nenhuma frase. Evitar quatro linhas de ícones minúsculos.
- Manga: vazia ou pequeno símbolo **somente se existir arquivo secundário aprovado**.
- Marca da academia anfitriã é opcional e só entra se houver permissão; não declarar "oficial" sem aprovação.

### B — CRIA COACH (equipe)
- Mesmo DNA visual, distinção de hierarquia por `TREINADOR` em local discreto (manga, costas superior), sem inventar titulação.
- Elegância e legibilidade a distância; sem fazer peça de treinador parecer uniforme de atleta competitivo.

### C — CRIA PREMIUM (streetwear/coleção)
- Black-on-black, branco e detalhe dourado; poucas palavras, tecido e acabamento de qualidade verificados.
- Numerar a coleção no código de produto; nomes de modelos não podem ser apresentados como edição limitada sem política real.

### D — COMPETIÇÃO (sob encomenda)
- Verificar regulamento vigente e patrocínios. Não gerar uniforme de competição como se fosse homologado por federação.
- Checar restrições de cor, tamanho e colocação de marcas com a organização e regulamento do evento específico.

## 5. Ficha de fabricação obrigatória
- Referência / versão / data / lote / designer / aprovador.
- Produto: camiseta, regata, rashguard, short. Modelagem, sexo/grade e tabela de medidas do fornecedor.
- Malha: composição **real** do produto, gramatura (g/m²), estrutura (malha lisa/mesh), elasticidade, toque, transparência, encolhimento e amostra.
- Construção: gola, viés, mangas, barras, costura, etiqueta e posicionamento.
- Cor: referência digital + prova de tecido/estampa. Preto de camiseta e preto de estampa não são equivalentes automaticamente.
- Arte: **arquivo-mestre com fundo transparente** ou vetor, versões separadas para frente/costas, dimensões físicas em mm, orientação, distância de costuras/golas e grade de tamanhos revisadas com a confecção.
- Processo: DTF, serigrafia, sublimação total, bordado ou método definido pela fábrica; perguntar mínimos e limites da técnica.
- Custos: peça em branco, impressão, setup, etiqueta, embalagem, frete, perdas, impostos; não inventar preços.
- Prova: pré-produção física em tamanho representativo, teste de lavagem/alongamento conforme processo, comparação com logo original, aprovação escrita.

## 6. Decisão do processo têxtil
- **DTF:** transfer por filme e calor. Pode atender pequenos lotes e logos multicores, com possível textura da aplicação. Validar compatibilidade com tecido, cola, pó, cura e lavagem com a fábrica.
- **Serigrafia:** indicada para desenhos de poucas cores e séries conforme cotação; requer separação de cores e pode ter custo de matriz. Não estabelecer quantidade mínima universal.
- **Sublimação:** ideal para arte total em poliéster branco/claro, por absorção de cor; não imprime branco sobre camiseta preta pronta. Se precisar peça preta inteiramente sublimada, aprovar confecção em painéis claros impressos antes da costura. Não é equivalente a transfer branco sobre malha preta.
- **Bordado:** para detalhe pequeno com matriz própria e teste de densidade, não presumir que lettering minúsculo da logo inteira seja bordável.
- **DTG:** dependerá da malha, tinta e pré-tratamento; pedir teste antes de aprovar peças sintéticas pretas.

Referências de processo (não significam homologação da fábrica escolhida):
Brother BR — https://solucoes.brother.com.br/como-fazer-impressao-dtf-na-impressora-dtg-brother
Brother DTG — https://www.brother.com.br/garment-printers/steps-of-dtg
Brother manual DTF (parâmetros específicos por equipamento): https://base.brother.digital/download/Reversal_Guide_EMEA_V2.0.pdf
Vistaprint — https://www.vistaprint.com/hub/dye-sublimation-printing

## 7. Qualidade gráfica
- Mockup não é peça física. Uma imagem gerada não preserva automaticamente logo de forma pixel a pixel e não serve como arte da fábrica.
- Separar saída: `MOCKUP_PREVIEW` (apresentação) e `TECH_PACK` (fabricação), com estado explícito.
- Logo e textos finais devem ser aplicados em camadas editáveis com composição determinística, não redesenhados no modelo generativo.
- Arte vetorial preferencial; raster somente com pixelagem adequada na dimensão física solicitada pelo fabricante (p. ex. 300 dpi como hipótese inicial, não uma exigência universal). Perfis ICC/CMYK/Pantone são definidos com a gráfica, não assumidos.
- Tratar grade e recortes do tecido, costuras, gola e área de estampa como restrições reais. Rechecar posicionamento por tamanho.

## 8. Auditoria e veto
A reprovação é automática se houver alteração do logo, marca de terceiro sem autorização, fornecedor/tecido inventado, processual de impressão incompatível, moldes inexistentes ou alegação de arquivo pronto sem master.

Checklist de QA 100 pontos:
1. Logo e rastreabilidade: 30
2. Legibilidade e hierarquia: 15
3. Adequação do produto: 15
4. Pré-impressão, separação e posicionamento: 20
5. Tecido, prova e uso: 10
6. Contratos, direitos e documentação: 10

**Veto absoluto** prevalece sobre qualquer pontuação.

## 9. Melhoria do último conceito
O mockup de alunos estava visualmente alinhado pela paleta e pela apresentação frente/costas, mas NÃO foi homologado para produção. Ajustes para a próxima versão:
- inserir a marca apenas como arquivo original (não gerar símbolo parecido);
- simplificar as costas para `TURMA DE BOXE` + 1 assinatura institucional;
- retirar promessas de "tecido respirável / alta durabilidade" sem amostra e ficha de malha;
- não afirmar que sleeve-icon ou etiqueta sejam arte oficial;
- obter arquivo transparente/vetorial, fornecedor, modelagem e lote antes da ficha final.

## 10. Complemento visual recebido — 11/11/2026

A nova série de dez páginas introduz expressamente o **ratel** como símbolo, grafismo de luvas vermelhas suspensas, marcadores de manga e nuca e uma linha mais urbana `FIGHTWEAR`. A marca continua sujeita à fidelidade do arquivo original — não recriar símbolo a partir de screenshot.

**Status das páginas:** referência fornecida pelo usuário, não identidade homologada para impressão. A auditoria de versões e os dez hashes estão em [APPAREL_REFERENCE_AUDIT_2026-11.md](APPAREL_REFERENCE_AUDIT_2026-11.md); conjuntos de cores e rotas têxteis em [apparel.reference-manual.json](../config/apparel.reference-manual.json).

**Dois produtos alternativos, não combinações:**
- Uniforme técnico (poliéster proposto, gramatura 150–160 g/m² ilustrada, sublimação total). Confirmar se o fabricante produz painéis coloridos antes da costura e verificar prova de cor.
- Camiseta lifestyle algodão penteado 30/1 proposta, serigrafia. Confirmar composição, gramatura verdadeira, tinta, registro e lote de produção.

**Variações de logo:** ratel branco isolado, ratel dourado (render ilustrativo), assinatura vertical com Fightwear, assinatura horizontal de etiqueta e versão antiga com coroa. Escolher lockup e master oficial caso a caso; não sintetizar fusão ou trocar caracteres.

**Dimensões:** nuca ~5,5 cm, manga ~4 cm, redução em torno de 15 mm para símbolo impresso/45 px digital são valores **representados nas imagens**, não parâmetros gerais finais. Aplicar teste físico, não presumir legibilidade em bordado.

**Linguagem:** `Nascido da rua. Forjado na disciplina.` e `Feito para vencer` aparecem como propostas editoriais; não vender como slogans formalmente aprovados sem verificar. `RATEL SPORTS` e `FIGHTWEAR` também precisam de hierarquia clara de marca.

**Nota de segurança de arquivo:** os PNGs de referência estão anexados na conversa original e não foram enviados ao repositório público. O hash documenta as imagens e não demonstra disponibilidade futura nem garante que o master exista.
