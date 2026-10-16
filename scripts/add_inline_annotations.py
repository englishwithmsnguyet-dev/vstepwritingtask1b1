# -*- coding: utf-8 -*-
with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/pure_extra_logic.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# Let's write the annotated essay generator function:
annotated_generator_func = """
function buildAnnotatedEssayHtml(rawText, errors) {
    if (!rawText) return '';
    let annotated = rawText;

    // Sort errors by wrong text length descending to avoid partial nested replacements
    const sortedErrors = [...errors].sort((a, b) => (b.wrong ? b.wrong.length : 0) - (a.wrong ? a.wrong.length : 0));

    // Replace each error in text
    sortedErrors.forEach(err => {
        if (!err.wrong || err.wrong.length < 2) return;
        // Escape regex special chars
        const escaped = err.wrong.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&');
        const reg = new RegExp(escaped, 'gi');
        annotated = annotated.replace(reg, `<span class="annotated-box"><del class="annotated-wrong">${err.wrong}</del> <ins class="annotated-correct"><i class="fa-solid fa-arrow-right"></i> ${err.correct}</ins></span>`);
    });

    // Format paragraphs
    const paras = annotated.split(/\\n+/).filter(p => p.trim() !== '');
    return paras.map(p => `<p class="annotated-para">${p.trim()}</p>`).join('');
}
"""

# Let's inspect where gradeExtraPractice builds the result HTML
idx_grade = js_code.find("function gradeExtraPractice(typeId) {")
idx_results_html = js_code.find("// Build Error Table HTML", idx_grade)

# Replace from // Build Error Table HTML to end of gradeExtraPractice
new_grade_tail = """    const data = extraPracticeData[typeId];

    // Build Inline Annotated Essay HTML
    const annotatedEssayHtml = buildAnnotatedEssayHtml(rawText, errors);

    // Build Error Table HTML
    let errorTableHtml = '';
    if (errors.length > 0) {
        let rowsHtml = errors.map((err, idx) => `
            <tr>
                <td style="font-weight: 700; color: var(--primary-color); text-align: center;">${idx + 1}</td>
                <td><span class="err-badge-type">${err.type}</span></td>
                <td><span class="err-text-wrong">${err.wrong}</span></td>
                <td><span class="err-text-correct"><i class="fa-solid fa-arrow-right"></i> ${err.correct}</span></td>
                <td style="font-size: 13px; color: var(--text-main); line-height: 1.5;">${err.reason}</td>
            </tr>
        `).join('');

        errorTableHtml = `
            <div class="extra-error-table-wrapper">
                <div class="error-table-title">
                    <i class="fa-solid fa-triangle-exclamation" style="color: #ef4444;"></i>
                    DANH SÁCH ${errors.length} LỖI CẦN SỬA CHI TIẾT (NGỮ PHÁP, MẠO TỪ, TỪ LOẠI, DÙNG TỪ, CHÍNH TẢ):
                </div>
                <div class="table-responsive">
                    <table class="error-table">
                        <thead>
                            <tr>
                                <th style="width: 40px; text-align: center;">#</th>
                                <th style="width: 170px;">Phân loại lỗi</th>
                                <th style="width: 190px;">Học viên viết</th>
                                <th style="width: 220px;">Đề xuất sửa đúng</th>
                                <th>Giải thích ngữ pháp chi tiết</th>
                            </tr>
                        </thead>
                        <tbody>
                            ${rowsHtml}
                        </tbody>
                    </table>
                </div>
            </div>
        `;
    } else {
        errorTableHtml = `
            <div class="extra-feedback-box" style="background: rgba(16, 185, 129, 0.08); border-color: rgba(16, 185, 129, 0.3); margin-top: 20px;">
                <div class="feedback-title" style="color: #059669;">
                    <i class="fa-solid fa-circle-check"></i> Không phát hiện lỗi ngữ pháp hay từ vựng đáng kể nào!
                </div>
                <p style="margin: 0; font-size: 14px; color: var(--text-main);">Bài làm của bạn rất chuẩn chỉnh, mạch lạc và tự nhiên.</p>
            </div>
        `;
    }

    // Build Results HTML
    resultCard.innerHTML = `
        <div class="extra-score-banner">
            <div class="score-main-group">
                <div class="score-circle-badge">${convertedScore.toFixed(2)} <span style="font-size: 13px; display: block; font-weight: 500; opacity: 0.9;">/ 3.00</span></div>
                <div class="score-text-info">
                    <h4>${vstepLevel} • ${convertedScore.toFixed(2)} / 3.00 ĐIỂM (30% TỔNG BÀI THI WRITING)</h4>
                    <p>Tương đương <strong>Band ${overallBand.toFixed(1)} / 10</strong> theo khung chấm Task 1 VSTEP. (Độ dài: <strong>${wordCount} từ</strong> - ${levelDesc})</p>
                </div>
            </div>
            <div class="extra-b1-badge" style="background: #ffffff; color: var(--primary-color);">
                TASK 1 = 30% ĐIỂM WRITING
            </div>
        </div>

        <!-- 4 Criteria Grid based on VSTEP SCORING GUIDE (Converted to 0.75 pts each) -->
        <div class="criteria-grid">
            <div class="criterion-card">
                <div class="criterion-name">
                    <span>Task Fulfilment (30%)</span>
                    <span class="criterion-score">${tfConv.toFixed(2)}/0.75 <small style="font-size: 11px; font-weight: normal; color: var(--text-muted);">(${tfScore.toFixed(1)}/10)</small></span>
                </div>
                <div class="criterion-desc">
                    ${hasStay ? '✓ Nơi ở ' : '✗ Nơi ở '}| 
                    ${hasDishes ? '✓ Món ăn ' : '✗ Món ăn '}| 
                    ${hasAttractions ? '✓ Điểm tham quan ' : '✗ Điểm tham quan '}| 
                    ${hasWear ? '✓ Trang phục' : '✗ Trang phục'}.
                    Độ dài: ${wordCount >= 120 ? 'Đạt chuẩn (≥120 từ)' : 'Chưa đủ từ'}.
                </div>
            </div>
            <div class="criterion-card">
                <div class="criterion-name">
                    <span>Organization (30%)</span>
                    <span class="criterion-score">${orgConv.toFixed(2)}/0.75 <small style="font-size: 11px; font-weight: normal; color: var(--text-muted);">(${orgScore.toFixed(1)}/10)</small></span>
                </div>
                <div class="criterion-desc">
                    Bố cục 5 phần hoàn chỉnh. Sử dụng linh hoạt các liên từ nối (Firstly, Secondly, Next, Finally, Moreover, Besides).
                </div>
            </div>
            <div class="criterion-card">
                <div class="criterion-name">
                    <span>Vocabulary (30%)</span>
                    <span class="criterion-score">${vocConv.toFixed(2)}/0.75 <small style="font-size: 11px; font-weight: normal; color: var(--text-muted);">(${vocScore.toFixed(1)}/10)</small></span>
                </div>
                <div class="criterion-desc">
                    Vốn từ vựng đúng chủ đề. ${vocabErrors.length > 0 ? `Bị trừ điểm do có ${vocabErrors.length} lỗi dùng từ/từ loại chưa chuẩn.` : 'Sử dụng từ vựng chính xác.'}
                </div>
            </div>
            <div class="criterion-card">
                <div class="criterion-name">
                    <span>Grammar & Accuracy (30%)</span>
                    <span class="criterion-score">${gramConv.toFixed(2)}/0.75 <small style="font-size: 11px; font-weight: normal; color: var(--text-muted);">(${gramScore.toFixed(1)}/10)</small></span>
                </div>
                <div class="criterion-desc">
                    Áp dụng tốt cấu trúc khuyên bảo B1. ${totalGrammarCount > 0 ? `Bị trừ điểm do mắc ${totalGrammarCount} lỗi ngữ pháp/mạo từ/câu ghép.` : 'Ngữ pháp chuẩn xác.'}
                </div>
            </div>
        </div>

        <!-- Section: Bản sửa lỗi trực tiếp trên bài viết của học viên -->
        <div class="annotated-essay-card">
            <div class="annotated-essay-header">
                <i class="fa-solid fa-pen-to-square"></i> BẢN SỬA LỖI TRỰC TIẾP TRÊN BÀI VIẾT CỦA BẠN (INLINE CORRECTIONS):
            </div>
            <div class="annotated-essay-body">
                ${annotatedEssayHtml}
            </div>
        </div>

        <!-- Detailed Error Table -->
        ${errorTableHtml}

        <!-- Unlocked Sample Model Letter -->
        <div class="extra-model-wrapper">
            <div class="extra-model-title">
                <i class="fa-solid fa-award"></i> BÀI VIẾT MẪU CHUẨN B1 THAM KHẢO (MODEL LETTER)
            </div>
            <div class="extra-model-letter">
                ${formatLetterParagraphs(data.sampleModel)}
            </div>
            <div class="extra-model-trans">
                <strong>BẢN DỊCH CHI TIẾT:</strong><br><br>
                ${formatLetterParagraphs(data.sampleModelVi)}
            </div>
        </div>
    `;

    resultCard.classList.remove('hidden');
    resultCard.scrollIntoView({ behavior: 'smooth', block: 'start' });

    // Send Form Report to Teacher
    sendExtraPracticeReport(typeId, wordCount, overallBand, convertedScore, errors.length, rawText);
}
"""

idx_grade_end = js_code.find("function sendExtraPracticeReport", idx_grade)
js_code = js_code[:idx_results_html] + new_grade_tail.strip() + "\n\n" + js_code[idx_grade_end:]

# Insert annotated_generator_func before gradeExtraPractice
js_code = js_code[:idx_grade] + annotated_generator_func.strip() + "\n\n" + js_code[idx_grade:]

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/pure_extra_logic.js", "w", encoding="utf-8") as f:
    f.write(js_code)

print("Updated pure_extra_logic.js with inline annotated essay & error breakdown!")
