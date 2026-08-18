import os
import glob
import re

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

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as fp:
        txt = fp.read()
    orig = txt
    
    # Normalize unicode curly primes in math tags
    def fix_math_primes(m_match):
        tag = m_match.group(1)
        body = m_match.group(2).replace('\u2019', "'").replace('\u2018', "'")
        return f"<{tag}>{body}</{tag}>"
    txt = re.sub(r'<(m|me|md|mrow)>([\s\S]*?)</\1>', fix_math_primes, txt)
    
    # 2. General prose formatting macros (outside code blocks)
    # Protect latex-image and asymptote blocks
    protected_blocks = []
    def save_block(m):
        idx = len(protected_blocks)
        protected_blocks.append(m.group(0))
        return f"___PROTECTED_{idx}___"
        
    txt = re.sub(r'<latex-image>[\s\S]*?</latex-image>', save_block, txt)
    txt = re.sub(r'<asymptote>[\s\S]*?</asymptote>', save_block, txt)
    
    # Replace macros
    txt = replace_macro_balanced(txt, 'textbf', '<strong>', '</strong>')
    txt = replace_macro_balanced(txt, 'emph', '<em>', '</em>')
    txt = replace_macro_balanced(txt, 'boxed', '', '')
    txt = replace_macro_balanced(txt, 'sectag', '', '')
    txt = replace_macro_balanced(txt, 'marginnote', '', '')
    txt = replace_macro_balanced(txt, 'margintip', '', '')
    txt = re.sub(r'\\noindent\b', '', txt)
    txt = re.sub(r'\\clearpage\b', '', txt)
    txt = re.sub(r'\\newpage\b', '', txt)
    txt = re.sub(r'\\item\b', '', txt)
    
    # Restore protected blocks
    for idx, block in enumerate(protected_blocks):
        txt = txt.replace(f"___PROTECTED_{idx}___", block)
        
    if txt != orig:
        with open(filepath, 'w', encoding='utf-8') as fp:
            fp.write(txt)
        return True
    return False

modified_count = 0
for f in sorted(glob.glob('source/**/*.xml', recursive=True) + glob.glob('source/**/*.ptx', recursive=True)):
    if clean_file(f):
        print(f"Cleaned macros in: {f}")
        modified_count += 1

print(f"Finished. Cleaned {modified_count} files.")
