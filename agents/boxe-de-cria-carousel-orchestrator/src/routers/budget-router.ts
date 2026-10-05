import type {SlidePlan} from "../types.js";
export interface BudgetResult{score:number;level:"LOW"|"MED"|"HIGH";reasons:string[];}
export function complexityBudget(s:SlidePlan):BudgetResult{
  const text=s.text_tiers.T0.join(" ").length+s.text_tiers.T1.join(" ").length+s.text_tiers.T2.join(" ").length;
  let score=Math.ceil(text/120); const reasons:string[]=[];
  if(text>700){score+=3;reasons.push("long exact copy");}
  if((s.diagram??"").length>120){score+=2;reasons.push("complex diagram");}
  if(/grappl|clinch|entang|throw|takedown/i.test(s.hero)){score+=2;reasons.push("interaction anatomy");}
  if(s.data_state==="CONFIRMED" && /chart|graph|data|%|doi|pmid|N·|m\/s/i.test((s.diagram??"")+" "+s.text_tiers.T2.join(" "))){score+=2;reasons.push("exact data");}
  if(s.criago.visibility==="ON") score+=1;
  return {score,level:score>=9?"HIGH":score>=5?"MED":"LOW",reasons};
}
export function attentionBudget(s:SlidePlan){
  const components={headline:30,hero:35,diagram:s.diagram?18:0,criago:s.criago.visibility==="ON"?7:0,chrome:5,footer:s.text_tiers.T2.length?5:2};
  const total=Object.values(components).reduce((a,b)=>a+b,0);
  return {components,total,overflow:total>100};
}