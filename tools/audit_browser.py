"""Check browser math, generated images, and page layout in every section."""
from pathlib import Path
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from threading import Thread
from playwright.sync_api import sync_playwright
from lxml import etree as ET
import json
import sys

ROOT=Path(__file__).resolve().parents[1]
class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self,*args): pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(QuietHandler,directory=str(ROOT/'output/web')))
Thread(target=server.serve_forever,daemon=True).start()
base=f'http://127.0.0.1:{server.server_port}/'
tree=ET.parse(str(ROOT/'source/main.ptx')); tree.xinclude()
ids=tree.xpath('//section/@xml:id',namespaces={'xml':'http://www.w3.org/XML/1998/namespace'})
extras=tree.xpath('//chapter/@xml:id|//appendix/@xml:id|//preface/@xml:id',namespaces={'xml':'http://www.w3.org/XML/1998/namespace'})
mode=sys.argv[1] if len(sys.argv)>1 else 'full'
if mode=='supplement':
    ids=extras+['sec-5-3-the-chain-rule','sec-15-5-alternating-series','sec-16-6-taylor-series-for-elementary-functions']
    ids=[sid for sid in ids if (ROOT/'output/web'/f'{sid}.html').exists()]
elif mode in {'recheck','recheck-supplement'}:
    ids=sys.argv[2:]
results=[]
resultfile=ROOT/'qa/audit'/('browser-supplement.json' if mode in {'supplement','recheck-supplement'} else 'browser-results.json')
previous=json.loads(resultfile.read_text('utf-8')) if mode in {'recheck','recheck-supplement'} else []

def save_results():
    if mode in {'recheck','recheck-supplement'}:
        checked={r['section']:r for r in results}
        data=[checked.pop(r['section'],r) for r in previous]
        data.extend(checked.values())
    else:
        data=results
    resultfile.write_text(json.dumps(data,indent=2),encoding='utf-8')
with sync_playwright() as pw:
    browser=pw.chromium.launch(channel='msedge')
    page=browser.new_page(viewport={'width':1440,'height':1000})
    for i,sid in enumerate(ids):
        errors=[]
        def onerror(error): errors.append(str(error))
        page.on('pageerror',onerror)
        print('Loading',sid,flush=True)
        response=page.goto(base+sid+'.html',wait_until='domcontentloaded',timeout=45000)
        try:
            # Return a boolean: Playwright awaits a returned Promise, whose
            # fulfilled undefined value would otherwise count as false.
            page.wait_for_function('!!(window.MathJax && MathJax.startup && MathJax.startup.promise)',timeout=15000)
            math_loaded=page.evaluate('() => Promise.race([MathJax.startup.promise.then(()=>true),new Promise(resolve=>setTimeout(()=>resolve(false),20000))])')
        except Exception as exc:
            math_loaded=False; errors.append(str(exc))
        # Check hints in their real sections, keeping each typesetting batch small.
        opened_hints=page.evaluate('''() => {
            const hints=[...document.querySelectorAll('details.hint')];
            for (const hint of hints) {
                hint.open=true;
                for (let p=hint.parentElement;p;p=p.parentElement)
                    if(p.tagName==='DETAILS') p.open=true;
            }
            return hints.length;
        }''')
        hints_loaded=page.evaluate('''() => !window.MathJax?.typesetPromise ? false :
            Promise.race([MathJax.typesetPromise([...document.querySelectorAll('details.hint')]).then(()=>true),
                new Promise(resolve=>setTimeout(()=>resolve(false),20000))])''')
        findings=page.evaluate('''() => ({
            mathErrors:[...document.querySelectorAll('mjx-merror,[data-mjx-error]')].map(e=>({text:e.textContent,error:e.getAttribute('data-mjx-error'),source:e.closest('mjx-container')?.previousElementSibling?.textContent})),
            brokenImages:[...document.images].filter(e=>e.getAttribute('src')?.startsWith('generated/')&&(!e.complete||e.naturalWidth===0)).map(e=>e.getAttribute('src')),
            horizontalOverflow:document.documentElement.scrollWidth>innerWidth+5,
            mathCount:document.querySelectorAll('mjx-container').length
        })''')
        page.set_viewport_size({'width':390,'height':844})
        mobile=page.evaluate('document.documentElement.scrollWidth>innerWidth+5')
        page.set_viewport_size({'width':1440,'height':1000})
        results.append({'section':sid,'status':response.status if response else None,
                        'mathLoaded':math_loaded,'javascriptErrors':errors,
                        'openedHints':opened_hints,'hintsLoaded':hints_loaded,
                        'mobileOverflow':mobile,**findings})
        page.remove_listener('pageerror',onerror)
        if (i+1)%10==0: print('Checked',i+1,'of',len(ids),flush=True)
        save_results()
    browser.close()
server.shutdown()
print('Sections:',len(results),'math errors:',sum(len(r['mathErrors']) for r in results),
      'failed math loads:',sum(not r['mathLoaded'] for r in results),'broken images:',sum(len(r['brokenImages']) for r in results),flush=True)
