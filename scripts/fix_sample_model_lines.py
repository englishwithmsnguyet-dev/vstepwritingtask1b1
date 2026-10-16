with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("${data.sampleModel.split('\\n\\n').join('<br><br>')}", "${formatLetterParagraphs(data.sampleModel)}")
content = content.replace("${data.sampleModelVi.split('\\n\\n').join('<br><br>')}", "${formatLetterParagraphs(data.sampleModelVi)}")
content = content.replace("${data.sampleModel.split('\n\n').join('<br><br>')}", "${formatLetterParagraphs(data.sampleModel)}")
content = content.replace("${data.sampleModelVi.split('\n\n').join('<br><br>')}", "${formatLetterParagraphs(data.sampleModelVi)}")

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated reconstruct_app.py!")
