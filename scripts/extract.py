import os
import zipfile
import re
import json
import xml.etree.ElementTree as ET

materials_dir = "/Users/nguyetpham/Desktop/WEBSITE/writing-letters/materials"
output_file = "/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/extracted_text.json"

results = {}

for filename in sorted(os.listdir(materials_dir)):
    if filename.endswith(".docx") and not filename.startswith("~$"):
        path = os.path.join(materials_dir, filename)
        try:
            docx = zipfile.ZipFile(path)
            xml_content = docx.read('word/document.xml')
            root = ET.fromstring(xml_content)
            
            # Extract text
            text_nodes = root.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
            text = ''.join([node.text for node in text_nodes if node.text])
            
            # Clean underscores
            cleaned = re.sub(r'_{3,}', '\n', text)
            
            results[filename] = cleaned
            print(f"Extracted {filename}, length: {len(cleaned)}")
        except Exception as e:
            print(f"Error extracting {filename}: {e}")

# Ensure scratch directory exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print("Done!")
