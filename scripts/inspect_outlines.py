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
    # Find II. DÀN Ý CHI TIẾT up to VÍ DỤ MINH HOẠ
    start = -1
    end = -1
    for i, p in enumerate(paragraphs):
        if "II. DÀN Ý CHI TIẾT" in p:
            start = i
        if "VÍ DỤ MINH HOẠ" in p:
            end = i
            break
    if start != -1 and end != -1:
        print("\n".join(paragraphs[start:end]))
    elif start != -1:
        print("\n".join(paragraphs[start:]))
    print("\n")
