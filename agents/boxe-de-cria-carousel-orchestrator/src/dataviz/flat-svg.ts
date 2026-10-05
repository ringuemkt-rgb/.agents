const esc=(s:string)=>s.replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]!));
export interface BarDatum{label:string;value:number;unit:string;}
export function flatBarChart(data:BarDatum[],opts={width:900,height:520,padding:80}):string{
  if(!data.length)throw new Error("No data");
  const max=Math.max(...data.map(d=>d.value)); const row=(opts.height-opts.padding*2)/data.length; const chartW=opts.width-opts.padding*2-180;
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${opts.width}" height="${opts.height}" viewBox="0 0 ${opts.width} ${opts.height}"><rect width="100%" height="100%" fill="#020A0E"/>${data.map((d,i)=>{const y=opts.padding+i*row;const w=max?chartW*d.value/max:0;return `<text x="${opts.padding}" y="${y+22}" fill="#F3F0EA" font-family="Inter,Arial" font-size="26">${esc(d.label)}</text><rect x="${opts.padding+180}" y="${y}" width="${w}" height="28" rx="4" fill="#3EC6C9"/><text x="${opts.padding+190+w}" y="${y+22}" fill="#F3F0EA" font-family="Inter,Arial" font-size="24">${esc(String(d.value))} ${esc(d.unit)}</text>`}).join("")}</svg>`;
}