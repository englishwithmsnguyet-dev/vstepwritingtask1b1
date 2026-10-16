import re

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace any broken replace(/\n\n/g, '<br><br>') with split('\n\n').join('<br><br>')
content = re.sub(r'\$\{data\.sampleModel\.replace\(.*?, \'<br><br>\'\)\}', "${data.sampleModel.split('\\\\n\\\\n').join('<br><br>')}", content, flags=re.DOTALL)
content = re.sub(r'\$\{data\.sampleModelVi\.replace\(.*?, \'<br><br>\'\)\}', "${data.sampleModelVi.split('\\\\n\\\\n').join('<br><br>')}", content, flags=re.DOTALL)

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed newline replacements in reconstruct_app.py")
