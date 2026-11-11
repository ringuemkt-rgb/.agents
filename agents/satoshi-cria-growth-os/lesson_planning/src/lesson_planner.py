#!/usr/bin/env python3
"""CRIA BOXE ACADEMY: offline, non-contact lesson plan compiler. stdlib only."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from datetime import datetime, timedelta
from html import escape

HERE=Path(__file__).resolve().parents[1]
GROWTH=HERE.parent
COACH="Treinador Satoshi Nishiuchi"
GOALS={
  "stance_jab":{"title":"Base, guarda e jab","objective":"Manter base estável, executar jab e recompor guarda sem perder equilíbrio.","cue":"Base primeiro; mão volta à guarda.","error":"Juntar os pés ou não recompor a guarda.","regress":"Jab parado e lento, com pausa.","progress":"Passo curto + jab + resposta a sinal visual.","metric":"4 de 5 tentativas com guarda recomposta e estabilidade.","drill":"Marcação no solo e jab em alvo fixo sem contato humano.","diagram":"jab"},
  "footwork":{"title":"Passos e distância","objective":"Deslocar-se em quatro direções sem cruzar os pés.","cue":"O pé que vai na direção do movimento inicia.","error":"Cruzar os pés ou saltar descontroladamente.","regress":"Passos únicos lentos.","progress":"Mudança de direção por estímulo.","metric":"4 de 5 percursos sem perder a base.","drill":"Quadrado de cones com instrução de direção.","diagram":"footwork"},
  "one_two":{"title":"Jab-direto e retorno","objective":"Executar jab-direto com base estável e recomposição da guarda.","cue":"Alternar os braços sem projetar o tronco excessivamente.","error":"Avançar sem base ou atrasar o retorno.","regress":"Jab e direto isolados.","progress":"Combinação + saída lateral sem contato.","metric":"4 de 5 sequências com controle e guarda.","drill":"Manoplas técnicas ou alvo de espuma, intensidade adaptada.","diagram":"jab"},
  "guard_defense":{"title":"Defesa e reposicionamento","objective":"Responder a sinal visual com passo defensivo e recuperação de base.","cue":"Reconhecer o sinal, responder e reposicionar.","error":"Perder equilíbrio ao reagir.","regress":"Uma opção de resposta previsível.","progress":"Alternar sinais e duas opções de resposta.","metric":"4 de 5 decisões adequadas com base preservada.","drill":"Manopla como marcador visual, sem golpe direcionado à cabeça.","diagram":"footwork"}
}
WEEKS=[
 ["stance_jab","footwork"],["footwork","stance_jab"],["stance_jab","one_two"],
 ["one_two","footwork"],["guard_defense","stance_jab"],["guard_defense","one_two"],
 ["one_two","guard_defense"],["footwork","guard_defense"],["one_two","footwork"],
 ["guard_defense","one_two"],["stance_jab","one_two"],["footwork","guard_defense"]
]
STAGES=[
 ("Acolhimento e segurança","Checar bem-estar, dor, tontura, sintomas de impacto e combinar sinal de pausa."),
 ("Aquecimento","Mobilidade dinâmica + marcha e posição de guarda sem impacto."),
 ("Demonstração","Mostrar movimento, explicar comando principal e praticar lentamente."),
 ("Prática orientada",None),
 ("Variabilidade e decisão",None),
 ("Volta à calma e avaliação","Recuperação; observar cinco repetições e registrar necessidade de correção.")
]
def facts():return json.loads((GROWTH/"public_facts.json").read_text(encoding="utf-8"))
def generate(request):
    classes=facts()["classes"]
    chosen=next((x for x in classes if x["id"]==request.get("class_id")),None)
    if chosen is None:raise ValueError("Turma não confirmada no cadastro público")
    if chosen["start_time"]!=request.get("start_time"):raise ValueError("Horário divergente da turma")
    n=int(request.get("duration_min",0))
    if n<20 or n>90:raise ValueError("Duração deve ser informada entre 20 e 90 minutos; nunca presumida")
    if request.get("contact",False):raise ValueError("Contato físico/sparring não é gerado automaticamente")
    week=int(request.get("week",1)); session=int(request.get("session",1))
    if not 1<=week<=12 or session not in (1,2):raise ValueError("Semana 1–12, sessão 1–2")
    goal=request.get("goal") or WEEKS[week-1][session-1]
    if goal not in GOALS:raise ValueError("Tema não reconhecido")
    th=GOALS[goal]
    weights=[0.10,0.15,0.20,0.25,0.20,0.10]
    mins=[round(n*w) for w in weights]; mins[-1]+=n-sum(mins)
    start=datetime.strptime(chosen["start_time"],"%H:%M")
    tasks=[]
    for i,(label,text) in enumerate(STAGES):
        end=start+timedelta(minutes=mins[i])
        content=text or (th["drill"] if i==3 else th["progress"])
        tasks.append(dict(start=start.strftime("%H:%M"),end=end.strftime("%H:%M"),
                          duration_min=mins[i],stage=label,task=content))
        start=end
    population=request.get("population","adultos iniciantes")
    return dict(title=th["title"],academy=chosen["academy"],coach=COACH,
                start=chosen["start_time"],end=start.strftime("%H:%M"),
                duration_min=n,population=population,week=week,session=session,
                equipment=request.get("equipment",["marcadores no chão","cones","alvo de espuma"]),
                objective=th["objective"],cue=th["cue"],error=th["error"],
                regression=th["regress"],progression=th["progress"],metric=th["metric"],
                diagram=th["diagram"],stages=tasks,
                safety="Treino sem contato entre pessoas; sem sparring ou golpes na cabeça. "
                       "Suspeita de concussão: interromper e não retornar no mesmo dia; encaminhar.",
                accessibility="Comandos curtos, demonstração visual, pausas e ajustes conforme necessidade relatada.",
                evidence="Drill pedagógico proposto; não é intervenção clínica validada.")
def diagram_svg(which):
    if which=="footwork":
        return ('<svg viewBox="0 0 400 125" xmlns="http://www.w3.org/2000/svg">'
         '<rect width="400" height="125" rx="10" fill="#f3f6f8"/>'
         '<g fill="#1e2932"><ellipse cx="185" cy="66" rx="13" ry="23" transform="rotate(-18 185 66)"/>'
         '<ellipse cx="215" cy="77" rx="13" ry="23" transform="rotate(18 215 77)"/></g>'
         '<g stroke="#c52431" stroke-width="4" fill="none"><path d="M200 43V13m-8 9 8-9 8 9M200 96v20m-8-9 8 9 8-9'
         'M160 66H102m8-8-8 8 8 8M240 66H297m-8-8 8 8-8 8"/></g></svg>')
    return ('<svg viewBox="0 0 400 125" xmlns="http://www.w3.org/2000/svg">'
            '<rect width="400" height="125" rx="10" fill="#f3f6f8"/>'
            '<g stroke="#283442" stroke-width="12" stroke-linecap="round" fill="none">'
            '<path d="M114 108L139 64L161 108M139 64V35M139 42L112 64M139 42L250 38"/></g>'
            '<circle cx="139" cy="23" r="13" fill="#283442"/><circle cx="250" cy="38" r="12" fill="#c52431"/>'
            '<g stroke="#c52431" stroke-width="3" fill="none"><path d="M265 38H328m-9-7 9 7-9 7"/>'
            '<path d="M236 62Q185 86 150 49" stroke-dasharray="4 5"/></g>'
            '<text x="217" y="102" font-family="Arial" font-size="12" fill="#24313d">Retorno à guarda</text></svg>')
def render_html(p):
    tr="".join("<tr><th>"+escape(x["start"]+"–"+x["end"])+"</th><td><b>"+escape(x["stage"])+"</b><br>"
       +escape(x["task"])+"</td></tr>" for x in p["stages"])
    return ('<!doctype html><html lang="pt-br"><meta charset="utf-8"><title>CRIA BOXE - Plano</title>'
      '<style>body{font:14px/1.5 Arial;max-width:820px;margin:25px auto;color:#172029}'
      'header{background:#141b23;color:white;padding:24px;border-top:7px solid #d1a83e}'
      'h1{margin:3px 0}h2{font-size:18px}table{width:100%;border-collapse:collapse}'
      'td,th{border-bottom:1px solid #dfe4e8;padding:10px;vertical-align:top}th{text-align:left;white-space:nowrap;color:#b52b32}'
      '.note{background:#fff2e3;padding:12px}.pair{background:#f3f5f6;padding:9px;margin:6px 0}'
      '@page{size:A4;margin:14mm}@media print{body{margin:0}}</style><body>'
      '<header><small>CRIA BOXE ACADEMY • PLANO AUTORAL</small><h1>'+escape(p["title"])+'</h1>'
      +escape(p["coach"]+' | '+p["academy"]+' | '+p["start"]+'–'+p["end"])+'</header>'
      '<h2>Competência observável</h2><p>'+escape(p["objective"])+'</p>'
      '<h2>Ilustração original</h2>'+diagram_svg(p["diagram"])
      +'<h2>Plano minuto a minuto</h2><table>'+tr+'</table>'
      '<h2>Correção</h2><div class="pair"><b>Cue:</b> '+escape(p["cue"])+'</div>'
      '<div class="pair"><b>Erro típico:</b> '+escape(p["error"])+'</div>'
      '<div class="pair"><b>Regressão:</b> '+escape(p["regression"])+'</div>'
      '<div class="pair"><b>Progressão:</b> '+escape(p["progression"])+'</div>'
      '<h2>Avaliação</h2><p>'+escape(p["metric"])+' (meta operacional sugerida, não validada).</p>'
      '<h2>Segurança</h2><div class="note">'+escape(p["safety"])+' '+escape(p["accessibility"])+'</div>'
      '<p><small>'+escape(p["evidence"])+'</small></p></body></html>')
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input",required=True,help="brief JSON")
    ap.add_argument("--output",required=True,help="output directory")
    a=ap.parse_args()
    req=json.loads(Path(a.input).read_text(encoding="utf-8"))
    p=generate(req)
    dest=Path(a.output);dest.mkdir(parents=True,exist_ok=True)
    (dest/"plan.json").write_text(json.dumps(p,ensure_ascii=False,indent=2),encoding="utf-8")
    (dest/"plan.html").write_text(render_html(p),encoding="utf-8")
    print(json.dumps({"ok":True,"end":p["end"],"files":["plan.json","plan.html"]},ensure_ascii=False))
if __name__=="__main__":main()
