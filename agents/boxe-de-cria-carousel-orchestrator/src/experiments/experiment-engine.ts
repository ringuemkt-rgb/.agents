import {createHash} from "node:crypto";
export interface Variant{id:string;hook:string;}
export function deterministicAssignment(experimentId:string,contentId:string,variants:Variant[]):Variant{
  if(!variants.length)throw new Error("No variants");
  const h=createHash("sha256").update(experimentId+":"+contentId).digest();
  return variants[h.readUInt32BE(0)%variants.length]!;
}
export function experimentReadout(a:{reach:number;shares:number;saves:number},b:{reach:number;shares:number;saves:number}){
  const metric=(x:{reach:number;shares:number;saves:number})=>x.reach?((x.shares+x.saves)/x.reach):0;
  return {a:metric(a),b:metric(b),winner:metric(a)===metric(b)?"TIE":metric(a)>metric(b)?"A":"B",warning:"Exploratory; control for topic, time, audience and reach before causal interpretation."};
}