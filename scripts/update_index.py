import json
import re

# 1. Update index.html
index_html_path = "/Users/nguyetpham/Desktop/WEBSITE/writing-letters-b1level/index.html"
with open(index_html_path, "r", encoding="utf-8") as f:
    index_content = f.read()

# Add tab button if not present
if 'data-tab="extraPractice"' not in index_content:
    old_tab_str = '<button class="tab-btn practice-tab" data-tab="writingPractice">\n                            <i class="fa-solid fa-graduation-cap"></i> TRẢ BÀI\n                        </button>'
    new_tab_str = '<button class="tab-btn practice-tab" data-tab="writingPractice">\n                            <i class="fa-solid fa-graduation-cap"></i> TRẢ BÀI\n                        </button>\n                        <button class="tab-btn extra-practice-tab" data-tab="extraPractice">\n                            <i class="fa-solid fa-pen-nib"></i> BÀI LUYỆN TẬP THÊM\n                        </button>'
    index_content = index_content.replace(old_tab_str, new_tab_str)

# Add panel container if not present
if 'id="extraPracticePanel"' not in index_content:
    old_panel_str = '                    <div class="tab-panel" id="writingPracticePanel">\n'
    new_panel_str = '                    <div class="tab-panel" id="extraPracticePanel">\n                        <!-- Filled by JS -->\n                    </div>\n\n                    <div class="tab-panel" id="writingPracticePanel">\n'
    index_content = index_content.replace(old_panel_str, new_panel_str)

with open(index_html_path, "w", encoding="utf-8") as f:
    f.write(index_content)

print("Updated index.html successfully!")
