"""One-time, content-preserving repair of the converted PreTeXt markup.

Uses only source/*.ptx and source/**/*.xml. Does not run the converters or
modify the LaTeX edition. The audit inventory records the before/after state.
"""
from pathlib import Path
from collections import Counter
import json
from lxml import etree as ET

ROOT = Path(__file__).resolve().parents[1]
changes = Counter()


def unwrap(el):
    parent = el.getparent()
    pos = parent.index(el)
    if el.text and el.text.strip():
        raise ValueError('Unexpected text outside blocks')
    for child in list(el):
        parent.insert(pos, child)
        pos += 1
    parent.remove(el)


for path in sorted((ROOT / 'source').rglob('*')):
    if path.suffix not in {'.xml', '.ptx'}:
        continue
    tree = ET.parse(str(path))
    root = tree.getroot()
    before = ET.tostring(tree)
    for el in list(root.iter('strong')):
        if any(a.tag in {'m', 'md', 'me', 'mrow'} for a in el.iterancestors()):
            # A prose XML emphasis tag cannot occur inside TeX math.
            parent = el.getparent()
            s = r'\textbf{' + ''.join(el.itertext()) + '}' + (el.tail or '')
            previous = el.getprevious()
            if previous is None:
                parent.text = (parent.text or '') + s
            else:
                previous.tail = (previous.tail or '') + s
            parent.remove(el)
            changes['math emphasis'] += 1
        else:
            el.tag = 'alert'
            changes['prose emphasis'] += 1
    for el in list(root.iter('md')):
        rows = el.findall('mrow')
        if rows and any(r'\begin{' in ''.join(row.itertext()) for row in rows):
            # The converter split cases/arrays at their internal row separators.
            # They must remain one TeX environment, not separate align rows.
            text = '\\\\\n'.join(''.join(row.itertext()).strip() for row in rows)
            for child in list(el):
                el.remove(child)
            el.text = text
            el.tag = 'me'
            changes['rejoined math environments'] += 1
        elif not rows:
            el.tag = 'me'
            changes['single displays'] += 1
        if el.getparent().tag != 'p':
            parent = el.getparent()
            pos = parent.index(el)
            tail = el.tail
            el.tail = None
            p = ET.Element('p')
            parent.insert(pos, p)
            p.append(el)
            p.tail = tail
            changes['display paragraphs'] += 1
    for el in root.iter():
        if not isinstance(el.tag, str):
            continue
        if el.tag in {'m', 'me', 'md', 'mrow'}:
            if el.text:
                changes['math prime characters'] += el.text.count('\u2019')
                el.text = el.text.replace('\u2019', "'")
        if el.tag == 'example':
            for statement in list(el.findall('statement')):
                unwrap(statement)
                changes['worked example structure'] += 1
    for el in list(root.iter('ol')) + list(root.iter('ul')):
        if el.getparent().tag not in {'p', 'li'}:
            parent = el.getparent()
            pos = parent.index(el)
            tail = el.tail
            el.tail = None
            p = ET.Element('p')
            parent.insert(pos, p)
            p.append(el)
            p.tail = tail
            changes['list paragraphs'] += 1
    for el in root.iter('table'):
        for caption in el.findall('caption'):
            caption.tag = 'title'
            changes['table titles'] += 1
        if el.find('caption') is None:
            title = el.find('title')
            if title is not None:
                pass
            else:
                caption = ET.Element('title')
                context = next((a.find('title') for a in el.iterancestors()
                                if a.find('title') is not None), None)
                caption.text = ' '.join(context.itertext()) if context is not None else 'Values and formulas'
                el.insert(0, caption)
            changes['table captions'] += 1
    # The converter sometimes let a worked example swallow the following
    # theorem/callout. End that example before the next independent block.
    for el in list(root.iter('example')):
        nested = next((c for c in el if c.tag in {'note', 'warning', 'theorem', 'definition'}), None)
        if nested is not None:
            parent = el.getparent()
            pos = parent.index(el) + 1
            rest = list(el)[el.index(nested):]
            for child in rest:
                parent.insert(pos, child)
                pos += 1
            changes['example boundaries'] += 1
    for el in root.iter('figure'):
        images = el.findall('image')
        if len(images) > 1:
            panels = ET.Element('sidebyside', widths=' '.join(['45%'] * len(images)))
            el.insert(el.index(images[0]), panels)
            for image in images:
                image.attrib.pop('width', None)
                panels.append(image)
            changes['multipanel structure'] += 1
    if root.tag in {'section', 'appendix'} and root.findall('subsection'):
        children = list(root)
        first = next(i for i, el in enumerate(children) if el.tag == 'subsection')
        initial = [el for el in children[:first] if el.tag not in {'title', 'introduction'} and isinstance(el.tag, str)]
        if initial:
            intro = ET.Element('introduction')
            root.insert(root.index(initial[0]), intro)
            for el in initial:
                intro.append(el)
            changes['section introductions'] += 1
        children = list(root)
        last = max(i for i, el in enumerate(children) if el.tag == 'subsection')
        final = [el for el in children[last+1:] if el.tag != 'conclusion' and isinstance(el.tag, str)]
        if final:
            end = ET.SubElement(root, 'conclusion')
            for el in final:
                end.append(el)
            changes['section conclusions'] += 1
    if ET.tostring(tree) != before:
        path.write_bytes(ET.tostring(tree, encoding='UTF-8', xml_declaration=True))

(ROOT / 'qa/audit/markup-repairs.json').write_text(json.dumps(changes, indent=2), encoding='utf-8')
print(json.dumps(changes, indent=2))
