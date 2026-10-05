"""Differential-equation hypotheses, model accuracy, and phase-plane figures."""
from audit_edit import ROOT,replace,save,record
import math,json
def sec(n):return f'chapters/ch13*/sections/sec-13-{n}-*.xml'
replace(sec(2),'acts like a attracting level','acts like an attracting level','Correct the indefinite article')
replace(sec(4),'The quantity <m>Q</m> approaches the equilibrium value <m>Q_{\\text{eq}}</m> exponentially.',
        'For <m>k&gt;0</m> and constant <m>Q_{\\text{eq}}</m>, the quantity <m>Q</m> approaches that equilibrium exponentially (or remains there if it starts there).',
        'The exponential approach requires positive k and a fixed equilibrium')
replace(sec(5),'Thus, for <m>P_0&gt;0</m>,','Thus, for <m>P_0&gt;0</m> and forward time <m>t\ge0</m>,',
        'Logistic solutions above carrying capacity have a pole in backward time')
replace(sec(5),'An equilibrium <m>y=c</m> is <em>stable</em> if solutions that start near <m>c</m> move toward <m>c</m> as <m>t</m> increases.',
        'An equilibrium <m>y=c</m> is <em>stable</em> if solutions starting sufficiently close to <m>c</m> stay as close as desired for all forward time. It is <em>asymptotically stable</em> if it is stable and all sufficiently nearby solutions also converge to <m>c</m>. The attracting equilibria below are asymptotically stable.',
        'Distinguish stability from the stronger property of asymptotic stability')
replace(sec(5),'It is <em>unstable</em> if solutions that start near <m>c</m> move away from <m>c</m> as <m>t</m> increases.',
        'It is <em>unstable</em> if it fails the stability condition: some arbitrarily nearby starting values leave a fixed neighborhood in forward time.',
        'An unstable equilibrium need not repel on both sides')
replace(sec(6),'If <m>q(t)=0</m>, the equation is called <em>homogeneous</em>. If <m>q(t)\\neq0</m>, it is called <em>nonhomogeneous</em>.',
        'If <m>q</m> is identically zero on the interval, the equation is called <em>homogeneous</em>. Otherwise it is called <em>nonhomogeneous</em>.',
        'Classify a forcing function on the interval, not its value at a point')
replace(sec(6),'The formula cannot be continued through <m>t=0</m> because of the term <m>C/t</m>, and the original equation itself is not defined at <m>0</m>.',
        'If <m>C\ne0</m>, the formula cannot be continued through <m>t=0</m> because of the term <m>C/t</m>. When <m>C=0</m>, the formula <m>y=t/2</m> extends smoothly through zero, but the original equation is still undefined there, so it has no solution interval containing zero.',
        'The C equals zero solution formula extends even though the equation does not')
replace(sec(6),'why can a formula such as <m>y=t/2+C/t</m> not be continued through zero?',
        'why does a formula such as <m>y=t/2+C/t</m> require special attention at zero even when <m>C=0</m>?',
        'Keep the domain checkpoint consistent with the removable case')
replace(sec(6),'B(10)\\approx30000(0.4918)=14754.', 'B(10)=30000(e^{0.4}-1)\\approx14754.74.',
        'Use full precision before rounding the account balance')
replace(sec(6),r'\$14{,}754',r'\$14{,}755','Round the full-precision account balance to the nearest dollar')
replace(sec(9),'So for this equation, Euler’s method behaves like decay only when',
        'So for this equation, Euler’s values decay in magnitude precisely when',
        'Magnitude decay can include oscillation; distinguish it from positive monotone decay')
replace(sec(9),'The step <m>h=0.6</m> is too large.',
        'The step <m>h=0.6</m> is too large. To preserve positive, strictly decreasing values as well, choose <m>0&lt;h&lt;1/4</m>; at <m>h=1/4</m> the next value is zero, and for <m>1/4&lt;h&lt;1/2</m> the values alternate signs while their magnitudes decay.',
        'State the stronger step restriction needed to preserve the true qualitative behavior')
# Clip drawn direction segments, which PGF individual plot clipping does not cover.
path=next((ROOT/'source').glob(sec(3))); s=path.read_text('utf-8')
a=s.index('\\foreach'); b=s.index('% exact solution',a)
before=s[a:b]; after='\\begin{scope}\n\\clip (rel axis cs:0,0) rectangle (rel axis cs:1,1);\n'+before+'\\end{scope}\n'
save(path,s[:a]+after+s[b:]); record(path,'Clip the slope field to the displayed Euler axes',before,after)
# Integrate an actual predator-prey orbit, recording invariant drift.
def rhs(r,w):return r*(.8-.02*w),w*(-.6+.01*r)
def step(r,w,h):
 a,b=rhs(r,w);c,d=rhs(r+h*a/2,w+h*b/2);e,f=rhs(r+h*c/2,w+h*d/2);g,j=rhs(r+h*e,w+h*f)
 return r+h*(a+2*c+2*e+g)/6,w+h*(b+2*d+2*f+j)/6
def invariant(r,w):return .01*r-.6*math.log(r)+.02*w-.8*math.log(w)
r,w=80.,20.; H=invariant(r,w); pts=[(r,w)]; drift=0.; crossed=False
for n in range(20000):
 oldw=w; r,w=step(r,w,.001);drift=max(drift,abs(invariant(r,w)-H))
 if n%30==0: pts.append((r,w))
 if w>40:crossed=True
 if crossed and oldw<20<=w and r>60:break
pts.append((r,w))
assert n<19999 and drift<1e-9
path=next((ROOT/'source').glob(sec(8)));s=path.read_text('utf-8')
a=s.index('% approximate closed orbit');b=s.index('% direction arrows',a);before=s[a:b]
after='% RK4 orbit of the stated system, starting at (80,20)\n\\addplot[very thick] coordinates {\n'+'\n'.join(f'({r:.8f},{w:.8f})' for r,w in pts)+'\n};\n\n'
save(path,s[:a]+after+s[b:]);record(path,'Replace an arbitrary ellipse with a computed trajectory of the actual system',before,after)
replace(sec(8),'moves according to the vector <m>(R\',W\')</m>.</caption>',
        'moves according to the vector <m>(R\',W\')</m>. The plotted orbit is a numerical trajectory from <m>(80,20)</m>. Its asymmetric shape comes from the stated equations.</caption>',
        'Describe the actual phase-plane orbit')
replace(sec(8),'    width=0.62\\textwidth,','    axis equal image,\n    width=0.62\\textwidth,',
        'Give oscillator circles equal coordinate units')
(ROOT/'qa/audit/predator-prey-orbit.json').write_text(json.dumps({'method':'RK4','step':.001,'time':(n+1)*.001,'max_invariant_drift':drift,'points':len(pts)}),encoding='utf-8')
