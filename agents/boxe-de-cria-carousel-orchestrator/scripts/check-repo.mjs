import {readFileSync,existsSync} from "node:fs";
const required=["SKILL.md","ACTIVATE.md","PROMPT_PROTOCOL_FIXED.md","PROMPT_TEMPLATE.md","canon/brand.tokens.json","canon/criago.lock.json","schemas/slide-compile.schema.json","src/compiler/compile-slide.ts","CAPTION_COMPILER.md"];
for(const p of required)if(!existsSync(p))throw new Error("Missing "+p);
const active=["SKILL.md","ACTIVATE.md","PROMPT_PROTOCOL_FIXED.md","PROMPT_TEMPLATE.md","AGENT.md","SYSTEM_PROMPT.md","MODULE_STATUS.md","README.md"];
const banned=[/v5\.1/i,/22 blocks/i,/22 blocos/i,/Z0.?Z5/i];
for(const p of active){const c=readFileSync(p,"utf8");for(const r of banned)if(r.test(c))throw new Error(`Legacy token ${r} in ${p}`);}
console.log("repository contract checks passed");