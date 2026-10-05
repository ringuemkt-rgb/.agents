import type {Claim,SourceRef} from "../types.js";
import {domainRouter,requiredEvidence} from "../routers/domain-router.js";
import {freshnessClass} from "../routers/freshness-router.js";

export interface AiProvider{ complete(input:{system:string;user:string}):Promise<string>; }
export interface CouncilTask{ id:string; role:string; mission:string; output:string[]; }
export interface ForensicCase{ topic:string; riskTier:"T0"|"T1"|"T2"|"T3"; dateCut:string; audience?:string; }

export function buildCouncil(c:ForensicCase):CouncilTask[]{
  const domain=domainRouter(c.topic); const req=requiredEvidence(domain);
  const tasks:CouncilTask[]=[
    {id:"scout",role:"SOURCE SCOUT",mission:"Map primary and high-authority sources; do not synthesize yet.",output:["source map","freshness"]},
    {id:"identity",role:"STUDY/RECORD IDENTITY AUDITOR",mission:"Resolve duplicate cohorts, documents, editions and study families.",output:["family ledger","overlap warnings"]},
    {id:"method",role:"METHODS AUDITOR",mission:"Extract design, population, measurement, denominator, bias and what was not measured.",output:req},
    {id:"contradiction",role:"CONTRADICTION HUNTER",mission:"Search rival explanations, nulls, counterexamples and evidence that could falsify the leading claim.",output:["rival hypotheses","contradictions","gaps"]},
    {id:"mechanism",role:"MECHANISM BRIDGE AUDITOR",mission:"Separate observed outcome, mechanism, didactic model and editorial inference.",output:["mechanism map","directness"]},
    {id:"visual",role:"VISUAL EVIDENCE AUDITOR",mission:"Find visual proofs that do not imply more than the evidence permits.",output:["visual proof classes","blocked visuals"]},
    {id:"editor",role:"EDITORIAL TRANSLATOR",mission:"Translate only approved claims into audience language without changing certainty.",output:["hook candidates","plain-language model","caveats"]},
    {id:"governor",role:"EVIDENCE GOVERNOR",mission:"Adjudicate conflicts and produce Best Current Explanation + Claim Ledger.",output:["BCE","claim ledger","final gate"]}
  ];
  if(c.riskTier==="T3")tasks.splice(5,0,{id:"safety",role:"SAFETY REVIEWER",mission:"Review harms, vulnerable populations, clinical boundaries and misinterpretation risk.",output:["harm ledger","safety wording","blocked advice"]});
  return tasks;
}

export function forensicSystemPrompt(c:ForensicCase):string{
  return [
    "You are BDC FORENSIC AI COUNCIL.",
    `Topic: ${c.topic}`,`Risk tier: ${c.riskTier}`,`Date cut: ${c.dateCut}`,
    `Domain: ${domainRouter(c.topic)}`,`Freshness: ${freshnessClass(c.topic)}`,
    "Evidence > eloquence. Rival hypothesis before conclusion. NOT FOUND ≠ DID NOT HAPPEN.",
    "Never invent citations, effect sizes, N, denominators, dates, rankings or causal links.",
    "Distinguish OBSERVED_DATA / DERIVED_DATA / MECHANISTIC_MODEL / DIDACTIC_MODEL / ARTISTIC_METAPHOR."
  ].join("\n");
}

export async function runCouncil(provider:AiProvider,c:ForensicCase):Promise<{reports:Record<string,string>;synthesis:string}>{
  const tasks=buildCouncil(c); const reports:Record<string,string>={};
  for(const task of tasks.filter(t=>t.id!=="governor")){
    reports[task.id]=await provider.complete({system:forensicSystemPrompt(c),user:`ROLE: ${task.role}\nMISSION: ${task.mission}\nOUTPUT: ${task.output.join(", ")}`});
  }
  const synthesis=await provider.complete({
    system:forensicSystemPrompt(c),
    user:"ROLE: EVIDENCE GOVERNOR\nSynthesize reports. Resolve contradictions and return Best Current Explanation, Claim Ledger candidates, gaps, blocked claims, visual-proof map and final gate.\n"+JSON.stringify(reports)
  });
  return {reports,synthesis};
}
export interface ForensicSynthesis{best_current_explanation:string;claims:Claim[];sources:SourceRef[];gaps:string[];blocked_claims:string[];}
