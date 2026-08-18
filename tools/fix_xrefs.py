import os
import glob
import re

xref_replacements = {
    'chap:differential-equations': 'ch13-differential-equations-laws-written-as-derivatives',
    'chap:numbers-functions-models': 'ch02-numbers-functions-and-models',
    'chap:sequences-infinite-series': 'ch15-sequences-and-infinite-series',
    'fig:direction-field-one-minus-y': 'fig-direction-field-one-minus-y',
    'fig:polar-coordinate-point': 'fig-polar-coordinate-point',
    'sec:one-dimensional-stokes-theorem': 'sec-17-4-the-one-dimensional-stokes-theorem',
    'subsec:differentiating-power-series': 'subsec-differentiating-power-series',
    'subsec:series-for-arctan': 'subsec-series-for-arctan',
    'subsec:series-for-log-one-plus-x': 'subsec-series-for-log-one-plus-x'
}

for f in sorted(glob.glob('source/chapters/**/*.xml', recursive=True)):
    with open(f, 'r', encoding='utf-8') as fp:
        txt = fp.read()
    orig = txt
    for old_ref, new_ref in xref_replacements.items():
        txt = txt.replace(f'<xref ref="{old_ref}"/>', f'<xref ref="{new_ref}"/>')
    if txt != orig:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(txt)
        print(f"Fixed xrefs in {f}")

print("Cross-references fixed.")
