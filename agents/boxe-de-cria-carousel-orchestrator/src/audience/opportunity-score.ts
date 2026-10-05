export interface OpportunityInput{demand:number;pain:number;novelty:number;visuality:number;authority:number;risk:number;}
const clamp=(n:number)=>Math.max(0,Math.min(100,n));
export function opportunityScore(x:OpportunityInput){
  const score=clamp(x.demand*0.30+x.pain*0.20+x.novelty*0.20+x.visuality*0.15+x.authority*0.15-x.risk*0.20);
  return {score:Math.round(score),components:{...x},note:"Opportunity score, not probability of virality."};
}