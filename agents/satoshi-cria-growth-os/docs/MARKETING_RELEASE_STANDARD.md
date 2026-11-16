# CRIA — Release Gate para campanhas e artes (16/11/2026)

## Problema resolvido
Arte de FIT BOX foi emitida com **Prof. Satoshi Nishiuchi** apesar de haver contrato exigindo **Treinador Satoshi Nishiuchi**. Também ocorreram representações gerativas da foto real da academia e logotipo, além de CTA `garanta sua vaga` sem inventário de vagas. A regra documental isolada não impediu a execução.

Este gate adiciona validação estruturada; **não faz OCR, não garante fidelidade de pixels, não transforma imagem gerada em arquivo oficial e não publica automaticamente**. O técnico deve revisar o render final e registrar aprovação.

## Fluxo obrigatório
1. Fonte canônica da turma em `public_facts.json`; informação proposta nunca vira oferta confirmada.
2. Brand: FIT BOX (grafia oficial), CTRK, BOXE DE CRIA, CB PRISCO TEAM, FISIOBOXE, sem mistura de logos.
3. Definir canal de conversão e o proprietário do Direct/WhatsApp. Preferir CTA claro, não urgência artificial.
4. Escrever copy final em PT-BR: 1 benefício para iniciante, 1 prova verdadeira de metodologia, dias/horas confirmados, nome do treinador, ação.
5. Gerar **apenas fundo e elementos ilustrativos** quando a fidelidade for essencial. Inserir fotografia e logo originais em sobreposição sem reinterpretação.
6. Conferir aspectos gráficos no arquivo entregue, não no prompt: contraste, cortes 4:5/9:16, espaçamento, nitidez, tamanho de fonte, logotipo e assinatura.
7. Rodar o programa de checagem com JSON do briefing e anexar evidência de inspeção humana do arquivo final.
8. Só depois de aprovação do proprietário, publicar manualmente pela conta autorizada; o script nunca publica.

```bash
python agents/satoshi-cria-growth-os/src/marketing_release_qa.py --input agents/satoshi-cria-growth-os/examples/fitbox_story_campaign.json --gate draft
python -m unittest discover -s agents/satoshi-cria-growth-os/tests -p "test_marketing_release_qa.py" -v
```

## Estados
- `DRAFT_REQUIRES_VISUAL_REVIEW`: brief passou, mas depende de composição e revisão.
- `BLOCKED`: falha material de data, nome, preço, promessa, ativo ou autorização.
- `APPROVAL_RECORDED_NOT_POSTED`: briefing passou o gate publish baseado nas declarações de conferência; **não significa que o arquivo foi inspecionado pela ferramenta nem publicado**.

## Auditoria visual humana — obrigatório
- Grafia da academia, informações de agenda e **Treinador** Satoshi Nishiuchi.
- Logo e foto idênticos ao arquivo aprovado, com hash de origem; não gerar novamente rostos, símbolos nem letreiros.
- Não representar pessoa real diferente, impacto não ocorrido ou ambiente transformado como foto documental.
- Verificar texto exportado em celular, legibilidade na margem da UI e corte do story.
- Sinalizar `aula experimental`, sem prometer `grátis` se não houver confirmação.
- Não usar `garanta sua vaga` sem evidência de vaga/capacidade, nem `últimas vagas` quando há desconhecimento.

## Métricas (somente em CRM PRIVADO)
`contatos` (leads distintos consentidos), `solicitou_info`, `agendou`, `compareceu`, `matriculou`, `pagou`, `retido_30dias`. Cada fase mede pessoas/mesma coorte e intervalo. Conversão = numerador do estágio seguinte dividido por denominador elegível anterior; nenhuma view paga vira lead automaticamente.
Usuário informou três matrículas em 11/2026; confirmação financeira e origem dos anúncios ainda faltam. **Não registrar esses valores operacionais em GitHub público**.

## Atualizações da plataforma e privacidade
Meta (22/10/2026): seguidores isolados não determinam alcance; engajamento, visualizações, tempo de exibição e compartilhamentos importam; views pagas podem somar às orgânicas. https://about.fb.com/br/news/2026/10/numero-de-seguidores-nao-determina-o-alcance/
Google Business Profile: relevância, distância e destaque; dados completos e opiniões podem ajudar descoberta local. https://support.google.com/business/answer/7091?hl=en
ANPD: tratamento de dados exige finalidade, hipótese legal, transparência e necessidade, especialmente para conversas em WhatsApp; o grupo não autoriza extração indiscriminada de contatos. https://www.gov.br/anpd/pt-br/acesso-a-informacao/perguntas-frequentes

## Limites
Permissões de administrador e contas de anúncios não são compartilhadas por links públicos. Integrações Grok/Manus via GitHub são **arquitetura portável**, não prova de conexão ativa. Nunca afirmar custos, resultados, vagas, preços ou publicação sem fonte e autorização.
