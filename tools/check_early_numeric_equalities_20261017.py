"""Check adjacent purely numeric equalities in the assigned early-book math.

Intentionally limited parser: unsupported or symbolic expressions are skipped,
not guessed. This complements, rather than replaces, full source reading.
"""
from pathlib import Path
import json
import re
from lxml import etree as E
import sympy as S
from sympy.parsing.sympy_parser import (
    parse_expr, standard_transformations, implicit_multiplication_application,
    rationalize,
)

ROOT = Path(__file__).resolve().parents[1]
functions = {"sin": S.sin, "cos": S.cos, "tan": S.tan, "exp": S.exp,
             "ln": S.log, "log": S.log, "sqrt": S.sqrt,
             "arcsin": S.asin, "arccos": S.acos, "arctan": S.atan,
             "pi": S.pi}
transforms = standard_transformations + (implicit_multiplication_application, rationalize)


def convert(src):
    src = src.strip().rstrip(".,;:")
    if any(x in src for x in ("\\begin", "\\sum", "\\lim", "\\pm", "\\circ", "\\approx", "\\amp", "\\infty", "\\to", "\\le", "\\ge", "<", ">", "\\neq")):
        raise ValueError("unsupported non-arithmetic expression")
    src = src.replace("{,}", "")
    src = re.sub(r"\\(?:left|right|bigl|bigr|Bigl|Bigr|displaystyle|quad|qquad)\b", " ", src)
    src = re.sub(r"\\[,;!]", " ", src)
    pos = 0

    def argument():
        nonlocal pos
        while pos < len(src) and src[pos].isspace():
            pos += 1
        if pos >= len(src):
            raise ValueError("missing argument")
        if src[pos] == "{":
            pos += 1
            return expression("}")
        if src[pos] == "\\":
            return command()
        value = src[pos]
        pos += 1
        return value

    def command():
        nonlocal pos
        pos += 1
        match = re.match(r"[A-Za-z]+", src[pos:])
        if not match:
            raise ValueError("unsupported control sequence")
        word = match[0]
        pos += len(word)
        if word in ("frac", "dfrac", "tfrac"):
            a, b = argument(), argument()
            return f"(({a})/({b}))"
        if word == "sqrt":
            return "sqrt(" + argument() + ")"
        if word == "text":
            # Units and explanatory labels are not arithmetic operands.
            argument()
            return ""
        if word in ("cdot", "times"):
            return "*"
        if word in functions:
            return word + " "
        raise ValueError("unsupported command " + word)

    def expression(close=None):
        nonlocal pos
        out = []
        while pos < len(src):
            char = src[pos]
            if char == close:
                pos += 1
                return "".join(out)
            if char == "\\":
                out.append(command())
            elif char == "{":
                pos += 1
                out.append("(" + expression("}") + ")")
            elif char == "^":
                pos += 1
                out.append("**(" + argument() + ")")
            elif char in ("$", "_", "&", "|", "[", "]", ":", "?", "!", "'", "\"", ","):
                raise ValueError("unsupported token " + char)
            else:
                pos += 1
                out.append(char)
        if close:
            raise ValueError("unclosed group")
        return "".join(out)

    result = expression().strip()
    names = re.findall(r"[A-Za-z]+", result)
    if any(name not in functions for name in names):
        raise ValueError("symbolic expression")
    value = parse_expr(result, local_dict=functions, transformations=transforms)
    if value.free_symbols or not value.is_number or value.has(S.zoo, S.oo, -S.oo, S.nan):
        raise ValueError("not a finite numeric expression")
    return value


paths = sorted((ROOT / "source/chapters").glob("ch0[1-6]-*/sections/*.xml"))
paths += sorted((ROOT / "source/appendices").glob("app[A-C]-*/sections/*.xml"))
results = []
for path in paths:
    tree = E.parse(str(path))
    for element in tree.xpath("//m|//me|//mrow"):
        source = ''.join(element.itertext())
        pieces = source.split("=")
        for left, right in zip(pieces, pieces[1:]):
            try:
                a, b = convert(left), convert(right)
            except Exception:
                continue
            delta = S.simplify(a-b)
            passed = delta == 0 or abs(complex(S.N(delta, 30))) < 1e-12
            results.append({"file": path.relative_to(ROOT).as_posix(),
                            "line": element.sourceline, "left": left,
                            "right": right, "passed": passed,
                            "residual": str(delta)})
report = {"checked_numeric_pairs": len(results),
          "failures": [r for r in results if not r["passed"]], "results": results}
(ROOT / "qa/audit-2026-10-17/early-numeric-equalities.json").write_text(
    json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(len(results), "numeric equality pairs checked;", len(report["failures"]), "to inspect")
for result in report["failures"]:
    print(json.dumps(result, ensure_ascii=False))
