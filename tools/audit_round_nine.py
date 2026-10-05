"""Corrections checked while reading the Fundamental Theorem chapter."""
from audit_edit import replace, ROOT, save, record
from lxml import etree as ET
replace('chapters/ch09*/sections/sec-9-1-*.xml',
        'This is the same idea as an odometer.  At each time, the odometer reading is the accumulated velocity up to that time.  If we know the velocity graph, then the odometer reading is an area-with-sign whose right endpoint moves.',
        'This is the same idea as recovering position from velocity. At each time, the position change is the accumulated signed velocity up to that time. If we know the velocity graph, that change is an area-with-sign whose right endpoint moves. An odometer instead accumulates speed, so its reading never decreases.',
        'An odometer accumulates speed rather than signed velocity')
replace('chapters/ch09*/sections/sec-9-2-*.xml',
        'Before this theorem, an antiderivative was something we might hope to find by guessing.',
        'A function <m>F</m> with <m>F\'=f</m> is called an <em>antiderivative</em> of <m>f</m>. Before this theorem, such a function was something we might hope to find by guessing.',
        'Define antiderivative at its first substantial use')
replace('chapters/ch09*/sections/sec-9-3-*.xml',
        'Now use <m>x=a</m>.',
        'The equality also holds at the endpoints: <m>A</m> is continuous there because boundedness of <m>f</m> gives <m>|A(x)-A(y)|\\le M|x-y|</m> for some <m>M</m>, and <m>F</m> is continuous by differentiability. Now use <m>x=a</m>.',
        'Extend the constant-difference identity from the interior to the endpoints before evaluation')
replace('chapters/ch09*/sections/sec-9-3-*.xml',
        'This is called the <em>net change theorem</em>.',
        'When <m>F\'</m> is continuous on <m>[a,b]</m>, this follows from Part II and is called the <em>net change theorem</em>. The more general version also holds for a Riemann-integrable derivative, but differentiability alone does not guarantee that the integral exists.',
        'Do not assert integrability of every derivative in the net-change rule')
replace('chapters/ch09*/sections/sec-9-3-*.xml',
        'It is positive on <m>[0,1]</m>, negative on <m>[1,3]</m>, and positive on <m>[3,4]</m>.',
        'It is positive on <m>[0,1)</m>, negative on <m>(1,3)</m>, and positive on <m>(3,4]</m>, with zeros at <m>t=1,3</m>.',
        'Keep the zero-velocity endpoints out of strict sign claims')
replace('chapters/ch09*/sections/sec-9-5-*.xml',
        'Substitution gave us a powerful rule:',
        'The reverse chain rule suggests a powerful substitution pattern, which we develop in this section:',
        'Do not claim a substitution rule was already developed in a nonexistent earlier section')
replace('chapters/ch09*/sections/sec-9-5-*.xml',
        'When <m>x=g(u)</m>,',
        'Let <m>f</m> be continuous on an interval <m>J</m>, and let <m>g</m> have a continuous derivative on the interval between <m>\\alpha</m> and <m>\\beta</m>, with all its values in <m>J</m>. When <m>x=g(u)</m>,',
        'State sufficient hypotheses for the substitution rule')
replace('chapters/ch09*/sections/sec-9-5-*.xml',
        'The derivative <m>g\'(u)</m> converts <m>du</m>-steps into oriented <m>dx</m>-steps.',
        'To prove the rule, choose an antiderivative <m>F</m> of <m>f</m>, which exists by Part I. The chain rule gives <m>(F\\circ g)\'(u)=f(g(u))g\'(u)</m>. Part II makes the right-hand integral <m>F(g(\\beta))-F(g(\\alpha))=F(b)-F(a)</m>, exactly the left-hand integral. No monotonicity of <m>g</m> is needed: oriented contributions cancel if it doubles back. The derivative <m>g\'(u)</m> converts <m>du</m>-steps into oriented <m>dx</m>-steps.',
        'Justify substitution by the chain rule and FTC rather than differential symbol manipulation alone')
replace('chapters/ch09*/sections/sec-9-5-*.xml',
        'If <m>F</m> is differentiable, then',
        'If <m>F</m> has a continuous derivative, then',
        'Use a sufficient integrability hypothesis before integrating exact differentials')
replace('chapters/ch09*/sections/sec-9-7-*.xml',
        '\\int_{0}^{1} \\frac{x}{\\sqrt{1-x^2}}\\,dx.',
        '\\int_{0}^{1/2} \\frac{x}{\\sqrt{1-x^2}}\\,dx.',
        'Avoid assigning an improper endpoint integral before improper integrals are defined')
replace('chapters/ch09*/sections/sec-9-7-*.xml',
        'The rate <m>R(t)</m> increases at first and then decreases.',
        'The rate <m>R(t)</m> increases on some subintervals and decreases on others.',
        'The sinusoidal rate turns upward again after t=6')
replace('chapters/ch09*/sections/sec-9-5-*.xml',
        '\\node[below] at (\\x,1.1) {\\(\\lab\\)};',
        '\\node[above] at (\\x,1.3) {\\(\\lab\\)};',
        'Separate substitution-scale tick labels from mapping arrows')
# Put the moving-endpoint checkpoint after the examples that introduce it.
path=next((ROOT/'source').glob('chapters/ch09*/sections/sec-9-2-*.xml'))
tree=ET.parse(str(path))
checks=tree.xpath('//exercise[contains(title,"moving endpoint bring")]')
if checks:
    check=checks[0]; target=tree.xpath('//subsection[title="Examples with variable upper limits"]')[0]
    if check.getparent()!=target:
        check.getparent().remove(check); target.append(check)
        save(path,ET.tostring(tree,encoding='UTF-8',xml_declaration=True))
        record(path,'Place moving-endpoint checkpoint after its rule and worked examples','checkpoint before formal proof','checkpoint after moving-endpoint examples')
