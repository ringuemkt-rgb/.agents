export type FreshnessClass="STATIC"|"MONTHS_12"|"DAYS_90"|"DAYS_30"|"DAYS_7"|"LIVE";
export function freshnessClass(topic:string):FreshnessClass{
  const t=topic.toLowerCase();
  if(/breaking|hoje|agora|placar|ao vivo|availability/.test(t)) return "LIVE";
  if(/notícia|news|evento|resultado/.test(t)) return "DAYS_7";
  if(/ranking|temporada|modelo de ia|gemini|instagram|plataforma/.test(t)) return "DAYS_30";
  if(/regra|federação|guideline|diretriz|policy/.test(t)) return "DAYS_90";
  if(/revisão sistemática|meta-análise/.test(t)) return "MONTHS_12";
  return "STATIC";
}