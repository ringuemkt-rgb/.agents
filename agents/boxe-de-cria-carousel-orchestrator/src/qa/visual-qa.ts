export interface VisualObservation{
  aspect_4_5:boolean;safe_area:boolean;headline_readable:boolean;exact_text:boolean;anatomy_ok:boolean;
  criago_ok:boolean;logo_ok:boolean;flags_ok:boolean;data_ok:boolean;render_2_5d:boolean;
  no_random_hud:boolean;contrast_ok:boolean;claim_visual_ok:boolean;
}
export function visualGate(o:VisualObservation){
  const critical=(Object.entries(o) as [keyof VisualObservation,boolean][]).filter(([,v])=>!v).map(([k])=>k);
  return {status:critical.length?"REPROVADO":"APROVADO",critical};
}
export const visualInspectionPrompt="Inspect a rendered BDC carousel slide. Return structured booleans for aspect_4_5, safe_area, headline_readable, exact_text, anatomy_ok, criago_ok, logo_ok, flags_ok, data_ok, render_2_5d, no_random_hud, contrast_ok, claim_visual_ok. Do not infer unreadable microtext; mark false/uncertain instead.";