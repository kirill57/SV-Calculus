import os
import re
import xml.etree.ElementTree as ET

def clean_inline_math(text):
    def repl_paren(m):
        content = m.group(1).strip()
        content = content.replace('&', r'\amp').replace('<', '&lt;').replace('>', '&gt;')
        return f'<m>{content}</m>'
    text = re.sub(r'\\\(([\s\S]*?)\\\)', repl_paren, text)
    def repl_dollar(m):
        content = m.group(1).strip()
        content = content.replace('&', r'\amp').replace('<', '&lt;').replace('>', '&gt;')
        return f'<m>{content}</m>'
    text = re.sub(r'(?<!\\)\$([^\$]+?)\$', repl_dollar, text)
    return text

def clean_display_math(raw):
    raw = raw.strip()
    if raw.startswith(r'\boxed{') and raw.endswith('}'):
        raw = raw[7:-1].strip()
    # Check if lines exist
    lines = [l.strip() for l in raw.split(r'\\') if l.strip()]
    if len(lines) > 1:
        clean_lines = []
        for l in lines:
            l_clean = l.replace('&', r'\amp').replace('<', '&lt;').replace('>', '&gt;')
            clean_lines.append(f'    <mrow>{l_clean}</mrow>')
        return '<md>\n' + '\n'.join(clean_lines) + '\n  </md>'
    else:
        l_clean = raw.replace('&', r'\amp').replace('<', '&lt;').replace('>', '&gt;')
        return f'<md>{l_clean}</md>'

def convert_latex_prose(text):
    text = re.sub(r'%.*', '', text)
    text = clean_inline_math(text)
    text = re.sub(r'\\emph\{([\s\S]*?)\}', r'<em>\1</em>', text)
    text = re.sub(r'\\textbf\{([\s\S]*?)\}', r'<strong>\1</strong>', text)
    text = re.sub(r'\\eqref\{([^}]+)\}', r'<xref ref="\1"/>', text)
    text = re.sub(r'\\ref\{([^}]+)\}', r'<xref ref="\1"/>', text)
    text = text.replace('``', '“').replace("''", '”').replace('`', '‘').replace("'", '’')
    text = text.replace('&', '&amp;')
    # restore XML entities that might have been double escaped
    text = text.replace('&amp;lt;', '&lt;').replace('&amp;gt;', '&gt;').replace('&amp;amp;', '&amp;')
    return text

def convert_tabular_block(table_match):
    body = table_match.group(0)
    tab_m = re.search(r'\\begin\{tabular\}\{([^}]+)\}([\s\S]*?)\\end\{tabular\}', body)
    if not tab_m:
        return ""
    col_spec = tab_m.group(1).strip()
    tab_body = tab_m.group(2).strip()
    
    raw_rows = [r.strip() for r in tab_body.split(r'\\') if r.strip()]
    xml_rows = []
    
    for idx, r in enumerate(raw_rows):
        is_header = False
        if r.endswith(r'\hline'):
            r = r[:-6].strip()
            if idx == 0:
                is_header = True
        elif r.startswith(r'\hline'):
            r = r[6:].strip()
            
        cells = [c.strip() for c in r.split('&')]
        cell_tags = []
        for c in cells:
            c_conv = convert_latex_prose(c)
            cell_tags.append(f'<cell>{c_conv}</cell>')
        
        attr = ' header="yes" bottom="medium"' if is_header else (' bottom="minor"' if idx < len(raw_rows)-1 and not is_header else '')
        row_str = f'      <row{attr}>\n        ' + '\n        '.join(cell_tags) + '\n      </row>'
        xml_rows.append(row_str)
        
    res = '  <table>\n    <tabular halign="left">\n' + '\n'.join(xml_rows) + '\n    </tabular>\n  </table>'
    return res

def convert_figure_block(fig_match):
    body = fig_match.group(0)
    cap_m = re.search(r'\\caption\{([\s\S]*?)\}', body)
    caption = convert_latex_prose(cap_m.group(1).strip()) if cap_m else ""
    
    lbl_m = re.search(r'\\label\{([^}]+)\}', body)
    fig_id = lbl_m.group(1).strip().replace(':', '-') if lbl_m else "fig-diagram"
    
    tikz_m = re.search(r'(\\begin\{tikzpicture\}[\s\S]*?\\end\{tikzpicture\})', body)
    if tikz_m:
        tikz = tikz_m.group(1).strip()
        tikz = tikz.replace('->', '-&gt;').replace('<-', '&lt;-').replace('>=', '&gt;=').replace('<=', '&lt;=')
        cap_tag = f'    <caption>{caption}</caption>\n' if caption else ''
        return f'  <figure xml:id="{fig_id}">\n{cap_tag}    <image width="75%">\n      <latex-image>\n{tikz}\n      </latex-image>\n    </image>\n  </figure>'
    return ""

print("convert_sections library loaded")
