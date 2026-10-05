"""Validate TeX grouping and repair split substack displays; scan repeated sentences."""
import re, json
from lxml import etree
from audit_edit import ROOT,save,record
issues=[]; repeats=[]
for path in (ROOT/'source').rglob('*.xml'):
    text=path.read_text('utf-8')
    for match in list(re.finditer(r'<md(?:\s[^>]*)?>.*?</md>',text,re.S))[::-1]:
        block=match.group()
        if '\\substack' in block:
            rows=re.findall(r'<mrow[^>]*>(.*?)</mrow>',block,re.S)
            after='<me>'+'\\\\\n'.join(rows)+'</me>'
            # Line breaks inside substack are meaningful; ordinary broken lines
            # surrounding it should be spaces, not extra mathematical rows.
            after=after.replace('\\\\\n','\n')
            after=re.sub(r'(\\substack\{[^{}]*?)\n\s*(i\\text\{)',r'\1\\\\\2',after)
            text=text[:match.start()]+after+text[match.end():]
            record(path,'Reassemble substack arguments split incorrectly into display rows',block,after)
    if text!=path.read_text('utf-8'): save(path,text)
    tree=etree.fromstring(text.encode())
    for node in tree.xpath('//m|//me|//mrow'):
        value=''.join(node.itertext()); level=0
        # An even number of preceding backslashes leaves the brace structural.
        for match in re.finditer(r'(\\*)[{}]',value):
            if len(match.group(1))%2: continue
            level+=1 if match.group()[-1]=='{' else -1
            if level<0: break
        if level: issues.append({'file':str(path.relative_to(ROOT)),'line':node.sourceline,'balance':level,'text':value})
    for node in tree.xpath('//p[not(ancestor::hint)]'):
        value=' '.join(''.join(node.itertext()).split())
        sentences=re.split(r'(?<=[.!?])\s+',value)
        for sentence in set(sentences):
            if len(sentence)>70 and sentences.count(sentence)>1:
                repeats.append({'file':str(path.relative_to(ROOT)),'line':node.sourceline,'sentence':sentence,'count':sentences.count(sentence)})
(ROOT/'qa/audit/math-grouping.json').write_text(json.dumps(issues,indent=2),encoding='utf-8')
(ROOT/'qa/audit/repeated-sentences.json').write_text(json.dumps(repeats,indent=2),encoding='utf-8')
print(json.dumps({'unbalanced_math':issues,'repeated_sentences':repeats},indent=2))
