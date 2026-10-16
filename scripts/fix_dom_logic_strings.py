with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the formatLetterParagraphs function with String.fromCharCode
content = content.replace("return str.split('\n\n').join('<br><br>');", "const doubleNl = String.fromCharCode(10) + String.fromCharCode(10);\n    return str.split(doubleNl).join('<br><br>');")

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated formatLetterParagraphs in reconstruct_app.py")
