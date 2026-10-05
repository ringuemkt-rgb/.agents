import type {BuildArtifact,CarouselPlan} from "../types.js";
import {compileSlide} from "./compile-slide.js";
import {compileCaptionPrompt} from "./compile-caption.js";
import {buildManifest} from "../provenance/build-manifest.js";
export function compileCarousel(plan:CarouselPlan):BuildArtifact[]{
  if(plan.slides.length!==plan.slide_count)throw new Error("slide_count does not match slides");
  const artifacts:BuildArtifact[]=plan.slides.map(s=>({filename:`${String(s.slide_index).padStart(2,"0")}-slide.md`,content:compileSlide(plan,s)}));
  if(plan.caption_required)artifacts.push({filename:"caption-prompt.md",content:compileCaptionPrompt(plan)});
  const manifest=buildManifest(plan,artifacts);
  artifacts.push({filename:"build-manifest.json",content:JSON.stringify(manifest,null,2)});
  return artifacts;
}