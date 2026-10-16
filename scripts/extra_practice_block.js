
// --- Extra Practice Data & Logic ---
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
                        "en": "stay at a homestay near Ninh Kieu Wharf",
                        "vi": "ở homestay gần Bến Ninh Kiều",
                        "reasonEn": "because you can easily visit many famous places.",
                        "reasonVi": "vì bạn có thể dễ dàng tham quan nhiều địa điểm nổi tiếng."
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
                        reasonEn: "because you can enjoy the lively atmosphere and learn more about local river culture.",
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
                        reasonEn: "because they can protect you from the strong sunlight during river tours.",
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
        sampleModel: `Dear Emily,

Thanks for your letter. I hope you are doing well. I’m writing to give you some advice for your trip to Can Tho in December.

Firstly, you should stay at a hotel near Ninh Kieu Wharf because it is very convenient to travel around the city. In addition, you can easily visit many famous restaurants and cafes in the evening. Secondly, it would be a good idea to try some delicious local dishes such as banh xeo, grilled snakehead fish, and fresh tropical fruits. These dishes are very famous in the Mekong Delta and can help you learn more about Vietnamese food culture. Next, if I were you, I would take a boat trip to Cai Rang Floating Market early in the morning and visit Binh Thuy Ancient House. These are the most popular tourist attractions in Can Tho. Finally, remember to wear light clothes and comfortable shoes because you will walk and explore a lot. You should also bring a hat and sunglasses to protect yourself from the sunlight.

I hope my advice will be helpful to you. Please let me know how everything turns out. Write back soon.

Best wishes,`,
        sampleModelVi: `Emily thân mến,

Cảm ơn thư của cậu. Tớ hy vọng cậu vẫn khỏe. Tớ viết thư này để đưa ra một vài gợi ý cho chuyến đi của cậu đến Cần Thơ vào tháng Mười Hai.

Đầu tiên, cậu nên ở một khách sạn gần Bến Ninh Kiều vì nó rất thuận tiện cho việc đi lại quanh thành phố. Ngoài ra, cậu có thể dễ dàng ghé thăm nhiều nhà hàng và quán cà phê nổi tiếng vào buổi tối. Thứ hai, cậu nên thử một số món ăn địa phương thơm ngon như bánh xèo, cá lóc nướng và trái cây nhiệt đới tươi. Những món ăn này rất nổi tiếng ở miền Tây và giúp cậu hiểu thêm về văn hóa ẩm thực Việt Nam. Tiếp theo, nếu tớ là cậu, tớ sẽ đi thuyền tham quan Chợ nổi Cái Răng vào sáng sớm và ghé thăm Nhà cổ Bình Thủy. Đây là những điểm du lịch nổi tiếng nhất ở Cần Thơ. Cuối cùng, hãy nhớ mặc quần áo mỏng nhẹ và đi giày thoải mái vì cậu sẽ đi bộ và khám phá rất nhiều. Cậu cũng nên mang theo mũ và kính râm để bảo vệ bản thân khỏi ánh nắng mặt trời.

Tớ hy vọng những lời khuyên của tớ sẽ giúp ích cho cậu. Hãy cho tớ biết chuyến đi diễn ra thế nào nhé. Hãy viết thư lại sớm nhé.

Chúc cậu mọi điều tốt lành,`,
        wordCount: 182
    }
};

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
                        <i class="fa-solid fa-wand-magic-sparkles"></i> Nộp bài & Chấm điểm
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
            const words = text ? text.split(/\s+/).length : 0;
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
    if (!rawText || rawText.split(/\s+/).length < 20) {
        alert('Vui lòng viết ít nhất một đoạn thư (tối thiểu 20 từ) trước khi nộp bài chấm điểm!');
        textarea.focus();
        return;
    }

    const words = rawText.split(/\s+/);
    const wordCount = words.length;
    const lower = rawText.toLowerCase();

    // 1. Task Fulfillment (2.5 pts)
    let tfScore = 0.5; // base
    let tfDetails = [];
    const hasStay = /stay|hotel|homestay|ninh kieu|city cent|room|book|accommodat/.test(lower);
    const hasDishes = /dish|food|eat|try|banh|fish|fruit|noodle|soup|pork|spring roll|delicio/.test(lower);
    const hasAttractions = /visit|place|attraction|cai rang|market|floating|ninh kieu|wharf|ancient house|orchard|tour/.test(lower);
    const hasWear = /wear|cloth|shoe|hat|sunglass|sunscreen|umbrella|jacket|weather|warm|hot|rain/.test(lower);

    if (hasStay) { tfScore += 0.5; tfDetails.push('Đã gợi ý nơi ở (Where to stay)'); }
    else { tfDetails.push('Chưa thấy rõ gợi ý nơi ở (Where to stay)'); }

    if (hasDishes) { tfScore += 0.5; tfDetails.push('Đã giới thiệu món ăn (What dishes to try)'); }
    else { tfDetails.push('Chưa thấy rõ món ăn gợi ý (What dishes to try)'); }

    if (hasAttractions) { tfScore += 0.5; tfDetails.push('Đã gợi ý điểm tham quan (Tourist attractions)'); }
    else { tfDetails.push('Chưa thấy rõ điểm tham quan (Tourist attractions)'); }

    if (hasWear) { tfScore += 0.5; tfDetails.push('Đã khuyên trang phục phù hợp (What to wear)'); }
    else { tfDetails.push('Chưa thấy rõ lời khuyên trang phục (What to wear)'); }

    // Length check for TF
    if (wordCount >= 120) {
        // full bonus
    } else if (wordCount >= 100) {
        tfScore = Math.max(1.0, tfScore - 0.3);
    } else {
        tfScore = Math.max(0.5, tfScore - 0.7);
    }

    // 2. Organization (2.5 pts)
    let orgScore = 0.5;
    let orgDetails = [];
    const hasGreeting = /dear\s+[a-z]+/i.test(rawText);
    const hasOpening = /thanks for your letter|hope you are doing well|give you some advice|writing to/i.test(rawText);
    const hasConnectors = /(firstly|secondly|next|finally|in addition|furthermore|moreover|also)/gi.test(rawText);
    const hasClosing = /hope my advice|helpful|let me know|write back/i.test(rawText);
    const hasSignoff = /(best wishes|yours sincerely|warm regards|love)/i.test(rawText);

    if (hasGreeting) { orgScore += 0.4; orgDetails.push('Có lời chào mở đầu chuẩn (Dear ...)'); }
    else { orgDetails.push('Thiếu lời chào mở đầu (Dear Emily,...)'); }

    if (hasOpening) { orgScore += 0.4; orgDetails.push('Có câu mở thư khuyên bảo tự nhiên'); }
    else { orgDetails.push('Nên bổ sung câu mở đầu chuẩn (Thanks for your letter...)'); }

    if (hasConnectors) { orgScore += 0.5; orgDetails.push('Có sử dụng liên từ nối mạch lạc (Firstly, Secondly, Next, Finally...)'); }
    else { orgDetails.push('Nên thêm các liên từ (Firstly, Secondly, Next, Finally...) để bài viết liền mạch hơn'); }

    if (hasClosing) { orgScore += 0.4; orgDetails.push('Có câu kết thư chuẩn B1'); }
    else { orgDetails.push('Thiếu câu kết thư chuẩn B1 (I hope my advice will be helpful...)'); }

    if (hasSignoff) { orgScore += 0.3; orgDetails.push('Có lời chào kết thúc (Best wishes,...)'); }
    else { orgDetails.push('Thiếu lời chào kết thúc (Best wishes,)'); }

    // 3. Vocabulary (2.5 pts)
    let vocScore = 1.0;
    let vocDetails = [];
    const richVocab = /(convenient|traditional|delicious|famous|popular|attraction|ancient|comfortable|protect|sunlight|explore|scenery)/gi;
    const matchVocab = rawText.match(richVocab);
    const uniqueVocab = matchVocab ? [...new Set(matchVocab.map(v => v.toLowerCase()))] : [];
    
    if (uniqueVocab.length >= 4) {
        vocScore += 1.5;
        vocDetails.push(`Từ vựng đa dạng, đúng chủ đề du lịch (${uniqueVocab.slice(0, 5).join(', ')}...)`);
    } else if (uniqueVocab.length >= 2) {
        vocScore += 1.0;
        vocDetails.push(`Sử dụng từ vựng phù hợp (${uniqueVocab.join(', ')}). Nên nâng cấp thêm từ vựng phong phú hơn.`);
    } else {
        vocScore += 0.5;
        vocDetails.push('Nên bổ sung thêm từ vựng mô tả địa điểm, món ăn và du lịch chuẩn B1.');
    }

    // 4. Grammar & Sentence Structures (2.5 pts)
    let gramScore = 1.0;
    let gramDetails = [];
    const adviceStructures = /(you should|it would be a good idea|if i were you|you can try|remember to|don't forget to)/gi;
    const matchStruct = rawText.match(adviceStructures);
    const uniqueStruct = matchStruct ? [...new Set(matchStruct.map(s => s.toLowerCase()))] : [];

    if (uniqueStruct.length >= 3) {
        gramScore += 1.5;
        gramDetails.push(`Áp dụng xuất sắc ${uniqueStruct.length} mẫu câu khuyên bảo chuẩn B1: "${uniqueStruct.join('", "')}"`);
    } else if (uniqueStruct.length >= 1) {
        gramScore += 1.0;
        gramDetails.push(`Đã sử dụng mẫu câu khuyên bảo: "${uniqueStruct.join('", "')}". Hãy phối hợp đa dạng hơn (vd: If I were you..., Remember to...).`);
    } else {
        gramScore += 0.4;
        gramDetails.push('Chưa thấy rõ các mẫu câu khuyên bảo chuẩn B1 (You should + Vo, It would be a good idea to + Vo, If I were you...).');
    }

    // Check punctuation spacing errors
    const punctSpacingErrors = rawText.match(/[a-zA-Z][,\.?!][a-zA-Z]/g);
    if (punctSpacingErrors && punctSpacingErrors.length > 0) {
        gramDetails.push(`Lưu ý dấu câu: Cần có khoảng trắng sau dấu phẩy/chấm (phát hiện lỗi dính từ ở: "${punctSpacingErrors.slice(0, 3).join('", "')}")`);
        gramScore = Math.max(0.5, gramScore - 0.3);
    }

    // Total Score calculation
    let totalScore = tfScore + orgScore + vocScore + gramScore;
    totalScore = Math.min(10.0, Math.max(1.0, Math.round(totalScore * 10) / 10));

    let levelLabel = "ĐẠT CHUẨN B1 (PASS)";
    let levelClass = "badge-pass";
    let levelDesc = "Bài viết tốt, bố cục rõ ràng và đáp ứng đầy đủ yêu cầu của đề bài.";
    if (totalScore >= 8.5) {
        levelLabel = "XUẤT SẮC - VƯỢT CHUẨN B1";
        levelDesc = "Bài viết rất ấn tượng! Bố cục chuẩn mực 5 bước, từ vựng và ngữ pháp khuyên bảo đa dạng.";
    } else if (totalScore < 5.5) {
        levelLabel = "CHƯA ĐẠT CHUẨN B1 (CẦN CẢI THIỆN)";
        levelDesc = "Bài viết còn thiếu ý hoặc chưa đủ số từ (yêu cầu ≥ 120 từ). Hãy tham khảo gợi ý và bài mẫu bên dưới nhé!";
    }

    const data = extraPracticeData[typeId];

    // Build Results HTML
    resultCard.innerHTML = `
        <div class="extra-score-banner">
            <div class="score-main-group">
                <div class="score-circle-badge">${totalScore.toFixed(1)}</div>
                <div class="score-text-info">
                    <h4>${levelLabel}</h4>
                    <p>${levelDesc} (Số từ bài làm: <strong>${wordCount} từ</strong>)</p>
                </div>
            </div>
            <div class="extra-b1-badge" style="background: #ffffff; color: var(--primary-color);">
                THANG ĐIỂM 10 VSTEP
            </div>
        </div>

        <!-- 4 Criteria Grid -->
        <div class="criteria-grid">
            <div class="criterion-card">
                <div class="criterion-name">
                    <span>Task Fulfillment</span>
                    <span class="criterion-score">${tfScore.toFixed(1)}/2.5</span>
                </div>
                <div class="criterion-desc">${tfDetails.join('. ')}.</div>
            </div>
            <div class="criterion-card">
                <div class="criterion-name">
                    <span>Organization</span>
                    <span class="criterion-score">${orgScore.toFixed(1)}/2.5</span>
                </div>
                <div class="criterion-desc">${orgDetails.join('. ')}.</div>
            </div>
            <div class="criterion-card">
                <div class="criterion-name">
                    <span>Vocabulary</span>
                    <span class="criterion-score">${vocScore.toFixed(1)}/2.5</span>
                </div>
                <div class="criterion-desc">${vocDetails.join('. ')}.</div>
            </div>
            <div class="criterion-card">
                <div class="criterion-name">
                    <span>Grammar & Accuracy</span>
                    <span class="criterion-score">${gramScore.toFixed(1)}/2.5</span>
                </div>
                <div class="criterion-desc">${gramDetails.join('. ')}.</div>
            </div>
        </div>

        <!-- Detailed Strengths and Corrections -->
        <div class="extra-feedback-box">
            <div class="feedback-title"><i class="fa-solid fa-circle-check" style="color: #059669;"></i> ĐÁNH GIÁ CHI TIẾT & LỜI KHUYÊN NÂNG CAO ĐIỂM:</div>
            <ul class="feedback-items-list">
                ${tfDetails.map(t => `<li class="strength"><i class="fa-solid fa-check"></i> ${t}</li>`).join('')}
                ${orgDetails.map(o => `<li><i class="fa-solid fa-arrow-right"></i> ${o}</li>`).join('')}
                ${gramDetails.map(g => `<li class="${g.includes('Lưu ý') || g.includes('Chưa') ? 'correction' : 'strength'}"><i class="fa-solid fa-angle-right"></i> ${g}</li>`).join('')}
            </ul>
        </div>

        <!-- Unlocked Sample Model Letter -->
        <div class="extra-model-wrapper">
            <div class="extra-model-title">
                <i class="fa-solid fa-award"></i> BÀI VIẾT MẪU CHUẨN B1 THAM KHẢO (MODEL LETTER)
            </div>
            <div class="extra-model-letter">
                ${data.sampleModel.replace(/\n\n/g, '<br><br>')}
            </div>
            <div class="extra-model-trans">
                <strong>BẢN DỊCH CHI TIẾT:</strong><br><br>
                ${data.sampleModelVi.replace(/\n\n/g, '<br><br>')}
            </div>
        </div>
    `;

    resultCard.classList.remove('hidden');
    resultCard.scrollIntoView({ behavior: 'smooth', block: 'start' });

    // Send Form Report to Teacher
    sendExtraPracticeReport(typeId, wordCount, totalScore, rawText);
}

function sendExtraPracticeReport(typeId, wordCount, score, studentText) {
    if (!currentStudentName || !currentStudentClass) return;
    const typeObj = letterTypes.find(t => t.id === typeId);
    const typeTitle = typeObj ? typeObj.titleVi : typeId;
    const now = new Date().toLocaleString('vi-VN');

    const reportPayload = `[BÀI LUYỆN TẬP THÊM - ${typeTitle.toUpperCase()}]: Học viên ${currentStudentName} (Lớp ${currentStudentClass}) | Điểm: ${score.toFixed(1)}/10 | Số từ: ${wordCount} words | Thời gian: ${now} | Bài làm: "${studentText.replace(/\n+/g, ' ').slice(0, 300)}..."`;

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
