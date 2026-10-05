export type DataState="CONFIRMED"|"ESTIMATED"|"INDIRECT"|"DIDACTIC_MODEL"|"NOT_INVESTIGATED"|"CONFLICTING";
export type ClaimStatus=DataState|"BLOCKED";
export type Certainty="LOW"|"MODERATE"|"HIGH"|"VERY_HIGH";
export type Directness="DIRECT"|"PARTIAL"|"INDIRECT"|"NOT_APPLICABLE";
export type Risk="LOW"|"MED"|"HIGH";
export type CriagoRole="CR0"|"CR1"|"CR2"|"CR3"|"CR4";
export type Humor="H0"|"H1"|"H2"|"H3";
export type VisualProofClass="DIRECT_PHYSICAL"|"DOCUMENTARY"|"MECHANISTIC"|"COMPARATIVE"|"CONCEPTUAL"|"DATA";
export interface SourceRef{ id:string; citation:string; url?:string; doi?:string; retrieved_at?:string; freshness?:string; }
export interface Claim{ id:string; text:string; status:ClaimStatus; certainty:Certainty; directness:Directness; population?:string|null; caveat?:string|null; source_ids:string[]; allowed_visuals?:string[]; blocked_visuals?:string[]; freshness?:string|null; }
export interface TextTiers{ T0:string[]; T1:string[]; T2:string[]; }
export interface RiskProfile{ text:Risk; anatomy:Risk; data:Risk; brand:Risk; }
export interface CriagoSpec{ role:CriagoRole; humor:Humor; visibility:"ON"|"OFF"; exact_line?:string; }
export interface SlidePlan{
  slide_index:number; slide_count:number; slide_job:string; claim_ids:string[]; visual_grammar:string;
  visual_proof_class:VisualProofClass; visual_proof:string; data_state:DataState; text_tiers:TextTiers;
  audience:string; jtbd:string; share_reason?:string; save_reason?:string; hero:string; diagram?:string;
  camera?:string; lighting?:string; materiality?:string; series:string; mode:string; criago:CriagoSpec;
  source_ids:string[]; rejection_conditions:string[]; specific_negatives?:string[];
}
export interface CarouselPlan{
  topic:string; mode:string; slide_count:number; forensic_tier:"T0"|"T1"|"T2"|"T3"; target_model:string;
  claims:Claim[]; sources:SourceRef[]; slides:SlidePlan[]; caption_required:true;
}
export interface BuildArtifact{ filename:string; content:string; }