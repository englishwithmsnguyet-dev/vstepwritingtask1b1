# -*- coding: utf-8 -*-
with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/pure_extra_logic.js", "r", encoding="utf-8") as f:
    js_code = f.read()

idx_render = js_code.find("function renderExtraPracticePanel(typeId) {")
idx_diagnose = js_code.find("// --- Comprehensive Diagnostic Rules Engine ---")

new_render_func = """function renderExtraPracticePanel(typeId) {
    const container = document.getElementById('extraPracticePanel');
    if (!container) return;

    const data = extraPracticeData[typeId];
    if (!data) {
        container.innerHTML = `
            <div class="content-block" style="text-align: center; padding: 40px 20px;">
                <i class="fa-solid fa-clock" style="font-size: 42px; color: var(--primary-light); margin-bottom: 16px;"></i>
                <h3 style="font-size: 18px; margin-bottom: 8px;">Đang cập nhật đề luyện tập thêm cho dạng thư này</h3>
                <p style="color: var(--text-muted);">Vui lòng chọn <strong>Dạng 01: Letter of Advice (Thư khuyên bảo)</strong> để làm bài luyện tập.</p>
            </div>
        `;
        return;
    }

    let hintsHtml = data.hints.map(hint => {
        let itemsHtml = hint.items.map(item => `
            <div style="margin-bottom: 14px; padding-left: 6px;">
                <p style="margin-bottom: 2px;">• <strong>${item.en}</strong> (${item.vi})</p>
                <p style="margin-bottom: 2px; color: var(--primary-color); padding-left: 16px;">➔ <em>${item.reasonEn}</em></p>
                <p style="margin-bottom: 0; color: var(--text-muted); font-size: 14px; padding-left: 16px;">(${item.reasonVi})</p>
            </div>
        `).join('');

        return `
            <div class="outline-step" style="margin-bottom: 16px;">
                <h4 style="margin-bottom: 12px; color: var(--accent-red); font-size: 17px;">${hint.title}</h4>
                ${itemsHtml}
            </div>
        `;
    }).join('');

    container.innerHTML = `
        <!-- Prompt Card (Using standard website style) -->
        <div class="sample-prompt-container">
            <div class="sample-prompt-header">
                <i class="fa-solid fa-file-circle-question"></i> ĐỀ BÀI (TOPIC PROMPT)
            </div>
            <div class="sample-prompt-text">
                <p>You have received a letter from a friend, <strong>Emily</strong>. She is going to visit Can Tho in December. Write a letter to give her some suggestions. You should tell her:</p>
                <ul>
                    <li>Where to stay</li>
                    <li>What dishes to try</li>
                    <li>Which tourist attractions to visit</li>
                    <li>What to wear</li>
                </ul>
                <p style="margin-top: 10px; font-style: italic; color: var(--text-muted);">
                    <i class="fa-solid fa-triangle-exclamation" style="color: #f59e0b;"></i> You should write at least 120 words. Do not include your name. Your response will be evaluated in terms of Task Fulfillment, Organization, Vocabulary, and Grammar.
                </p>
            </div>
        </div>

        <!-- Suggestions Collapsible Accordion (Bấm vào mới hiện) -->
        <div class="content-block" style="margin-top: 25px;">
            <div class="outline-step" style="cursor: pointer; display: flex; justify-content: space-between; align-items: center; padding: 18px 22px; transition: all 0.2s ease;" onclick="toggleExtraHints()">
                <h4 style="margin: 0; color: var(--accent-red); font-size: 17px; display: flex; align-items: center; gap: 10px;">
                    <i class="fa-solid fa-lightbulb" style="color: #f59e0b;"></i> GỢI Ý Ý TƯỞNG (BẤM ĐỂ XEM/ẨN GỢI Ý)
                </h4>
                <i class="fa-solid fa-chevron-down" id="extraHintsChevron" style="color: var(--primary-color); font-size: 16px; transition: transform 0.25s ease;"></i>
            </div>
            <div id="extraHintsContent" class="hidden" style="margin-top: 14px;">
                ${hintsHtml}
            </div>
        </div>

        <!-- Student Writing Area (Using standard editor style) -->
        <div class="content-block" style="margin-top: 25px;">
            <h3><i class="fa-solid fa-pen-nib"></i> BÀI LÀM CỦA HỌC VIÊN</h3>
            <div class="editor-area">
                <div class="editor-header">
                    <span>Nhập bài viết tại đây (Yêu cầu ≥ 120 từ):</span>
                    <div class="word-count" id="extraLiveWordCount">Số từ: <strong>0</strong></div>
                </div>
                <textarea id="extraWritingArea" placeholder="Dear Emily,&#10;&#10;Thanks for your letter. I hope you are doing well..." rows="12"></textarea>
                <div class="editor-actions">
                    <button class="btn btn-secondary" onclick="resetExtraPracticeArea()"><i class="fa-solid fa-rotate-left"></i> Viết lại</button>
                    <button class="btn btn-primary" onclick="gradeExtraPractice('${typeId}')"><i class="fa-solid fa-circle-check"></i> Nộp bài & Chấm điểm VSTEP (30%)</button>
                </div>
            </div>
        </div>

        <!-- Evaluation Results Area -->
        <div class="content-block hidden" id="extraResultCard" style="margin-top: 30px;">
            <!-- Filled on submission -->
        </div>
    `;

    const writingArea = document.getElementById('extraWritingArea');
    if (writingArea) {
        writingArea.addEventListener('input', updateExtraWordCount);
    }
}

function toggleExtraHints() {
    const content = document.getElementById('extraHintsContent');
    const chevron = document.getElementById('extraHintsChevron');
    if (!content || !chevron) return;
    content.classList.toggle('hidden');
    chevron.classList.toggle('fa-chevron-up');
    chevron.classList.toggle('fa-chevron-down');
}

function updateExtraWordCount() {
    const writingArea = document.getElementById('extraWritingArea');
    const display = document.getElementById('extraLiveWordCount');
    if (!writingArea || !display) return;
    const text = writingArea.value.trim();
    const count = text === '' ? 0 : text.split(/\\s+/).length;
    display.innerHTML = `Số từ: <strong>${count}</strong>`;
    if (count >= 120) {
        display.classList.add('success');
    } else {
        display.classList.remove('success');
    }
}

function resetExtraPracticeArea() {
    const writingArea = document.getElementById('extraWritingArea');
    const resultCard = document.getElementById('extraResultCard');
    if (!writingArea) return;
    if (confirm('Bạn có chắc muốn xóa bài làm hiện tại để viết lại không?')) {
        writingArea.value = '';
        updateExtraWordCount();
        if (resultCard) resultCard.classList.add('hidden');
        writingArea.focus();
    }
}
"""

js_code = js_code[:idx_render] + new_render_func.strip() + "\n\n" + js_code[idx_diagnose:]

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/pure_extra_logic.js", "w", encoding="utf-8") as f:
    f.write(js_code)

print("Updated pure_extra_logic.js with clickable accordion hints!")
