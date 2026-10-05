"""Collect final audit receipts; fail if a required check is incomplete."""
from pathlib import Path
from lxml import etree as E
import json,hashlib,datetime

ROOT=Path(__file__).resolve().parents[1];QA=ROOT/'qa/audit'
def read(name):return json.loads((QA/name).read_text('utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def passed(row):
    return row['status']==200 and row['mathLoaded'] and row['hintsLoaded'] and not any([
        row['mathErrors'],row['javascriptErrors'],row['brokenImages'],row['horizontalOverflow'],row['mobileOverflow']])

inv=read('inventory.json');browser=read('browser-results.json');supplement=read('browser-supplement.json')
nums=read('numerical-code-checks.json');bounds=read('print-physical-boundaries.json');visual=read('print-visual-review.json')
baseline=read('baseline-inventory.json')['original_edition_sha256']
original={str(p.relative_to(ROOT)):sha(p) for p in (ROOT/'Single_Variable_Calculus_Change__Accumulation__and_Approximation').rglob('*') if p.is_file()}
assert original==baseline,'Original LaTeX edition changed'
preservation={'files':len(original),'unchanged':True,'changed':[],'added':[]}
(QA/'original-edition-preservation.json').write_text(json.dumps(preservation,indent=2),encoding='utf-8')
assert not inv['errors']
assert not (QA/'schema-current.log').read_text().strip()
assert not read('math-grouping.json')
assert len(browser)==182 and all(passed(r) for r in browser)
assert sum(r['openedHints'] for r in browser)==580
assert len(supplement)==28 and all(passed(r) for r in supplement)
assert len(nums)==40 and all(r['passed'] for r in nums)
assert not read('inline-sphere-errors.json')
interactive=read('interactive-sphere.json')
assert interactive['webgl'] and interactive['libraryLoaded'] and not interactive['errors'] and not interactive['failedRequests']
pdfsha=sha(ROOT/'output/print/main.pdf')
assert bounds['sha256']==pdfsha and not bounds['outsidePage']
assert visual['sha256']==pdfsha and visual['visualReview']=='reviewed'
assert not any(r['points']>=12 for r in read('print-overfull.json'))

files=sorted(p for p in (ROOT/'source').rglob('*') if p.suffix in {'.ptx','.xml'})
files += [ROOT/'project.ptx',ROOT/'publication/publication.ptx']
r={'completed':datetime.datetime.now(datetime.timezone.utc).isoformat(),
   'scope':'PreTeXt edition only', 'chapters':17,'appendices':6,
   'sourceSha256':{str(p.relative_to(ROOT)):sha(p) for p in files},
   'schemaErrors':0,'inventoryErrors':0,'browserSections':len(browser),'openedHints':580,
   'browserSupplementPages':len(supplement),'renderedMathNodes':sum(r['mathCount'] for r in browser),
   'browserProblems':0,'numericalChecks':len(nums),'numericalFailures':0,
   'figures':inv['counts']['figure'],'imagePanels':inv['counts']['image'],
   'pdfPages':bounds['pages'],'pdfSha256':pdfsha,'pdfOutOfPageSpans':0,
   'visuallyReviewedPdfPages':len(visual['renderedPages']),
   'originalEditionPreserved':True,'originalFiles':len(original),
   'limitations':['Local native Asymptote PDF renderer requires the documented static export',
                  'Installed publication schema and HTML configuration are incompatible; verified builds succeed',
                  'CLI version differs from project requirements; deprecated markup remains supported']}
(QA/'final-validation.json').write_text(json.dumps(r,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in r.items() if k!='sourceSha256'},indent=2))
