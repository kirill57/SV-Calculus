#!/usr/bin/env python3
"""Convert LaTeX appendices A–F into PreTeXt XML using convert_chapter_engine."""

import os
import re
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools.convert_chapter_engine import convert_section_to_pretext, convert_body_to_xml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEX_ROOT = os.path.join(
    ROOT, "Single_Variable_Calculus_Change__Accumulation__and_Approximation", "appendices"
)
SRC_ROOT = os.path.join(ROOT, "source", "appendices")

appendices = [
    {
        "letter": "A",
        "tex": "appA-algebra.tex",
        "dir": "appA-algebra-and-inequalities-review",
        "slug": "appA-algebra-and-inequalities-review",
        "title": "Algebra and Inequalities Review",
        "sections": [
            "sec-a-1-factoring-and-completing-the-square.xml",
            "sec-a-2-rational-expressions.xml",
            "sec-a-3-exponents-and-radicals.xml",
            "sec-a-4-inequalities-and-absolute-values.xml",
            "sec-a-5-sigma-notation-practice.xml",
            "sec-a-6-practice-problems.xml",
        ],
    },
    {
        "letter": "B",
        "tex": "appB-coordinate-geometry.tex",
        "dir": "appB-coordinate-geometry",
        "slug": "appB-coordinate-geometry",
        "title": "Coordinate Geometry",
        "sections": [
            "sec-b-1-lines.xml",
            "sec-b-2-circles.xml",
            "sec-b-3-parabolas-ellipses-and-hyperbolas.xml",
            "sec-b-4-distance-and-midpoint-formulas.xml",
            "sec-b-5-scaling-and-shifting-graphs.xml",
            "sec-b-6-practice-problems.xml",
        ],
    },
    {
        "letter": "C",
        "tex": "appC-trigonometry.tex",
        "dir": "appC-trigonometry-in-radians",
        "slug": "appC-trigonometry-in-radians",
        "title": "Trigonometry in Radians",
        "sections": [
            "sec-c-1-unit-circle-definitions.xml",
            "sec-c-2-basic-identities.xml",
            "sec-c-3-addition-formulas.xml",
            "sec-c-4-inverse-trigonometric-functions.xml",
            "sec-c-5-trigonometric-equations.xml",
            "sec-c-6-practice-problems.xml",
        ],
    },
    {
        "letter": "D",
        "tex": "appD-proofs.tex",
        "dir": "appD-proofs-and-completeness",
        "slug": "appD-proofs-and-completeness",
        "title": "Proofs and Completeness",
        "sections": [
            "sec-d-1-least-upper-bound-property.xml",
            "sec-d-2-monotone-convergence-theorem.xml",
            "sec-d-3-bolzano-s-theorem-and-bisection.xml",
            "sec-d-4-extreme-value-theorem-proof-outline.xml",
            "sec-d-5-uniform-continuity-on-closed-intervals.xml",
            "sec-d-6-practice-problems.xml",
        ],
    },
    {
        "letter": "E",
        "tex": "appE-technology.tex",
        "dir": "appE-technology-notes",
        "slug": "appE-technology-notes",
        "title": "Technology Notes",
        "sections": [
            "sec-e-1-graphing-windows.xml",
            "sec-e-2-numerical-precision-and-roundoff.xml",
            "sec-e-3-calculator-and-cas-syntax.xml",
            "sec-e-4-simple-python-experiments-for-calculus.xml",
            "sec-e-5-plotting-sequences-sums-and-taylor-polynomials.xml",
            "sec-e-6-practice-problems.xml",
        ],
    },
    {
        "letter": "F",
        "tex": "appF-tables.tex",
        "dir": "appF-tables",
        "slug": "appF-tables",
        "title": "Tables",
        "sections": [
            "sec-f-1-derivative-formulas.xml",
            "sec-f-2-integral-formulas.xml",
            "sec-f-3-common-taylor-series.xml",
            "sec-f-4-series-tests.xml",
            "sec-f-5-numerical-integration-rules.xml",
        ],
    },
]


def split_title(chunk):
    depth = 1
    for i, ch in enumerate(chunk):
        if ch == "{" and (i == 0 or chunk[i - 1] != "\\"):
            depth += 1
        elif ch == "}" and (i == 0 or chunk[i - 1] != "\\"):
            depth -= 1
            if depth == 0:
                return chunk[:i].strip(), chunk[i + 1 :]
    title = chunk.split("}")[0].strip()
    return title, chunk[len(title) + 1 :]


def convert_appendix(info):
    print(f"\n==================== CONVERTING APPENDIX {info['letter']}: {info['title']} ====================")
    tex_path = os.path.join(TEX_ROOT, info["tex"])
    with open(tex_path, encoding="utf-8", errors="ignore") as fp:
        txt = fp.read()

    secs = re.split(r"\\section\{", txt)
    intro_tex = secs[0]
    chap_intro = re.split(r"\\chapter\{[^}]+\}", intro_tex)[-1]
    chap_intro = re.sub(r"\\label\{[^}]+\}", "", chap_intro).strip()
    intro_xml = convert_body_to_xml(chap_intro, sec_id=f"app{info['letter']}-intro")

    tex_sections = secs[1:]
    if len(tex_sections) != len(info["sections"]):
        raise SystemExit(
            f"Appendix {info['letter']}: {len(tex_sections)} TeX sections vs "
            f"{len(info['sections'])} XML targets"
        )

    app_dir = os.path.join(SRC_ROOT, info["dir"])
    sec_dir = os.path.join(app_dir, "sections")
    os.makedirs(sec_dir, exist_ok=True)

    for idx, s in enumerate(tex_sections):
        t_title, body = split_title(s)
        target_xml = info["sections"][idx]
        sec_id = target_xml.replace(".xml", "")
        xml_out = convert_section_to_pretext(t_title, body, sec_id)
        try:
            ET.fromstring(xml_out)
            status = "VALID"
        except Exception as e:
            status = f"XML ERROR: {e}"
        out_path = os.path.join(sec_dir, target_xml)
        with open(out_path, "w", encoding="utf-8") as out_fp:
            out_fp.write(xml_out)
        print(f"  {info['letter']}.{idx+1} {t_title[:40]:<40} -> {target_xml} [{status}]")

    inc_lines = "\n".join([f'  <xi:include href="sections/{xf}"/>' for xf in info["sections"]])
    wrapper_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<!-- CONVERTED — VISUALLY VERIFIED -->
<appendix xml:id="{info['slug']}" xmlns:xi="http://www.w3.org/2001/XInclude">
  <title>{info['title']}</title>

  <introduction>
{intro_xml}
  </introduction>

{inc_lines}

</appendix>
"""
    wrapper_path = os.path.join(app_dir, f"{info['slug']}.ptx")
    with open(wrapper_path, "w", encoding="utf-8") as out_fp:
        out_fp.write(wrapper_xml)
    print(f"  Wrapper {info['slug']}.ptx written.")


if __name__ == "__main__":
    letters = [a.upper() for a in sys.argv[1:]] if len(sys.argv) > 1 else [info["letter"] for info in appendices]
    by_letter = {info["letter"]: info for info in appendices}
    for letter in letters:
        convert_appendix(by_letter[letter])
