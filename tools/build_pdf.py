#!/usr/bin/env python3
"""Rebuild business/Heaft-Business-Model.pdf from business/index.html.
One page per slide, every build forced visible, no deck chrome.
    python3 build_pdf.py <deck.html> <out.pdf>
"""
import re, subprocess, sys, pathlib
src, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
h = src.read_text()
style = re.search(r'<style>(.*?)</style>', h, re.S).group(1)
slides = re.findall(r'<section class="slide[^"]*"[^>]*>.*?</section>', h, re.S)
assert len(slides) >= 2, slides
print(f'{len(slides)} slides')
EXPORT = """
  @page{size:960pt 540pt;margin:0}
  *{print-color-adjust:exact;-webkit-print-color-adjust:exact}
  body{background:#fff;display:block}
  .stage{position:relative;width:960pt;height:540pt;container-type:size;background:#fff;
         color:var(--ink);overflow:hidden;border-radius:0;box-shadow:none;break-after:page}
  .stage:last-child{break-after:auto}
  .slide{position:absolute;inset:0}
  [data-build]{opacity:1!important;transform:none!important;transition:none!important}
  .draw{stroke-dashoffset:0!important}
  .flow,.pulse{display:none!important}
"""
pages = "\n".join(f'<div class="stage">{s}</div>' for s in slides)
doc = (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
       f'{re.search(r"<link rel=.stylesheet.[^>]*>", h).group(0)}'
       f'<style>{style}{EXPORT}</style></head><body>{pages}</body></html>')
tmp = out.with_suffix('.print.html'); tmp.write_text(doc)
subprocess.run(['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
                '--headless', '--disable-gpu', '--no-pdf-header-footer',
                '--virtual-time-budget=20000', f'--print-to-pdf={out}',
                f'file://{tmp.resolve()}'], check=True,
               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
tmp.unlink()
print(subprocess.run(['pdfinfo', str(out)], capture_output=True, text=True).stdout.strip())
