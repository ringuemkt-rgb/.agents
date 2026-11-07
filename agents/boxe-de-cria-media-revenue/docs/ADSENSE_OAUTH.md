# AdSense somente leitura — configuração
1. Aprovar site no Google e conectar a conta do titular.
2. Habilitar AdSense Management API v2 em projeto Google Cloud.
3. Criar credenciais OAuth e realizar fluxo de consentimento por app apropriado, somente `adsense.readonly`.
4. Disponibilizar **token de acesso temporário** como `ADSENSE_ACCESS_TOKEN` no ambiente local/secret manager, nunca no GitHub.
5. Executar `python runtime/adsense_report.py --account accounts/<ID> --date-range LAST_7_DAYS --output var/adsense.json`.
6. Conferir moeda, fuso horário e diferença entre receita estimada e pagamento final. Nunca inventar valores quando token ausente.
A rotina não gera, renova, exibe nem armazena credenciais de OAuth; a obtenção da autorização deve ser implementada separadamente por sistema confiável. Ela é uma consulta **read-only** e não gerencia anúncios.
Referência: https://developers.google.com/adsense/management/reference/rest/v2/accounts.reports/generate
