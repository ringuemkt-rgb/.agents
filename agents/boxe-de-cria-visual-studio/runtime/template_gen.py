"""Generate editable neutral SVG layouts, never journalistic photographs or logos."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
from textwrap import wrap
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "config" / "image-presets.json"
TOKENS = ROOT / "config" / "brand.tokens.json"

def render_template(preset: str, title: str, section: str, out: Path) -> dict:
    presets = json.loads(SOURCE.read_text(encoding="utf8"))["presets"]
    brand = json.loads(TOKENS.read_text(encoding="utf8"))["colors"]
    if preset not in presets:
        raise ValueError("Preset desconhecido")
    title = " ".join(title.split()).strip()
    section = " ".join(section.split()).strip()
    if not 5 <= len(title) <= 96 or not 2 <= len(section) <= 24:
        raise ValueError("Titulo precisa ter 5-96 caracteres e editoria 2-24")
    if any(ord(c) < 32 for c in title + section):
        raise ValueError("Caracteres de controle nao permitidos")
    size = presets[preset]
    w, h, margin_pct = size["width"], size["height"], size["safe_area_percent"]
    margin = int(round(w * margin_pct / 100))
    avail = w - margin * 2
    title_font = max(27, round(w * (0.053 if w >= 1200 else 0.062)))
    if h > w:
        title_font = round(title_font * 0.93)
    line_count = max(12, min(42, int(avail // (title_font * 0.56))))
    # Conservative width bound for uppercase display text and mobile previews.
    lines = wrap(title, width=line_count, break_long_words=False)
    if len(lines) > 3:
        raise ValueError("Titulo exige reducao editorial: mais de tres linhas")
    title_lines = "\n".join(
        f'<text x="{margin}" y="{int(h*0.62) + i*int(title_font*1.25)}" '
        f'font-family="Oswald,Arial,sans-serif" font-size="{title_font}" '
        f'font-weight="700" fill="{brand["paper"]}">{escape(line)}</text>'
        for i, line in enumerate(lines)
    )
    stamp = "MODELO EDITAVEL - NAO PUBLICAR"
    placeholder = "INSERIR FOTO AUTORIZADA OU ILUSTRACAO IDENTIFICADA"
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Template editorial ainda sem arte ou logo autorizado">
  <title>{escape(section)} - template de arte, não publicável</title>
  <defs>
    <linearGradient id="surface" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{brand["ink"]}"/>
      <stop offset="1" stop-color="{brand["graphite"]}"/>
    </linearGradient>
  </defs>
  <rect width="{w}" height="{h}" fill="url(#surface)"/>
  <rect x="{margin}" y="{margin}" width="{max(1,w-2*margin)}" height="{round(h*.42)}"
    rx="18" fill="none" stroke="{brand["gold"]}" stroke-width="2" stroke-opacity=".7" stroke-dasharray="12 8"/>
  <text x="{w//2}" y="{margin + int(h*.2)}" fill="{brand["paper"]}" opacity=".7"
    font-family="Arial,sans-serif" text-anchor="middle" font-size="{max(14,int(w*.016))}">{placeholder}</text>
  <rect x="{margin}" y="{round(h*.53)}" width="{min(190,round(w*.24))}" height="5" fill="{brand["red"]}"/>
  <text x="{margin}" y="{round(h*.58)}" fill="{brand["gold"]}"
    font-family="Arial,sans-serif" font-weight="700" font-size="{max(18,int(w*.024))}">{escape(section.upper())}</text>
  {title_lines}
  <text x="{margin}" y="{h-margin}" fill="{brand["paper"]}" font-family="Arial,sans-serif"
    font-size="{max(12,int(w*.016))}" opacity=".75">{stamp}</text>
  <rect x="{w-margin-175}" y="{h-margin-38}" width="175" height="38" rx="4"
    fill="none" stroke="{brand["gold"]}" stroke-width="1.5" stroke-dasharray="5 4"/>
  <text x="{w-margin-87}" y="{h-margin-15}" font-size="13" text-anchor="middle"
    font-family="Arial,sans-serif" fill="{brand["paper"]}">LOGO ORIGINAL AQUI</text>
</svg>
'''
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(svg, encoding="utf8")
    manifest = {
        "preset": preset, "width": w, "height": h, "safe_area_percent": margin_pct,
        "title": title, "section": section,
        "state": "template_not_publishable",
        "official_logo": "not_included",
        "photo": "not_included",
        "review_requirements": ["approved editorial title", "licensed photography or disclosed illustration",
                                "unchanged official logo", "visual and factual QA"],
    }
    out.with_suffix(".manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2),
                                                    encoding="utf8")
    return {"svg": str(out), "manifest": str(out.with_suffix(".manifest.json")),
            "publishable": False, "dimensions": [w, h]}

def main(argv=None):
    parser = argparse.ArgumentParser(description="Produce editable nonpublishable BDC layouts")
    parser.add_argument("--preset", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--section", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        print(json.dumps(render_template(args.preset,args.title,args.section,args.output), ensure_ascii=False))
        return 0
    except (OSError, ValueError) as error:
        print(json.dumps({"ok": False, "error": str(error)}, ensure_ascii=False))
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
