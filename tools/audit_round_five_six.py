"""Corrections of domain and theorem conditions in Chapters 5--6."""
from audit_edit import replace,ROOT,record
from lxml import etree as ET

replace('chapters/ch05*/sections/sec-5-8-*.xml',
        'Suppose a cable hangs under its own weight.  Place the lowest point at the center.  Let <m>s(x)</m> be the arc length of the cable from the lowest point to the point with horizontal coordinate <m>x</m>.',
        'Suppose a flexible cable with uniform mass per unit length hangs under its own weight. Place the lowest point at the center. On the right half, <m>x\\ge0</m>, let <m>s(x)</m> be the arc length, meaning the length measured along the cable, from the lowest point to the point with horizontal coordinate <m>x</m>. The left half follows by reflection.',
        'State the cable-model assumptions and avoid treating unsigned length as negative on the left')
replace('chapters/ch05*/sections/sec-5-8-*.xml',
        'The derivative of arc length with respect to <m>x</m> is',
        'For a tiny horizontal step, the Pythagorean theorem gives the length factor <m>\\sqrt{1+(y\')^2}</m>. Thus the derivative of arc length with respect to <m>x</m> is',
        'Explain the arc-length notion and formula before its preview use')
replace('chapters/ch05*/sections/sec-5-10-*.xml',
        'Assume all factors are nonzero.  Take logarithms and differentiate to show',
        'Work on an interval where all factors are nonzero. Take the logarithm of the absolute value, using <m>\\ln|P(x)|=\\sum_{j=1}^n\\ln|x-a_j|</m>, and differentiate to show',
        'A nonzero product can be negative, so logarithmic differentiation needs absolute values')
replace('chapters/ch05*/sections/sec-5-7-*.xml',
        'The remaining inverse trigonometric derivatives follow from the same method.  With the usual choices of inverse branches,',
        'The remaining inverse trigonometric derivatives follow from the same method. Here <m>\\operatorname{arccot}</m> has range <m>(0,\\pi)</m>, <m>\\operatorname{arcsec}</m> has range <m>[0,\\pi]\\setminus\\{\\pi/2\\}</m>, and <m>\\operatorname{arccsc}</m> has range <m>[-\\pi/2,\\pi/2]\\setminus\\{0\\}</m>. The arcsecant and arccosecant derivative formulas hold for <m>|x|&gt;1</m>; the arccotangent formula holds for every real <m>x</m>. With these branch choices,',
        'Specify the inverse branches and domains needed for the derivative signs')
replace('chapters/ch06*/sections/sec-6-1-*.xml',
        'A speedometer does not only tell how fast a car is moving. Its sign tells the direction of motion.',
        'Velocity tells both how fast a car is moving and its direction. Its sign tells the direction of motion; a speedometer reports the nonnegative speed.',
        'A speedometer has no signed velocity reading')
replace('chapters/ch06*/sections/sec-6-2-*.xml',
        '<p>everywhere.</p>',
        '<p>at every interior point.</p>',
        'Respect the book\'s two-sided derivative convention at endpoints')
replace('chapters/ch06*/sections/sec-6-4-*.xml',
        'on the graph of <m>f</m> is an <em>inflection point</em> if the concavity of <m>f</m> changes at <m>c</m>.',
        'on the graph of <m>f</m> is an <em>inflection point</em> if <m>f</m> is continuous at <m>c</m> and the concavity of <m>f</m> changes there.',
        'Make the inflection definition agree with the continuity requirement used in sketches')
replace('chapters/ch06*/sections/sec-6-5-*.xml',
        'The symbol <m>\\sim</m> here means that the two expressions have the same leading behavior.  The difference between them approaches <m>0</m>.',
        'The symbol <m>\\sim</m> means that the ratio of the two expressions approaches <m>1</m>. In this example the stronger statement also holds: their difference approaches <m>0</m>.',
        'Do not confuse asymptotic equivalence with a difference tending to zero')
replace('chapters/ch06*/sections/sec-6-6-*.xml',
        'Suppose</p>\n\n  <p><me>f(a)=0, \\qquad g(a)=0,</me></p>',
        'In the finite-input <m>0/0</m> case, extend the functions to <m>a</m>, if necessary, by their limits. They are then continuous at <m>a</m>, with</p>\n\n  <p><me>f(a)=0, \\qquad g(a)=0,</me></p>',
        'Supply endpoint continuity before applying Cauchy\'s theorem in the l\'Hospital proof')

# All nondegenerate MVT statements need distinct ordered endpoints.
for path in (ROOT/'source').rglob('*.xml'):
    tree=ET.parse(str(path)); changed=False
    for el in tree.xpath('//theorem | //note'):
        title=''.join(el.find('title').itertext()) if el.find('title') is not None else ''
        if title not in ['Rolle’s Theorem','Mean Value Theorem','Cauchy’s Mean Value Theorem']: continue
        paragraph=el.find('statement/p') if el.tag=='theorem' else el.find('p')
        if paragraph is not None:
            paragraph.text='Assume '+(paragraph.text or '').removeprefix('Suppose ').removeprefix('Suppose')
            assumption=ET.Element('p'); m=ET.SubElement(assumption,'m'); m.text='a&lt;b'.replace('&lt;','<'); m.tail='.'
            el.insert(list(el).index(el.find('title'))+1,assumption) if el.tag=='note' else el.find('statement').insert(0,assumption)
            changed=True
    if changed:
        path.write_bytes(ET.tostring(tree,encoding='utf-8',xml_declaration=True))
        record(path,'State a<b in Rolle, Mean Value, and Cauchy theorems','Implicit interval convention','Explicit nondegenerate ordered endpoints')
