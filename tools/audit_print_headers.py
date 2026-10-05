from audit_edit import ROOT,save,record
import re
shorts=['Velocity and Distance','Numbers and Functions','Limits and Continuity','The Derivative','Differentiation Rules','Shape and the Mean Value Theorem','Optimization and Models','The Integral','The Fundamental Theorem','Applications of Integration','Integration Techniques','Numerical Calculus','Differential Equations','Parametric and Polar Curves','Sequences and Series','Power Series and Taylor Series','Complex Numbers and the Road Ahead']
for i,p in enumerate(sorted((ROOT/'source/chapters').glob('ch*/*.ptx'))):
 s=p.read_text('utf-8');b=re.search(r'<title>[\s\S]*?</title>',s).group();a=b+'\n  <shorttitle>'+shorts[i]+'</shorttitle>'
 if '<shorttitle>' in s:continue
 save(p,s.replace(b,a,1));record(p,'Provide a short running title to prevent print-header overflow',b,a)
