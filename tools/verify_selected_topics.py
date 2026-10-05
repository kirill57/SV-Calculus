"""Independent symbolic/numerical checks for the selected additions."""
from pathlib import Path
import json, math, inspect, ast
import sympy as s
from lxml import etree as E
from selected_numerical_methods import adaptive_simpson, ode_step, romberg_rows
ROOT=Path(__file__).resolve().parents[1]
out=ROOT/'qa/additions'
checks=[]
def check(name, passed, **details):
    checks.append({'name':name,'passed':bool(passed),**details})
def expect_failure(name, fn, message):
    try:
        fn(); check(name,False,reason='Returned success')
    except (ValueError,ArithmeticError) as exc:
        check(name,message in str(exc),message=str(exc))

x=s.symbols('x',real=True)
forms=[
 ('arsinh',s.log(x+s.sqrt(1+x*x)),1/s.sqrt(1+x*x),[-3,-s.Rational(1,2),0,2]),
 ('arcosh',s.log(x+s.sqrt(x*x-1)),1/s.sqrt(x*x-1),[s.Rational(3,2),3]),
 ('artanh',s.log((1+x)/(1-x))/2,1/(1-x*x),[-s.Rational(1,2),0,s.Rational(2,3)]),
 ('arcoth',s.log((x+1)/(x-1))/2,1/(1-x*x),[-3,-s.Rational(3,2),2]),
 ('arsech',s.log((1+s.sqrt(1-x*x))/x),-1/(x*s.sqrt(1-x*x)),[s.Rational(1,4),s.Rational(3,4)]),
 ('arcsch',s.log(1/x+s.sqrt(1+1/x**2)),-1/(s.Abs(x)*s.sqrt(1+x*x)),[-3,-s.Rational(1,2),s.Rational(1,3),2])]
for name, f, target, points in forms:
    diff=s.diff(f,x)-target
    check(name+' logarithmic derivative branches',all(abs(complex(diff.subs(x,v).evalf(60)))<1e-50 for v in points))

antiderivatives=[
 ('positive square root',s.acosh(x/3),1/s.sqrt(x*x-9),[4,6]),
 ('negative square root',-s.acosh(-x/3),1/s.sqrt(x*x-9),[-4,-6]),
 ('rational inside',s.atanh(x/3)/3,1/(9-x*x),[-2,0,2]),
 ('rational outside',s.log((x+3)/(x-3))/6,1/(9-x*x),[-4,4]),
 ('inverse sinh integral',x*s.asinh(x)-s.sqrt(1+x*x),s.asinh(x),[-2,0,2]),
 ('inverse cosh integral',x*s.acosh(x)-s.sqrt(x*x-1),s.acosh(x),[2,4]),
 ('inverse tanh integral',x*s.atanh(x)+s.log(1-x*x)/2,s.atanh(x),[-s.Rational(1,2),s.Rational(1,3)])]
for sign,points in ((1,[s.Rational(1,2),1]),(-1,[-s.Rational(1,2),-1])):
    u=sign*x/2
    antiderivatives.extend([
        ('reciprocal minus root '+str(sign),-s.acosh(1/u)/2,1/(x*s.sqrt(4-x*x)),points),
        ('reciprocal plus root '+str(sign),-s.asinh(1/u)/2,1/(x*s.sqrt(4+x*x)),points)])
for name,f,target,points in antiderivatives:
    check('antiderivative '+name,all(abs(complex((s.diff(f,x)-target).subs(x,v).evalf(60)))<1e-50 for v in points))

# Verify summation by parts on exact rational inputs, including p=q.
for p,q in ((1,1),(1,7),(4,9)):
    a={k:s.Rational((-1)**k,k+1) for k in range(1,q+1)}
    b={k:s.Rational(1,k+2) for k in range(1,q+1)}
    A=lambda k:sum(a[j] for j in range(p,k+1))
    lhs=sum(a[k]*b[k] for k in range(p,q+1))
    rhs=A(q)*b[q]+sum(A(k)*(b[k]-b[k+1]) for k in range(p,q))
    check(f'summation by parts {p}:{q}',lhs==rhs)
theta=s.pi/7
for n in (1,4,12):
    lhs=sum(s.sin(k*theta) for k in range(1,n+1))
    rhs=(s.cos(theta/2)-s.cos((n+s.Rational(1,2))*theta))/(2*s.sin(theta/2))
    check(f'Dirichlet sine telescoping n={n}',abs(float((lhs-rhs).evalf(40)))<1e-35)

for k in range(5):
    value,error,evals,panels=adaptive_simpson(lambda x:x**k,0,1,1e-10)
    check(f'adaptive monomial degree {k}',abs(value-1/(k+1))<1e-10 and error<=1e-10,
          value=value,actualError=abs(value-1/(k+1)),indicator=error,evaluations=evals,leaves=len(panels))
value,error,evals,panels=adaptive_simpson(lambda x:4/(1+x*x),0,1,1e-8)
check('adaptive pi reference',abs(value-math.pi)<1e-8 and error<=1e-8,
      actualError=abs(value-math.pi),indicator=error,evaluations=evals)
f=lambda x:math.exp(-2500*(x-.37)**2)
value,error,evals,panels=adaptive_simpson(f,0,1,1e-9)
reference=math.sqrt(math.pi)/100*(math.erf(50*.63)+math.erf(50*.37))
near=[b-a for a,b in panels if abs((a+b)/2-.37)<.05]
far=[b-a for a,b in panels if abs((a+b)/2-.37)>.2]
check('adaptive localized Gaussian reference and refinement',abs(value-reference)<1e-9 and min(near)<max(far),
      actualError=abs(value-reference),indicator=error,evaluations=evals,leaves=len(panels))
expect_failure('adaptive evaluation budget',lambda:adaptive_simpson(lambda x:x**4,0,1,1e-8,max_evals=3),'Evaluation budget')
expect_failure('adaptive max depth',lambda:adaptive_simpson(lambda x:x**4,0,1,1e-15,max_depth=0,min_depth=0),'Maximum subdivision')
expect_failure('adaptive invalid tolerance',lambda:adaptive_simpson(lambda x:x,0,1,0),'tol > 0')
expect_failure('adaptive invalid interval',lambda:adaptive_simpson(lambda x:x,1,0,1e-8),'a < b')
expect_failure('adaptive invalid depth',lambda:adaptive_simpson(lambda x:x,0,1,1e-8,max_depth=0),'depth')
expect_failure('adaptive nonfinite sample',lambda:adaptive_simpson(lambda x:math.inf,0,1,1e-8),'Nonfinite function')
expect_failure('adaptive representable midpoint',lambda:adaptive_simpson(lambda x:x,1,math.nextafter(1,2),1e-8),'No representable')
expect_failure('adaptive roundoff floor',lambda:adaptive_simpson(lambda x:1,0,1,1e-30),'roundoff indicator')
g=lambda x:math.prod((x-j/16)**2 for j in range(17))
v,e,n,panels=adaptive_simpson(g,0,1,1e-35)
gp=s.prod((x-s.Rational(j,16))**2 for j in range(17))
exact=s.integrate(gp,(x,0,1))
check('aliasing counterexample: estimator is not certificate',v==0 and e==0 and exact>0,
      returned=v,indicator=e,positiveIntegral=float(exact),evaluations=n)
# Printed Python is the executable algorithm, not an unchecked transcription.
file=next((ROOT/'source').rglob('sec-additional-adaptive-quadrature.xml'))
printed=E.parse(str(file)).find('.//pre').text
ns={};exec(compile(printed,'printed-adaptive','exec'),ns)
check('printed adaptive code matches executable function',
      ast.dump(ast.parse(inspect.getsource(adaptive_simpson)).body[0])==
      ast.dump(next(n for n in ast.parse(printed).body if isinstance(n,ast.FunctionDef))))
check('printed adaptive code executes',abs(ns['adaptive_simpson'](lambda x:x**4,0,1,1e-10)[0]-.2)<1e-10)

rows=romberg_rows(lambda x:x**4,0,1,3)
target=[[.5],[.28125,5/24],[.220703125,77/384, .2]]
check('Romberg printed quartic table',all(abs(a-b)<1e-15 for row,trow in zip(rows,target) for a,b in zip(row,trow)),rows=rows)
rows=romberg_rows(lambda x:x*x,0,1,4)
check('Romberg quadratic exact first column',all(abs(row[1]-1/3)<1e-15 for row in rows[1:]))
h=s.symbols('h')
c,I=s.symbols('c I')
check('Richardson cubic leading cancellation',s.expand((8*(I+c*(h/2)**3)-(I+c*h**3))/7)==I)
check('two-panel Simpson derivative-bound constant',2*s.Rational(1,2)**5/2880==s.Rational(1,46080))

# An independently computed exact-arithmetic stage expansion for a time-dependent,
# nonlinear polynomial slope law. This catches stage time and state mistakes.
t,y=s.symbols('t y')
F=lambda t,y:1+t+t*y+y*y
trim=lambda z:s.series(z,h,0,5).removeO().expand()
k1=F(t,y);k2=trim(F(t+h/2,y+h*k1/2))
k3=trim(F(t+h/2,y+h*k2/2));k4=trim(F(t+h,y+h*k3))
increment=trim(h*(k1+2*k2+2*k3+k4)/6)
D=lambda z:s.diff(z,t)+F(t,y)*s.diff(z,y)
exact=trim(h*F(t,y)+h*h*D(F(t,y))/2+h**3*D(D(F(t,y)))/6+h**4*D(D(D(F(t,y))))/24)
check('RK4 nonlinear nonautonomous Taylor match degree four',s.expand(increment-exact)==0)
errors={}
for method,order in (('Euler',1),('Heun',2),('Midpoint',2),('RK4',4)):
    ee=[]
    for n in (16,32,64):
        yy=1.
        for j in range(n):yy=ode_step(lambda t,y:t+y,j/n,yy,1/n,method)
        ee.append(abs(yy-(2*math.e-2)))
    ratios=[ee[i]/ee[i+1] for i in range(2)]
    check(f'{method} observed order on time-dependent ODE',abs(ratios[-1]-2**order)<.15*2**order,
          errors=ee,ratios=ratios)
    errors[method]=ee
check('RK4 stability counterexample',ode_step(lambda t,y:-4*y,0,1,1,'RK4')==5)
for n in (1,3,13):
    xx=0.
    for j in range(n):xx=(xx+2)/3
    bound=3**(-n)
    check(f'contraction a priori bound n={n}',abs(xx-1)<=bound+2e-16,error=abs(xx-1),bound=bound)
for c in (0.,1.,2.):
    for tt in (-1.,c,c+.5):
        yy=max(tt-c,0)**2;dy=2*max(tt-c,0)
        check(f'waiting solution c={c} t={tt}',dy==2*math.sqrt(abs(yy)))

file=out/'mathematical-checks.json'
file.write_text(json.dumps(checks,indent=2),encoding='utf-8')
failed=[c['name'] for c in checks if not c['passed']]
print(json.dumps({'checks':len(checks),'failed':failed},indent=2))
raise SystemExit(bool(failed))
