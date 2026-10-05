export interface ReferenceDNA{
  layout_type:string;hierarchy:string[];color_functions:string[];negative_space:string;
  hero_ratio:number;text_density:"LOW"|"MED"|"HIGH";reading_path:string[];
  cta_type?:string;background_function:string;visual_proof?:string;keep_functions:string[];do_not_copy:string[];
}
export function referenceForensics(dna:ReferenceDNA){
  return {
    functional_blueprint:{layout:dna.layout_type,hierarchy:dna.hierarchy,reading_path:dna.reading_path,visual_proof:dna.visual_proof,background_function:dna.background_function},
    originality_guard:dna.do_not_copy,
    transferable:dna.keep_functions
  };
}