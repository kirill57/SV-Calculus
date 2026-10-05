"""Corrections checked during the audit of Chapters 1--3."""
from audit_edit import replace, record, ROOT
from lxml import etree as ET
import re

replace('chapters/ch02*/sections/sec-2-7-*.xml',
        'The smallest such positive <m>T</m>, when it exists, is called the <em>period</em>.',
        'The smallest such positive <m>T</m>, when it exists, is called the <em>period</em>. The period formulas below assume <m>A\\neq0</m>; when <m>A=0</m>, the function is constant and has no smallest positive period.',
        'State the nonzero-amplitude assumption in period formulas')
replace('chapters/ch02*/sections/sec-2-6-*.xml',
        'multiplying the input by <m>k</m> multiplies the output by <m>k^p</m>:',
        'for <m>x&gt;0</m> and <m>k&gt;0</m>, multiplying the input by <m>k</m> multiplies the output by <m>k^p</m>:',
        'Restrict the scaling law for arbitrary real powers to positive inputs')
replace('chapters/ch02*/sections/sec-2-7-*.xml',
        '<p>This is exponential growth.</p>',
        '<p>This is exponential growth. These are values of a continuous population model, rather than exact counts of individual bacteria; fractional values represent an approximation to the population.</p>',
        'Explain fractional values in the bacterial-population model')
replace('chapters/ch02*/sections/sec-2-2-*.xml',
        'A limiting process is a promise that approximations have a destination. Completeness says that, for the real line, the destination exists.',
        'A convergent limiting process has a destination. Completeness guarantees a real destination when the approximations satisfy appropriate conditions, such as nested closed intervals whose lengths shrink to zero, or a bounded monotone sequence. It does not make every sequence converge.',
        'Completeness does not imply that all limiting processes converge')
replace('chapters/ch03*/sections/sec-3-8-*.xml',
        'is a sequence.  If those slopes settle toward one number, the graph is telling us its instantaneous rate of change.</p>\n\n  <p>That number will be the derivative.',
        'is a sequence. If the derivative exists, these slopes converge to it. Convergence of this one sequence alone does not establish a derivative: for <m>f(x)=|x|</m> at <m>a=0</m>, these slopes are all <m>1</m>, while negative steps give slope <m>-1</m>.</p>\n\n  <p>A derivative requires the same limit as <m>h</m> approaches zero through all allowed nonzero steps, not just <m>h=1/n</m>.',
        'Convergence along one sequence of secants does not establish differentiability')

path=next((ROOT/'source').glob('chapters/ch03*/sections/sec-3-6-*.xml'))
tree=ET.parse(str(path)); el=tree.xpath('//theorem[title="Idea of the proof of the Intermediate Value Theorem"]')[0]
el.tag='note'; statement=el.find('statement'); i=list(el).index(statement)
for child in list(statement): el.insert(i,child); i+=1
el.remove(statement)
p=el.xpath('p[m="h(a)"]')[0] if el.xpath('p[m="h(a)"]') else el.findall('p')[2]
# Insert the termination case before the interval iteration.
p.text='If an endpoint or a midpoint has value zero, we have already found the desired point. Otherwise, if '
tree.write(str(path),encoding='utf-8',xml_declaration=True)
record(path,'Treat the IVT proof sketch as a note and include the bisection termination case','Proof sketch labeled as a separate theorem','Proof sketch note; stop on an exact zero')

# Recover literal subsubsection headings left behind by the import.
count=0
for path in (ROOT/'source').rglob('*.xml'):
    tree=ET.parse(str(path)); changed=False
    for heading in list(tree.xpath('//p[starts-with(text(), "\\subsubsection*{")]')):
        combined=''.join(heading.itertext())
        if not re.fullmatch(r'\\subsubsection\*\{.*\}', combined, re.S): continue
        parent=heading.getparent(); position=parent.index(heading)
        group=ET.Element('paragraphs'); title=ET.SubElement(group,'title')
        title.text=(heading.text or '')[len('\\subsubsection*{'):]
        for child in list(heading): title.append(child)
        if len(title): title[-1].tail=(title[-1].tail or '').removesuffix('}')
        else: title.text=(title.text or '').removesuffix('}')
        parent.replace(heading,group)
        while len(parent)>position+1:
            sibling=parent[position+1]
            if sibling.tag=='p' and ''.join(sibling.itertext()).startswith('\\subsubsection*{'): break
            group.append(sibling)
        count+=1; changed=True
    if changed:
        tree.write(str(path),encoding='utf-8',xml_declaration=True)
        record(path,'Convert leaked LaTeX review headings to PreTeXt paragraph groups','Literal subsubsection commands','Titled paragraph groups preserving the review problems')
print('Converted headings:',count)
