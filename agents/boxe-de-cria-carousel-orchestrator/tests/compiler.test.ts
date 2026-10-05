import {describe,it,expect} from "vitest";
import {readFileSync} from "node:fs";
import {resolve} from "node:path";
import type {CarouselPlan} from "../src/types.js";
import {compileCarousel} from "../src/compiler/compile-carousel.js";
const plan=JSON.parse(readFileSync(resolve(process.cwd(),"examples/biomechanics-jab.plan.json"),"utf8")) as CarouselPlan;
describe("compiler",()=>{it("compiles autonomous 25-block prompts and caption",()=>{const a=compileCarousel(plan);const slide=a.find(x=>x.filename==="01-slide.md")!.content;for(let i=1;i<=25;i++)expect(slide).toContain(String(i).padStart(2,"0")+" —");expect(slide).not.toMatch(/same as previous|mesmo do slide anterior/i);expect(slide).toContain("Mellivora capensis");expect(a.some(x=>x.filename==="caption-prompt.md")).toBe(true);expect(a.some(x=>x.filename==="build-manifest.json")).toBe(true);});});