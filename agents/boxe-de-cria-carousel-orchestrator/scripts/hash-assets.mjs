import {createHash} from "node:crypto";
import {readFileSync,writeFileSync,existsSync} from "node:fs";
import {resolve} from "node:path";

const registryPath=resolve("canon/assets.registry.json");
const registry=JSON.parse(readFileSync(registryPath,"utf8"));
let changed=false;
for(const asset of registry.assets){
  if(!asset.file) continue;
  const p=resolve(asset.file);
  if(!existsSync(p)){ console.warn("missing asset:",asset.id,p); continue; }
  asset.sha256=createHash("sha256").update(readFileSync(p)).digest("hex");
  asset.status="APPROVED_HASHED";
  changed=true;
}
if(changed){
  writeFileSync(registryPath,JSON.stringify(registry,null,2)+"\n");
  console.log("asset hashes updated");
}else{
  console.log("no registered asset files to hash");
}
