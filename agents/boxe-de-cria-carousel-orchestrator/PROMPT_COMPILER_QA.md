# BDC PROMPT COMPILER & QA v1.0

## Missão

Tratar cada fence como código compilável. O prompt só sai quando passa por lint estrutural, simulação perceptiva, rastreabilidade visual e QA pós-render.

## 1. Compile order

```text
CLAIM LOCK
→ DIDACTIC JOB
→ EXACT COPY
→ VISUAL CLAIM MAP
→ GRAMMAR
→ COLOR/TYPE
→ FRAME/BACKGROUND
→ HERO/INFOGRAPHIC
→ CRIAGO/LOGO
→ NEGATIVES
→ PRE-RENDER LINT
→ THUMBNAIL SIMULATION
→ RENDER
→ POST-RENDER INSPECTION
```

## 2. Structural linter — hard fail

Todo fence deve conter os 22 blocos, na ordem.

Falhar se:
- faltar bloco;
- existir "mesmo do anterior", "como antes", "seguir slide anterior";
- faltar formato, A11Y, FRAME, BACKGROUND, DEPTH, FULL CRIAGO, LOGO, NEGATIVE, QA;
- aparecer 3D/CGI como instrução positiva;
- existir número sem source/context lock;
- existir claim acima do Claim Lock;
- existir logo reconstruída sem pedido;
- existir terceiro acento sem justificativa;
- body em fonte condensada;
- texto essencial abaixo do mínimo definido;
- data-viz usar cor como único canal.

## 3. Contradiction linter

Detectar conflitos como:
- "photoreal" + RENDER LOCK 2.5D;
- "neon glow" + NO engine bloom;
- "fundo claro" + dark-field canonical sem motivo;
- "red body" + A11Y;
- "Criago OFF" + instrução para pose visível;
- logo "recriar" + "usar external asset";
- headline longa + STOP LOCK.

Em conflito: a autoridade mais alta vence e o fence deve ser reescrito antes de sair.

## 4. Claim-to-visual traceability

Antes do render, criar internamente:

| Claim | Evidence | Visual element | Label | Caveat |
|---|---|---|---|---|

Regra:
- todo elemento visual importante deve ensinar algo;
- todo claim material deve ter representação visual ou texto explícito;
- seta não pode existir sem direção/mecanismo real;
- highlight anatômico não pode fingir medição;
- ícone não substitui dado;
- diagrama causal deve ser rotulado como mecanismo/hipótese quando não medido diretamente.

## 5. Density linter

Reprovar capa com:
- >1 tese;
- >1 parágrafo;
- >3 microchamadas;
- herói + 4 cards + gráfico simultaneamente.

Reprovar slide explicativo com:
- >4 unidades principais;
- >3 cards equivalentes;
- 2 gráficos concorrentes;
- >2 caixas de caveat.

## 6. Thumbnail simulation gate

Simular o export a ~25%:
- headline ainda legível?
- primeira leitura em 1–2 elementos?
- herói ainda reconhecível?
- palavra em acento ainda é a certa?
- source não virou ruído?
- bordas não comem texto?
- brand chrome aparece sem competir?

Não usar "2 segundos" como métrica científica; usar como meta editorial operacional.

## 7. Sunlight / low-contrast simulation

Inspecionar mentalmente como se:
- brilho do telemóvel estivesse baixo;
- ambiente externo;
- viewer com menor sensibilidade a contraste;
- captura reenviada por WhatsApp.

Se corpo sumir, reprovar.

## 8. Color-blind robustness

Toda distinção de série deve ter pelo menos 2 canais:
- cor + label;
- cor + shape;
- cor + dash;
- cor + position.

## 9. Post-render multimodal QA

Depois que a imagem existir, verificar visualmente:

TEXT
- ortografia pt-BR;
- texto literal corresponde EXACT TEXT LOCK;
- números/unidades corretos;
- nenhum texto hallucinado;
- fonte não virou ilegível.

ANATOMY
- mãos/dedos;
- braços;
- cervical;
- articulações;
- postura plausível;
- técnica coerente com modalidade.

BRAND
- logo oficial sem mutação;
- Criago = ratel adulto;
- Brasil manga direita correto;
- Bahia manga esquerda correta;
- ALELUIADO + laço sem puzzle;
- 2.5D matte, sem CGI.

DATA
- gráfico preserva valores;
- eixo/rótulo/unidade;
- sem perspectiva enganosa;
- sem barras 3D;
- source presente quando necessário.

A11Y
- contraste;
- size;
- hierarchy;
- não depender apenas de hue.

## 10. Automatic repair loop

Se P0/P1:
1. identificar falha;
2. localizar bloco responsável;
3. corrigir somente a causa;
4. recompilar;
5. reexecutar QA.

Máximo de 2 iterações automáticas antes de marcar REPROVADO e explicar o bloqueio.

## 11. Severity

P0 — factual/safety/brand/data integrity: bloqueia.
P1 — legibilidade/A11Y/anatomia/2.5D/autonomia: bloqueia.
P2 — hierarchy/density/retention: corrigir antes da entrega.
P3 — polish: pode sair com ressalva.

## 12. Fence insertion

Bloco 21 deve conter:
- STRUCTURAL LINT: PASS.
- CONTRADICTION LINT: PASS.
- CLAIM→VISUAL TRACE: PASS.
- DENSITY: PASS.
- THUMBNAIL: PASS.
- A11Y: PASS.

Bloco 22 deve exigir inspeção pós-render e REJECT ON FAIL.
