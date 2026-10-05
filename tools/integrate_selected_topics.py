"""Add navigation and summary links for the new material."""
from pathlib import Path
from lxml import etree as E
import json
ROOT=Path(__file__).resolve().parents[1]
changes=json.loads((ROOT/'qa/additions/changed-source.json').read_text('utf-8'))
def add_before(p,before,content):
    old=p.read_text('utf-8')
    assert old.count(before)==1
    new=old.replace(before,content+before)
    E.fromstring(new.encode());p.write_text(new,encoding='utf-8')
    changes.append(str(p.relative_to(ROOT)))
front=ROOT/'source/frontmatter.ptx'
text=front.read_text('utf-8')
anchor='<p>Return to Appendices'
guide='''<p>Sections headed <em>Additional topics</em> are optional extensions. Richardson and Romberg integration and adaptive quadrature follow numerical integration; Runge–Kutta methods follow differential equations; contraction iteration follows sequences; and the Weierstrass M-test follows uniform convergence. The local existence and uniqueness theorem is placed at the end of the book because its proof uses the Cauchy criterion, contraction theorem, and uniform convergence. It can be read after those topics without the intervening complex-number material.</p>'''
assert text.count(anchor)==1
front.write_text(text.replace(anchor,guide+anchor),encoding='utf-8')
changes.append(str(front.relative_to(ROOT)))
summaries={
'sec-f-1-derivative-formulas.xml':'''<p>The inverse hyperbolic branches, their domains, and all six derivative formulas are collected in <xref ref="subsec-inverse-hyperbolic-functions" text="title"/>.</p>''',
'sec-f-2-integral-formulas.xml':'''<p>For inverse hyperbolic antiderivatives, including the negative square-root branch and reciprocal patterns, see <xref ref="subsec-inverse-hyperbolic-integrals" text="title"/>. For absolute and conditional improper convergence, see <xref ref="subsec-absolute-conditional-improper-integrals" text="title"/>.</p>''',
'sec-f-4-series-tests.xml':'''<p>The Cauchy criteria for sequences and series are <xref ref="thm-cauchy-sequences"/> and <xref ref="thm-cauchy-series"/>. For signed series with bounded partial sums, use <xref ref="thm-dirichlet-series"/>; for a convergent series multiplied by a bounded monotone factor, use <xref ref="thm-abel-series"/>. The optional uniform-convergence test is <xref ref="thm-weierstrass-m-test"/>.</p>''',
'sec-f-5-numerical-integration-rules.xml':'''<p>Optional extensions give Richardson and Romberg extrapolation in <xref ref="sec-additional-richardson-romberg"/> and a complete adaptive Simpson implementation in <xref ref="sec-additional-adaptive-quadrature"/>. Their difference-based indicators are error estimates; certified bounds require additional hypotheses and error analysis.</p>''',
'sec-12-6-computing-experiments.xml':'''<p>For further numerical methods, the optional sections <xref ref="sec-additional-richardson-romberg"/> and <xref ref="sec-additional-adaptive-quadrature"/> derive extrapolation and provide a complete adaptive algorithm with a stopping rule and explicit failure conditions.</p>''',
}
for filename,content in summaries.items():
    p=next((ROOT/'source').rglob(filename))
    # Insert inside the final subsection, preserving section structure.
    closing='</subsection>' if '</subsection>' in p.read_text('utf-8') else '</section>'
    old=p.read_text('utf-8');at=old.rfind(closing)
    new=old[:at]+content+'\n'+old[at:]
    E.fromstring(new.encode());p.write_text(new,encoding='utf-8')
    changes.append(str(p.relative_to(ROOT)))
# Add the two cancellation tests to the existing strategy table.
p=next((ROOT/'source').rglob('sec-15-6-absolute-convergence-and-stronger-tests.xml'))
old=p.read_text('utf-8')
at=old.index('<subsection xml:id="subsec-strategy-for-testing-series">')
end=old.index('</tabular>',at)
rows='''<row><cell><p>Bounded partial sums times a monotone factor tending to zero</p></cell><cell><p>Dirichlet's test</p></cell></row>
<row><cell><p>A convergent series times a bounded monotone factor</p></cell><cell><p>Abel's test</p></cell></row>'''.replace('\\textquotesingle ',"'")
new=old[:end]+rows+'\n'+old[end:]
E.fromstring(new.encode());p.write_text(new,encoding='utf-8')
(ROOT/'qa/additions/changed-source.json').write_text(json.dumps(sorted(set(changes)),indent=2),encoding='utf-8')
print('Integrated optional-topic navigation and formula-summary links.')
