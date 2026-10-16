# -*- coding: utf-8 -*-
with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace regex that broke
old_regex = "const rTransitionNoComma = /(^|[.\n])\\s*(Firstly|Secondly|Finally|Moreover|Besides|Furthermore|In addition|Therefore|For example)\\s+([a-zA-Z])/gi;"

new_regex = "const rTransitionNoComma = new RegExp('(^|[\\\\.\\\\n])\\\\s*(Firstly|Secondly|Finally|Moreover|Besides|Furthermore|In addition|Therefore|For example)\\\\s+([a-zA-Z])', 'gi');"

content = content.replace(old_regex, new_regex)

# Check any other broken regex
import re
content = re.sub(r'const rTransitionNoComma = /\(\^\|\[\..*?\/gi;', new_regex, content, flags=re.DOTALL)

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed regex constructors!")
