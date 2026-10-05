from audit_pretext import assembled,XML_ID
import sys
hints=assembled().findall('.//hint')
a=int(sys.argv[1]);b=int(sys.argv[2])
for i,h in enumerate(hints[a:b],a):
 e=h.getparent();title=e.find('title');print(i,e.get(XML_ID), ' '.join(''.join(title.itertext()).split()) if title is not None else '')
 print('HINT:',' '.join(''.join(h.itertext()).split()))
print('TOTAL',len(hints))
