import type {CarouselPlan} from "../types.js";
import {canonicalBundle,pretty} from "../lib/canon.js";
export function compileCaptionPrompt(p:CarouselPlan):string{
  const c=canonicalBundle();
  const used=[...new Set(p.slides.flatMap(s=>s.claim_ids))];
  const claims=p.claims.filter(x=>used.includes(x.id));
  const sourceIds=new Set(p.slides.flatMap(s=>s.source_ids));
  const sources=p.sources.filter(x=>sourceIds.has(x.id));
  return [
    "# PROMPT COMPLETO DA DESCRIÇÃO / LEGENDA — COPIAR E COLAR",
    "Escreva SOMENTE a legenda final pronta para publicação em PT-BR.",
    "TEMA: "+p.topic,
    "OBJETIVO: clareza, utilidade, compartilhamento e salvamento legítimos; não prometa viralização.",
    "CLAIMS AUTORIZADOS:\n"+pretty(claims),
    "FONTES:\n"+pretty(sources),
    "CONTRATO DE LEGENDA:\n"+pretty(c.caption),
    "Obrigatório: preservar caveats e estados de evidência; SEO natural; CTA útil; sem engagement bait."
  ].join("\n\n");
}