import os
import glob
import re
from collections import Counter

id_counts = Counter()
id_files = {}

for f in sorted(glob.glob('source/chapters/**/*.xml', recursive=True)):
    with open(f, encoding='utf-8', errors='ignore') as fp:
        txt = fp.read()
    ids = re.findall(r'xml:id="([^"]+)"', txt)
    for i in ids:
        id_counts[i] += 1
        if i not in id_files:
            id_files[i] = []
        id_files[i].append(f)

for f in sorted(glob.glob('source/chapters/**/*.ptx', recursive=True)):
    with open(f, encoding='utf-8', errors='ignore') as fp:
        txt = fp.read()
    ids = re.findall(r'xml:id="([^"]+)"', txt)
    for i in ids:
        id_counts[i] += 1
        if i not in id_files:
            id_files[i] = []
        id_files[i].append(f)

dups = {k: v for k, v in id_counts.items() if v > 1}
print(f"Total IDs: {len(id_counts)}, Duplicate IDs: {len(dups)}")
for k, count in sorted(dups.items()):
    print(f"  {k} ({count} times):")
    for fn in id_files[k]:
        print(f"    - {fn}")
