import {readFileSync,mkdirSync,writeFileSync,readdirSync} from "node:fs";
import {resolve} from "node:path";
import type {CarouselPlan} from "./types.js";
import {compileCarousel} from "./compiler/compile-carousel.js";
import {validateAgainstSchema} from "./lib/validation.js";
import {canonicalBundle} from "./lib/canon.js";
function validateRepo(){
  canonicalBundle();
  const examples=readdirSync(resolve(process.cwd(),"examples")).filter(x=>x.endsWith(".plan.json"));
  for(const x of examples){const p=JSON.parse(readFileSync(resolve(process.cwd(),"examples",x),"utf8")) as CarouselPlan;validateAgainstSchema(p,"schemas/carousel-plan.schema.json");compileCarousel(p);}
  console.log(`validated canon + ${examples.length} example plan(s)`);
}
const [cmd,input,out]=process.argv.slice(2);
if(cmd==="validate")validateRepo();
else if(cmd==="compile"){if(!input||!out)throw new Error("Usage: compile <plan.json> <out-dir>");const p=JSON.parse(readFileSync(resolve(input),"utf8")) as CarouselPlan;validateAgainstSchema(p,"schemas/carousel-plan.schema.json");const a=compileCarousel(p);mkdirSync(resolve(out),{recursive:true});for(const x of a)writeFileSync(resolve(out,x.filename),x.content);console.log(`compiled ${a.length} artifacts to ${out}`);}
else console.log("Commands: validate | compile <plan.json> <out-dir>");
