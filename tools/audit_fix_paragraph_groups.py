"""Flatten nested paragraph groups while retaining their visible headings."""
from lxml import etree as ET
from audit_edit import ROOT,record
for path in (ROOT/'source').rglob('*.xml'):
    tree=ET.parse(str(path)); changed=False
    for el in reversed(tree.xpath('//paragraphs[parent::paragraphs or ancestor::example]')):
        parent=el.getparent(); pos=parent.index(el)
        title=el.find('title')
        if title is not None:
            p=ET.Element('p'); alert=ET.SubElement(p,'alert'); alert.text=title.text
            for child in list(title): alert.append(child)
            parent.insert(pos,p); pos+=1; el.remove(title)
        for child in list(el): parent.insert(pos,child); pos+=1
        parent.remove(el); changed=True
    if changed:
        path.write_bytes(ET.tostring(tree,encoding='utf-8',xml_declaration=True))
        record(path,'Avoid unsupported nested paragraph groups','Nested paragraphs','Inner headings retained as emphasized paragraphs')
