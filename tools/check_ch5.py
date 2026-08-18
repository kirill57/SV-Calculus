import glob
import re
import os

with open('Single_Variable_Calculus_Change__Accumulation__and_Approximation/chapters/ch05-differentiation-rules.tex', encoding='utf-8') as fp:
    tex_raw = fp.read()
tex_secs = re.split(r'\\section\{', tex_raw)[1:]
print(f"LaTeX has {len(tex_secs)} sections in Chapter 5:")
for i, s in enumerate(tex_secs):
    print(f"  [{i+1}] {s.split('}')[0]}")

from tools.verify_paragraphs_and_formulas import section_sort_key

xml_files = sorted(glob.glob('source/chapters/ch05-differentiation-rules-and-elementary-functions/sections/*.xml'), key=section_sort_key)
print(f"\nXML has {len(xml_files)} files in Chapter 5:")
for i, x in enumerate(xml_files):
    print(f"  [{i+1}] {os.path.basename(x)}")
