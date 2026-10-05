from audit_edit import ROOT,replace,save,record
from lxml import etree as E
import math,json

def s(ch,n):return f'chapters/ch{ch:02}*/sections/sec-{ch}-{n}-*.xml'
replace(s(6,6),'Let <m>n</m> be a positive integer.  Consider',r'Let <m>n</m> be a positive integer. We write <m>n!=1\cdot2\cdots n</m> for its factorial, and use the convention <m>0!=1</m>. Consider','Define factorial notation before its first use')
replace(s(15,1),r'\lim_{n\to\infty}\frac{3n^2+2n-5}{n^2-4}.</me></p>',r'\lim_{n\to\infty}\frac{3n^2+2n-5}{n^2-4}.</me></p><p>Use the sequence for <m>n\ge3</m>; the quotient is undefined at <m>n=2</m>, which does not affect its limit.','Exclude the undefined early sequence term')
replace(s(15,2),'If <m>r=-1</m>, then','For the remaining divergent cases, assume <m>a\ne0</m>. If <m>r=-1</m>, then','Zero first term gives a convergent zero geometric series at every ratio')
replace(s(15,4),r'1.54977+\frac1{11} \le S \le 1.54977+\frac1{10}.',r'S_{10}+\frac1{11} \le S \le S_{10}+\frac1{10}.','Rigorous bounds must retain the unrounded partial sum')
replace(s(15,4),r'1.64067\lesssim S\lesssim1.64977.',r'1.64067&lt;S&lt;1.64977.','Round interval endpoints outward to preserve the guarantee')
replace(s(15,5),'There is also a sign rule.  The error has the sign of the first omitted term:', 'There is also a sign rule. If the error is nonzero, it has the sign of the first omitted term:', 'Weakly decreasing alternating terms can leave zero error')
replace(s(15,5),'So if the next term is positive, the true sum is above the partial sum.  If the next term is negative, the true sum is below the partial sum.', 'So if the next term is positive, the true sum is at least the partial sum. If the next term is negative, the true sum is at most the partial sum. Equality is possible when consecutive remaining terms cancel.', 'Use non-strict inequalities for general alternating-series bounds')
replace(s(15,7),'Suppose the target number is <m>T</m>.','Suppose the target number is <m>T</m>. Take unused positive terms in their original order, and do the same for negative terms. If the running sum already exceeds <m>T</m>, begin with the negative block. Insert any zero terms in their original order, one between successive blocks. Thus every original term is eventually used exactly once.','Specify a genuine rearrangement that exhausts both subsequences and zero terms')
replace(s(15,9),'with a rigorous error statement.</p>', 'with a rigorous error statement.</p><p>A short interval for <m>S</m> does not by itself mean that <m>S_N</m> is close to <m>S</m>: the interval may include a nonzero tail correction. To guarantee an error less than <m>0.001</m> for <m>S_N</m> itself, also require your upper bound for <m>|S-S_N|</m> to be less than <m>0.001</m>.','Distinguish interval width from the error of an uncorrected partial sum')
replace(s(16,1),'converges in a disk of some radius', 'converges in an interval of some radius','The variable and endpoints in this chapter are real')
replace(s(16,4),'The degree <m>n</m> Taylor polynomial for <m>f</m> centered at <m>a</m> is','The Taylor polynomial of order <m>n</m> for <m>f</m> centered at <m>a</m> has degree at most <m>n</m> and is','Vanishing leading coefficients can lower the polynomial degree')
replace(s(16,5),r'e=2.718254\ldots',r'e\approx2.718254','The displayed decimal is an approximation to e rather than an equality')
replace(s(16,5),r'Now integrate by parts with <p><me>u=f\'(t), \qquad dv=dt.</me></p>',r'Now integrate by parts with <p><me>u=f\'(t), \qquad dv=dt.</me></p>','dummy') if False else None
# Record independently recomputed, unchanged chapter 15 table.
receipt={str(n):{str(p):math.fsum(k**(-p) for k in range(1,n+1)) for p in [.99,1.01]} for n in [10,100,1000,10000]}
save(ROOT/'qa/audit/series-partial-sums.json',json.dumps(receipt,indent=2))
