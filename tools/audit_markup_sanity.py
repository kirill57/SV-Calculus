"""Check source defects that can survive XML/schema validation."""
from pathlib import Path
from lxml import etree as E
import json, re

ROOT=Path(__file__).resolve().parents[1]
QA=ROOT/'qa/audit-2026-10-17'
ID='{http://www.w3.org/XML/1998/namespace}id'
tree=E.parse(str(ROOT/'source/main.ptx')); tree.xinclude()
ids={e.get(ID):e for e in tree.iter() if e.get(ID)}
unnumbered=[]; raw=[]; spacing=[]
skip={'m','me','men','md','mdn','mrow','macros','latex-image-preamble','latex-image','asymptote','pre','c'}
for e in tree.iter():
    if not isinstance(e.tag,str):continue
    if e.tag=='xref' and not e.get('text') and e.get('ref') in ids:
        if ids[e.get('ref')].tag in {'subsection','paragraphs','introduction'}:
            unnumbered.append({'file':e.base,'line':e.sourceline,'ref':e.get('ref')})
    for text,context in [(e.text,e),(e.tail,e.getparent())]:
        if not text or context is None:continue
        if any(a.tag in skip for a in [context,*context.iterancestors()]):continue
        if re.search(chr(92)*2+r'[A-Za-z]+',text):
            raw.append({'file':e.base,'line':e.sourceline,'text':text.strip()})
for p in (ROOT/'source').rglob('*'):
    if p.suffix not in {'.xml','.ptx'}:continue
    lines=p.read_text('utf-8').splitlines()
    for i,line in enumerate(lines[1:],1):
        if line.strip().startswith('[') and lines[i-1].rstrip().endswith(chr(92)*2):
            if re.match(r'\[[0-9.]+(?:mm|pt|ex|em)\]',line.strip()):
                spacing.append({'file':str(p.relative_to(ROOT)),'line':i+1,'text':line.strip()})
result={'unnumberedReferencesWithoutTitles':unnumbered,'detachedArraySpacing':spacing,
        'rawTexInOrdinaryTextCandidates':raw}
(QA/'markup-sanity.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
assert not unnumbered and not spacing
