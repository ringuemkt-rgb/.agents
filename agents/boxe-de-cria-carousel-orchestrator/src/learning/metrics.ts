export interface Performance{content_id:string;reach:number;non_follower_reach?:number;saves?:number;shares?:number;comments?:number;profile_visits?:number;follows?:number;carousel_completion_rate?:number|null;}
const rate=(n=0,d=0)=>d>0?n/d:null;
export function normalizePerformance(p:Performance){
  return {
    content_id:p.content_id,
    save_rate:rate(p.saves,p.reach),share_rate:rate(p.shares,p.reach),comment_rate:rate(p.comments,p.reach),
    profile_visit_rate:rate(p.profile_visits,p.reach),follow_rate:rate(p.follows,p.reach),
    non_follower_ratio:rate(p.non_follower_reach,p.reach),completion_rate:p.carousel_completion_rate??null,
    warning:"Descriptive metrics only; one post does not establish causality."
  };
}