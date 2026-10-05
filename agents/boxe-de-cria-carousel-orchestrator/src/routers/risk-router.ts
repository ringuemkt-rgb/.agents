import type {RiskProfile,SlidePlan,Risk} from "../types.js";
const risk=(n:number):Risk=>n>=3?"HIGH":n>=1?"MED":"LOW";
export function generativeRisk(s:SlidePlan):RiskProfile{
  let t=0,a=0,d=0,b=0;
  const exact=[...s.text_tiers.T0,...s.text_tiers.T1,...s.text_tiers.T2].join(" ");
  if(exact.length>550)t+=2; else if(exact.length>250)t++;
  if(s.text_tiers.T2.length>2)t++;
  if(/[±%]|DOI|PMID|N·|m\/s|\bN\b/.test(exact)) d+=2;
  if(/chart|graph|axis|bar|error/i.test(s.diagram??"")) d+=2;
  if(/grappl|clinch|throw|takedown|entang|two fighters|dois atletas/i.test(s.hero)) a+=2;
  if(/hand|punch|grip|foot|joint|mão|punho|pé|articula/i.test(s.hero)) a++;
  if(s.criago.visibility==="ON") b++;
  if(/logo|flag|patch|bandeira/i.test(exact+" "+s.hero)) b+=2;
  return {text:risk(t),anatomy:risk(a),data:risk(d),brand:risk(b)};
}
export function renderRoute(r:RiskProfile):"G1_IN_MODEL"|"G2_FINALIZATION_SAFE"{
  return Object.values(r).includes("HIGH")?"G2_FINALIZATION_SAFE":"G1_IN_MODEL";
}