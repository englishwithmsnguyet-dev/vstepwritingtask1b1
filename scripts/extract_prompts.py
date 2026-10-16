import zipfile
import xml.etree.ElementTree as ET
import os

materials_dir = "/Users/nguyetpham/Desktop/WEBSITE/writing-letters-b1level/materials"

def extract_docx_paragraphs(docx_path):
    with zipfile.ZipFile(docx_path) as z:
        xml_content = z.read('word/document.xml')
        tree = ET.fromstring(xml_content)
        paragraphs = []
        for p in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
            texts = [node.text for node in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if node.text]
            t = ''.join(texts).strip()
            if t and not t.startswith('______'):
                paragraphs.append(t)
        return paragraphs

files = sorted([f for f in os.listdir(materials_dir) if f.endswith('.docx')])

for f in files:
    path = os.path.join(materials_dir, f)
    paragraphs = extract_docx_paragraphs(path)
    print("="*80)
    print("FILE:", f)
    print("="*80)
    # Find VÍ DỤ MINH HOẠ
    idx = -1
    for i, p in enumerate(paragraphs):
        if "VÍ DỤ MINH HOẠ" in p:
            idx = i
            break
    if idx != -1:
        print("\n".join(paragraphs[idx:]))
    else:
        print("Not found VÍ DỤ MINH HOẠ")
    print("\n")
