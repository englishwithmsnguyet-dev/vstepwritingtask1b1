# -*- coding: utf-8 -*-
import re

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace broken regex
clean_line = r"const rTransitionNoComma = /(^|[.!?])\s*(Firstly|Secondly|Finally|Moreover|Besides|Furthermore|In addition|Therefore|For example)\s+([a-zA-Z])/gi;"

content = re.sub(r'const rTransitionNoComma = .*?;', lambda m: clean_line, content, flags=re.DOTALL)

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Clean regex fix applied!")
