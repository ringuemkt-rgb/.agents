"""BDC Visual Studio: deterministic brand, presets and asset provenance checks. Python 3.11+."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_PRESETS = {
    "news_hero", "article_card", "open_graph",
    "social_portrait", "fighter_portrait", "event_poster", "fisio_hero",
}
REQUIRED_COLORS = {
    "ink": "#0B0B0B", "gold": "#C9A24E", "red": "#B33939",
    "paper": "#F3F3F3", "graphite": "#242424",
}

def read_json(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"JSON object required: {path}")
    return data

def luminance(color: str) -> float:
    if re.fullmatch(r"#[0-9a-fA-F]{6}", color) is None:
        raise ValueError("Hex RGB color required")
    values = [int(color[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    linear = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
              for v in values]
    return sum(a * b for a, b in zip(linear, (0.2126, 0.7152, 0.0722)))

def contrast_ratio(a: str, b: str) -> float:
    hi, lo = sorted((luminance(a), luminance(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)

def check_tokens(path: Path | None = None) -> dict:
    data = read_json(path or ROOT / "config" / "brand.tokens.json")
    colors = data.get("colors", {})
    if colors != REQUIRED_COLORS:
        raise ValueError("Brand colors changed without approval")
    semantic = data.get("semantic", {})
    for key in ("background", "background_secondary", "text_primary", "accent"):
        if semantic.get(key) not in colors:
            raise ValueError(f"Unknown semantic token: {key}")
    layout = data.get("layout", {})
    if layout.get("grid_columns") != 12:
        raise ValueError("12-column web grid required")
    if layout.get("min_safe_area_percent", 0) < 7:
        raise ValueError("Insufficient safe area")
    target = layout.get("body_contrast_ratio_min", 0)
    if target < 4.5:
        raise ValueError("Text contrast minimum below WCAG AA")
    for fg, bg in (("paper", "ink"), ("gold", "ink"), ("ink", "gold")):
        if contrast_ratio(colors[fg], colors[bg]) < 4.5:
            raise ValueError(f"Brand colors fail contrast: {fg}/{bg}")
    if data.get("policies", {}).get("logo") != "original_asset_immutable_sha256_verified":
        raise ValueError("Logo integrity policy altered")
    return {"ok": True, "brand": data.get("brand"), "colors": len(colors),
            "paper_on_ink_contrast": round(contrast_ratio(colors["paper"], colors["ink"]), 2),
            "gold_on_ink_contrast": round(contrast_ratio(colors["gold"], colors["ink"]), 2)}

def check_presets(path: Path | None = None) -> dict:
    data = read_json(path or ROOT / "config" / "image-presets.json")
    presets = data.get("presets", {})
    if not REQUIRED_PRESETS.issubset(presets):
        raise ValueError("Required image presets missing")
    for name, item in presets.items():
        w, h = item.get("width", 0), item.get("height", 0)
        if not isinstance(w, int) or not isinstance(h, int) or not (320 <= w <= 8192 and 320 <= h <= 8192):
            raise ValueError(f"Bad export dimensions: {name}")
        if not (7 <= item.get("safe_area_percent", 0) <= 25):
            raise ValueError(f"Unsafe margins: {name}")
    if (presets["open_graph"]["width"], presets["open_graph"]["height"]) != (1200, 630):
        raise ValueError("OpenGraph preset must be 1200x630")
    if (presets["social_portrait"]["width"], presets["social_portrait"]["height"]) != (1080, 1350):
        raise ValueError("4:5 social preset must be 1080x1350")
    return {"ok": True, "presets": len(presets), "minimum_safe_area_percent": 7}

def check_asset_registry(path: Path, strict_files: bool = False) -> dict:
    data = read_json(path)
    assets = data.get("assets")
    if not isinstance(assets, list):
        raise ValueError("Registry assets must be a list")
    ids = set()
    for asset in assets:
        if not isinstance(asset, dict):
            raise ValueError("Asset entry must be object")
        fields = ("asset_id", "type", "origin", "rights_status", "usage_scope", "sha256", "reviewed_by")
        if any(not asset.get(x) for x in fields):
            raise ValueError("Missing provenance, rights or reviewer")
        if asset["asset_id"] in ids:
            raise ValueError("Duplicate asset id")
        ids.add(asset["asset_id"])
        if asset["rights_status"] != "approved":
            raise ValueError("Only approved assets can be released")
        if not re.fullmatch(r"[0-9a-f]{64}", asset["sha256"]):
            raise ValueError("Invalid SHA-256")
        kind = asset["type"]
        if kind in ("official_logo", "licensed_photo", "provided_photo"):
            if kind == "official_logo" and not asset.get("immutable_original"):
                raise ValueError("Official logo must remain immutable")
            if kind in ("licensed_photo", "provided_photo") and not asset.get("identity_and_context_preserved"):
                raise ValueError("Photo fidelity not confirmed")
        elif kind == "ai_illustration":
            if not asset.get("labeled_as_illustration"):
                raise ValueError("AI illustration needs clear editorial labeling")
        elif kind not in ("original_illustration", "scientific_diagram"):
            raise ValueError("Unknown asset type")
        if asset.get("minor_subject") and not asset.get("minor_privacy_review"):
            raise ValueError("Minor protection missing")
        if strict_files:
            local = asset.get("local_original_path")
            if not local:
                raise ValueError("Local file path needed for hash check")
            file = Path(local)
            if not file.is_file():
                raise ValueError("Original file not found")
            if hashlib.sha256(file.read_bytes()).hexdigest() != asset["sha256"]:
                raise ValueError("Original hash mismatch")
    return {"ok": True, "assets": len(assets), "rights_verified_from_metadata": bool(assets)}

def main(argv=None):
    parser = argparse.ArgumentParser(description="BDC Visual Studio verification")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("tokens")
    sub.add_parser("presets")
    reg = sub.add_parser("registry")
    reg.add_argument("--manifest", type=Path, required=True)
    reg.add_argument("--strict-files", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.command == "tokens":
            result = check_tokens()
        elif args.command == "presets":
            result = check_presets()
        else:
            result = check_asset_registry(args.manifest, args.strict_files)
        print(json.dumps(result, ensure_ascii=False))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(json.dumps({"ok": False, "error": str(error)}, ensure_ascii=False))
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
