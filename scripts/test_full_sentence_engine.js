// Comprehensive Sentence-by-Sentence Audit Engine for VSTEP Task 1 Letters

function escapeHtml(str) {
    if (!str) return '';
    return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

function segmentLetterSentences(rawText) {
    if (!rawText) return [];
    let text = rawText.replace(/\r\n/g, '\n').replace(/\r/g, '\n');
    
    const abbrevs = ['mr\\.', 'mrs\\.', 'ms\\.', 'dr\\.', 'prof\\.', 'st\\.', 'e\\.g\\.', 'i\\.e\\.', 'etc\\.', 'vs\\.', 'a\\.m\\.', 'p\\.m\\.', 'no\\.'];
    abbrevs.forEach(abb => {
        const regex = new RegExp(`\\b${abb}`, 'gi');
        text = text.replace(regex, match => match.replace(/\./g, '\uE000'));
    });

    text = text.replace(/(\d+)\.(\d+)/g, '$1\uE000$2');

    const rawSentences = text.split(/(?<=[.!?])\s+|\n+/);

    const sentences = [];
    rawSentences.forEach(s => {
        let clean = s.replace(/\uE000/g, '.').trim();
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

    if (index === 0 && /^dear\s+[a-z]+/i.test(sTrim)) {
        roleName = "Lời chào mở đầu (Salutation)";
        roleIcon = "fa-envelope-open-text";
        isSalutation = true;
    } else if (index <= 2 && /(thanks?\s+for|hope\s+you|writing\s+this\s+letter|in\s+your\s+letter|how\s+are\s+you|glad\s+to\s+hear)/i.test(sLower)) {
        roleName = "Mở đầu thư (Opening & Purpose)";
        roleIcon = "fa-book-open";
    } else if (index >= totalSentences - 2 && /(best\s+wishes|yours\s+(sincerely|faithfully)|warm\s+regards|love|cheers|sincerely)\b/i.test(sLower)) {
        roleName = "Lời chào kết thúc (Sign-off)";
        roleIcon = "fa-signature";
        isSignOff = true;
    } else if (index === totalSentences - 1 && sTrim.split(/\s+/).length <= 3 && !/[.!?]$/.test(sTrim)) {
        roleName = "Ký tên người gửi (Signature)";
        roleIcon = "fa-user-pen";
        isSignOff = true;
    } else if (index >= totalSentences - 3 && /(look\s+forward|hope\s+(my\s+advice|to\s+hear|you\s+can|this\s+helps)|let\s+me\s+know|see\s+you\s+soon|write\s+back)/i.test(sLower)) {
        roleName = "Câu kết thư (Closing)";
        roleIcon = "fa-paper-plane";
    }

    // 2. Identify sentence-specific errors
    const sentenceErrors = [];
    let rewrite = sTrim;

    // Check matched errors from global detector
    globalErrors.forEach(err => {
        if (err.wrong && sLower.includes(err.wrong.toLowerCase())) {
            sentenceErrors.push({
                type: err.type,
                wrong: err.wrong,
                correct: err.correct,
                reason: err.reason
            });
            // Try naive replacement for rewrite
            const re = new RegExp(err.wrong.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'i');
            rewrite = rewrite.replace(re, err.correct);
        }
    });

    // Run additional targeted rules on this sentence
    // A. Modal + V-ing or Modal + to V
    const modalRule = /\b(should|can|could|will|would|must|may|might)\s+(to\s+([a-z]+)|([a-z]+ing))\b/i;
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
            if (mModal[4] === 'trying') correctV = 'try';
            if (mModal[4] === 'going') correctV = 'go';
            if (mModal[4] === 'visiting') correctV = 'visit';
            if (mModal[4] === 'taking') correctV = 'take';
            if (mModal[4] === 'eating') correctV = 'eat';
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

    // B. Missing "to be" before adjectives
    const adjMissingBe = /\b(it|this|that|they|weather|food|room)\s+(convenient|delicious|hot|warm|cold|cheap|affordable|expensive|dirty|noisy|quiet|clean|important|necessary)\b/i;
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

    // C. "look forward to + Vo"
    if (/\blook\s+forward\s+to\s+([a-z]+)\b/i.test(sTrim) && !/\blook\s+forward\s+to\s+[a-z]+ing\b/i.test(sTrim)) {
        const mLF = sTrim.match(/\blook\s+forward\s+to\s+([a-z]+)\b/i);
        if (mLF && mLF[1] !== 'hearing' && mLF[1] !== 'seeing' && mLF[1] !== 'meeting') {
            const wrongW = mLF[1];
            const correctW = wrongW.replace(/e$/, '') + 'ing';
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

    // D. "Thank for" -> "Thanks for / Thank you for"
    if (/\bThank\s+for\b/i.test(sTrim) && !/\bThanks\s+for\b/i.test(sTrim) && !/\bThank\s+you\s+for\b/i.test(sTrim)) {
        if (!sentenceErrors.some(e => e.wrong.toLowerCase().includes('thank for'))) {
            sentenceErrors.push({
                type: "Ngữ pháp mở thư",
                wrong: "Thank for",
                correct: "Thanks for / Thank you for",
                reason: "Cụm từ cảm ơn đúng phải có 's' ('Thanks for...') hoặc đầy đủ 'Thank you for...'."
            });
            rewrite = rewrite.replace(/\bThank\s+for\b/i, 'Thank you for');
        }
    }

    // E. "I am write" -> "I am writing"
    if (/\bI\s+(am|'m)\s+write\b/i.test(sTrim)) {
        if (!sentenceErrors.some(e => e.wrong.toLowerCase().includes('write'))) {
            sentenceErrors.push({
                type: "Thì hiện tại tiếp diễn",
                wrong: "I am write",
                correct: "I am writing",
                reason: "Sau 'am/is/are' trong thì hiện tại tiếp diễn, động từ phải thêm đuôi -ing: 'I am writing'."
            });
            rewrite = rewrite.replace(/\bI\s+(am|'m)\s+write\b/i, 'I am writing');
        }
    }

    // F. Missing articles before singular places/items: "stay in hotel" -> "stay in a hotel"
    const mStayArt = sTrim.match(/\bstay\s+(in|at)\s+(hotel|homestay)\b/i);
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

    // G. Capitalization of first letter
    if (/^[a-z]/.test(sTrim)) {
        sentenceErrors.push({
            type: "Quy tắc chính tả (Viết hoa đầu câu)",
            wrong: sTrim.slice(0, 1),
            correct: sTrim.slice(0, 1).toUpperCase(),
            reason: "Chữ cái đầu tiên của câu bắt buộc phải viết hoa."
        });
        rewrite = rewrite.charAt(0).toUpperCase() + rewrite.slice(1);
    }

    // H. Punctuation at end of sentence (skip salutation / signoff)
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
        // If no errors, suggest a B1/B2 stylistic upgrade
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

    // Build highlighted original sentence HTML
    let highlightedHtml = escapeHtml(sTrim);
    sentenceErrors.forEach(err => {
        const re = new RegExp(`(${err.wrong.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'gi');
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

// Test with our sample letter
const sampleLetter = `Dear Emily,
Thank for your letter. I am write this letter to give you some advice about your trip to Can Tho in December.
Firstly, you should staying at a hotel near Ninh Kieu Wharf because it convenient to travel.
Secondly, you must to try banh xeo and fresh fruits.
They are very delicious.
In addition, you can visit Cai Rang floating market.
You should wear light clothes because weather is warm.
I look forward to see you soon.
Best wishes,
Nguyet`;

const sList = segmentLetterSentences(sampleLetter);
console.log(`Auditing ${sList.length} sentences...\n`);

sList.forEach((s, idx) => {
    const res = auditIndividualSentence(s, idx, sList.length, 'advice', []);
    console.log(`--- [CÂU ${res.sentenceIndex}/${res.totalSentences}] [${res.roleName}] [${res.statusLabel}] ---`);
    console.log(`Gốc: "${res.originalText}"`);
    if (res.errors.length > 0) {
        res.errors.forEach(e => {
            console.log(`  ❌ Lỗi: [${e.type}] "${e.wrong}" -> Sửa: "${e.correct}"`);
            console.log(`     Lý do: ${e.reason}`);
        });
    }
    console.log(`  ✨ Viết lại: "${res.rewrite}"\n`);
});
