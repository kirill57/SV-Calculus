"""Extract openings and record narrowly scoped language edits."""
from pathlib import Path
from lxml import etree as E
import json, sys, re, time
ROOT=Path(__file__).resolve().parents[1]
QA=ROOT/'qa/additions'
ID='{http://www.w3.org/XML/1998/namespace}id'
def find(xid):
    for p in (ROOT/'source').rglob('*'):
        if p.suffix not in {'.xml','.ptx'}: continue
        tree=E.parse(str(p))
        for el in tree.iter():
            if el.get(ID)==xid:return p,el
    raise KeyError(xid)
def opening(xid, reason, new, preserve_embedded=False):
    p,el=find(xid)
    intro=el.find('introduction')
    assert intro is not None,xid
    assert preserve_embedded or all(n.tag=='p' for n in intro), ('Preserve embedded material',xid)
    raw=E.tostring(intro,encoding='unicode',with_tail=False)
    # Locate the original bytes without serializing the rest of the manuscript.
    text=p.read_text('utf-8')
    start=text.index('<introduction>')
    end=text.index('</introduction>',start)+len('</introduction>')
    before=text[start:end]
    kept=''.join(E.tostring(n,encoding='unicode',with_tail=False)
                 for n in intro if n.tag!='p') if preserve_embedded else ''
    replacement='<introduction>'+new.strip()+kept+'</introduction>'
    if before==replacement:return
    E.fromstring(replacement.encode())
    write(p,text[:start]+replacement+text[end:])
    record(p,xid,reason,before,replacement)
def replace(xid,reason,before,after):
    p,el=find(xid)
    text=p.read_text('utf-8')
    if text.count(before)!=1:
        if after in text:return
        pattern=r'\s+'.join(re.escape(w) for w in before.split())
        found=list(re.finditer(pattern,text))
        assert len(found)==1,(xid,before)
        before=found[0].group()
    text=text.replace(before,after)
    E.fromstring(text.encode())
    write(p,text)
    record(p,xid,reason,before,after)
def write(p,text):
    for attempt in range(3):
        try:
            p.write_text(text,encoding='utf-8');return
        except OSError as exc:
            if exc.errno!=22 or attempt==2:raise
            time.sleep(.2)
def record(p,xid,reason,before,after):
    with (QA/'language-changes.jsonl').open('a',encoding='utf-8') as f:
        f.write(json.dumps({'file':str(p.relative_to(ROOT)),'id':xid,'flag':reason,
                            'before':before,'after':after},ensure_ascii=False)+'\n')
def extract(numbers):
    tree=E.parse(str(ROOT/'source/main.ptx'));tree.xinclude()
    chapters=tree.findall('.//chapter')
    for number in numbers:
        chapter=chapters[number-1] if isinstance(number,int) else tree.findall('.//appendix')[ord(number.upper())-65]
        print('\nCHAPTER',number)
        for el in [chapter]+chapter.findall('section'):
            intro=el.find('introduction')
            if intro is None: continue
            for raw in intro.xpath('.//latex-image|.//asymptote|.//description|.//hint'):
                raw.getparent().remove(raw)
            print('\nID:',el.get(ID))
            print('TITLE:',''.join(el.find('title').itertext()))
            for p in intro:
                print(' '.join(''.join(p.itertext()).split()))
if __name__=='__main__':extract([int(n) if n.isdigit() else n for n in sys.argv[1:]])
