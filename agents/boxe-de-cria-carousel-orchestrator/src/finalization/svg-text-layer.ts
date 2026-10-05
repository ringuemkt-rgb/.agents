const e=(s:string)=>s.replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]!));
export interface TextBlock{x:number;y:number;text:string;size:number;weight?:number;fill?:string;}
export function textLayer(blocks:TextBlock[],width=1080,height=1350):string{
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" viewBox="0 0 ${width} ${height}">${blocks.map(b=>`<text x="${b.x}" y="${b.y}" fill="${b.fill??"#F3F0EA"}" font-family="Inter,Arial,sans-serif" font-size="${b.size}" font-weight="${b.weight??700}">${e(b.text)}</text>`).join("")}</svg>`;
}