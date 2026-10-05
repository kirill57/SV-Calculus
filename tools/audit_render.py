"""Render every SVG actually referenced by the book into review contact sheets."""
from pathlib import Path
from collections import defaultdict
from lxml import etree as ET
from lxml import html
from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright
import json
import math
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'qa/audit/figures'
OUT.mkdir(parents=True, exist_ok=True)
tree = ET.parse(str(ROOT / 'source/main.ptx'))
tree.xinclude()
groups = defaultdict(list)
missing = []
for division in tree.findall('.//chapter') + tree.findall('.//appendix'):
    xid = division.get('{http://www.w3.org/XML/1998/namespace}id')
    group = xid.split('-')[0]
    for section in division.findall('section'):
        sid = section.get('{http://www.w3.org/XML/1998/namespace}id')
        path = ROOT / 'output/web' / (sid + '.html')
        if not path.exists():
            missing.append(str(path))
            continue
        doc = html.parse(str(path))
        for src in doc.xpath('//img/@src'):
            if not src.startswith('generated/'):
                continue
            asset = ROOT / 'output/web' / src
            if not asset.exists():
                missing.append(str(asset))
            elif asset not in groups[group]:
                groups[group].append(asset)
font = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 16)
manifest = []
with sync_playwright() as pw:
    browser = pw.chromium.launch(channel='msedge')
    page = browser.new_page(viewport={'width': 900, 'height': 750}, device_scale_factor=2)
    for group, assets in groups.items():
        for batch in range(math.ceil(len(assets)/16)):
            subset = assets[batch*16:(batch+1)*16]
            sheet = Image.new('RGB', (2200, 1720), 'white')
            draw = ImageDraw.Draw(sheet)
            for j, asset in enumerate(subset):
                page.goto(asset.as_uri())
                page.locator('svg').evaluate("el => { el.style.background='white'; }")
                png = OUT / (asset.stem + '.png')
                page.locator('svg').screenshot(path=str(png))
                tile = Image.open(png).convert('RGB')
                tile.thumbnail((535, 355))
                x, y = (j%4)*550, (j//4)*430
                sheet.paste(tile, (x+(550-tile.width)//2, y+8))
                label = asset.stem
                label_lines = re.findall('.{1,58}', label)
                for k, line in enumerate(label_lines[:3]):
                    draw.text((x+8,y+365+k*18), line, fill='black', font=font)
                manifest.append({'group':group, 'asset':str(asset.relative_to(ROOT)),
                                 'sheet': f'{group}-{batch+1}.png', 'tile':j+1})
            dest = OUT / f'{group}-{batch+1}.png'
            sheet.save(dest)
            print(dest.name, len(subset), flush=True)
    browser.close()
(OUT.parent / 'figure-manifest.json').write_text(json.dumps({'images':manifest,'missing':missing},indent=2),encoding='utf-8')
print('IMAGES',len(manifest),'MISSING',len(missing),flush=True)
