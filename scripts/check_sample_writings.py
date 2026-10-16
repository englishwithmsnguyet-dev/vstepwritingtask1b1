import re

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "r", encoding="utf-8") as f:
    content = f.read()

# Let's find each letterType object
types = re.findall(r'id:\s*[\'"]([^\'"]+)[\'"].*?sampleWriting:\s*`([^`]+)`', content, re.DOTALL)
for t_id, sw in types:
    print("="*60)
    print("TYPE ID:", t_id)
    print("="*60)
    print(sw[:500])
    print("...\n")
