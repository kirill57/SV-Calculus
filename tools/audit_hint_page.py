from pathlib import Path
from lxml import html
ROOT=Path(__file__).resolve().parents[1]
web=ROOT/'output/web'
first=next(web.glob('sec-1-1-*.html'));doc=html.parse(str(first));head=doc.find('head');body=html.Element('body');count=0
for path in sorted(web.glob('sec-*.html')):
 d=html.parse(str(path))
 for h in d.xpath('//details[contains(concat(" ",normalize-space(@class)," ")," hint ")]'):
  h.set('open','open');body.append(h);count+=1
page=html.Element('html');head.insert(0,html.Element('base',href='/output/web/'));page.append(head);page.append(body)
(ROOT/'qa/audit/hints-render.html').write_bytes(html.tostring(page,encoding='utf-8',method='html'));print('HINTS',count)
