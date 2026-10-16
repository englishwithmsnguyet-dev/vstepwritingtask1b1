# -*- coding: utf-8 -*-
import json
import re

print("--- Integrating Sentence-by-Sentence Audit Engine ---")

SENTENCE_AUDIT_JS = '''
// ==========================================================================
// VSTEP B1 WRITING TASK 1 - SENTENCE-BY-SENTENCE AUDIT & DIAGNOSTIC ENGINE
// ==========================================================================

function segmentLetterSentences(rawText) {
    if (!rawText) return [];
    let text = rawText.replace(/\\r\\n/g, '\\n').replace(/\\r/g, '\\n');
    
    // Protect common abbreviations from premature sentence splitting
    const abbrevs = ['mr\\\\.', 'mrs\\\\.', 'ms\\\\.', 'dr\\\\.', 'prof\\\\.', 'st\\\\.', 'e\\\\.g\\\\.', 'i\\\\.e\\\\.', 'etc\\\\.', 'vs\\\\.', 'a\\\\.m\\\\.', 'p\\\\.m\\\\.', 'no\\\\.'];
    abbrevs.forEach(abb => {
        const regex = new RegExp(`\\\\b${abb}`, 'gi');
        text = text.replace(regex, match => match.replace(/\\./g, '\\uE000'));
    });

    // Protect decimal numbers
    text = text.replace(/(\\d+)\\.(\\d+)/g, '$1\\uE000$2');

    // Split on sentence terminals (. ! ?) followed by whitespace or line break
    const rawSentences = text.split(/(?<=[.!?])\\s+|\\n+/);

    const sentences = [];
    rawSentences.forEach(s => {
        let clean = s.replace(/\\uE000/g, '.').trim();
        if (clean.length > 0) {
            sentences.push(clean);
        }
    });

    return sentences;
}

function auditIndividualSentence(sentence, index, totalSentences, typeId, globalErrors = []) {
    const sTrim = sentence.trim();
    const sLower = sTrim.toLowerCase();

    // 1. Determine Section & Role
    let roleName = "Thân bài (Body)";
    let roleIcon = "fa-pencil";
    let isSalutation = false;
    let isSignOff = false;

    if (index === 0 && /^dear\\s+[a-z]+/i.test(sTrim)) {
        roleName = "Lời chào mở đầu (Salutation)";
        roleIcon = "fa-envelope-open-text";
        isSalutation = true;
    } else if (index <= 2 && /(thanks?\\s+for|hope\\s+you|writing\\s+this\\s+letter|in\\s+your\\s+letter|how\\s+are\\s+you|glad\\s+to\\s+hear|i\\s+am\\s+writing)/i.test(sLower)) {
        roleName = "Mở đầu thư (Opening & Purpose)";
        roleIcon = "fa-book-open";
    } else if (index >= totalSentences - 2 && /(best\\s+wishes|yours\\s+(sincerely|faithfully)|warm\\s+regards|love|cheers|sincerely)\\b/i.test(sLower)) {
        roleName = "Lời chào kết thúc (Sign-off)";
        roleIcon = "fa-signature";
        isSignOff = true;
    } else if (index === totalSentences - 1 && sTrim.split(/\\s+/).length <= 3 && !/[.!?]$/.test(sTrim)) {
        roleName = "Ký tên người gửi (Signature)";
        roleIcon = "fa-user-pen";
        isSignOff = true;
    } else if (index >= totalSentences - 3 && /(look\\s+forward|hope\\s+(my\\s+advice|to\\s+hear|you\\s+can|this\\s+helps)|let\\s+me\\s+know|see\\s+you\\s+soon|write\\s+back)/i.test(sLower)) {
        roleName = "Câu kết thư (Closing)";
        roleIcon = "fa-paper-plane";
    }

    // 2. Identify sentence-specific errors
    const sentenceErrors = [];
    let rewrite = sTrim;

    // Check matched errors from global detector
    if (Array.isArray(globalErrors)) {
        globalErrors.forEach(err => {
            if (err.wrong && sLower.includes(err.wrong.toLowerCase())) {
                if (!sentenceErrors.some(e => e.wrong.toLowerCase() === err.wrong.toLowerCase())) {
                    sentenceErrors.push({
                        type: err.type || "Lỗi ngữ pháp",
                        wrong: err.wrong,
                        correct: err.correct,
                        reason: err.reason || "Cần điều chỉnh theo cấu trúc chuẩn."
                    });
                }
                const re = new RegExp(err.wrong.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&'), 'i');
                rewrite = rewrite.replace(re, err.correct);
            }
        });
    }

    // Modal + V-ing or Modal + to V
    const modalRule = /\\b(should|can|could|will|would|must|may|might)\\s+(to\\s+([a-z]+)|([a-z]+ing))\\b/i;
    const mModal = sTrim.match(modalRule);
    if (mModal) {
        const full = mModal[0];
        const modal = mModal[1];
        let correctV = '';
        if (mModal[2].startsWith('to ')) {
            correctV = mModal[3];
        } else {
            correctV = mModal[4].replace(/ing$/, '');
            if (mModal[4] === 'staying') correctV = 'stay';
            else if (mModal[4] === 'trying') correctV = 'try';
            else if (mModal[4] === 'going') correctV = 'go';
            else if (mModal[4] === 'visiting') correctV = 'visit';
            else if (mModal[4] === 'taking') correctV = 'take';
            else if (mModal[4] === 'eating') correctV = 'eat';
            else if (mModal[4] === 'wearing') correctV = 'wear';
        }
        if (!sentenceErrors.some(e => e.wrong.toLowerCase() === full.toLowerCase())) {
            sentenceErrors.push({
                type: "Động từ khuyết thiếu (Modal Verb)",
                wrong: full,
                correct: `${modal} ${correctV}`,
                reason: `Sau động từ khuyết thiếu '${modal}', động từ luôn ở dạng nguyên mẫu không 'to' (V-bare), không dùng 'to V' hay 'V-ing'.`
            });
            rewrite = rewrite.replace(new RegExp(full, 'i'), `${modal} ${correctV}`);
        }
    }

    // Missing 'to be' before adjectives
    const adjMissingBe = /\\b(it|this|that|they|weather|food|room)\\s+(convenient|delicious|hot|warm|cold|cheap|affordable|expensive|dirty|noisy|quiet|clean|important|necessary)\\b/i;
    const mAdj = sTrim.match(adjMissingBe);
    if (mAdj) {
        const subj = mAdj[1];
        const adj = mAdj[2];
        const be = (subj.toLowerCase() === 'they') ? 'are' : 'is';
        if (!sentenceErrors.some(e => e.wrong.toLowerCase() === mAdj[0].toLowerCase())) {
            sentenceErrors.push({
                type: "Cấu trúc câu (Thiếu động từ 'to be')",
                wrong: mAdj[0],
                correct: `${subj} ${be} ${adj}`,
                reason: `Sau chủ ngữ '${subj}' đi kèm tính từ '${adj}' bắt buộc phải có liên động từ '${be}'.`
            });
            rewrite = rewrite.replace(new RegExp(mAdj[0], 'i'), `${subj} ${be} ${adj}`);
        }
    }

    // "look forward to + Vo"
    if (/\\blook\\s+forward\\s+to\\s+([a-z]+)\\b/i.test(sTrim) && !/\\blook\\s+forward\\s+to\\s+[a-z]+ing\\b/i.test(sTrim)) {
        const mLF = sTrim.match(/\\blook\\s+forward\\s+to\\s+([a-z]+)\\b/i);
        if (mLF && mLF[1] !== 'hearing' && mLF[1] !== 'seeing' && mLF[1] !== 'meeting' && mLF[1] !== 'receiving') {
            const wrongW = mLF[1];
            let correctW = wrongW.replace(/e$/, '') + 'ing';
            if (wrongW === 'see') correctW = 'seeing';
            const fullW = mLF[0];
            const fixedW = `look forward to ${correctW}`;
            if (!sentenceErrors.some(e => e.wrong.toLowerCase() === fullW.toLowerCase())) {
                sentenceErrors.push({
                    type: "Cấu trúc câu (Look forward to + V-ing)",
                    wrong: fullW,
                    correct: fixedW,
                    reason: "Sau cụm cố định 'look forward to', động từ theo sau luôn chia ở dạng V-ing."
                });
                rewrite = rewrite.replace(new RegExp(fullW, 'i'), fixedW);
            }
        }
    }

    // "Thank for" -> "Thanks for / Thank you for"
    if (/\\bThank\\s+for\\b/i.test(sTrim) && !/\\bThanks\\s+for\\b/i.test(sTrim) && !/\\bThank\\s+you\\s+for\\b/i.test(sTrim)) {
        if (!sentenceErrors.some(e => e.wrong.toLowerCase().includes('thank for'))) {
            sentenceErrors.push({
                type: "Ngữ pháp mở thư",
                wrong: "Thank for",
                correct: "Thanks for / Thank you for",
                reason: "Cụm từ cảm ơn đúng phải có 's' ('Thanks for...') hoặc đầy đủ 'Thank you for...'."
            });
            rewrite = rewrite.replace(/\\bThank\\s+for\\b/i, 'Thank you for');
        }
    }

    // "I am write" -> "I am writing"
    if (/\\bI\\s+(am|'m)\\s+write\\b/i.test(sTrim)) {
        if (!sentenceErrors.some(e => e.wrong.toLowerCase().includes('write'))) {
            sentenceErrors.push({
                type: "Thì hiện tại tiếp diễn",
                wrong: "I am write",
                correct: "I am writing",
                reason: "Sau 'am/is/are' trong thì hiện tại tiếp diễn, động từ phải thêm đuôi -ing: 'I am writing'."
            });
            rewrite = rewrite.replace(/\\bI\\s+(am|'m)\\s+write\\b/i, 'I am writing');
        }
    }

    // Missing articles before singular places/items
    const mStayArt = sTrim.match(/\\bstay\\s+(in|at)\\s+(hotel|homestay)\\b/i);
    if (mStayArt) {
        if (!sentenceErrors.some(e => e.wrong.toLowerCase() === mStayArt[0].toLowerCase())) {
            sentenceErrors.push({
                type: "Mạo từ (Articles)",
                wrong: mStayArt[0],
                correct: `stay ${mStayArt[1]} a ${mStayArt[2]}`,
                reason: `Danh từ đếm được số ít '${mStayArt[2]}' cần có mạo từ 'a' phía trước.`
            });
            rewrite = rewrite.replace(new RegExp(mStayArt[0], 'i'), `stay ${mStayArt[1]} a ${mStayArt[2]}`);
        }
    }

    // Capitalization of first letter
    if (/^[a-z]/.test(sTrim)) {
        sentenceErrors.push({
            type: "Chính tả (Viết hoa đầu câu)",
            wrong: sTrim.slice(0, 1),
            correct: sTrim.slice(0, 1).toUpperCase(),
            reason: "Chữ cái đầu tiên của câu bắt buộc phải viết hoa."
        });
        rewrite = rewrite.charAt(0).toUpperCase() + rewrite.slice(1);
    }

    // Punctuation at end of sentence (skip salutation / signoff)
    if (!isSalutation && !isSignOff && !/[.!?]$/.test(sTrim)) {
        sentenceErrors.push({
            type: "Dấu câu (Thiếu dấu kết câu)",
            wrong: sTrim.slice(-5),
            correct: sTrim.slice(-5) + '.',
            reason: "Câu kết thúc hoàn chỉnh cần có dấu chấm câu (.)."
        });
        rewrite = rewrite + '.';
    }

    // Determine sentence status
    let status = "success";
    let statusLabel = "✓ Câu viết chuẩn xác";
    let statusBadgeClass = "badge-success";

    if (sentenceErrors.length > 0) {
        status = "warning";
        statusLabel = `⚠️ Có ${sentenceErrors.length} lỗi cần khắc phục`;
        statusBadgeClass = "badge-warning";
    } else {
        // If no errors, suggest stylistic upgrade
        if (roleName.includes("Opening") && sLower.includes("give you some advice")) {
            rewrite = "I am writing this letter to share some useful recommendations for your upcoming trip to Can Tho in December.";
            status = "upgrade";
            statusLabel = "💡 Gợi ý nâng cấp B2 tự nhiên hơn";
            statusBadgeClass = "badge-upgrade";
        } else if (roleName.includes("Closing") && sLower.includes("see you soon")) {
            rewrite = "I hope these suggestions are helpful, and I cannot wait to see you in Can Tho!";
            status = "upgrade";
            statusLabel = "💡 Gợi ý nâng cấp B2 ấn tượng hơn";
            statusBadgeClass = "badge-upgrade";
        } else if (sLower.includes("they are very delicious")) {
            rewrite = "Not only are these local dishes incredibly delicious, but they are also very affordable.";
            status = "upgrade";
            statusLabel = "💡 Gợi ý cấu trúc nâng Band (Đảo ngữ)";
            statusBadgeClass = "badge-upgrade";
        }
    }

    // Highlight errors in original text
    let highlightedHtml = escapeHtml(sTrim);
    sentenceErrors.forEach(err => {
        const re = new RegExp(`(${err.wrong.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&')})`, 'gi');
        highlightedHtml = highlightedHtml.replace(re, '<span class="audit-err-highlight">$1</span>');
    });

    return {
        sentenceIndex: index + 1,
        totalSentences,
        originalText: sTrim,
        highlightedHtml,
        roleName,
        roleIcon,
        status,
        statusLabel,
        statusBadgeClass,
        errors: sentenceErrors,
        rewrite: rewrite.trim()
    };
}

function renderSentenceAuditSectionHtml(sentenceAudits) {
    if (!sentenceAudits || sentenceAudits.length === 0) return '';

    const correctCount = sentenceAudits.filter(s => s.status === 'success').length;
    const warningCount = sentenceAudits.filter(s => s.status === 'warning').length;
    const upgradeCount = sentenceAudits.filter(s => s.status === 'upgrade').length;

    return `
        <div class="sentence-audit-wrapper" style="margin-top: 30px;">
            <div class="sentence-audit-header">
                <div class="sentence-audit-title">
                    <i class="fa-solid fa-list-check" style="color: var(--primary-color, #6366f1);"></i>
                    <span>BẢNG RÀ SOÁT CHI TIẾT TỪNG CÂU HỌC VIÊN ĐÃ VIẾT (${sentenceAudits.length} CÂU)</span>
                </div>
                <div class="sentence-audit-stats">
                    <span class="stat-pill success"><i class="fa-solid fa-circle-check"></i> ${correctCount} câu chuẩn</span>
                    ${warningCount > 0 ? `<span class="stat-pill warning"><i class="fa-solid fa-triangle-exclamation"></i> ${warningCount} câu có lỗi</span>` : ''}
                    ${upgradeCount > 0 ? `<span class="stat-pill upgrade"><i class="fa-solid fa-wand-magic-sparkles"></i> ${upgradeCount} câu gợi ý nâng Band</span>` : ''}
                </div>
            </div>
            <p class="sentence-audit-sub">
                Hệ thống bóc tách tỉ mỉ từng câu trong bài viết của bạn, đối chiếu ngữ pháp, chỉ ra lỗi cụ thể và cung cấp câu viết lại chuẩn B1/B2 để bạn học hỏi và cải thiện:
            </p>

            <div class="sentence-cards-list">
                ${sentenceAudits.map(s => `
                    <div class="sentence-audit-card ${s.status}">
                        <div class="sentence-card-head">
                            <div class="sentence-head-left">
                                <span class="sentence-index-badge">CÂU ${s.sentenceIndex}/${s.totalSentences}</span>
                                <span class="sentence-role-badge"><i class="fa-solid ${s.roleIcon}"></i> ${s.roleName}</span>
                            </div>
                            <span class="sentence-status-pill ${s.statusBadgeClass}">${s.statusLabel}</span>
                        </div>

                        <div class="sentence-card-content">
                            <div class="sentence-row original-row">
                                <span class="row-tag original-tag">Học viên viết:</span>
                                <div class="sentence-text original-text">"${s.highlightedHtml}"</div>
                            </div>

                            ${s.errors.length > 0 ? `
                                <div class="sentence-errors-box">
                                    <strong style="color: #dc2626; font-size: 13.5px;"><i class="fa-solid fa-circle-xmark"></i> Các lỗi cần khắc phục trong câu này:</strong>
                                    <ul class="sentence-error-items">
                                        ${s.errors.map(err => `
                                            <li>
                                                <span class="err-sub-type">[${escapeHtml(err.type)}]</span> 
                                                Viết sai: <span class="err-strike">"${escapeHtml(err.wrong)}"</span> 
                                                ➔ Sửa đúng: <strong class="err-fix">"${escapeHtml(err.correct)}"</strong>
                                                <div class="err-reason-note">💡 ${escapeHtml(err.reason)}</div>
                                            </li>
                                        `).join('')}
                                    </ul>
                                </div>
                            ` : ''}

                            <div class="sentence-row rewrite-row">
                                <span class="row-tag rewrite-tag"><i class="fa-solid fa-wand-magic-sparkles"></i> ${s.errors.length > 0 ? 'Viết lại đúng chuẩn:' : 'Gợi ý câu chuẩn B1/B2 mượt mà hơn:'}</span>
                                <div class="sentence-text rewrite-text">"${escapeHtml(s.rewrite)}"</div>
                            </div>
                        </div>
                    </div>
                `).join('')}
            </div>
        </div>
    `;
}
'''

# 1. Update scratch/dom_logic_full.js
with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/dom_logic_full.js", "r", encoding="utf-8") as f:
    dom_code = f.read()

# Add SENTENCE_AUDIT_JS before renderFullPracticeEvaluationResult
if "function segmentLetterSentences" not in dom_code:
    idx_render = dom_code.find("function renderFullPracticeEvaluationResult(")
    if idx_render != -1:
        dom_code = dom_code[:idx_render] + SENTENCE_AUDIT_JS + "\n\n" + dom_code[idx_render:]
        print("Injected sentence audit functions into dom_logic_full.js")

# In renderFullPracticeEvaluationResult, compute sentenceAudits and insert into HTML
if "const sentenceAudits = segmentedSentences.map" not in dom_code:
    target_pos = dom_code.find("const annotatedEssayHtml = (typeof buildAnnotatedEssayHtml === 'function')")
    if target_pos != -1:
        sentence_calc_code = """
    // Segment and audit every single sentence
    const segmentedSentences = segmentLetterSentences(rawText);
    const sentenceAudits = segmentedSentences.map((s, idx) => 
        auditIndividualSentence(s, idx, segmentedSentences.length, typeId, errors)
    );
    const sentenceAuditSectionHtml = renderSentenceAuditSectionHtml(sentenceAudits);
    """
        dom_code = dom_code[:target_pos] + sentence_calc_code.strip() + "\n\n    " + dom_code[target_pos:]

# Insert ${sentenceAuditSectionHtml} right above <!-- Detailed Error Table -->
if "${sentenceAuditSectionHtml}" not in dom_code:
    dom_code = dom_code.replace(
        "<!-- Detailed Error Table -->",
        "${sentenceAuditSectionHtml}\n\n        <!-- Detailed Error Table -->"
    )
    print("Injected sentenceAuditSectionHtml into fullPracticeResultBox HTML in dom_logic_full.js")

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/dom_logic_full.js", "w", encoding="utf-8") as f:
    f.write(dom_code)


# 2. Update scratch/pure_extra_logic.js
with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/pure_extra_logic.js", "r", encoding="utf-8") as f:
    extra_code = f.read()

if "function segmentLetterSentences" not in extra_code:
    # Append at bottom or before gradeExtraPractice
    idx_grade = extra_code.find("function gradeExtraPractice(")
    if idx_grade != -1:
        extra_code = extra_code[:idx_grade] + SENTENCE_AUDIT_JS + "\n\n" + extra_code[idx_grade:]
        print("Injected sentence audit functions into pure_extra_logic.js")

if "const sentenceAudits = segmentedSentences.map" not in extra_code:
    target_pos = extra_code.find("const annotatedEssayHtml = buildAnnotatedEssayHtml(rawText, errors);")
    if target_pos != -1:
        sentence_calc_code = """
    // Segment and audit every single sentence
    const segmentedSentences = segmentLetterSentences(rawText);
    const sentenceAudits = segmentedSentences.map((s, idx) => 
        auditIndividualSentence(s, idx, segmentedSentences.length, typeId, errors)
    );
    const sentenceAuditSectionHtml = renderSentenceAuditSectionHtml(sentenceAudits);
    """
        extra_code = extra_code[:target_pos] + sentence_calc_code.strip() + "\n\n    " + extra_code[target_pos:]

if "${sentenceAuditSectionHtml}" not in extra_code:
    extra_code = extra_code.replace(
        "${errorTableHtml}",
        "${sentenceAuditSectionHtml}\n\n            ${errorTableHtml}"
    )
    print("Injected sentenceAuditSectionHtml into resultCard HTML in pure_extra_logic.js")

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/pure_extra_logic.js", "w", encoding="utf-8") as f:
    f.write(extra_code)


# 3. Add CSS to writing-letters-b1level/style.css
CSS_ADDITION = """
/* ==========================================================================
   BẢNG RÀ SOÁT CHI TIẾT TỪNG CÂU (SENTENCE-BY-SENTENCE AUDIT STYLES)
   ========================================================================== */
.sentence-audit-wrapper {
    background: var(--bg-card, #ffffff);
    border: 1.5px solid var(--border-color, #e2e8f0);
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.05);
}

.sentence-audit-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: 8px;
}

.sentence-audit-title {
    font-size: 17px;
    font-weight: 800;
    color: var(--text-main, #1e293b);
    display: flex;
    align-items: center;
    gap: 10px;
}

.sentence-audit-stats {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
}

.stat-pill {
    font-size: 12.5px;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: 20px;
    display: inline-flex;
    align-items: center;
    gap: 6px;
}

.stat-pill.success {
    background: #ecfdf5;
    color: #059669;
    border: 1px solid #10b981;
}

.stat-pill.warning {
    background: #fef2f2;
    color: #dc2626;
    border: 1px solid #ef4444;
}

.stat-pill.upgrade {
    background: #f5f3ff;
    color: #7c3aed;
    border: 1px solid #8b5cf6;
}

.sentence-audit-sub {
    font-size: 14px;
    color: var(--text-muted, #64748b);
    margin: 0 0 20px 0;
    line-height: 1.5;
}

.sentence-cards-list {
    display: flex;
    flex-direction: column;
    gap: 16px;
}

.sentence-audit-card {
    background: var(--bg-main, #f8fafc);
    border: 1.5px solid var(--border-color, #cbd5e1);
    border-radius: 12px;
    padding: 16px 20px;
    transition: all 0.2s ease;
}

.sentence-audit-card.success {
    border-left: 5px solid #10b981;
}

.sentence-audit-card.warning {
    border-left: 5px solid #ef4444;
    background: #fffafa;
}

.sentence-audit-card.upgrade {
    border-left: 5px solid #8b5cf6;
    background: #faf8ff;
}

.sentence-card-head {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 12px;
    border-bottom: 1px dashed var(--border-color, #e2e8f0);
    padding-bottom: 10px;
}

.sentence-head-left {
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
}

.sentence-index-badge {
    font-size: 12px;
    font-weight: 800;
    background: var(--primary-color, #6366f1);
    color: #ffffff;
    padding: 3px 8px;
    border-radius: 6px;
}

.sentence-role-badge {
    font-size: 12.5px;
    font-weight: 600;
    color: var(--text-muted, #64748b);
    display: inline-flex;
    align-items: center;
    gap: 5px;
}

.sentence-status-pill {
    font-size: 12px;
    font-weight: 700;
    padding: 3px 10px;
    border-radius: 12px;
}

.sentence-status-pill.badge-success {
    background: #d1fae5;
    color: #065f46;
}

.sentence-status-pill.badge-warning {
    background: #fee2e2;
    color: #991b1b;
}

.sentence-status-pill.badge-upgrade {
    background: #ede9fe;
    color: #5b21b6;
}

.sentence-card-content {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.sentence-row {
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.row-tag {
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.row-tag.original-tag {
    color: var(--text-muted, #64748b);
}

.row-tag.rewrite-tag {
    color: #059669;
    display: flex;
    align-items: center;
    gap: 5px;
}

.sentence-text {
    font-size: 15px;
    line-height: 1.6;
    padding: 8px 12px;
    border-radius: 8px;
}

.sentence-text.original-text {
    background: rgba(0, 0, 0, 0.03);
    color: var(--text-main, #1e293b);
    font-style: italic;
}

.sentence-text.rewrite-text {
    background: rgba(16, 185, 129, 0.08);
    color: #065f46;
    font-weight: 600;
    border: 1px solid rgba(16, 185, 129, 0.2);
}

.audit-err-highlight {
    background: #fecaca;
    color: #991b1b;
    padding: 1px 4px;
    border-radius: 4px;
    border-bottom: 2px solid #ef4444;
    font-weight: 700;
}

.sentence-errors-box {
    background: #fff5f5;
    border: 1px solid #fecaca;
    border-radius: 8px;
    padding: 10px 14px;
}

.sentence-error-items {
    margin: 6px 0 0 18px;
    padding: 0;
    font-size: 13.5px;
    line-height: 1.6;
    color: #7f1d1d;
}

.sentence-error-items li {
    margin-bottom: 6px;
}

.err-sub-type {
    font-weight: 700;
    color: #b91c1c;
}

.err-strike {
    text-decoration: line-through;
    color: #ef4444;
    font-weight: 600;
}

.err-fix {
    color: #059669;
    font-weight: 700;
}

.err-reason-note {
    font-size: 12.5px;
    color: #555555;
    margin-top: 2px;
}

/* Dark mode compatibility */
[data-theme="dark"] .sentence-audit-wrapper {
    background: #1e293b;
    border-color: #334155;
}

[data-theme="dark"] .sentence-audit-card {
    background: #0f172a;
    border-color: #334155;
}

[data-theme="dark"] .sentence-audit-card.warning {
    background: #1f1315;
}

[data-theme="dark"] .sentence-audit-card.upgrade {
    background: #171228;
}

[data-theme="dark"] .sentence-text.original-text {
    background: rgba(255, 255, 255, 0.04);
    color: #e2e8f0;
}

[data-theme="dark"] .sentence-text.rewrite-text {
    background: rgba(16, 185, 129, 0.15);
    color: #6ee7b7;
    border-color: rgba(16, 185, 129, 0.35);
}

[data-theme="dark"] .sentence-errors-box {
    background: rgba(239, 68, 68, 0.1);
    border-color: rgba(239, 68, 68, 0.3);
}

[data-theme="dark"] .sentence-error-items {
    color: #fca5a5;
}

[data-theme="dark"] .err-reason-note {
    color: #cbd5e1;
}
"""

style_css_path = "/Users/nguyetpham/Desktop/WEBSITE/writing-letters-b1level/style.css"
with open(style_css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

if "BẢNG RÀ SOÁT CHI TIẾT TỪNG CÂU" not in css_content:
    with open(style_css_path, "a", encoding="utf-8") as f:
        f.write("\n\n" + CSS_ADDITION)
    print("Added sentence audit CSS styles to style.css")


# 4. Reassemble writing-letters-b1level/app.js
import subprocess
result = subprocess.run(
    ["python3", "/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/assemble_complete_working_app.py"],
    capture_output=True,
    text=True
)
print("Assemble output:", result.stdout)
if result.stderr:
    print("Assemble stderr:", result.stderr)


# 5. Bump version to v=52.0 in index.html
index_html_path = "/Users/nguyetpham/Desktop/WEBSITE/writing-letters-b1level/index.html"
with open(index_html_path, "r", encoding="utf-8") as f:
    index_html = f.read()

index_html = re.sub(r'style\.css\?v=[0-9.]+', 'style.css?v=52.0', index_html)
index_html = re.sub(r'app\.js\?v=[0-9.]+', 'app.js?v=52.0', index_html)

with open(index_html_path, "w", encoding="utf-8") as f:
    f.write(index_html)

print("Bumped version to v=52.0 in index.html")
print("--- Integration complete! ---")
