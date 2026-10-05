"""Executable numerical examples accompanying the selected PreTeXt additions."""
from math import isfinite, fsum
from sys import float_info


def adaptive_simpson(f, a, b, tol, max_depth=20,
                     max_evals=100000, min_depth=2):
    """Return (value, estimated_error, evaluations, accepted_intervals).

    Error is an estimator, not a rigorous bound for arbitrary functions.
    Fail explicitly on invalid inputs or exhausted safeguards.
    """
    if not all(isfinite(v) for v in (a, b, tol, b-a)):
        raise ValueError("Require finite endpoints, width, and tolerance")
    if not a < b or not tol > 0:
        raise ValueError("Require a < b and tol > 0")
    if (type(min_depth) is not int or type(max_depth) is not int
            or not 0 <= min_depth <= max_depth
            or type(max_evals) is not int or max_evals < 3):
        raise ValueError("Invalid depth or evaluation budget")
    evaluations = 0

    def sample(x):
        nonlocal evaluations
        if evaluations >= max_evals:
            raise ArithmeticError("Evaluation budget exhausted")
        evaluations += 1
        value = f(x)
        if not isfinite(value):
            raise ArithmeticError("Nonfinite function value")
        return value

    def midpoint(left, right):
        mid = left + (right-left)/2
        if not left < mid < right:
            raise ArithmeticError("No representable midpoint")
        return mid

    def simpson(left, right, fl, fm, fr):
        value = ((right-left)/6)*fsum((fl, 4*fm, fr))
        if not isfinite(value):
            raise ArithmeticError("Nonfinite quadrature value")
        return value

    m = midpoint(a, b)
    fa, fm, fb = sample(a), sample(m), sample(b)
    coarse = simpson(a, b, fa, fm, fb)
    stack = [(a, b, fa, fm, fb, coarse, tol, 0)]
    values, errors, intervals = [], [], []
    while stack:
        left, right, fl, fm, fr, old, budget, depth = stack.pop()
        mid = midpoint(left, right)
        lm, rm = midpoint(left, mid), midpoint(mid, right)
        f_lm, f_rm = sample(lm), sample(rm)
        sl = simpson(left, mid, fl, f_lm, fm)
        sr = simpson(mid, right, fm, f_rm, fr)
        fine = fsum((sl, sr))
        delta = fine-old
        floor = 50*float_info.epsilon*(abs(sl)+abs(sr))
        estimate = max(abs(delta)/15, floor)
        corrected = fine+delta/15
        if not all(isfinite(v) for v in (fine, estimate, corrected)):
            raise ArithmeticError("Nonfinite refinement result")
        if depth >= min_depth and estimate <= budget:
            values.append(corrected)
            errors.append(estimate)
            intervals.append((left, right))
            continue
        if depth >= max_depth:
            raise ArithmeticError("Maximum subdivision depth reached")
        if depth >= min_depth and budget < floor:
            raise ArithmeticError("Tolerance below roundoff indicator")
        half_budget = budget/2
        if half_budget == 0:
            raise ArithmeticError("Tolerance budget underflow")
        # Right child first: the left child is processed next.
        stack.append((mid, right, fm, f_rm, fr, sr,
                      half_budget, depth+1))
        stack.append((left, mid, fl, f_lm, fm, sl,
                      half_budget, depth+1))
    value, error = fsum(values), fsum(errors)
    if not isfinite(value) or not isfinite(error) or error > tol:
        raise ArithmeticError("Final accumulation failed")
    return value, error, evaluations, intervals


def ode_step(f, t, y, h, method):
    k1 = f(t, y)
    if method == "Euler":
        return y+h*k1
    if method == "Heun":
        k2 = f(t+h, y+h*k1)
        return y+h*(k1+k2)/2
    if method == "Midpoint":
        k2 = f(t+h/2, y+h*k1/2)
        return y+h*k2
    if method == "RK4":
        k2 = f(t+h/2, y+h*k1/2)
        k3 = f(t+h/2, y+h*k2/2)
        k4 = f(t+h, y+h*k3)
        return y+h*(k1+2*k2+2*k3+k4)/6
    raise ValueError("Unknown method")


def romberg_rows(f, a, b, levels):
    """Rows R[k][j], with levels a positive integer."""
    if type(levels) is not int or levels < 1 or not a < b:
        raise ValueError("Require positive levels and a < b")
    t = (b-a)*(f(a)+f(b))/2
    if not isfinite(t):
        raise ArithmeticError("Nonfinite initial trapezoid")
    rows = [[t]]
    for k in range(1, levels):
        h = (b-a)/(2**k)
        if not a < a+h < b:
            raise ArithmeticError("Grid cannot be refined")
        t = rows[-1][0]/2+h*fsum(
            f(a+(2*i-1)*h) for i in range(1, 2**(k-1)+1))
        row = [t]
        for j in range(1, k+1):
            row.append(row[j-1]+(row[j-1]-rows[k-1][j-1])
                       /(4**j-1))
        if not all(isfinite(v) for v in row):
            raise ArithmeticError("Nonfinite Romberg row")
        rows.append(row)
    return rows
