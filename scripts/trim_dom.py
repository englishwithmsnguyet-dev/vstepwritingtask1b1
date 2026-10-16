# -*- coding: utf-8 -*-
with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/dom_logic_full.js", "r", encoding="utf-8") as f:
    dom_logic = f.read()

# Remove any trailing python code
end_idx = dom_logic.rfind("});")
if end_idx != -1:
    dom_logic = dom_logic[:end_idx + 3]

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/dom_logic_full.js", "w", encoding="utf-8") as f:
    f.write(dom_logic)

print("Trimmed dom_logic_full.js!")
