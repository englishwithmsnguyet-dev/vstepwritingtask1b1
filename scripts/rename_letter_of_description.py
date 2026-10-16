# -*- coding: utf-8 -*-

# 1. Update reconstruct_app.py
reconstruct_path = "/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py"
with open(reconstruct_path, "r", encoding="utf-8") as f:
    rec_code = f.read()

rec_code = rec_code.replace('"titleEn": "Letter of Giving Information"', '"titleEn": "Letter of Description"')
with open(reconstruct_path, "w", encoding="utf-8") as f:
    f.write(rec_code)

# 2. Update pure_extra_logic.js
extra_path = "/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/pure_extra_logic.js"
with open(extra_path, "r", encoding="utf-8") as f:
    extra_code = f.read()

extra_code = extra_code.replace(
    'title: "DẠNG 03: LETTER OF GIVING INFORMATION (THƯ CUNG CẤP THÔNG TIN)"',
    'title: "DẠNG 03: LETTER OF DESCRIPTION (THƯ CUNG CẤP THÔNG TIN)"'
)
with open(extra_path, "w", encoding="utf-8") as f:
    f.write(extra_code)

print("Renamed to Letter of Description in reconstruct_app.py and pure_extra_logic.js!")
