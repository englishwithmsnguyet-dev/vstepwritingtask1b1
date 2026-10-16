# -*- coding: utf-8 -*-
with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/pure_extra_logic.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# Replace scoring calculation & resultCard HTML in pure_extra_logic.js
target_find = r"""    // Total VSTEP Band
    let overallBand = (tfScore + orgScore + vocScore + gramScore) / 4.0;
    overallBand = Math.round(overallBand * 10) / 10;

    let vstepLevel = "B1 LEVEL (ĐẠT CHUẨN)";
    let levelDesc = "Bài viết đáp ứng đầy đủ yêu cầu đề bài, cấu trúc đoạn rõ ràng. Tuy nhiên còn một số lỗi ngữ pháp, mạo từ và dùng từ cần lưu ý sửa chữa.";
    if (overallBand >= 8.5) {
        vstepLevel = "B2 LEVEL (XUẤT SẮC - VƯỢT CHUẨN)";
        levelDesc = "Bài viết rất ấn tượng! Bố cục chuẩn mực 5 bước, từ vựng và ngữ pháp khuyên bảo đa dạng, hầu như không có lỗi sai.";
    } else if (overallBand < 6.0) {
        vstepLevel = "DƯỚI CHUẨN B1 (CẦN CẢI THIỆN)";
        levelDesc = "Bài viết còn nhiều lỗi ngữ pháp hoặc chưa đủ số từ (yêu cầu ≥ 120 từ). Hãy xem kỹ bảng sửa lỗi và bài mẫu bên dưới nhé!";
    }"""

new_calc = r"""    // Total VSTEP Band (Thang 10) & Quy đổi 30% bài thi Writing VSTEP (Thang 3.0 điểm)
    let overallBand = (tfScore + orgScore + vocScore + gramScore) / 4.0;
    overallBand = Math.round(overallBand * 10) / 10;

    // Quy đổi Thư (Task 1) chiếm 30% tổng điểm bài thi Writing (Thang 3.0 điểm)
    let convertedScore = Math.round((overallBand / 10.0) * 3.0 * 100) / 100; // ví dụ 2.19 / 3.00

    // Quy đổi 4 tiêu chí ra thang 0.75 điểm mỗi tiêu chí (0.75 x 4 = 3.00 điểm)
    let tfConv = Math.round((tfScore / 10.0) * 0.75 * 100) / 100;
    let orgConv = Math.round((orgScore / 10.0) * 0.75 * 100) / 100;
    let vocConv = Math.round((vocScore / 10.0) * 0.75 * 100) / 100;
    let gramConv = Math.round((gramScore / 10.0) * 0.75 * 100) / 100;

    let vstepLevel = "B1 LEVEL (ĐẠT CHUẨN)";
    let levelDesc = "Bài viết đáp ứng đầy đủ yêu cầu đề bài, cấu trúc đoạn rõ ràng. Tuy nhiên còn một số lỗi ngữ pháp, mạo từ và dùng từ cần lưu ý sửa chữa.";
    if (overallBand >= 8.5) {
        vstepLevel = "B2 LEVEL (XUẤT SẮC - VƯỢT CHUẨN)";
        levelDesc = "Bài viết rất ấn tượng! Bố cục chuẩn mực 5 bước, từ vựng và ngữ pháp khuyên bảo đa dạng, hầu như không có lỗi sai.";
    } else if (overallBand < 6.0) {
        vstepLevel = "DƯỚI CHUẨN B1 (CẦN CẢI THIỆN)";
        levelDesc = "Bài viết còn nhiều lỗi ngữ pháp hoặc chưa đủ số từ (yêu cầu ≥ 120 từ). Hãy xem kỹ bảng sửa lỗi và bài mẫu bên dưới nhé!";
    }"""

js_code = js_code.replace(target_find, new_calc)

# Update ResultCard HTML
target_html = r"""        <div class="extra-score-banner">
            <div class="score-main-group">
                <div class="score-circle-badge">${overallBand.toFixed(1)}</div>
                <div class="score-text-info">
                    <h4>${vstepLevel} - BAND ${overallBand.toFixed(1)}/10</h4>
                    <p>${levelDesc} (Số từ bài làm: <strong>${wordCount} từ</strong>)</p>
                </div>
            </div>
            <div class="extra-b1-badge" style="background: #ffffff; color: var(--primary-color);">
                THANG ĐIỂM VSTEP TỔNG THỂ
            </div>
        </div>

        <!-- 4 Criteria Grid based on VSTEP SCORING GUIDE -->
        <div class="criteria-grid">
            <div class="criterion-card">
                <div class="criterion-name">
                    <span>Task Fulfilment</span>
                    <span class="criterion-score">${tfScore.toFixed(1)}/10</span>
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
                    <span>Organization</span>
                    <span class="criterion-score">${orgScore.toFixed(1)}/10</span>
                </div>
                <div class="criterion-desc">
                    Bố cục 5 phần hoàn chỉnh. Sử dụng linh hoạt các liên từ nối (Firstly, Secondly, Next, Finally, Moreover, Besides).
                </div>
            </div>
            <div class="criterion-card">
                <div class="criterion-name">
                    <span>Vocabulary</span>
                    <span class="criterion-score">${vocScore.toFixed(1)}/10</span>
                </div>
                <div class="criterion-desc">
                    Vốn từ vựng đúng chủ đề. ${vocabErrors.length > 0 ? `Bị trừ điểm do có ${vocabErrors.length} lỗi dùng từ/từ loại chưa chuẩn.` : 'Sử dụng từ vựng chính xác.'}
                </div>
            </div>
            <div class="criterion-card">
                <div class="criterion-name">
                    <span>Grammar & Accuracy</span>
                    <span class="criterion-score">${gramScore.toFixed(1)}/10</span>
                </div>
                <div class="criterion-desc">
                    Áp dụng tốt cấu trúc khuyên bảo B1. ${grammarCount > 0 ? `Bị trừ điểm do mắc ${grammarCount} lỗi ngữ pháp/mạo từ/câu ghép.` : 'Ngữ pháp chuẩn xác.'}
                </div>
            </div>
        </div>"""

new_html = r"""        <div class="extra-score-banner">
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
                    Áp dụng tốt cấu trúc khuyên bảo B1. ${grammarCount > 0 ? `Bị trừ điểm do mắc ${grammarCount} lỗi ngữ pháp/mạo từ/câu ghép.` : 'Ngữ pháp chuẩn xác.'}
                </div>
            </div>
        </div>"""

js_code = js_code.replace(target_html, new_html)

# Update sendExtraPracticeReport call
js_code = js_code.replace("sendExtraPracticeReport(typeId, wordCount, overallBand, errors.length, rawText);", "sendExtraPracticeReport(typeId, wordCount, overallBand, convertedScore, errors.length, rawText);")

target_report = r"""function sendExtraPracticeReport(typeId, wordCount, score, errorCount, studentText) {
    if (!currentStudentName || !currentStudentClass) return;
    const typeObj = letterTypes.find(t => t.id === typeId);
    const typeTitle = typeObj ? typeObj.titleVi : typeId;
    const now = new Date().toLocaleString('vi-VN');

    const cleanSnippet = studentText.split('\n').join(' ').slice(0, 250);
    const reportPayload = `[BÀI LUYỆN TẬP THÊM - ${typeTitle.toUpperCase()}]: Học viên ${currentStudentName} (Lớp ${currentStudentClass}) | Band VSTEP: ${score.toFixed(1)}/10 | Số từ: ${wordCount} | Lỗi: ${errorCount} lỗi | Thời gian: ${now} | Bài làm: "${cleanSnippet}..."`;"""

new_report = r"""function sendExtraPracticeReport(typeId, wordCount, bandScore, convertedScore, errorCount, studentText) {
    if (!currentStudentName || !currentStudentClass) return;
    const typeObj = letterTypes.find(t => t.id === typeId);
    const typeTitle = typeObj ? typeObj.titleVi : typeId;
    const now = new Date().toLocaleString('vi-VN');

    const cleanSnippet = studentText.split('\n').join(' ').slice(0, 250);
    const reportPayload = `[BÀI LUYỆN TẬP THÊM - ${typeTitle.toUpperCase()}]: Học viên ${currentStudentName} (Lớp ${currentStudentClass}) | Điểm Task 1 (30%): ${convertedScore.toFixed(2)}/3.00 (Band ${bandScore.toFixed(1)}/10) | Số từ: ${wordCount} | Lỗi: ${errorCount} lỗi | Thời gian: ${now} | Bài làm: "${cleanSnippet}..."`;"""

js_code = js_code.replace(target_report, new_report)

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/pure_extra_logic.js", "w", encoding="utf-8") as f:
    f.write(js_code)

print("Updated pure_extra_logic.js with 30% score conversion!")
