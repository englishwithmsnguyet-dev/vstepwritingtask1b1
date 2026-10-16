# -*- coding: utf-8 -*-
"""
Applies enhanced sample writings to reconstruct_app.py and reassembles app.js.
"""
import sys
import os
import json

sys.path.insert(0, "/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch")
from generate_enhanced_sample_writings import SAMPLE_DATA, generate_sample_html

rec_path = "/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py"

with open(rec_path, "r", encoding="utf-8") as f:
    rec_code = f.read()

idx_types = rec_code.find("letter_types = [")
idx_types_end = rec_code.find("js_array_code = ")

if idx_types == -1 or idx_types_end == -1:
    raise Exception("Could not find letter_types in reconstruct_app.py")

exec(rec_code[idx_types:idx_types_end])

print(f"Loaded {len(letter_types)} letter types.")

for t in letter_types:
    tid = t["id"]
    if tid in SAMPLE_DATA:
        old_sw = t["sampleWriting"]
        # extract prompt container
        p_start = old_sw.find("<div class=\"sample-prompt-container\">")
        p_end = old_sw.find("<div class=\"content-block\">")
        if p_start != -1 and p_end != -1:
            prompt_html = old_sw[p_start:p_end].strip()
        else:
            # fallback
            prompt_html = f'''
            <div class="sample-prompt-container">
                <div class="sample-prompt-header">
                    <i class="fa-solid fa-file-circle-question"></i> ĐỀ BÀI (TOPIC PROMPT)
                </div>
                <div class="sample-prompt-text">
                    <p>{t.get("practicePrompt", "")}</p>
                </div>
            </div>
            '''.strip()

        new_html = generate_sample_html(tid, SAMPLE_DATA[tid], prompt_html)
        t["sampleWriting"] = new_html
        print(f"Successfully generated enhanced sample writing for: {tid}")
    else:
        print(f"Warning: No sample data for {tid}")

# Now serialize letter_types back into python code representation
new_letter_types_py = "letter_types = [\n"
for t in letter_types:
    new_letter_types_py += "    {\n"
    for k, v in t.items():
        val_repr = json.dumps(v, ensure_ascii=False)
        new_letter_types_py += f"        {json.dumps(k)}: {val_repr},\n"
    new_letter_types_py += "    },\n"
new_letter_types_py += "]\n\n"

new_rec_code = rec_code[:idx_types] + new_letter_types_py + rec_code[idx_types_end:]

with open(rec_path, "w", encoding="utf-8") as f:
    f.write(new_rec_code)

print("Updated reconstruct_app.py successfully!")
