"""Put the inverse derivative result before its first use for logarithms."""
from lxml import etree as ET
from audit_edit import ROOT,record

p7=next((ROOT/'source').glob('chapters/ch05*/sections/sec-5-7-*.xml'))
p6=next((ROOT/'source').glob('chapters/ch05*/sections/sec-5-6-*.xml'))
t7=ET.parse(str(p7)); t6=ET.parse(str(p6))
note=t7.xpath('//note[title="Derivative of an inverse function"]')[0]
parent=note.getparent(); start=parent.index(note)
stop=next(i for i in range(start+1,len(parent)) if parent[i].tag=='exercise')
blocks=list(parent)[start:stop]
target=t6.xpath('//subsection[title="The derivative of \\ln x"]')[0]
group=ET.Element('paragraphs'); ET.SubElement(group,'title').text='The inverse derivative rule'
intro=ET.SubElement(group,'p')
intro.text='Before differentiating the logarithm, we need a rule for reversing a function. A continuous strictly monotone function on an interval has a continuous inverse: points on either side of an input have outputs on either side of its output, so trapping the output traps the inverse input.'
for block in blocks: group.append(block)
target.insert(1,group)
recall=ET.Element('p'); recall.text='The inverse derivative rule proved in the preceding section gives '
math=ET.SubElement(recall,'m'); math.text="(f^{-1})'(b)=1/f'(a)"; math.tail=' when '
math=ET.SubElement(recall,'m'); math.text='b=f(a)'; math.tail=' and '
math=ET.SubElement(recall,'m'); math.text="f'(a)\\neq0"; math.tail=' for a differentiable strictly monotone function on an interval.'
parent.insert(start,recall)
for path,tree in [(p6,t6),(p7,t7)]:
    path.write_bytes(ET.tostring(tree,encoding='utf-8',xml_declaration=True))
    record(path,'Prove inverse differentiability before differentiating the logarithm','Inverse rule first proved in Section 5.7','Existing inverse rule and proof moved to Section 5.6 before logarithms')

# The product warning had used differentials as though they were exact finite changes.
from audit_edit import replace
replace('chapters/ch05*/sections/sec-5-9-*.xml',
        'In differential notation,',
        'For exact finite changes, write <m>\\Delta f=f(x+\\Delta x)-f(x)</m> and <m>\\Delta g=g(x+\\Delta x)-g(x)</m>. Then',
        'Distinguish exact product changes from differentials')
replace('chapters/ch05*/sections/sec-5-9-*.xml',
        'd(fg) = (f+df)(g+dg)-fg.',
        '\\Delta(fg) = (f+\\Delta f)(g+\\Delta g)-fg.',
        'Use finite increments in the exact product identity')
replace('chapters/ch05*/sections/sec-5-9-*.xml',
        'd(fg)=f\\,dg+g\\,df+df\\,dg.',
        '\\Delta(fg)=f\\,\\Delta g+g\\,\\Delta f+\\Delta f\\,\\Delta g.',
        'A differential product has no quadratic corner term')
replace('chapters/ch05*/sections/sec-5-9-*.xml',
        'The term <m>df\\,dg</m> is much smaller than the first-order terms when the change is tiny.  Dividing by <m>dx</m> and passing to the limit gives',
        'For differentiable factors, <m>\\Delta f\\,\\Delta g</m> divided by <m>\\Delta x</m> approaches zero. Dividing the exact identity by <m>\\Delta x</m> and passing to the limit gives',
        'Use the correct limiting argument for the product corner term')
