import type {CarouselPlan,SlidePlan} from "../types.js";
import {ClaimLedger} from "../evidence/claim-ledger.js";
const banned=/same as previous|mesmo (?:do|que o) slide anterior|22 blocks|22 blocos|v5\.1|Z0.?Z5/i;
const ranking=/\b(melhor|maior|lidera|ganha|pesa mais|top 1|número 1)\b/i;
export function lintSlide(plan:CarouselPlan,s:SlidePlan,prompt?:string):string[]{
  const issues:string[]=[]; const ledger=new ClaimLedger(plan.claims);
  for(const id of s.claim_ids){const c=ledger.get(id);if(c.status==="BLOCKED")issues.push("blocked claim "+id);ledger.assertVisualAllowed(id,s.visual_proof+" "+s.hero+" "+(s.diagram??""));}
  const txt=[...s.text_tiers.T0,...s.text_tiers.T1,...s.text_tiers.T2].join(" ");
  if(s.data_state==="NOT_INVESTIGATED"&&ranking.test(txt))issues.push("ranking language with NOT_INVESTIGATED data");
  if(prompt&&banned.test(prompt))issues.push("legacy/cross-slide dependency found");
  if(s.slide_index<1||s.slide_index>s.slide_count)issues.push("invalid slide index");
  if(s.source_ids.some(id=>!plan.sources.some(x=>x.id===id)))issues.push("unknown source id");
  return issues;
}