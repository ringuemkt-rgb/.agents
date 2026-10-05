export interface VisualBaseline{palette:string[];chrome_budget_max:number;render_style:string;criago_required_features:string[];}
export function metadataRegression(b:VisualBaseline,c:VisualBaseline){
  const issues:string[]=[];
  if(c.chrome_budget_max>b.chrome_budget_max)issues.push("chrome budget increased");
  if(c.render_style!==b.render_style)issues.push("render style drift");
  for(const f of b.criago_required_features)if(!c.criago_required_features.includes(f))issues.push("missing Criago feature: "+f);
  return {pass:issues.length===0,issues};
}