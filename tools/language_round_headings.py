"""Align figurative headings with the revised questions and explanations."""
from language_audit import ROOT,record,write
from lxml import etree as E
headings={
'What promise is a limit making?':'What accuracy does a limit assertion require?',
'Units already tell the story':'Units of velocity and distance',
'The brachistochrone story':'The brachistochrone problem',
'Why is an exact antiderivative not the whole story?':'When is numerical integration needed?',
'Why are the two parts of the Fundamental Theorem the same story?':'How do the two parts of the Fundamental Theorem connect?',
'Why is a Taylor polynomial a local promise?':'What does a Taylor polynomial match at its center?',
'Why is differentiating the honest check of an antiderivative?':'How does differentiation check an antiderivative?',
'A new function is sometimes the honest answer':'Defining a function by an integral',
'Why can Euler’s method follow the wrong story?':'Why can Euler’s method contradict the exact solution?',
'What does damping change in the energy story?':'How does damping change the energy?',
'What story does the nonhomogeneous term <m>q(t)</m> tell?':'What input does the term <m>q(t)</m> represent?',
'Why does continuity not promise a derivative?':'Why does continuity not imply differentiability?',
'What continuity can and cannot promise':'Continuity and differentiability',
'Separation rule of honesty':'Check equilibrium solutions before division',
'Which Extreme Value Theorem hypotheses can quietly fail?':'Which Extreme Value Theorem hypotheses fail in these examples?',
'What does the Intermediate Value Theorem promise, and what does it refuse to compute?':'What does the Intermediate Value Theorem establish?',
'The logistic story':'Interpreting the logistic model',
'A model is a promise with conditions':'Check the model’s assumptions',
'Why is a model a promise with conditions?':'Why must a model’s assumptions be checked?',
}
for p in (ROOT/'source').rglob('*'):
    if p.suffix not in {'.xml','.ptx'}:continue
    text=p.read_text('utf-8');original=text
    xid=E.fromstring(text.encode()).get('{http://www.w3.org/XML/1998/namespace}id')
    applied=[]
    for before,after in headings.items():
        a='<title>'+before+'</title>';b='<title>'+after+'</title>'
        if a in text:text=text.replace(a,b);applied.append((a,b))
    if text!=original:
        E.fromstring(text.encode());write(p,text)
        for a,b in applied:record(p,xid,'Make the heading name the concept or question directly.',a,b)
print('Revised figurative headings.')
