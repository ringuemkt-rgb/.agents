# Asset provenance e direito de imagem

Cada asset utilizado no portal deve ter um registro privado de proveniência:
`asset_id`, `type`, `source_path/url`, `rights_status`, `licensed_by/permission_reference`, `photographer_credit` quando exigido, `usage_scope`, `subject_authorization`, `edited_by`, `original_sha256`, `derivative_sha256`, `timestamp`, `reviewer`, `ai_generated`, `ai_disclosure`.

Não publicar contratos, documentos, RG, telefones, emails pessoais de atletas, fotos privadas ou autorização de menores em repo público. Armazene o registro de consentimento no ambiente seguro; no repo ficam apenas políticas e exemplos sem dados.

Matriz:
- `licensed_photo`/ `provided_photo`: requer direito confirmado e fidelidade.
- `original_illustration`: requer autoria/revisão e dados sem invenção.
- `ai_illustration`: requer transparência contextual e não pode representar falsamente evento real.
- `official_logo`: requer arquivo mestre original + SHA-256 validado antes de compor; nunca redesenhar.
- `scientific_diagram`: requer conferência dos conceitos e referências.

Não remover marca d'água, autoria ou crédito de terceiros para contornar direitos. Referências estéticas não são autorização para copiar layout e marca de concorrente.
