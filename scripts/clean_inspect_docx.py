import zipfile
import xml.etree.ElementTree as ET
import os

materials_dir = "/Users/nguyetpham/Desktop/WEBSITE/writing-letters-b1level/materials"

def extract_docx_text(docx_path):
    with zipfile.ZipFile(docx_path) as z:
        xml_content = z.read('word/document.xml')
        tree = ET.fromstring(xml_content)
        paragraphs = []
        for p in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
            texts = [node.text for node in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if node.text]
            t = ''.join(texts).strip()
            if t:
                paragraphs.append(t)
        return '\n'.join(paragraphs)

files = sorted([f for f in os.listdir(materials_dir) if f.endswith('.docx')])

for f in files:
    path = os.path.join(materials_dir, f)
    text = extract_docx_text(path)
    print("############################################################")
    print("### FILE:", f)
    print("############################################################")
    print(text)
    print("\n")
