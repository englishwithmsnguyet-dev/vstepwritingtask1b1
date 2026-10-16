with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "r", encoding="utf-8") as f:
    app_py = f.read()

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/extra_practice_block.js", "r", encoding="utf-8") as f:
    extra_block = f.read()

# Check if extra_practice_block is already in app_py
if "const extraPracticeData =" not in app_py:
    # Insert extra_block before "function selectLetterType"
    target = "function selectLetterType(id) {"
    idx = app_py.find(target)
    if idx == -1:
        raise Exception("Could not find selectLetterType")
    
    app_py = app_py[:idx] + extra_block + "\n\n" + app_py[idx:]

# In selectLetterType, ensure renderExtraPracticePanel(id) is called
target_render = "if (sampleWritingPanel) sampleWritingPanel.innerHTML = typeData.sampleWriting;"
if "renderExtraPracticePanel(id);" not in app_py:
    app_py = app_py.replace(target_render, target_render + "\n\n    // Render Extra Practice\n    renderExtraPracticePanel(id);")

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "w", encoding="utf-8") as f:
    f.write(app_py)

print("Injected Extra Practice into reconstruct_app.py successfully!")
