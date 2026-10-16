import zipfile
import xml.etree.ElementTree as ET
import os

materials_dir = "/Users/nguyetpham/Desktop/WEBSITE/writing-letters-b1level/materials"

def extract_docx_text(docx_path):
    try:
        with zipfile.ZipFile(docx_path) as z:
            xml_content = z.read('word/document.xml')
            tree = ET.fromstring(xml_content)
            paragraphs = []
            for p in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
                texts = [node.text for node in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if node.text]
                if texts:
                    paragraphs.append(''.join(texts))
                else:
                    paragraphs.append('')
            return '\n'.join(paragraphs)
    except Exception as e:
        return f"Error reading {docx_path}: {e}"

files = sorted([f for f in os.listdir(materials_dir) if f.endswith('.docx')])

for f in files:
    path = os.path.join(materials_dir, f)
    print("="*60)
    print("FILE:", f)
    print("="*60)
    text = extract_docx_text(path)
    print(text)
    print("\n\n")
