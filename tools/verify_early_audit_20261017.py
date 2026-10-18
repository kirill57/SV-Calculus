"""Exact symbolic/numerical cross-checks for the October 17 early-book review.

These calculations supplement the written proof review; finite checks are not
presented as proofs of a general calculus theorem.
"""
from pathlib import Path
import json
import sympy as S

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "qa/audit-2026-10-17"
checks = []
x, h, y = S.symbols("x h y", real=True)


def check(label, actual, expected):
    residual = S.trigsimp(S.simplify(actual - expected))
    if residual != 0:
        residual = S.trigsimp(residual, method="fu")
    checks.append({"id": label, "passed": residual == 0,
                   "residual": str(residual)})


check("trip signed areas", 30 + 50 * S.Rational(3, 2) - 20 * S.Rational(3, 2) + 40, 115)
check("trip unsigned distance", 30 + 75 + 30 + 40, 175)
check("finite telescoping displacement", 2 + 4 + 1 - 3 + 5, 9)
check("step-model distance", 2 + 4 + 1 + 3 + 5, 15)
for n, left, mid, right in [
        (4, S.Rational(7, 4), S.Rational(21, 8), S.Rational(15, 4)),
        (8, S.Rational(35, 16), S.Rational(85, 32), S.Rational(51, 16)),
        (16, S.Rational(155, 64), S.Rational(341, 128), S.Rational(187, 64))]:
    step = S.Rational(2, n)
    check(f"chapter 1 left sum n={n}", sum((j * step) ** 2 * step for j in range(n)), left)
    check(f"chapter 1 midpoint sum n={n}", sum(((j + S.Rational(1, 2)) * step) ** 2 * step for j in range(n)), mid)
    check(f"chapter 1 right sum n={n}", sum((j * step) ** 2 * step for j in range(1, n + 1)), right)

for label, f, df in [
        ("product", (x*x+1)*(x**3-5), 5*x**4+3*x*x-10*x),
        ("product high powers", x**4*(x*x-3*x+2), 6*x**5-15*x**4+8*x**3),
        ("quotient", (x*x+1)/(x-3), (x*x-6*x-1)/(x-3)**2),
        ("rational derivative", x**3/(x*x+1), (x**4+3*x*x)/(x*x+1)**2),
        ("nested reciprocal", 1/(1+x*x)**3, -6*x/(1+x*x)**4),
        ("chain", (1+(2*x-3)**2)**5, 20*(2*x-3)*(1+(2*x-3)**2)**4),
        ("trigonometric quotient", S.cos(x)/(1+S.sin(x)), -1/(1+S.sin(x))),
        ("variable exponent", (x*x+1)**S.sin(x),
         (x*x+1)**S.sin(x)*(S.cos(x)*S.log(x*x+1)+2*x*S.sin(x)/(x*x+1))),
        ("hyperbolic product", S.exp(x)*S.cosh(x), S.exp(2*x)),
        ("graph-sketch rational first", x**3/(x*x-1), x*x*(x*x-3)/(x*x-1)**2),
        ("graph-sketch rational second", S.diff(x**3/(x*x-1), x), 2*x*(x*x+3)/(x*x-1)**3),
        ("chapter 6 quartic derivative", x**4-4*x*x, 4*x*(x*x-2)),
        ("chapter 6 cubic review derivative", x**3/3-x*x, x*(x-2)),
]:
    check(label, S.diff(f, x), df)

check("implicit cubic second derivative at (1,2)",
      -(6*S.Integer(2)*S.Rational(-2, 13)**2+2*S.Rational(-2, 13))/13,
      S.Rational(4, 2197))
circle_dy = -x/y
circle_d2y = S.diff(circle_dy, x) + S.diff(circle_dy, y)*circle_dy
check("circle implicit second derivative", S.together(circle_d2y).subs(x*x, 25-y*y), -25/y**3)

a, b = S.symbols("a b", real=True)
check("strict increase without MVT", (b**3+b)-(a**3+a), (b-a)*(a*a+a*b+b*b+1))
check("strict increase positivity identity", a*a+a*b+b*b, (a+b/2)**2+3*b*b/4)
f = lambda z: 2*z
g = lambda z: z+1
check("different composites same derivatives", S.diff(f(g(x)), x), S.diff(g(f(x)), x))

p, q = S.symbols("p q", positive=True)
check("midpoint inequality square identity", (p*p+q*q)/2-p*q, (p-q)**2/2)
B, D = S.symbols("B D", nonnegative=True)
check("square-root estimate nonnegative residual", (B+D)**2-B**2-D**2, 2*B*D)

for label, original, result in [
        ("A quadratic grouping", 6*x*x+x-2, (3*x+2)*(2*x-1)),
        ("A complete square 1", x*x-6*x+10, (x-3)**2+1),
        ("A complete square 2", 2*x*x+8*x-5, 2*(x+2)**2-13),
        ("A practice factoring 1", x*x+7*x+12, (x+3)*(x+4)),
        ("A practice factoring 2", 2*x*x-5*x-3, (2*x+1)*(x-3)),
        ("A practice complete square 1", x*x+10*x+13, (x+5)**2-12),
        ("A practice complete square 2", 3*x*x-12*x+7, 3*(x-2)**2-5),
        ("A rational sum", 1/x+1/(x+2), 2*(x+1)/(x*(x+2))),
        ("A reciprocal difference quotient", (1/(x+h)-1/x)/h, -1/(x*(x+h))),
        ("B circle completion", x*x+y*y+8*x-10*y+16, (x+4)**2+(y-5)**2-25),
        ("B hyperbola completion", 9*y*y-18*y-4*x*x-4*x-28, 9*(y-1)**2-4*(x+S.Rational(1, 2))**2-36),
        ("B ellipse completion", 4*x*x+9*y*y-16*x+18*y-11, 4*(x-2)**2+9*(y+1)**2-36),
]:
    check(label, original, result)

check("B diameter length", S.sqrt((5-(-3))**2+(8-2)**2), 10)
check("B midpoint x", S.Rational(-3+5, 2), 1)
check("B midpoint y", S.Rational(2+8, 2), 5)
check("C sine 75 degrees", S.sin(5*S.pi/12), (S.sqrt(6)+S.sqrt(2))/4)
check("C cosine 75 degrees", S.cos(5*S.pi/12), (S.sqrt(6)-S.sqrt(2))/4)
check("C tangent 105 degrees", S.tan(7*S.pi/12), -2-S.sqrt(3))
check("C product-to-sum sine-cosine", S.sin(5*x)*S.cos(2*x), (S.sin(7*x)+S.sin(3*x))/2)
check("C product-to-sum cosine-cosine", S.cos(4*x)*S.cos(x), (S.cos(5*x)+S.cos(3*x))/2)
check("quartic inflection ordinate left", (x**4-4*x*x).subs(x, -S.sqrt(S.Rational(2, 3))), -S.Rational(20, 9))
check("quartic inflection ordinate right", (x**4-4*x*x).subs(x, S.sqrt(S.Rational(2, 3))), -S.Rational(20, 9))
for n in (1, 2, 5, 20):
    check(f"finite cube-sum identity n={n}", sum(j**3 for j in range(1, n+1)), (S.Rational(n*(n+1), 2))**2)

failures = [c for c in checks if not c["passed"]]
report = {"checks": len(checks), "failures": failures, "results": checks,
          "scope": "Exact computational cross-checks; the existence and theorem-hypothesis arguments also require the written review."}
(OUT / "early-mathematical-checks.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(len(checks), "checks;", len(failures), "failures")
if failures:
    raise SystemExit(1)
