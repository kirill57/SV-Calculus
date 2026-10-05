"""Corrections checked in applications of integration."""
from audit_edit import replace
replace('chapters/ch10*/sections/sec-10-3-*.xml',
        'The shell formula becomes',
        'If the region lies entirely on one side of the axis, so that different strips give different shell radii, the shell formula becomes',
        'Absolute radii alone do not prevent double counting when a region crosses the rotation axis')
replace('chapters/ch10*/sections/sec-10-3-*.xml',
        '|y-k|.</me></p>\n\n  <p>Then</p>',
        '|y-k|.</me></p>\n\n  <p>If the region lies entirely on one side of the axis, then</p>',
        'State the same nonoverlap condition for horizontal shells')
replace('chapters/ch10*/sections/sec-10-4-*.xml',
        'Area and volume assume the material is uniform.  But real objects are often heavier in one place than another.',
        'Area and volume describe geometry without telling us how mass is distributed. Real objects are often heavier in one place than another.',
        'Geometric area and volume do not assume uniform material density')
replace('chapters/ch10*/sections/sec-10-4-*.xml',
        'assuming constant areal density <m>\\sigma</m>.',
        'assuming constant areal density <m>\\sigma&gt;0</m>.',
        'Require positive total mass before dividing in the lamina example')
replace('chapters/ch10*/sections/sec-10-5-*.xml',
        'If the force points opposite the direction of motion, then <m>F(x)&lt;0</m>,',
        'For motion in the increasing <m>x</m>-direction, a force pointing opposite the motion has <m>F(x)&lt;0</m>,',
        'A force component is negative relative to the chosen axis, not relative to arbitrary motion')
replace('chapters/ch10*/sections/sec-10-6-*.xml',
        'F=\\gamma\\int_D y\\,dA,',
        'F=\\gamma\\int_a^b y\\,w(y)\\,dy,',
        'Express the centroid shortcut using the one-variable strip integral already defined')
replace('chapters/ch10*/sections/sec-10-6-*.xml',
        'where <m>D</m> is the plate and <m>y</m> is depth below the surface.',
        'where <m>w(y)</m> is the plate width at depth <m>y</m>, and <m>a,b</m> are its depth limits.',
        'Define the width and limits in the centroid shortcut')
replace('chapters/ch10*/sections/sec-10-6-*.xml',
        '\\int_D y\\,dA=A\\bar y.',
        '\\int_a^b y\\,w(y)\\,dy=A\\bar y.',
        'Avoid undefined multivariable integration notation in the centroid identity')
replace('chapters/ch10*/sections/sec-10-7-*.xml',
        '\\text{average}=\\frac{\\text{total accumulated amount}}{\\text{size of the interval}}.',
        '\\text{weighted average}=\\frac{\\text{weighted accumulated amount}}{\\text{total weight}}.',
        'Expected value uses probability weights rather than division by interval length')
replace('chapters/ch10*/sections/sec-10-7-*.xml',
        'Let <m>f</m> be continuous on <m>[a,b]</m>.',
        'Let <m>f</m> be continuous on <m>[a,b]</m>, with <m>a&lt;b</m>.',
        'Exclude a zero-length interval in the average-value construction')
replace('chapters/ch10*/sections/sec-10-7-*.xml',
        'If <m>f</m> is continuous on <m>[a,b]</m>, then',
        'If <m>f</m> is continuous on <m>[a,b]</m>, with <m>a&lt;b</m>, then',
        'State the nondegenerate-interval hypothesis in the average-value theorem')
replace('chapters/ch10*/sections/sec-10-7-*.xml',
        'The normal density with mean <m>\\mu</m> and standard deviation <m>\\sigma</m> is',
        'The normal density with mean <m>\\mu</m> and standard deviation <m>\\sigma&gt;0</m> is',
        'The normal-density scale parameter must be positive')
replace('chapters/ch10*/sections/sec-10-8-*.xml',
        'The surface area is therefore',
        'Apply the surface-area formula first on <m>[-R+\\varepsilon,R-\\varepsilon]</m>, where the derivative is continuous, and then let <m>\\varepsilon\\to0^+</m>. The limiting surface area is therefore',
        'Use truncated smooth arcs before taking the sphere limit at vertical-tangent endpoints')
replace('chapters/ch10*/sections/sec-10-8-*.xml',
        'So the exact length cannot be written using only the usual elementary functions.',
        'So the usual elementary antiderivative rules do not provide an exact endpoint formula for this length.',
        'Nonexistence of an elementary primitive does not by itself prove a definite integral has no elementary value')
replace('chapters/ch10*/sections/sec-10-8-*.xml',
        'a perfectly meaningful integral that cannot be written with the usual elementary functions.',
        'a perfectly meaningful integral whose integrand has no elementary antiderivative.',
        'Keep the arc-length checkpoint claim within the established non-elementary antiderivative fact')
