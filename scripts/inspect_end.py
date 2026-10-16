with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("Total lines:", len(lines))
for i in range(max(0, len(lines)-30), len(lines)):
    print(f"{i+1}: {repr(lines[i])}")
