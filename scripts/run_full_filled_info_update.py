# -*- coding: utf-8 -*-
"""
Full update:
1. Update generate_enhanced_sample_writings.py with CLEAN_FILLED_LETTERS
2. Update style.css: text-indent: 0 !important, styling for .sample-filled-info
3. Run apply_enhanced_sample_writings.py
4. Run assemble_complete_working_app.py
5. Bump version to v=46.0 in index.html
"""
import re
import subprocess

gen_path = "/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/generate_enhanced_sample_writings.py"
filled_path = "/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/update_filled_info_clean_view.py"

with open(filled_path, "r", encoding="utf-8") as f:
    filled_code = f.read()

idx_dict_start = filled_code.find("CLEAN_FILLED_LETTERS = {")
if idx_dict_start == -1:
    raise Exception("Could not find CLEAN_FILLED_LETTERS")

dict_code = filled_code[idx_dict_start:].strip()

with open(gen_path, "r", encoding="utf-8") as f:
    gen_code = f.read()

# Insert CLEAN_FILLED_LETTERS before generate_sample_html
if "CLEAN_FILLED_LETTERS = {" not in gen_code:
    idx_def = gen_code.find("def generate_sample_html(")
    gen_code = gen_code[:idx_def] + dict_code + "\n\n" + gen_code[idx_def:]

# Now replace View 2 building block inside generate_sample_html
idx_v2_start = gen_code.find("    # Build View 2: Clean Letter View")
idx_v3_start = gen_code.find("    # Build View 3: Bilingual View")

if idx_v2_start != -1 and idx_v3_start != -1:
    new_v2_block = """    # Build View 2: Clean Letter View (Full Letter with filled-in information highlighted)
    clean_en_content = CLEAN_FILLED_LETTERS[type_id]["en"]
    clean_vi_content = CLEAN_FILLED_LETTERS[type_id]["vi"]

    clean_html = f'''
        <div id="sampleViewClean" class="sample-view-content" style="display: none;">
            <!-- Header for English Clean Letter -->
            <div class="clean-view-header" style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; flex-wrap: wrap; gap: 10px;">
                <div style="font-size: 15px; font-weight: 700; color: var(--primary-color); display: flex; align-items: center; gap: 8px;">
                    <i class="fa-solid fa-envelope-open-text"></i> TOÀN VĂN LÁ THƯ TIẾNG ANH (BẢN CHUẨN THI - THÔNG TIN THẾ VÀO ĐƯỢC LÀM NỔI BẬT)
                </div>
                <button class="btn-sample-audio" onclick="playCurrentSampleLetter()" title="Nghe đọc toàn bộ bức thư này" style="padding: 6px 14px; font-size: 12.5px;">
                    <i class="fa-solid fa-volume-high"></i> Nghe đọc bản này
                </button>
            </div>

            <!-- Authentic Stationery Box (Clean English Letter) -->
            <div class="sample-letter-box">
                {clean_en_content}
            </div>

            <!-- Header for Vietnamese Clean Translation -->
            <div class="clean-view-header" style="display: flex; align-items: center; justify-content: space-between; margin-top: 28px; margin-bottom: 12px;">
                <div style="font-size: 15px; font-weight: 700; color: #059669; display: flex; align-items: center; gap: 8px;">
                    <i class="fa-solid fa-language"></i> BẢN DỊCH TIẾNG VIỆT HOÀN CHỈNH (THÔNG TIN THẾ VÀO ĐƯỢC LÀM NỔI BẬT)
                </div>
            </div>

            <!-- Clean Translation Box (Clean Vietnamese Letter) -->
            <div class="translation-box" style="background-color: var(--bg-card); border: 1px solid var(--border-color); padding: 25px 32px; border-radius: 12px; font-family: var(--font-body); line-height: 1.85; color: var(--text-main); box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03);">
                {clean_vi_content}
            </div>
        </div>
    '''
\n"""
    gen_code = gen_code[:idx_v2_start] + new_v2_block + gen_code[idx_v3_start:]
    print("Replaced View 2 block in generate_enhanced_sample_writings.py!")
else:
    raise Exception("Could not find View 2 block indices in generate_enhanced_sample_writings.py")

with open(gen_path, "w", encoding="utf-8") as f:
    f.write(gen_code)

print("Updated generate_enhanced_sample_writings.py successfully!")

# 2. Update style.css
css_path = "/Users/nguyetpham/Desktop/WEBSITE/writing-letters-b1level/style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

# Replace text-indent in .sample-letter-box p
css_content = re.sub(
    r'\.sample-letter-box p\s*\{[^}]*text-indent:\s*24px;[^}]*\}',
    '''.sample-letter-box p {
    margin: 0 0 16px 0;
    text-indent: 0 !important;
}''',
    css_content
)

# Also ensure any .translation-box p has text-indent: 0 !important;
if ".translation-box p {" not in css_content:
    css_content += """
.translation-box p {
    text-indent: 0 !important;
}
"""

# Add .sample-filled-info styles
filled_info_css = """
/* Highlight for Filled-in Information (Thông tin đã thế vào) */
.sample-filled-info {
    color: #1d4ed8;
    font-weight: 700;
    background-color: rgba(219, 234, 254, 0.6);
    padding: 1px 6px;
    border-radius: 4px;
    border-bottom: 2px solid #3b82f6;
    display: inline;
}

[data-theme="dark"] .sample-filled-info {
    color: #93c5fd;
    background-color: rgba(59, 130, 246, 0.25);
    border-bottom-color: #60a5fa;
}
"""

if ".sample-filled-info {" not in css_content:
    css_content += "\n" + filled_info_css.strip() + "\n"
else:
    # replace existing
    css_content = re.sub(
        r'/\* Highlight for Filled-in Information.*?\n\[data-theme="dark"\] \.sample-filled-info \{[^}]*\}',
        filled_info_css.strip(),
        css_content,
        flags=re.DOTALL
    )

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css_content)

print("Updated style.css successfully!")
