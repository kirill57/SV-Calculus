"""Assemble audit receipts and verify the published HTML against local bytes.

Read-only checks except for writing QA receipts and output/web/audit-build.json.
Browser runs must have been completed with audit_live_html.py first.
"""
from pathlib import Path
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlsplit, unquote
import argparse, datetime, hashlib, json, subprocess
import requests
from lxml import etree as E
from audit_live_html import source_pages

ROOT = Path(__file__).resolve().parents[1]
QA = ROOT / 'qa/audit-2026-10-17'
WEB = ROOT / 'output/web'
BASE = 'https://kirill57.github.io/SV-Calculus/'

def read(path):
    return json.loads(Path(path).read_text('utf-8'))

def write(path, value):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(value, indent=2)+'\n', encoding='utf-8')

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def healthy(row):
    return (row.get('status') == 200 and row.get('mathLoaded')
            and row.get('expandedMathLoaded') and not any(row.get(k) for k in
            ['mathErrors', 'brokenImages', 'desktopOverflow', 'mobileOverflow', 'desktopWideMath', 'mobileWideBlocks',
             'javascriptErrors', 'exception', 'visibleSpacingArtifacts']))

def merge(target, runs):
    rows = {r['page']: r for r in read(QA/target/'results.json')} if (QA/target/'results.json').exists() else {}
    for run in runs:
        rows.update({r['page']: r for r in read(QA/run/'results.json')})
    sections, others = source_pages()
    order = sections + others
    order += sorted(p.stem for p in WEB.glob('*.html') if p.stem not in order)
    assert set(rows) == set(order), (set(order)-set(rows), set(rows)-set(order))
    result = [rows[s] for s in order]
    summary = {
        'pages': len(result), 'openedHints': sum(r.get('openedHints', 0) for r in result if r['page'] in sections),
        'mathNodes': sum(r.get('mathCount', 0) for r in result),
        'problemPages': [r['page'] for r in result if not healthy(r)],
        'captureCounts': dict(Counter(c['kind'] for r in result for c in r.get('captures', []))),
        'mergedRunsInOrder': runs,
    }
    write(QA/target/'results.json', result)
    write(QA/target/'summary.json', summary)
    print(json.dumps(summary, indent=2))

def current_inputs():
    paths = sorted(p for p in (ROOT/'source').rglob('*') if p.suffix in {'.ptx', '.xml'})
    paths += [ROOT/p for p in ['project.ptx', 'publication/publication.ptx', 'requirements.txt']]
    return {str(p.relative_to(ROOT)): sha(p) for p in paths}

def local_receipt():
    inputs = current_inputs()
    assert inputs == read(QA/'validated-input.json'), 'Sources changed after validated build'
    inv = read(QA/'inventory.json')
    assert not inv['errors']
    assert inv['original_edition_sha256'] == read(ROOT/'qa/audit/baseline-inventory.json')['original_edition_sha256']
    assert not any(read(QA/'markup-sanity.json').values())
    for name in ['manuscript-schema.log', 'publication-schema.log']:
        assert not (QA/name).read_text('utf-8').strip(), name
    assert 'without errors.' in (QA/'local-build-final.log').read_text('utf-8')
    rows = read(QA/'local-final/results.json')
    assert len(rows) == 249 and all(healthy(r) for r in rows)
    for r in rows:
        assert sha(WEB/(r['page']+'.html')) == r['htmlSha256'], r['page']+' changed after browser review'
    counts = Counter(c['kind'] for r in rows for c in r.get('captures', []))
    assert counts == {'figure':327, 'table':159, 'array':112}, counts
    numeric = read(ROOT/'qa/audit/numerical-code-checks.json')
    selected = read(ROOT/'qa/additions/mathematical-checks.json')
    assert len(numeric)==40 and len(selected)==63 and all(x['passed'] for x in numeric+selected)
    checks = {}
    for group, name in [('early','early-mathematical-checks.json'), ('early_numeric','early-numeric-equalities.json'),
                        ('middle','middle-verification.json'), ('late','late-verification.json')]:
        data=read(QA/name)
        assert not data.get('failures') and not data.get('failed'), name
        results=data.get('results', data.get('checks', []))
        if isinstance(results,list): assert all(r['passed'] for r in results), name
        checks[group] = data.get('checks', len(results) if isinstance(results,list) else results)
    # Assets actually referenced by the generated pages, including every figure panel.
    assets=set()
    for p in WEB.glob('*.html'):
        doc=E.HTML(p.read_bytes())
        for el in doc.xpath('//*[@src] | //link[@href]'):
            ref=el.get('src') or el.get('href')
            parts=urlsplit(ref)
            if parts.scheme or parts.netloc or not parts.path or parts.path.startswith('/'):
                continue
            rel=unquote(parts.path)
            if (WEB/rel).is_file(): assets.add(rel)
    manifest={p:sha(WEB/p) for p in sorted(assets)}
    write(QA/'referenced-assets.json',manifest)
    for group in ['early','middle','late','front']:
        review=read(QA/(group+'-local-visual.json'))
        assert not review.get('remaining_visual_issues') and not review.get('other_visible_issues')
        assert not review.get('unresolvedFindings'), group+' visual review pending'
    result={
        'auditDate':'2026-10-17', 'status':'passed', 'startingSourceCommit':'afde796172ecd268507c15604551363c95ce95a8',
        'pretextVersion':'2.53.0', 'scope':'PreTeXt source and HTML; original LaTeX edition preserved',
        'sourceFiles':inv['source_files'], 'chapters':17, 'appendices':6, 'sections':188,
        'examples':614, 'exercisesAndHints':592, 'htmlPages':len(rows), 'captures':dict(counts),
        'mathNodes':sum(r['mathCount'] for r in rows), 'schemaErrors':0, 'structuralErrors':[], 'browserProblemPages':[],
        'existingNumericalChecks':len(numeric), 'selectedTopicChecks':len(selected), 'newCheckGroups':checks,
        'originalEditionFilesUnchanged':len(inv['original_edition_sha256']),
        'sourceFingerprint':hashlib.sha256(json.dumps(inputs,sort_keys=True).encode()).hexdigest(),
        'referencedAssetCount':len(manifest),
        'htmlSha256':{r['page']+'.html':r['htmlSha256'] for r in rows},
        'visualReviews':['early-local-visual.json','middle-local-visual.json','late-local-visual.json','front-local-visual.json'],
        'independentProofReview':['5.6 exponential defining limit and unique base e',
                                  '12.8 repeated-integration finite remainder before Taylor chapter',
                                  '17.6 supported C2 variations and zero extension'],
    }
    write(QA/'final-validation.json',result)
    print(json.dumps({k:v for k,v in result.items() if k!='htmlSha256'},indent=2))

def stamp():
    validation=read(QA/'final-validation.json')
    assert current_inputs()==read(QA/'validated-input.json')
    subprocess.run(['git','diff','--quiet','HEAD','--','source','project.ptx',
                    'publication/publication.ptx','requirements.txt'],cwd=ROOT,check=True)
    commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    value={'auditDate':'2026-10-17','sourceCommit':commit,'pretextVersion':'2.53.0',
           'sourceFingerprint':validation['sourceFingerprint'], 'htmlSha256':validation['htmlSha256'],
           'referencedAssetsSha256':read(QA/'referenced-assets.json'),
           'generatedAtUTC':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    write(WEB/'audit-build.json',value)
    print(commit)

def remote():
    stamp=read(WEB/'audit-build.json')
    expected={**stamp['htmlSha256'],**stamp['referencedAssetsSha256'],'audit-build.json':sha(WEB/'audit-build.json')}
    def get(item):
        path,digest=item
        try:
            response=requests.get(urljoin(BASE,path),timeout=45)
            actual=hashlib.sha256(response.content).hexdigest()
            return {'path':path,'status':response.status_code,'passed':response.status_code==200 and actual==digest,
                    'expectedSha256':digest,'actualSha256':actual}
        except Exception as exc:return {'path':path,'passed':False,'exception':str(exc)}
    with ThreadPoolExecutor(max_workers=8) as pool: results=list(pool.map(get,expected.items()))
    browser=read(QA/'live-after/results.json')
    problems=[r['page'] for r in browser if not healthy(r) or r.get('htmlSha256')!=stamp['htmlSha256'].get(r['page']+'.html')]
    receipt={'sourceCommit':stamp['sourceCommit'],'checkedAtUTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),
             'url':BASE+'single-variable-calculus.html','filesChecked':len(results),
             'mismatches':[r for r in results if not r['passed']], 'browserPages':len(browser),
             'browserProblemPages':problems,'openedHints':sum(r.get('openedHints',0) for r in browser)}
    write(ROOT/'output/publication-verification.json',receipt)
    print(json.dumps(receipt,indent=2))
    assert not receipt['mismatches'] and not problems and len(browser)==249

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('action',choices=['merge','local','stamp','remote'])
    parser.add_argument('--target')
    parser.add_argument('--runs',nargs='*',default=[])
    args=parser.parse_args()
    if args.action=='merge':merge(args.target,args.runs)
    elif args.action=='local':local_receipt()
    elif args.action=='stamp':stamp()
    else:remote()
