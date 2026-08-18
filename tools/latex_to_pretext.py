import os
import re
import xml.etree.ElementTree as ET

def sanitize_math(math_str):
    # inside <m> or <md>, XML entities &lt; and &gt; are needed, and & in alignments must be \amp
    math_str = math_str.replace('&', r'\amp')
    math_str = math_str.replace('<', '&lt;')
    math_str = math_str.replace('>', '&gt;')
    # remove \boxed{...} if it wraps the whole display
    math_str = re.sub(r'\\boxed\{([\s\S]*)\}', r'\1', math_str.strip())
    return math_str

def convert_inline_math(text):
    def repl_paren(m):
        content = sanitize_math(m.group(1))
        return f'<m>{content}</m>'
    text = re.sub(r'\\\(([\s\S]*?)\\\)', repl_paren, text)
    def repl_dollar(m):
        content = sanitize_math(m.group(1))
        return f'<m>{content}</m>'
    text = re.sub(r'(?<!\\)\$([^\$]+?)\$', repl_dollar, text)
    return text

def convert_display_math(text):
    def repl_bracket(m):
        raw = m.group(1).strip()
        # handle boxed inside
        if raw.startswith(r'\boxed{') and raw.endswith('}'):
            raw = raw[7:-1].strip()
        lines = [l.strip() for l in raw.split(r'\\') if l.strip()]
        if len(lines) > 1:
            rows = '\n'.join([f'    <mrow>{sanitize_math(l)}</mrow>' for l in lines])
            return f'\n  <md>\n{rows}\n  </md>\n'
        else:
            return f'\n  <md>{sanitize_math(raw)}</md>\n'
            
    text = re.sub(r'\\\[([\s\S]*?)\\\]', repl_bracket, text)
    
    def repl_align(m):
        raw = m.group(1).strip()
        lines = [l.strip() for l in raw.split(r'\\') if l.strip()]
        rows = '\n'.join([f'    <mrow>{sanitize_math(l)}</mrow>' for l in lines])
        return f'\n  <md>\n{rows}\n  </md>\n'
        
    text = re.sub(r'\\begin\{align\*?\}([\s\S]*?)\\end\{align\*?\}', repl_align, text)
    return text

print("latex_to_pretext engine module loaded")
