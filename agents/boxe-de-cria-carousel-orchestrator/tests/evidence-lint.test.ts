import {describe,it,expect} from "vitest";
import type {CarouselPlan} from "../src/types.js";
import {lintSlide} from "../src/qa/contract-linter.js";
const plan:CarouselPlan={topic:"x",mode:"CAROUSEL_PRODUCTION",slide_count:1,forensic_tier:"T1",target_model:"Gemini",caption_required:true,claims:[{id:"C1",text:"not investigated",status:"NOT_INVESTIGATED",certainty:"LOW",directness:"NOT_APPLICABLE",source_ids:[]}],sources:[],slides:[]};
const s:any={slide_index:1,slide_count:1,slide_job:"x",claim_ids:["C1"],visual_grammar:"SPLIT",visual_proof_class:"CONCEPTUAL",visual_proof:"comparison",data_state:"NOT_INVESTIGATED",text_tiers:{T0:["BAHIA GANHA EM VOLUME"],T1:[],T2:[]},audience:"x",jtbd:"x",hero:"x",series:"x",mode:"x",criago:{role:"CR0",humor:"H0",visibility:"OFF"},source_ids:[],rejection_conditions:[]};
describe("linter",()=>it("blocks ranking language with non-investigated data",()=>expect(lintSlide(plan,s).join(" ")).toMatch(/ranking/i)));