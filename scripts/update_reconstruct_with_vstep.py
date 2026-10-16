# -*- coding: utf-8 -*-
with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/full_extra_logic.js", "r", encoding="utf-8") as f:
    new_extra_js = f.read()

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "r", encoding="utf-8") as f:
    app_py = f.read()

# Replace from "// --- Extra Practice Data & Logic ---" up to "function selectLetterType(id) {"
start_marker = "// --- Extra Practice Data & Logic ---"
end_marker = "function selectLetterType(id) {"

start_idx = app_py.find(start_marker)
end_idx = app_py.find(end_marker)

if start_idx == -1 or end_idx == -1:
    # Try alternative search
    start_marker = "const extraPracticeData ="
    start_idx = app_py.find(start_marker)

if start_idx != -1 and end_idx != -1:
    app_py = app_py[:start_idx] + new_extra_js + "\n\n" + app_py[end_idx:]
else:
    raise Exception(f"Markers not found: start={start_idx}, end={end_idx}")

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "w", encoding="utf-8") as f:
    f.write(app_py)

print("Updated reconstruct_app.py with new VSTEP logic successfully!")
