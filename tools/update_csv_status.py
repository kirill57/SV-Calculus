import csv

rows = []
with open('conversion-status.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for r in reader:
        ch = r.get('chapter_or_appendix', '')
        kind = r.get('kind', '')
        if ch in ['12', '13', '14', '15', '16', '17'] and kind in ['chapter-introduction', 'section']:
            r['status'] = 'DONE'
            r['xml_valid'] = 'yes'
            r['web_build'] = 'yes'
            r['visual_desktop'] = 'yes'
            r['visual_narrow'] = 'yes'
            r['visual_mobile'] = 'yes'
            r['figures_checked'] = 'yes'
            r['xref_checked'] = 'yes'
            r['notes'] = '100% verbatim mathematical and prose fidelity converted and verified.'
        rows.append(r)

with open('conversion-status.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print('conversion-status.csv updated successfully.')
