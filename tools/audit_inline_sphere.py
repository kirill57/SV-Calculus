from pathlib import Path
from functools import partial
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from threading import Thread
from playwright.sync_api import sync_playwright
import json
ROOT=Path(__file__).resolve().parents[1]
class Q(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
s=ThreadingHTTPServer(('127.0.0.1',0),partial(Q,directory=str(ROOT/'output/web')));Thread(target=s.serve_forever,daemon=True).start()
errors=[]
with sync_playwright() as p:
 b=p.chromium.launch(channel='msedge');page=b.new_page(viewport={'width':1440,'height':1000})
 page.on('pageerror',lambda e:errors.append({'message':str(e),'stack':e.stack}))
 page.goto(f'http://127.0.0.1:{s.server_port}/sec-14-3-length-and-area-for-parametric-curves.html',wait_until='networkidle')
 (ROOT/'qa/audit/inline-sphere-errors.json').write_text(json.dumps(errors,indent=2),encoding='utf-8')
 page.evaluate('document.querySelector("iframe.asymptote").scrollIntoView()')
 page.screenshot(path=str(ROOT/'qa/audit/inline-sphere.png'))
 print(json.dumps(errors));(ROOT/'qa/audit/inline-sphere-errors.json').write_text(json.dumps(errors,indent=2),encoding='utf-8');b.close()
s.shutdown()
