from pathlib import Path
import ast, collections, contextlib, hashlib, io, json, math, os, re, sys
from fractions import Fraction
import sympy as s
from lxml import etree
ROOT=Path.cwd();OUT=ROOT/'qa/audit-2026-10-17';os.environ['MPLCONFIGDIR']=str(OUT/'.late-mpl-cache')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.show=lambda *a,**kw:None
results=[]
def check(name,condition,detail=''):
 ok=bool(condition);results.append(dict(name=name,passed=ok,detail=str(detail)))
 if not ok:raise AssertionError((name,detail))
def content(ch,fn):return (next((ROOT/'source'/('appendices' if ch.startswith('app') else 'chapters')).glob(ch))/'sections'/fn).read_text(encoding='utf-8')
folders=sorted((ROOT/'source/chapters').glob('ch1[3-7]*'))+sorted((ROOT/'source/appendices').glob('app[D-E]*'))
counts=collections.Counter();source_hashes={};trees={}
for folder in folders:
 for f in sorted(folder.rglob('*.xml'))+sorted(folder.glob('*.ptx')):
  rt=etree.parse(str(f));trees[f]=rt;counts['source_files']+=1
  source_hashes[f.relative_to(ROOT).as_posix()]=hashlib.sha256(f.read_bytes()).hexdigest()
  for e in rt.getroot().iter():counts[e.tag]+=1
check('Owned-source XML parses',counts['section']==62,dict(counts))
check('Owned exercise hints present',counts['exercise']==counts['hint']==191)
ids=[e.get('{http://www.w3.org/XML/1998/namespace}id') for rt in trees.values() for e in rt.getroot().iter() if e.get('{http://www.w3.org/XML/1998/namespace}id')]
check('Owned XML IDs unique',len(ids)==len(set(ids)))
for fn,arr in [('sec-13-2-direction-fields.xml',r'\draw[-&gt;, thick] (0,-0.25) -- (0,-0.65);'),('sec-13-5-logistic-and-threshold-models.xml',r'\draw[-&gt;, thick] (0,-0.35) -- (0,-0.8);')]:
 check('Negative logistic arrow: '+fn,arr in content('ch13*',fn) and all(y*(1-y)<0 for y in [-.1,-1,-10]))
x=s.symbols('x',real=True)
f=s.Rational(55,100)*(x-s.Rational(21,10))**3+s.Rational(35,100)*(x-s.Rational(21,10))
check('Bolzano endpoint dots match cubic',f.subs(x,s.Rational(8,10))==-s.Rational(166335,100000) and f.subs(x,s.Rational(34,10))==s.Rational(166335,100000))
check('Bolzano marked root and monotonicity',f.subs(x,s.Rational(21,10))==0 and s.simplify(s.diff(f,x)-s.Rational(165,100)*(x-s.Rational(21,10))**2)==s.Rational(35,100))
window=content('ch14*','sec-14-6-conic-sections.xml')
e=s.Rational(1,2);p=s.Integer(2)
check('Complete ellipse lies inside corrected panel',float(-p/(1-e))>-4.3 and float(p/(1+e))<1.65 and float(p/s.sqrt(1-e*e))<2.8 and 'xmin=-4.3, xmax=1.65' in window)
for n,prefix in [(8,'2.717857'),(16,'3.380728')]:
 h=sum((Fraction(1,k) for k in range(1,n+1)),Fraction())
 check('Harmonic displayed prefix '+str(n),str(float(h)).startswith(prefix),h)
check('Harmonic figure uses exact scaled term heights',r'1.6/(9+\i)' in content('ch15*','sec-15-3-the-harmonic-series-and-first-warnings.xml'))
check('Final harmonic block lower bound',all(Fraction(1,k)>=Fraction(1,16) for k in range(9,17)) and sum(Fraction(1,k) for k in range(9,17))>=Fraction(1,2))
a=Fraction(1,2);P7=sum(((-1)**j*a**(2*j+1)/math.factorial(2*j+1) for j in range(4)),Fraction());next_term=a**9/math.factorial(9)
check('Sine P7 exact displayed bracket',Fraction(479425533,10**9)<P7<Fraction(479425534,10**9),P7)
check('Sine exact alternating enclosure rounds to six places',P7+next_term<Fraction(479425540,10**9) and format(float(P7),'.6f')==format(float(P7+next_term),'.6f')=='0.479426')
check('Half unit in sixth decimal',Fraction(1,2)*Fraction(1,10**6)==Fraction(5,10**7))
check('Contraction exercise iteration count',Fraction(1,3)**13<=Fraction(1,10**6)<Fraction(1,3)**12)
# Independent algebraic checks of representative laws and all printed RK comparison values.
t=s.symbols('t',real=True)
cooling=20+60*s.exp(-s.Rational(8,100)*t)
check('Cooling model solves initial value problem',s.simplify(s.diff(cooling,t)+s.Rational(8,100)*(cooling-20))==0 and cooling.subs(t,0)==80)
damped=s.exp(-t/5)*s.cos(2*t)
check('Damped oscillator identity',s.simplify(s.diff(damped,t,2)+s.Rational(2,5)*s.diff(damped,t)+s.Rational(101,25)*damped)==0)
logistic=1000/(1+9*s.exp(-s.Rational(2,5)*t))
check('Logistic example identity',s.simplify(s.diff(logistic,t)-s.Rational(2,5)*logistic*(1-logistic/1000))==0)
for n in [4,8,16]:
 h=1/n
 vals=[abs((1+h)**n-math.e),abs((1+h+h*h/2)**n-math.e),abs(sum(h**j/math.factorial(j) for j in range(5))**n-math.e)]
 texts=[['0.276876','0.0234261','7.18893e-5'],['0.152497','0.00644059','4.98404e-6'],['0.0803533','0.00168831','3.28118e-7']][[4,8,16].index(n)]
 check('RK printed errors n='+str(n),all(abs(v-float(q))<=max(5e-7,abs(v)*5e-6) for v,q in zip(vals,texts)),vals)
# Check finite power-series products without assuming Euler's formula.
z,w=s.symbols('z w')
check('Exponential addition coefficients',all(s.expand(sum(z**k*w**(n-k)/(s.factorial(k)*s.factorial(n-k)) for k in range(n+1))-(z+w)**n/s.factorial(n))==0 for n in range(11)))
exp_i=sum((s.I*t)**n/s.factorial(n) for n in range(14));cs=sum((-1)**k*t**(2*k)/s.factorial(2*k) for k in range(7));sn=sum((-1)**k*t**(2*k+1)/s.factorial(2*k+1) for k in range(7))
check('Euler even-odd split',s.expand(exp_i-cs-s.I*sn)==0)
tex=content('ch17*','sec-17-1-complex-numbers-and-euler-s-formula.xml')
check('Euler consequence occurs after Euler theorem',tex.index('Combining Euler')>tex.index('note-sec-17-1-complex-numbers-and-euler-s-formula-112'))
check('Fourier orthogonality positive frequencies',all(s.integrate(s.sin(m*t)*s.sin(n*t),(t,-s.pi,s.pi))==(s.pi if m==n else 0) and s.integrate(s.cos(m*t)*s.cos(n*t),(t,-s.pi,s.pi))==(s.pi if m==n else 0) for m in range(1,5) for n in range(1,5)))
check('Square-wave Fourier coefficients',all(s.simplify(2/s.pi*s.integrate(s.sin(n*t),(t,0,s.pi))-(4/(s.pi*n) if n%2 else 0))==0 for n in range(1,9)))
a_n,b_n=s.symbols('a_n b_n',real=True)
check('Symmetric complex Fourier sum equals real pair',s.simplify(s.expand_complex((a_n-s.I*b_n)/2*s.exp(s.I*t)+(a_n+s.I*b_n)/2*s.exp(-s.I*t))-(a_n*s.cos(t)+b_n*s.sin(t)))==0)
u,v=s.symbols('u v',real=True)
eta=((x-u)*(v-x))**3
check('Explicit supported variation joins with two zero derivatives',all(s.diff(eta,x,k).subs(x,endpoint)==0 for k in range(3) for endpoint in [u,v]))

# The given predator-prey plotted orbit must preserve its first integral, within numeric precision.
rt=next(rt for f,rt in trees.items() if f.name=='sec-13-8-systems-and-interaction-models.xml')
code=rt.xpath('//*[@xml:id="fig-predator-prey-phase-plane"]//latex-image',namespaces={'xml':'http://www.w3.org/XML/1998/namespace'})[0].text
coords=re.search(r'\\addplot\[very thick\] coordinates\s*\{(.*?)\};',code,re.S).group(1)
points=[tuple(map(float,m)) for m in re.findall(r'\(([-.\d]+),([-.\d]+)\)',coords)]
I=lambda R,W:.01*R-.6*math.log(R)+.02*W-.8*math.log(W)
drift=max(abs(I(*q)-I(*points[0])) for q in points)
check('Predator-prey figure trajectory invariant',len(points)>20 and drift<1e-5,dict(points=len(points),max_invariant_drift=drift))
check('Picard exercise bounds',max(abs(t+y*y) for t in [-1,1] for y in [0,2])==5 and 2*2==4 and Fraction(1,5)*4<1)

# Every sampled point of each newly expanded polar figure must lie inside its axes.
spiral=[(q*math.cos(q),q*math.sin(q)) for q in [2*math.pi*k/20000 for k in range(20001)]]
check('Full first spiral turn inside window',all(-4.1<x<6.8 and -6.6<y<6.6 for x,y in spiral))
check('Three-turn spiral inside window',.18*6*math.pi<3.7)
check('Both intersecting circles inside window',all(-1.3<1+math.cos(q)<2.4 and -1.3<math.sin(q)<2.4 and -1.3<math.cos(q)<2.4 and -1.3<1+math.sin(q)<2.4 for q in [2*math.pi*k/1000 for k in range(1001)]))

# Run every printed Appendix E code block in document order, separately per section.
code_blocks=0;outputs={}
for f,rt in trees.items():
 if 'appE-' not in f.as_posix():continue
 env={};buf=io.StringIO()
 for index,pre in enumerate(rt.xpath('//pre')):
  source=''.join(pre.itertext()).strip();ast.parse(source)
  with contextlib.redirect_stdout(buf):exec(compile(source,str(f)+'#'+str(index),'exec'),env)
  code_blocks+=1
 plt.close('all');outputs[f.name]=buf.getvalue()
check('All printed Appendix E code executes',code_blocks==13,dict(blocks=code_blocks))
check('Opaque excluded-point markers',all('mark=o' not in content(ch,fn) for ch,fn in [('appE*','sec-e-1-graphing-windows.xml'),('appD*','sec-d-3-bolzano-s-theorem-and-bisection.xml'),('ch16*','sec-16-8-uniform-convergence-preview.xml')]))
changes=[json.loads(x) for x in OUT.joinpath('late-changes.jsonl').read_text(encoding='utf-8').splitlines()]
receipt=dict(status='passed',checks=len(results),failures=sum(not r['passed'] for r in results),results=results,coverage={k:counts[k] for k in ['source_files','section','subsection','figure','image','table','exercise','hint','theorem','definition','example','pre']},source_sha256=source_hashes,corrections=len(changes),changed_source_files=len({c['file'] for c in changes}),figure_ids=sorted({i for c in changes for i in c['changed_figure_ids']}),printed_code_outputs=outputs)
OUT.joinpath('late-verification.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in receipt.items() if k in ['status','checks','failures','coverage','corrections','changed_source_files','figure_ids']},indent=2))
