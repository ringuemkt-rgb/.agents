import {readFileSync} from "node:fs";
import {dirname,resolve} from "node:path";
import {fileURLToPath} from "node:url";
const here=dirname(fileURLToPath(import.meta.url));
export const projectRoot=resolve(here,"..","..");
export function loadJson<T>(relative:string):T{
  return JSON.parse(readFileSync(resolve(projectRoot,relative),"utf8")) as T;
}
export function canonicalBundle(){
  return {
    brand:loadJson<any>("canon/brand.tokens.json"),palette:loadJson<any>("canon/palette.tokens.json"),
    typography:loadJson<any>("canon/typography.tokens.json"),accessibility:loadJson<any>("canon/accessibility.lock.json"),
    frame:loadJson<any>("canon/frame.lock.json"),background:loadJson<any>("canon/background.lock.json"),
    render:loadJson<any>("canon/render.lock.json"),criago:loadJson<any>("canon/criago.lock.json"),
    evidenceStates:loadJson<any>("canon/evidence.states.json"),caption:loadJson<any>("canon/caption.lock.json"),
    grammar:loadJson<any>("canon/grammar.registry.json"),freshness:loadJson<any>("canon/freshness.policy.json"),
    assets:loadJson<any>("canon/assets.registry.json")
  };
}
export const pretty=(v:unknown)=>JSON.stringify(v,null,2);