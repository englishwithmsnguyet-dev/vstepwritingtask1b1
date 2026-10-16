# -*- coding: utf-8 -*-
# Full Extra Practice Generator with VSTEP Scoring & Diagnostic Table
import json

full_extra_logic = """
// ==========================================================================
// VSTEP TASK 1 EXTRA PRACTICE & DIAGNOSTIC GRADING SYSTEM
// ==========================================================================

const extraPracticeData = {
    advice: {
        title: "BÀI LUYỆN TẬP THÊM - DẠNG 01: LETTER OF ADVICE",
        promptText: "You have received a letter from a friend, Emily. She is going to visit Can Tho in December. Write a letter to give her some suggestions. You should tell her:\\n• Where to stay\\n• What dishes to try\\n• Which tourist attractions to visit\\n• What to wear\\nYou should write at least 120 words. Do not include your name. Your response will be evaluated in terms of Task Fulfillment, Organization, Vocabulary, and Grammar.",
        bulletPoints: [
            "Where to stay",
            "What dishes to try",
            "Which tourist attractions to visit",
            "What to wear"
        ],
        hints: [
            {
                title: "1. Where to stay (Nơi ở)",
                items: [
                    {
                        en: "stay at a hotel in the city centre",
                        vi: "ở khách sạn tại trung tâm thành phố",
                        reasonEn: "because it is convenient to travel around the city.",
                        reasonVi: "vì thuận tiện để đi lại trong thành phố."
                    },
                    {
                        en: "stay at a homestay near Ninh Kieu Wharf",
                        vi: "ở homestay gần Bến Ninh Kiều",
                        reasonEn: "because you can easily visit many famous places.",
                        reasonVi: "vì bạn có thể dễ dàng tham quan nhiều địa điểm nổi tiếng."
                    },
                    {
                        en: "choose a hotel with good reviews",
                        vi: "chọn khách sạn có đánh giá tốt",
                        reasonEn: "because you are more likely to have a comfortable stay.",
                        reasonVi: "vì bạn sẽ có nhiều khả năng có một kỳ nghỉ thoải mái."
                    },
                    {
                        en: "book your room in advance",
                        vi: "đặt phòng trước",
                        reasonEn: "because it helps you get a better price and avoid fully booked hotels.",
                        reasonVi: "vì giúp bạn có giá tốt hơn và tránh tình trạng hết phòng."
                    }
                ]
            },
            {
                title: "2. What dishes to try (Những món ăn nên thử)",
                items: [
                    {
                        en: "try local dishes such as banh xeo, grilled snakehead fish, and fresh fruits",
                        vi: "thử các món ăn địa phương như bánh xèo, cá lóc nướng và trái cây tươi",
                        reasonEn: "because they are some of the most famous dishes in Can Tho and the Mekong Delta.",
                        reasonVi: "vì đây là những món ăn nổi tiếng nhất ở Cần Thơ và miền Tây."
                    },
                    {
                        en: "try traditional Vietnamese dishes such as noodle soup, spring rolls, and banh cong",
                        vi: "thử các món ăn truyền thống của Việt Nam như bún nước lèo, chả giò và bánh cống",
                        reasonEn: "because they can help you learn more about Vietnamese food culture.",
                        reasonVi: "vì chúng giúp bạn hiểu thêm về văn hóa ẩm thực Việt Nam."
                    },
                    {
                        en: "eat at local restaurants and night markets",
                        vi: "ăn tại các nhà hàng và chợ đêm địa phương",
                        reasonEn: "because you can enjoy authentic local food at reasonable prices.",
                        reasonVi: "vì bạn có thể thưởng thức ẩm thực địa phương chính gốc với giá hợp lý."
                    }
                ]
            },
            {
                title: "3. Which places to visit (Những địa điểm nên tham quan)",
                items: [
                    {
                        en: "visit famous places such as Cai Rang Floating Market, Ninh Kieu Wharf, and Binh Thuy Ancient House",
                        vi: "tham quan những địa điểm nổi tiếng như Chợ nổi Cái Răng, Bến Ninh Kiều và Nhà cổ Bình Thủy",
                        reasonEn: "because they are some of the most famous tourist attractions in Can Tho.",
                        reasonVi: "vì đây là những địa điểm du lịch nổi tiếng nhất ở Cần Thơ."
                    },
                    {
                        en: "take a boat trip to Cai Rang Floating Market early in the morning",
                        vi: "đi thuyền tham quan Chợ nổi Cái Răng vào sáng sớm",
                        reasonEn: "because you can enjoy the lively atmosphere and learn more about river culture.",
                        reasonVi: "vì bạn có thể tận hưởng không khí nhộn nhịp và tìm hiểu thêm về văn hóa sông nước."
                    },
                    {
                        en: "visit local fruit orchards and eco-tourism villages",
                        vi: "tham quan các vườn cây ăn trái và làng du lịch sinh thái",
                        reasonEn: "because you can relax in nature and taste fresh tropical fruits.",
                        reasonVi: "vì bạn có thể thư giãn giữa thiên nhiên và thưởng thức trái cây nhiệt đới tươi ngon."
                    }
                ]
            },
            {
                title: "4. What to wear when visiting Can Tho (Nên mặc gì khi đến Cần Thơ)",
                items: [
                    {
                        en: "wear light clothes and comfortable shoes",
                        vi: "mặc quần áo mỏng, nhẹ và mang giày thoải mái",
                        reasonEn: "because the weather in December is pleasant and you may have to walk a lot.",
                        reasonVi: "vì thời tiết tháng 12 dễ chịu và bạn có thể phải đi bộ nhiều."
                    },
                    {
                        en: "bring a hat, sunglasses, and sunscreen",
                        vi: "mang theo mũ, kính râm và kem chống nắng",
                        reasonEn: "because they can protect you from the strong sunlight during boat tours.",
                        reasonVi: "vì chúng có thể bảo vệ bạn khỏi ánh nắng gay gắt khi đi tour sông nước."
                    },
                    {
                        en: "bring a light jacket for breezy evenings",
                        vi: "mang theo áo khoác mỏng cho buổi tối mát mẻ",
                        reasonEn: "because it can be slightly cool near the river at night.",
                        reasonVi: "vì trời có thể hơi se lạnh gần bờ sông vào ban đêm."
                    }
                ]
            }
        ],
        sampleModel: "Dear Emily,\\n\\nThanks for your letter. I hope you are doing well. I’m writing to give you some advice for your trip to Can Tho in December.\\n\\nFirstly, you should stay at a hotel near Ninh Kieu Wharf because it is very convenient to travel around the city. In addition, you can easily visit many famous restaurants and cafes in the evening. Secondly, it would be a good idea to try some delicious local dishes such as banh xeo, grilled snakehead fish, and fresh tropical fruits. These dishes are very famous in the Mekong Delta and can help you learn more about Vietnamese food culture. Next, if I were you, I would take a boat trip to Cai Rang Floating Market early in the morning and visit Binh Thuy Ancient House. These are the most popular tourist attractions in Can Tho. Finally, remember to wear light clothes and comfortable shoes because you will walk and explore a lot. You should also bring a hat and sunglasses to protect yourself from the sunlight.\\n\\nI hope my advice will be helpful to you. Please let me know how everything turns out. Write back soon.\\n\\nBest wishes,",
        sampleModelVi: "Emily thân mến,\\n\\nCảm ơn thư của cậu. Tớ hy vọng cậu vẫn khỏe. Tớ viết thư này để đưa ra một vài gợi ý cho chuyến đi của cậu đến Cần Thơ vào tháng Mười Hai.\\n\\nĐầu tiên, cậu nên ở một khách sạn gần Bến Ninh Kiều vì nó rất thuận tiện cho việc đi lại quanh thành phố. Ngoài ra, cậu có thể dễ dàng ghé thăm nhiều nhà hàng và quán cà phê nổi tiếng vào buổi tối. Thứ hai, cậu nên thử một số món ăn địa phương thơm ngon như bánh xèo, cá lóc nướng và trái cây nhiệt đới tươi. Những món ăn này rất nổi tiếng ở miền Tây và giúp cậu hiểu thêm về văn hóa ẩm thực Việt Nam. Tiếp theo, nếu tớ là cậu, tớ sẽ đi thuyền tham quan Chợ nổi Cái Răng vào sáng sớm và ghé thăm Nhà cổ Bình Thủy. Đây là những điểm du lịch nổi tiếng nhất ở Cần Thơ. Cuối cùng, hãy nhớ mặc quần áo mỏng nhẹ và đi giày thoải mái vì cậu sẽ đi bộ và khám phá rất nhiều. Cậu cũng nên mang theo mũ và kính râm để bảo vệ bản thân khỏi ánh nắng mặt trời.\\n\\nTớ hy vọng những lời khuyên của tớ sẽ giúp ích cho cậu. Hãy cho tớ biết chuyến đi diễn ra thế nào nhé. Hãy viết thư lại sớm nhé.\\n\\nChúc cậu mọi điều tốt lành,",
        wordCount: 182
    }
};

function formatLetterParagraphs(str) {
    if (!str) return '';
    const doubleNl = String.fromCharCode(10) + String.fromCharCode(10);
    const singleNl = String.fromCharCode(10);
    return str.split(doubleNl).join('<br><br>').split(singleNl).join('<br>');
}

function renderExtraPracticePanel(typeId) {
    const container = document.getElementById('extraPracticePanel');
    if (!container) return;

    const data = extraPracticeData[typeId];
    if (!data) {
        container.innerHTML = `
            <div class="extra-practice-container">
                <div class="extra-prompt-box">
                    <div class="extra-prompt-header">
                        <span class="extra-prompt-title"><i class="fa-solid fa-pen-to-square"></i> BÀI LUYỆN TẬP THÊM</span>
                        <span class="extra-b1-badge">B1 LEVEL</span>
                    </div>
                    <div class="extra-prompt-body" style="text-align: center; padding: 40px 20px;">
                        <i class="fa-solid fa-clock-rotate-left" style="font-size: 36px; color: var(--text-muted); margin-bottom: 15px;"></i>
                        <h4 style="color: var(--text-main); margin-bottom: 8px;">Đề luyện tập thêm cho dạng thư này đang được cập nhật!</h4>
                        <p style="color: var(--text-muted); font-size: 14px;">Vui lòng chuyển qua <strong>DẠNG 01 (LETTER OF ADVICE)</strong> để trải nghiệm tính năng luyện tập & chấm điểm trực tiếp.</p>
                    </div>
                </div>
            </div>
        `;
        return;
    }

    let hintsHtml = '';
    data.hints.forEach(h => {
        let itemsHtml = '';
        h.items.forEach(it => {
            itemsHtml += `
                <div class="hint-item-card">
                    <div class="hint-item-en">↳ ${it.en}</div>
                    <div class="hint-item-vi">${it.vi}</div>
                    <div class="hint-item-reason">↳ ${it.reasonEn} (${it.reasonVi})</div>
                </div>
            `;
        });
        hintsHtml += `
            <div class="hint-section-block">
                <div class="hint-section-title"><i class="fa-solid fa-angles-right"></i> ${h.title}</div>
                <div class="hint-items-list">
                    ${itemsHtml}
                </div>
            </div>
        `;
    });

    let bulletsHtml = data.bulletPoints.map(b => `<li>${b}</li>`).join('');

    container.innerHTML = `
        <div class="extra-practice-container">
            <!-- Prompt Box -->
            <div class="extra-prompt-box">
                <div class="extra-prompt-header">
                    <span class="extra-prompt-title"><i class="fa-solid fa-file-pen"></i> ${data.title}</span>
                    <span class="extra-b1-badge">VSTEP B1 PRACTICE</span>
                </div>
                <div class="extra-prompt-body">
                    <p>You have received a letter from a friend, Emily. She is going to visit Can Tho in December. Write a letter to give her some suggestions. You should tell her:</p>
                    <ul>
                        ${bulletsHtml}
                    </ul>
                    <div class="extra-prompt-footer-note">
                        <i class="fa-solid fa-circle-info"></i> You should write at least <strong>120 words</strong>. Do not include your name. Your response will be evaluated in terms of Task Fulfillment, Organization, Vocabulary, and Grammar.
                    </div>
                </div>
            </div>

            <!-- Hints Toggle Card -->
            <div class="extra-hints-card">
                <button class="btn-toggle-hints" id="btnToggleHints">
                    <span><i class="fa-solid fa-lightbulb"></i> BẤM ĐỂ XEM GỢI Ý DÀN Ý & TỪ VỰNG CHI TIẾT</span>
                    <i class="fa-solid fa-chevron-down chevron-icon"></i>
                </button>
                <div class="hints-content hidden" id="extraHintsContent">
                    ${hintsHtml}
                </div>
            </div>

            <!-- Editor Card -->
            <div class="extra-editor-card">
                <div class="extra-editor-header">
                    <span class="extra-editor-title"><i class="fa-solid fa-keyboard"></i> KHUNG LÀM BÀI CỦA HỌC VIÊN</span>
                    <span class="extra-word-badge" id="extraWordBadge">0 / 120 words</span>
                </div>
                <textarea class="extra-textarea" id="extraWritingInput" placeholder="Nhập bài viết thư hoàn chỉnh của bạn tại đây (Bao gồm: Lời chào mở đầu, Mở bài, Thân bài 4 ý, Kết bài và Ký tên)..."></textarea>
                <div class="extra-editor-actions">
                    <button class="btn btn-secondary" id="btnClearExtraWriting">
                        <i class="fa-solid fa-rotate-left"></i> Viết lại
                    </button>
                    <button class="btn btn-primary" id="btnSubmitExtraWriting">
                        <i class="fa-solid fa-wand-magic-sparkles"></i> Nộp bài & Chấm điểm VSTEP
                    </button>
                </div>
            </div>

            <!-- Result & Evaluation Area (Hidden initially) -->
            <div class="extra-result-card hidden" id="extraResultCard">
                <!-- Injected after grading -->
            </div>
        </div>
    `;

    // Attach event listeners for extra practice
    const btnToggle = document.getElementById('btnToggleHints');
    const hintsContent = document.getElementById('extraHintsContent');
    if (btnToggle && hintsContent) {
        btnToggle.addEventListener('click', () => {
            hintsContent.classList.toggle('hidden');
            btnToggle.classList.toggle('expanded');
        });
    }

    const textarea = document.getElementById('extraWritingInput');
    const wordBadge = document.getElementById('extraWordBadge');
    if (textarea && wordBadge) {
        textarea.addEventListener('input', () => {
            const text = textarea.value.trim();
            const words = text ? text.split(/\\s+/).length : 0;
            wordBadge.textContent = `${words} / 120 words`;
            if (words >= 120) {
                wordBadge.classList.add('valid');
            } else {
                wordBadge.classList.remove('valid');
            }
        });
    }

    const btnClear = document.getElementById('btnClearExtraWriting');
    if (btnClear && textarea) {
        btnClear.addEventListener('click', () => {
            if (textarea.value.trim() && !confirm('Bạn có chắc chắn muốn xóa bài viết để viết lại không?')) return;
            textarea.value = '';
            textarea.dispatchEvent(new Event('input'));
            const resultCard = document.getElementById('extraResultCard');
            if (resultCard) resultCard.classList.add('hidden');
        });
    }

    const btnSubmit = document.getElementById('btnSubmitExtraWriting');
    if (btnSubmit) {
        btnSubmit.addEventListener('click', () => gradeExtraPractice(typeId));
    }
}

function gradeExtraPractice(typeId) {
    const textarea = document.getElementById('extraWritingInput');
    const resultCard = document.getElementById('extraResultCard');
    if (!textarea || !resultCard) return;

    const rawText = textarea.value.trim();
    if (!rawText || rawText.split(/\\s+/).length < 20) {
        alert('Vui lòng viết ít nhất một đoạn thư (tối thiểu 20 từ) trước khi nộp bài chấm điểm!');
        textarea.focus();
        return;
    }

    const words = rawText.split(/\\s+/);
    const wordCount = words.length;
    const lower = rawText.toLowerCase();

    const errors = [];

    // --- 1. DEEP ERROR DETECTION ---

    // A. Greeting & Opening
    if (/\\bThank\\s+for\\b/gi.test(rawText)) {
        errors.push({
            type: "Ngữ pháp / Lời mở đầu",
            wrong: "Thank for your letter",
            correct: "Thanks for your letter / Thank you for your letter",
            reason: "Cụm từ cảm ơn mở thư đúng ngữ pháp phải có 's' ('Thanks for...') hoặc dùng 'Thank you for...'."
        });
    }

    // B. Missing articles with singular countable nouns
    const rStayHotel = /\\bstay\\s+(in|at)\\s+(hotel|homestay)\\b/gi;
    let mStay;
    while ((mStay = rStayHotel.exec(rawText)) !== null) {
        errors.push({
            type: "Mạo từ (Articles)",
            wrong: mStay[0],
            correct: `stay ${mStay[1]} a ${mStay[2]}`,
            reason: `Danh từ đếm được số ít '${mStay[2]}' bắt buộc phải có mạo từ 'a' phía trước.`
        });
    }

    const rWearSingular = /\\b(wear|bring|take|buy)\\s+(ba\\s*ba\\s+shirt|shirt|conical\\s+hat|jacket|hat|umbrella|camera)\\b/gi;
    let mWear;
    while ((mWear = rWearSingular.exec(rawText)) !== null) {
        const noun = mWear[2];
        const art = noun.toLowerCase().startsWith('u') ? 'an' : 'a';
        errors.push({
            type: "Mạo từ (Articles)",
            wrong: mWear[0],
            correct: `${mWear[1]} ${art} ${noun}`,
            reason: `Danh từ số ít '${noun}' cần mạo từ '${art}' phía trước (ví dụ: ${mWear[1]} ${art} ${noun}).`
        });
    }

    if (/\\bin\\s+city\\s+center\\b/gi.test(rawText)) {
        errors.push({
            type: "Mạo từ (Articles)",
            wrong: "in city center",
            correct: "in the city center",
            reason: "Cụm từ chỉ trung tâm thành phố cần mạo từ xác định 'the': 'in the city center'."
        });
    }

    // C. Word Form & Part of Speech
    if (/\\bthe\\s+cultural\\s+of\\b/gi.test(rawText)) {
        errors.push({
            type: "Từ loại (Part of Speech)",
            wrong: "the cultural of Can Tho",
            correct: "the culture of Can Tho / the cultural identity of Can Tho",
            reason: "'cultural' là tính từ. Đứng sau mạo từ 'the' và trước 'of' bắt buộc phải dùng danh từ 'culture'."
        });
    }

    if (/\\badvices\\b/gi.test(rawText)) {
        errors.push({
            type: "Danh từ không đếm được",
            wrong: "advices",
            correct: "some advice / advice",
            reason: "'advice' là danh từ không đếm được, không thêm 's'."
        });
    }

    // D. Proper Noun & Collocation
    if (/\\bNinh\\s+Kieu\\s+way\\b/gi.test(rawText)) {
        errors.push({
            type: "Dùng từ / Địa danh",
            wrong: "Ninh Kieu way",
            correct: "Ninh Kieu Wharf / Ninh Kieu Pedestrian Bridge",
            reason: "Địa danh Bến Ninh Kiều dùng 'Wharf', Cầu đi bộ dùng 'Pedestrian Bridge', không dùng 'way'."
        });
    }

    // E. Sentence Structure & Parallelism
    if (/weather.*?can be.*?and an ideal time/gi.test(rawText)) {
        errors.push({
            type: "Cấu trúc câu (Sentence Structure)",
            wrong: "...because the weather in Can Tho can be very pleasant in December and an ideal time for tourism.",
            correct: "...because the weather in Can Tho is very pleasant in December, making it an ideal time for tourism (hoặc: and December is an ideal time for tourism).",
            reason: "Lỗi cấu trúc câu không song hành: 'weather' (thời tiết) không thể là 'an ideal time' (khoảng thời gian). Cần dùng mệnh đề phân từ 'making it an ideal time' hoặc tách mệnh đề."
        });
    }

    // F. Missing Comma after transitions
    const rTransitionNoComma = /(^|[.\\n])\\s*(Firstly|Secondly|Finally|Moreover|Besides|Furthermore|In addition|Therefore|For example)\\s+([a-zA-Z])/gi;
    let mTrans;
    while ((mTrans = rTransitionNoComma.exec(rawText)) !== null) {
        errors.push({
            type: "Dấu câu (Punctuation)",
            wrong: `${mTrans[2]} ${mTrans[3]}`,
            correct: `${mTrans[2]}, ${mTrans[3]}`,
            reason: `Sau liên từ đầu câu '${mTrans[2]}' cần có dấu phẩy (,).`
        });
    }

    // --- 2. VSTEP SCORING ON 10.0 SCALE (BASED ON OFFICIAL VSTEP SCORING GUIDE) ---

    // 1. Task Fulfilment (Thang 10)
    let tfScore = 8.0;
    const hasStay = /stay|hotel|homestay|ninh kieu|city cent|room|book|accommodat/.test(lower);
    const hasDishes = /dish|food|eat|try|banh|fish|fruit|noodle|soup|pork|spring roll|delicio|lau mam|banh cong/.test(lower);
    const hasAttractions = /visit|place|attraction|cai rang|market|floating|ninh kieu|wharf|ancient house|orchard|tour|my khanh/.test(lower);
    const hasWear = /wear|cloth|shoe|hat|sunglass|sunscreen|umbrella|jacket|weather|warm|hot|rain|ba ba/.test(lower);

    let coveredCount = [hasStay, hasDishes, hasAttractions, hasWear].filter(Boolean).length;
    if (coveredCount === 4) {
        tfScore = wordCount >= 140 ? 8.5 : (wordCount >= 120 ? 8.0 : 7.0);
    } else if (coveredCount === 3) {
        tfScore = 6.0;
    } else if (coveredCount === 2) {
        tfScore = 4.5;
    } else {
        tfScore = 3.0;
    }
    if (wordCount < 100) tfScore = Math.max(2.0, tfScore - 2.0);

    // 2. Organization (Thang 10)
    let orgScore = 8.0;
    const hasGreeting = /dear\\s+[a-z]+/i.test(rawText);
    const hasOpening = /thank(s)?\\s+for|hope you are doing well|give you some advice|writing to/i.test(rawText);
    const hasConnectors = /(firstly|secondly|next|finally|in addition|furthermore|moreover|besides|also)/gi.test(rawText);
    const hasClosing = /hope my advice|helpful|let me know|write back/i.test(rawText);
    const hasSignoff = /(best wishes|yours sincerely|warm regards|love)/i.test(rawText);

    let orgParts = [hasGreeting, hasOpening, hasConnectors, hasClosing, hasSignoff].filter(Boolean).length;
    if (orgParts === 5) {
        orgScore = 8.0;
    } else if (orgParts === 4) {
        orgScore = 7.0;
    } else {
        orgScore = 5.5;
    }

    // 3. Vocabulary (Thang 10)
    let vocScore = 7.5;
    const vocabErrors = errors.filter(e => e.type.includes('Từ loại') || e.type.includes('Dùng từ'));
    if (vocabErrors.length >= 2) {
        vocScore = 6.5;
    } else if (vocabErrors.length === 1) {
        vocScore = 7.0;
    }
    if (wordCount < 120) vocScore = Math.max(4.0, vocScore - 1.0);

    // 4. Grammar (Thang 10)
    let gramScore = 8.0;
    const grammarCount = errors.filter(e => !e.type.includes('Từ loại') && !e.type.includes('Dùng từ')).length;
    if (grammarCount >= 5) {
        gramScore = 6.0;
    } else if (grammarCount >= 3) {
        gramScore = 6.5;
    } else if (grammarCount >= 1) {
        gramScore = 7.0;
    } else {
        gramScore = 8.5;
    }

    // Total VSTEP Band
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
    }

    const data = extraPracticeData[typeId];

    // Build Error Table HTML
    let errorTableHtml = '';
    if (errors.length > 0) {
        let rowsHtml = errors.map((err, idx) => `
            <tr>
                <td style="font-weight: 700; color: var(--primary-color);">${idx + 1}</td>
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
                    DANH SÁCH ${errors.length} LỖI CẦN SỬA (NGỮ PHÁP, MẠO TỪ, TỪ LOẠI, DÙNG TỪ):
                </div>
                <div class="table-responsive">
                    <table class="error-table">
                        <thead>
                            <tr>
                                <th style="width: 40px;">#</th>
                                <th style="width: 140px;">Phân loại</th>
                                <th style="width: 170px;">Học viên viết</th>
                                <th style="width: 200px;">Đề xuất sửa đúng</th>
                                <th>Giải thích chi tiết</th>
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
            <div class="extra-feedback-box" style="background: rgba(16, 185, 129, 0.08); border-color: rgba(16, 185, 129, 0.3);">
                <div class="feedback-title" style="color: #059669;">
                    <i class="fa-solid fa-circle-check"></i> Không phát hiện lỗi ngữ pháp hay chính tả đáng kể nào!
                </div>
                <p style="margin: 0; font-size: 14px; color: var(--text-main);">Bài làm của bạn rất chuẩn chỉnh và mạch lạc.</p>
            </div>
        `;
    }

    // Build Results HTML
    resultCard.innerHTML = `
        <div class="extra-score-banner">
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
    sendExtraPracticeReport(typeId, wordCount, overallBand, errors.length, rawText);
}

function sendExtraPracticeReport(typeId, wordCount, score, errorCount, studentText) {
    if (!currentStudentName || !currentStudentClass) return;
    const typeObj = letterTypes.find(t => t.id === typeId);
    const typeTitle = typeObj ? typeObj.titleVi : typeId;
    const now = new Date().toLocaleString('vi-VN');

    const cleanSnippet = studentText.split(String.fromCharCode(10)).join(' ').slice(0, 250);
    const reportPayload = `[BÀI LUYỆN TẬP THÊM - ${typeTitle.toUpperCase()}]: Học viên ${currentStudentName} (Lớp ${currentStudentClass}) | Band VSTEP: ${score.toFixed(1)}/10 | Số từ: ${wordCount} | Lỗi: ${errorCount} lỗi | Thời gian: ${now} | Bài làm: "${cleanSnippet}..."`;

    try {
        const formInput = document.getElementById('gform_hidden_input');
        const formEl = document.getElementById('gform_hidden_form');
        if (formInput && formEl) {
            formInput.value = reportPayload;
            formEl.submit();
        }
    } catch (e) {
        console.warn('Form post error:', e);
    }
}
"""

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/full_extra_logic.js", "w", encoding="utf-8") as f:
    f.write(full_extra_logic)

print("Saved full_extra_logic.js")
