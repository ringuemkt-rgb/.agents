#!/usr/bin/env python3
"""Generate a Cane Corso do Cangaço carousel prompt pack skeleton.

This script does not call any AI API. It creates a Markdown structure you can
paste into any AI chat after activating SYSTEM_PROMPT.md.
"""

from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path


def slugify(text: str) -> str:
    out = []
    for ch in text.lower():
        if ch.isalnum():
            out.append(ch)
        elif ch in " -_/":
            out.append("-")
    slug = "".join(out)
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-") or "tema"


def build_pack(theme: str, slides: int = 8) -> str:
    date = datetime.now().strftime("%Y-%m-%d")
    lines = [
        f"# Pacote de carrossel — {theme}",
        "",
        f"Data: {date}",
        "Marca: Cane Corso do Cangaço",
        "Sistema: Intelligence Compound System v3.0",
        "",
        "---",
        "",
        "## 1. Diagnóstico estratégico",
        "",
        "- Tema:",
        "- Objetivo estratégico:",
        "- Público-alvo:",
        "- Dor real do público:",
        "- Crença errada a quebrar:",
        "- Tese central:",
        "- Base técnica:",
        "- Nível de evidência:",
        "- Métrica principal esperada:",
        "",
        "---",
        "",
        "## 2. Variações de capa A/B/C",
        "",
        "### Capa A — Direta",
        "",
        "Headline:",
        "Subheadline:",
        "",
        "### Capa B — Provocativa",
        "",
        "Headline:",
        "Subheadline:",
        "",
        "### Capa C — Checklist",
        "",
        "Headline:",
        "Subheadline:",
        "",
        "---",
        "",
        "## 3. Roteiro slide por slide",
        "",
    ]

    for n in range(1, slides + 1):
        lines.extend([
            f"### Slide {n}/{slides}",
            "",
            "Função estratégica:",
            "Headline:",
            "Subheadline:",
            "Blocos:",
            "Selo:",
            "Barra final:",
            "",
        ])

    lines.extend([
        "---",
        "",
        "## 4. Prompts individuais autônomos",
        "",
    ])

    for n in range(1, slides + 1):
        lines.extend([
            f"### Prompt Slide {n}/{slides}",
            "",
            "```text",
            "Criar arte estática vertical 4:5, 2160x2700 px, ultra nítida, estilo infográfico premium 2.5D da marca CANE CORSO DO CANGAÇO.",
            "",
            "OBJETIVO DO SLIDE:",
            "{preencher}",
            "",
            "DNA VISUAL:",
            "fundo escuro premium em preto fosco e azul-preto profundo, textura sutil de couro e metal envelhecido, grid técnico discreto, molduras heráldicas refinadas, cards arredondados, acentos em bronze envelhecido, dourado fosco, couro marrom escuro, vermelho profundo e bege queimado, sombras suaves, profundidade 2.5D realista controlada, estética de brasão, território, tradição, honra, força sob controle e guardião de família.",
            "",
            "IDENTIDADE:",
            "visual inspirado na logo oficial Cane Corso do Cangaço: brasão circular, Cane Corso preto imponente e equilibrado, atmosfera nordestina refinada, rusticidade premium, proteção, disciplina, masculinidade firme e confiança.",
            "",
            "ELEMENTOS FIXOS:",
            f"topo esquerdo: “CANE CORSO DO CANGAÇO | CRIAÇÃO RESPONSÁVEL”\ntopo direito: “Slide {n}/{slides}”\nlaterais: “CANE CORSO DO CANGAÇO • CONTEÚDO ORIGINAL”\ncanto inferior esquerdo: logo oficial Cane Corso do Cangaço em versão dourada/bronze\ncanto inferior direito: ícone discreto ligado ao tema\nrodapé: “CANE CORSO DO CANGAÇO • Bahia”",
            "",
            "COMPOSIÇÃO:",
            "{preencher com descrição minuciosa}",
            "",
            "TEXTO DO SLIDE:",
            "Headline:\n{preencher}",
            "",
            "Subheadline:\n{preencher}",
            "",
            "Blocos:\n{preencher}",
            "",
            "Selo central:\n{preencher}",
            "",
            "Barra de conclusão:\n{preencher}",
            "",
            "RODAPÉ TÉCNICO:",
            "Base: padrão da raça • saúde • temperamento • criação responsável",
            "",
            "TIPOGRAFIA:",
            "headline em estilo Cinzel, Trajan ou Marcellus; apoio em Montserrat, Inter ou Sora; selos em Bebas Neue, Oswald ou Anton; alto contraste; leitura mobile-first.",
            "",
            "DIREÇÃO DE ARTE:",
            "iluminação dramática lateral suave, reflexos discretos em bronze, textura premium, profundidade 2.5D, composição limpa, cara de marca forte, autoral e confiável.",
            "",
            "REGRAS:",
            "português do Brasil, sem texto em inglês, uma ideia principal por slide, máximo impacto com mínimo texto, nunca vender agressividade como qualidade.",
            "",
            "NEGATIVE PROMPT:",
            "sem visual infantil, sem cartoon exagerado, sem estética pet shop genérico, sem cão raivoso, sem sangue, sem armas, sem violência gratuita, sem briga, sem mordida, sem ataque, sem texto em inglês, sem watermark, sem erro de ortografia, sem excesso de texto, sem poluição visual, sem panfleto barato, sem aparência amadora, sem anatomia deformada, sem gigantismo artificial, sem glamourizar agressividade.",
            "```",
            "",
        ])

    lines.extend([
        "---",
        "",
        "## 5. Legenda final",
        "",
        "```text",
        "{GANCHO FORTE} 🐕‍🦺🔥",
        "",
        "{Problema em linguagem simples}",
        "",
        "No Cane Corso, {verdade técnica}.",
        "",
        "Um bom guardião não nasce da aparência.",
        "Ele nasce de origem, saúde, temperamento, rotina e condução.",
        "",
        "{FRASE SALVÁVEL}",
        "",
        "👉 Comente {PALAVRA-CHAVE} para receber {benefício}.",
        "",
        "📌 Salve este post antes de tomar decisão.",
        "📤 Envie para quem precisa entender isso.",
        "",
        "#canecorso #canecorsobrasil #canecorsodocangaco #criacaoresponsavel #guardiaodefamilia",
        "```",
        "",
        "---",
        "",
        "## 6. Reels derivado",
        "",
        "- Hook:",
        "- Erro comum:",
        "- Verdade técnica:",
        "- Exemplo visual:",
        "- Frase salvável:",
        "- CTA:",
        "",
        "---",
        "",
        "## 7. 5 próximos temas com maior potencial viral — IPV",
        "",
        "1. Tema:",
        "IPV estimado:",
        "Métrica principal:",
        "Nível de evidência:",
        "Por que fazer:",
        "Gancho sugerido:",
        "Prioridade:",
    ])

    return "\n".join(lines) + "\n"


def main() -> int:
    if len(sys.argv) < 2:
        print('Uso: python3 scripts/prompt_pack_generator.py "Tema do carrossel" [slides]', file=sys.stderr)
        return 2
    theme = sys.argv[1]
    slides = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    content = build_pack(theme, slides)
    out_dir = Path("generated")
    out_dir.mkdir(exist_ok=True)
    path = out_dir / f"{slugify(theme)}.md"
    path.write_text(content, encoding="utf-8")
    print(f"Gerado: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
