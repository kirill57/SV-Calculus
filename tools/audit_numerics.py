from pathlib import Path
from lxml import etree as E
import math,json,io,contextlib
ROOT=Path(__file__).resolve().parents[1]
receipts=[]
def q(f,a,b,n,kind):
 h=(b-a)/n
 if kind=='M':return h*sum(f(a+(i+.5)*h) for i in range(n))
 if kind=='T':return h*(.5*f(a)+sum(f(a+i*h) for i in range(1,n))+.5*f(b))
 return h/3*(f(a)+f(b)+sum((4 if i%2 else 2)*f(a+i*h) for i in range(1,n)))
funs={'pi':(lambda x:4/(1+x*x),0,1),'normal':(lambda x:math.exp(-x*x/2)/math.sqrt(2*math.pi),-1,1),'gaussian':(lambda x:math.exp(-x*x),0,1),'sqrt':(math.sqrt,0,1)}
t=E.parse(str(next((ROOT/'source').glob('**/sec-12-6-*.xml'))))
ids=[('2',['pi']*3,['M','T','S']),('3',['normal'],['S']),('4',['gaussian','sqrt'],['S','S'])]
for suffix,fnames,kinds in ids:
 tab=t.xpath('//table[@xml:id="tab-sec-12-6-computing-experiments-'+suffix+'"]',namespaces={'xml':'http://www.w3.org/XML/1998/namespace'})[0]
 for row in tab.findall('.//row')[1:]:
  cells=[''.join(c.itertext()).strip() for c in row.findall('cell')];n=int(cells[0])
  for printed,fname,kind in zip(cells[1:],fnames,kinds):
   f,a,b=funs[fname];actual=q(f,a,b,n,kind);ok=abs(actual-float(printed))<=.500001e-6
   receipts.append(dict(check='quadrature table',function=fname,rule=kind,n=n,printed=printed,computed=actual,passed=ok))
for n in range(4):
 x=(n+.5)/4; actual=math.exp(-x*x)
 receipts.append(dict(check='Gaussian midpoint sample',x=x,computed=actual,passed=True))
for j in range(4):
 for k in ('M','T','S'):
  actual=q(lambda x:x**j,0,1,4,k)
  if k=='S' or j<2:receipts.append(dict(check='Polynomial exactness',degree=j,rule=k,computed=actual,passed=abs(actual-1/(j+1))<1e-14))
# Execute the actual printed appendix snippets in their intended order.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
code_output=[]
for glob in ('**/sec-e-4-*.xml','**/sec-e-5-*.xml'):
 p=next((ROOT/'source').glob(glob));tree=E.parse(str(p));ns={};out=io.StringIO()
 with contextlib.redirect_stdout(out):
  for i,pre in enumerate(tree.findall('.//pre')):
   exec(compile(pre.text,str(p)+':snippet'+str(i+1),'exec'),ns)
   for num in plt.get_fignums():
    fig=plt.figure(num);fig.savefig(ROOT/'qa/audit'/f'python-{p.stem}-{i+1}.png');plt.close(fig)
 code_output.append(dict(file=str(p.relative_to(ROOT)),snippets=len(tree.findall('.//pre')),output=out.getvalue(),passed=True))
receipts+=code_output
receipts.append(dict(check='positive bank balance',computed=30000*(math.exp(.4)-1),passed=abs(30000*(math.exp(.4)-1)-14754.74)<.005))
piapprox=4*sum((-1)**k*(1/2)**(2*k+1)/(2*k+1)+(-1)**k*(1/3)**(2*k+1)/(2*k+1) for k in range(5))
receipts.append(dict(check='arctangent pi approximation',computed=piapprox,error=abs(piapprox-math.pi),passed=abs(piapprox-math.pi)<.00018))
(ROOT/'qa/audit/numerical-code-checks.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
failed=[r for r in receipts if not r['passed']];print('CHECKS',len(receipts),'FAILED',len(failed));print(json.dumps(failed,indent=2))
