from pathlib import Path
from lxml import etree as E
from audit_edit import ROOT,save,record
import re,json,math
receipts=[]
for p in (ROOT/'source').rglob('*.xml'):
 s=p.read_text('utf-8');old=s
 # Pure prose arrays should use wrapping text columns rather than math-mode text boxes.
 pat=r'<me>\s*\\begin\{array\}\{[^}]+\}([\s\S]*?)\\end\{array\}\s*</me>'
 def prose_array(m):
  rows=re.split(r'\\\\',m.group(1).strip());cells=[r.split(r'\amp') for r in rows];clean=[]
  for row in cells:
   rr=[]
   for cell in row:
    n=re.fullmatch(r'\s*\\text\{([^{}\\]+)\}\s*',cell)
    if not n:return m.group()
    rr.append(n.group(1))
   clean.append(rr)
  if len(set(map(len,clean)))!=1:return m.group()
  n=len(clean[0]);width=100/n
  return '<tabular width="100%" halign="left">'+''.join(f'<col width="{width:g}%"/>' for _ in range(n))+''.join('<row>'+''.join('<cell>'+c+'</cell>' for c in row)+'</row>' for row in clean)+'</tabular>'
 s=re.sub(pat,prose_array,s)
 # Constrain every table to the page; wrap long prose rather than shrinking it.
 for m in list(re.finditer(r'<tabular\b[^>]*>[\s\S]*?</tabular>',s))[::-1]:
  block=m.group();tab=E.fromstring(block.encode());rows=tab.findall('row')
  if not rows:continue
  n=max(len(row.findall('cell')) for row in rows)
  prose=False;weights=[]
  for i in range(n):
   texts=[]
   for row in rows:
    cs=row.findall('cell')
    if i>=len(cs):continue
    c=cs[i];plain=''.join(c.itertext());texts.append(len(plain))
    # A prose cell has substantial text outside its math children.
    direct=(c.text or '')+''.join(x.tail or '' for x in c)
    if len(direct.strip())>45:prose=True
   weights.append(max(12,math.sqrt(max(texts or [1]))))
  if tab.get('width') is None:tab.set('width','100%')
  if prose and not tab.findall('col') and n<=5:
   raw=[round(100*w/sum(weights),1) for w in weights];raw[-1]=round(100-sum(raw[:-1]),1)
   for i,w in reversed(list(enumerate(raw))):tab.insert(0,E.Element('col',width=f'{w:g}%'))
  new=E.tostring(tab,encoding='unicode',with_tail=False)
  if new!=block:
   s=s[:m.start()]+new+s[m.end():];receipts.append({'file':str(p.relative_to(ROOT)),'columns':n,'wrap_prose':prose,'id':tab.getparent().get('{http://www.w3.org/XML/1998/namespace}id') if tab.getparent() is not None else None})
 if s!=old:save(p,s);record(p,'Constrain tables to page width and wrap long prose columns; convert pure prose arrays to semantic tables',old,s)
(ROOT/'qa/audit/print-table-layout.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8');print('TABLES',len(receipts))
