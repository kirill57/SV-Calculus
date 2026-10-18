"""Audit the actual rendered PreTeXt book, remotely or from a local build.

The browser opens every exercise/example and hint, typesets their mathematics,
checks desktop/mobile layout, and optionally captures all figures and tables.
Receipts belong to the specified run, rather than replacing historical audits.
"""
from pathlib import Path
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from threading import Thread
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urljoin
import argparse, datetime, hashlib, json, re, time
from lxml import etree as E
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
QA = ROOT/'qa/audit-2026-10-17'
ID = '{http://www.w3.org/XML/1998/namespace}id'

def source_pages():
    tree = E.parse(str(ROOT/'source/main.ptx'))
    tree.xinclude()
    sections = [n.get(ID) for n in tree.iter('section')]
    others = [n.get(ID) for n in tree.iter()
              if n.tag in {'chapter','appendix','preface','part','book'} and n.get(ID)]
    return sections, others+['frontmatter','backmatter']

class Quiet(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass

def inspect_part(ids, base, out, capture, worker):
    rows = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(channel='msedge')
        page = browser.new_page(viewport={'width':1440,'height':1000}, device_scale_factor=1)
        for sid in ids:
            row = {'page':sid, 'url':urljoin(base,sid+'.html'), 'checkedAt':datetime.datetime.now(datetime.timezone.utc).isoformat()}
            errors=[]
            def onerror(e): errors.append(str(e))
            page.on('pageerror',onerror)
            try:
                response = page.goto(row['url'], wait_until='domcontentloaded', timeout=45000)
                row['status'] = response.status if response else None
                if sid=='index':
                    # The instant meta-refresh can evict the navigation response
                    # from Chromium's body cache. Read that tiny redirect through
                    # the request context and inspect its actual destination.
                    body=page.request.get(row['url']).body()
                    meta=next(e for e in E.HTML(body).iter('meta') if e.get('http-equiv','').lower()=='refresh')
                    target=meta.get('content').split(';',1)[1].split('=',1)[1].strip().strip(chr(34)+chr(39))
                    redirect=urljoin(row['url'],target)
                    if not redirect.startswith(base):
                        raise ValueError('Index redirects outside this book: '+redirect)
                    page.wait_for_url(redirect,wait_until='domcontentloaded',timeout=20000)
                    row['redirectTarget']=redirect
                else:
                    body=response.body() if response else b''
                row['htmlSha256'] = hashlib.sha256(body).hexdigest()
                row['finalUrl']=page.url
                page.wait_for_function('!!window.MathJax?.startup?.promise',timeout=20000)
                row['mathLoaded'] = page.evaluate('''() => Promise.race([
                    MathJax.startup.promise.then(()=>true),
                    new Promise(r=>setTimeout(()=>r(false),25000))])''')
                # Native details already contain their content; opening them also
                # ensures their diagrams are measured at their displayed sizes.
                row['openedHints'] = page.evaluate('''() => {
                    for(const e of document.querySelectorAll('main details:not(.image-description)')) e.open=true;
                    return document.querySelectorAll('main details.hint').length;
                }''')
                row['expandedMathLoaded'] = page.evaluate('''() => Promise.race([
                    MathJax.typesetPromise([...document.querySelectorAll('main details:not(.image-description)')]).then(()=>true),
                    new Promise(r=>setTimeout(()=>r(false),25000))])''')
                page.evaluate('''() => Promise.race([document.fonts.ready,new Promise(r=>setTimeout(r,3000))])''')
                page.wait_for_function('''() => [...document.querySelectorAll('main img')].every(e=>e.complete)''',timeout=10000)
                row.update(page.evaluate('''() => ({
                    title:document.title,
                    mathCount:document.querySelectorAll('main mjx-container').length,
                    mathErrors:[...document.querySelectorAll('mjx-merror,[data-mjx-error]')].map(e=>({text:e.textContent,error:e.getAttribute('data-mjx-error')})),
                    brokenImages:[...document.querySelectorAll('main img')].filter(e=>!e.complete||!e.naturalWidth).map(e=>e.src),
                    desktopOverflow:document.documentElement.scrollWidth>innerWidth+5,
                    desktopWideMath:[...document.querySelectorAll('main mjx-container[display="true"]')].filter(e=>e.getBoundingClientRect().width>e.parentElement.clientWidth+12).map(e=>({id:e.parentElement.id,width:e.getBoundingClientRect().width,available:e.parentElement.clientWidth})),
                    visibleSpacingArtifacts:[...document.querySelectorAll('main mjx-container')].filter(e=>['[1mm]','[2mm]','[3mm]','[4pt]','[6pt]'].some(s=>e.textContent.includes(s))).map(e=>({id:e.parentElement.id,text:e.textContent.slice(0,350)})),
                    figures:[...document.querySelectorAll('main figure.figure-like')].map(e=>({id:e.id,caption:e.querySelector('figcaption')?.textContent.trim(),images:[...e.querySelectorAll('img')].map(i=>({src:i.src,width:i.width,height:i.height,naturalWidth:i.naturalWidth,naturalHeight:i.naturalHeight}))})),
                    headings:[...document.querySelectorAll('main h1,main h2')].map(e=>({text:e.textContent.trim(),height:e.getBoundingClientRect().height}))
                })'''))
                if capture:
                    folder=out/'screenshots'/sid
                    folder.mkdir(parents=True,exist_ok=True)
                    page.screenshot(path=str(folder/'opening-desktop.png'))
                    # A sticky site toolbar can cover the top of a component
                    # when locator.screenshot scrolls it into view. Preserve
                    # normal page screenshots, but hide that chrome while
                    # inspecting the figure/table itself.
                    page.evaluate('''() => {
                        for(const e of document.querySelectorAll('body *')) {
                            if(e.closest('main')) continue;
                            if(['fixed','sticky'].includes(getComputedStyle(e).position)) {
                                e.dataset.auditVisibility=e.style.visibility;
                                e.style.visibility='hidden';
                            }
                        }
                    }''')
                    row['captures'] = []
                    for kind, selector in [('figure','main figure.figure-like'),('table','main figure.table-like')]:
                        for i,loc in enumerate(page.locator(selector).all()):
                            if not loc.is_visible(): continue
                            xid=loc.get_attribute('id') or f'{kind}-{i+1}'
                            dest=folder/f'{kind}-{xid}.png'
                            loc.screenshot(path=str(dest),timeout=15000)
                            row['captures'].append({'kind':kind,'id':xid,'file':str(dest.relative_to(ROOT))})
                    arrays=page.evaluate('''() => {
                        const a=Array.from(MathJax.startup.document.math).filter(m=>
                            m.display&&m.math.includes('begin{array}')&&m.typesetRoot.closest('main'));
                        return a.map((m,i)=>{
                            m.typesetRoot.setAttribute('data-audit-array',String(i+1));
                            return {index:i+1,id:m.typesetRoot.parentElement.id||('array-'+(i+1)),tex:m.math};
                        });
                    }''')
                    row['arrayCount']=len(arrays)
                    for array in arrays:
                        loc=page.locator('[data-audit-array="'+str(array['index'])+'"]')
                        dest=folder/f'array-{array["index"]:02}.png'
                        loc.screenshot(path=str(dest),timeout=15000)
                        row['captures'].append({'kind':'array','id':array['id'],'file':str(dest.relative_to(ROOT))})
                    page.evaluate('''() => {
                        for(const e of document.querySelectorAll('[data-audit-visibility]')) {
                            e.style.visibility=e.dataset.auditVisibility;
                            delete e.dataset.auditVisibility;
                        }
                    }''')
                page.set_viewport_size({'width':390,'height':844})
                row['mobileOverflow'] = page.evaluate('document.documentElement.scrollWidth>innerWidth+5')
                row['mobileWideBlocks'] = page.evaluate('''() => [...document.querySelectorAll('main .para,main figure,main pre')]
                    .filter(e=>e.getBoundingClientRect().width>innerWidth+5 && getComputedStyle(e).display!=='none')
                    .slice(0,12).map(e=>({id:e.id,width:e.getBoundingClientRect().width}))''')
                if capture:
                    page.evaluate('scrollTo(0,0)')
                    page.screenshot(path=str(folder/'opening-mobile.png'))
                page.set_viewport_size({'width':1440,'height':1000})
            except Exception as exc:
                row['exception']=str(exc)
            row['javascriptErrors']=errors
            rows.append(row)
            page.remove_listener('pageerror',onerror)
            (out/f'worker-{worker}.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
            print(f'[{worker}] {len(rows)}/{len(ids)} {sid}',flush=True)
        browser.close()
    return rows

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--base',default='local')
    ap.add_argument('--run',required=True)
    ap.add_argument('--capture',action='store_true')
    ap.add_argument('--workers',type=int,default=3)
    ap.add_argument('--ids',nargs='*')
    ap.add_argument('--sections-only',action='store_true')
    ap.add_argument('--generated-pages',action='store_true',help='Include introduction chunks, colophon, and the index redirect.')
    args=ap.parse_args()
    out=QA/args.run; out.mkdir(parents=True,exist_ok=True)
    sections,others=source_pages()
    ids=args.ids or sections+([] if args.sections_only else others)
    if args.generated_pages and not args.ids:
        extras=sorted(p.stem for p in (ROOT/'output/web').glob('*.html') if p.stem not in ids)
        ids+=extras
    server=None
    if args.base=='local':
        server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(ROOT/'output/web')))
        Thread(target=server.serve_forever,daemon=True).start()
        base=f'http://127.0.0.1:{server.server_port}/'
    else:
        base=args.base.rstrip('/')+'/'
    results=[]
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        jobs=[pool.submit(inspect_part,ids[i::args.workers],base,out,args.capture,i+1) for i in range(args.workers)]
        for job in as_completed(jobs): results.extend(job.result())
    order={sid:i for i,sid in enumerate(ids)}
    results.sort(key=lambda row:order[row['page']])
    (out/'results.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
    problems=[r['page'] for r in results if not (
        r.get('status')==200 and r.get('mathLoaded') and r.get('expandedMathLoaded')
        and not any(r.get(k) for k in ['mathErrors','brokenImages','desktopOverflow','mobileOverflow','javascriptErrors','exception','visibleSpacingArtifacts']))]
    summary={'base':base,'pages':len(results),'openedHints':sum(r.get('openedHints',0) for r in results if r['page'] in sections),
             'mathNodes':sum(r.get('mathCount',0) for r in results), 'problemPages':problems,
             'captureCount':sum(len(r.get('captures',[])) for r in results)}
    (out/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    if server:server.shutdown()
    print(json.dumps(summary,indent=2),flush=True)

if __name__=='__main__':main()
