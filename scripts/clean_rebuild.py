with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace any data.sampleModel.split(...) or data.sampleModel.replace(...) with formatLetterParagraphs(data.sampleModel)
content = content.replace("${data.sampleModel.split('\n\n').join('<br><br>')}", "${formatLetterParagraphs(data.sampleModel)}")
content = content.replace("${data.sampleModelVi.split('\n\n').join('<br><br>')}", "${formatLetterParagraphs(data.sampleModelVi)}")

# Also add formatLetterParagraphs function definition if not present
if "function formatLetterParagraphs(" not in content:
    func_def = """
function formatLetterParagraphs(str) {
    if (!str) return '';
    return str.split('\\n\\n').join('<br><br>');
}
"""
    content = content.replace("function gradeExtraPractice(", func_def + "\nfunction gradeExtraPractice(")

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Saved clean rebuild!")
