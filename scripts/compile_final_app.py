# -*- coding: utf-8 -*-
with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/pure_extra_logic.js", "r", encoding="utf-8") as f:
    pure_extra_code = f.read()

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "r", encoding="utf-8") as f:
    app_py = f.read()

# Replace between the start of extra practice and selectLetterType
start_marker = "// ==========================================================================\n// VSTEP TASK 1 EXTRA PRACTICE"
end_marker = "function selectLetterType(id) {"

start_idx = app_py.find(start_marker)
end_idx = app_py.find(end_marker)

if start_idx == -1:
    # Look for const extraPracticeData =
    start_marker = "const extraPracticeData ="
    start_idx = app_py.find(start_marker)

if start_idx != -1 and end_idx != -1:
    app_py = app_py[:start_idx] + pure_extra_code.strip() + "\n\n\n" + app_py[end_idx:]
else:
    raise Exception(f"Markers not found! start={start_idx}, end={end_idx}")

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "w", encoding="utf-8") as f:
    f.write(app_py)

print("Updated reconstruct_app.py with pure_extra_code!")
