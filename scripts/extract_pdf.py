import os
import json
from pypdf import PdfReader

materials_dir = "/Users/nguyetpham/Desktop/WEBSITE/writing-letters/materials"
output_file = "/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/extracted_pdf_text.json"

results = {}

for filename in sorted(os.listdir(materials_dir)):
    if filename.endswith(".pdf"):
        path = os.path.join(materials_dir, filename)
        try:
            reader = PdfReader(path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            
            results[filename] = text
            print(f"Extracted {filename}, length: {len(text)}")
        except Exception as e:
            print(f"Error extracting {filename}: {e}")

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print("Done!")
