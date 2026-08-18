import os
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

print(f"Total valid xml:ids: {len(all_ids)}")

# Collect all xref refs
missing_xrefs = {}
for f in sorted(glob.glob('source/chapters/**/*.xml', recursive=True) + glob.glob('source/chapters/**/*.ptx', recursive=True)):
    with open(f, encoding='utf-8', errors='ignore') as fp:
        txt = fp.read()
    xrefs = re.findall(r'<xref[^>]*\bref="([^"]+)"', txt)
    for xr in xrefs:
        if xr not in all_ids:
            if xr not in missing_xrefs:
                missing_xrefs[xr] = []
            missing_xrefs[xr].append(f)

print(f"Total missing xrefs: {len(missing_xrefs)}")
for k, files in sorted(missing_xrefs.items()):
    print(f"  {k} in {len(files)} files: {files[0]}")
