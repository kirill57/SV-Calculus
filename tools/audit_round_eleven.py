"""Corrections checked in integration techniques and improper integrals."""
from audit_edit import replace
replace('chapters/ch11*/sections/sec-11-1-*.xml',
        'are differentiable functions, then', 'have continuous derivatives on the interval in question, then',
        'Use sufficient existence hypotheses for the integration-by-parts primitives')
replace('chapters/ch11*/sections/sec-11-1-*.xml',
        'If <m>u</m> and <m>v</m> are differentiable on <m>[a,b]</m>, then',
        'If <m>u</m> and <m>v</m> have continuous derivatives on <m>[a,b]</m>, then',
        'Differentiability alone does not guarantee the definite integrals in integration by parts exist')
replace('chapters/ch11*/sections/sec-11-2-*.xml',
        'If the power of <m>\\sec x</m> is even, save one factor',
        'If the power of <m>\\sec x</m> is a positive even integer (at least <m>2</m>), save one factor',
        'A zero secant power does not contain a secant-squared differential to save')
replace('chapters/ch11*/sections/sec-11-3-*.xml',
        'The three common square-root patterns match the three Pythagorean identities.',
        'For <m>a&gt;0</m>, the three common square-root patterns match the three Pythagorean identities.',
        'State positivity of the scale in square-root substitution patterns')
replace('chapters/ch11*/sections/sec-11-3-*.xml',
        'The triangle helps us return to <m>x</m>.</caption>',
        'The triangles shown assume <m>x&gt;0</m> (and <m>x&gt;a</m> in the secant case); their side lengths must be nonnegative. For negative <m>x</m>, use the signed substitution equations and the chosen angle range.</caption>',
        'Do not depict a negative input as a positive triangle side length')
replace('chapters/ch11*/sections/sec-11-3-*.xml',
        'when <m>x\\ge a</m>.', 'when <m>u\\ge0</m>, so <m>x\\ge a</m>.',
        'Cosh alone does not select the positive sign of sinh')
replace('chapters/ch11*/sections/sec-11-3-*.xml',
        'we have</p>\n\n  <p><me>u=\\operatorname{arsinh}',
        'we use <m>\\operatorname{arsinh}</m>, the inverse of the strictly increasing function <m>\\sinh:\\mathbb R\\to\\mathbb R</m>, and have</p>\n\n  <p><me>u=\\operatorname{arsinh}',
        'Define inverse hyperbolic sine before using its notation')
replace('chapters/ch11*/sections/sec-11-3-*.xml',
        'where <m>\\sec\\theta&gt;0</m> on the chosen interval.',
        'where we choose <m>-\\pi/2&lt;\\theta&lt;\\pi/2</m>, so <m>\\sec\\theta&gt;0</m>.',
        'Give the angle interval that was only alluded to in the tangent substitution')
replace('chapters/ch11*/sections/sec-11-4-*.xml',
        'and</p>\n\n  <p><me>\\int \\frac{dx}{(x-h)^2+a^2}',
        'and, for <m>a&gt;0</m>,</p>\n\n  <p><me>\\int \\frac{dx}{(x-h)^2+a^2}',
        'Exclude the zero scale from the arctangent building block')
replace('chapters/ch11*/sections/sec-11-6-*.xml',
        'A table may list</p>\n\n  <p><me>\\int e^{ax}\\cos(bx)',
        'For real constants <m>a,b</m> with <m>a^2+b^2&gt;0</m>, a table may list</p>\n\n  <p><me>\\int e^{ax}\\cos(bx)',
        'Exclude simultaneous zero parameters from a formula with denominator a squared plus b squared')
replace('chapters/ch11*/sections/sec-11-6-*.xml',
        'That is the problem of improper integrals. Computing',
        'That is the problem of improper integrals.',
        'Remove a stray imported heading fragment at the section end')
replace('chapters/ch11*/sections/sec-11-7-*.xml',
        'Suppose</p>\n\n  <p><me>0\\le f(x)\\le g(x)',
        'Suppose <m>f</m> and <m>g</m> are continuous on <m>[a,\\infty)</m>, and</p>\n\n  <p><me>0\\le f(x)\\le g(x)',
        'Exclude untreated finite singularities from a comparison of infinite tails')
replace('chapters/ch11*/sections/sec-11-7-*.xml',
        'Suppose <m>f(x)&gt;0</m> and <m>g(x)&gt;0</m> for all sufficiently large <m>x</m>.',
        'Suppose <m>f</m> and <m>g</m> are continuous on <m>[a,\\infty)</m>, with <m>f(x)&gt;0</m> and <m>g(x)&gt;0</m> for all sufficiently large <m>x</m>.',
        'State local integrability before applying the tail limit-comparison test')
