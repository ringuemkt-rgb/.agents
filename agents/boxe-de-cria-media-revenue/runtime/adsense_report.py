"""Google AdSense Management API v2: somente leitura, requer OAuth do titular."""
import argparse
import json
import os
import re
import urllib.error
import urllib.parse
import urllib.request

METRICS=("ESTIMATED_EARNINGS","PAGE_VIEWS","PAGE_VIEWS_RPM")
ALLOWED_RANGES=("YESTERDAY","LAST_7_DAYS","LAST_30_DAYS","THIS_MONTH","LAST_MONTH")

def report(account,token,date_range="LAST_7_DAYS"):
    if not re.fullmatch(r"accounts/[A-Za-z0-9_-]+",account):
        raise ValueError("Conta deve estar em formato accounts/ID")
    if date_range not in ALLOWED_RANGES:
        raise ValueError("Intervalo nao autorizado")
    if not token or len(token)<12:
        raise ValueError("OAuth token de acesso exigido")
    query=[("dateRange",date_range),("dimensions","DATE")]
    query.extend(("metrics",x) for x in METRICS)
    url="https://adsense.googleapis.com/v2/"+account+"/reports:generate?"+urllib.parse.urlencode(query)
    req=urllib.request.Request(url,headers={"Authorization":"Bearer "+token,"Accept":"application/json"})
    try:
        with urllib.request.urlopen(req,timeout=30) as response:
            return json.loads(response.read(2_000_000))
    except urllib.error.HTTPError as exc:
        raise RuntimeError("AdSense API erro HTTP "+str(exc.code)) from None

def main():
    ap=argparse.ArgumentParser(description="Relatorio real AdSense v2 somente leitura")
    ap.add_argument("--account",required=True,help="accounts/<ID> da conta autorizada")
    ap.add_argument("--date-range",choices=ALLOWED_RANGES,default="LAST_7_DAYS")
    ap.add_argument("--output",help="JSON local; nao publique em repositorio publico")
    args=ap.parse_args()
    data=report(args.account,os.environ.get("ADSENSE_ACCESS_TOKEN",""),args.date_range)
    serialized=json.dumps(data,ensure_ascii=False,indent=2)
    if args.output:
        from pathlib import Path
        p=Path(args.output)
        p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(serialized,encoding="utf8")
        print(json.dumps({"saved_to":str(p),"contains_private_financial_data":True}))
    else:
        print(serialized)

if __name__=="__main__":main()
