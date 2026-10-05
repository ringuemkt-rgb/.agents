export type Domain="SCIENCE"|"HISTORY"|"NEWS_RULES"|"HYBRID";
export function domainRouter(topic:string):Domain{
  const t=topic.toLowerCase();
  const science=/biomec|fisiolog|lesão|concuss|performance|psicolog|autismo|força|pressão|rfd/.test(t);
  const history=/história|origem|primeiro registro|documento|arquivo|jofre|antigo/.test(t);
  const news=/ranking|regra|evento|hoje|2026|federação|campeonato/.test(t);
  if([science,history,news].filter(Boolean).length>1) return "HYBRID";
  if(science) return "SCIENCE";
  if(history) return "HISTORY";
  if(news) return "NEWS_RULES";
  return "HYBRID";
}
export function requiredEvidence(domain:Domain):string[]{
  if(domain==="SCIENCE") return ["study design","population","outcome","directness","risk of bias","caveat"];
  if(domain==="HISTORY") return ["primary source","date","provenance","corroboration","disputed claims","record ≠ origin caveat"];
  if(domain==="NEWS_RULES") return ["current official source","publication/update date","jurisdiction","freshness"];
  return ["source map","claim ledger","contradiction check","provenance"];
}