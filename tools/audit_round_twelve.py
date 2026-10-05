"""Numerical-method corrections, with finite arguments before Taylor's chapter."""
import re
from audit_edit import ROOT, replace, save, record
def sec(n): return f'chapters/ch12*/sections/sec-12-{n}-*.xml'
def span(n, start, end, after, issue):
    path=next((ROOT/'source').glob(sec(n))); text=path.read_text('utf-8')
    a=text.index(start); b=text.index(end,a)
    before=text[a:b]; save(path,text[:a]+after+text[b:]); record(path,issue,before,after)

replace(sec(2),'Doubling the number of subintervals usually divides these error bounds by about <m>4</m>.',
        'Doubling the number of subintervals divides these bounds by <m>4</m>. The actual errors need not change by exactly that factor.',
        'Distinguish exact scaling of a bound from observed scaling of the error')
replace(sec(2),'On one short subinterval of width <m>\\Delta x</m>, Taylor’s theorem says that the failure of the graph to be linear is controlled by <m>f\'\'</m>. The one-interval trapezoid error is at most',
        r'''On a subinterval <m>[c,d]</m>, let <m>L</m> be the line through the endpoint values. For an interior point <m>x</m>, choose <m>C</m> so that <m>f(t)-L(t)-C(t-c)(t-d)</m> vanishes at <m>c,x,d</m>. Applying Rolle’s Theorem twice gives <m>C=f''(\xi)/2</m>. Hence <m>|f(x)-L(x)|\le K(x-c)(d-x)/2</m>. Integrating this bound, with <m>\Delta x=d-c</m>, shows that the one-interval trapezoid error is at most''',
        'Prove the quadrature estimate using Rolle instead of a theorem introduced in Chapter 16')
replace(sec(2),'and the one-interval midpoint error is at most',
        r'''For the midpoint <m>m=(c+d)/2</m>, the quadratic remainder argument from <xref ref="subsec-newton-convergence-good-start"/> gives <m>|f(x)-f(m)-f'(m)(x-m)|\le K(x-m)^2/2</m>. The linear term integrates to zero by symmetry. Integrating the bound gives a one-interval midpoint error at most''',
        'Explain the midpoint constant before Taylor theory')
replace(sec(2),'The constants come from integrating the quadratic error term in Taylor’s formula.',
        'Both constants come from integrating the quadratic bounds just obtained.',
        'Remove the remaining forward dependency on Taylor theory')
span(2,r'\pgfplotsinvokeforeach{0,1,2,3}{',r'\addplot[very thick, domain=0:1',
     '\n'.join(r'\draw[fill=gray!14, draw=gray!55] (axis cs:'+str(i/4)+r',0) rectangle (axis cs:'+str((i+1)/4)+','+str(__import__('math').exp(-((i+.5)/4)**2))+');' for i in range(4))+'\n',
     'Freeze all four rectangle coordinates instead of deferred loop macros that draw only the last rectangle')
replace(sec(3),'A line is determined by two points. A parabola is determined by three points.',
        'A polynomial of degree at most one is determined by two points with distinct inputs. A polynomial of degree at most two is determined by three points with distinct inputs.',
        'Quadratic interpolation can degenerate to a line or constant')
replace(sec(3),'A line is determined by two points, while a parabola is determined by three.',
        'Linear interpolation uses two distinct inputs, while interpolation by a polynomial of degree at most two uses three.',
        'Keep the checkpoint consistent with degenerate interpolation cases')
path=next((ROOT/'source').glob(sec(3))); txt=path.read_text('utf-8')
match=re.search(r'  <exercise xml:id="checkpoint-12-3-hypotheses-still-matter">.*?</exercise>',txt,re.S)
block=match.group(); txt=txt.replace(block,'')
# Put the checkpoint after the subsection that establishes the error hypothesis.
end=txt.index('</subsection>',txt.index('<exercise xml:id="checkpoint-12-3-fourth-derivative"'))
txt=txt[:end]+block+'\n'+txt[end:]; save(path,txt)
record(path,'Move the fourth-derivative checkpoint after its error-bound discussion',block,'Moved after checkpoint-12-3-fourth-derivative')
span(4,'  <p>To see the size of the error,','  <note xml:id="note-sec-12-4-numerical-differentiation-62">',r'''  <p>Assume <m>f'''"'''"r'''</m> is continuous near <m>a</m>, with <m>|f'''"'''"r'''|\le K</m>. Repeated use of the Fundamental Theorem of Calculus gives the finite identity</p>
  <p><me>f(a+s)=f(a)+f'(a)s+\frac12f''(a)s^2+R_3(s),\qquad R_3(s)=\frac12\int_0^s(s-t)^2f'''"'''"r'''(a+t)\,dt.</me></p>
  <p>The orientation of the integral makes the identity valid for negative <m>s</m> too. In either direction, <m>|R_3(s)|\le K|s|^3/6</m>. Therefore</p>
  <p><me>D_h^+f(a)=f'(a)+\frac12f''(a)h+\frac{R_3(h)}h,\qquad D_h^-f(a)=f'(a)-\frac12f''(a)h-\frac{R_3(-h)}h.</me></p>
  <p>Each remainder quotient has absolute value at most <m>Kh^2/6</m>. The one-sided errors generally have opposite leading terms proportional to <m>h</m>. Averaging the quotients cancels those terms:</p>
  <p><me>D_h^0f(a)=f'(a)+\frac{R_3(h)-R_3(-h)}{2h},\qquad |D_h^0f(a)-f'(a)|\le\frac{Kh^2}{6}.</me></p>
  <p>Continuity of <m>f'''"'''"r'''</m> also gives <m>R_3(s)/s^3\to f'''"'''"r'''(a)/6</m>: subtract <m>f'''"'''"r'''(a)</m> in the integral and bound the difference by its maximum near <m>a</m>. Consequently</p>
  <p><me>\lim_{h\to0}\frac{D_h^0f(a)-f'(a)}{h^2}=\frac16f'''"'''"r'''(a).</me></p>
  <p>The leading centered error is usually proportional to <m>h^2</m>. These are finite remainder estimates; Taylor polynomials will be developed in Chapter 16.</p>

''','Replace an unjustified infinite Taylor equality and its forward dependency by a finite integral remainder')
replace(sec(4),'Taylor expansions show that the first-order error terms of the left and right secants have opposite signs and cancel in the centered quotient.',
        'The finite quadratic remainder identities show that the terms proportional to the step have opposite signs and cancel in the centered quotient.',
        'Make the hint depend on the argument already supplied')
replace(sec(4),'The Taylor expansion is not only a formal calculation. It tells us how the error behaves.',
        'The finite remainder estimate tells us how the error behaves.', 'Avoid referring to an expansion not yet developed')
replace(sec(4),'may have error as large as approximately','may have absolute error as large as', 'The numerator bound is an exact bound of twice eta')
# Keep the final quotients correctly rounded from full precision.
for num, den, value in [(r'e^{0.1}-e^0','0.1','1.051709'),(r'e^0-e^{-0.1}','0.1','0.951626'),(r'e^{0.1}-e^{-0.1}','0.2','1.001668')]:
    path=next((ROOT/'source').glob(sec(4))); txt=path.read_text('utf-8')
    a=txt.index(r'\frac{'+num+'}{'+den+'}'); b=txt.index(value+'.',a)+len(value)+1
    before=txt[a:b]; after=r'\frac{'+num+'}{'+den+'}\n\\approx\n'+value+'.'
    save(path,txt[:a]+after+txt[b:]); record(path,'Do not equate rounded exponential data to an exact quotient',before,after)
replace(sec(5),'Earlier, Taylor’s formula gave the Newton error relation',
        'Earlier, the quadratic remainder argument using Rolle’s Theorem gave the Newton error relation',
        'Use the corrected earlier proof, before Taylor theory')
replace(sec(5),'then the graph touches the axis more flatly.',
        'then the graph meets the axis with zero slope; it may touch the axis or cross it flatly.',
        'A zero derivative at a root does not force a touch')
replace(sec(5),'and it is a double root. Since',
        r'''and it is a double root. More generally, a root has <em>multiplicity</em> <m>m</m> if, near the root, <m>f(x)=(x-r)^m g(x)</m>, where <m>m</m> is a positive integer and <m>g</m> is continuous with <m>g(r)\ne0</m>. For the differentiations below we also assume <m>g</m> is sufficiently differentiable. Here <m>m=2</m> and <m>g=1</m>. Since''',
        'Define root multiplicity before using it in general statements')
replace(sec(5),'By <m>n=3</m>, both the residual and the step size are tiny. The sequence has stabilized for any ordinary decimal purpose.',
        'By <m>n=3</m>, the residual is tiny and the step is small enough for a moderate decimal tolerance. The required precision determines whether another step is needed.',
        'Avoid claiming arbitrary accuracy from a step of about two millionths')
replace(sec(5),'The residual is approximately', 'For the displayed decimal input, the residual satisfies',
        'A rounded residual must be rounded upward to support a guaranteed error bound')
replace(sec(5),r'|f(x_3)|\approx 4.51\cdot10^{-12}.',r'|f(x_3)|&lt;4.52\cdot10^{-12}.', 'Use a verified upper bound for the residual')
replace(sec(5),r'\frac{4.51\cdot10^{-12}}{2}',r'\frac{4.52\cdot10^{-12}}{2}', 'Preserve the inequality when using the residual bound')
span(5,'    <caption>Placeholder:', '      </latex-image>',r'''    <caption>The Newton map <m>N(x)=(x-1/x)/2</m> for <m>f(x)=x^2+1</m> has a vertical asymptote at zero. The input <m>1</m> maps to zero, where the next step is undefined. The nearby input <m>1.01</m> maps to about <m>0.0099505</m>, whose next image is about <m>-50.2438</m>, far below the displayed window.</caption>
    <image width="75%">
      <latex-image>
\begin{tikzpicture}
\begin{axis}[width=0.82\textwidth,height=0.56\textwidth,
 xmin=-3,xmax=3,ymin=-4,ymax=4,axis lines=middle,
 xlabel={\(x\)},ylabel={\(N(x)\)},xtick={-2,-1,0,1,2},ytick={-4,-2,2,4},
 grid=both,grid style={line width=.1pt,draw=gray!25}]
\addplot[very thick,domain=-3:-0.08,samples=200] {(x-1/x)/2};
\addplot[very thick,domain=0.08:3,samples=200] {(x-1/x)/2};
\draw[dashed,gray] (axis cs:0,-4)--(axis cs:0,4);
\addplot[only marks,mark=*] coordinates {(1,0)};
\node[anchor=west] at (axis cs:1,0) {\(N(1)=0\)};
\node[anchor=west] at (axis cs:1.3,2.8) {\(N(x)=\frac12(x-1/x)\)};
\draw[->,thick] (axis cs:0.0099505,-2.5)--(axis cs:0.0099505,-3.9);
\node[anchor=west,align=left] at (axis cs:0.25,-2.5) {\(N(0.0099505)\approx-50.2438\)\\below the window};
\end{axis}
\end{tikzpicture}
''','Replace a missing mathematical illustration with a graph of the actual Newton map')
replace(sec(7),'For smooth functions,',r'''For smooth functions, we use the notation <m>R(h)=O(h^p)</m> to mean that there are constants <m>C,\delta&gt;0</m> such that <m>|R(h)|\le C|h|^p</m> whenever <m>0&lt;|h|&lt;\delta</m>. With this notation,''', 'Define big-O notation at its first use')
replace(sec(7),'Use Taylor expansion to show that',
        'Assume the third derivative is continuous near <m>a</m>. Use the finite remainder estimate from <xref ref="subsec-truncation-error"/> to show that',
        'Use available finite remainder theory in the review exercise')
replace(sec(7),r"f'(a)+\frac16 f'''(a)h^2+\text{higher-order terms}.",
        r"f'(a)+\frac16 f'''(a)h^2+\rho(h),\qquad \frac{\rho(h)}{h^2}\to0.",
        'Specify the review remainder under the stated differentiability hypothesis')
