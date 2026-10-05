from audit_edit import ROOT,save,record
from lxml import etree as E

def figure(xid,changes):
 matches=[]
 for p in (ROOT/'source').rglob('*.xml'):
  t=E.parse(str(p));found=t.xpath('//*[@xml:id=$id]',namespaces={'xml':'http://www.w3.org/XML/1998/namespace'},id=xid)
  if found:matches.append((p,t,found[0]))
 assert len(matches)==1,xid
 p,t,e=matches[0];im=e.find('.//latex-image');before=im.text;after=changes(before)
 assert after!=before,xid
 im.text=after;save(p,E.tostring(t,encoding='UTF-8',xml_declaration=True));record(p,'Correct geometry or overlapping labels in '+xid,before,after)
figure('fig-radius-of-convergence',lambda q:q.replace(r'\node[above] at (-1.5,0.15) {converges absolutely};',r'\node[above] at (0,0.65) {converges absolutely inside};').replace(r'\node[above] at (1.5,0.15) {inside};',''))
figure('fig-fourth-roots-unity',lambda q:q.replace(r'\node[\pos]',r'\node[\pos, inner sep=6pt]'))
figure('fig-spring-solution-amplitude-phase',lambda q:q.replace(r'\node[anchor=west] at (axis cs:0.4,3.8)',r'\node[anchor=south] at (rel axis cs:0.5,1.04)').replace(r'\node[anchor=west] at (axis cs:4.35,4.55)',r'\node[anchor=north] at (rel axis cs:0.72,0.38)'))
figure('fig-phase-plane-energy-ellipse',lambda q:q.replace(r'width=0.62\textwidth,',r'width=0.62\textwidth, axis equal image,').replace('{6*sin(x)}','{-6*sin(x)}').replace(r'\draw[->, thick] (axis cs:3,0) arc [start angle=0, end angle=35, x radius=3, y radius=6];',r'\draw[->, thick] (axis cs:3,0) -- (axis cs:2.954,-1.042) -- (axis cs:2.819,-2.052);').replace(r'\node[anchor=west] at (axis cs:1.15,5.3)',r'\node[align=center] at (axis cs:0,2.2)').replace('constant energy curve',r'constant\\energy curve').replace(r'\node[anchor=west] at (axis cs:0.6,-4.7)',r'\node at (axis cs:0,-2.2)'))
figure('fig-rational-hole-sqrt2',lambda q:q.replace('(1.58,0.15)','(1.58,0.7)'))
figure('fig-evt-maximum-reached',lambda q:q.replace('2.4 + 1.0*sin(deg(1.5*x)) - 0.18*(x-2.6)^2 + 0.25*cos(deg(3*x))','3 - 0.18*(x-1.4)^2').replace('1.402','1.4').replace('3.176','3').replace('(axis cs:3.0,3.26)','(axis cs:3.0,3)'))
figure('fig-trig-substitution-domain-branches',lambda q:q.replace('fill=white','fill=black').replace(r'\(x>2\)',r'\(x\ge2\)').replace(r'\(x<-2\)',r'\(x\le-2\)').replace('real only on two separate intervals','real on two closed intervals; antiderivatives use the interiors'))
figure('fig-rational-complete-sketch',lambda q:q.replace(r'anchor=south east] at (axis cs:-1.85,-2.15)',r'anchor=west] at (axis cs:-1.732,-2.598)').replace(r'anchor=north west] at (axis cs:1.85,2.15)',r'anchor=west] at (axis cs:1.732,2.598)').replace(r'anchor=south] at (axis cs:-0.35,0.22)',r'anchor=west] at (axis cs:0,0)'))
# Add the picture needed to see the moving-spike counterexample.
p=next((ROOT/'source').glob('chapters/ch16*/sections/sec-16-8-*.xml'));t=E.parse(str(p));ss=t.xpath('//*[p[contains(.,"Pointwise convergence can fail to control area")]]')
section=next(e for e in t.findall('.//subsection') if any('Pointwise convergence can fail to control area' in ''.join(v.itertext()) for v in e.findall('p')))
f=E.fromstring(r'''<figure xml:id="fig-shrinking-spikes-fixed-area"><caption>The spikes for <m>n=4</m> and <m>n=8</m> become narrower and taller, while each has area <m>1</m>.</caption><image width="75%"><latex-image>
\begin{tikzpicture}
\begin{axis}[width=0.8\textwidth,height=0.48\textwidth,xmin=0,xmax=1,ymin=0,ymax=9,axis lines=left,xlabel={$x$},ylabel={$g_n(x)$},xtick={0,0.125,0.25,0.5,1},ytick={0,4,8},legend style={draw=none,at={(0.98,0.97)},anchor=north east}]
\addplot[very thick] coordinates {(0,0)(0.25,4)(0.5,0)(1,0)};\addlegendentry{$n=4$}
\addplot[very thick,dashed] coordinates {(0,0)(0.125,8)(0.25,0)(1,0)};\addlegendentry{$n=8$}
\end{axis}
\end{tikzpicture}
</latex-image></image></figure>''')
section.insert(2,f);save(p,E.tostring(t,encoding='UTF-8',xml_declaration=True));record(p,'Illustrate the shrinking-spike counterexample with fixed area','missing illustration',E.tostring(f,encoding='unicode'))
