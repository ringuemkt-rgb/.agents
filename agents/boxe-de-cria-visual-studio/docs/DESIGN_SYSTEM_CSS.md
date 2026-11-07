# Como aplicar o CSS de referência

`config/design-system.css` é uma **folha de estilo de referência**, não um patch aplicado ao Lovable.

As classes são deliberadamente escopadas em `.bdc-theme` para evitar conflito com os componentes atuais. O técnico que editar o projeto Lovable deve comparar tokens existentes, importar o CSS somente após teste visual, avaliar o dark mode e garantir que o render das imagens não cause CLS.

Atributos `width`, `height`, `loading`, `decoding`, `srcset` e `sizes` devem ser definidos no HTML/React conforme o contexto. Não há arquivos de fonte ou foto incluídos aqui. A qualidade dos tokens não valida automaticamente contraste de uma imagem sob texto: verificação visual continua obrigatória.
