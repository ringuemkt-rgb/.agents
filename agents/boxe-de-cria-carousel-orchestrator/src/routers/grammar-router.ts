export function recommendGrammar(input:{job:string;proof:string;quantitative?:boolean;history?:boolean;forces?:boolean;comparison?:boolean;sequence?:boolean;}):string{
  if(input.quantitative) return "FLAT_CHART";
  if(input.forces) return "FREE_BODY";
  if(input.history) return "DOCUMENT_CARD";
  if(input.comparison) return "EVIDENCE_SPLIT";
  if(input.sequence) return "PATH";
  if(/cover|stop|hook/i.test(input.job)) return "CINE_COVER";
  if(/system|factors|synthesis|sistema|síntese/i.test(input.job)) return "HUB";
  return "CLIPBOARD";
}