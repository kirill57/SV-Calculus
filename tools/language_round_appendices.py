"""One-time language corrections in appendix openings."""
from language_audit import opening, replace
edits={
'appA-algebra-and-inequalities-review':r'<p>This appendix reviews factoring, completing the square, rational expressions, powers, inequalities, and finite sums. These algebraic tools are used to simplify calculus expressions, determine domains, and prove error bounds.</p>',
'sec-a-1-factoring-and-completing-the-square':r'<p>Factoring expresses a polynomial as a product. It reveals zeros and signs and can expose common factors for cancellation. Completing the square gives a form useful for recognizing graphs and evaluating integrals.</p>',
'sec-a-3-exponents-and-radicals':r'<p>Rewriting roots and reciprocals as powers can simplify differentiation and integration. The exponent laws must be used on domains where the expressions are defined.</p>',
'sec-a-4-inequalities-and-absolute-values':r'<p>Inequalities compare quantities and bound errors. Absolute values measure distances and unsigned magnitudes. This section reviews the rules used in limit proofs, approximation bounds, and convergence comparisons.</p>',
'appB-coordinate-geometry':r'<p>Coordinate geometry expresses shapes using equations. This appendix reviews lines, circles, conics, distances, midpoints, and graph transformations, including the forms used for tangents and integral boundaries.</p>',
'sec-b-1-lines':r'<p>A line is determined by two distinct points or by a point and a slope. Line equations are used for secants, tangents, linear approximations, and Newton steps.</p>',
'appC-trigonometry-in-radians':r'<p>This appendix reviews the unit-circle definitions, identities, addition formulas, inverse functions, and equations used in calculus. Angles are measured in radians unless degrees are explicitly stated. The derivative formulas for sine and cosine depend on that convention.</p>',
'appD-proofs-and-completeness':r'<p>Completeness of the real numbers supports the existence results used throughout calculus. This appendix develops the least-upper-bound property, monotone convergence, bisection, extrema, and uniform continuity. The main-text Cauchy criterion in <xref ref="thm-cauchy-sequences"/> gives another formulation of completeness.</p>',
'sec-d-1-least-upper-bound-property':r'<p>The least-upper-bound property states completeness in terms of bounded sets of real numbers. Every nonempty set bounded above has a smallest real upper bound. We will use that property to justify limiting values.</p>',
'sec-d-2-monotone-convergence-theorem':r'<p>An increasing sequence bounded above converges to the supremum of its terms. A decreasing sequence bounded below converges to their infimum. This section proves both statements from the least-upper-bound property.</p>',
'sec-d-4-extreme-value-theorem-proof-outline':r'<p>A continuous function on a closed, bounded interval attains its maximum and minimum. This section outlines a proof using completeness and the interval conditions.</p>',
'appE-technology-notes':r'<p>This appendix explains graphing windows, finite precision, calculator syntax, and Python experiments. Use reference values and mathematical error estimates to check numerical results, and account for the sampling limitations of plots.</p>',
'sec-e-3-calculator-and-cas-syntax':r'<p>Calculator and computer-algebra inputs require explicit syntax. Parentheses, multiplication signs, and angle settings affect how an expression is evaluated. Check the interpretation of the input as well as the returned value.</p>',
'sec-e-4-simple-python-experiments-for-calculus':r'<p>These short Python examples implement numerical calculations from the book. Some use the built-in <c>math</c> module. Check their results against the known formulas and error estimates; plotting examples appear in the next section.</p>',
'appF-tables':r'<p>These tables provide quick reference to formulas and tests developed in the text. Check the domain and hypotheses before using a formula, and include an applicable error bound or qualified estimate when reporting numerical accuracy. Trigonometric arguments are in radians unless stated otherwise.</p>',
'sec-f-3-common-taylor-series':r'<p>The following series represent their functions on the stated domains. Constructing Taylor coefficients alone does not prove representation; the Taylor remainder must tend to zero.</p>',
}
for xid,new in edits.items():opening(xid,'Replace appendix-opening filler or unsupported generalizations with scope and conditions.',new)
replace('sec-11-6-computer-algebra-systems-and-integral-tables','Replace personification in a substitution explanation.',
 'But the numerator is <m>dx</m>, while the table formula wants <m>du</m>.',
 'The numerator uses <m>dx</m>, whereas the table formula requires <m>du</m>.')
print('Appendix-language corrections:',len(edits)+1)
