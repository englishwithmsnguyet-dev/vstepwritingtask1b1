with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("studentText.replace(/\\n+/g, ' ')", "studentText.split(String.fromCharCode(10)).join(' ')")
content = content.replace("studentText.replace(/\n+/g, ' ')", "studentText.split(String.fromCharCode(10)).join(' ')")

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed report payload in reconstruct_app.py")
