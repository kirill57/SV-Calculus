"""Render representative PDF pages for the book's final visual audit."""
from pathlib import Path
import fitz
from PIL import Image, ImageDraw
import json, hashlib

ROOT = Path(__file__).resolve().parents[1]
pdf = ROOT/'output/print/main.pdf'
doc = fitz.open(pdf)
out = ROOT/'qa/audit/print-pages'; out.mkdir(exist_ok=True)
pages = {}

def pick(n, reason):
    if 1 <= n <= len(doc):
        pages.setdefault(n, []).append(reason)

for n in [1,4,5]:
    pick(n, 'Title page and frontmatter')

for level, title, n in doc.get_toc():
    if level == 2:
        pick(n, 'Chapter or appendix opening: '+title)
    if title in ['Calculus without limits: finite differences and finite sums',
                 'Models before calculus', 'Chapter review and applications',
                 'Simpson’s Rule', "Simpson's Rule"]:
        pick(n, title)
    if title=='Numerical integration rules':
        for k in range(n,n+3):pick(k, 'Quadrature reference tables')

terms = ['Piecewise motion', 'Power-law scaling', 'Models and calculus',
         'Finite sums: ', 'Quantities measured by integrals',
         'Common mistakes with rectangular sums', 'rotating the upper semicircle',
         'The spikes for', 'The sphere is built', 'Newton map', 'Simple Python experiments',
         'a full distance function', 'true error', 'direction fields',
         'numbers as points and distances', 'signature behavior',
         'Where are equilibria, and are they stable?']
for term in terms:
    for i, page in enumerate(doc):
        if i>=12 and term.lower() in ' '.join(page.get_text().lower().split()):
            pick(i+1, 'Changed material: '+term)
            break

manifest = []
for n, reasons in sorted(pages.items()):
    name = f'p{n:04}.png'
    doc[n-1].get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False).save(out/name)
    manifest.append({'page': n, 'file':str((out/name).relative_to(ROOT)), 'reasons':reasons})

for start in range(0, len(manifest), 12):
    group=manifest[start:start+12]
    sheet=Image.new('RGB',(1600,1950),'#ddd'); draw=ImageDraw.Draw(sheet)
    for j, entry in enumerate(group):
        im=Image.open(ROOT/entry['file']); im.thumbnail((385,605))
        x=(j%4)*400+(400-im.width)//2; y=(j//4)*650+32
        sheet.paste(im,(x,y)); draw.text(((j%4)*400+10,(j//4)*650+10),f"PDF page {entry['page']}",fill='black')
    sheet.save(out/f'contact-{start//12+1:02}.png')

result={'pdf':str(pdf.relative_to(ROOT)), 'sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
        'pages':len(doc), 'renderedPages':manifest, 'visualReview':'pending'}
(ROOT/'qa/audit/print-visual-review.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print('Rendered pages:',len(manifest))
