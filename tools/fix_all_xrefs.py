import os
import glob
import re

xref_alias_map = {
    'chap-integral-as-accumulation': 'ch08-the-integral-as-accumulation',
    'chap-what-integrals-measure': 'ch10-what-integrals-measure',
    'sec-signed-motion': 'sec-1-3-forward-backward-and-signed-motion',
    'sec-calculating-limits': 'sec-3-2-calculating-limits',
    'sec-precise-limit-definition': 'sec-3-4-the-precise-definition-of-a-limit',
    'sec-warning-examples-limits-continuity': 'sec-3-7-warning-examples',
    'sec-instantaneous-rate-of-change': 'sec-4-2-instantaneous-rate-of-change',
    'sec-local-absolute-extrema': 'sec-6-2-local-and-absolute-extrema',
    'sec-rolle-mvt': 'sec-6-3-rolle-s-theorem-and-the-mean-value-theorem',
    'sec-trigonometric-integrals': 'sec-11-2-trigonometric-integrals',
    'sec-one-dimensional-stokes-theorem': 'sec-17-4-the-one-dimensional-stokes-theorem',
}

# Collect all valid xml:ids
all_ids = set()
for f in sorted(glob.glob('source/**/*.xml', recursive=True) + glob.glob('source/**/*.ptx', recursive=True)):
    with open(f, encoding='utf-8', errors='ignore') as fp:
        txt = fp.read()
    for i in re.findall(r'xml:id="([^"]+)"', txt):
        all_ids.add(i)

# Also dynamically map any sec-* that matches a unique xml:id
for f in sorted(glob.glob('source/chapters/**/sections/*.xml', recursive=True)):
    sec_id = os.path.basename(f).replace('.xml', '')
    all_ids.add(sec_id)
    # e.g. sec-17-4-the-one-dimensional-stokes-theorem -> sec-the-one-dimensional-stokes-theorem, etc.
    parts = sec_id.split('-')
    if len(parts) > 3 and parts[1].isdigit() and parts[2].isdigit():
        short_slug = 'sec-' + '-'.join(parts[3:])
        if short_slug not in xref_alias_map and short_slug not in all_ids:
            xref_alias_map[short_slug] = sec_id

print(f"Aliases known: {len(xref_alias_map)}")

for f in sorted(glob.glob('source/**/*.xml', recursive=True) + glob.glob('source/**/*.ptx', recursive=True)):
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        txt = fp.read()
    orig = txt
    
    # 1. Replace aliases
    for alias, canonical in xref_alias_map.items():
        txt = re.sub(rf'<xref([^>]*)\bref="{re.escape(alias)}"', rf'<xref\1ref="{canonical}"', txt)
        
    # 2. Add text="title" to subsection xrefs if not present
    def fix_subsec_xref(m):
        full = m.group(0)
        ref = m.group(1)
        if ref.startswith('subsec-') and 'text=' not in full:
            return f'<xref ref="{ref}" text="title"/>'
        return full
    txt = re.sub(r'<xref[^>]*\bref="([^"]+)"[^>]*/>', fix_subsec_xref, txt)
    
    if txt != orig:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(txt)
        print(f"Fixed xrefs in: {f}")

print("Xref fixing complete.")
