"""Repeatable focused verification for the chapter7-12 / AppendixF audit.

Reads current PreTeXt sources; writes only this audit's verification receipt.
No publication, build, or source mutation.
"""
from pathlib import Path
from lxml import etree as ET
import json
import hashlib
import math
import re
import sys
import sympy as sp
import mpmath as mp

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'source'
OUT = Path(__file__).with_name('middle-verification.json')
results = []
mp.mp.dps = 60
x = sp.symbols('x', real=True)
xp = sp.symbols('x', positive=True)
a, b, L, K, r, t, A = sp.symbols('a b L K r t A', positive=True)

def check(name, condition, details=''):
    results.append(dict(name=name, passed=bool(condition), details=str(details)))

def same(name, got, expected):
    residual = sp.simplify(sp.trigsimp(got-expected))
    check(name, residual == 0, f'residual={residual}')

def close(name, got, expected, tolerance=1e-12):
    error = abs(float(got)-float(expected))
    check(name, error <= tolerance, f'got={got}; expected={expected}; error={error}; tolerance={tolerance}')

def file(stem):
    paths = list(SOURCE.rglob(stem+'.xml'))
    assert len(paths) == 1, (stem, paths)
    return paths[0]

def xml(stem):
    return ET.parse(str(file(stem)))

def rows(stem, table_id):
    tab = xml(stem).xpath('//*[@xml:id=$id]', id=table_id)[0]
    return [[' '.join(''.join(c.itertext()).split()) for c in row.findall('cell')]
            for row in tab.xpath('.//tabular/row')][1:]

def printed6(name, got, printed):
    check(name, f'{float(got):.6f}' == printed,
          f'computed={float(got):.15g}; printed={printed}')

def rules(f, left, right, n):
    h = (right-left)/n
    mid = h*math.fsum(f(left+(i+.5)*h) for i in range(n))
    trap = h*(.5*f(left)+math.fsum(f(left+i*h) for i in range(1,n))+.5*f(right))
    simp = None
    if n%2 == 0:
        simp = h/3*(f(left)+f(right)+4*math.fsum(f(left+i*h) for i in range(1,n,2))
                    +2*math.fsum(f(left+i*h) for i in range(2,n,2)))
    return mid, trap, simp

# Parse every owned file, and count the actual review surface.
dirs = [next((SOURCE/'chapters').glob(f'ch{n:02}-*')) for n in range(7,13)]
dirs += [SOURCE/'appendices'/'appF-tables']
owned = sorted(p for d in dirs for p in d.rglob('*') if p.suffix in ('.xml','.ptx'))
counts = {key:0 for key in ('sections','examples','exercises','hints','figures','tables')}
for p in owned:
    tree = ET.parse(str(p))
    for key,tag in [('sections','section'),('examples','example'),('exercises','exercise'),
                    ('hints','hint'),('figures','figure'),('tables','table')]:
        counts[key] += len(tree.xpath('//'+tag))
check('All owned XML parses', True, dict(files=len(owned), **counts))

# Related rates, optimization, approximations, exponential and logistic models.
same('Balloon radial rate',24*sp.pi/(4*sp.pi*3**2),sp.Rational(2,3))
same('Ladder vertical rate',-sp.Rational(6,8)*2,-sp.Rational(3,2))
same('Shadow and tip rates',4+sp.Rational(2,3)*4,sp.Rational(20,3))
same('Cone water rate',2/(sp.pi*6**2/9),1/(2*sp.pi))
same('Open-box volume at maximizer', (x*(12-2*x)**2).subs(x,2),128)
same('Open-box critical points',sp.diff(x*(12-2*x)**2,x),(12-2*x)*(12-6*x))
same('Optimal closed can h=2r',sp.diff(2*sp.pi*x**2+2*A/x,x).subs(A,2*sp.pi*x**3),0)
distance = sp.sqrt(x**2+a**2)+sp.sqrt((L-x)**2+b**2)
same('Reflected path stationary at aL/(a+b)',sp.diff(distance,x).subs(x,a*L/(a+b)),0)
same('Reflected path strict convexity',sp.diff(distance,x,2),a**2/(x**2+a**2)**sp.Rational(3,2)+b**2/((L-x)**2+b**2)**sp.Rational(3,2))
same('Sphere differential bound',4*sp.pi*3**2*sp.Rational(2,100),sp.Rational(72,100)*sp.pi)
same('Disk relative differential bound',2*sp.Rational(2,10)/24,sp.Rational(1,60))
close('Survey differential at 45 degrees',200*math.pi/180,3.49,.005)
close('Survey differential at 80 degrees',100/(math.cos(80*math.pi/180)**2)*math.pi/180,57.9,.05)
close('Coffee after30 minutes',20+70*(4/7)**3,33.1,.05)
close('Logistic half-capacity time',math.log(9)/.8,2.75,.005)
logistic = K/(1+A*sp.exp(-r*t))
same('Logistic solution satisfies ODE',sp.diff(logistic,t),r*logistic*(1-logistic/K))
least_time = sp.sqrt(x*x+16)/3+sp.sqrt((7-x)**2+9)/4
same('Refraction example stationary point',sp.diff(least_time,x).subs(x,3),0)
close('577/408 square-root error',sp.Rational(577,408)-sp.sqrt(2),2.123901414755e-6,1e-17)

# Numerical Newton tables (including residuals calculated before display rounding).
z=1.5
for i in range(5):
    expected = ['1.500000000','1.416666667','1.414215686','1.414213562','1.414213562'][i]
    check(f'Square-root Newton iterate{i}',f'{z:.9f}'==expected,f'{z:.17g}')
    z=z-(z*z-2)/(2*z)
z=1.0
for i,expected in enumerate(['1.000000000','0.750363868','0.739112891','0.739085133','0.739085133']):
    check(f'Cosine Newton iterate{i}',f'{z:.9f}'==expected,f'{z:.17g}')
    z=z+(math.cos(z)-z)/(math.sin(z)+1)
z=1.5
for i,row in enumerate(rows('sec-12-5-newton-s-method-revisited','tab-sec-12-5-newton-s-method-revisited-2')):
    check(f'Newton review displayed iterate{i}',f'{z:.9f}'==row[1],repr(z))
    coefficient,exponent=re.fullmatch(r'([0-9.]+)\\cdot10\^\{(-?[0-9]+)\}',row[2]).groups()
    expected=float(coefficient)*10**int(exponent)
    close(f'Newton review residual{i}',abs(z*z-2),expected,max(1e-25,expected*6e-7))
    z=z-(z*z-2)/(2*z)

# Geometric, physical, and probability evaluations, independently integrated.
integrals = [
 ('Area line/parabola',2*x-x*x,0,2,sp.Rational(4,3)),
 ('Area sideways parabolas',2-2*x*x,-1,1,sp.Rational(8,3)),
 ('Area second line/parabola',2-x-x*x,-2,1,sp.Rational(9,2)),
 ('Disk volume',sp.pi*x,0,4,8*sp.pi),
 ('Washer volume',sp.pi*(x*x-x**4),0,1,2*sp.pi/15),
 ('Square cross-section volume',x,0,4,8),
 ('Semicircle cross-section volume',sp.pi*x/8,0,4,sp.pi),
 ('Parabolic shell volume',2*sp.pi*x*(4-x*x),0,2,8*sp.pi),
 ('Hyperbolic shell volume',2*sp.pi,1,3,4*sp.pi),
 ('Between-curves shell volume',2*sp.pi*x*(x-x*x),0,1,sp.pi/6),
 ('Horizontal shell volume',2*sp.pi*x*(2-2*x*x),0,1,sp.pi),
 ('Rod mass',2+x,0,4,16),
 ('Rod first moment',x*(2+x),0,4,sp.Rational(112,3)),
 ('Symmetric nonuniform moment',x*(1+x*x),-1,1,0),
 ('Triangle lamina x-moment',x*x/2,0,2,sp.Rational(4,3)),
 ('Increasing-force work',5+2*x,0,3,24),
 ('Spring first stretch work',200*x,0,sp.Rational(1,5),4),
 ('Spring additional stretch work',200*x,sp.Rational(1,5),sp.Rational(1,2),21),
 ('Chain lifting work',2*x,0,10,100),
 ('Rectangular pumping work',sp.Rational(624,10)*24*(5-x),0,5,18720),
 ('Conical pumping work',sp.Rational(624,10)*sp.pi*x*x*(6-x)/4,0,6,sp.Rational(16848,10)*sp.pi),
 ('Rectangular plate force',sp.Rational(624,10)*4*x,0,6,sp.Rational(44928,10)),
 ('Triangular plate force',sp.Rational(624,10)*4*x*(1-x/6),0,6,sp.Rational(14976,10)),
 ('Dam force',9800*30*x,0,12,21168000),
 ('Circular window force',9800*x*2*sp.sqrt(1-(x-3)**2),2,4,29400*sp.pi),
 ('Average x-squared',x*x/3,0,3,3),
 ('Average temperature',(60+10*sp.sin(sp.pi*x/12))/12,0,12,60+20/sp.pi),
 ('Triangular probability normalization',2*x,0,1,1),
 ('Triangular probability left-half',2*x,0,sp.Rational(1,2),sp.Rational(1,4)),
 ('Triangular probability mean',2*x*x,0,1,sp.Rational(2,3)),
 ('Power-curve arc length',sp.sqrt(1+x),0,3,sp.Rational(14,3)),
 ('Parts definite exponential',x*sp.exp(x),0,1,1),
 ('Parts definite sine',x*sp.sin(x),0,sp.pi,sp.pi),
 ('Improper exponential',sp.exp(-x),0,sp.oo,1),
 ('Improper exponential first moment',x*sp.exp(-x),0,sp.oo,1),
 ('Improper Cauchy integral',1/(1+x*x),-sp.oo,sp.oo,sp.pi),
]
for name,f,left,right,expected in integrals:
    same(name,sp.integrate(f,(x,left,right)),expected)
close('Sine arc length',mp.quad(lambda z:mp.sqrt(1+mp.cos(z)**2),[0,mp.pi]),3.820197789027712,1e-14)
same('Disk and shell alternative under1/x',sp.pi*sp.integrate(8,(x,0,sp.Rational(1,3)))+sp.pi*sp.integrate(x**-2-1,(x,sp.Rational(1,3),1)),4*sp.pi)

# Antiderivatives: all log formulas use a real open component of the domain.
# Replacing log|g| by log(g) for symbolic differentiation is valid on g>0;
# the derivative g'/g remains the same on a negative component.
antiderivatives = [
 ('Parts log',x*sp.log(x)-x,sp.log(x)),
 ('Parts cosine',x*sp.sin(x)+sp.cos(x),x*sp.cos(x)),
 ('Parts twice',sp.exp(x)*(x*x-2*x+2),x*x*sp.exp(x)),
 ('Trig even powers',x/8-sp.sin(4*x)/32,sp.sin(x)**2*sp.cos(x)**2),
 ('Trig tangent-secant',sp.tan(x)**4/4+sp.tan(x)**6/6,sp.tan(x)**3*sp.sec(x)**4),
 ('Trig secant-tangent',sp.sec(x)**7/7-sp.sec(x)**5/5,sp.sec(x)**5*sp.tan(x)**3),
 ('Trig product-to-sum',-sp.cos(7*x)/14-sp.cos(3*x)/6,sp.sin(5*x)*sp.cos(2*x)),
 ('Radical positive quadratic',sp.log(x+sp.sqrt(x*x+4)),1/sp.sqrt(x*x+4)),
 ('Partial fractions improper rational',x**3/3+x*x/2+x+2*sp.log(x-1),(x**3+1)/(x-1)),
 ('Partial fractions two linear',sp.Rational(11,3)*sp.log(x-2)-sp.Rational(2,3)*sp.log(x+1),(3*x+5)/((x-2)*(x+1))),
 ('Partial fractions repeated linear',-sp.log(x-1)/9-1/(3*(x-1))+sp.log(x+2)/9,1/((x-1)**2*(x+2))),
 ('Partial fractions irreducible',5*sp.log(x-1)/2-5*sp.log(x*x+1)/4-sp.atan(x)/2,(2*x+3)/((x-1)*(x*x+1))),
 ('Completed-square rational',3*sp.log(x*x+4*x+13)/2+sp.atan((x+2)/3)/3,(3*x+7)/(x*x+4*x+13)),
 ('Strategy partial fraction',8*sp.log(x-3)/5-3*sp.log(x+2)/5,(x+5)/(x*x-x-6)),
 ('Strategy substitution',sp.exp(x*x)/2,x*sp.exp(x*x)),
 ('Strategy log parts',x*x*sp.log(x)/2-x*x/4,x*sp.log(x)),
 ('Strategy translated radical',2*(x+1)**sp.Rational(5,2)/5-2*(x+1)**sp.Rational(3,2)/3,x*sp.sqrt(x+1)),
 ('Strategy rationalization',2*(x+1)**sp.Rational(3,2)/3-2*x**sp.Rational(3,2)/3,1/(sp.sqrt(x+1)+sp.sqrt(x))),
 ('Strategy cubic radical', (x*x+1)**sp.Rational(3,2)/3-sp.sqrt(x*x+1),x**3/sp.sqrt(x*x+1)),
 ('CAS exp/trig',sp.exp(2*x)*(2*sp.cos(3*x)+3*sp.sin(3*x))/13,sp.exp(2*x)*sp.cos(3*x)),
 ('CAS arctangent scaled',sp.atan((2*x-1)/3)/6,1/(9+(2*x-1)**2)),
 ('Inverse hyperbolic parts asinh',x*sp.asinh(x)-sp.sqrt(1+x*x),sp.asinh(x)),
 ('Inverse hyperbolic parts atanh',x*sp.atanh(x)+sp.log(1-x*x)/2,sp.atanh(x)),
 ('Challenge substitution then parts',sp.exp(x*x)*(x*x-1)/2,x**3*sp.exp(x*x)),
 ('F arccot derivative',sp.acot(x),0),
]
for name,F,f in antiderivatives:
    if name=='F arccot derivative': same(name,sp.diff(F,x),-1/(1+x*x))
    else: same(name,sp.diff(F,x),f)
# Negative-branch and absolute-value checks substitute positive magnitudes.
u=sp.symbols('u',positive=True)
same('Inverse hyperbolic negative arcosh branch',sp.diff(-sp.acosh(-x/a),x).subs(x,-a*sp.cosh(u)),1/(a*sp.sinh(u)))
for sign in (-1,1):
    xx=sign*a*sp.sech(u)
    expected=(1/(x*sp.sqrt(a*a-x*x))).subs(x,xx)
    derivative=(-1/a)*(-1/((sp.Abs(x)/a)*sp.sqrt(1-(sp.Abs(x)/a)**2)))*sp.sign(x)/a
    same(f'Arsech integral sign{sign}',derivative.subs(x,xx),expected)
    xx=sign*a/sp.sinh(u)
    expected=(1/(x*sp.sqrt(a*a+x*x))).subs(x,xx)
    derivative=(-1/a)*(-1/((sp.Abs(x)/a)*sp.sqrt(1+(sp.Abs(x)/a)**2)))*sp.sign(x)/a
    same(f'Arcsch integral sign{sign}',derivative.subs(x,xx),expected)
same('Log decay counterexample primitive',sp.diff(sp.log(sp.log(x)),x),1/(x*sp.log(x)))
same('Conditional sine integration by parts',sp.diff(-sp.cos(x)/x,x)-sp.cos(x)/x**2,sp.sin(x)/x)
same('Conditional sine lobe lower bound',sp.Rational(1,2)*(2*sp.pi/3)/((K+1)*sp.pi),1/(3*(K+1)))

# Reproduce every numerical quadrature table and selected derivative tables.
gaussian=lambda z:math.exp(-z*z)
for row in rows('sec-12-1-why-approximate-integrals','tab-sec-12-1-why-approximate-integrals-2'):
    n=int(row[0]);printed6(f'Intro Gaussian midpoint n{n}',rules(gaussian,0,1,n)[0],row[1])
for row in rows('sec-12-2-midpoint-and-trapezoidal-rules','tab-sec-12-2-midpoint-and-trapezoidal-rules-4'):
    m=float(row[1]);printed6(f'Gaussian midpoint sample{m}',gaussian(m),row[2])
for row,got in zip(rows('sec-12-3-simpson-s-rule','tab-sec-12-3-simpson-s-rule-1'),rules(gaussian,0,1,4)):
    printed6('Gaussian rule n4 '+row[0],got,row[1])
for row in rows('sec-12-6-computing-experiments','tab-sec-12-6-computing-experiments-2'):
    n=int(row[0])
    for label,got,printed in zip(('M','T','S'),rules(lambda z:4/(1+z*z),0,1,n),row[1:]):
        printed6(f'Pi {label} n{n}',got,printed)
normal=lambda z:math.exp(-z*z/2)/math.sqrt(2*math.pi)
for row in rows('sec-12-6-computing-experiments','tab-sec-12-6-computing-experiments-3'):
    n=int(row[0]);printed6(f'Normal Simpson n{n}',rules(normal,-1,1,n)[2],row[1])
for row in rows('sec-12-6-computing-experiments','tab-sec-12-6-computing-experiments-4'):
    n=int(row[0]);printed6(f'Gaussian Simpson n{n}',rules(gaussian,0,1,n)[2],row[1]);printed6(f'Sqrt Simpson n{n}',rules(math.sqrt,0,1,n)[2],row[2])
for label,got,printed in zip(('forward','backward','centered'),[(math.exp(.1)-1)/.1,(1-math.exp(-.1))/.1,(math.exp(.1)-math.exp(-.1))/.2],rows('sec-12-4-numerical-differentiation','tab-sec-12-4-numerical-differentiation-2')):
    printed6(f'Finite difference {label}',got,printed[1]);printed6(f'Finite difference error {label}',abs(got-1),printed[2])

# Gaussian fourth derivative bound K=12 on[0,1], by exact critical points.
g4=sp.diff(sp.exp(-x*x),x,4)
same('Gaussian fourth derivative expression',g4,(16*x**4-48*x*x+12)*sp.exp(-x*x))
critical=[sp.Integer(0),sp.Integer(1),sp.sqrt((5-sp.sqrt(10))/2)]
check('Gaussian Simpson derivative bound12',all(abs(float(g4.subs(x,c)))<=12+1e-12 for c in critical),[(str(c),float(g4.subs(x,c))) for c in critical])

# Richardson and Romberg exact identities and all printed quartic table values.
h=sp.symbols('h',positive=True)
c2,c4,I=sp.symbols('c2 c4 I')
Th=I+c2*h*h+c4*h**4
same('Richardson cancels h squared',(4*Th.subs(h,h/2)-Th)/3,I-c4*h**4/4)
romberg=[]
for k in range(3):
    width=sp.Rational(1,2**k)
    row=[sp.Rational(1,5)+width**2/3-width**4/30]
    for j in range(1,k+1):row.append(row[-1]+(row[-1]-romberg[k-1][j-1])/(4**j-1))
    romberg.append(row)
for k,row in enumerate(rows('sec-additional-richardson-romberg','tab-romberg-quartic')):
    for j in range(k+1):check(f'Quartic Romberg R{k},{j}',f'{float(romberg[k][j]):.10f}'==row[j+1],str(romberg[k][j]))
same('Quartic Romberg final exact',romberg[2][2],sp.Rational(1,5))
same('Two-half-panel Simpson bound constant',2*(sp.Rational(1,2))**5/2880,sp.Rational(1,46080))

# Execute exactly the algorithm printed in the current book, with success/failure paths.
namespace={}
exec(xml('sec-additional-adaptive-quadrature').find('.//pre').text,namespace)
adaptive=namespace['adaptive_simpson']
for k in range(5):
    value,indicator,evals,intervals=adaptive(lambda z,k=k:z**k,0,1,1e-10)
    close(f'Adaptive polynomial degree{k}',value,1/(k+1),1e-10)
    check(f'Adaptive polynomial accounting{k}',indicator<=1e-10 and evals==4*len(intervals)+1,dict(indicator=indicator,evaluations=evals,leaves=len(intervals)))
value,indicator,evals,intervals=adaptive(lambda z:4/(1+z*z),0,1,1e-8)
close('Adaptive pi accuracy',value,math.pi,1e-8)
check('Adaptive pi indicator',indicator<=1e-8,dict(value=value,indicator=indicator,evaluations=evals,leaves=len(intervals)))
peak=lambda z:math.exp(-2500*(z-.37)**2)
reference=mp.quad(lambda z:mp.exp(-2500*(z-mp.mpf('.37'))**2),[0,.3,.37,.45,1])
value,indicator,evals,intervals=adaptive(peak,0,1,1e-9)
close('Adaptive localized peak',value,reference,1e-9)
for name,args,kwargs in [
 ('Evaluation budget',(lambda z:z**4,0,1,1e-12),dict(max_evals=3)),
 ('Depth budget',(lambda z:z**4,0,1,1e-12),dict(min_depth=0,max_depth=0)),
 ('Nonfinite sample',(lambda z:float('nan'),0,1,1e-8),{}),
 ('Adjacent floating endpoints',(lambda z:z,1,math.nextafter(1,2),1e-8),{}),
 ('Roundoff floor',(lambda z:1.,0,1,1e-18),{}),
]:
    try:adaptive(*args,**kwargs)
    except (ArithmeticError,ValueError) as e:check('Adaptive failure: '+name,True,str(e))
    else:check('Adaptive failure: '+name,False,'Unexpected success')
alias=lambda z:math.prod((z-j/16)**2 for j in range(17))
value,indicator,evals,intervals=adaptive(alias,0,1,1e-8)
check('Adaptive aliasing counterexample exactly sampled zeros',value==0 and indicator==0 and alias(1/32)>0,dict(value=value,indicator=indicator,evaluations=evals))

receipt=dict(owned_source_counts=counts,
             source_sha256={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in owned},
             checks=len(results),passed=sum(r['passed'] for r in results),
             failed=sum(not r['passed'] for r in results),results=results)
OUT.write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
for result in results:
    if not result['passed']:print('FAIL',result['name'],result['details'])
print(f"{receipt['passed']}/{receipt['checks']} checks passed; {OUT}")
sys.exit(bool(receipt['failed']))
