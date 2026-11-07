# Segurança
- Chaves: apenas variáveis de ambiente em secret manager; nunca em `sources.json`, Git ou mensagens.
- Metadados externos: não confiáveis. Não executar instruções de RSS ou texto vindo de fonte.
- Coleta: feeds preaprovados, HTTPS, XML sem DTD, tamanho limitado, sem redirects; em produção usar isolamento de rede/egress para bloquear DNS rebinding e SSRF.
- Backend do site: Supabase RLS e policies específicas para equipe; jamais incluir service role no navegador.
- Dados de crianças/adolescentes: minimização e revisão reforçada antes de publicação, respeitar legislação aplicável.
- Tráfego inválido: nunca clicar nos próprios anúncios, empregar bot de visualizações ou induzir cliques.
- Arte/fotos: usar licenças ou autorização; verificar termos antes de usar dados de outras plataformas.
- Publicação: o runtime gera JSON de staging; integração com CMS requer autenticação e aprovação de editor.
- Revisão: arquivo de audit local é operacional, não trilha de certificação legal; integridade forte exige log imutável e backups.
