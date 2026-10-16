# -*- coding: utf-8 -*-
"""
Updates generate_enhanced_sample_writings.py to include a dedicated, complete,
unannotated letter view (BẢN ĐẦY ĐỦ KHÔNG CHÚ THÍCH) with unified body paragraph
and complete unannotated Vietnamese translation.
"""

file_path = "/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/generate_enhanced_sample_writings.py"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the beginning of annotated_html to include the quick banner
old_ann_start = """    # Build View 1: Annotated Structure
    annotated_html = f'''
        <div id="sampleViewAnnotated" class="sample-view-content active">
            <!-- Filter Bar -->"""

new_ann_start = """    # Build View 1: Annotated Structure
    annotated_html = f'''
        <div id="sampleViewAnnotated" class="sample-view-content active">
            <!-- Quick Link to Clean Letter -->
            <div class="clean-letter-quick-banner" style="background: var(--bg-card); border: 1px dashed var(--primary-color); border-radius: 10px; padding: 12px 18px; margin-bottom: 16px; display: flex; align-items: center; justify-content: space-between; gap: 12px; flex-wrap: wrap;">
                <div style="font-size: 13.5px; font-weight: 600; color: var(--text-main);">
                    <i class="fa-solid fa-book-open-reader" style="color: var(--primary-color); margin-right: 6px;"></i> Bạn muốn đọc hoặc học thuộc trọn vẹn bức thư liền mạch không chú thích?
                </div>
                <button type="button" class="btn btn-outline" onclick="switchSampleView('sampleViewClean', document.querySelector('[data-view=\\'sampleViewClean\\']'))" style="font-size: 12.5px; padding: 6px 14px; border-radius: 6px; cursor: pointer; border-color: var(--primary-color); color: var(--primary-color); font-weight: 600;">
                    <i class="fa-solid fa-file-lines"></i> Mở Bản Đầy Đủ Không Chú Thích <i class="fa-solid fa-arrow-right"></i>
                </button>
            </div>

            <!-- Filter Bar -->"""

if old_ann_start in content:
    content = content.replace(old_ann_start, new_ann_start)
    print("Replaced annotated_html start with quick banner!")
else:
    print("Warning: old_ann_start not found.")

# Replace Build View 2: Clean Letter View
idx_v2 = content.find("    # Build View 2: Clean Letter View")
idx_v3 = content.find("    # Build View 3: Bilingual View")

if idx_v2 != -1 and idx_v3 != -1:
    new_v2_code = """    # Build View 2: Clean Letter View (Full Letter without annotations)
    if type_id == "application":
        clean_body_en = "".join([f"<p>{p['en']}</p>" for p in data["points"]])
        clean_body_vi = "".join([f"<p style=\\\"margin: 0 0 14px 0; text-indent: 20px;\\\">{p['vi']}</p>" for p in data["points"]])
    else:
        clean_body_en = f"<p>{' '.join([p['en'] for p in data['points']])}</p>"
        clean_body_vi = f"<p style=\\\"margin: 0 0 14px 0; text-indent: 20px;\\\">{' '.join([p['vi'] for p in data['points']])}</p>"

    clean_html = f'''
        <div id="sampleViewClean" class="sample-view-content" style="display: none;">
            <!-- Header for English Clean Letter -->
            <div class="clean-view-header" style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; flex-wrap: wrap; gap: 10px;">
                <div style="font-size: 15px; font-weight: 700; color: var(--primary-color); display: flex; align-items: center; gap: 8px;">
                    <i class="fa-solid fa-envelope-open-text"></i> TOÀN VĂN LÁ THƯ TIẾNG ANH (BẢN CHUẨN THI - KHÔNG CHÚ THÍCH)
                </div>
                <button class="btn-sample-audio" onclick="playCurrentSampleLetter()" title="Nghe đọc toàn bộ bức thư này" style="padding: 6px 14px; font-size: 12.5px;">
                    <i class="fa-solid fa-volume-high"></i> Nghe đọc bản này
                </button>
            </div>

            <!-- Authentic Stationery Box (Clean English Letter) -->
            <div class="sample-letter-box">
                <strong>{data['salutation']['en']}</strong>
                <p>{data['opening']['en']}</p>
                {clean_body_en}
                <p>{data['closing']['en']}</p>
                <strong>{data['signoff']['en']}</strong>
            </div>

            <!-- Header for Vietnamese Clean Translation -->
            <div class="clean-view-header" style="display: flex; align-items: center; justify-content: space-between; margin-top: 28px; margin-bottom: 12px;">
                <div style="font-size: 15px; font-weight: 700; color: #059669; display: flex; align-items: center; gap: 8px;">
                    <i class="fa-solid fa-language"></i> BẢN DỊCH TIẾNG VIỆT HOÀN CHỈNH (ĐẦY ĐỦ KHÔNG CHÚ THÍCH)
                </div>
            </div>

            <!-- Clean Translation Box (Clean Vietnamese Letter) -->
            <div class="translation-box" style="background-color: var(--bg-card); border: 1px solid var(--border-color); padding: 25px 32px; border-radius: 12px; font-family: var(--font-body); line-height: 1.85; color: var(--text-main); box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03);">
                <strong style="color: var(--text-main); display: block; margin-bottom: 14px;">{data['salutation']['vi']}</strong>
                <p style="margin: 0 0 14px 0; text-indent: 20px;">{data['opening']['vi']}</p>
                {clean_body_vi}
                <p style="margin: 0 0 14px 0; text-indent: 20px;">{data['closing']['vi']}</p>
                <strong style="color: var(--text-main); display: block; margin-top: 14px;">{data['signoff']['vi']}</strong>
            </div>
        </div>
    '''
\n"""
    content = content[:idx_v2] + new_v2_code + content[idx_v3:]
    print("Replaced clean_html view successfully!")
else:
    print("Warning: could not find View 2 indices.")

# Replace Tab Button labels
old_tab_clean = """                <button class="sample-view-tab-btn" data-view="sampleViewClean" onclick="switchSampleView('sampleViewClean', this)">
                    <i class="fa-solid fa-envelope"></i> ✉️ Bức thư chuẩn
                </button>"""

new_tab_clean = """                <button class="sample-view-tab-btn" data-view="sampleViewClean" onclick="switchSampleView('sampleViewClean', this)">
                    <i class="fa-solid fa-file-lines"></i> 📄 Toàn văn lá thư đầy đủ (Không chú thích)
                </button>"""

if old_tab_clean in content:
    content = content.replace(old_tab_clean, new_tab_clean)
    print("Updated tab button label to 'Toàn văn lá thư đầy đủ (Không chú thích)'!")
else:
    print("Warning: old_tab_clean not found.")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated generate_enhanced_sample_writings.py successfully!")
