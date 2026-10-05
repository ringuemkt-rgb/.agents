import type {Claim,DataState} from "../types.js";
export class ClaimLedger{
  private byId=new Map<string,Claim>();
  constructor(claims:Claim[]){for(const c of claims){if(this.byId.has(c.id))throw new Error("Duplicate claim "+c.id);this.byId.set(c.id,c);}}
  get(id:string):Claim{const c=this.byId.get(id);if(!c)throw new Error("Unknown claim "+id);return c;}
  use(ids:string[]):Claim[]{return ids.map(id=>this.get(id));}
  assertVisualAllowed(id:string,visual:string):void{
    const c=this.get(id);
    if(c.status==="BLOCKED")throw new Error("Blocked claim used: "+id);
    for(const x of c.blocked_visuals??[]){if(visual.toLowerCase().includes(x.toLowerCase()))throw new Error(`Visual violates ${id}: ${x}`);}
  }
  publicState(id:string):DataState{const s=this.get(id).status;if(s==="BLOCKED")throw new Error("Blocked claim has no public state");return s;}
}