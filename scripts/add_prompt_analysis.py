# -*- coding: utf-8 -*-
with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/pure_extra_logic.js", "r", encoding="utf-8") as f:
    js_code = f.read()

idx_prompt_end = js_code.find("</p>\n            </div>\n        </div>")

analysis_grid_html = """
                <div class="sample-analysis-grid">
                    <div class="sample-analysis-item">
                        <strong>Người nhận</strong>
                        <span>Emily (Bạn bè)</span>
                    </div>
                    <div class="sample-analysis-item">
                        <strong>Mục đích</strong>
                        <span>Gợi ý cho chuyến du lịch Cần Thơ vào tháng 12</span>
                    </div>
                    <div class="sample-analysis-item">
                        <strong>Văn phong</strong>
                        <span>Thân mật (Informal Letter)</span>
                    </div>
                    <div class="sample-analysis-item">
                        <strong>Yêu cầu cốt lõi</strong>
                        <span>Nơi ở, món ăn, điểm tham quan, trang phục</span>
                    </div>
                </div>"""

if "sample-analysis-grid" not in js_code:
    js_code = js_code.replace(
        "            </div>\n        </div>\n\n        <!-- Suggestions Collapsible Accordion",
        f"            </div>{analysis_grid_html}\n        </div>\n\n        <!-- Suggestions Collapsible Accordion"
    )

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/pure_extra_logic.js", "w", encoding="utf-8") as f:
    f.write(js_code)

print("Added sample-analysis-grid to extra practice prompt!")
