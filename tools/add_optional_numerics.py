"""One-time authoring of optional numerical topics; do not replay."""
from pathlib import Path
from html import escape
import json, math
from lxml import etree as ET
from selected_numerical_methods import ode_step
ROOT=Path(__file__).resolve().parents[1]
CH=ROOT/'source/chapters'
changes=json.loads((ROOT/'qa/additions/changed-source.json').read_text('utf-8'))
def add(chapter, filename, content):
    folder=next(CH.glob(chapter+'*'))
    p=folder/'sections'/filename
    assert not p.exists(), p
    ET.fromstring(content.encode())
    p.write_text(content.strip()+'\n',encoding='utf-8')
    cp=next(folder.glob('*.ptx'))
    old=cp.read_text('utf-8')
    cp.write_text(old.replace('</chapter>',f'  <xi:include href="sections/{filename}"/>\n\n</chapter>'),encoding='utf-8')
    changes.extend([str(p.relative_to(ROOT)),str(cp.relative_to(ROOT))])

add('ch12-', 'sec-additional-richardson-romberg.xml', r'''
<section xml:id="sec-additional-richardson-romberg">
  <title>Additional topics: Richardson and Romberg methods</title>
  <introduction><p>Refining a numerical rule makes its error smaller. If we know how the leading error depends on the step size, two approximations can also cancel that error. This optional section extends the midpoint, trapezoidal, Simpson, and numerical-differentiation methods already developed in this chapter.</p></introduction>
  <subsection xml:id="subsec-richardson-extrapolation"><title>Cancel a leading error term</title>
    <p>Suppose an approximation to <m>I</m> has the expansion</p><p><me>A(h)=I+ch^p+O(h^{p+r}),\qquad p,r&gt;0,</me></p><p>where the same coefficient <m>c</m> applies at <m>h</m> and <m>h/2</m>. Here <m>O(h^s)</m> means an absolute value bounded by a fixed constant times <m>h^s</m> for all sufficiently small positive <m>h</m>. Then <m>A(h/2)=I+c h^p/2^p+O(h^{p+r})</m>. Multiplying the finer value by <m>2^p</m> and subtracting cancels the leading error:</p><p><me>Q(h)=\frac{2^pA(h/2)-A(h)}{2^p-1}=I+O(h^{p+r}).</me></p><p>This is <em>Richardson extrapolation</em>. In the same regime,</p><p><me>I-A(h/2)\approx\frac{A(h/2)-A(h)}{2^p-1}.</me></p><p>The difference gives an error <em>estimate</em> only while the assumed expansion describes the actual calculation. Cancellation, insufficient smoothness, or rounding can invalidate this interpretation.</p>
    <example xml:id="ex-richardson-centered-difference"><title>Improve a numerical derivative</title><p>If <m>f</m> has five continuous derivatives near <m>x</m>, finite Taylor expansions give</p><p><me>D(h)=\frac{f(x+h)-f(x-h)}{2h}=f'(x)+\frac{f^{(3)}(x)}6h^2+O(h^4).</me></p><p>Thus <m>(4D(h/2)-D(h))/3</m> approximates <m>f'(x)</m> with error <m>O(h^4)</m>. This does not remove the division by a small number: at very small <m>h</m>, subtracting nearly equal function values can make rounding dominate.</p></example>
  </subsection>
  <subsection xml:id="subsec-romberg-integration"><title>Repeated extrapolation of trapezoidal rules</title>
    <p>For a sufficiently smooth function on <m>[a,b]</m>, the composite trapezoidal rule has an expansion in even powers of its uniform mesh width:</p><p><me>T(h)=I+c_2h^2+c_4h^4+\cdots+c_{2m}h^{2m}+O(h^{2m+2}).</me></p><p>One sufficient condition for this expansion through the displayed order is that <m>f</m> have <m>2m+2</m> continuous derivatives on the interval. It comes from Taylor expansion on the panels and summing their endpoint contributions. The first coefficient is <m>c_2=(f'(b)-f'(a))/12</m>; symmetry removes the odd powers. This expansion is stronger information than the trapezoidal error bound alone.</p>
    <p>Let <m>h_k=(b-a)/2^k</m>. Set <m>R_{k,0}=T(h_k)</m> and form the triangular <em>Romberg table</em> by</p><p><me>R_{k,j}=R_{k,j-1}+\frac{R_{k,j-1}-R_{k-1,j-1}}{4^j-1},\qquad 1\le j\le k.</me></p><p>Column <m>j</m> cancels the leading term of order <m>h^{2j}</m> left by the preceding column. For each fixed <m>j</m>, under sufficient smoothness its error is <m>O(h_k^{2j+2})</m>. This is an asymptotic statement as the mesh is refined; it does not promise that every new diagonal entry improves a finite-precision calculation.</p>
    <p>Each refinement reuses previous function values:</p><p><me>R_{k,0}=\frac12R_{k-1,0}+h_k\sum_{i=1}^{2^{k-1}}f(a+(2i-1)h_k).</me></p><p>Only the newly inserted midpoints are evaluated. The first extrapolated column is exactly the composite Simpson rule on that grid: <m>R_{k,1}=(4T(h_k)-T(2h_k))/3</m>.</p>
    <example xml:id="ex-romberg-quartic"><title>An exactly checkable table</title><p>For <m>f(x)=x^4</m> on <m>[0,1]</m>, <m>I=1/5</m> and direct finite summation gives <m>T(h)=1/5+h^2/3-h^4/30</m>.</p>
      <table xml:id="tab-romberg-quartic"><title>Romberg integration of <m>x^4</m></title><tabular width="100%" halign="left"><col width="10%"/><col width="30%"/><col width="30%"/><col width="30%"/>
        <row header="yes"><cell><p><m>k</m></p></cell><cell><p><m>R_{k,0}</m></p></cell><cell><p><m>R_{k,1}</m></p></cell><cell><p><m>R_{k,2}</m></p></cell></row>
        <row><cell><p>0</p></cell><cell><p>0.5000000000</p></cell><cell><p>—</p></cell><cell><p>—</p></cell></row>
        <row><cell><p>1</p></cell><cell><p>0.2812500000</p></cell><cell><p>0.2083333333</p></cell><cell><p>—</p></cell></row>
        <row><cell><p>2</p></cell><cell><p>0.2207031250</p></cell><cell><p>0.2005208333</p></cell><cell><p>0.2000000000</p></cell></row>
      </tabular></table><p>The second extrapolation cancels the <m>h^4</m> term, leaving the exact integral in exact arithmetic.</p>
    </example>
    <paragraphs><title>A practical stopping policy</title><p>Choose a tolerance <m>\tau=\tau_{\rm abs}+\tau_{\rm rel}|R_{k,k}|</m> with <m>\tau_{\rm abs}&gt;0</m>, <m>\tau_{\rm rel}\ge0</m>. One policy requires at least three refinements and two consecutive diagonal changes below the current tolerance. Also impose a maximum refinement level and function-evaluation budget, reject nonfinite values, and stop with a failure report if the mesh cannot be represented or the changes cease decreasing while the tolerance is unmet. Report the latest diagonal change as an estimate, not a certified bound. A known derivative bound or other rigorous remainder estimate is needed for a certified stopping decision.</p></paragraphs>
    <warning xml:id="warn-romberg-smoothness"><title>The expansion has hypotheses</title><p>For <m>f(x)=\sqrt{x}</m> on <m>[0,1]</m>, derivatives blow up at zero and the usual even-power expansion is unavailable. Applying the Romberg recurrence is still possible, but the advertised orders no longer follow. Increasing the table depth cannot repair an unjustified error model.</p></warning>
    <exercise xml:id="exr-romberg"><title>Derive and test an extrapolation</title><statement><p>If <m>A(h)=I+ch^3+O(h^4)</m>, find the Richardson combination. Build the first three Romberg rows for <m>\int_0^1x^2\,dx</m>. Which column first gives the exact result, and why?</p></statement><hint><p>Use <m>(8A(h/2)-A(h))/7</m>. For the quadratic, <m>T(h)=1/3+h^2/6</m>, so the first extrapolated column is exact.</p></hint></exercise>
  </subsection>
</section>
''')

code=(ROOT/'tools/selected_numerical_methods.py').read_text('utf-8')
adaptive=code[:code.index('\n\ndef ode_step')]
add('ch12-', 'sec-additional-adaptive-quadrature.xml', r'''
<section xml:id="sec-additional-adaptive-quadrature">
  <title>Additional topics: a complete adaptive quadrature algorithm</title>
  <introduction><p>The computing experiments refined a uniform grid. Adaptive quadrature instead subdivides individual intervals where an error indicator is large. This optional section supplies a complete adaptive Simpson algorithm, an absolute-tolerance stopping rule, and explicit failure safeguards. Its Richardson estimate uses <xref ref="sec-additional-richardson-romberg"/>.</p></introduction>
  <subsection xml:id="subsec-adaptive-simpson-estimate"><title>Compare one panel with two</title>
    <p>On <m>[a,b]</m>, put <m>m=(a+b)/2</m> and</p><p><me>S(a,b)=\frac{b-a}{6}\bigl(f(a)+4f(m)+f(b)\bigr).</me></p><p>Compare <m>S_1=S(a,b)</m> with <m>S_2=S(a,m)+S(m,b)</m>. In the smooth asymptotic regime, halving the mesh reduces the leading Simpson error by a factor of <m>16</m>. Therefore</p><p><me>E\approx\frac{|S_2-S_1|}{15},\qquad Q=S_2+\frac{S_2-S_1}{15}.</me></p><p>The difference divided by <m>15</m> estimates the error of <m>S_2</m>; the correction <m>Q</m> cancels its leading term. With a smooth enough integrand, <m>Q</m> has a higher order than <m>S_2</m>. We retain the more conservative indicator <m>E</m> for accepting the interval.</p>
    <p>Give the whole interval an absolute error budget <m>\tau&gt;0</m>. When an interval is split, give each child half its parent's budget. Accept a leaf when its indicator is at most its budget. The leaf budgets sum to <m>\tau</m>, so the sum of the accepted indicators is at most <m>\tau</m>. This is an accounting guarantee for the indicators, not a theorem that every possible integrand has that actual error.</p>
  </subsection>
  <subsection xml:id="subsec-adaptive-simpson-algorithm"><title>An implementation with explicit outcomes</title>
    <p>The following Python implementation assumes a finite-valued integrand throughout a finite interval <m>a&lt;b</m>. It returns the approximation, the summed error indicator, the number of function evaluations, and the accepted intervals. It uses a stack rather than unbounded recursion, reuses parent samples, and performs at least two subdivision levels by default to reduce premature acceptance. Exhausting the depth or evaluation budget, encountering a nonfinite value, or losing representable midpoints raises a failure instead of reporting success. The roundoff indicator <m>50\epsilon_{\rm mach}(|S_L|+|S_R|)</m> is a practical scale check, where <m>\epsilon_{\rm mach}</m> is the spacing from one to the next larger floating-point number. It is not a bound on all floating-point errors.</p>
    <pre>''' + escape(adaptive.rstrip()) + r'''</pre>
    <p>The stopping rule is implemented in the acceptance branch and checked again after accumulation. The minimum depth does not override the maximum depth, and all resource limits have explicit outcomes. If the routine fails, increase resources only after examining the reason; a singularity or unattainable tolerance may require a change of variables or an analytic treatment.</p>
  </subsection>
  <subsection xml:id="subsec-adaptive-safeguards"><title>Test cases and the limits of sampling</title>
    <example xml:id="ex-adaptive-pi"><title>A known integral</title><p>Calling <c>adaptive_simpson(lambda x: 4/(1+x*x), 0, 1, 1e-8)</c> approximates <m>\pi</m>. Compare the returned value with <m>\pi</m> and record the indicator and evaluation count. For a more localized problem, try <m>f(x)=e^{-2500(x-0.37)^2}</m> on <m>[0,1]</m> and plot the accepted interval widths. Small intervals should cluster near the peak. Compare with a high-accuracy reference calculation; do not infer accuracy from the indicator alone.</p></example>
    <warning xml:id="warn-adaptive-aliasing"><title>A small indicator cannot certify an arbitrary function</title><p>On <m>[0,1]</m>, the nonnegative polynomial</p><p><me>g(x)=\prod_{j=0}^{16}(x-j/16)^2</me></p><p>vanishes at every point sampled before the default minimum-depth acceptance decisions. The algorithm can return zero with zero indicator, although the integral is positive. This is <em>sampling aliasing</em>: the data miss the behavior between samples. More initial panels, independent shifted samples, and known breakpoints reduce the risk; no finite sampling scheme alone certifies all continuous functions.</p></warning>
    <paragraphs><title>How a derivative bound changes the guarantee</title><p>If a valid bound <m>|f^{(4)}|\le K</m> is known on a leaf of width <m>w</m>, the two-panel Simpson value <m>S_2</m> has the rigorous exact-arithmetic bound</p><p><me>\left|\int_a^b f-S_2\right|\le\frac{Kw^5}{46080}.</me></p><p>Each half-panel contributes at most <m>K(w/2)^5/2880</m>, and adding the two bounds gives this constant. A certified variant accepts leaves using this derivative bound and returns the uncorrected <m>S_2</m>, summing the valid leaf bounds. It must also account for floating-point evaluation and accumulation errors. The corrected value <m>Q</m> requires its own error analysis; the bound for <m>S_2</m> cannot simply be attached to it.</p></paragraphs>
    <exercise xml:id="exr-adaptive-safeguards"><title>Test success and failure paths</title><statement><p>Check the routine on <m>1,x,x^2,x^3,x^4</m> over <m>[0,1]</m>. Force separate failures with an evaluation budget of three, maximum depth zero, a nonfinite function value, and adjacent floating-point endpoints. Use <m>\int_0^1x^k\,dx=1/(k+1)</m> as the reference. Explain why the aliasing example is a more demanding test than the cubic examples.</p></statement><hint><p>For the depth test set <c>min_depth=0</c> and use a noncubic integrand with a small tolerance. Cubics are exactly integrated by Simpson's rule in exact arithmetic. The aliasing polynomial has positive area but supplies zeros at all sampled points, so exact sample arithmetic would still miss it.</p></hint></exercise>
  </subsection>
</section>
''')

rows=[]
for n in (4,8,16):
    errors=[]
    for method in ('Euler','Heun','RK4'):
        y=1.0
        for k in range(n): y=ode_step(lambda t,y:y,k/n,y,1/n,method)
        errors.append(abs(math.e-y))
    rows.append('<row><cell><p>'+str(n)+'</p></cell>'+''.join(
        '<cell><p><m>'+f'{e:.6g}'.replace('e-',r'\times10^{-')+('}' if 'e-' in f'{e:.6g}' else '')+'</m></p></cell>' for e in errors)+'</row>')
add('ch13-', 'sec-additional-runge-kutta.xml', r'''
<section xml:id="sec-additional-runge-kutta">
  <title>Additional topics: Runge–Kutta methods</title>
  <introduction><p>Euler's method advances with one slope at the start of a step. Runge–Kutta methods sample additional slopes to approximate the change more accurately. This optional section compares explicit Euler, improved Euler (Heun), midpoint, and classical fourth-order Runge–Kutta methods. It assumes an initial value problem with a smooth solution on the interval being computed.</p></introduction>
  <subsection xml:id="subsec-runge-kutta-formulas"><title>Two slopes and four slopes</title>
    <p>For <m>y'=F(t,y)</m>, use a step from <m>(t_n,y_n)</m> to <m>t_n+h</m>. Explicit Euler is <m>y_{n+1}=y_n+hF(t_n,y_n)</m>. Heun's method predicts with Euler and averages the initial and predicted final slopes:</p><p><md><mrow>k_1\amp=F(t_n,y_n),</mrow><mrow>k_2\amp=F(t_n+h,y_n+hk_1),</mrow><mrow>y_{n+1}\amp=y_n+\tfrac h2(k_1+k_2).</mrow></md></p><p>The explicit midpoint method uses the initial slope to predict the midpoint, then uses its slope for the whole step:</p><p><me>k_1=F(t_n,y_n),\qquad k_2=F(t_n+h/2,y_n+hk_1/2),\qquad y_{n+1}=y_n+hk_2.</me></p><p>Both are second-order methods, but they need not give the same value on a nonlinear equation. Here the <m>k_i</m> are slopes; the factor <m>h</m> is applied when forming changes.</p>
    <note xml:id="note-rk4-formula"><title>Classical RK4</title><p><md><mrow>k_1\amp=F(t_n,y_n),</mrow><mrow>k_2\amp=F(t_n+h/2,y_n+hk_1/2),</mrow><mrow>k_3\amp=F(t_n+h/2,y_n+hk_2/2),</mrow><mrow>k_4\amp=F(t_n+h,y_n+hk_3),</mrow><mrow>y_{n+1}\amp=y_n+\tfrac h6(k_1+2k_2+2k_3+k_4).</mrow></md></p></note><p>The two midpoint slopes are evaluated at different predicted values of <m>y</m>. Replacing one by the other changes the method. For a system, apply the same formulas to vector values, evaluating all components of each stage together.</p>
  </subsection>
  <subsection xml:id="subsec-runge-kutta-accuracy"><title>Local error and accumulated error</title>
    <p>The <em>one-step local error</em> is the difference between an exact solution value at the end of a step and one numerical step started from the exact value at its beginning. A method has order <m>p</m> when this error is <m>O(h^{p+1})</m> and its accumulated, or <em>global</em>, error over a fixed finite interval is <m>O(h^p)</m>. Some texts divide the local error by <m>h</m>; here we do not.</p>
    <p>For the following orders, assume <m>F</m> and its partial derivatives through order four are continuous and bounded in a neighborhood containing the exact and numerical trajectories, and <m>F</m> is Lipschitz in <m>y</m> there. A partial derivative in <m>t</m> or <m>y</m> means varying that input while holding the other fixed. The initial value is exact, the interval length is fixed, and the stated orders describe exact arithmetic as <m>h\to0</m>.</p>
    <table xml:id="tab-runge-kutta-orders"><title>Orders and slope costs</title><tabular width="100%" halign="left"><col width="31%"/><col width="23%"/><col width="23%"/><col width="23%"/>
      <row header="yes"><cell><p>Method</p></cell><cell><p>Slopes per step</p></cell><cell><p>Local error</p></cell><cell><p>Global error</p></cell></row>
      <row><cell><p>Explicit Euler</p></cell><cell><p>1</p></cell><cell><p><m>O(h^2)</m></p></cell><cell><p><m>O(h)</m></p></cell></row>
      <row><cell><p>Heun or midpoint</p></cell><cell><p>2</p></cell><cell><p><m>O(h^3)</m></p></cell><cell><p><m>O(h^2)</m></p></cell></row>
      <row><cell><p>Classical RK4</p></cell><cell><p>4</p></cell><cell><p><m>O(h^5)</m></p></cell><cell><p><m>O(h^4)</m></p></cell></row>
    </tabular></table>
    <p>To see the second-order match, write <m>F_t,F_y</m> for the two derivatives at the starting point. Along an exact solution, <m>y''=F_t+F_yF</m>. Expanding the final slope in Heun's method gives <m>k_2=F+h(F_t+F_yF)+O(h^2)</m>; its averaged update is <m>y+hF+\tfrac12h^2(F_t+F_yF)+O(h^3)</m>, matching the exact Taylor expansion through degree two. The midpoint calculation gives the same degree-two match.</p>
    <p>For RK4, Taylor expansion of all four stages matches the exact solution through degree four. One compact way to state this calculation is to define <m>DG=G_t+FG_y</m> for any smooth function <m>G(t,y)</m>. The exact change and the RK4 change both have the expansion</p><p><me>hF+\frac{h^2}{2}DF+\frac{h^3}{6}D^2F+\frac{h^4}{24}D^3F+O(h^5),</me></p><p>with all terms evaluated at the start. Here <m>D^2F=D(DF)</m> and <m>D^3F=D(D^2F)</m>. The weights alone are not a quadrature proof: the predicted stage values must also produce this Taylor match.</p>
    <p>The loss of one power in global error comes from accumulating about <m>1/h</m> steps. More precisely, smoothness gives a one-step perturbation bound <m>1+Ch</m> for some fixed <m>C\ge0</m>. If the local error is at most <m>Kh^{p+1}</m>, then the global errors satisfy <m>e_{n+1}\le(1+Ch)e_n+Kh^{p+1}</m>. Iterating this inequality over <m>nh\le T</m> gives <m>e_n\le KTh^p e^{CT}</m> when <m>e_0=0</m>. This explains why local accuracy needs both smoothness and control of error propagation.</p>
    <example xml:id="ex-runge-kutta-errors"><title>A reproducible accuracy comparison</title><p>For <m>y'=y</m>, <m>y(0)=1</m>, the exact endpoint is <m>y(1)=e</m>. With <m>h=1/n</m>, the one-step multipliers are <m>1+h</m> for Euler, <m>1+h+h^2/2</m> for Heun and midpoint, and <m>1+h+h^2/2+h^3/6+h^4/24</m> for RK4. Raise each multiplier to the <m>n</m>-th power to reproduce these endpoint absolute errors:</p>
      <table xml:id="tab-runge-kutta-errors"><title>Absolute errors at time one</title><tabular width="100%" halign="left"><col width="10%"/><col width="30%"/><col width="30%"/><col width="30%"/>
        <row header="yes"><cell><p><m>n</m></p></cell><cell><p>Euler</p></cell><cell><p>Heun</p></cell><cell><p>RK4</p></cell></row>
        '''+'\n'.join(rows)+r'''
      </tabular></table><p>Halving the step eventually divides the error by roughly <m>2</m>, <m>4</m>, and <m>16</m>, respectively. At equal slope-evaluation cost, compare Euler with <m>4n</m> steps, Heun with <m>2n</m> steps, and RK4 with <m>n</m> steps; equal step counts alone do not give equal work.</p>
    </example>
    <warning xml:id="warn-runge-kutta-stability"><title>Higher order does not remove stability restrictions</title><p>For <m>y'=\lambda y</m>, RK4 advances with multiplier <m>P(z)=1+z+z^2/2+z^3/6+z^4/24</m>, where <m>z=h\lambda</m>. On <m>y'=-4y</m>, choosing <m>h=1</m> gives <m>P(-4)=5</m>, so the numerical values grow although the exact solution decays. A higher-order explicit method still needs a suitable step. Nonsmooth laws, long time intervals, rapidly decaying components, and roundoff require separate attention.</p></warning>
    <exercise xml:id="exr-runge-kutta"><title>Compare accuracy at equal cost</title><statement><p>Approximate <m>y(1)</m> for <m>y'=t+y</m>, <m>y(0)=1</m>, using Euler with <m>16</m> steps, Heun with <m>8</m>, and RK4 with <m>4</m>. Each uses <m>16</m> slope evaluations. Compare with <m>y(t)=2e^t-t-1</m>. Repeat with twice as many evaluations. Also verify the RK4 multiplier on the test equation.</p></statement><hint><p>Use the correct time in every stage. Expected error ratios approach <m>2,4,16</m> as the step shrinks. Successive substitutions in the four stages give the degree-four polynomial multiplier.</p></hint></exercise>
  </subsection>
</section>
''')
(ROOT/'qa/additions/changed-source.json').write_text(json.dumps(sorted(set(changes)),indent=2),encoding='utf-8')
print('Added three optional numerical sections.')

