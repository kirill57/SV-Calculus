"""Remove repeated generated reference labels and finish two heading refinements."""
from pathlib import Path
import re
from lxml import etree as E
from language_audit import ROOT, record, write, opening, replace

ID = '{http://www.w3.org/XML/1998/namespace}id'
for p in (ROOT/'source').rglob('*'):
    if p.suffix not in {'.xml', '.ptx'}:
        continue
    text = p.read_text('utf-8')
    matches = list(re.finditer(r'(?:Chapter|Section|Figure|Theorem|Appendix|Example) (<xref\b[^>]*/>)', text, re.I))
    if not matches:
        continue
    xid = E.parse(str(p)).getroot().get(ID)
    for m in reversed(matches):
        before, after = m.group(), m.group(1)
        text = text[:m.start()]+after+text[m.end():]
        record(p, xid, 'Use the generated reference label once; title references already name the linked subsection.', before, after)
    write(p, text)

opening('sec-6-3-rolle-s-theorem-and-the-mean-value-theorem',
        'Explain what each theorem establishes, then give the motion example directly.',
        r'''<p>Rolle’s Theorem combines the existence of absolute extrema with the zero-derivative condition at an interior extremum. The Mean Value Theorem extends the result to unequal endpoint values.</p>
<p>For example, a car moving from mile marker <m>10</m> at noon to mile marker <m>160</m> at <m>3{:}00</m> has average velocity</p>
<p><me>\frac{160-10}{3-0}=50</me></p>
<p>miles per hour. If its position is continuous throughout the trip and its velocity exists between the endpoint times, then at some instant its velocity is</p>
<p><me>50\text{ miles per hour}.</me></p>
<p>The car’s velocity may vary during the trip. The Mean Value Theorem guarantees an instant when it equals the average velocity.</p>''')
replace('sec-3-9-chapter-review-and-discovery-problems',
        'Name the mathematical topic instead of using an editorial label.',
        '<title>End-of-chapter hook</title>', '<title>The derivative as a limit</title>')
