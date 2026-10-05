"""Repair plot clipping and geometric reflection scale in PreTeXt only."""
from audit_edit import replace,ROOT,record
from lxml import etree as ET

replace('docinfo.ptx','clip=false,','clip=true,\n        clip mode=individual,',
        'Clip plot curves to the chosen window while leaving annotation nodes visible')
replace('docinfo.ptx','  <directories external="../assets"/>\n','',
        'Remove the duplicate external directory setting already supplied in publication')
ids=['fig-square-inverse','fig-inverse-slopes-reciprocal','fig-x-cubed-inverse-vertical','fig-arcsin-reflection']
for path in (ROOT/'source').rglob('*.xml'):
    tree=ET.parse(str(path)); changed=False
    for fig in tree.xpath('//figure'):
        if fig.get('{http://www.w3.org/XML/1998/namespace}id') not in ids: continue
        for drawing in fig.findall('.//latex-image'):
            if '\\begin{axis}[' in (drawing.text or '') and 'axis equal image' not in drawing.text:
                drawing.text=drawing.text.replace('\\begin{axis}[','\\begin{axis}[\n    axis equal image,')
                changed=True
    if changed:
        path.write_bytes(ET.tostring(tree,encoding='utf-8',xml_declaration=True))
        record(path,'Use equal coordinate-unit lengths for inverse reflection diagrams','Unequal axis units','Equal axis units for reflection across y=x')

replace('chapters/ch04*/sections/sec-4-4-*.xml','ytick={2.025},','ytick={2.025},\n    yticklabels={\\(2.025\\)},',
        'Do not round the linearization height tick from 2.025 to 2.03')
