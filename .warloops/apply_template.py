#!/usr/bin/env python3
"""War Loops — propagate the Field Manual guide template to a guide page.

The guide pages all share the SAME class names (hero/eyebrow/toc/secnum/callout/
pre/download/grid/gp/dlbtn/footer), so converting one is a deterministic swap of:
  1. the Google-Fonts <link>  -> brand 4-font stack
  2. the <style> block         -> the locked template CSS (read from skills-101.html)
  3. inject the manifest bar after <div class="wrap">  (idempotent)
  4. replace the download-button down-arrow glyph with an inline SVG

Body copy + the download <script> are never touched. Run: python3 apply_template.py <file...>
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
TEMPLATE = (ROOT / "guides" / "skills-101.html").read_text()

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com"/>\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>\n'
    '<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@800;900'
    '&family=Playfair+Display:wght@700&family=DM+Sans:wght@400;500;600;700'
    '&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet"/>'
)
STYLE = re.search(r"<style>.*?</style>", TEMPLATE, re.S).group(0)
MANIFEST = re.search(r'<div class="manifest">.*?</div>', TEMPLATE, re.S).group(0)
DL_SVG = ('<svg viewBox="0 0 24 24" aria-hidden="true">'
          '<path d="M12 4v12m0 0l-5-5m5 5l5-5M5 20h14"/></svg> ')

def convert(text: str) -> str:
    # 1. fonts: any existing googleapis stylesheet link -> brand stack
    text = re.sub(r'(?:<link rel="preconnect"[^>]*>\s*)*'
                  r'<link href="https://fonts\.googleapis\.com[^"]*" rel="stylesheet"/>',
                  lambda _m: FONTS, text, count=1)
    # 2. style block
    text = re.sub(r"<style>.*?</style>", lambda _m: STYLE, text, count=1, flags=re.S)
    # 3. manifest bar (skip if already present)
    if 'class="manifest"' not in text:
        text = text.replace('<div class="wrap">', '<div class="wrap">\n' + MANIFEST + '\n', 1)
    # 4. download arrow glyph -> SVG
    text = text.replace('downloadAsset()">↓ ', 'downloadAsset()">' + DL_SVG)
    return text

if __name__ == "__main__":
    for f in sys.argv[1:]:
        p = pathlib.Path(f)
        out = convert(p.read_text())
        p.write_text(out)
        print("converted", p.resolve().relative_to(ROOT))
