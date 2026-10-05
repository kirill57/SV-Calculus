"""One-time repair: paragraph cells are required for PreTeXt column wrapping."""
from lxml import etree as E
from audit_edit import ROOT,save,record
import json,re

changed_sections=[]
tables=0;cells=0
for path in (ROOT/'source').rglob('*'):
    if path.suffix not in {'.xml','.ptx'}:continue
    before=path.read_text('utf-8');tree=E.fromstring(before.encode());changed=False
    for tab in tree.findall('.//tabular'):
        rows=tab.findall('row')
        if not rows:continue
        plain=[''.join(c.xpath('.//text()[not(ancestor::m)]')).strip() for c in tab.findall('.//cell')]
        if not any(len(re.findall(r'[A-Za-z]+',s))>=3 or sum(c.isalpha() for c in s)>=18 for s in plain):continue
        n=max(len(r.findall('cell')) for r in rows)
        if not tab.findall('col'):
            widths=[round(100/n,1)]*n;widths[-1]=round(100-sum(widths[:-1]),1)
            for w in reversed(widths):tab.insert(0,E.Element('col',width=f'{w}%'))
        modified=False
        for c in tab.findall('./row/cell'):
            if c.find('p') is not None or (not (c.text or '').strip() and not len(c)):continue
            p=E.Element('p');p.text=c.text;c.text=None
            for child in list(c):c.remove(child);p.append(child)
            c.append(p);modified=True;cells+=1
        if modified:tables+=1;changed=True
    if changed:
        after=E.tostring(tree,encoding='unicode',pretty_print=True);save(path,after)
        record(path,'Use paragraph cells so specified column widths wrap prose at readable print size',before,after)
        sid=tree.get('{http://www.w3.org/XML/1998/namespace}id')
        if tree.tag=='section':changed_sections.append(sid)
(ROOT/'qa/audit/paragraph-cell-repairs.json').write_text(json.dumps({'tables':tables,'cells':cells,'sections':changed_sections},indent=2),encoding='utf-8')
print('Paragraph cells',cells,'tables',tables,'sections',len(changed_sections))
