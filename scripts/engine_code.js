# Comprehensive VSTEP Task 1 Diagnostic & Grading Engine
engine_code = """
// ==========================================================================
// COMPREHENSIVE VSTEP TASK 1 DIAGNOSTIC & SCORING ENGINE
// ==========================================================================

function analyzeStudentLetterDetailed(rawText, typeId) {
    const text = rawText.trim();
    const words = text ? text.split(/\\s+/) : [];
    const wordCount = words.length;
    const lower = text.toLowerCase();

    const errors = [];
    let annotatedHtml = text;

    // --- 1. DETAILED ERROR DETECTION RULES ---

    // Rule A: Thank for -> Thanks for / Thank you for
    const rThankFor = /\\bThank\\s+for\\b/gi;
    if (rThankFor.test(text)) {
        errors.push({
            type: "Ngữ pháp / Lời mở đầu",
            category: "grammar",
            wrong: "Thank for your letter",
            correct: "Thanks for your letter / Thank you for your letter",
            reason: "Cụm từ cảm ơn mở thư đúng ngữ pháp phải có 's' (Thanks for...) hoặc dùng 'Thank you for...'."
        });
    }

    // Rule B: Missing articles with singular countable nouns
    // 1. stay in/at hotel / homestay
    const rStayHotel = /\\bstay\\s+(in|at)\\s+(hotel|homestay)\\b/gi;
    let mStay;
    while ((mStay = rStayHotel.exec(text)) !== null) {
        errors.push({
            type: "Mạo từ (Articles)",
            category: "article",
            wrong: mStay[0],
            correct: `stay ${mStay[1]} a ${mStay[2]}`,
            reason: `Danh từ đếm được số ít '${mStay[2]}' bắt buộc phải có mạo từ 'a' phía trước.`
        });
    }

    // 2. wear / bring + shirt / hat / jacket / umbrella / conical hat / shoes
    const rWearSingular = /\\b(wear|bring|take|buy)\\s+(ba\\s*ba\\s+shirt|shirt|conical\\s+hat|jacket|hat|umbrella|camera)\\b/gi;
    let mWear;
    while ((mWear = rWearSingular.exec(text)) !== null) {
        const noun = mWear[2];
        const art = noun.toLowerCase().startsWith('u') ? 'an' : 'a';
        errors.push({
            type: "Mạo từ (Articles)",
            category: "article",
            wrong: mWear[0],
            correct: `${mWear[1]} ${art} ${noun}`,
            reason: `Danh từ số ít '${noun}' cần mạo từ '${art}' phía trước (ví dụ: ${mWear[1]} ${art} ${noun}).`
        });
    }

    // 3. in city center -> in the city center
    if (/\\bin\\s+city\\s+center\\b/gi.test(text)) {
        errors.push({
            type: "Mạo từ (Articles)",
            category: "article",
            wrong: "in city center",
            correct: "in the city center",
            reason: "Cụm từ chỉ trung tâm thành phố cần mạo từ xác định 'the': 'in the city center'."
        });
    }

    // Rule C: Word Form & Part of Speech
    // 1. the cultural of -> the culture of
    if (/\\bthe\\s+cultural\\s+of\\b/gi.test(text)) {
        errors.push({
            type: "Từ loại (Part of Speech)",
            category: "word_form",
            wrong: "the cultural of Can Tho",
            correct: "the culture of Can Tho",
            reason: "'cultural' là tính từ. Đứng sau mạo từ 'the' và trước 'of' phải là danh từ 'culture'."
        });
    }

    // 2. Uncountable nouns with plural 's'
    if (/\\badvices\\b/gi.test(text)) {
        errors.push({
            type: "Danh từ không đếm được",
            category: "grammar",
            wrong: "advices",
            correct: "some advice / advice",
            reason: "'advice' là danh từ không đếm được trong tiếng Anh, không được thêm 's'."
        });
    }
    if (/\\binformations\\b/gi.test(text)) {
        errors.push({
            type: "Danh từ không đếm được",
            category: "grammar",
            wrong: "informations",
            correct: "information / some information",
            reason: "'information' là danh từ không đếm được, không có dạng số nhiều 'informations'."
        });
    }

    // Rule D: Proper Nouns & Collocations
    // 1. Ninh Kieu way
    if (/\\bNinh\\s+Kieu\\s+way\\b/gi.test(text)) {
        errors.push({
            type: "Dùng từ / Địa danh",
            category: "vocab",
            wrong: "Ninh Kieu way",
            correct: "Ninh Kieu Wharf / Ninh Kieu Pedestrian Bridge",
            reason: "Địa danh Bến Ninh Kiều dùng 'Wharf', Cầu đi bộ dùng 'Pedestrian Bridge', không dùng 'way'."
        });
    }

    // 2. convenient for travelling -> convenient to travel around
    if (/\\bconvenient\\s+for\\s+travelling\\b/gi.test(text)) {
        errors.push({
            type: "Kết hợp từ (Collocation)",
            category: "vocab",
            wrong: "convenient for travelling",
            correct: "convenient to travel / convenient for getting around",
            reason: "Cấu trúc tự nhiên và chuẩn hơn là 'convenient to travel around the city'."
        });
    }

    // Rule E: Sentence Structure & Parallelism
    // weather can be very pleasant ... and an ideal time
    if (/weather.*?can be.*?and an ideal time/gi.test(text)) {
        errors.push({
            type: "Cấu trúc câu (Sentence Structure)",
            category: "grammar",
            wrong: "...the weather in Can Tho can be very pleasant in December and an ideal time for tourism.",
            correct: "...the weather in Can Tho is very pleasant in December, making it an ideal time for tourism.",
            reason: "Lỗi câu không song hành: 'thời tiết' (weather) không thể đi kèm 'và là khoảng thời gian lý tưởng' (and an ideal time). Cần dùng mệnh đề phân từ 'making it an ideal time' hoặc tách câu."
        });
    }

    // Rule F: Modal verbs & Form patterns
    if (/\\bshould\\s+to\\s+[a-z]+/gi.test(text)) {
        errors.push({
            type: "Ngữ pháp (Modal verb)",
            category: "grammar",
            wrong: "should to + V",
            correct: "should + Vo (nguyên mẫu không 'to')",
            reason: "Động từ khiếm khuyết 'should' đi trực tiếp với động từ nguyên mẫu không 'to'."
        });
    }
    if (/\\bif\\s+i\\s+was\\s+you\\b/gi.test(text)) {
        errors.push({
            type: "Câu điều kiện loại 2",
            category: "grammar",
            wrong: "If I was you",
            correct: "If I were you",
            reason: "Trong câu điều kiện loại 2 giả định, dùng 'were' cho tất cả các ngôi (If I were you, I would...)."
        });
    }
    if (/\\bremember\\s+wear\\b/gi.test(text)) {
        errors.push({
            type: "Dạng động từ (Verb pattern)",
            category: "grammar",
            wrong: "remember wear",
            correct: "remember to wear",
            reason: "Cấu trúc nhắc nhở ai làm gì: 'Remember to + Vo'."
        });
    }
    if (/\\bdon't\\s+forget\\s+bring\\b/gi.test(text)) {
        errors.push({
            type: "Dạng động từ (Verb pattern)",
            category: "grammar",
            wrong: "don't forget bring",
            correct: "don't forget to bring",
            reason: "Cấu trúc: 'Don't forget to + Vo'."
        });
    }

    // Rule G: Missing comma after introductory transition words
    const rTransitionNoComma = /(^|[.\\n])\\s*(Firstly|Secondly|Finally|Moreover|Besides|Furthermore|In addition|Therefore|For example)\\s+([a-zA-Z])/gi;
    let mTrans;
    while ((mTrans = rTransitionNoComma.exec(text)) !== null) {
        errors.push({
            type: "Dấu câu (Punctuation)",
            category: "punctuation",
            wrong: `${mTrans[2]} ${mTrans[3]}`,
            correct: `${mTrans[2]}, ${mTrans[3]}`,
            reason: `Sau liên từ đứng đầu câu '${mTrans[2]}' bắt buộc phải có dấu phẩy (,).`
        });
    }

    // Rule H: Punctuation spacing (word.word)
    const punctSpacingErrors = text.match(/[a-zA-Z][,\\.?!][a-zA-Z]/g);
    if (punctSpacingErrors && punctSpacingErrors.length > 0) {
        errors.push({
            type: "Khoảng cách dấu câu",
            category: "punctuation",
            wrong: punctSpacingErrors.slice(0, 3).join(', '),
            correct: "Cần có khoảng trắng sau dấu câu",
            reason: "Lỗi dính chữ sau dấu câu. Luôn để một dấu cách sau dấu chấm/phẩy."
        });
    }

    // --- 2. VSTEP 4-CRITERIA SCORING ALIGNED WITH OFFICIAL BANDS (0 - 10) ---

    // 1. Task Fulfilment (Thang 10)
    let tfBand = 8.0;
    const hasStay = /stay|hotel|homestay|ninh kieu|city cent|room|book|accommodat/.test(lower);
    const hasDishes = /dish|food|eat|try|banh|fish|fruit|noodle|soup|pork|spring roll|delicio|lau mam|banh cong/.test(lower);
    const hasAttractions = /visit|place|attraction|cai rang|market|floating|ninh kieu|wharf|ancient house|orchard|tour|my khanh/.test(lower);
    const hasWear = /wear|cloth|shoe|hat|sunglass|sunscreen|umbrella|jacket|weather|warm|hot|rain|ba ba/.test(lower);

    let coveredCount = [hasStay, hasDishes, hasAttractions, hasWear].filter(Boolean).length;
    if (coveredCount === 4) {
        tfBand = wordCount >= 140 ? 8.5 : (wordCount >= 120 ? 8.0 : 7.0);
    } else if (coveredCount === 3) {
        tfBand = 6.0;
    } else if (coveredCount === 2) {
        tfBand = 4.5;
    } else {
        tfBand = 3.0;
    }
    if (wordCount < 100) tfBand = Math.max(2.0, tfBand - 2.0);

    // 2. Organization (Thang 10)
    let orgBand = 7.5;
    const hasGreeting = /dear\\s+[a-z]+/i.test(text);
    const hasOpening = /thank(s)?\\s+for|hope you are doing well|give you some advice|writing to/i.test(text);
    const hasConnectors = /(firstly|secondly|next|finally|in addition|furthermore|moreover|besides|also)/gi.test(text);
    const hasClosing = /hope my advice|helpful|let me know|write back/i.test(text);
    const hasSignoff = /(best wishes|yours sincerely|warm regards|love)/i.test(text);

    let orgParts = [hasGreeting, hasOpening, hasConnectors, hasClosing, hasSignoff].filter(Boolean).length;
    if (orgParts === 5) {
        orgBand = 8.0;
    } else if (orgParts === 4) {
        orgBand = 7.0;
    } else if (orgParts >= 2) {
        orgBand = 5.5;
    } else {
        orgBand = 3.5;
    }

    // 3. Vocabulary (Thang 10)
    let vocBand = 7.5;
    const vocabErrors = errors.filter(e => e.category === 'vocab' || e.category === 'word_form');
    if (vocabErrors.length >= 2) {
        vocBand = 6.5;
    } else if (vocabErrors.length === 1) {
        vocBand = 7.0;
    }
    if (wordCount < 120) vocBand = Math.max(4.0, vocBand - 1.0);

    // 4. Grammar (Thang 10)
    let gramBand = 8.0;
    const grammarErrors = errors.filter(e => e.category === 'grammar' || e.category === 'article');
    const totalGrammarErrors = grammarErrors.length + (errors.filter(e => e.category === 'punctuation').length > 0 ? 1 : 0);

    if (totalGrammarErrors >= 5) {
        gramBand = 6.0;
    } else if (totalGrammarErrors >= 3) {
        gramBand = 6.5;
    } else if (totalGrammarErrors >= 1) {
        gramBand = 7.0;
    } else {
        gramBand = 8.5;
    }

    // Overall Score (VSTEP Weighted Average)
    let overallBand = (tfBand + orgBand + vocBand + gramBand) / 4.0;
    overallBand = Math.round(overallBand * 10) / 10;

    let vstepLevel = "B1 LEVEL (ĐẠT CHUẨN)";
    let badgeClass = "badge-b1";
    let summaryComment = "Bài viết đáp ứng đầy đủ yêu cầu của đề bài, bố cục rõ ràng theo chuẩn 5 bước. Tuy nhiên còn một số lỗi ngữ pháp và mạo từ cần chỉnh sửa để đạt điểm tối ưu.";

    if (overallBand >= 8.5) {
        vstepLevel = "B2 LEVEL (XUẤT SẮC - VƯỢT CHUẨN)";
        badgeClass = "badge-b2";
        summaryComment = "Bài viết xuất sắc! Độ hoàn thành cao, câu văn tự nhiên và hầu như không mắc lỗi ngữ pháp.";
    } else if (overallBand < 6.0) {
        vstepLevel = "DƯỚI CHUẨN B1 (CẦN CẢI THIỆN)";
        badgeClass = "badge-below";
        summaryComment = "Bài viết còn nhiều lỗi ngữ pháp hoặc thiếu ý/thiếu từ. Cần ôn kỹ lại dàn ý và làm theo các mẫu câu gợi ý.";
    }

    return {
        wordCount,
        errors,
        scores: {
            tf: tfBand,
            org: orgBand,
            voc: vocBand,
            gram: gramBand,
            overall: overallBand
        },
        level: vstepLevel,
        badgeClass,
        summary: summaryComment,
        coveredItems: {
            stay: hasStay,
            dishes: hasDishes,
            attractions: hasAttractions,
            wear: hasWear
        }
    };
}
"""

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/engine_code.js", "w", encoding="utf-8") as f:
    f.write(engine_code)

print("Saved engine_code.js")
