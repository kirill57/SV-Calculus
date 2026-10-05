"""Find prose to inspect; word matches are review cues, not automatic judgments."""
from pathlib import Path
import re,json,sys
from lxml import etree as E
ROOT=Path(__file__).resolve().parents[1]
path=ROOT/'qa/additions/language-candidates.json'
pattern=re.compile(r'\b(?:promises?|stor(?:y|ies)|friendly|polite|magic|calm|honest|surprises?|obedient|myster(?:y|ious)|wants|deeper|miracle|quiet(?:er)?|generous)\b',re.I)
def build():
    rows=[]
    for p in sorted((ROOT/'source').rglob('*')):
        if p.suffix not in {'.xml','.ptx'}:continue
        text=p.read_text('utf-8')
        root=E.fromstring(text.encode());xid=root.get('{http://www.w3.org/XML/1998/namespace}id')
        for match in re.finditer(r'<p>(?:(?!<p>).)*?</p>',text,re.S):
            raw=match.group()
            try:el=E.fromstring(raw.encode())
            except E.XMLSyntaxError:continue
            plain=' '.join(''.join(el.itertext()).split())
            if pattern.search(plain):rows.append({'index':len(rows),'file':str(p.relative_to(ROOT)),
                'id':xid,'line':text[:match.start()].count('\n')+1,'before':raw,'text':plain})
    path.write_text(json.dumps(rows,indent=2,ensure_ascii=False),encoding='utf-8')
    print('Candidates:',len(rows))
def show(start,end):
    rows=json.loads(path.read_text('utf-8'))
    for row in rows[start:end]:print(row['index'],row['id'],'|',row['text'])
if __name__=='__main__':
    if len(sys.argv)==1:build()
    else:show(int(sys.argv[1]),int(sys.argv[2]))
