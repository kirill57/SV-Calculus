"""Repair remaining TeX leaked into prose and tables by the importer."""
from lxml import etree as ET
from audit_edit import ROOT,record,replace
import re

# A row splitter mistook the line breaks inside substack for table rows.
path=next((ROOT/'source').glob('appendices/appF*/sections/sec-f-5-*.xml'))
tree=ET.parse(str(path)); table=tree.xpath('//table')[0].find('tabular')
rows=list(table); row=rows[5]
for child in list(row): row.remove(child)
ET.SubElement(row,'cell').text='Simpson’s rule'
cell=ET.SubElement(row,'cell'); cell.text='For even '
m=ET.SubElement(cell,'m'); m.text='n'; m.tail=', '
m=ET.SubElement(cell,'m'); m.text=r'\displaystyle S_n=\frac{\Delta x}{3}\left[f(x_0)+4\sum_{\substack{1\le j\le n-1\\j\text{ odd}}}f(x_j)+2\sum_{\substack{2\le j\le n-2\\j\text{ even}}}f(x_j)+f(x_n)\right].'
ET.SubElement(row,'cell').text='Parabolic arcs'
for extra in rows[6:]: table.remove(extra)
path.write_bytes(ET.tostring(tree,encoding='utf-8',xml_declaration=True))
record(path,'Restore the Simpson formula split into three broken table rows','Three malformed rows','One complete Simpson row with a correctly grouped substack')

skip={'m','me','men','md','mdn','mrow','latex-image','asymptote','code','pre','macros','latex-image-preamble','latex-preamble'}
pat=re.compile(r'\\\[([\s\S]*?)\\\]|\\texttt\{([^{}]*)\}|\\(?:subparagraph|paragraph)\{([^{}]*)\}')
for path in (ROOT/'source').rglob('*'):
    if path.suffix not in {'.xml','.ptx'}: continue
    tree=ET.parse(str(path)); changed=False
    for el in list(tree.iter()):
        if not isinstance(el.tag,str): continue
        if el.tag in {'m','me','men','mrow'} and el.text:
            new=re.sub(r'([A-Za-z])”',r"\1''",el.text)
            if new!=el.text: el.text=new; changed=True
        for attr in ['text','tail']:
            value=getattr(el,attr)
            if not value: continue
            ancestors=[el]+list(el.iterancestors()) if attr=='text' else list(el.iterancestors())
            if any(a.tag in skip for a in ancestors): continue
            cleaned=re.sub(r'\\(?:begin|end)\{center\}|\\label\{[^{}]*\}|\[4mm\]\s*\\hline','',value)
            cleaned=cleaned.replace(r'\newline',' ').replace(r'\Computing',' Computing')
            if cleaned!=value: setattr(el,attr,cleaned); changed=True
            value=cleaned; matches=list(pat.finditer(value))
            if not matches: continue
            parent=el if attr=='text' else el.getparent()
            position=0 if attr=='text' else parent.index(el)+1
            setattr(el,attr,value[:matches[0].start()])
            for i,match in enumerate(matches):
                tag='m' if match.group(1) is not None else ('c' if match.group(2) is not None else 'alert')
                node=ET.Element(tag); node.text=next(g for g in match.groups() if g is not None).strip()
                node.tail=value[match.end():matches[i+1].start() if i+1<len(matches) else len(value)]
                parent.insert(position,node); position+=1
            changed=True
    for p in list(tree.xpath('//p')):
        if not len(p) and not (p.text or '').strip(): p.getparent().remove(p); changed=True
    if changed:
        path.write_bytes(ET.tostring(tree,encoding='utf-8',xml_declaration=True))
        record(path,'Convert leaked TeX in prose and tables to PreTeXt','Raw commands, display delimiters, or curly derivative quotes','Native inline math, code, and emphasized headings')

replace('chapters/ch16*/sections/sec-16-4-*.xml','<title>\\cos x</title>','<title>Early Maclaurin polynomials</title>',
        'Give the shared exponential, sine, and cosine table a descriptive title')
replace('chapters/ch11*/sections/sec-11-3-*.xml','Two ways to return from  \\theta','Two ways to return from <m>\\theta</m>',
        'Put the angle symbol in title math')
replace('chapters/ch12*/sections/sec-12-3-*.xml','Example: Simpson’s Rule for  \\int_0^1 e^{-x^2}\\,dx',
        'Example: Simpson’s Rule for <m>\\int_0^1 e^{-x^2}\\,dx</m>',
        'Render the integral in the example title')
replace('chapters/ch12*/sections/sec-12-6-*.xml','Experiment 1: approximate  \\pi  by integration',
        'Experiment 1: approximate <m>\\pi</m> by integration','Render pi as mathematics in the experiment title')
