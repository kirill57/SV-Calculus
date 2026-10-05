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
errors=[];failed=[]
with sync_playwright() as p:
 b=p.chromium.launch(channel='msedge');page=b.new_page(viewport={'width':900,'height':850})
 page.on('pageerror',lambda e:errors.append(str(e)));page.on('requestfailed',lambda r:failed.append({'url':r.url,'error':r.failure}))
 page.goto(f'http://127.0.0.1:{s.server_port}/generated/asymptote/fig-sphere-from-parametric-semicircle-2.html',wait_until='networkidle')
 page.locator('canvas').screenshot(path=str(ROOT/'qa/audit/interactive-sphere.png'))
 result=page.evaluate('''() => ({canvasCount:document.querySelectorAll('canvas').length,width:document.querySelector('canvas')?.width,height:document.querySelector('canvas')?.height,libraryLoaded:!!document.asy,webgl:!!document.querySelector('canvas')?.getContext('webgl')})''')
 result.update(errors=errors,failedRequests=failed);(ROOT/'qa/audit/interactive-sphere.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result));b.close()
s.shutdown()
