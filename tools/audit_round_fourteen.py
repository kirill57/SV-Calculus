"""Tracing, regularity, and coordinate-domain corrections."""
from audit_edit import ROOT,replace,save,record
import re
def sec(n):return f'chapters/ch14*/sections/sec-14-{n}-*.xml'
replace(sec(1),'the point moves down the lower branch to the vertex <m>(-1,0)</m>, then up the upper branch.',
        'the point moves upward along the lower branch to the vertex <m>(-1,0)</m>, then continues upward along the upper branch.',
        'The coordinate y equals t and increases throughout the tracing')
replace(sec(2),'Suppose <m>x(t)</m> and <m>y(t)</m> are differentiable near <m>t=t_0</m>, and',
        'Suppose <m>x(t)</m> and <m>y(t)</m> have continuous derivatives near <m>t=t_0</m>, and',
        'Ensure local invertibility used in the graph slope formula')
replace(sec(2),'For a differentiable parametrization <m>x=x(t)</m>, <m>y=y(t)</m>:',
        'For a parametrization <m>x=x(t)</m>, <m>y=y(t)</m> with continuous derivatives:',
        'State sufficient regularity for local tangent tests')
replace(sec(3),'A circle of radius <m>R</m> can be parametrized by',
        'A circle of radius <m>R&gt;0</m> can be parametrized by', 'The speed simplification uses a positive radius')
replace(sec(3),'around the <m>x</m>-axis gives surface area',
        'around the <m>x</m>-axis gives the following accumulated band area. It equals the geometric surface area when the generated surface is covered once; repeated or overlapping coverage must be removed before applying it:',
        'Surface area integrals count coverage multiplicity just like length integrals')
replace(sec(3),'For a simple closed curve traced once counterclockwise,',
        'For a simple closed curve with piecewise continuous coordinate derivatives, traced once counterclockwise,',
        'State regularity for the closed-curve area integrals')
replace(sec(3),'This traces the ellipse counterclockwise.',
        'Here <m>a,b&gt;0</m>, so this traces the ellipse counterclockwise.',
        'Axis scales must be positive to fix the orientation and positive area')
replace(sec(4),'produce flower-shaped curves called <em>roses</em>.',
        'produce flower-shaped curves called <em>roses</em> when <m>a&gt;0</m> and <m>n</m> is a positive integer. The petal count below uses these assumptions.',
        'Rose petal rules require an integer frequency and nonzero amplitude')
replace(sec(5),'is the inner curve on',
        r'is the inner curve, with <m>0\le\rho(\theta)\le R(\theta)</m>, on',
        'The difference-of-sectors formula requires actual nonnegative ordered radii')
replace(sec(5),'the length of the polar curve is',
        'assuming <m>r</m> has a continuous derivative, the distance traveled along the polar curve is',
        'State smoothness and account for repeated tracing in polar length')
replace(sec(5),'and hence</p>\n\n  <p><me>\\theta=\\frac{\\pi}{4}.</me></p>',
        'and hence</p>\n\n  <p><me>\\theta=\\frac{\\pi}{4}+k\\pi,\\qquad k\\in\\mathbb Z.</me></p>',
        'Give all same-angle solutions; the extra angle retraces the same point')
replace(sec(6),'have constant difference.', 'have a constant positive absolute difference.',
        'An unsigned difference is needed to include both hyperbola branches')
replace(sec(6),'Fix a point <m>F</m>, called the <em>focus</em>, and a line <m>\\ell</m>, called the <em>directrix</em>.',
        'Fix a point <m>F</m>, called the <em>focus</em>, and a line <m>\\ell</m> not containing <m>F</m>, called the <em>directrix</em>.',
        'Exclude degenerate focus-on-directrix loci from the conic classification')
replace(sec(6),'For the horizontal hyperbola centered at the origin,',
        'For the horizontal hyperbola centered at the origin, with <m>a,b&gt;0</m>,',
        'Exclude zero scales from hyperbola standard form')
replace(sec(6),'For a point <m>P</m> with polar coordinates <m>(r,\\theta)</m>, the distance to the focus is',
        r'First use <m>r\ge0</m> for a point <m>P</m> to the left of the directrix. Its distance to the focus is',
        'A directed polar radius is not always the distance to the focus')
replace(sec(6),'The number <m>p</m> is called the <em>semi-latus rectum</em>.',
        r'For an ellipse or parabola, these nonnegative radii describe the whole conic. For a hyperbola they describe the branch to the left of the directrix. Allowing negative radii in the same algebraic polar formula also traces the other branch; there the focus distance is <m>|r|</m> and the directrix distance is <m>|d-r\cos\theta|</m>. The number <m>p</m> is called the <em>semi-latus rectum</em>.',
        'Explain how the signed-radius conic equation extends the one-branch distance derivation')
path=next((ROOT/'source').glob(sec(6)));s=path.read_text('utf-8')
a=s.index('  <exercise xml:id="checkpoint-',s.index('<title>What does eccentricity')) if False else 0
pattern=r'<exercise[^>]*>\s*<title>What does eccentricity measure geometrically\?</title>.*?</exercise>'
m=re.search(pattern,s,re.S);block=m.group();s=s.replace(block,'');end=s.index('</example>',s.index('Find the foci and eccentricity'))+len('</example>')
save(path,s[:end]+'\n'+block+s[end:]);record(path,'Move the eccentricity checkpoint after c and a have been defined',block,'Moved after the ellipse example')
replace(sec(7),'That sentence is Kepler’s first law.',
        'That sentence is Kepler’s first law. We use the ideal two-body model: the central body is fixed, the force is inverse-square attraction, and other bodies and drag are neglected.',
        'State the idealization behind exact conic planetary orbits')
replace(sec(7),'So gravity can pull the planet inward or outward along the radial direction, but it does not push sideways.',
        'Gravity pulls the planet inward along the radial direction; it has no sideways force component.',
        'Attractive gravity does not point radially outward')
replace(sec(7),'The equal-area law says this precisely.',
        r'''The equal-area law directly controls angular speed. To check the ordinary speed along this elliptical orbit, write <m>h=r^2\theta'&gt;0</m>. From <m>r=p/(1+e\cos\theta)</m>, differentiation gives <m>r'=he\sin\theta/p</m>. Hence <m>v^2=(r')^2+(r\theta')^2=(h/p)^2(1+e^2+2e\cos\theta)=(h/p)^2(e^2-1+2p/r)</m>. This increases as the distance <m>r</m> decreases, so the speed is also larger nearer the sun.''',
        'Do not infer linear speed from angular speed alone')
replace(sec(7),'Because the directions <m>\\mathbf e_r</m> and <m>\\mathbf e_\\theta</m> rotate as the planet moves,',
        r'''In coordinates, <m>\mathbf e_r=\langle\cos\theta,\sin\theta\rangle</m> and <m>\mathbf e_\theta=\langle-\sin\theta,\cos\theta\rangle</m>. Differentiate each coordinate to get <m>\mathbf e_r'=\theta'\mathbf e_\theta</m> and <m>\mathbf e_\theta'=-\theta'\mathbf e_r</m>. Because these directions rotate as the planet moves,''',
        'Define the unit vectors and their derivative rules before using the acceleration formula')
replace(sec(8),'The angle <m>\\theta</m> that <m>z</m> makes with the positive real axis is called an <em>argument</em> of <m>z</m>.',
        r'For <m>z\ne0</m>, an angle <m>\\theta</m> that <m>z</m> makes with the positive real axis is called an <em>argument</em> of <m>z</m>. Zero has modulus zero and no defined argument.',
        'Complex argument is undefined at zero')
replace(sec(8),'differentiate:</p>','differentiate the real and imaginary parts separately:</p>',
        'Define the real-parameter complex derivative being used in this preview')
