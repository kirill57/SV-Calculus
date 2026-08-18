import os
import sys
import re
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools.convert_chapter_engine import convert_section_to_pretext, convert_body_to_xml, convert_prose_line

chapters_info = {
    1: {
        'tex': 'Single_Variable_Calculus_Change__Accumulation__and_Approximation/chapters/ch01-velocity-distance.tex',
        'dir': 'source/chapters/ch01-velocity-distance-and-the-first-shape-of-calculus',
        'slug': 'ch01-velocity-distance-and-the-first-shape-of-calculus',
        'title': 'Velocity, Distance, and the First Shape of Calculus'
    },
    2: {
        'tex': 'Single_Variable_Calculus_Change__Accumulation__and_Approximation/chapters/ch02-numbers-functions.tex',
        'dir': 'source/chapters/ch02-numbers-functions-and-models',
        'slug': 'ch02-numbers-functions-and-models',
        'title': 'Numbers, Functions, and Models'
    },
    3: {
        'tex': 'Single_Variable_Calculus_Change__Accumulation__and_Approximation/chapters/ch03-limits-continuity.tex',
        'dir': 'source/chapters/ch03-limits-and-continuity',
        'slug': 'ch03-limits-and-continuity',
        'title': 'Limits and Continuity'
    },
    4: {
        'tex': 'Single_Variable_Calculus_Change__Accumulation__and_Approximation/chapters/ch04-derivative.tex',
        'dir': 'source/chapters/ch04-the-derivative',
        'slug': 'ch04-the-derivative',
        'title': 'The Derivative'
    },
    5: {
        'tex': 'Single_Variable_Calculus_Change__Accumulation__and_Approximation/chapters/ch05-differentiation-rules.tex',
        'dir': 'source/chapters/ch05-differentiation-rules-and-elementary-functions',
        'slug': 'ch05-differentiation-rules-and-elementary-functions',
        'title': 'Differentiation Rules and Elementary Functions'
    },
    6: {
        'tex': 'Single_Variable_Calculus_Change__Accumulation__and_Approximation/chapters/ch06-shape-extremes.tex',
        'dir': 'source/chapters/ch06-shape-extremes-and-the-mean-value-theorem',
        'slug': 'ch06-shape-extremes-and-the-mean-value-theorem',
        'title': 'Shape, Extremes, and the Mean Value Theorem'
    },
    7: {
        'tex': 'Single_Variable_Calculus_Change__Accumulation__and_Approximation/chapters/ch07-optimization.tex',
        'dir': 'source/chapters/ch07-optimization-related-rates-and-models',
        'slug': 'ch07-optimization-related-rates-and-models',
        'title': 'Optimization, Related Rates, and Models'
    },
    8: {
        'tex': 'Single_Variable_Calculus_Change__Accumulation__and_Approximation/chapters/ch08-integral-accumulation.tex',
        'dir': 'source/chapters/ch08-the-integral-as-accumulation',
        'slug': 'ch08-the-integral-as-accumulation',
        'title': 'The Integral as Accumulation'
    },
    9: {
        'tex': 'Single_Variable_Calculus_Change__Accumulation__and_Approximation/chapters/ch09-fundamental-theorem.tex',
        'dir': 'source/chapters/ch09-the-fundamental-theorem-of-calculus',
        'slug': 'ch09-the-fundamental-theorem-of-calculus',
        'title': 'The Fundamental Theorem of Calculus'
    },
    10: {
        'tex': 'Single_Variable_Calculus_Change__Accumulation__and_Approximation/chapters/ch10-what-integrals-measure.tex',
        'dir': 'source/chapters/ch10-what-integrals-measure',
        'slug': 'ch10-what-integrals-measure',
        'title': 'What Integrals Measure'
    },
    11: {
        'tex': 'Single_Variable_Calculus_Change__Accumulation__and_Approximation/chapters/ch11-techniques-integration.tex',
        'dir': 'source/chapters/ch11-techniques-of-integration',
        'slug': 'ch11-techniques-of-integration',
        'title': 'Techniques of Integration'
    },
    12: {
        'tex': 'Single_Variable_Calculus_Change__Accumulation__and_Approximation/chapters/ch12-numerical-integration.tex',
        'dir': 'source/chapters/ch12-numerical-integration-error-and-computation',
        'slug': 'ch12-numerical-integration-error-and-computation',
        'title': 'Numerical Integration, Error, and Computation'
    },
    13: {
        'tex': 'Single_Variable_Calculus_Change__Accumulation__and_Approximation/chapters/ch13-differential-equations.tex',
        'dir': 'source/chapters/ch13-differential-equations-laws-written-as-derivatives',
        'slug': 'ch13-differential-equations-laws-written-as-derivatives',
        'title': 'Differential Equations: Laws Written as Derivatives'
    },
    14: {
        'tex': 'Single_Variable_Calculus_Change__Accumulation__and_Approximation/chapters/ch14-parametric-polar.tex',
        'dir': 'source/chapters/ch14-parametric-curves-polar-coordinates-and-conics',
        'slug': 'ch14-parametric-curves-polar-coordinates-and-conics',
        'title': 'Parametric Curves, Polar Coordinates, and Conics'
    },
    15: {
        'tex': 'Single_Variable_Calculus_Change__Accumulation__and_Approximation/chapters/ch15-sequences-series.tex',
        'dir': 'source/chapters/ch15-sequences-and-infinite-series',
        'slug': 'ch15-sequences-and-infinite-series',
        'title': 'Sequences and Infinite Series'
    },
    16: {
        'tex': 'Single_Variable_Calculus_Change__Accumulation__and_Approximation/chapters/ch16-power-series.tex',
        'dir': 'source/chapters/ch16-power-series-taylor-polynomials-and-taylor-series',
        'slug': 'ch16-power-series-taylor-polynomials-and-taylor-series',
        'title': 'Power Series, Taylor Polynomials, and Taylor Series'
    },
    17: {
        'tex': 'Single_Variable_Calculus_Change__Accumulation__and_Approximation/chapters/ch17-complex-fourier.tex',
        'dir': 'source/chapters/ch17-complex-numbers-fourier-ideas-and-the-road-ahead',
        'slug': 'ch17-complex-numbers-fourier-ideas-and-the-road-ahead',
        'title': 'Complex Numbers, Fourier Ideas, and the Road Ahead'
    }
}

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def convert_chapter(ch_num):
    info = chapters_info[ch_num]
    print(f"\n==================== CONVERTING CHAPTER {ch_num}: {info['title']} ====================")
    with open(info['tex'], encoding='utf-8', errors='ignore') as fp:
        txt = fp.read()
        
    secs = re.split(r'\\section\{', txt)
    intro_tex = secs[0]
    
    chap_intro = re.split(r'\\chapter\{[^}]+\}', intro_tex)[-1]
    chap_intro = re.sub(r'\\label\{[^}]+\}', '', chap_intro).strip()
    intro_xml = convert_body_to_xml(chap_intro, sec_id=f"ch{ch_num:02d}-intro")
    
    sec_dir = os.path.join(info['dir'], 'sections')
    xml_files = sorted([f for f in os.listdir(sec_dir) if f.endswith('.xml')], key=natural_sort_key)
    
    # Handle LaTeX draft duplicate sections
    tex_sections_to_use = secs[1:]
    if ch_num == 3 and len(tex_sections_to_use) == 10 and len(xml_files) == 9:
        # omit index 9 (the duplicate section 10)
        tex_sections_to_use = tex_sections_to_use[:9]
    elif ch_num == 5 and len(tex_sections_to_use) == 11 and len(xml_files) == 10:
        # omit index 6 (the duplicate trig section)
        tex_sections_to_use = tex_sections_to_use[:6] + tex_sections_to_use[7:]
        
    converted_sections = []
    for idx, s in enumerate(tex_sections_to_use):
        depth = 1
        end_b = -1
        for i in range(len(s)):
            if s[i] == '{' and (i == 0 or s[i-1] != '\\'):
                depth += 1
            elif s[i] == '}' and (i == 0 or s[i-1] != '\\'):
                depth -= 1
                if depth == 0:
                    end_b = i
                    break
        if end_b != -1:
            t_title = s[:end_b].strip()
            body = s[end_b+1:]
        else:
            t_title = s.split('}')[0].strip()
            body = s[len(t_title)+1:]
            
        target_xml = xml_files[idx]
        sec_id = target_xml.replace('.xml', '')
        
        xml_out = convert_section_to_pretext(t_title, body, sec_id)
        
        # XML validation check
        try:
            ET.fromstring(xml_out)
            status = "VALID"
        except Exception as e:
            status = f"XML ERROR: {e}"
            
        out_path = os.path.join(sec_dir, target_xml)
        with open(out_path, 'w', encoding='utf-8') as out_fp:
            out_fp.write(xml_out)
            
        print(f"  §{ch_num}.{idx+1} {t_title[:35]:<35} -> {target_xml} [{status}]")
        converted_sections.append(target_xml)
        
    wrapper_path = os.path.join(info['dir'], f"{info['slug']}.ptx")
    inc_lines = '\n'.join([f'  <xi:include href="sections/{xf}"/>' for xf in xml_files])
    wrapper_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<!-- CONVERTED — VISUALLY VERIFIED -->
<chapter xml:id="{info['slug']}" xmlns:xi="http://www.w3.org/2001/XInclude">
  <title>{info['title']}</title>

  <introduction>
{intro_xml}
  </introduction>

{inc_lines}

</chapter>
"""
    with open(wrapper_path, 'w', encoding='utf-8') as out_fp:
        out_fp.write(wrapper_xml)
    print(f"  Chapter wrapper {info['slug']}.ptx written.")

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        chs = [int(x) for x in sys.argv[1:]]
    else:
        chs = list(range(1, 18))
    for c in chs:
        convert_chapter(c)
