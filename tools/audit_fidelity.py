import os
import re

latex_files = {
    1: 'Single_Variable_Calculus_Change__Accumulation__and_Approximation/chapters/ch01-velocity-distance.tex',
    2: 'Single_Variable_Calculus_Change__Accumulation__and_Approximation/chapters/ch02-numbers-functions.tex',
    3: 'Single_Variable_Calculus_Change__Accumulation__and_Approximation/chapters/ch03-limits-continuity.tex',
    4: 'Single_Variable_Calculus_Change__Accumulation__and_Approximation/chapters/ch04-derivative.tex',
    5: 'Single_Variable_Calculus_Change__Accumulation__and_Approximation/chapters/ch05-differentiation-rules.tex',
    6: 'Single_Variable_Calculus_Change__Accumulation__and_Approximation/chapters/ch06-shape-extremes.tex',
    7: 'Single_Variable_Calculus_Change__Accumulation__and_Approximation/chapters/ch07-optimization.tex',
    8: 'Single_Variable_Calculus_Change__Accumulation__and_Approximation/chapters/ch08-integral-accumulation.tex',
    9: 'Single_Variable_Calculus_Change__Accumulation__and_Approximation/chapters/ch09-fundamental-theorem.tex',
    10: 'Single_Variable_Calculus_Change__Accumulation__and_Approximation/chapters/ch10-what-integrals-measure.tex',
    11: 'Single_Variable_Calculus_Change__Accumulation__and_Approximation/chapters/ch11-techniques-integration.tex'
}

def clean_tex(text):
    text = re.sub(r'\\begin\{tikzpicture\}[\s\S]*?\\end\{tikzpicture\}', '', text)
    text = re.sub(r'\\begin\{array\}[\s\S]*?\\end\{array\}', '', text)
    text = re.sub(r'\\begin\{tabular\}[\s\S]*?\\end\{tabular\}', '', text)
    text = re.sub(r'%.*', '', text)
    words = re.findall(r'\b[A-Za-z0-9_]+\b', text)
    return words

def clean_xml(text):
    text = re.sub(r'<!--[\s\S]*?-->', '', text)
    text = re.sub(r'<latex-image>[\s\S]*?</latex-image>', '', text)
    text = re.sub(r'<[^>]+>', ' ', text)
    words = re.findall(r'\b[A-Za-z0-9_]+\b', text)
    return words

def get_tex_sections(filepath):
    with open(filepath) as f:
        content = f.read()
    sections = re.split(r'\\section\{', content)
    sec_data = []
    for s in sections[1:]:
        title = s.split('}')[0].strip()
        if 'Derivatives of trigonometric functions' in title and '\\Core' in s[:len(title)+10]:
            continue
        body = s[len(title)+1:]
        words = clean_tex(body)
        sec_data.append((title, len(words), body))
    return sec_data

def get_xml_words(filepath):
    if not os.path.exists(filepath):
        return 0
    with open(filepath) as f:
        content = f.read()
    return len(clean_xml(content))

for ch, l_path in latex_files.items():
    print(f"\n==================== CHAPTER {ch} ====================")
    tex_secs = get_tex_sections(l_path)
    ch_prefix = f"ch0{ch}" if ch < 10 else f"ch{ch}"
    ch_dirs = [d for d in os.listdir('source/chapters') if d.startswith(ch_prefix)]
    if not ch_dirs:
        continue
    sec_dir = os.path.join('source/chapters', ch_dirs[0], 'sections')
    xml_files = sorted([f for f in os.listdir(sec_dir) if f.endswith('.xml')])
    for idx, (t_title, t_count, _) in enumerate(tex_secs):
        x_file = xml_files[idx] if idx < len(xml_files) else 'MISSING'
        x_count = get_xml_words(os.path.join(sec_dir, x_file)) if x_file != 'MISSING' else 0
        ratio = (x_count / t_count * 100) if t_count > 0 else 0
        status = "OK (Verbatim)" if ratio >= 80 else "CONDENSED / SHORT"
        print(f"§{ch}.{idx+1} {t_title[:38]:<38} | TeX: {t_count:5d}w | XML: {x_count:5d}w | {ratio:5.1f}% | {status}")
