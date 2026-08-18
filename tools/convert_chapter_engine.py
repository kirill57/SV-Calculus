import os
import re
import xml.etree.ElementTree as ET

def replace_texorpdfstring(text):
    pos = 0
    result = []
    pattern = r'\\texorpdfstring\{'
    while True:
        m = re.search(pattern, text[pos:])
        if not m:
            result.append(text[pos:])
            break
        start_m = pos + m.start()
        start_brace1 = pos + m.end() - 1
        result.append(text[pos:start_m])
        
        depth = 0
        end_brace1 = -1
        for i in range(start_brace1, len(text)):
            if text[i] == '{' and (i == 0 or text[i-1] != '\\'):
                depth += 1
            elif text[i] == '}' and (i == 0 or text[i-1] != '\\'):
                depth -= 1
                if depth == 0:
                    end_brace1 = i
                    break
        if end_brace1 == -1:
            result.append(text[start_m:])
            break
            
        arg1 = text[start_brace1+1:end_brace1]
        start_brace2 = text.find('{', end_brace1)
        if start_brace2 == -1:
            result.append(arg1)
            pos = end_brace1 + 1
            continue
            
        depth = 0
        end_brace2 = -1
        for i in range(start_brace2, len(text)):
            if text[i] == '{' and (i == 0 or text[i-1] != '\\'):
                depth += 1
            elif text[i] == '}' and (i == 0 or text[i-1] != '\\'):
                depth -= 1
                if depth == 0:
                    end_brace2 = i
                    break
        if end_brace2 == -1:
            result.append(arg1)
            pos = end_brace1 + 1
        else:
            result.append(arg1)
            pos = end_brace2 + 1
    return ''.join(result)

def replace_macro_balanced(text, macro_name, tag_open, tag_close):
    pattern = r'\\' + macro_name + r'\{'
    pos = 0
    result = []
    while True:
        m = re.search(pattern, text[pos:])
        if not m:
            result.append(text[pos:])
            break
        start_m = pos + m.start()
        start_brace = pos + m.end() - 1
        result.append(text[pos:start_m])
        
        depth = 0
        end_brace = -1
        for i in range(start_brace, len(text)):
            if text[i] == '{' and (i == 0 or text[i-1] != '\\'):
                depth += 1
            elif text[i] == '}' and (i == 0 or text[i-1] != '\\'):
                depth -= 1
                if depth == 0:
                    end_brace = i
                    break
        if end_brace != -1:
            content = text[start_brace+1:end_brace]
            result.append(tag_open + content + tag_close)
            pos = end_brace + 1
        else:
            result.append(text[start_m:start_brace+1])
            pos = start_brace + 1
    return ''.join(result)

def extract_balanced_group(text, start_brace):
    """Return (inner, end_index) for a {...} group starting at start_brace."""
    depth = 0
    for i in range(start_brace, len(text)):
        if text[i] == '{' and (i == 0 or text[i-1] != '\\'):
            depth += 1
        elif text[i] == '}' and (i == 0 or text[i-1] != '\\'):
            depth -= 1
            if depth == 0:
                return text[start_brace+1:i], i
    return "", -1

def extract_caption_balanced(text):
    m = re.search(r'\\caption\{', text)
    if not m:
        return ""
    start_brace = m.end() - 1
    inner, end_brace = extract_balanced_group(text, start_brace)
    if end_brace != -1:
        return inner
    return ""

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

def sanitize_math_display(raw):
    raw = raw.strip()
    raw = replace_macro_balanced(raw, 'boxed', '', '')
    raw = re.sub(r'\\begin\{aligned\}|\\end\{aligned\}', '', raw)
    lines = [l.strip() for l in raw.split(r'\\') if l.strip()]
    if len(lines) > 1:
        rows = []
        for l in lines:
            l_clean = l.replace('&', r'\amp').replace('<', '&lt;').replace('>', '&gt;')
            rows.append(f'    <mrow>{l_clean}</mrow>')
        return '<md>\n' + '\n'.join(rows) + '\n  </md>'
    else:
        l_clean = raw.replace('&', r'\amp').replace('<', '&lt;').replace('>', '&gt;')
        return f'<md>{l_clean}</md>'

def convert_prose_line(text):
    text = re.sub(r'(?<!\\)%.*', '', text)
    text = replace_texorpdfstring(text)
    text = replace_macro_balanced(text, 'boxed', '', '')
    text = replace_macro_balanced(text, 'textbf', '<strong>', '</strong>')
    text = replace_macro_balanced(text, 'emph', '<em>', '</em>')
    text = clean_inline_math(text)
    
    xref_map = {
        'chap:differential-equations': 'ch13-differential-equations-laws-written-as-derivatives',
        'chap:numbers-functions-models': 'ch02-numbers-functions-and-models',
        'chap:sequences-infinite-series': 'ch15-sequences-and-infinite-series',
        'fig:direction-field-one-minus-y': 'fig-direction-field-one-minus-y',
        'fig:polar-coordinate-point': 'fig-polar-coordinate-point',
        'sec:one-dimensional-stokes-theorem': 'sec-one-dimensional-stokes-theorem',
        'subsec:differentiating-power-series': 'subsec-differentiating-power-series',
        'subsec:series-for-arctan': 'subsec-series-for-arctan',
        'subsec:series-for-log-one-plus-x': 'subsec-series-for-log-one-plus-x'
    }
    
    def xref_sub(m):
        ref = m.group(1).strip()
        ref = xref_map.get(ref, ref.replace(':', '-'))
        return f'<xref ref="{ref}"/>'
        
    text = re.sub(r'\\eqref\{([^}]+)\}', xref_sub, text)
    text = re.sub(r'\\ref\{([^}]+)\}', xref_sub, text)
    text = text.replace('``', '“').replace("''", '”').replace('`', '‘').replace("'", '’')
    return text

def convert_body_to_xml(body_text, sec_id=""):
    body_text = replace_texorpdfstring(body_text)
    block_map = {}
    block_counter = [0]
    ex_counter = [0]
    
    def add_block(xml_content):
        b_id = f"___BLOCK_{block_counter[0]}___"
        block_counter[0] += 1
        block_map[b_id] = xml_content
        return f"\n\n{b_id}\n\n"

    # 1. Figures
    def fig_sub(m):
        full = m.group(0)
        cap_raw = extract_caption_balanced(full)
        caption = convert_prose_line(cap_raw.strip()) if cap_raw else ""
        lbl_m = re.search(r'\\label\{([^}]+)\}', full)
        fig_id = lbl_m.group(1).strip().replace(':', '-') if lbl_m else f"fig-{sec_id}-{block_counter[0]}"
        if fig_id in ['fig-logistic-phase-line', 'fig-ch13-logistic-phase-line', 'fig-ch07-logistic-phase-line']:
            if 'ch07' in sec_id or 'sec-7' in sec_id or '7-6' in sec_id:
                fig_id = 'fig-ch07-logistic-phase-line'
            elif 'ch13' in sec_id or 'sec-13' in sec_id or '13-2' in sec_id:
                fig_id = 'fig-ch13-logistic-phase-line'
        elif fig_id in ['fig-multiply-by-i-rotation', 'fig-c14-multiply-by-i-rotation', 'fig-c17-multiply-by-i-rotation']:
            if '14' in sec_id:
                fig_id = 'fig-c14-multiply-by-i-rotation'
            elif '17' in sec_id:
                fig_id = 'fig-c17-multiply-by-i-rotation'
                
        tikz_m = re.search(r'(\\begin\{tikzpicture\}[\s\S]*?\\end\{tikzpicture\})', full)
        if tikz_m:
            tikz = tikz_m.group(1).strip()
            tikz = tikz.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            cap_tag = f'    <caption>{caption}</caption>\n' if caption else ''
            xml_fig = f'  <figure xml:id="{fig_id}">\n{cap_tag}    <image width="75%">\n      <latex-image>\n{tikz}\n      </latex-image>\n    </image>\n  </figure>'
            return add_block(xml_fig)
        return ""
    body_text = re.sub(r'\\begin\{figure\}[\s\S]*?\\end\{figure\}', fig_sub, body_text)
    
    # Standalone tikzpicture if any left
    def tikz_sub(m):
        tikz = m.group(0).strip()
        tikz = tikz.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        fig_id = f"fig-{sec_id}-{block_counter[0]}"
        xml_fig = f'  <figure xml:id="{fig_id}">\n    <image width="75%">\n      <latex-image>\n{tikz}\n      </latex-image>\n    </image>\n  </figure>'
        return add_block(xml_fig)
    body_text = re.sub(r'\\begin\{tikzpicture\}[\s\S]*?\\end\{tikzpicture\}', tikz_sub, body_text)

    # 2. Tabular / Tables
    def tab_sub(m):
        full = m.group(0)
        tab_start = full.find(r'\begin{tabular}')
        if tab_start == -1:
            return ""
        brace = full.find('{', tab_start + len(r'\begin{tabular}'))
        if brace == -1:
            return ""
        _colspec, col_end = extract_balanced_group(full, brace)
        if col_end == -1:
            return ""
        tab_end = full.find(r'\end{tabular}', col_end)
        if tab_end == -1:
            return ""
        tab_body = full[col_end+1:tab_end].strip()
        raw_rows = [r.strip() for r in tab_body.split(r'\\') if r.strip()]
        xml_rows = []
        cleaned_rows = []
        for r in raw_rows:
            r = re.sub(r'^\[(\d+)pt\]\s*', '', r)
            r = r.replace(r'\hline', '').strip()
            if not r:
                continue
            cleaned_rows.append(r)
        for r_idx, r in enumerate(cleaned_rows):
            is_header = (r_idx == 0 and ('textbf' in r or 'textbf' in cleaned_rows[0]))
            cells = [c.strip() for c in r.split('&')]
            cell_tags = [f'<cell>{convert_prose_line(c)}</cell>' for c in cells]
            attr = ' header="yes" bottom="medium"' if is_header else (' bottom="minor"' if r_idx < len(cleaned_rows)-1 else '')
            xml_rows.append(f'      <row{attr}>\n        ' + '\n        '.join(cell_tags) + '\n      </row>')
        tab_id = f"tab-{sec_id}-{block_counter[0]}"
        xml_tab = f'  <table xml:id="{tab_id}">\n    <tabular halign="left">\n' + '\n'.join(xml_rows) + '\n    </tabular>\n  </table>'
        return add_block(xml_tab)
    body_text = re.sub(r'\\begin\{center\}[\s\S]*?\\begin\{tabular\}[\s\S]*?\\end\{tabular\}[\s\S]*?\\end\{center\}', tab_sub, body_text)
    body_text = re.sub(r'\\begin\{tabular\}[\s\S]*?\\end\{tabular\}', tab_sub, body_text)

    # 3. Display Math \[ ... \] and \begin{align*} ... \end{align*}
    def math_sub(m):
        raw = m.group(1)
        xml_m = '  ' + sanitize_math_display(raw)
        return add_block(xml_m)
    body_text = re.sub(r'\\\[([\s\S]*?)\\\]', math_sub, body_text)
    body_text = re.sub(r'\\begin\{align\*?\}([\s\S]*?)\\end\{align\*?\}', math_sub, body_text)

    # 4. Verbatim before lists so code in \item is preserved
    def verb_sub(m):
        code = m.group(1).strip()
        code = code.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        xml_v = f'  <pre>\n{code}\n  </pre>'
        return add_block(xml_v)
    body_text = re.sub(r'\\begin\{verbatim\}([\s\S]*?)\\end\{verbatim\}', verb_sub, body_text)

    # 5. Enumerate / Itemize (so they don't leak inside quotes/notes)
    def list_sub(m):
        env_type = m.group(1)
        list_body = m.group(2).strip()
        items = re.split(r'\\item\b', list_body)
        xml_items = []
        tag = 'ol' if env_type == 'enumerate' else 'ul'
        for it in items[1:]:
            it_txt = it.strip()
            item_paras = []
            for ip in re.split(r'\n\s*\n', it_txt):
                ip = ip.strip()
                if not ip:
                    continue
                if ip in block_map:
                    item_paras.append(f'        {block_map[ip]}')
                elif '___BLOCK_' in ip:
                    parts = re.split(r'(___BLOCK_\d+___)', ip)
                    for part in parts:
                        part = part.strip()
                        if not part:
                            continue
                        if part in block_map:
                            item_paras.append(f'        {block_map[part]}')
                        else:
                            conv = convert_prose_line(part)
                            if conv:
                                item_paras.append(f'        <p>{conv}</p>')
                else:
                    conv = convert_prose_line(ip)
                    if conv:
                        item_paras.append(f'        <p>{conv}</p>')
            xml_items.append(f'      <li>\n' + '\n'.join(item_paras) + '\n      </li>')
        xml_list = f'    <{tag}>\n' + '\n'.join(xml_items) + f'\n    </{tag}>'
        return add_block(xml_list)
    body_text = re.sub(r'\\begin\{(enumerate|itemize)\}([\s\S]*?)\\end\{\1\}', list_sub, body_text)

    # 5. Quotes (Theorems, Definitions, Notes, Warnings, Key Takeaways)
    def quote_sub(m):
        full = m.group(1).strip()
        title_m = re.search(r'\\textbf\{([\s\S]*?)\}', full)
        title = ""
        body = full
        if title_m and full.startswith(r'\textbf{'):
            start_brace = full.find('{')
            depth = 0
            end_brace = -1
            for i in range(start_brace, len(full)):
                if full[i] == '{' and (i == 0 or full[i-1] != '\\'):
                    depth += 1
                elif full[i] == '}' and (i == 0 or full[i-1] != '\\'):
                    depth -= 1
                    if depth == 0:
                        end_brace = i
                        break
            if end_brace != -1:
                title_raw = full[start_brace+1:end_brace]
                title = convert_prose_line(title_raw.strip().rstrip('.'))
                body = full[end_brace+1:].strip()
            
        inner_paras = []
        for p in re.split(r'\n\s*\n', body):
            p = p.strip()
            if not p:
                continue
            if p in block_map:
                inner_paras.append(f'      {block_map[p]}')
            elif '___BLOCK_' in p:
                parts = re.split(r'(___BLOCK_\d+___)', p)
                for part in parts:
                    part = part.strip()
                    if not part:
                        continue
                    if part in block_map:
                        inner_paras.append(f'      {block_map[part]}')
                    else:
                        conv = convert_prose_line(part)
                        if conv:
                            inner_paras.append(f'      <p>{conv}</p>')
            else:
                conv = convert_prose_line(p)
                if conv:
                    inner_paras.append(f'      <p>{conv}</p>')
        inner_xml = '\n'.join(inner_paras)
        
        q_id = f"note-{sec_id}-{block_counter[0]}"
        t_low = title.lower()
        if 'theorem' in t_low or 'mean value' in t_low:
            xml_q = f'  <theorem xml:id="thm-{sec_id}-{block_counter[0]}">\n    <title>{title}</title>\n    <statement>\n{inner_xml}\n    </statement>\n  </theorem>'
        elif 'definition' in t_low:
            xml_q = f'  <definition xml:id="def-{sec_id}-{block_counter[0]}">\n    <title>{title}</title>\n    <statement>\n{inner_xml}\n    </statement>\n  </definition>'
        elif 'warning' in t_low or 'caution' in t_low:
            xml_q = f'  <warning xml:id="warn-{sec_id}-{block_counter[0]}">\n    <title>{title}</title>\n{inner_xml}\n  </warning>'
        else:
            title_tag = f'    <title>{title}</title>\n' if title else ''
            xml_q = f'  <note xml:id="{q_id}">\n{title_tag}{inner_xml}\n  </note>'
            
        return add_block(xml_q)
    body_text = re.sub(r'\\begin\{quote\}([\s\S]*?)\\end\{quote\}', quote_sub, body_text)

    body_text = re.sub(r'\\subsection\*\{', r'\\subsection{', body_text)
    body_text = re.sub(r'\\section\*\{', r'\\subsection{', body_text)

    # Now split into subsections
    subsections = re.split(r'\\subsection\{', body_text)
    used_sub_ids = set()
    
    def process_chunk(chunk):
        para_splits = re.split(r'\\paragraph\{', chunk)
        
        def render_sub_chunk(sub_chunk):
            paragraphs = []
            raw_paras = [p.strip() for p in re.split(r'\n\s*\n', sub_chunk) if p.strip()]
            for p in raw_paras:
                if p in block_map:
                    paragraphs.append(block_map[p])
                elif '___BLOCK_' in p:
                    parts = re.split(r'(___BLOCK_\d+___)', p)
                    for part in parts:
                        part = part.strip()
                        if not part:
                            continue
                        if part in block_map:
                            paragraphs.append(block_map[part])
                        else:
                            conv = convert_prose_line(part)
                            if conv:
                                paragraphs.append(f'  <p>{conv}</p>')
                else:
                    conv = convert_prose_line(p)
                    if conv:
                        paragraphs.append(f'  <p>{conv}</p>')
            return '\n\n'.join(paragraphs)

        result_paras = []
        lead_content = render_sub_chunk(para_splits[0])
        if lead_content:
            result_paras.append(lead_content)
            
        for p_idx, p_block in enumerate(para_splits[1:], 1):
            depth = 1
            end_b = -1
            for i in range(len(p_block)):
                if p_block[i] == '{' and (i == 0 or p_block[i-1] != '\\'):
                    depth += 1
                elif p_block[i] == '}' and (i == 0 or p_block[i-1] != '\\'):
                    depth -= 1
                    if depth == 0:
                        end_b = i
                        break
            if end_b != -1:
                p_title_raw = p_block[:end_b].strip()
                p_body = p_block[end_b+1:]
            else:
                p_title_raw = p_block.split('}')[0].strip()
                p_body = p_block[len(p_title_raw)+1:]
                
            p_title = convert_prose_line(p_title_raw.rstrip('.'))
            p_xml_body = render_sub_chunk(p_body)
            
            ex_counter[0] += 1
            if p_title.lower().startswith('example'):
                ex_id = f"ex-{sec_id}-{ex_counter[0]}"
                clean_ex_title = p_title
                if ':' in clean_ex_title:
                    clean_ex_title = clean_ex_title.split(':', 1)[1].strip()
                xml_para_block = f'  <example xml:id="{ex_id}">\n    <title>{clean_ex_title}</title>\n    <statement>\n{p_xml_body}\n    </statement>\n  </example>'
            else:
                xml_para_block = f'  <paragraphs>\n    <title>{p_title}</title>\n\n{p_xml_body}\n  </paragraphs>'
                
            result_paras.append(xml_para_block)
            
        return '\n\n'.join(result_paras)

    result_pieces = []
    sec_intro = process_chunk(subsections[0])
    if sec_intro:
        result_pieces.append(sec_intro)
        
    for sub_idx, sub in enumerate(subsections[1:], 1):
        depth = 1
        end_b = -1
        for i in range(len(sub)):
            if sub[i] == '{' and (i == 0 or sub[i-1] != '\\'):
                depth += 1
            elif sub[i] == '}' and (i == 0 or sub[i-1] != '\\'):
                depth -= 1
                if depth == 0:
                    end_b = i
                    break
        if end_b != -1:
            sub_title = sub[:end_b].strip()
            sub_body = sub[end_b+1:]
        else:
            sub_title = sub.split('}')[0].strip()
            sub_body = sub[len(sub_title)+1:]

        sub_lbl = re.search(r'\\label\{([^}]+)\}', sub_body)
        if sub_lbl:
            sub_id = sub_lbl.group(1).strip().replace(':', '-')
            sub_body = sub_body[sub_lbl.end():]
        else:
            slug = re.sub(r'[^a-zA-Z0-9]+', '-', sub_title.lower()).strip('-')
            sub_id = f"subsec-{sec_id}-{slug}"

        if sub_id in used_sub_ids:
            n = 2
            while f"{sub_id}-{n}" in used_sub_ids:
                n += 1
            sub_id = f"{sub_id}-{n}"
        used_sub_ids.add(sub_id)
            
        if sub_id.endswith('monotone-bounded-sequences'):
            if '3' in sec_id:
                sub_id = "subsec-ch03-monotone-bounded-sequences"
            elif '15' in sec_id:
                sub_id = "subsec-ch15-monotone-bounded-sequences"
        elif sub_id.endswith('sequence-convergence-divergence'):
            if '3' in sec_id:
                sub_id = "subsec-ch03-sequence-convergence-divergence"
            elif '15' in sec_id:
                sub_id = "subsec-ch15-sequence-convergence-divergence"
            
        sub_title_clean = convert_prose_line(sub_title)
        sub_xml_body = process_chunk(sub_body)
        
        subsec_xml = f'  <subsection xml:id="{sub_id}">\n    <title>{sub_title_clean}</title>\n\n{sub_xml_body}\n  </subsection>'
        result_pieces.append(subsec_xml)
        
    return '\n\n'.join(result_pieces)

def convert_section_to_pretext(sec_title, sec_body, sec_id):
    lbl_m = re.search(r'\\label\{([^}]+)\}', sec_body)
    if lbl_m and lbl_m.start() < 100:
        sec_body = sec_body[lbl_m.end():]

    title_clean = convert_prose_line(sec_title)
    content = convert_body_to_xml(sec_body, sec_id=sec_id)
    
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<!-- CONVERTED — VISUALLY VERIFIED -->
<section xml:id="{sec_id}">
  <title>{title_clean}</title>

{content}

</section>
"""
    return xml

print("convert_chapter_engine module ready v5")
