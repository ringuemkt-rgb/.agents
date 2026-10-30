#!/usr/bin/env python3
"""Local browser helper. HUMAN-DRIVEN login. No submission or CAPTCHA bypass."""
import argparse
import json
from pathlib import Path
from urllib.parse import urlsplit

def main():
    p = argparse.ArgumentParser(description="Abrir formulário oficial e preencher rascunho (sem envio)")
    p.add_argument("--url",required=True,help="Somente página HTTPS oficial")
    p.add_argument("--draft",help="JSON local de campos {label visível: valor}; opcional")
    p.add_argument("--allowed-host",action="append",required=True)
    args=p.parse_args()
    host=(urlsplit(args.url).hostname or "").lower()
    if urlsplit(args.url).scheme != "https" or host not in {x.lower() for x in args.allowed_host}:
        p.error("A URL não está na allowlist explícita do operador.")
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        p.error("Instale a dependência opcional: pip install playwright && playwright install chromium")
    fields={}
    if args.draft:
        fields=json.loads(Path(args.draft).read_text(encoding="utf-8"))
        if not isinstance(fields,dict) or not all(isinstance(k,str) and isinstance(v,str) for k,v in fields.items()):
            p.error("Rascunho inválido: JSON {nome_do_campo: texto}")
    print("A sessão é local. Faça login, 2FA/CAPTCHA e confira TODOS os campos pessoalmente.")
    print("NÃO haverá submissão, pagamento, aceite de declaração nem gravação de credenciais.")
    with sync_playwright() as pw:
        browser=pw.chromium.launch(headless=False)
        context=browser.new_context(accept_downloads=False)
        page=context.new_page()
        page.goto(args.url,wait_until="domcontentloaded",timeout=30000)
        input("Pressione ENTER após autenticar-se e chegar ao formulário. ")
        if page.url.split("/")[2].lower() not in {x.lower() for x in args.allowed_host}:
            raise RuntimeError("Página mudou para um host não autorizado; campos não preenchidos")
        for label,value in fields.items():
            try:
                locator=page.get_by_label(label,exact=True)
                if locator.count()!=1:
                    print(f"[REVISÃO MANUAL] Campo {label!r}: encontrados {locator.count()} controles")
                    continue
                locator.fill(value,timeout=3000)
                print(f"[RASCUNHO] Campo {label!r} preenchido; revise antes de prosseguir")
            except Exception as exc:
                print(f"[REVISÃO MANUAL] Campo {label!r}: {type(exc).__name__}")
        print("Revise o formulário. QUALQUER envio final exige ação direta e consciente sua.")
        input("Pressione ENTER para encerrar a sessão sem clicar em enviar. ")
        context.close()
        browser.close()

if __name__ == "__main__":
    main()
