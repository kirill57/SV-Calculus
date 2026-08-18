import glob
import re

# Collect all valid xml:ids
all_ids = set()
for f in sorted(glob.glob('source/**/*.xml', recursive=True) + glob.glob('source/**/*.ptx', recursive=True)):
    with open(f, encoding='utf-8', errors='ignore') as fp:
        txt = fp.read()
    ids = re.findall(r'xml:id="([^"]+)"', txt)
    for i in ids:
        all_ids.add(i)

targets = [
    'chap:differential-equations',
    'chap:numbers-functions-models',
    'chap:sequences-infinite-series',
    'fig:direction-field-one-minus-y',
    'fig:polar-coordinate-point',
    'sec:one-dimensional-stokes-theorem',
    'subsec:differentiating-power-series',
    'subsec:series-for-arctan',
    'subsec:series-for-log-one-plus-x'
]

for t in targets:
    t_clean = t.replace(':', '-')
    # find best match in all_ids
    matches = [i for i in all_ids if t_clean in i or i in t_clean or t.split(':')[-1] in i]
    print(f"Target: {t} -> Matches: {matches}")
