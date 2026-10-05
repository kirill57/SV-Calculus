"""Render every page of the added material, plus all chapter openings."""
from pathlib import Path
import hashlib, json
import fitz
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / 'output/print/main.pdf'
OUT = ROOT / 'qa/additions/print-pages'
OUT.mkdir(parents=True, exist_ok=True)
doc = fitz.open(PDF)
texts = [' '.join(p.get_text().lower().split()) for p in doc]
toc = doc.get_toc()
pages = {}

def pick(n, reason):
    pages.setdefault(n, []).append(reason)

def locate(term, lo=20):
    hits = [i + 1 for i, text in enumerate(texts) if i >= lo and term.lower() in text]
    assert hits, term
    return hits[0]

# Full subsection ranges include their concluding exercise and hint.
core = [
    ('Inverse hyperbolic functions: branches and derivatives', 'Why hyperbolic functions appear in hanging cables', None),
    ('Integrals and inverse hyperbolic functions', None, 2),
    ('Absolute and conditional convergence', None, 3),
    ('The Cauchy criterion: convergence without knowing the limit', 'Recursive sequences and fixed points', None),
    ('The Cauchy criterion for series', None, 1),
    ("Dirichlet’s and Abel’s tests: controlled cancellation", 'Strategy for testing series', None),
]
for title, ending, count in core:
    # PDF punctuation may be extracted as ASCII or a replacement glyph.
    variants = [title, title.replace('’', "'"), title.replace('’', '�')]
    hits = [i+1 for i,t in enumerate(texts) if any(v.lower() in t for v in variants)]
    hits = [n for n in hits if n > 20]
    assert hits, title
    start = hits[0]
    if count is not None:
        end = start + count - 1
    else:
        tail = [i+1 for i,t in enumerate(texts) if i+1 >= start and ending.lower() in t]
        assert tail, ending
        end = tail[0]
    for n in range(start, end+1):
        pick(n, title)

for j, (level, title, start) in enumerate(toc):
    if title.startswith('Additional topics:'):
        end = next(n for lev, t, n in toc[j+1:] if lev <= level) - 1
        for n in range(start, end+1):
            pick(n, title)
    if level == 2:
        pick(start, 'Chapter or appendix opening: ' + title)
    if level == 3 and 'Rolle' in title and 'Mean Value' in title:
        pick(start, 'Revised Mean Value Theorem introduction')

for n in [1, 4, 5, locate('Jump discontinuity: unequal one-sided limits')]:
    pick(n, 'Frontmatter or revised Section 3.7')

manifest = []
for n, reasons in sorted(pages.items()):
    name = f'p{n:04}.png'
    doc[n-1].get_pixmap(matrix=fitz.Matrix(1.75, 1.75), alpha=False).save(OUT/name)
    manifest.append({'page': n, 'file': str((OUT/name).relative_to(ROOT)), 'reasons': reasons})

for start in range(0, len(manifest), 8):
    group = manifest[start:start+8]
    sheet = Image.new('RGB', (1800, 1400), '#ddd')
    draw = ImageDraw.Draw(sheet)
    for j, row in enumerate(group):
        im = Image.open(ROOT/row['file'])
        im.thumbnail((440, 650))
        x = j%4*450+(450-im.width)//2
        y = j//4*700+35
        sheet.paste(im, (x,y))
        draw.text((j%4*450+10,j//4*700+10), f"PDF page {row['page']}", fill='black')
    sheet.save(OUT/f'contact-{start//8+1:02}.png')

result = {'pdf': str(PDF.relative_to(ROOT)), 'sha256': hashlib.sha256(PDF.read_bytes()).hexdigest(),
          'pages': len(doc), 'renderedPages': manifest, 'visualReview': 'pending'}
(ROOT/'qa/additions/print-visual-review.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
print('Rendered', len(manifest), 'pages')
