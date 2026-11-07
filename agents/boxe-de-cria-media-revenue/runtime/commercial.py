"""Pipeline simples de patrocinadores; NAO cria contratos nem pagamentos reais."""
import argparse
import datetime as dt
from decimal import Decimal,InvalidOperation
import json
from pathlib import Path
import sqlite3

STAGES=("lead","contacted","proposal","negotiation","contracted","paid","lost")
SCHEMA="""
CREATE TABLE IF NOT EXISTS opportunities (
 id TEXT PRIMARY KEY, organization TEXT NOT NULL, product TEXT NOT NULL,
 amount_brl TEXT NOT NULL, stage TEXT NOT NULL, notes TEXT,
 updated_at TEXT NOT NULL, CHECK(stage IN ('lead','contacted','proposal','negotiation','contracted','paid','lost')));
CREATE TABLE IF NOT EXISTS opportunity_history (
 id INTEGER PRIMARY KEY AUTOINCREMENT, opportunity_id TEXT NOT NULL,
 previous_stage TEXT, new_stage TEXT NOT NULL, at TEXT NOT NULL);
"""

def connect(path):
    p=Path(path);p.parent.mkdir(parents=True,exist_ok=True)
    con=sqlite3.connect(p);con.row_factory=sqlite3.Row;con.executescript(SCHEMA)
    return con

def update(con,oid,organization,product,amount_brl,stage,notes=""):
    if stage not in STAGES: raise ValueError("Estagio nao reconhecido")
    try:amount=Decimal(amount_brl)
    except InvalidOperation:raise ValueError("Valor invalido") from None
    if amount<0 or amount>Decimal("10000000"):raise ValueError("Fora de faixa")
    if not oid.strip() or not organization.strip() or not product.strip():raise ValueError("Campos obrigatorios")
    before=con.execute("SELECT stage FROM opportunities WHERE id=?",(oid,)).fetchone()
    old=before["stage"] if before else None
    now=dt.datetime.now(dt.timezone.utc).isoformat()
    con.execute("INSERT INTO opportunities(id,organization,product,amount_brl,stage,notes,updated_at) VALUES(?,?,?,?,?,?,?) "
                "ON CONFLICT(id) DO UPDATE SET organization=excluded.organization,product=excluded.product,"
                "amount_brl=excluded.amount_brl,stage=excluded.stage,notes=excluded.notes,updated_at=excluded.updated_at",
                (oid,organization,product,str(amount),stage,notes,now))
    con.execute("INSERT INTO opportunity_history(opportunity_id,previous_stage,new_stage,at) VALUES(?,?,?,?)",
                (oid,old,stage,now))
    con.commit()
    return {"id":oid,"stage":stage,"amount_brl":str(amount),"note":"Etapa registrada; nao comprova recebimento bancario"}

def summary(con):
    rows=con.execute("SELECT stage,amount_brl FROM opportunities").fetchall()
    totals={s:Decimal("0") for s in STAGES};counts={s:0 for s in STAGES}
    for row in rows:
        totals[row["stage"]]+=Decimal(row["amount_brl"]);counts[row["stage"]]+=1
    return {"counts":counts,"amounts_brl_by_stage":{k:str(v) for k,v in totals.items()},
            "warning":"Valores reportados manualmente, nao reconciliados a pagamentos ou impostos"}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--db",default="var/sales.sqlite3")
    sub=ap.add_subparsers(dest="cmd",required=True)
    p=sub.add_parser("upsert")
    for k in ("id","organization","product","amount","stage"):p.add_argument("--"+k,required=True)
    p.add_argument("--notes",default="")
    sub.add_parser("summary")
    a=ap.parse_args()
    with connect(a.db) as con:
        data=update(con,a.id,a.organization,a.product,a.amount,a.stage,a.notes) if a.cmd=="upsert" else summary(con)
    print(json.dumps(data,ensure_ascii=False,indent=2))

if __name__=="__main__":main()
