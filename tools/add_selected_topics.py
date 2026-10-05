"""One-time authoring script for the maintainer's selected additions.

Do not replay against an already expanded manuscript. Editable content is in source/.
"""
from pathlib import Path
import hashlib, json
from lxml import etree as ET

ROOT = Path(__file__).resolve().parents[1]
CH = ROOT / 'source/chapters'
QA = ROOT / 'qa/additions'
QA.mkdir(exist_ok=True)
baseline = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in (ROOT / 'source').rglob('*') if p.suffix in {'.xml', '.ptx'}}
(QA / 'source-before.json').write_text(json.dumps(baseline, indent=2), encoding='utf-8')
changes = []

def insert(chapter, filename, text, before='</section>'):
    p = next(CH.glob(chapter + '*')) / 'sections' / filename
    old = p.read_text('utf-8')
    assert text.split('xml:id="', 1)[1].split('"', 1)[0] not in old
    assert old.count(before) == 1, (p, before)
    new = old.replace(before, text.strip() + '\n\n  ' + before)
    ET.fromstring(new.encode())
    p.write_text(new, encoding='utf-8')
    changes.append(str(p.relative_to(ROOT)))

insert('ch05-', 'sec-5-8-general-power-rule-and-hyperbolic-functions.xml', r'''
  <subsection xml:id="subsec-inverse-hyperbolic-functions">
    <title>Inverse hyperbolic functions: branches and derivatives</title>
    <p>The identity <m>\cosh^2 t-\sinh^2 t=1</m> gives the derivatives of the inverses once we choose their branches. We use the names <m>\operatorname{arsinh}</m>, <m>\operatorname{arcosh}</m>, and <m>\operatorname{artanh}</m> to avoid confusing an inverse with a reciprocal. For example, <m>\operatorname{arsinh}x</m> is an inverse function, whereas <m>\operatorname{csch}x=1/\sinh x</m>.</p>
    <p>Complete the family by defining <m>\coth t=\cosh t/\sinh t</m> and <m>\operatorname{csch}t=1/\sinh t</m> for <m>t\ne0</m>. The quotient and reciprocal rules give</p>
    <p><me>(\coth t)'=-\operatorname{csch}^2t,\qquad
      (\operatorname{sech}t)'=-\operatorname{sech}t\tanh t,\qquad
      (\operatorname{csch}t)'=-\operatorname{csch}t\coth t.</me></p>
    <p>Since <m>\cosh t&gt;0</m>, <m>\sinh</m> is strictly increasing from <m>\mathbb R</m> onto <m>\mathbb R</m>. The function <m>\tanh</m> is strictly increasing from <m>\mathbb R</m> onto <m>(-1,1)</m>. The even functions <m>\cosh</m> and <m>\operatorname{sech}</m> must be restricted to <m>t\ge0</m> to have inverses. For <m>\coth</m> and <m>\operatorname{csch}</m>, the positive and negative branches have disjoint ranges, so both branches can be inverted together.</p>
    <table xml:id="tab-inverse-hyperbolic-branches">
      <title>Real inverse hyperbolic functions</title>
      <tabular width="100%" halign="left"><col width="25%"/><col width="35%"/><col width="40%"/>
        <row header="yes"><cell><p>Inverse</p></cell><cell><p>Domain</p></cell><cell><p>Range (chosen branch)</p></cell></row>
        <row><cell><p><m>\operatorname{arsinh}x</m></p></cell><cell><p><m>\mathbb R</m></p></cell><cell><p><m>\mathbb R</m></p></cell></row>
        <row><cell><p><m>\operatorname{arcosh}x</m></p></cell><cell><p><m>[1,\infty)</m></p></cell><cell><p><m>[0,\infty)</m></p></cell></row>
        <row><cell><p><m>\operatorname{artanh}x</m></p></cell><cell><p><m>(-1,1)</m></p></cell><cell><p><m>\mathbb R</m></p></cell></row>
        <row><cell><p><m>\operatorname{arcoth}x</m></p></cell><cell><p><m>(-\infty,-1)\cup(1,\infty)</m></p></cell><cell><p><m>\mathbb R\setminus\{0\}</m></p></cell></row>
        <row><cell><p><m>\operatorname{arsech}x</m></p></cell><cell><p><m>(0,1]</m></p></cell><cell><p><m>[0,\infty)</m></p></cell></row>
        <row><cell><p><m>\operatorname{arcsch}x</m></p></cell><cell><p><m>\mathbb R\setminus\{0\}</m></p></cell><cell><p><m>\mathbb R\setminus\{0\}</m></p></cell></row>
      </tabular>
    </table>
    <p>Solving the exponential definitions gives logarithmic formulas on precisely these domains:</p>
    <p><md>
      <mrow>\operatorname{arsinh}x\amp=\ln(x+\sqrt{x^2+1}),</mrow>
      <mrow>\operatorname{arcosh}x\amp=\ln(x+\sqrt{x^2-1}),</mrow>
      <mrow>\operatorname{artanh}x\amp=\tfrac12\ln\frac{1+x}{1-x},</mrow>
      <mrow>\operatorname{arcoth}x\amp=\tfrac12\ln\frac{x+1}{x-1},</mrow>
      <mrow>\operatorname{arsech}x\amp=\ln\frac{1+\sqrt{1-x^2}}{x},</mrow>
      <mrow>\operatorname{arcsch}x\amp=\operatorname{arsinh}(1/x)
       =\ln\left(\frac1x+\sqrt{1+\frac1{x^2}}\right).</mrow>
    </md></p>
    <p>For example, write <m>x=\sinh y</m> and set <m>z=e^y&gt;0</m>. Then <m>z^2-2xz-1=0</m>, whose positive root is <m>x+\sqrt{x^2+1}</m>. Taking its logarithm proves the first formula. For <m>x=\cosh y</m>, the roots are <m>x\pm\sqrt{x^2-1}</m>; the branch <m>y\ge0</m> selects the plus sign. Solving <m>x=(e^{2y}-1)/(e^{2y}+1)</m> proves the formula for <m>\operatorname{artanh}</m>. The other formulas follow by taking reciprocals in these three inverse relations.</p>
    <figure xml:id="fig-inverse-hyperbolic-branches">
      <caption>The three basic inverse branches. The branch of <m>\operatorname{arcosh}</m> begins at <m>(1,0)</m>; <m>\operatorname{artanh}</m> has vertical asymptotes at <m>x=\pm1</m>.</caption>
      <image width="85%"><description><p>Separate plots of arsinh on the real line, arcosh for x at least one, and artanh between minus one and one, with dashed vertical asymptotes for artanh.</p></description><latex-image>
\begin{tikzpicture}
\begin{axis}[width=0.30\textwidth,height=0.29\textwidth,xmin=-3,xmax=3,ymin=-2.4,ymax=2.4,axis lines=middle,xlabel={$x$},title={$\operatorname{arsinh}x$},xtick={-2,0,2},ytick={-2,0,2}]
\addplot[thick,domain=-3:3,samples=100]{ln(x+sqrt(x*x+1))};
\end{axis}
\begin{axis}[at={(0.34\textwidth,0)},anchor=south west,width=0.30\textwidth,height=0.29\textwidth,xmin=0,xmax=4,ymin=-0.2,ymax=2.4,axis lines=middle,xlabel={$x$},title={$\operatorname{arcosh}x$},xtick={1,2,3,4},ytick={0,1,2}]
\addplot[thick,domain=1:4,samples=150]{ln(x+sqrt(x*x-1))};
\addplot[only marks,mark=*] coordinates {(1,0)};
\end{axis}
\begin{axis}[at={(0.68\textwidth,0)},anchor=south west,width=0.30\textwidth,height=0.29\textwidth,xmin=-1.25,xmax=1.25,ymin=-2.4,ymax=2.4,axis lines=middle,xlabel={$x$},title={$\operatorname{artanh}x$},xtick={-1,0,1},ytick={-2,0,2}]
\addplot[thick,domain=-0.98:0.98,samples=150]{0.5*ln((1+x)/(1-x))};
\draw[dashed] (axis cs:-1,-2.4)--(axis cs:-1,2.4);
\draw[dashed] (axis cs:1,-2.4)--(axis cs:1,2.4);
\end{axis}
\end{tikzpicture}
      </latex-image></image>
    </figure>
    <note xml:id="note-inverse-hyperbolic-derivatives"><title>Derivative formulas and their domains</title>
      <p><md>
        <mrow>(\operatorname{arsinh}x)'\amp=\frac1{\sqrt{1+x^2}},\quad x\in\mathbb R,</mrow>
        <mrow>(\operatorname{arcosh}x)'\amp=\frac1{\sqrt{x^2-1}},\quad x&gt;1,</mrow>
        <mrow>(\operatorname{artanh}x)'\amp=\frac1{1-x^2},\quad |x|&lt;1,</mrow>
        <mrow>(\operatorname{arcoth}x)'\amp=\frac1{1-x^2},\quad |x|&gt;1,</mrow>
        <mrow>(\operatorname{arsech}x)'\amp=-\frac1{x\sqrt{1-x^2}},\quad 0&lt;x&lt;1,</mrow>
        <mrow>(\operatorname{arcsch}x)'\amp=-\frac1{|x|\sqrt{1+x^2}},\quad x\ne0.</mrow>
      </md></p>
    </note>
    <p>For <m>y=\operatorname{arsinh}x</m>, implicit differentiation gives <m>1=\cosh y\,y'</m>. Since <m>\cosh y=\sqrt{1+x^2}&gt;0</m>, the first derivative follows. For <m>y=\operatorname{arcosh}x</m> with <m>x&gt;1</m>, we have <m>y&gt;0</m> and <m>\sinh y=\sqrt{x^2-1}</m>. For <m>\operatorname{artanh}</m> and <m>\operatorname{arcoth}</m>, the logarithmic formulas immediately give <m>1/(1-x^2)</m>. Finally, <m>\operatorname{arsech}x=\operatorname{arcosh}(1/x)</m> and <m>\operatorname{arcsch}x=\operatorname{arsinh}(1/x)</m>; the chain rule gives the last two formulas. In the last calculation, <m>\sqrt{1+1/x^2}=\sqrt{1+x^2}/|x|</m>, so the absolute value cannot be dropped.</p>
    <warning xml:id="warn-inverse-hyperbolic-endpoints"><title>The endpoints still matter</title><p>The functions <m>\operatorname{arcosh}</m> and <m>\operatorname{arsech}</m> are defined at <m>x=1</m>, but they have no finite one-sided derivative there. Also, <m>\operatorname{arcosh}(\cosh t)=|t|</m>, whereas <m>\operatorname{arsinh}(\sinh t)=t</m>. The restriction used to define an inverse remains part of the answer.</p></warning>
    <example xml:id="ex-inverse-hyperbolic-chain"><title>A derivative with a branch restriction</title><p>For <m>x&gt;0</m>, put <m>g(x)=\operatorname{arcosh}(1+x^2)</m>. Then</p><p><me>g'(x)=\frac{2x}{\sqrt{(1+x^2)^2-1}}=\frac2{\sqrt{x^2+2}}.</me></p><p>On <m>x&lt;0</m> the answer has the opposite sign, because the square root in the denominator is <m>|x|\sqrt{x^2+2}</m>. At zero the resulting two one-sided slopes disagree.</p></example>
    <exercise xml:id="exr-inverse-hyperbolic-derivatives"><title>Check the inverses</title><statement><p>Differentiate <m>\operatorname{arsinh}(x^2)</m>, <m>\operatorname{artanh}(2x)</m>, and <m>\operatorname{arcsch}(-x)</m>. State each domain. Explain why <m>\operatorname{arcosh}(\cosh x)</m> is not differentiable at zero.</p></statement><hint><p>The derivatives are <m>2x/\sqrt{1+x^4}</m> on <m>\mathbb R</m>, <m>2/(1-4x^2)</m> on <m>(-1/2,1/2)</m>, and <m>1/(|x|\sqrt{1+x^2})</m> for <m>x\ne0</m>. The last composition is <m>|x|</m>.</p></hint></exercise>
    <p>These derivatives will supply antiderivatives in <xref ref="subsec-inverse-hyperbolic-integrals"/> when integration has been developed. For another treatment of this family, see <url href="https://openstax.org/books/calculus-volume-2/pages/2-9-calculus-of-the-hyperbolic-functions">OpenStax, Calculus Volume 2, Section 2.9</url>.</p>
  </subsection>
''', before='  <subsection xml:id="subsec-hanging-cables-hyperbolic-functions">')

insert('ch11-', 'sec-11-3-trigonometric-substitution.xml', r'''
  <subsection xml:id="subsec-inverse-hyperbolic-integrals">
    <title>Integrals and inverse hyperbolic functions</title>
    <p>The derivatives in <xref ref="subsec-inverse-hyperbolic-functions"/> organize several square-root and rational integrals. For a constant <m>a&gt;0</m>, substitution <m>u=x/a</m> gives</p>
    <p><md>
      <mrow>\int\frac{dx}{\sqrt{x^2+a^2}}\amp=\operatorname{arsinh}(x/a)+C,\quad x\in\mathbb R,</mrow>
      <mrow>\int\frac{dx}{\sqrt{x^2-a^2}}\amp=\operatorname{arcosh}(x/a)+C,\quad x&gt;a,</mrow>
      <mrow>\int\frac{dx}{\sqrt{x^2-a^2}}\amp=-\operatorname{arcosh}(-x/a)+C,\quad x&lt;-a,</mrow>
      <mrow>\int\frac{dx}{a^2-x^2}\amp=\frac1a\operatorname{artanh}(x/a)+C,\quad |x|&lt;a,</mrow>
      <mrow>\int\frac{dx}{a^2-x^2}\amp=\frac1a\operatorname{arcoth}(x/a)+C,\quad |x|&gt;a.</mrow>
    </md></p>
    <p>The logarithmic form <m>\ln|x+\sqrt{x^2-a^2}|+C</m> works on either interval <m>x&gt;a</m> or <m>x&lt;-a</m>, with an independent constant on each. The logarithmic form of the rational antiderivative is <m>\frac1{2a}\ln|(a+x)/(a-x)|+C</m>. It also works on each interval separated by <m>x=\pm a</m>. No antiderivative crosses either singularity.</p>
    <p>Two reciprocal patterns complete the list:</p>
    <p><md>
      <mrow>\int\frac{dx}{x\sqrt{a^2-x^2}}\amp=-\frac1a\operatorname{arsech}(|x|/a)+C,\quad 0&lt;|x|&lt;a,</mrow>
      <mrow>\int\frac{dx}{x\sqrt{a^2+x^2}}\amp=-\frac1a\operatorname{arcsch}(|x|/a)+C,\quad x\ne0.</mrow>
    </md></p>
    <p>Differentiate these formulas separately on the positive and negative intervals. The derivative of <m>|x|</m> supplies the sign needed to recover <m>1/x</m>. Using <m>\operatorname{arcsch}(x/a)</m> without the absolute value would give the wrong sign on the negative interval.</p>
    <example xml:id="ex-negative-hyperbolic-integral"><title>Choosing the negative branch</title><p>For <m>x&lt;-3</m>,</p><p><me>\int\frac{dx}{\sqrt{x^2-9}}=-\operatorname{arcosh}(-x/3)+C.</me></p><p>The chain-rule factors are <m>(-1)(-1/3)</m>, and <m>\sqrt{x^2/9-1}=\sqrt{x^2-9}/3</m>. Their product gives the positive integrand. The expression <m>\operatorname{arcosh}(x/3)</m> would not even be real on this interval.</p></example>
    <example xml:id="ex-integrating-inverse-hyperbolic"><title>Integrating an inverse function itself</title><p>Integration by parts with <m>u=\operatorname{arsinh}x</m> and <m>dv=dx</m> gives</p><p><me>\int\operatorname{arsinh}x\,dx=x\operatorname{arsinh}x-\sqrt{1+x^2}+C.</me></p><p>The same method gives <m>\int\operatorname{arcosh}x\,dx=x\operatorname{arcosh}x-\sqrt{x^2-1}+C</m> for <m>x&gt;1</m>, and <m>\int\operatorname{artanh}x\,dx=x\operatorname{artanh}x+\tfrac12\ln(1-x^2)+C</m> for <m>|x|&lt;1</m>. In each case differentiating the answer makes the two extra terms cancel.</p></example>
    <exercise xml:id="exr-inverse-hyperbolic-integrals"><title>Domains belong to an integral formula</title><statement><p>Evaluate <m>\int_0^2 dx/\sqrt{x^2+4}</m>, find an antiderivative of <m>1/(9-x^2)</m> on <m>(3,\infty)</m>, and find an antiderivative of <m>1/(x\sqrt{4-x^2})</m> on <m>(-2,0)</m>.</p></statement><hint><p>The answers are <m>\operatorname{arsinh}1=\ln(1+\sqrt2)</m>, <m>\tfrac13\operatorname{arcoth}(x/3)+C</m>, and <m>-\tfrac12\operatorname{arsech}(|x|/2)+C</m>. Differentiate the last answer using <m>|x|=-x</m>.</p></hint></exercise>
  </subsection>
''')

insert('ch11-', 'sec-11-7-improper-integrals.xml', r'''
  <subsection xml:id="subsec-absolute-conditional-improper-integrals">
    <title>Absolute and conditional convergence</title>
    <p>Cancellation can make a signed accumulation finite even when the total unsigned area is infinite. An improper integral <m>\int_a^\infty f(x)\,dx</m> is <em>absolutely convergent</em> if <m>\int_a^\infty|f(x)|\,dx</m> converges. It is <em>conditionally convergent</em> if the signed integral converges but the absolute-value integral diverges. Use the same definitions at a singular endpoint, and require convergence on every piece when several endpoints or singularities are involved.</p>
    <note xml:id="note-absolute-improper-implies-convergence"><title>Absolute convergence implies convergence</title><p>Assume <m>f</m> is continuous on each finite subinterval. Put <m>f_+=\max(f,0)</m> and <m>f_-=\max(-f,0)</m>. Both are nonnegative and bounded above by <m>|f|</m>. Comparison shows that their improper integrals converge if the integral of <m>|f|</m> does. Since <m>f=f_+-f_-</m>, the signed integral then converges too. Moreover, for any tail beginning at <m>R</m>,</p><p><me>\left|\int_R^\infty f(x)\,dx\right|\le\int_R^\infty|f(x)|\,dx.</me></p></note>
    <example xml:id="ex-absolutely-integrable-oscillation"><title>Oscillation with finite unsigned area</title><p>For <m>x\ge1</m>, <m>|\sin x|/x^2\le1/x^2</m>. Thus <m>\int_1^\infty \sin x/x^2\,dx</m> converges absolutely, and its tail after <m>R\ge1</m> has magnitude at most <m>1/R</m>.</p></example>
    <example xml:id="ex-conditionally-integrable-sine"><title>A convergent oscillation with infinite unsigned area</title><p>Consider <m>\int_1^\infty \sin x/x\,dx</m>. Integration by parts on a finite interval gives</p><p><me>\int_R^T\frac{\sin x}{x}\,dx=-\frac{\cos T}{T}+\frac{\cos R}{R}-\int_R^T\frac{\cos x}{x^2}\,dx.</me></p><p>The boundary term at <m>T</m> tends to zero, and the last integral converges absolutely by comparison with <m>1/x^2</m>. This proves convergence and the tail bound</p><p><me>\left|\int_R^\infty\frac{\sin x}{x}\,dx\right|\le\frac2R.</me></p><p>To test absolute convergence, use the disjoint intervals</p><p><me>J_k=[k\pi+\pi/6,k\pi+5\pi/6],\qquad k=1,2,\ldots.</me></p><p>On each <m>J_k</m>, <m>|\sin x|\ge1/2</m> and <m>x\le(k+1)\pi</m>. Therefore</p><p><me>\int_{J_k}\frac{|\sin x|}{x}\,dx\ge\frac{1}{3(k+1)}.</me></p><p>The partial sums of these lower bounds grow without bound: among indices with <m>2^j\le k+1&lt;2^{j+1}</m>, there are <m>2^j</m> terms, each at least <m>1/(3\cdot2^{j+1})</m>, so each group contributes at least <m>1/6</m>. The unsigned integral diverges. The original integral is conditionally convergent.</p></example>
    <figure xml:id="fig-conditional-improper-lobes"><caption>The signed lobes of <m>\sin x/x</m> cancel in the improper integral. Replacing the integrand by its absolute value turns every lobe upward and gives infinite area.</caption><image width="80%"><description><p>The graph of sine x divided by x from one to four pi, with positive lobes shaded blue and negative lobes shaded red, and a dashed absolute-value curve above the axis.</p></description><latex-image>
\begin{tikzpicture}
\begin{axis}[width=0.85\textwidth,height=0.36\textwidth,xmin=1,xmax=12.57,ymin=-0.3,ymax=0.95,axis lines=middle,xlabel={$x$},xtick={3.14159,6.28318,9.42478,12.56637},xticklabels={$\pi$,$2\pi$,$3\pi$,$4\pi$},ytick={0,0.5},legend style={draw=none,at={(0.98,0.98)},anchor=north east}]
\addplot[draw=none,fill=blue!15,domain=1:3.14159,samples=80]{sin(deg(x))/x}\closedcycle;
\addplot[draw=none,fill=red!15,domain=3.14159:6.28318,samples=80]{sin(deg(x))/x}\closedcycle;
\addplot[draw=none,fill=blue!15,domain=6.28318:9.42478,samples=80]{sin(deg(x))/x}\closedcycle;
\addplot[draw=none,fill=red!15,domain=9.42478:12.56637,samples=80]{sin(deg(x))/x}\closedcycle;
\addplot[thick,domain=1:12.56637,samples=300]{sin(deg(x))/x};\addlegendentry{$\sin x/x$}
\addplot[dashed,domain=1:12.56637,samples=300]{abs(sin(deg(x)))/x};\addlegendentry{$|\sin x|/x$}
\end{axis}
\end{tikzpicture}
    </latex-image></image></figure>
    <p>This example also produces a singular oscillation: substituting <m>t=1/x</m> on truncated intervals shows that <m>\int_0^1 \sin(1/x)/x\,dx=\int_1^\infty\sin t/t\,dt</m>. Thus it converges conditionally at zero. By contrast, <m>\int_1^\infty\sin x\,dx</m> diverges because <m>\cos1-\cos T</m> has no limit. Oscillation by itself does not ensure convergence.</p>
    <warning xml:id="warn-conditional-not-principal-value"><title>Keep the two tails separate</title><p>Conditional convergence still requires each improper piece to converge. The symmetric values <m>\int_{-R}^R\sin x\,dx=0</m> do not make <m>\int_{-\infty}^\infty\sin x\,dx</m> convergent. Such a symmetric limiting procedure is called a <em>Cauchy principal value</em>; it is a different definition.</p></warning>
    <exercise xml:id="exr-conditional-improper"><title>Classify oscillatory integrals</title><statement><p>Classify <m>\int_1^\infty\cos x/x\,dx</m>, <m>\int_1^\infty\cos x/x^2\,dx</m>, and <m>\int_0^1\sin(1/x)\,dx</m> as absolutely convergent, conditionally convergent, or divergent.</p></statement><hint><p>The first is conditional: integrate by parts using the bounded antiderivative <m>\sin x</m>, and adapt the lobe lower bound for <m>|\cos x|</m>. The other two are absolute; bound by <m>1/x^2</m> and by <m>1</m>, respectively.</p></hint></exercise>
  </subsection>
''')

insert('ch15-', 'sec-15-1-sequences.xml', r'''
  <subsection xml:id="subsec-cauchy-sequences">
    <title>The Cauchy criterion: convergence without knowing the limit</title>
    <p>Sometimes an approximation has no known target value. We can still ask whether all sufficiently late terms are close to one another. A real sequence <m>(a_n)</m> is <em>Cauchy</em> if, for every <m>\varepsilon&gt;0</m>, there is an integer <m>N</m> such that</p><p><me>|a_m-a_n|&lt;\varepsilon\qquad\text{for all }m,n\ge N.</me></p>
    <theorem xml:id="thm-cauchy-sequences"><title>Cauchy criterion for real sequences</title><statement><p>A sequence of real numbers converges to a real number if and only if it is Cauchy.</p></statement><proof><p>If <m>a_n\to L</m>, choose <m>N</m> so that <m>|a_n-L|&lt;\varepsilon/2</m> for all <m>n\ge N</m>. The triangle inequality proves the Cauchy condition.</p><p>Conversely, a Cauchy sequence is bounded: take an eventual distance bound of <m>1</m> from one fixed term and then include the finitely many earlier terms. Define the tail bounds</p><p><me>\ell_N=\inf\{a_n:n\ge N\},\qquad u_N=\sup\{a_n:n\ge N\}.</me></p><p>Here <m>\inf</m> means greatest lower bound and <m>\sup</m> means least upper bound; completeness of the real line ensures both exist. The sequence <m>\ell_N</m> increases and <m>u_N</m> decreases, and both are bounded. The Monotone Convergence Theorem gives their limits. The Cauchy condition implies <m>u_N-\ell_N\to0</m>: if every pair of tail terms has distance less than <m>\varepsilon</m>, the tail's supremum minus its infimum is at most <m>\varepsilon</m>. Their limits are therefore the same number <m>L</m>. Since <m>\ell_N\le a_N\le u_N</m>, squeezing gives <m>a_N\to L</m>.</p></proof></theorem>
    <example xml:id="ex-cauchy-geometric-steps"><title>Controlling all later steps</title><p>If <m>|a_{n+1}-a_n|\le2^{-n}</m> for <m>n\ge0</m>, then for <m>m&gt;n</m> the finite geometric sum gives</p><p><me>|a_m-a_n|\le\sum_{k=n}^{m-1}2^{-k}\le2^{1-n}.</me></p><p>This tends to zero independently of <m>m</m>, so the sequence converges. We have proved existence of a limit before identifying it.</p></example>
    <warning xml:id="warn-cauchy-adjacent"><title>Adjacent terms are not enough</title><p>The condition <m>|a_{n+1}-a_n|\to0</m> is weaker. For <m>a_n=\ln n</m>, adjacent differences <m>\ln(1+1/n)</m> tend to zero, but <m>|a_{2n}-a_n|=\ln2</m>. This sequence is not Cauchy.</p><p>The criterion depends on the number system being complete. Rational decimal truncations of <m>\sqrt2</m> are Cauchy, yet they have no rational limit. They do have a real limit.</p></warning>
    <exercise xml:id="exr-cauchy-sequences"><title>Use the quantifiers</title><statement><p>Prove directly that <m>a_n=1/n</m> is Cauchy and that <m>b_n=(-1)^n</m> is not. Why does bounding just <m>|a_{n+1}-a_n|</m> fail to check the definition?</p></statement><hint><p>For <m>m,n\ge N</m>, <m>|1/m-1/n|\le1/N</m>. Opposite-parity indices make the second distance equal to <m>2</m>, however large the indices are. The definition requires every pair of late terms.</p></hint></exercise>
  </subsection>
''', before='  <subsection xml:id="subsec-recursive-sequences-fixed-points">')

insert('ch15-', 'sec-15-2-infinite-series.xml', r'''
  <subsection xml:id="subsec-cauchy-series">
    <title>The Cauchy criterion for series</title>
    <p>Apply <xref ref="thm-cauchy-sequences"/> to the partial sums <m>S_n=\sum_{k=1}^n a_k</m>, with <m>S_0=0</m>. The difference of two partial sums is a finite tail.</p>
    <theorem xml:id="thm-cauchy-series"><title>Cauchy criterion for real series</title><statement><p>The series <m>\sum_{k=1}^\infty a_k</m> converges if and only if, for every <m>\varepsilon&gt;0</m>, there is an integer <m>N</m> such that</p><p><me>\left|\sum_{k=p}^q a_k\right|&lt;\varepsilon\qquad\text{whenever }q\ge p\ge N.</me></p></statement><proof><p>Use <m>\sum_{k=p}^q a_k=S_q-S_{p-1}</m>. The Cauchy condition for <m>(S_n)</m> implies the displayed condition after increasing the starting index by one. Conversely, if two partial-sum indices are sufficiently large, their difference is either zero or a tail of this form. Thus <m>(S_n)</m> is Cauchy and converges.</p></proof></theorem>
    <p>Taking <m>q=p</m> shows that convergence requires <m>a_p\to0</m>. But the criterion controls tails of <em>every length</em>. For <m>a_k=1/k</m>,</p><p><me>\sum_{k=p}^{2p-1}\frac1k\ge\frac{p}{2p}=\frac12.</me></p><p>So this series fails the criterion even though each term tends to zero. For a geometric series with <m>|r|&lt;1</m>, on the other hand, <m>|\sum_{k=p}^q r^k|\le |r|^p/(1-|r|)</m>, which proves convergence directly.</p>
    <exercise xml:id="exr-cauchy-series"><title>A bound that proves convergence</title><statement><p>Suppose <m>|\sum_{k=p}^q a_k|\le 3/p</m> for every <m>q\ge p\ge1</m>. Prove convergence. Then explain why the weaker information <m>|a_p|\le3/p</m> does not prove convergence.</p></statement><hint><p>Choose <m>N&gt;3/\varepsilon</m> for the tail bound. The harmonic series satisfies the term bound and still diverges.</p></hint></exercise>
  </subsection>
''')

insert('ch15-', 'sec-15-6-absolute-convergence-and-stronger-tests.xml', r'''
  <subsection xml:id="subsec-dirichlet-abel-tests">
    <title>Dirichlet's and Abel's tests: controlled cancellation</title>
    <p>The alternating-series test is one way to control cancellation. A more general method separates a series into a factor with bounded accumulated sums and a factor whose size changes monotonically.</p>
    <paragraphs><title>Summation by parts</title><p>For integers <m>q\ge p</m>, put <m>A_{p,k}=\sum_{j=p}^k a_j</m> and <m>A_{p,p-1}=0</m>. Since <m>a_k=A_{p,k}-A_{p,k-1}</m>, expanding and shifting the finite sums gives</p><p><me>\sum_{k=p}^q a_kb_k=A_{p,q}b_q+\sum_{k=p}^{q-1}A_{p,k}(b_k-b_{k+1}).</me></p><p>This is the discrete version of integration by parts. It uses only finite sums, so no convergence is assumed in the identity.</p></paragraphs>
    <theorem xml:id="thm-dirichlet-series"><title>Dirichlet's test</title><statement><p>Suppose the partial sums <m>A_n=\sum_{k=1}^n a_k</m> are bounded in absolute value, and <m>b_n\ge0</m> decreases to zero. Then <m>\sum_{n=1}^\infty a_nb_n</m> converges.</p></statement><proof><p>If <m>|A_n|\le M</m>, with <m>A_0=0</m>, then <m>|A_{p,k}|=|A_k-A_{p-1}|\le2M</m>. Summation by parts gives</p><p><me>\left|\sum_{k=p}^q a_kb_k\right|\le2M\left(b_q+\sum_{k=p}^{q-1}(b_k-b_{k+1})\right)=2Mb_p.</me></p><p>The bound tends to zero independently of <m>q</m>. The Cauchy criterion for series proves convergence.</p></proof></theorem>
    <p>More generally, a monotone real sequence tending to zero has one sign (or is identically zero); reversing its sign if necessary reduces it to the stated version. Taking <m>a_n=(-1)^{n-1}</m> recovers the alternating-series test.</p>
    <example xml:id="ex-dirichlet-trig-series"><title>Cancellation without alternating every term</title><p>For <m>\theta\notin2\pi\mathbb Z</m>, the identity</p><p><me>\sum_{n=1}^N\sin(n\theta)=\frac{\cos(\theta/2)-\cos((N+1/2)\theta)}{2\sin(\theta/2)}</me></p><p>follows by telescoping <m>2\sin(\theta/2)\sin(n\theta)=\cos((n-1/2)\theta)-\cos((n+1/2)\theta)</m>. Its magnitude is at most <m>1/|\sin(\theta/2)|</m>. Thus <m>\sum_{n=1}^\infty\sin(n\theta)/n</m> converges by Dirichlet. If <m>\theta\in2\pi\mathbb Z</m>, all terms are zero, so convergence holds there too. For <m>\theta=\pi/2</m>, the absolute-value series is <m>1+1/3+1/5+\cdots</m>, which diverges by comparison with half the harmonic series. This instance is conditionally convergent.</p></example>
    <theorem xml:id="thm-abel-series"><title>Abel's test for series</title><statement><p>If <m>\sum a_n</m> converges and <m>(b_n)</m> is a bounded monotone real sequence, then <m>\sum a_nb_n</m> converges.</p></statement><proof><p>By monotone convergence, <m>b_n\to b</m> for some real <m>b</m>. Put <m>c_n=b_n-b</m>. The sequence <m>c_n</m> is monotone and tends to zero. The partial sums of <m>a_n</m> are bounded because they converge. Dirichlet's test, with a sign reversal if needed, proves convergence of <m>\sum a_nc_n</m>. Since <m>\sum a_nb_n=b\sum a_n+\sum a_nc_n</m> at the level of partial sums, Abel's test follows.</p></proof></theorem>
    <example xml:id="ex-abel-nonzero-limit"><title>A factor need not tend to zero</title><p>The alternating harmonic series converges, and <m>b_n=2+1/n</m> is bounded and decreasing. Abel's test therefore proves convergence of <m>\sum(-1)^{n-1}(2+1/n)/n</m>. Dirichlet's test with the product split in this particular way would not apply, because <m>b_n\to2</m>, rather than zero.</p></example>
    <warning xml:id="warn-dirichlet-abel-hypotheses"><title>Keep the hypotheses attached</title><p>Bounded partial sums alone do not imply that <m>\sum a_n</m> converges. Also, replacing monotonicity by boundedness is invalid: <m>\sum(-1)^n/n</m> converges and <m>b_n=(-1)^n</m> is bounded, but their product is the divergent harmonic series. Abel's test here is a test for numerical series; a theorem about limits of power series at endpoints is a different result.</p></warning>
    <exercise xml:id="exr-dirichlet-abel"><title>Select the cancellation test</title><statement><p>Prove that <m>\sum_{n=1}^\infty\cos(n\pi/2)/\sqrt n</m> converges conditionally. Then use Abel's test to show that <m>\sum_{n=1}^\infty(-1)^{n-1}(3-1/n)/n</m> converges.</p></statement><hint><p>The cosine partial sums are bounded; the nonzero absolute terms are <m>1/\sqrt{2k}</m>, whose sum diverges. For the second series, multiply the convergent alternating harmonic series by the bounded increasing sequence <m>3-1/n</m>.</p></hint></exercise>
  </subsection>
''', before='  <subsection xml:id="subsec-strategy-for-testing-series">')

(QA / 'changed-source.json').write_text(json.dumps(changes, indent=2), encoding='utf-8')
print('Added core material to', len(changes), 'sections.')
