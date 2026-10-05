"""Scan every generated PDF page for text outside physical page boundaries."""
from pathlib import Path
import fitz, json, re, hashlib
ROOT=Path(__file__).resolve().parents[1];QA=ROOT/'qa/audit'
p=ROOT/'output/print/main.pdf';doc=fitz.open(p);outside=[];small=[]
for i,page in enumerate(doc):
    for block in page.get_text('dict')['blocks']:
        for line in block.get('lines',[]):
            for span in line['spans']:
                x0,y0,x1,y1=span['bbox']
                if x0 < -1 or y0 < -1 or x1 > page.rect.width+1 or y1 > page.rect.height+1:
                    outside.append({'page':i+1,'text':span['text'],'bbox':span['bbox']})
                if 0<span['size']<7.5 and sum(c.isalpha() for c in span['text'])>18 and len(span['text'].split())>2:
                    small.append({'page':i+1,'size':span['size'],'text':span['text']})
r={'pages':len(doc),'file':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'outsidePage':outside}
(QA/'print-physical-boundaries.json').write_text(json.dumps(r,indent=2),encoding='utf-8')
(QA/'print-small-text.json').write_text(json.dumps(small,indent=2),encoding='utf-8')
log=(ROOT/'output/print/main.log').read_text(errors='replace');tex=(ROOT/'output/print/main.tex').read_text('utf-8').splitlines();over=[]
for m in re.finditer(r'Overfull \\hbox \(([\d.]+)pt[^\n]*?(?:at lines|at line) (\d+)(?:--\d+)?',log):
    n=int(m[2]);over.append({'points':float(m[1]),'line':n,'context':'\n'.join(tex[max(0,n-7):n+1])})
(QA/'print-overfull.json').write_text(json.dumps(over,indent=2),encoding='utf-8')
print('Pages',len(doc),'outside-page spans',len(outside),'overfull boxes >=12pt',sum(x['points']>=12 for x in over))
