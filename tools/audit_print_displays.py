"""One-time semantic repairs for prose set as oversized display mathematics."""
from lxml import etree as E
import re
from audit_edit import ROOT, save, record


def add_text(e, text):
    if len(e):
        e[-1].tail = (e[-1].tail or '') + text
    else:
        e.text = (e.text or '') + text


def prose(e, text):
    for token in re.split(r'(\\\(.*?\\\)|\\(?:longrightarrow|Longrightarrow|Rightarrow)\b)', text, flags=re.S):
        if token.startswith(r'\('):
            E.SubElement(e, 'm').text = token[2:-2]
        elif token.startswith('\\'):
            E.SubElement(e, 'm').text = token
        else:
            add_text(e, token)


def cell_content(cell, tex):
    """Retain math, and allow the prose parts of comparison tables to wrap."""
    for part in re.split(r'(\\(?:text|textbf)\{[^{}]*\})', tex):
        m = re.fullmatch(r'\\(text|textbf)\{([^{}]*)\}', part, re.S)
        if m:
            if m[1] == 'textbf':
                prose(E.SubElement(cell, 'em'), m[2])
            else:
                prose(cell, m[2])
        elif part.strip():
            E.SubElement(cell, 'm').text = part.strip()


specs = [
    ('piecewise behavior', 'Piecewise motion', [48, 52]),
    ('doubling input', 'Power-law scaling', [35, 30, 35]),
    ('least-time paths', 'Models and calculus', [28, 42, 30]),
    ('what changes?', 'Related rates and optimization', [27, 35, 38]),
    ('forgetting units', 'Common mistakes with rectangular sums', [48, 52]),
    ('accumulated height divided', 'Quantities measured by integrals', [30, 33, 37]),
]
counts = {'prose': 0, 'tables': 0, 'comparisons': 0}
for path in (ROOT/'source').rglob('*'):
    if path.suffix not in {'.xml', '.ptx'}:
        continue
    before = path.read_text('utf-8')
    tree = E.fromstring(before.encode())
    changed = False
    for e in list(tree.findall('.//me')):
        tex = (e.text or '').strip()
        remaining = re.sub(r'\\text\{[^{}]*\}', '', tex)
        remaining = re.sub(r'\\(?:quad|qquad|longrightarrow|Longrightarrow|Rightarrow)\b', '', remaining)
        plain = re.sub(r'\\text\{([^{}]*)\}', lambda m: m[1], tex)
        if r'\text{' in tex and '\\' not in remaining and not any(c in remaining for c in '{}_^') and len(plain) > 80:
            plain = re.sub(r'\\(?:quad|qquad)\b', ' ', plain)
            plain = ' '.join(plain.split())
            em = E.Element('em')
            prose(em, plain)
            em.tail = e.tail
            e.getparent().replace(e, em)
            changed = True
            counts['prose'] += 1
            continue
        for key, title, widths in specs:
            if key not in tex or r'\begin{array}' not in tex:
                continue
            p = e.getparent()
            assert p.tag == 'p' and len(p) == 1 and not (p.text or '').strip()
            array = re.fullmatch(r'\\begin\{array\}\{[^}]+\}(.*?)\\end\{array\}', tex, re.S)
            assert array, tex
            body = array[1].replace(r'\hline', '')
            body = re.sub(r'\[\d+mm\]', '', body)
            rows = [r.strip() for r in re.split(r'\\\\', body) if r.strip()]
            table = E.Element('table')
            E.SubElement(table, 'title').text = title
            tabular = E.SubElement(table, 'tabular', width='100%', halign='left')
            for width in widths:
                E.SubElement(tabular, 'col', width=f'{width}%')
            for rowtex in rows:
                cells = rowtex.split(r'\amp')
                assert len(cells) == len(widths), cells
                row = E.SubElement(tabular, 'row')
                for celltex in cells:
                    cell_content(E.SubElement(row, 'cell'), celltex.strip())
            table.tail = p.tail
            p.getparent().replace(p, table)
            changed = True
            counts['tables'] += 1
            break
        else:
            if 'matched positive' in tex:
                # Give both columns their own full-width line rather than shrinking formulas.
                body = re.fullmatch(r'\\begin\{array\}\{[^}]+\}(.*?)\\end\{array\}', tex, re.S)[1]
                body = body.replace(r'\hline', '')
                body = re.sub(r'\[\d+mm\]', '', body)
                rows = [r.strip() for r in re.split(r'\\\\', body) if r.strip()][1:]
                p = e.getparent()
                assert p.tag == 'p' and len(p) == 1
                block = E.Element('ol')
                for row in rows:
                    left, right = row.split(r'\amp')
                    li = E.SubElement(block, 'li')
                    for name, content in [('Finite sums: ', left), ('Integrals: ', right)]:
                        pp = E.SubElement(li, 'p'); E.SubElement(pp, 'em').text = name
                        # Formulas can occupy the full text width, while sentences wrap.
                        if re.fullmatch(r'\s*\\text\{[^{}]*\}\s*', content):
                            cell_content(pp, content.strip())
                        else:
                            E.SubElement(pp, 'me').text = content.strip()
                block.tail = p.tail; p.getparent().replace(p, block)
                changed = True; counts['comparisons'] += 1
    if changed:
        after = E.tostring(tree, encoding='unicode', pretty_print=True)
        save(path, after)
        record(path, 'Make long prose displays and comparison arrays wrap in print without dropping words or formulas', before, after)
print(counts)
