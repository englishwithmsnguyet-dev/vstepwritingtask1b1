# -*- coding: utf-8 -*-

comprehensive_js = r"""
// ==========================================================================
// VSTEP TASK 1 EXTRA PRACTICE & ULTRA-DETAILED DIAGNOSTIC GRADING SYSTEM
// ==========================================================================

const extraPracticeData = {
    advice: {
        title: "BÀI LUYỆN TẬP THÊM - DẠNG 01: LETTER OF ADVICE",
        promptText: "You have received a letter from a friend, Emily. She is going to visit Can Tho in December. Write a letter to give her some suggestions. You should tell her:\n• Where to stay\n• What dishes to try\n• Which tourist attractions to visit\n• What to wear\nYou should write at least 120 words. Do not include your name. Your response will be evaluated in terms of Task Fulfillment, Organization, Vocabulary, and Grammar.",
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
        sampleModel: `Dear Emily,\n\nThanks for your letter. I hope you are doing well. I’m writing to give you some advice for your trip to Can Tho in December.\n\nFirstly, you should stay at a hotel near Ninh Kieu Wharf because it is very convenient to travel around the city. In addition, you can easily visit many famous restaurants and cafes in the evening. Secondly, it would be a good idea to try some delicious local dishes such as banh xeo, grilled snakehead fish, and fresh tropical fruits. These dishes are very famous in the Mekong Delta and can help you learn more about Vietnamese food culture. Next, if I were you, I would take a boat trip to Cai Rang Floating Market early in the morning and visit Binh Thuy Ancient House. These are the most popular tourist attractions in Can Tho. Finally, remember to wear light clothes and comfortable shoes because you will walk and explore a lot. You should also bring a hat and sunglasses to protect yourself from the sunlight.\n\nI hope my advice will be helpful to you. Please let me know how everything turns out. Write back soon.\n\nBest wishes,`,
        sampleModelVi: `Emily thân mến,\n\nCảm ơn thư của cậu. Tớ hy vọng cậu vẫn khỏe. Tớ viết thư này để đưa ra một vài gợi ý cho chuyến đi của cậu đến Cần Thơ vào tháng Mười Hai.\n\nĐầu tiên, cậu nên ở một khách sạn gần Bến Ninh Kiều vì nó rất thuận tiện cho việc đi lại quanh thành phố. Ngoài ra, cậu có thể dễ dàng ghé thăm nhiều nhà hàng và quán cà phê nổi tiếng vào buổi tối. Thứ hai, cậu nên thử một số món ăn địa phương thơm ngon như bánh xèo, cá lóc nướng và trái cây nhiệt đới tươi. Những món ăn này rất nổi tiếng ở miền Tây và giúp cậu hiểu thêm về văn hóa ẩm thực Việt Nam. Tiếp theo, nếu tớ là cậu, tớ sẽ đi thuyền tham quan Chợ nổi Cái Răng vào sáng sớm và ghé thăm Nhà cổ Bình Thủy. Đây là những điểm du lịch nổi tiếng nhất ở Cần Thơ. Cuối cùng, hãy nhớ mặc quần áo mỏng nhẹ và đi giày thoải mái vì cậu sẽ đi bộ và khám phá rất nhiều. Cậu cũng nên mang theo mũ và kính râm để bảo vệ bản thân khỏi ánh nắng mặt trời.\n\nTớ hy vọng những lời khuyên của tớ sẽ giúp ích cho cậu. Hãy cho tớ biết chuyến đi diễn ra thế nào nhé. Hãy viết thư lại sớm nhé.\n\nChúc cậu mọi điều tốt lành,`,
        wordCount: 182
    }
};

function formatLetterParagraphs(str) {
    if (!str) return '';
    return str.split('\n\n').join('<br><br>').split('\n').join('<br>');
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
                        <i class="fa-solid fa-wand-magic-sparkles"></i> Nộp bài & Chấm điểm VSTEP (30%)
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
            const words = text ? text.split(/\s+/) : [];
            wordBadge.textContent = `${words.length} / 120 words`;
            if (words.length >= 120) {
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
    if (!rawText || rawText.split(/\s+/).length < 20) {
        alert('Vui lòng viết ít nhất một đoạn thư (tối thiểu 20 từ) trước khi nộp bài chấm điểm!');
        textarea.focus();
        return;
    }

    const words = rawText.split(/\s+/);
    const wordCount = words.length;
    const lower = rawText.toLowerCase();

    const errors = [];

    // =========================================================================
    // 1. ULTRA-DETAILED VSTEP TASK 1 ERROR DIAGNOSTIC RULES
    // =========================================================================

    // --- A. GREETINGS, OPENINGS & CLOSINGS ---
    if (/\bDear\s+[a-z]/g.test(rawText)) {
        const m = rawText.match(/\bDear\s+([a-z][a-zA-Z]*)/);
        if (m) {
            errors.push({
                type: "Chính tả / Viết hoa",
                category: "spelling",
                wrong: `Dear ${m[1]}`,
                correct: `Dear ${m[1].charAt(0).toUpperCase() + m[1].slice(1)},`,
                reason: `Tên riêng '${m[1]}' sau 'Dear' bắt buộc phải viết hoa chữ cái đầu và có dấu phẩy ở cuối.`
            });
        }
    }

    if (/\bDear\s+[A-Z][a-zA-Z]*\./g.test(rawText)) {
        errors.push({
            type: "Dấu câu (Punctuation)",
            category: "punctuation",
            wrong: "Dear [Name].",
            correct: "Dear [Name], (dùng dấu phẩy)",
            reason: "Lời chào đầu thư bằng tiếng Anh bắt buộc kết thúc bằng dấu phẩy (,), không dùng dấu chấm (.)."
        });
    }

    if (/\bThank\s+for\b/i.test(rawText)) {
        errors.push({
            type: "Ngữ pháp / Lời mở đầu",
            category: "grammar",
            wrong: "Thank for your letter",
            correct: "Thanks for your letter / Thank you for your letter",
            reason: "Cụm từ cảm ơn mở thư đúng ngữ pháp phải có 's' ('Thanks for...') hoặc dùng 'Thank you for...'."
        });
    }

    if (/\bThanks\s+you\s+for\b/i.test(rawText)) {
        errors.push({
            type: "Ngữ pháp / Lời mở đầu",
            category: "grammar",
            wrong: "Thanks you for",
            correct: "Thank you for / Thanks for",
            reason: "Không dùng 'Thanks you'. Chọn một trong hai: 'Thank you for...' hoặc 'Thanks for...'."
        });
    }

    if (/\b(i\s+am\s+write|i'm\s+write)\b/i.test(rawText)) {
        errors.push({
            type: "Ngữ pháp (Thì HTTD)",
            category: "grammar",
            wrong: "I am write / I'm write",
            correct: "I am writing / I'm writing",
            reason: "Cấu trúc thì hiện tại tiếp diễn: S + am/is/are + V-ing ('I am writing to...')."
        });
    }

    if (/\bI\s+write\s+this\s+letter\s+to\b/i.test(rawText)) {
        errors.push({
            type: "Cách diễn đạt mở thư",
            category: "vocab",
            wrong: "I write this letter to",
            correct: "I am writing this letter to / I am writing to",
            reason: "Trong thư tiếng Anh, chuẩn văn phong tự nhiên là dùng Hiện tại tiếp diễn: 'I am writing to give you some advice...'."
        });
    }

    if (/\bhope\s+you\s+well\b/i.test(rawText) && !/hope\s+you\s+are\s+well/i.test(rawText)) {
        errors.push({
            type: "Ngữ pháp (Thiếu động từ to be)",
            category: "grammar",
            wrong: "hope you well",
            correct: "I hope you are well / I hope you are doing well",
            reason: "Cần có động từ 'are' trước tính từ 'well': 'I hope you are well'."
        });
    }

    if (/\blook\s+forward\s+to\s+hear\b/i.test(rawText)) {
        errors.push({
            type: "Ngữ pháp (V-ing sau giới từ)",
            category: "grammar",
            wrong: "look forward to hear",
            correct: "look forward to hearing from you",
            reason: "Cấu trúc: 'look forward to + V-ing' ('look forward to hearing from you')."
        });
    }

    if (/\bBest\s+wish\b/i.test(rawText) && !/\bBest\s+wishes\b/i.test(rawText)) {
        errors.push({
            type: "Lời chào kết thúc",
            category: "spelling",
            wrong: "Best wish",
            correct: "Best wishes,",
            reason: "Lời chào kết thư chuẩn là 'Best wishes,' (danh từ số nhiều có 'es' kèm dấu phẩy)."
        });
    }

    if (/\bYours\s+sincere\b/i.test(rawText)) {
        errors.push({
            type: "Lời chào kết thúc",
            category: "grammar",
            wrong: "Yours sincere",
            correct: "Yours sincerely,",
            reason: "Cần dùng trạng từ: 'Yours sincerely,'."
        });
    }

    // --- B. ARTICLES (A / AN / THE / ZERO ARTICLE) ---
    const rStayHotel = /\bstay\s+(in|at)\s+(hotel|homestay)\b/gi;
    let mStay;
    while ((mStay = rStayHotel.exec(rawText)) !== null) {
        errors.push({
            type: "Mạo từ (Articles)",
            category: "article",
            wrong: mStay[0],
            correct: `stay ${mStay[1]} a ${mStay[2]}`,
            reason: `Danh từ đếm được số ít '${mStay[2]}' bắt buộc phải có mạo từ 'a' phía trước.`
        });
    }

    const rSingularItems = /\b(wear|bring|take|buy|choose|visit|rent|book)\s+(ba\s*ba\s+shirt|shirt|dress|hat|jacket|camera|conical\s+hat|umbrella|raincoat|room|hotel|homestay|taxi|bus|boat|museum|market|temple|pagoda)\b/gi;
    let mSingular;
    while ((mSingular = rSingularItems.exec(rawText)) !== null) {
        const verb = mSingular[1];
        const noun = mSingular[2];
        const art = noun.toLowerCase().startsWith('u') ? 'an' : 'a';
        errors.push({
            type: "Mạo từ (Articles)",
            category: "article",
            wrong: mSingular[0],
            correct: `${verb} ${art} ${noun}`,
            reason: `Danh từ đếm được số ít '${noun}' cần mạo từ '${art}' phía trước (${verb} ${art} ${noun}).`
        });
    }

    if (/\bin\s+city\s+center\b/gi.test(rawText) || /\bin\s+city\s+centre\b/gi.test(rawText)) {
        errors.push({
            type: "Mạo từ (Articles)",
            category: "article",
            wrong: "in city center",
            correct: "in the city center",
            reason: "Cụm từ chỉ trung tâm thành phố cần mạo từ xác định 'the': 'in the city center'."
        });
    }

    if (/\b(in\s+morning|in\s+afternoon|in\s+evening)\b/gi.test(rawText)) {
        const m = rawText.match(/\b(in\s+morning|in\s+afternoon|in\s+evening)\b/i);
        if (m) {
            errors.push({
                type: "Mạo từ (Articles)",
                category: "article",
                wrong: m[0],
                correct: m[0].replace('in ', 'in the '),
                reason: `Cụm từ chỉ buổi trong ngày cần mạo từ 'the' (${m[0].replace('in ', 'in the ')}).`
            });
        }
    }

    if (/\bby\s+a\s+(bus|taxi|car|train|plane|boat)\b/gi.test(rawText)) {
        const m = rawText.match(/\bby\s+a\s+(bus|taxi|car|train|plane|boat)\b/i);
        if (m) {
            errors.push({
                type: "Mạo từ (Zero Article)",
                category: "article",
                wrong: m[0],
                correct: `by ${m[1]}`,
                reason: `Cụm từ 'by + phương tiện giao thông' không dùng mạo từ (ví dụ: by ${m[1]}).`
            });
        }
    }

    // --- C. UNCOUNTABLE NOUNS ---
    if (/\badvices\b/gi.test(rawText)) {
        errors.push({
            type: "Danh từ không đếm được",
            category: "grammar",
            wrong: "advices",
            correct: "some advice / advice",
            reason: "'advice' là danh từ không đếm được trong tiếng Anh, không được thêm 's'."
        });
    }
    if (/\ban\s+advice\b/gi.test(rawText)) {
        errors.push({
            type: "Danh từ không đếm được",
            category: "grammar",
            wrong: "an advice",
            correct: "a piece of advice / some advice",
            reason: "'advice' không dùng với mạo từ 'an'. Hãy dùng 'some advice' hoặc 'a piece of advice'."
        });
    }
    if (/\binformations\b/gi.test(rawText)) {
        errors.push({
            type: "Danh từ không đếm được",
            category: "grammar",
            wrong: "informations",
            correct: "information / some information",
            reason: "'information' là danh từ không đếm được, không có dạng số nhiều 'informations'."
        });
    }
    if (/\bclothings\b/gi.test(rawText)) {
        errors.push({
            type: "Danh từ không đếm được",
            category: "grammar",
            wrong: "clothings",
            correct: "clothes / clothing",
            reason: "'clothing' không thêm 's'. Muốn chỉ quần áo hãy dùng 'clothes'."
        });
    }

    // --- D. PARTS OF SPEECH & COLLOCATIONS ---
    if (/\bthe\s+cultural\s+of\b/gi.test(rawText)) {
        errors.push({
            type: "Từ loại (Part of Speech)",
            category: "word_form",
            wrong: "the cultural of Can Tho",
            correct: "the culture of Can Tho / the cultural identity of Can Tho",
            reason: "'cultural' là tính từ. Đứng sau mạo từ 'the' và trước 'of' bắt buộc phải dùng danh từ 'culture'."
        });
    }

    if (/\bvery\s+beauty\b/gi.test(rawText)) {
        errors.push({
            type: "Từ loại (Part of Speech)",
            category: "word_form",
            wrong: "very beauty",
            correct: "very beautiful",
            reason: "'beauty' là danh từ. Sau trạng từ chỉ mức độ 'very' cần dùng tính từ 'beautiful'."
        });
    }

    if (/\bdeliciously\s+food\b/gi.test(rawText)) {
        errors.push({
            type: "Từ loại (Part of Speech)",
            category: "word_form",
            wrong: "deliciously food",
            correct: "delicious food",
            reason: "Trước danh từ 'food' cần dùng tính từ 'delicious' để bổ nghĩa, không dùng trạng từ 'deliciously'."
        });
    }

    if (/\btradition\s+(dishes|food|culture|clothes)\b/gi.test(rawText)) {
        const m = rawText.match(/\btradition\s+(dishes|food|culture|clothes)\b/i);
        if (m) {
            errors.push({
                type: "Từ loại (Part of Speech)",
                category: "word_form",
                wrong: m[0],
                correct: `traditional ${m[1]}`,
                reason: `Trước danh từ '${m[1]}' cần dùng tính từ 'traditional' (truyền thống).`
            });
        }
    }

    if (/\bfame\s+(places|attractions|restaurants)\b/gi.test(rawText)) {
        const m = rawText.match(/\bfame\s+(places|attractions|restaurants)\b/i);
        if (m) {
            errors.push({
                type: "Từ loại (Part of Speech)",
                category: "word_form",
                wrong: m[0],
                correct: `famous ${m[1]}`,
                reason: `Cần dùng tính từ 'famous' (nổi tiếng) trước danh từ '${m[1]}'.`
            });
        }
    }

    if (/\bgive\s+you\s+some\s+advise\b/gi.test(rawText)) {
        errors.push({
            type: "Nhầm lẫn từ (Confusing words)",
            category: "word_form",
            wrong: "give you some advise",
            correct: "give you some advice",
            reason: "'advise' là động từ (khuyên), còn danh từ lời khuyên là 'advice' (đuôi -ce)."
        });
    }

    // Proper Noun & Collocations
    if (/\bNinh\s+Kieu\s+way\b/gi.test(rawText)) {
        errors.push({
            type: "Dùng từ / Địa danh",
            category: "vocab",
            wrong: "Ninh Kieu way",
            correct: "Ninh Kieu Wharf / Ninh Kieu Pedestrian Bridge",
            reason: "Địa danh Bến Ninh Kiều dùng 'Wharf', Cầu đi bộ dùng 'Pedestrian Bridge', không dùng 'way'."
        });
    }

    // --- E. ADVICE STRUCTURES & VERB PATTERNS ---
    if (/\bshould\s+to\s+[a-z]+/gi.test(rawText)) {
        errors.push({
            type: "Dạng động từ (Verb Form)",
            category: "grammar",
            wrong: "should to + V",
            correct: "should + Vo (không dùng 'to')",
            reason: "Sau modal verb 'should' dùng động từ nguyên mẫu không 'to'."
        });
    }

    if (/\bshould\s+(stays|visits|wears|eats|tries|goes)\b/gi.test(rawText)) {
        const m = rawText.match(/\bshould\s+(stays|visits|wears|eats|tries|goes)\b/i);
        if (m) {
            const vo = m[1].replace(/s$/, '');
            errors.push({
                type: "Dạng động từ (Verb Form)",
                category: "grammar",
                wrong: m[0],
                correct: `should ${vo}`,
                reason: `Sau 'should' luôn là động từ nguyên mẫu không chia 's/es' (should ${vo}).`
            });
        }
    }

    if (/\bwould\s+be\s+a\s+good\s+idea\s+(try|stay|visit|wear|go|eat|book)\b/gi.test(rawText)) {
        const m = rawText.match(/\bwould\s+be\s+a\s+good\s+idea\s+(try|stay|visit|wear|go|eat|book)\b/i);
        if (m) {
            errors.push({
                type: "Cấu trúc khuyên bảo (Advice)",
                category: "grammar",
                wrong: m[0],
                correct: `would be a good idea to ${m[1]}`,
                reason: `Cấu trúc chuẩn: 'It would be a good idea to + Vo' (cần có 'to').`
            });
        }
    }

    if (/\bif\s+i\s+was\s+you\b/gi.test(rawText)) {
        errors.push({
            type: "Câu điều kiện loại 2",
            category: "grammar",
            wrong: "If I was you",
            correct: "If I were you",
            reason: "Trong câu điều kiện loại 2 đưa ra lời khuyên, quy tắc ngữ pháp chuẩn dùng 'were' cho tất cả các ngôi (If I were you, I would...)."
        });
    }

    if (/\bif\s+i\s+were\s+you[,\s]+i\s+will\b/gi.test(rawText)) {
        errors.push({
            type: "Câu điều kiện loại 2",
            category: "grammar",
            wrong: "If I were you, I will",
            correct: "If I were you, I would",
            reason: "Mệnh đề chính của câu điều kiện loại 2 dùng 'would + Vo', không dùng 'will'."
        });
    }

    if (/\bremember\s+(wear|bring|take|try|visit|book|stay)\b/gi.test(rawText)) {
        const m = rawText.match(/\bremember\s+(wear|bring|take|try|visit|book|stay)\b/i);
        if (m) {
            errors.push({
                type: "Dạng động từ (Verb pattern)",
                category: "grammar",
                wrong: m[0],
                correct: `remember to ${m[1]}`,
                reason: `Cấu trúc nhắc nhở ai nhớ làm việc gì: 'Remember to + Vo'.`
            });
        }
    }

    if (/\bdon't\s+forget\s+(bring|wear|take|visit|try|book|stay)\b/gi.test(rawText)) {
        const m = rawText.match(/\bdon't\s+forget\s+(bring|wear|take|visit|try|book|stay)\b/i);
        if (m) {
            errors.push({
                type: "Dạng động từ (Verb pattern)",
                category: "grammar",
                wrong: m[0],
                correct: `don't forget to ${m[1]}`,
                reason: `Cấu trúc: 'Don't forget to + Vo'.`
            });
        }
    }

    if (/\bsuggest\s+you\s+to\b/gi.test(rawText)) {
        errors.push({
            type: "Cấu trúc động từ Suggest",
            category: "grammar",
            wrong: "suggest you to [V]",
            correct: "suggest that you should [V] / suggest [V-ing]",
            reason: "'suggest' không đi với tân ngữ + to-V (không dùng 'suggest you to'). Dùng 'suggest that you (should) + Vo' hoặc 'suggest + V-ing'."
        });
    }

    // --- F. PREPOSITIONS OF TIME & PLACE ---
    if (/\b(on\s+December|at\s+December)\b/gi.test(rawText)) {
        errors.push({
            type: "Giới từ chỉ thời gian",
            category: "preposition",
            wrong: "on December / at December",
            correct: "in December",
            reason: "Với tháng trong năm, bắt buộc dùng giới từ 'in' ('in December')."
        });
    }

    if (/\bin\s+(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\b/gi.test(rawText)) {
        const m = rawText.match(/\bin\s+(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\b/i);
        if (m) {
            errors.push({
                type: "Giới từ chỉ thời gian",
                category: "preposition",
                wrong: m[0],
                correct: `on ${m[1]}`,
                reason: `Với thứ trong tuần, bắt buộc dùng giới từ 'on' (on ${m[1]}).`
            });
        }
    }

    if (/\barrive\s+to\s+Can\s+Tho\b/gi.test(rawText)) {
        errors.push({
            type: "Giới từ (Preposition)",
            category: "preposition",
            wrong: "arrive to Can Tho",
            correct: "arrive in Can Tho",
            reason: "Đến một thành phố/quốc gia dùng 'arrive in', không dùng 'arrive to'."
        });
    }

    if (/\bfamous\s+with\b/gi.test(rawText)) {
        errors.push({
            type: "Giới từ đi với tính từ",
            category: "preposition",
            wrong: "famous with",
            correct: "famous for",
            reason: "Nổi tiếng vì điều gì dùng cấu trúc 'famous for', không dùng 'famous with'."
        });
    }

    // --- G. SENTENCE STRUCTURE & PARALLELISM ---
    if (/weather.*?can be.*?and an ideal time/gi.test(rawText)) {
        errors.push({
            type: "Cấu trúc câu (Sentence Structure)",
            category: "grammar",
            wrong: "...because the weather in Can Tho can be very pleasant in December and an ideal time for tourism.",
            correct: "...because the weather in Can Tho is very pleasant in December, making it an ideal time for tourism (hoặc: and December is an ideal time for tourism).",
            reason: "Lỗi cấu trúc câu không song hành: 'weather' (thời tiết) không thể là 'an ideal time' (khoảng thời gian). Cần dùng mệnh đề phân từ 'making it an ideal time' hoặc tách mệnh đề."
        });
    }

    if (/\bAlthough.*?but\b/gi.test(rawText)) {
        errors.push({
            type: "Cấu trúc liên từ kép",
            category: "grammar",
            wrong: "Although ..., but ...",
            correct: "Although ... [không dùng 'but'] (hoặc chỉ dùng '... but ...')",
            reason: "Trong tiếng Anh không dùng song song 'Although' và 'but' trong cùng một câu."
        });
    }

    if (/\bBecause.*?so\b/gi.test(rawText)) {
        errors.push({
            type: "Cấu trúc liên từ kép",
            category: "grammar",
            wrong: "Because ..., so ...",
            correct: "Because ... [không dùng 'so'] (hoặc chỉ dùng '... so ...')",
            reason: "Trong tiếng Anh không dùng song song 'Because' và 'so' trong cùng một câu."
        });
    }

    // Missing Comma after transition words
    const rTransitionNoComma = /(^|[.!?])\s*(Firstly|Secondly|Finally|Moreover|Besides|Furthermore|In addition|Therefore|For example|However)\s+([a-zA-Z])/gi;
    let mTrans;
    while ((mTrans = rTransitionNoComma.exec(rawText)) !== null) {
        errors.push({
            type: "Dấu câu (Punctuation)",
            category: "punctuation",
            wrong: `${mTrans[2]} ${mTrans[3]}`,
            correct: `${mTrans[2]}, ${mTrans[3]}`,
            reason: `Sau liên từ đầu câu '${mTrans[2]}' bắt buộc phải có dấu phẩy (,).`
        });
    }

    // --- H. SUBJECT - VERB AGREEMENT ---
    if (/\b(places|attractions|dishes|hotels|homestays|prices)\s+is\b/gi.test(rawText)) {
        const m = rawText.match(/\b(places|attractions|dishes|hotels|homestays|prices)\s+is\b/i);
        if (m) {
            errors.push({
                type: "Hòa hợp Chủ ngữ - Động từ",
                category: "grammar",
                wrong: m[0],
                correct: `${m[1]} are`,
                reason: `Chủ ngữ số nhiều '${m[1]}' đi với động từ to be số nhiều 'are', không dùng 'is'.`
            });
        }
    }

    // --- I. COMMON SPELLING ERRORS DICTIONARY ---
    const spellDict = {
        'recieve': 'receive',
        'untill': 'until',
        'beautifull': 'beautiful',
        'restuarant': 'restaurant',
        'resturant': 'restaurant',
        'delicous': 'delicious',
        'deliciouse': 'delicious',
        'traditionel': 'traditional',
        'conveniant': 'convenient',
        'intresting': 'interesting',
        'recommand': 'recommend',
        'cloths': 'clothes',
        'comfortible': 'comfortable',
        'pleasent': 'pleasant',
        'attact': 'attract',
        'attaction': 'attraction',
        'attractions': 'attractions',
        'floting': 'floating',
        'villige': 'village',
        'touristm': 'tourism',
        'adviced': 'advised',
        'helpfull': 'helpful',
        'alot': 'a lot',
        'seperate': 'separate',
        'tomorow': 'tomorrow',
        'truely': 'truly',
        'freind': 'friend',
        'exciteing': 'exciting',
        'specialy': 'specially / especially'
    };

    for (const [wrongSp, correctSp] of Object.entries(spellDict)) {
        const regexSp = new RegExp('\\b' + wrongSp + '\\b', 'gi');
        if (regexSp.test(rawText)) {
            errors.push({
                type: "Chính tả (Spelling)",
                category: "spelling",
                wrong: wrongSp,
                correct: correctSp,
                reason: `Lỗi chính tả từ '${wrongSp}'. Từ đúng chuẩn là '${correctSp}'.`
            });
        }
    }

    // Lowercase 'i' as pronoun
    if (/(^|[.\s])i\s+(hope|am|think|suggest|would|was|were|can|will|have)\b/g.test(rawText)) {
        errors.push({
            type: "Viết hoa đại từ 'I'",
            category: "spelling",
            wrong: "i [động từ]",
            correct: "I [viết hoa]",
            reason: "Đại từ nhân xưng ngôi thứ nhất 'I' (tôi) trong tiếng Anh luôn luôn phải viết hoa."
        });
    }

    // Punctuation Spacing Errors (e.g. "word.Word" or "word ,word")
    const punctSpacingErrors = rawText.match(/[a-zA-Z][,\.?!][a-zA-Z]/g);
    if (punctSpacingErrors && punctSpacingErrors.length > 0) {
        errors.push({
            type: "Dấu câu / Khoảng trắng",
            category: "punctuation",
            wrong: punctSpacingErrors.slice(0, 3).join(', '),
            correct: "Thêm dấu cách sau dấu câu",
            reason: "Cần có một dấu cách sau dấu phẩy (,), dấu chấm (.) hoặc dấu chấm hỏi (?)."
        });
    }

    // Space before punctuation: "word ,"
    if (/\s+[,.?!]/g.test(rawText)) {
        errors.push({
            type: "Dấu câu / Khoảng trắng",
            category: "punctuation",
            wrong: "Có dấu cách trước dấu câu (ví dụ: 'từ ,')",
            correct: "Đặt dấu câu liền ngay sau từ (ví dụ: 'từ,')",
            reason: "Không đặt khoảng trắng trước dấu phẩy, dấu chấm hay dấu hỏi."
        });
    }

    // =========================================================================
    // 2. VSTEP SCORING ON 10.0 SCALE (OFFICIAL VSTEP BAND CRITERIA)
    // =========================================================================

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
    const hasGreeting = /dear\s+[a-z]+/i.test(rawText);
    const hasOpening = /thank(s)?\s+for|hope you are doing well|give you some advice|writing to/i.test(rawText);
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
    const vocabErrors = errors.filter(e => e.category === 'vocab' || e.category === 'word_form');
    if (vocabErrors.length >= 3) {
        vocScore = 6.0;
    } else if (vocabErrors.length === 2) {
        vocScore = 6.5;
    } else if (vocabErrors.length === 1) {
        vocScore = 7.0;
    }
    if (wordCount < 120) vocScore = Math.max(4.0, vocScore - 1.0);

    // 4. Grammar (Thang 10)
    let gramScore = 8.0;
    const grammarErrors = errors.filter(e => e.category === 'grammar' || e.category === 'article' || e.category === 'preposition');
    const totalGrammarCount = grammarErrors.length + (errors.filter(e => e.category === 'punctuation' || e.category === 'spelling').length > 0 ? 1 : 0);

    if (totalGrammarCount >= 6) {
        gramScore = 5.5;
    } else if (totalGrammarCount >= 4) {
        gramScore = 6.0;
    } else if (totalGrammarCount >= 2) {
        gramScore = 6.5;
    } else if (totalGrammarCount === 1) {
        gramScore = 7.0;
    } else {
        gramScore = 8.5;
    }

    // Total VSTEP Band (Thang 10) & Quy đổi 30% bài thi Writing VSTEP (Thang 3.0 điểm)
    let overallBand = (tfScore + orgScore + vocScore + gramScore) / 4.0;
    overallBand = Math.round(overallBand * 10) / 10;

    // Quy đổi Thư (Task 1) chiếm 30% tổng điểm bài thi Writing (Thang 3.0 điểm)
    let convertedScore = Math.round((overallBand / 10.0) * 3.0 * 100) / 100;

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
    }

    const data = extraPracticeData[typeId];

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
                                <th style="width: 160px;">Phân loại lỗi</th>
                                <th style="width: 180px;">Học viên viết</th>
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

function sendExtraPracticeReport(typeId, wordCount, bandScore, convertedScore, errorCount, studentText) {
    if (!currentStudentName || !currentStudentClass) return;
    const typeObj = letterTypes.find(t => t.id === typeId);
    const typeTitle = typeObj ? typeObj.titleVi : typeId;
    const now = new Date().toLocaleString('vi-VN');

    const cleanSnippet = studentText.split('\n').join(' ').slice(0, 250);
    const reportPayload = `[BÀI LUYỆN TẬP THÊM - ${typeTitle.toUpperCase()}]: Học viên ${currentStudentName} (Lớp ${currentStudentClass}) | Điểm Task 1 (30%): ${convertedScore.toFixed(2)}/3.00 (Band ${bandScore.toFixed(1)}/10) | Số từ: ${wordCount} | Lỗi: ${errorCount} lỗi | Thời gian: ${now} | Bài làm: "${cleanSnippet}..."`;

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

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/pure_extra_logic.js", "w", encoding="utf-8") as f:
    f.write(comprehensive_js)

print("Saved comprehensive pure_extra_logic.js successfully!")
