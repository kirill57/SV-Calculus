"""Repairs of derivative claims and their hypotheses."""
from audit_edit import replace,record,ROOT
from lxml import etree as ET

replace('chapters/ch04*/sections/sec-4-3-*.xml',
        'f\\text{ is rising} \\amp f\'(x)&gt;0',
        'f\\text{ is increasing near }x \\amp f\'(x)\\ge0\\text{, when the derivative exists}',
        'An increasing function can have a zero derivative')
replace('chapters/ch04*/sections/sec-4-3-*.xml',
        'f\\text{ is falling} \\amp f\'(x)&lt;0',
        'f\\text{ is decreasing near }x \\amp f\'(x)\\le0\\text{, when the derivative exists}',
        'A decreasing function can have a zero derivative')
replace('chapters/ch04*/sections/sec-4-3-*.xml',
        'If <m>f\'(x)&gt;0</m>, then the tangent slopes are positive, so <m>f</m> is rising.',
        'If <m>f\'(x)&gt;0</m> throughout an interval, then the tangent slopes are positive there, so <m>f</m> is increasing on that interval. Chapter 6 will justify this conclusion with the Mean Value Theorem.',
        'Distinguish a derivative sign at one point from monotonicity on an interval')
replace('chapters/ch04*/sections/sec-4-3-*.xml',
        'If <m>f\'(x)&lt;0</m>, then the tangent slopes are negative, so <m>f</m> is falling.',
        'If <m>f\'(x)&lt;0</m> throughout an interval, then <m>f</m> is decreasing on that interval.',
        'State the interval hypothesis in the decreasing-function criterion')
replace('chapters/ch04*/sections/sec-4-4-*.xml',
        '|dA|\n\\approx\n2\\pi(10)(0.05)',
        '|dA|\n\\le\n2\\pi(10)(0.05)',
        'Use an inequality for the differential error bound')
replace('chapters/ch04*/sections/sec-4-4-*.xml',
        '\\left|\\frac{dA}{A}\\right|\n\\approx\n2\\frac{0.05}{10}',
        '\\left|\\frac{dA}{A}\\right|\n\\le\n2\\frac{0.05}{10}',
        'Use an inequality for the relative differential error bound')
replace('chapters/ch05*/sections/sec-5-3-*.xml',
        'where</p>\n\n  <p><me>\\varepsilon(k)\\to0',
        'where we define <m>\\varepsilon(0)=0</m>, and</p>\n\n  <p><me>\\varepsilon(k)\\to0',
        'Define the chain-rule error at zero so a constant inner function is covered')
replace('chapters/ch05*/sections/sec-5-2-*.xml',
        'where <m>g(x)\\neq0</m>.',
        'provided <m>g</m> is differentiable at <m>x</m> and <m>g(x)\\neq0</m>.',
        'State differentiability in the reciprocal-rule hypothesis')

path=next((ROOT/'source').glob('chapters/ch03*/sections/sec-3-5-*.xml'))
tree=ET.parse(str(path))
checkpoint=tree.xpath('//exercise[@xml:id="checkpoint-3-5-algebra-and-composition"]',namespaces={'xml':'http://www.w3.org/XML/1998/namespace'})[0]
target=tree.xpath('//subsection[@xml:id="subsec-continuity-compositions"]',namespaces={'xml':'http://www.w3.org/XML/1998/namespace'})[0]
checkpoint.getparent().remove(checkpoint); target.append(checkpoint)
path.write_bytes(ET.tostring(tree,encoding='utf-8',xml_declaration=True))
record(path,'Move composition checkpoint after the composition rule','Checkpoint before rule','Checkpoint after rule and counterexamples')
