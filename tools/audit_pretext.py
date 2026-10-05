"""Read-only structural checks and review extracts for the PreTeXt edition.

Run ``python tools/audit_pretext.py`` for the full source inventory, or
``python tools/audit_pretext.py read 6`` for chapter 6 without drawing code.
The original LaTeX edition is only hashed, never rewritten.
"""
from pathlib import Path
from collections import Counter
import argparse
import hashlib
import json
import re
from lxml import etree as ET

ROOT = Path(__file__).resolve().parents[1]
XML_ID = '{http://www.w3.org/XML/1998/namespace}id'
QA = ROOT / 'qa' / 'audit'


def assembled():
    tree = ET.parse(str(ROOT / 'source/main.ptx'))
    tree.xinclude()
    return tree


def inventory():
    tree = assembled()
    counts = Counter(e.tag for e in tree.iter() if isinstance(e.tag, str))
    ids, errors = {}, []
    for e in tree.iter():
        if not isinstance(e.tag, str):
            continue
        xid = e.get(XML_ID)
        if xid:
            if xid in ids:
                errors.append(f'duplicate id: {xid}')
            ids[xid] = e
        if e.tag in {'me', 'men', 'md', 'mdn'} and e.getparent().tag != 'p':
            errors.append(f'display outside p: {e.base}:{e.sourceline}')
        if e.tag in {'md', 'mdn'} and not e.findall('mrow'):
            errors.append(f'md without mrow: {e.base}:{e.sourceline}')
        if e.tag == 'image' and not (e.get('source') or len(e)):
            errors.append(f'empty image: {e.base}:{e.sourceline}')
    for e in tree.findall('.//xref'):
        for ref in re.split(r'[,\s]+', e.get('ref', '')):
            if ref and ref not in ids:
                errors.append(f'unresolved xref: {ref}')
    files = sorted(p for p in (ROOT / 'source').rglob('*') if p.suffix in {'.xml', '.ptx'})
    original = ROOT / 'Single_Variable_Calculus_Change__Accumulation__and_Approximation'
    hashes = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
              for p in original.rglob('*') if p.is_file()}
    figures = []
    for e in tree.findall('.//figure'):
        figures.append({'id': e.get(XML_ID), 'file': str(e.base), 'line': e.sourceline,
                        'caption': ' '.join(e.find('caption').itertext()).strip() if e.find('caption') is not None else '',
                        'images': len(e.findall('.//image'))})
    result = {'source_files': len(files), 'counts': dict(counts), 'errors': errors,
              'original_edition_sha256': hashes, 'figures': figures}
    QA.mkdir(parents=True, exist_ok=True)
    (QA / 'inventory.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    tree.write(str(QA / 'assembled.xml'), encoding='utf-8', xml_declaration=True)
    # XInclude inserts xml:base attributes for locating source files. Those are
    # assembly metadata, not author markup, and the schema must not see them.
    for e in tree.iter():
        e.attrib.pop('{http://www.w3.org/XML/1998/namespace}base', None)
    tree.write(str(QA / 'schema-input.xml'), encoding='utf-8', xml_declaration=True)
    print(json.dumps({'source_files': len(files), 'counts': dict(counts),
                      'errors': len(errors), 'error_examples': errors[:8]}, indent=2))
    return bool(errors)


def read(chapter, part=None, limit=None):
    tree = assembled()
    nodes = tree.findall('.//chapter') if chapter.isdigit() else tree.findall('.//appendix')
    node = nodes[int(chapter)-1] if chapter.isdigit() else nodes[ord(chapter.upper())-65]
    # Render every text and formula, omitting only raw drawing code and repetitive hints.
    # Exercises and all worked examples remain in this extract.
    for e in node.xpath('.//latex-image | .//asymptote | .//hint'):
        e.getparent().remove(e)
    units = [node.find('introduction')] + node.findall('section')
    if part is not None:
        units = units[part:part + (limit or 1)]
    for unit in units:
        if unit is None:
            continue
        print('\nFILE', unit.base, 'ID', unit.get(XML_ID, 'introduction'))
        for e in unit.iter():
            if not isinstance(e.tag, str):
                continue
            if e.tag in {'title', 'p', 'me', 'md', 'mrow', 'caption', 'cell', 'pre'}:
                if e.tag == 'p' and (e.find('ol') is not None or e.find('ul') is not None):
                    continue
                # p already includes its math children; mrow is emitted only for bare md.
                if e.tag in {'me', 'md', 'mrow'} and any(a.tag == 'p' for a in e.iterancestors()):
                    continue
                if e.tag == 'mrow' and e.getparent().tag == 'md':
                    continue
                text = ' '.join(''.join(e.itertext()).split())
                if text:
                    print(('TITLE: ' if e.tag == 'title' else 'FIGURE: ' if e.tag == 'caption' else '') + text)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('mode', nargs='?', default='inventory', choices=['inventory', 'read'])
    ap.add_argument('chapter', nargs='?', default='1')
    ap.add_argument('--part', type=int)
    ap.add_argument('--limit', type=int)
    args = ap.parse_args()
    if args.mode == 'read':
        read(args.chapter, args.part, args.limit)
    else:
        raise SystemExit(inventory())
