import {createHash} from "node:crypto";
import type {CarouselPlan} from "../types.js";
export function buildManifest(plan:CarouselPlan,promptFiles:{filename:string;content:string}[]){
  const payload=JSON.stringify({topic:plan.topic,claims:plan.claims.map(c=>c.id),sources:plan.sources.map(s=>s.id),prompts:promptFiles.map(x=>x.content)});
  const hash=createHash("sha256").update(payload).digest("hex");
  return {
    build_id:`BDC-${new Date().toISOString().slice(0,10)}-${hash.slice(0,10)}`,
    generated_at:new Date().toISOString(),topic:plan.topic,
    claims:plan.claims.map(c=>c.id),sources:plan.sources.map(s=>s.id),
    compiler_version:"7.1.0-runtime.1",content_hash:hash
  };
}