import type {CarouselPlan,SlidePlan} from "../types.js";
import {canonicalBundle,pretty} from "../lib/canon.js";
import {ClaimLedger} from "../evidence/claim-ledger.js";
import {generativeRisk,renderRoute} from "../routers/risk-router.js";
import {complexityBudget,attentionBudget} from "../routers/budget-router.js";
import {lintSlide} from "../qa/contract-linter.js";

const section=(n:number,title:string,body:string)=>`\n────────────────────────────────\n${String(n).padStart(2,"0")} — ${title}\n────────────────────────────────\n${body.trim()}\n`;

export function compileSlide(plan:CarouselPlan,s:SlidePlan):string{
  const canon=canonicalBundle(); const ledger=new ClaimLedger(plan.claims); const claims=ledger.use(s.claim_ids);
  for(const c of claims)ledger.assertVisualAllowed(c.id,s.visual_proof+" "+s.hero+" "+(s.diagram??""));
  const risk=generativeRisk(s),route=renderRoute(risk),complexity=complexityBudget(s),attention=attentionBudget(s);
  const b:string[]=[];
  b.push(`BOXE DE CRIA — BDC EDITORIAL INTELLIGENCE SYSTEM v7.1\nEVIDENCE × METAPHOR × MEMORY\nFISIOBOXE • ${s.series}\nSLIDE ${String(s.slide_index).padStart(2,"0")}/${String(s.slide_count).padStart(2,"0")}\nPROMPT INTEGRALMENTE AUTÔNOMO. NÃO DEPENDER DE OUTRO SLIDE OU PROMPT.`);
  b.push(section(1,"TASK / TARGET / OUTPUT LOCK",`TARGET: ${plan.target_model}\nONE vertical 4:5 slide. Design grid 2160×2700. Final crop/export 1080×1350. sRGB. 12-column grid. Safe top/left/right 7%, bottom 6%. Spacing ×8. Render route: ${route}.\nRENDER LOCK:\n${pretty(canon.render)}`));
  b.push(section(2,"BRAND / MODE / SÉRIE",`BRAND CANON:\n${pretty(canon.brand)}\nSERIES: ${s.series}\nMODE: ${s.mode}`));
  b.push(section(3,"EVIDENCE / CLAIM LOCK",pretty(claims)));
  b.push(section(4,"AUDIENCE / JTBD / INTENT",`AUDIENCE: ${s.audience}\nJTBD: ${s.jtbd}\nSHARE REASON: ${s.share_reason??"not specified"}\nSAVE REASON: ${s.save_reason??"not specified"}`));
  b.push(section(5,"NARRATIVE / ATTENTION / SHARE-SAVE JOB",`SLIDE JOB: ${s.slide_job}\nPRIMARY VISUAL PROOF: ${s.visual_proof}\nAttention: ${pretty(attention)}\nComplexity: ${pretty(complexity)}`));
  b.push(section(6,"EXACT TEXT / T0-T1-T2",`T0:\n${s.text_tiers.T0.join("\n")}\n\nT1:\n${s.text_tiers.T1.join("\n")}\n\nT2:\n${s.text_tiers.T2.join("\n")}\nPOLICY: verbatim; no paraphrase/translation/additional copy. If high risk, reserve clean zones for deterministic finalization.`));
  b.push(section(7,"COLOR / A11Y / SEMANTIC COLOR",`PALETTE:\n${pretty(canon.palette)}\nA11Y:\n${pretty(canon.accessibility)}`));
  b.push(section(8,"TYPOGRAPHY / LEGIBILITY",pretty(canon.typography)));
  b.push(section(9,"GRID / SAFE AREA / DENSITY / ZONES",`Use canonical 12-column grid/safe area. Chrome tertiary. One thesis, 2–4 information units. Complexity: ${complexity.level}. HIGH => simplify before generation.`));
  b.push(section(10,"FRAME / CHROME LOCK",pretty(canon.frame)));
  b.push(section(11,"BACKGROUND L0–L9",pretty(canon.background)));
  b.push(section(12,"DEPTH Z0–Z6","Z0 field\nZ1 environment/material\nZ2 grid/blueprint\nZ3 hero\nZ4 diagram/evidence\nZ5 exact copy\nZ6 frame/brand"));
  b.push(section(13,"VISUAL GRAMMAR / METAPHOR",`GRAMMAR: ${s.visual_grammar}\nPROOF CLASS: ${s.visual_proof_class}\nVISUAL PROOF: ${s.visual_proof}\nNever add a second competing grammar.`));
  b.push(section(14,"HERO / COMPOSITION / ANATOMY",`HERO: ${s.hero}\nAnatomy and sport technique plausible. No implied claim outside C-IDs.`));
  b.push(section(15,"DIAGRAM / DATA-VIZ / CLAIM TRACE",`DIAGRAM: ${s.diagram??"none"}\nDATA STATE: ${s.data_state}\nTRACE:\n${claims.map(c=>`${c.id} → visual proof → label → caveat/source`).join("\n")}`));
  b.push(section(16,"CAMERA / PERSPECTIVE",s.camera??"Editorial 3/4 or orthographic view chosen for comprehension; no fisheye distortion."));
  b.push(section(17,"LIGHTING",s.lighting??"Controlled editorial key/fill/rim; no engine bloom."));
  b.push(section(18,"MATERIALITY",s.materiality??"Matte leather/canvas/paper/rubber/metal; tactile grain; no plastic CGI."));
  b.push(section(19,"CRIAGO FULL CANON / CR-ROLE / H-LEVEL",`FULL CANON:\n${pretty(canon.criago)}\nTHIS SLIDE:\n${pretty(s.criago)}`));
  b.push(section(20,"OFFICIAL ASSETS / REFERENCE HANDLING",`ASSET REGISTRY:\n${pretty(canon.assets)}\nUse exact owner assets only. Third-party references provide functional composition/hierarchy clues only.`));
  b.push(section(21,"SOURCE / PROVENANCE / DATA STATE",`SOURCES:\n${pretty(plan.sources.filter(x=>s.source_ids.includes(x.id)))}\nPUBLIC DATA STATE: ${s.data_state}`));
  b.push(section(22,"NEGATIVE / DO-NOT-DRAW",`GLOBAL: no 3D/CGI, fake source/data/ranking, random HUD, invented logo, Criago drift, misleading arrow, unsafe overclaim.\nSLIDE: ${(s.specific_negatives??[]).join("; ")||"none"}`));
  b.push(section(23,"PRE-RENDER COMPILER",`RISK: ${pretty(risk)}\nROUTE: ${route}\nMust pass structure/version/claim/evidence/contradiction/density/thumbnail/A11Y/color-blind/2.5D/text/anatomy/data/brand checks.`));
  b.push(section(24,"POST-RENDER QA / REPAIR","Validate exact copy, anatomy, brand, data, A11Y, 2.5D, crop, logo/Criago and visual meaning. Repair only failing layer. Max 2 generative repairs, then deterministic finalization or reject."));
  b.push(section(25,"REJECTION CONDITIONS",s.rejection_conditions.map(x=>"- "+x).join("\n")));
  const prompt=b.join("");
  const issues=lintSlide(plan,s,prompt); if(issues.length)throw new Error("Slide lint failed: "+issues.join(" | "));
  return prompt;
}