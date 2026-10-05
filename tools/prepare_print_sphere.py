"""Export the book's verified interactive Asymptote sphere as a print fallback.
Run after the web build; this addresses the local MiKTeX Asymptote PDF limitation.
"""
from pathlib import Path
from functools import partial
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from threading import Thread
from playwright.sync_api import sync_playwright
from PIL import Image
import json
ROOT=Path(__file__).resolve().parents[1]
class Q(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
s=ThreadingHTTPServer(('127.0.0.1',0),partial(Q,directory=str(ROOT/'output/web')));Thread(target=s.serve_forever,daemon=True).start()
asset='fig-sphere-from-parametric-semicircle-2'
errors=[]
with sync_playwright() as p:
 b=p.chromium.launch(channel='msedge');page=b.new_page(viewport={'width':1500,'height':1500},device_scale_factor=2)
 page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto(f'http://127.0.0.1:{s.server_port}/generated/asymptote/{asset}.html',wait_until='networkidle')
 page.wait_for_function('!!document.asy && !!document.querySelector("canvas")',timeout=15000)
 png=ROOT/'qa/audit/sphere-print-fallback.png';page.locator('canvas').screenshot(path=str(png));b.close()
s.shutdown()
if errors:raise RuntimeError(errors)
out=ROOT/'generated-assets/asymptote'/f'{asset}.pdf'
Image.open(png).convert('RGB').save(out,'PDF',resolution=300)
(ROOT/'qa/audit/sphere-print-fallback.json').write_text(json.dumps({'asset':str(out.relative_to(ROOT)),'pixels':Image.open(png).size,'errors':errors,'method':'Static export of the book’s original verified WebGL figure'},indent=2),encoding='utf-8')
print(out)
