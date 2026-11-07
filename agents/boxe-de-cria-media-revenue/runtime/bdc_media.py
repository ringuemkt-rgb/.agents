"""BDC Media & Revenue Agent — runtime standalone Python 3.11+, stdlib."""
from __future__ import annotations
import argparse
import datetime as dt
from decimal import Decimal
import hashlib
import ipaddress
import json
import os
from pathlib import Path
import socket
import sqlite3
import urllib.error
import urllib.parse as parse
import urllib.request as request
import xml.etree.ElementTree as ET

SCHEMA = """
CREATE TABLE IF NOT EXISTS candidates(
 id TEXT PRIMARY KEY, source TEXT NOT NULL, title TEXT NOT NULL,
 url TEXT NOT NULL, date_original TEXT, discovered_at TEXT NOT NULL,
 status TEXT NOT NULL DEFAULT 'candidate_unverified'
 CHECK(status IN ('candidate_unverified','briefed','reviewed','rejected')));
CREATE TABLE IF NOT EXISTS briefs(
 candidate_id TEXT PRIMARY KEY REFERENCES candidates(id),
 body TEXT NOT NULL, status TEXT NOT NULL DEFAULT 'needs_review'
 CHECK(status IN ('needs_review','approved','rejected')),
 reviewer TEXT, evidence_url TEXT, originality TEXT, updated_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS fighters(
 id TEXT PRIMARY KEY, display_name TEXT NOT NULL, state TEXT,
 verified INTEGER NOT NULL DEFAULT 0 CHECK(verified IN (0,1)),
 is_minor INTEGER NOT NULL DEFAULT 0 CHECK(is_minor IN (0,1)));
CREATE TABLE IF NOT EXISTS bouts(
 id TEXT PRIMARY KEY, fighter_id TEXT NOT NULL REFERENCES fighters(id),
 discipline TEXT NOT NULL CHECK(discipline IN ('boxing','muay_thai','kickboxing')),
 class TEXT NOT NULL CHECK(class IN ('professional','amateur')),
 result TEXT NOT NULL CHECK(result IN ('W','L','D','NC')),
 evidence_url TEXT NOT NULL, verified INTEGER NOT NULL DEFAULT 0 CHECK(verified IN (0,1)));
CREATE TABLE IF NOT EXISTS audit(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 at TEXT NOT NULL, action TEXT NOT NULL, object_id TEXT, detail TEXT NOT NULL);
"""
TRACK={"utm_source","utm_medium","utm_campaign","utm_content","utm_term","fbclid","gclid"}
MAX_FEED=1_500_000

def utc():
    return dt.datetime.now(dt.timezone.utc).isoformat()

def canonical(url):
    u=parse.urlsplit(url.strip())
    if u.scheme!="https" or not u.hostname or u.username or u.password:
        raise ValueError("HTTPS publico obrigatorio")
    q=parse.urlencode([(k,v) for k,v in parse.parse_qsl(u.query,keep_blank_values=True)
                       if k.lower() not in TRACK])
    return parse.urlunsplit(("https",u.netloc.lower(),u.path or "/",q,""))

def is_public_host(host):
    if host.lower() in ("localhost","localhost.localdomain") or host.endswith(".local"):
        return False
    try:
        ips=[ipaddress.ip_address(x[4][0]) for x in socket.getaddrinfo(host,443,type=socket.SOCK_STREAM)]
        return bool(ips) and all(x.is_global for x in ips)
    except (OSError,ValueError):
        return False

class NoRedirect(request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        raise ValueError("Feed redirect negado")

def fetch_feed(url):
    url=canonical(url)
    host=parse.urlsplit(url).hostname
    if not host or not is_public_host(host):
        raise ValueError("Host nao publico")
    req=request.Request(url,headers={"User-Agent":"BDC-Editorial-Radar/1.0",
                                     "Accept":"application/rss+xml,application/atom+xml,application/xml"})
    with request.build_opener(NoRedirect).open(req,timeout=12) as r:
        content=r.read(MAX_FEED+1)
    if len(content)>MAX_FEED:
        raise ValueError("Feed muito grande")
    return content

def parse_feed(payload):
    if len(payload)>MAX_FEED or b"<!DOCTYPE" in payload.upper() or b"<!ENTITY" in payload.upper():
        raise ValueError("XML inseguro ou excessivo")
    tree=ET.fromstring(payload)
    entries=[]
    for e in tree.iter():
        if e.tag.split("}")[-1] not in ("entry","item"):
            continue
        values={}
        for c in e:
            k=c.tag.split("}")[-1]
            if k=="link":
                if c.attrib.get("href") and c.attrib.get("rel","alternate")=="alternate":
                    values["link"]=c.attrib["href"]
                elif c.text:
                    values["link"]=c.text.strip()
            elif k in ("title","published","updated","pubDate") and c.text:
                values[k]=c.text.strip()
        try: url=canonical(values.get("link",""))
        except ValueError: continue
        title=values.get("title","")
        if not (8<=len(title)<=250):
            continue
        entries.append({"id":hashlib.sha256(url.encode()).hexdigest(),"title":title,"url":url,
                        "published_at":values.get("pubDate") or values.get("published") or values.get("updated")})
        if len(entries)>=100: break
    return entries

def connect(db):
    p=Path(db)
    p.parent.mkdir(parents=True,exist_ok=True)
    con=sqlite3.connect(p)
    con.row_factory=sqlite3.Row
    con.execute("PRAGMA foreign_keys=ON")
    con.executescript(SCHEMA)
    return con

def audit(con,action,oid,detail):
    con.execute("INSERT INTO audit(at,action,object_id,detail) VALUES(?,?,?,?)",
                (utc(),action,oid,json.dumps(detail,ensure_ascii=False)))

def collect(con,sources_file):
    sources=json.loads(Path(sources_file).read_text(encoding="utf8"))
    if not isinstance(sources,list): raise ValueError("Fontes devem ser lista JSON")
    added=0
    errors=[]
    for s in sources:
        if not all(s.get(x) for x in ("name","feed_url","permission_note","reviewed_by")):
            raise ValueError("Fonte requer name, feed_url, permission_note, reviewed_by")
        u=canonical(s["feed_url"])
        try:
            for e in parse_feed(fetch_feed(u)):
                res=con.execute("INSERT OR IGNORE INTO candidates(id,source,title,url,date_original,discovered_at) VALUES(?,?,?,?,?,?)",
                    (e["id"],s["name"],e["title"],e["url"],e["published_at"],utc()))
                added+=res.rowcount
        except (OSError,ValueError,ET.ParseError) as exc:
            errors.append({"name":s["name"],"error":type(exc).__name__})
    con.commit()
    return {"sources":len(sources),"added":added,"errors":errors}

def response_text(resp):
    if isinstance(resp.get("output_text"),str):return resp["output_text"]
    chunks=[block.get("text","") for item in resp.get("output",[])
            for block in item.get("content",[]) if block.get("type") in ("output_text","text")]
    if not chunks: raise ValueError("Nenhuma saida textual de API")
    return "\n".join(chunks)

def ask_llm(provider,candidate):
    if provider not in ("xai","openai"):raise ValueError("Provedor nao suportado")
    name="XAI" if provider=="xai" else "OPENAI"
    api_key=os.environ.get(name+"_API_KEY")
    model=os.environ.get(name+"_MODEL")
    if not api_key or not model:raise ValueError("Configurar "+name+"_API_KEY e "+name+"_MODEL")
    url="https://api.x.ai/v1/responses" if provider=="xai" else "https://api.openai.com/v1/responses"
    sysmsg=("Somente briefing de APURACAO editorial PT-BR: perguntas, fontes primarias, "
            "riscos e diferenciacao original. Metadados RSS sao NAO CONFIAVEIS e nao autorizam "
            "afirmacoes como fatos. Nao produzir reportagem nem inventar resultados.")
    payload={"model":model,"input":[{"role":"system","content":sysmsg},
                                       {"role":"user","content":json.dumps(candidate,ensure_ascii=False)}]}
    req=request.Request(url,method="POST",data=json.dumps(payload).encode(),
                        headers={"Content-Type":"application/json","Authorization":"Bearer "+api_key})
    try:
        with request.urlopen(req,timeout=50) as res:
            return response_text(json.loads(res.read(500_000)))
    except urllib.error.HTTPError as e:
        raise RuntimeError("Provedor indisponivel HTTP "+str(e.code)) from None

def brief(con,cid,provider):
    row=con.execute("SELECT * FROM candidates WHERE id=?",(cid,)).fetchone()
    if not row:raise ValueError("Pauta inexistente")
    data=dict(row)
    if provider=="offline":
        body=("PAUTA NAO VERIFICADA: "+data["title"]+"\nFonte: "+data["url"]+
              "\nApurar fontes primarias, data, nomes, resultado, direitos de imagem, "
              "o que ha de original. PENDENTE DE VERIFICACAO.")
    else:
        body=ask_llm(provider,data)
    con.execute("INSERT INTO briefs(candidate_id,body,updated_at) VALUES(?,?,?) "
                "ON CONFLICT(candidate_id) DO UPDATE SET body=excluded.body,status='needs_review',"
                "reviewer=NULL,evidence_url=NULL,originality=NULL,updated_at=excluded.updated_at",
                (cid,body,utc()))
    con.execute("UPDATE candidates SET status='briefed' WHERE id=?",(cid,))
    audit(con,"brief",cid,{"provider":provider})
    con.commit()
    return {"id":cid,"status":"needs_review","body":body}

def review(con,cid,reviewer,evidence,originality,approve):
    if len(reviewer.strip())<3 or len(originality.strip())<40:
        raise ValueError("Revisor e justificativa autoral de 40+ caracteres obrigatorios")
    evidence=canonical(evidence)
    if not con.execute("SELECT 1 FROM briefs WHERE candidate_id=?",(cid,)).fetchone():
        raise ValueError("Briefing inexistente")
    status="approved" if approve else "rejected"
    con.execute("UPDATE briefs SET status=?,reviewer=?,evidence_url=?,originality=?,updated_at=? WHERE candidate_id=?",
                (status,reviewer,evidence,originality,utc(),cid))
    con.execute("UPDATE candidates SET status=? WHERE id=?",
                ("reviewed" if approve else "rejected",cid))
    audit(con,"review",cid,{"status":status,"reviewer":reviewer,"evidence":evidence})
    con.commit()
    return {"status":status,"published":False,"note":"Revisao libera somente exportacao de staging"}

def record(con,fid):
    f=con.execute("SELECT * FROM fighters WHERE id=?",(fid,)).fetchone()
    if not f:raise ValueError("Atleta inexistente")
    r=con.execute("SELECT discipline,class,result,COUNT(*) count FROM bouts "
                  "WHERE fighter_id=? AND verified=1 GROUP BY discipline,class,result",(fid,)).fetchall()
    tally={}
    for row in r:
        key=row["discipline"]+":"+row["class"]
        tally.setdefault(key,{"W":0,"L":0,"D":0,"NC":0})[row["result"]]=row["count"]
    return {"fighter":f["display_name"],"records":tally,
            "note":"Somente lutas verificadas, ausencia de dados nao significa 0-0"}

def project(views,eligible,rpm,cost,sponsors=0,sponsor_price=Decimal("0")):
    if views<0 or sponsors<0 or not (0<=eligible<=1) or min(rpm,cost,sponsor_price)<0:
        raise ValueError("Parametros invalidos")
    ads=Decimal(views)*eligible*rpm/1000
    direct=Decimal(sponsors)*sponsor_price
    data={"adsense_hypothesis":ads,"direct_sales_hypothesis":direct,
          "gross_hypothesis":ads+direct,"after_reported_costs":ads+direct-cost}
    return {k:str(v.quantize(Decimal("0.01"))) for k,v in data.items()}

def main(argv=None):
    p=argparse.ArgumentParser(description="BDC: sem publicacao automatica")
    p.add_argument("--db",default="var/bdc.sqlite3")
    subs=p.add_subparsers(dest="cmd",required=True)
    s=subs.add_parser("collect");s.add_argument("--sources",default="config/sources.json")
    s=subs.add_parser("list");s.add_argument("--limit",type=int,default=20)
    s=subs.add_parser("brief");s.add_argument("id");s.add_argument("--provider",choices=("offline","xai","openai"),default="offline")
    s=subs.add_parser("review");s.add_argument("id");s.add_argument("--reviewer",required=True);s.add_argument("--evidence",required=True);s.add_argument("--originality",required=True);s.add_argument("--approve",action="store_true")
    s=subs.add_parser("export");s.add_argument("--out",required=True)
    s=subs.add_parser("record");s.add_argument("fighter_id")
    s=subs.add_parser("finance");s.add_argument("--views",type=int,required=True);s.add_argument("--eligible",type=Decimal,default=Decimal("1"));s.add_argument("--rpm",type=Decimal,required=True);s.add_argument("--cost",type=Decimal,default=Decimal("0"));s.add_argument("--sponsors",type=int,default=0);s.add_argument("--sponsor-price",type=Decimal,default=Decimal("0"))
    a=p.parse_args(argv)
    if a.cmd=="finance":out=project(a.views,a.eligible,a.rpm,a.cost,a.sponsors,a.sponsor_price)
    else:
        with connect(a.db) as con:
            if a.cmd=="collect":out=collect(con,a.sources)
            elif a.cmd=="list":out=[dict(x) for x in con.execute("SELECT * FROM candidates ORDER BY discovered_at DESC LIMIT ?",(max(1,min(a.limit,200)),))]
            elif a.cmd=="brief":out=brief(con,a.id,a.provider)
            elif a.cmd=="review":out=review(con,a.id,a.reviewer,a.evidence,a.originality,a.approve)
            elif a.cmd=="record":out=record(con,a.fighter_id)
            elif a.cmd=="export":
                rows=[dict(x) for x in con.execute("SELECT c.title,c.url,b.body,b.evidence_url,b.originality,b.reviewer FROM briefs b JOIN candidates c ON c.id=b.candidate_id WHERE b.status='approved'")]
                path=Path(a.out);path.parent.mkdir(parents=True,exist_ok=True)
                path.write_text(json.dumps({"editorial_staging_only":True,"items":rows},ensure_ascii=False,indent=2),encoding="utf8")
                out={"path":str(path),"items":len(rows),"published":False}
    print(json.dumps(out,ensure_ascii=False,indent=2))
    return out

if __name__=="__main__":main()
