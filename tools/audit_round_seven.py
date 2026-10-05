"""Corrections checked during the applications chapter."""
from audit_edit import replace
replace('chapters/ch07*/sections/sec-7-2-*.xml',
        'The maximum area occurs when',
        'Since <m>A\'\'(x)=-4&lt;0</m>, the area is concave down; also <m>A(0)=A(100)=0</m> and <m>A(50)=5000</m>. Thus the absolute maximum area occurs when',
        'Verify the global maximum in the first optimization example')
replace('chapters/ch07*/sections/sec-7-2-*.xml',
        'This condition is the familiar reflection rule:',
        'Here <m>a,b,L&gt;0</m>. The second derivative is <m>D\'\'(x)=a^2/(x^2+a^2)^{3/2}+b^2/((L-x)^2+b^2)^{3/2}&gt;0</m>, and the critical point lies in <m>(0,L)</m>, so it is the unique absolute minimum. This condition is the familiar reflection rule:',
        'Justify that the reflected-path stationary point minimizes the distance')
replace('chapters/ch07*/sections/sec-7-3-*.xml',
        'where <m>C</m> and <m>n</m> are constants.',
        'where <m>C\\neq0</m> and <m>n</m> are constants, and <m>x&gt;0</m>.',
        'State the nonzero-output and positive-input assumptions in relative power-law error')
replace('chapters/ch07*/sections/sec-7-3-*.xml',
        '\\frac{dy}{y}\\approx n\\frac{dx}{x}.',
        '\\frac{\\Delta y}{y}\\approx n\\frac{\\Delta x}{x}.',
        'The differential identity is exact; the finite relative change is approximate')
replace('chapters/ch07*/sections/sec-7-3-*.xml',
        'For a power law, the relative output error is approximately <m>n</m> times the relative input error.',
        'For a power law, the magnitude of the relative output error is approximately <m>|n|</m> times the magnitude of the relative input error.',
        'Use the absolute exponent for error magnitudes')
replace('chapters/ch07*/sections/sec-7-3-*.xml',
        'The distance error is the same.  The angle error is the same.',
        'The horizontal distance is the same. The angle error is the same.',
        'The surveyor example varies angle, not a stated distance error')
replace('chapters/ch07*/sections/sec-7-4-*.xml',
        'The solution is a point where the graph of <m>f</m> crosses the <m>x</m>-axis.',
        'A solution is an input where the graph of <m>f</m> meets the <m>x</m>-axis; it may cross the axis or merely touch it.',
        'A multiple root need not cross the axis')
replace('chapters/ch07*/sections/sec-7-4-*.xml',
        'Taylor’s formula around <m>x_n</m> gives',
        'We can obtain a quadratic error formula using Rolle’s Theorem twice, without assuming a later Taylor formula. Choose <m>C</m> so that <m>F(t)=f(t)-f(x_n)-f\'(x_n)(t-x_n)-C(t-x_n)^2</m> satisfies <m>F(r)=0</m>. We also have <m>F(x_n)=F\'(x_n)=0</m>. Rolle’s Theorem first gives a zero of <m>F\'</m> between <m>x_n</m> and <m>r</m>, and then a zero of <m>F\'\'</m> between that point and <m>x_n</m>. Thus <m>C=f\'\'(c_n)/2</m> for a point <m>c_n</m> between <m>x_n</m> and <m>r</m>. (If <m>x_n=r</m>, the root has already been found.) Therefore',
        'Establish the Newton quadratic remainder using only theorems already introduced')
replace('chapters/ch07*/sections/sec-7-4-*.xml',
        'This behavior is called <em>quadratic convergence</em>.',
        'This behavior is called <em>quadratic convergence</em>. To make the convergence claim precise, continuity bounds <m>|f\'\'|</m> above and <m>|f\'|</m> away from zero in a small interval about <m>r</m>. Hence <m>|x_{n+1}-r|\\le C|x_n-r|^2</m> there for a fixed <m>C</m>. Choose the starting error small enough that <m>C|x_0-r|\\le1/2</m> and the starting point lies in that interval. Each next error is at most half the previous one, so all iterates remain in the interval and converge to <m>r</m>.',
        'Explain how the Newton error estimate guarantees that all iterates stay near the root')
replace('chapters/ch07*/sections/sec-7-6-*.xml',
        'the growth rate should be large when <m>P</m> is small and close to <m>0</m> when <m>P</m> is near <m>K</m>.',
        'the relative growth rate should be close to its unrestricted value when <m>P</m> is small and close to <m>0</m> when <m>P</m> is near <m>K</m>.',
        'Distinguish absolute and relative growth in the logistic motivation')
replace('chapters/ch07*/sections/sec-7-6-*.xml',
        'then</p>\n        <p><me>\nP(t)=\\frac{K}{1+\\left(\\dfrac{K-P_0}{P_0}\\right)e^{-rt}}.\n</me></p>',
        'then, for <m>t\\ge0</m>,</p>\n        <p><me>P(t)=\\frac{K}{1+\\left(\\dfrac{K-P_0}{P_0}\\right)e^{-rt}}.</me></p>',
        'Specify the forward-time domain of the positive-population logistic solution')
replace('chapters/ch07*/sections/sec-7-2-*.xml',
        '\\node[below] at (3.5,0) {mirror};',
        '\\node[below] at (6.5,0) {mirror};',
        'Separate the mirror caption from the reflection-point label')
replace('chapters/ch07*/sections/sec-7-3-*.xml',
        '\\draw[dashed] (axis cs:26,0) -- (axis cs:26,5.1);',
        '\\draw[dashed] (axis cs:26,4.4) -- (axis cs:26,5.1);',
        'Keep the square-root guide line inside the plotted window')
replace('chapters/ch07*/sections/sec-7-3-*.xml',
        '|dV|\\lesssim 0.72\\pi', '|\\Delta V|\\lesssim 0.72\\pi',
        'Use the approximate differential bound for the finite volume error')
replace('chapters/ch07*/sections/sec-7-3-*.xml',
        '|dA|\\lesssim 9.6\\pi', '|\\Delta A|\\lesssim 9.6\\pi',
        'Use the approximate differential bound for the finite area error')
replace('chapters/ch07*/sections/sec-7-3-*.xml',
        '\\frac{|dA|}{A}\n\\lesssim', '\\frac{|dA|}{A}\n\\le',
        'The differential relative-error bound is exact')
replace('chapters/ch07*/sections/sec-7-5-*.xml',
        'then the account grows at <m>5\\%</m> per year.',
        'then the continuous annual rate is <m>5\\%</m>. Over one year the balance grows by the effective rate <m>e^{0.05}-1\\approx5.13\\%</m>.',
        'Distinguish the continuous annual interest rate from the effective yearly increase')
replace('chapters/ch07*/sections/sec-7-7-*.xml',
        'has the same length as the straightened path',
        'has the same length as the reflected broken path',
        'The reflected path is straight only at the minimizing crossing')
