from pathlib import Path
from http.server import SimpleHTTPRequestHandler
ROOT=Path(__file__).resolve().parents[1]
class Q(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
from functools import partial
from http.server import ThreadingHTTPServer
from threading import Thread
from playwright.sync_api import sync_playwright
import json

s=ThreadingHTTPServer(('127.0.0.1',0),partial(Q,directory=str(ROOT)));Thread(target=s.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(channel='msedge');page=b.new_page(viewport={'width':1200,'height':900})
 page.goto(f'http://127.0.0.1:{s.server_port}/qa/audit/hints-render.html',wait_until='domcontentloaded')
 page.wait_for_function('!!(window.MathJax && MathJax.startup && MathJax.startup.promise)',timeout=15000);page.evaluate('() => MathJax.startup.promise');page.evaluate('() => MathJax.typesetPromise()')
 r=page.evaluate('''() => ({hints:document.querySelectorAll('details.hint').length,math:document.querySelectorAll('mjx-container').length,errors:[...document.querySelectorAll('mjx-merror,[data-mjx-error]')].map(e=>e.textContent)})''');print(json.dumps(r));(ROOT/'qa/audit/hints-browser.json').write_text(json.dumps(r,indent=2),encoding='utf-8');b.close()
s.shutdown()
