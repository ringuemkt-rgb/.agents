---
name: boxe-de-cria-apparel-design
description: Identidade, modelagem visual, mockup, briefing técnico e auditoria para camisas, uniformes de alunos, regatas, rashguards e coleções BOXE DE CRIA. Preserve o logo original e só libere para produção após validações.
version: 1.1.0
---

# BOXE DE CRIA — Apparel Design Master Skill

## Acionamento
Ative quando a solicitação mencionar: camisa, camiseta, uniforme, turma de boxe, rashguard, regata, short, vestuário, estampa, silk, sublimação, DTF, bordado, etiqueta, grade de tamanhos, facção, coleção ou mockup ligados à marca BOXE DE CRIA.

## Fontes únicas
1. Marca: `../../config/brand.tokens.json` e `../../BRAND_GUIDELINES.md` (não duplicar nem mudar cores/valores sem aprovação).
2. Especialização têxtil: `../../docs/APPAREL_MANUAL.md`.
3. Brief para fábrica: `../../templates/PRODUCTION_BRIEF.md`.
4. Dados estruturados: `../../examples/student_training_tee.json`.
5. Verificador: `../../runtime/apparel_qa.py`.

## Obrigatório em cada pedido
1. Identificar linha: Alunos / Treinador / Premium / Equipe de competição / Edição especial.
2. Confirmar público, finalidade, cortes masculino/feminino/unissex, grade e orçamento quando necessários.
3. Conferir arte-mestre da logo, licença/autorização, procedência e hash SHA-256. A foto/arte enviada pelo usuário é referência, não aprovação automática para redesenho.
4. Escolher frente e costas com uma tese por superfície. Integrar cor/shape do uniforme ao texto, não cobrir logo com efeitos.
5. Produzir mockup como representação estética. **Arquivo para estamparia é outro entregável**.
6. Preparar ficha técnica: tecido, gramatura, modelagem, costura, acabamento, cor da malha, método de estampa, dimensões físicas, posicionamento, tamanho do lote, provas de cor e teste de lavagem.
7. Executar QA de marca, legibilidade em tecido, proveniência, ortografia, tamanho, marcação de versão e impressão.
8. Bloquear qualquer alegação de "pronto para produzir" sem arquivo-mestre aprovado, fornecedor, especificações e prova física.

## Regras inegociáveis
- **Logo oficial imutável**: nunca aproximar, vetorizar criativamente, trocar forma de símbolo, alterar lettering/coroa, reescrever palavras ou inserir sombra/glow dentro dos pixels da marca.
- A versão enviada como JPG 1536×1536 com fundo preto é referência visual, não um master automaticamente transparente ou arquivo final de impressão.
- Cores canônicas no arquivo de tokens, com prova física para material/fornecedor. Dourado impresso não equivale a tinta metalizada.
- Fotos reais, rostos, proporções e tatuagens são preservados, sem recriação generativa quando o usuário exige fidelidade.
- Não introduzir marca FIT BOX, CTRK, CB Prisco ou qualquer parceira sem consentimento e arquivo original autorizado.
- Não inventar tecido "respirável", "antibacteriano", "antiodor", "secagem rápida", "alta durabilidade" sem especificação do fornecedor.
- Arte para crianças exige cuidado com consentimento, fotos, nomes e dados pessoais.
- Marcas, fotos e fichas comerciais privadas NÃO entram no repositório GitHub público.

## Três linhas
- **TURMA / TRAINING:** preto predominante, original frontal legível, detalhes dourados discretos; verso com identidade de aluno e lema curto.
- **COACH / STAFF:** visual distinto e sóbrio, identificação "TREINADOR" somente para quem ocupa a função.
- **CRIA PREMIUM:** composição minimalista, recortes e acabamentos refinados; sem perder identidade.

## Saída padrão
Brief + arte conceitual (somente se pedida) + vistas frente/costas + ficha técnica preliminar + relatório de fontes e direitos + QA + pendências de fábrica.

## Compatibilidade
Instruções Markdown portáveis para ChatGPT, Grok e Manus. Isso não conecta APIs nem instala motores gráficos. Para conteúdo de marketing use o Growth OS; para editorial use o Visual Studio. Não atribua sucesso de fabricação a mockups sintéticos.

## Extensão — manual visual fornecido (11/11/2026)
- Ler [a perícia das dez referências](../../docs/APPAREL_REFERENCE_AUDIT_2026-11.md) e o [manifesto das variantes](../../config/apparel.reference-manual.json) antes de desenhar qualquer camisa. Essas imagens são referência, não original vetorial de produção.
- Símbolo identificado nas referências: **ratel**. Preservar olho, focinho, curva e recortes sem trocar a espécie, fazer reinterpretção por IA ou distorcer geometria.
- Duas paletas candidatas conflitantes: NÃO substituir os tokens canônicos até aprovação explícita da nova versão. Nunca misturar vermelho de uma versão com tons de outra por acaso.
- Distinguir assinatura `BOXE DE CRIA`, assinatura `FIGHTWEAR`, ratel isolado, selo da nuca e manga. Requer arquivo original aprovado para cada uso.
- Manter **duas rotas de fabricação independentes**: poliéster dry-fit + sublimação total, versus algodão + serigrafia, com fichas e orçamentos separados.
- As dimensões e gramaturas apresentadas nas imagens são **hipóteses do manual visual**, não especificações comprovadas de fábrica. Revalidar com confecção, tamanho e prova física.
- Páginas do manual apresentam distorções de microtexto, instruções inconsistentes e logos de conceito; refazer todo texto como tipografia editável e usar somente arte original.
