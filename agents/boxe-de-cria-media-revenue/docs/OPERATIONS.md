# Operação e governança
**Funções automáticas permitidas:** ingestão de metadados de RSS/Atom autorizados, deduplicação, triagem, briefing, cálculos de receita e relatórios. **Revisão humana obrigatória:** notícias, acusações, resultados esportivos, fotos, dados sensíveis/menores, alterações de produção, pagamentos e publicidade. Nunca confundir RSS com comprovação.

A base de cartel exige luta, evento, data, adversário, disciplina, classe, resultado, evidência URL e revisor. Somar apenas lutas verificadas. Ausência de lutas cadastradas não significa cartel de 0-0.

SQLite do runtime é fila de pesquisa e demonstração, não banco do site. Lovable tem seu banco e regras RLS próprias que exigem auditoria antes de integração. Login e upload público devem ser implementados separadamente; não supor que existem.

**Segurança:** fontes configuradas manualmente, HTTPS, sem redirecionamentos, limites de tamanho, XML sem DTD, tokens fora do Git. O controle de rede deve impedir DNS rebinding/SSRF em ambientes com acesso interno; não confie somente na verificação do host. Textos externos não executam ferramentas.

**Implantação:** testes unitários → fontes autorizadas → operações humanas → CMS protegido → AdSense só com aprovação do Google → métricas reais → otimizações de SEO e campanhas. Relatar erro/limitação antes de anunciar sucesso.