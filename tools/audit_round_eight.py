"""Corrections checked while reading the integral construction."""
from audit_edit import replace
replace('chapters/ch08*/sections/sec-8-4-*.xml', '\\frac{42}{4}', '\\frac{46}{4}',
        'Correct the sum of the four sampled heights')
replace('chapters/ch08*/sections/sec-8-4-*.xml', '\\frac{21}{4}.</mrow>', '\\frac{23}{4}.</mrow>',
        'Correct the right-endpoint Riemann sum')
replace('chapters/ch08*/sections/sec-8-4-*.xml', '\\frac{21}{4}=5.25.', '\\frac{23}{4}=5.75.',
        'Make the stated Riemann sum agree with its arithmetic and the review table')
replace('chapters/ch08*/sections/sec-8-1-*.xml',
        'We may only have speedometer readings at certain times.',
        'We may only have speedometer readings at certain times. A speedometer gives speed; in the following example we assume motion in the positive direction, so speed equals velocity.',
        'State the direction assumption when speedometer samples are treated as velocities')
replace('chapters/ch08*/sections/sec-8-1-*.xml',
        'constant for a while, then another constant, then another.',
        'constant for a while, then another constant, then another. This idealized model has instantaneous velocity changes. At each jump the position is continuous but has no two-sided derivative; the velocity formula describes the motion away from those instants.',
        'Reconcile idealized velocity jumps with velocity as a position derivative')
replace('chapters/ch08*/sections/sec-8-2-*.xml',
        'A more reliable idea is to use the largest and smallest function values on each small interval.',
        'For a continuous function, a more reliable idea is to use the largest and smallest function values on each small interval. We assume continuity in this construction; later we will use least upper bounds and greatest lower bounds for general bounded functions.',
        'Do not assume a general function attains extrema on each subinterval')
replace('chapters/ch08*/sections/sec-8-3-*.xml',
        'we start with the binomial expansion of the difference of <m>(p+1)</m>-th powers:',
        'we start with the binomial expansion of the difference of <m>(p+1)</m>-th powers. Here <m>\\binom{N}{k}=N(N-1)\\cdots(N-k+1)/(1\\cdot2\\cdots k)</m> for <m>1\\le k\\le N</m>, and <m>\\binom{N}{0}=1</m>; these are the coefficients obtained by expanding <m>(k+1)^{p+1}</m> by multiplication:',
        'Define binomial coefficients at their first use rather than relying on the later series chapter')
replace('chapters/ch08*/sections/sec-8-7-*.xml',
        'For friendly functions, these are just the minimum and maximum values of <m>f</m> on that subinterval.',
        'The notation <m>\\inf</m> means the greatest lower bound and <m>\\sup</m> means the least upper bound. They exist here by completeness because the sets are nonempty and bounded. For continuous functions, they are the minimum and maximum values of <m>f</m> on that subinterval.',
        'Define infimum and recall why both bounds exist before using upper-lower sums')
replace('chapters/ch08*/sections/sec-8-7-*.xml',
        'and the same meaning of “close enough” works everywhere on the interval.',
        'and the same meaning of “close enough” works everywhere on the interval. This property is called <em>uniform continuity</em>. To see why it follows here, suppose it failed for some fixed output gap <m>\\eta&gt;0</m>. Bisect the closed interval repeatedly, each time retaining a half that still contains pairs of arbitrarily close inputs with output gap at least <m>\\eta</m>. Such a half must exist: otherwise the two halves have distance thresholds, and continuity at their common endpoint also controls pairs straddling it. The retained intervals are nested and their lengths tend to zero, so completeness gives a common point <m>c</m>. Eventually a retained interval lies wholly in a neighborhood of <m>c</m> where continuity makes every value differ from <m>f(c)</m> by less than <m>\\eta/2</m>. No two values there can have gap at least <m>\\eta</m>, a contradiction.',
        'Justify the uniform control needed by the integrability proof using previously introduced nested intervals')
replace('chapters/ch08*/sections/sec-8-7-*.xml',
        'meaning all the bad points can be covered by a collection of intervals whose total cumulative length is arbitrarily small.',
        'meaning that, for every <m>\\varepsilon&gt;0</m>, those points can be covered by a finite or countable collection of open intervals whose lengths sum to less than <m>\\varepsilon</m>. This criterion is stated here for perspective; its proof requires a later course in analysis.',
        'Make the stated measure-zero criterion precise and distinguish it from proved results')
replace('chapters/ch08*/sections/sec-8-8-*.xml',
        '\\text{distance}\\approx \\sum \\text{velocity}\\cdot\\text{time}.',
        '\\text{displacement}\\approx \\sum \\text{velocity}\\cdot\\text{time}.',
        'Velocity accumulates signed displacement in the review summary')
replace('chapters/ch08*/sections/sec-8-7-*.xml',
        '\\addplot[only marks, mark=*, mark size=1.4pt] coordinates {\n    (0.02,0) (0.09,0) (0.14,0) (0.19,0) (0.27,0) (0.31,0)\n    (0.38,0) (0.45,0) (0.57,0) (0.63,0) (0.70,0) (0.76,0)\n    (0.84,0) (0.91,0) (0.97,0)\n};',
        '\\addplot[only marks, mark=*, mark size=1.4pt, domain=1:15, samples=15] ({sqrt(2)*(x-0.5)/22},{0});',
        'Use irrational abscissas for the schematic zero-height samples of the Dirichlet function')
