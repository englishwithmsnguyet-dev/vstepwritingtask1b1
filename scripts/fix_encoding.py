# -*- coding: utf-8 -*-
with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/generate_vstep_grading.py", "r", encoding="utf-8") as f:
    code = f.read()

if not code.startswith("# -*- coding: utf-8 -*-"):
    code = "# -*- coding: utf-8 -*-\n" + code

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/generate_vstep_grading.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Added encoding header!")
