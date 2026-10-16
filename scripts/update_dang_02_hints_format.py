# -*- coding: utf-8 -*-

pure_extra_code = r"""// ==========================================
// VSTEP B1 WRITING TASK 1 - EXTRA PRACTICE & DIAGNOSTIC SYSTEM
// ==========================================

const extraPracticeData = {
    advice: {
        title: "DẠNG 01: LETTER OF ADVICE (THƯ KHUYÊN BẢO)",
        prompt: `You have received a letter from a friend, Emily. She is going to visit Can Tho in December. Write a letter to give her some suggestions. You should tell her:
• Where to stay
• What dishes to try
• Which tourist attractions to visit
• What to wear
You should write at least 120 words. Do not include your name. Your response will be evaluated in terms of Task Fulfillment, Organization, Vocabulary, and Grammar.`,
        analysis: {
            recipient: "Emily (Bạn bè)",
            purpose: "Gợi ý cho chuyến du lịch Cần Thơ vào tháng 12",
            style: "Thân mật (Informal Letter)",
            requirements: "Nơi ở, món ăn, điểm tham quan, trang phục"
        },
        hints: [
            {
                title: "1. Where to stay (Nơi ở)",
                type: "standard",
                items: [
                    {
                        en: "stay at a hotel in the city centre",
                        vi: "ở khách sạn tại trung tâm thành phố",
                        reasonEn: "because it is convenient to travel around the city.",
                        reasonVi: "vì thuận tiện để đi lại trong thành phố."
                    },
                    {
                        en: "stay at a hotel near Ninh Kieu Wharf",
                        vi: "ở khách sạn gần Bến Ninh Kiều",
                        reasonEn: "because you can easily visit many famous restaurants and cafes in the evening.",
                        reasonVi: "vì bạn có thể dễ dàng ghé thăm nhiều nhà hàng và quán cà phê nổi tiếng vào buổi tối."
                    },
                    {
                        en: "choose a hotel with good reviews",
                        vi: "chọn khách sạn có đánh giá tốt",
                        reasonEn: "because you can enjoy better services and reasonable prices.",
                        reasonVi: "vì bạn có thể tận hưởng dịch vụ tốt hơn và giá cả hợp lý."
                    }
                ]
            },
            {
                title: "2. What dishes to try (Món ăn)",
                type: "standard",
                items: [
                    {
                        en: "try local dishes such as Vietnamese pancake (banh xeo) and grilled pork noodles",
                        vi: "thử các món ăn địa phương như bánh xèo và bún thịt nướng",
                        reasonEn: "because they are very delicious and popular in the Mekong Delta.",
                        reasonVi: "vì chúng rất ngon và phổ biến ở vùng Đồng bằng sông Cửu Long."
                    },
                    {
                        en: "enjoy fresh tropical fruits",
                        vi: "thưởng thức các loại trái cây nhiệt đới tươi ngon",
                        reasonEn: "because they are fresh, sweet, and affordable.",
                        reasonVi: "vì chúng tươi, ngọt và giá cả rất phải chăng."
                    },
                    {
                        en: "taste grilled snakehead fish (ca loc nuong trui)",
                        vi: "thưởng thức món cá lóc nướng trui",
                        reasonEn: "because this is a famous specialty of the southwestern region of Vietnam.",
                        reasonVi: "vì đây là một đặc sản nổi tiếng của miền Tây Nam Bộ."
                    }
                ]
            },
            {
                title: "3. Which tourist attractions to visit (Điểm tham quan)",
                type: "standard",
                items: [
                    {
                        en: "take a boat trip to Cai Rang Floating Market",
                        vi: "đi thuyền tham quan Chợ nổi Cái Răng",
                        reasonEn: "because you can experience the unique daily life of local people on the river.",
                        reasonVi: "vì bạn có thể trải nghiệm cuộc sống thường ngày độc đáo của người dân trên sông."
                    },
                    {
                        en: "visit Binh Thuy Ancient House",
                        vi: "ghé thăm Nhà cổ Bình Thủy",
                        reasonEn: "because you can learn about traditional architecture and local history.",
                        reasonVi: "vì bạn có thể tìm hiểu về kiến trúc truyền thống và lịch sử địa phương."
                    },
                    {
                        en: "take a walk along Ninh Kieu Pedestrian Bridge in the evening",
                        vi: "đi dạo dọc Cầu đi bộ Ninh Kiều vào buổi tối",
                        reasonEn: "because you can take beautiful photos and enjoy the fresh air.",
                        reasonVi: "vì bạn có thể chụp những bức ảnh đẹp và tận hưởng không khí trong lành."
                    }
                ]
            },
            {
                title: "4. What to wear (Trang phục)",
                type: "standard",
                items: [
                    {
                        en: "wear light and comfortable clothes",
                        vi: "mặc quần áo mỏng nhẹ và thoải mái",
                        reasonEn: "because the weather in Can Tho is warm and sunny during the day.",
                        reasonVi: "vì thời tiết ở Cần Thơ ban ngày khá ấm áp và nhiều nắng."
                    },
                    {
                        en: "bring a hat and sunglasses",
                        vi: "mang theo mũ và kính râm",
                        reasonEn: "because they help protect you from strong sunlight when traveling outdoors.",
                        reasonVi: "vì chúng giúp bảo vệ bạn khỏi ánh nắng gắt khi đi lại ngoài trời."
                    },
                    {
                        en: "wear comfortable walking shoes or sneakers",
                        vi: "đi giày đi bộ thoải mái hoặc giày thể thao",
                        reasonEn: "because you will walk and explore different places a lot.",
                        reasonVi: "vì bạn sẽ phải đi bộ và khám phá nhiều địa điểm khác nhau."
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

Chúc cậu mọi điều tốt lành,`
    },

    request: {
        title: "DẠNG 02: LETTER OF REQUEST (THƯ YÊU CẦU / HỎI THÔNG TIN)",
        prompt: `Your friend has just completed an English course at Rainbow Language Center and had a great experience. You are planning to study English as well and would like to know more about the course. Write a letter to your friend asking for more information about the course. In your email, you should ask about:
• The address of the center
• The tuition fee
• The teachers
• The training program
You should write at least 120 words. Do not include your name. Your response will be evaluated in terms of Task Fulfillment, Organization, Vocabulary, and Grammar.`,
        analysis: {
            recipient: "Bạn của bạn (Moonie / Peter / John)",
            purpose: "Hỏi thông tin về khóa học tiếng Anh tại Rainbow Language Center",
            style: "Thân mật (Informal Letter)",
            requirements: "Địa chỉ trung tâm, học phí, giáo viên, chương trình đào tạo"
        },
        hints: [
            {
                title: "1. The address of the center (Địa chỉ của trung tâm)",
                type: "custom_outline_choice",
                sentences: [
                    {
                        en: "I want to choose a center that is easy to get to.",
                        vi: "Mình muốn chọn một trung tâm dễ đi đến."
                    },
                    {
                        en: "It would be more convenient for me if the center was near my home.",
                        vi: "Sẽ thuận tiện hơn cho mình nếu trung tâm ở gần nhà."
                    },
                    {
                        en: "I want to make sure I can get there easily every day.",
                        vi: "Mình muốn đảm bảo rằng mình có thể dễ dàng đến đó mỗi ngày."
                    },
                    {
                        en: "A convenient location would help me save time when travelling.",
                        vi: "Một địa điểm thuận tiện sẽ giúp mình tiết kiệm thời gian đi lại."
                    },
                    {
                        en: "I want to know if/whether I can get there by motorbike.",
                        vi: "Mình cũng muốn biết liệu mình có thể đi xe máy đến đó không."
                    }
                ]
            },
            {
                title: "2. The tuition fee (Học phí)",
                type: "custom_outline_choice",
                sentences: [
                    {
                        en: "I need to know the cost before I decide to join the course.",
                        vi: "Mình cần biết chi phí trước khi quyết định tham gia khóa học."
                    },
                    {
                        en: "I want to make sure the course is suitable for my budget.",
                        vi: "Mình muốn đảm bảo khóa học phù hợp với ngân sách của mình."
                    },
                    {
                        en: "I also want to know if there are any discounts for students/ group registration.",
                        vi: "Mình cũng muốn biết liệu có giảm giá cho sinh viên/ đăng ký nhóm không."
                    },
                    {
                        en: "I need to prepare enough money for the whole course.",
                        vi: "Mình cần chuẩn bị đủ tiền cho toàn bộ khóa học."
                    },
                    {
                        en: "The tuition fee is important because I am still a student.",
                        vi: "Học phí quan trọng vì mình vẫn còn là sinh viên."
                    }
                ]
            },
            {
                title: "3. The teachers (Giáo viên)",
                type: "custom_outline_choice",
                sentences: [
                    {
                        en: "I would like to know if they are experienced and friendly.",
                        vi: "Mình muốn biết liệu họ có kinh nghiệm và thân thiện không."
                    },
                    {
                        en: "I want to learn from teachers who can explain things clearly.",
                        vi: "Mình muốn học từ những giáo viên có thể giải thích mọi thứ rõ ràng."
                    },
                    {
                        en: "Good teachers are important because I want to improve my English effectively.",
                        vi: "Giáo viên tốt rất quan trọng vì mình muốn cải thiện tiếng Anh hiệu quả."
                    },
                    {
                        en: "I would feel more comfortable learning with friendly teachers.",
                        vi: "Mình sẽ cảm thấy thoải mái hơn khi học với những giáo viên thân thiện."
                    },
                    {
                        en: "Experienced teachers can help students learn more effectively.",
                        vi: "Giáo viên có kinh nghiệm có thể giúp học viên học hiệu quả hơn."
                    }
                ]
            },
            {
                title: "4. The training program (Chương trình đào tạo)",
                type: "custom_outline_choice",
                sentences: [
                    {
                        en: "I want to know what skills the course focuses on.",
                        vi: "Mình muốn biết khóa học tập trung vào những kỹ năng nào."
                    },
                    {
                        en: "I would like to know what topics students will study.",
                        vi: "Mình muốn biết học viên sẽ học những chủ đề nào."
                    },
                    {
                        en: "It would be helpful to know the class schedule and course length.",
                        vi: "Sẽ hữu ích nếu biết lịch học và thời lượng khóa học."
                    },
                    {
                        en: "I want to make sure the program is suitable for my English level.",
                        vi: "Mình muốn đảm bảo chương trình phù hợp với trình độ tiếng Anh của mình."
                    },
                    {
                        en: "I also want to know if students have enough opportunities to practise English.",
                        vi: "Mình cũng muốn biết liệu học viên có đủ cơ hội để thực hành tiếng Anh không."
                    }
                ]
            }
        ],
        sampleModel: `Dear Moonie,

How are you? I hope you are doing well. I’m writing to ask for some information about the English course at Rainbow Language Center because I am planning to study English there soon.

First of all, could you tell me the address of the center? I want to know if it is near my house so that I can get there easily every day. In addition, I would like to know about the tuition fee for the course. I need to know the cost before I decide to join because I want to make sure it is suitable for my budget. Furthermore, can you tell me more about the teachers? Are they friendly and experienced? I want to learn from teachers who can explain things clearly. Finally, I was wondering if you could give me some details about the training program and class schedule. It would be helpful to know what skills the course focuses on.

I hope you can help me with this. Write back soon.

Best wishes,`,
        sampleModelVi: `Moonie thân mến,

Cậu khỏe không? Tớ hy vọng cậu vẫn khỏe. Tớ viết thư này để hỏi xin một vài thông tin về khóa học tiếng Anh tại Trung tâm Ngoại ngữ Rainbow vì tớ đang có kế hoạch học tiếng Anh ở đó sắp tới.

Trước hết, cậu có thể cho tớ biết địa chỉ của trung tâm không? Tớ muốn biết liệu nó có gần nhà tớ không để tớ có thể dễ dàng đến đó mỗi ngày. Ngoài ra, tớ muốn biết về học phí của khóa học. Tớ cần biết chi phí trước khi quyết định tham gia vì tớ muốn đảm bảo nó phù hợp với ngân sách của mình. Hơn nữa, cậu có thể kể thêm cho tớ về các giáo viên ở đó không? Họ có thân thiện và giàu kinh nghiệm không? Tớ muốn học từ những giáo viên có thể giải thích mọi thứ rõ ràng. Cuối cùng, tớ đang băn khoăn liệu cậu có thể cho tớ biết thêm chi tiết về chương trình đào tạo và lịch học không. Sẽ rất hữu ích nếu biết khóa học tập trung vào những kỹ năng nào.

Tớ hy vọng cậu có thể giúp tớ việc này. Hãy trả lời thư sớm nhé.

Chúc cậu mọi điều tốt lành,`
    }
};

function renderExtraPracticePanel(typeId) {
    const container = document.getElementById('extraPracticePanel');
    if (!container) return;

    const data = extraPracticeData[typeId];
    if (!data) {
        container.innerHTML = `
            <div class="content-block" style="text-align: center; padding: 40px 20px;">
                <i class="fa-solid fa-clock" style="font-size: 42px; color: var(--primary-light); margin-bottom: 16px;"></i>
                <h3 style="font-size: 18px; margin-bottom: 8px;">Đang cập nhật đề luyện tập thêm cho dạng thư này</h3>
                <p style="color: var(--text-muted);">Vui lòng chọn <strong>Dạng 01: Letter of Advice</strong> hoặc <strong>Dạng 02: Letter of Request</strong> để làm bài luyện tập.</p>
            </div>
        `;
        return;
    }

    let hintsHtml = data.hints.map(hint => {
        if (hint.type === "custom_outline_choice") {
            let sentHtml = hint.sentences.map(st => `
                <div style="margin-bottom: 10px; padding-left: 12px;">
                    <p style="margin-bottom: 2px;">• <strong>${st.en}</strong></p>
                    <p style="margin-bottom: 0; color: var(--text-muted); font-size: 13.5px;">(${st.vi})</p>
                </div>
            `).join('');

            return `
                <div class="outline-step" style="margin-bottom: 18px;">
                    <h4 style="margin-bottom: 12px; color: var(--accent-red); font-size: 17px;">${hint.title}</h4>
                    
                    <div style="margin-bottom: 14px; padding-left: 4px;">
                        <p style="font-weight: 700; color: var(--text-main); margin-bottom: 4px;">
                            Cấu trúc hỏi thông tin:
                        </p>
                        <p style="margin-bottom: 0; padding-left: 14px; color: var(--primary-color); font-style: italic; font-weight: 500;">
                            ↳ Tự chọn 1 cấu trúc ghép vô
                        </p>
                    </div>

                    <div style="padding-left: 4px;">
                        <p style="font-weight: 700; color: var(--text-main); margin-bottom: 8px;">
                            Câu mở rộng:
                        </p>
                        ${sentHtml}
                    </div>
                </div>
            `;
        } else {
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
        }
    }).join('');

    const promptBullets = data.prompt.split('\n').filter(l => l.startsWith('•')).map(l => `<li>${l.replace('•', '').trim()}</li>`).join('');
    const promptIntro = data.prompt.substring(0, data.prompt.indexOf('•')).trim();

    container.innerHTML = `
        <!-- Prompt Card (Using standard website style) -->
        <div class="sample-prompt-container">
            <div class="sample-prompt-header">
                <i class="fa-solid fa-file-circle-question"></i> ĐỀ BÀI (TOPIC PROMPT) - ${data.title}
            </div>
            <div class="sample-prompt-text">
                <p>${promptIntro.replace(/\n+/g, ' ')}</p>
                <ul>
                    ${promptBullets}
                </ul>
                <p style="margin-top: 10px; font-style: italic; color: var(--text-muted);">
                    <i class="fa-solid fa-triangle-exclamation" style="color: #f59e0b;"></i> You should write at least 120 words. Do not include your name. Your response will be evaluated in terms of Task Fulfillment, Organization, Vocabulary, and Grammar.
                </p>
            </div>
            <div class="sample-analysis-grid">
                <div class="sample-analysis-item">
                    <strong>Người nhận</strong>
                    <span>${data.analysis.recipient}</span>
                </div>
                <div class="sample-analysis-item">
                    <strong>Mục đích</strong>
                    <span>${data.analysis.purpose}</span>
                </div>
                <div class="sample-analysis-item">
                    <strong>Văn phong</strong>
                    <span>${data.analysis.style}</span>
                </div>
                <div class="sample-analysis-item">
                    <strong>Yêu cầu cốt lõi</strong>
                    <span>${data.analysis.requirements}</span>
                </div>
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
                <textarea id="extraWritingArea" placeholder="Dear friend,&#10;&#10;How are you? I hope you are doing well..." rows="12"></textarea>
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
    const count = text === '' ? 0 : text.split(/\s+/).length;
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

// --- Comprehensive Diagnostic Rules Engine ---
function diagnoseVstepErrors(rawText, promptData) {
    const errors = [];
    const lower = rawText.toLowerCase();

    // --- A. SALUTATION & GREETING ---
    if (/\bDear\s+[a-z]+/i.test(rawText)) {
        const m = rawText.match(/\bDear\s+([a-zA-Z]+)/);
        if (m && m[1][0] !== m[1][0].toUpperCase()) {
            errors.push({
                type: "Lời mở đầu (Chính tả)",
                category: "spelling",
                wrong: m[0],
                correct: `Dear ${m[1][0].toUpperCase() + m[1].slice(1)},`,
                reason: "Tên riêng của người nhận bắt buộc phải viết hoa chữ cái đầu và có dấu phẩy sau lời chào."
            });
        }
    }

    if (/\bThank\s+for\b/i.test(rawText) && !/\bThanks\s+for\b/i.test(rawText) && !/\bThank\s+you\s+for\b/i.test(rawText)) {
        errors.push({
            type: "Ngữ pháp / Lời mở đầu",
            category: "grammar",
            wrong: "Thank for your letter",
            correct: "Thanks for your letter / Thank you for your letter",
            reason: "Cụm từ cảm ơn mở thư đúng ngữ pháp phải có 's' ('Thanks for...') hoặc dùng 'Thank you for...'."
        });
    }

    if (/\bI('m| am)\s+write\b/i.test(rawText)) {
        errors.push({
            type: "Thì của động từ (Tenses)",
            category: "grammar",
            wrong: "I am write / I'm write",
            correct: "I am writing / I'm writing",
            reason: "Sau to be (am/is/are) trong thì hiện tại tiếp diễn phải dùng V-ing ('I am writing to...')."
        });
    }

    if (/\bhope\s+you\s+well\b/i.test(rawText) && !/\bhope\s+you\s+are\s+well\b/i.test(rawText) && !/\bhope\s+you\s+are\s+doing\s+well\b/i.test(rawText)) {
        errors.push({
            type: "Cấu trúc câu (Thiếu động từ)",
            category: "grammar",
            wrong: "hope you well",
            correct: "hope you are well / hope you are doing well",
            reason: "Thiếu to be 'are' hoặc trợ động từ: 'I hope you are well' hoặc 'I hope you are doing well'."
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

    // --- B. INDIRECT QUESTIONS (CÂU HỎI GIÁN TIẾP - ĐẶC TRƯNG THƯ REQUEST) ---
    const rIndirectInversion = /\b(tell\s+me|know|wondering|wonder)\s+(where\s+is|what\s+is|how\s+much\s+is|how\s+is|who\s+is)\s+([a-zA-Z\s]+?)([.?!,]|$)/gi;
    let mInd;
    while ((mInd = rIndirectInversion.exec(rawText)) !== null) {
        const lead = mInd[1];
        const whVerb = mInd[2].split(/\s+/);
        const whWord = whVerb[0];
        const verb = whVerb[1];
        const subject = mInd[3].trim();
        errors.push({
            type: "Cấu trúc câu hỏi gián tiếp",
            category: "grammar",
            wrong: mInd[0].trim(),
            correct: `${lead} ${whWord} ${subject} ${verb}`,
            reason: `Trong câu hỏi gián tiếp sau '${lead}', không đảo trợ động từ/to be lên trước chủ ngữ. Cấu trúc chuẩn là: '${whWord} + Chủ ngữ (${subject}) + Động từ (${verb})'.`
        });
    }

    // --- C. ARTICLES (A / AN / THE / ZERO ARTICLE) ---
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

    const rSingularItems = /\b(wear|bring|take|buy|choose|visit|rent|book|join|take)\s+(ba\s*ba\s+shirt|shirt|dress|hat|jacket|camera|conical\s+hat|umbrella|raincoat|room|hotel|homestay|taxi|bus|boat|museum|market|temple|pagoda|course|center)\b/gi;
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

    const rAndSingular = /\b(and|or)\s+(umbrella|raincoat|camera|hat|jacket|shirt|conical\s+hat|map|guide)\b/gi;
    let mAnd;
    while ((mAnd = rAndSingular.exec(rawText)) !== null) {
        const conj = mAnd[1];
        const noun = mAnd[2];
        const art = noun.toLowerCase().startsWith('u') ? 'an' : 'a';
        errors.push({
            type: "Mạo từ (Articles)",
            category: "article",
            wrong: mAnd[0],
            correct: `${conj} ${art} ${noun}`,
            reason: `Danh từ đếm được số ít '${noun}' sau liên từ '${conj}' cần mạo từ '${art}' (${conj} ${art} ${noun}).`
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

    if (/\bby\s+a\s+(bus|taxi|car|train|plane|boat|motorbike)\b/gi.test(rawText)) {
        const m = rawText.match(/\bby\s+a\s+(bus|taxi|car|train|plane|boat|motorbike)\b/i);
        if (m) {
            errors.push({
                type: "Mạo từ (Articles)",
                category: "article",
                wrong: m[0],
                correct: m[0].replace('by a ', 'by '),
                reason: `Khi chỉ phương tiện đi lại bằng cấu trúc 'by + phương tiện', không dùng mạo từ 'a/an' (${m[0].replace('by a ', 'by ')}).`
            });
        }
    }

    // --- D. UNCOUNTABLE NOUNS ---
    if (/\b(advices|an\s+advice)\b/gi.test(rawText)) {
        const m = rawText.match(/\b(advices|an\s+advice)\b/i);
        errors.push({
            type: "Danh từ không đếm được",
            category: "grammar",
            wrong: m ? m[0] : "advices",
            correct: "some advice / a piece of advice",
            reason: "'advice' là danh từ không đếm được, không thêm 's' và không dùng mạo từ 'an'."
        });
    }

    if (/\b(informations|an\s+information)\b/gi.test(rawText)) {
        const m = rawText.match(/\b(informations|an\s+information)\b/i);
        errors.push({
            type: "Danh từ không đếm được",
            category: "grammar",
            wrong: m ? m[0] : "informations",
            correct: "some information / a piece of information",
            reason: "'information' là danh từ không đếm được, không có dạng số nhiều 'informations'."
        });
    }

    if (/\bclothings\b/gi.test(rawText)) {
        errors.push({
            type: "Danh từ không đếm được",
            category: "grammar",
            wrong: "clothings",
            correct: "clothes / clothing",
            reason: "'clothing' không đếm được (không có 's'). Nếu muốn chỉ quần áo nói chung, hãy dùng 'clothes'."
        });
    }

    // --- E. PARTS OF SPEECH & CONFUSING WORDS ---
    if (/\bexperience\s+teachers\b/gi.test(rawText)) {
        errors.push({
            type: "Từ loại (Part of Speech)",
            category: "vocab",
            wrong: "experience teachers",
            correct: "experienced teachers",
            reason: "Cần dùng tính từ 'experienced' (giàu kinh nghiệm) để bổ nghĩa cho danh từ 'teachers'."
        });
    }

    if (/\bthe\s+cultural\s+of\b/gi.test(rawText)) {
        errors.push({
            type: "Từ loại (Part of Speech)",
            category: "vocab",
            wrong: "the cultural of Can Tho",
            correct: "the culture of Can Tho / the cultural identity of Can Tho",
            reason: "'cultural' là tính từ. Đứng sau mạo từ 'the' và trước 'of' bắt buộc phải dùng danh từ 'culture'."
        });
    }

    if (/\bvery\s+beauty\b/gi.test(rawText)) {
        errors.push({
            type: "Từ loại (Part of Speech)",
            category: "vocab",
            wrong: "very beauty",
            correct: "very beautiful",
            reason: "Sau phó từ 'very' bổ nghĩa cho địa điểm/cảnh quan phải dùng tính từ 'beautiful', không dùng danh từ 'beauty'."
        });
    }

    if (/\b(give|give you)\s+some\s+advise\b/gi.test(rawText)) {
        errors.push({
            type: "Cặp từ dễ nhầm lẫn",
            category: "vocab",
            wrong: "give you some advise",
            correct: "give you some advice",
            reason: "'advise' là động từ (khuyên bảo). Danh từ 'lời khuyên' phải viết là 'advice' (đuôi -ce)."
        });
    }

    if (/\bNinh\s+Kieu\s+way\b/gi.test(rawText)) {
        errors.push({
            type: "Dùng từ / Địa danh",
            category: "vocab",
            wrong: "Ninh Kieu way",
            correct: "Ninh Kieu Wharf / Ninh Kieu Pedestrian Bridge",
            reason: "Địa danh Bến Ninh Kiều dùng 'Wharf', Cầu đi bộ dùng 'Pedestrian Bridge', không dùng 'way'."
        });
    }

    // --- F. PREPOSITIONS & COLLOCATIONS ---
    if (/\bsuitable\s+with\b/gi.test(rawText)) {
        errors.push({
            type: "Giới từ đi kèm tính từ",
            category: "grammar",
            wrong: "suitable with",
            correct: "suitable for",
            reason: "'suitable' đi với giới từ 'for' (suitable for my budget / suitable for me)."
        });
    }

    if (/\bconvenient\s+with\s+me\b/gi.test(rawText)) {
        errors.push({
            type: "Giới từ đi kèm tính từ",
            category: "grammar",
            wrong: "convenient with me",
            correct: "convenient for me",
            reason: "'convenient' đi với giới từ 'for' (convenient for me)."
        });
    }

    if (/\bfocus\s+in\b/gi.test(rawText)) {
        errors.push({
            type: "Giới từ đi kèm động từ",
            category: "grammar",
            wrong: "focus in",
            correct: "focus on",
            reason: "Động từ 'focus' đi kèm giới từ 'on' (focus on skills)."
        });
    }

    if (/\b(on\s+December|at\s+December|on\s+January|on\s+February|on\s+June|on\s+July)\b/gi.test(rawText)) {
        const m = rawText.match(/\b(on|at)\s+(December|January|February|March|April|May|June|July|August|September|October|November)\b/i);
        if (m) {
            errors.push({
                type: "Giới từ chỉ thời gian",
                category: "grammar",
                wrong: m[0],
                correct: `in ${m[2]}`,
                reason: `Trước tháng (không có ngày cụ thể) bắt buộc phải dùng giới từ 'in' (ví dụ: in ${m[2]}).`
            });
        }
    }

    // --- G. VERB PATTERNS & ADVICE STRUCTURES ---
    if (/\bshould\s+to\s+[a-z]+\b/gi.test(rawText)) {
        const m = rawText.match(/\bshould\s+to\s+([a-z]+)\b/i);
        if (m) {
            errors.push({
                type: "Cấu trúc động từ khuyết thiếu",
                category: "grammar",
                wrong: m[0],
                correct: `should ${m[1]}`,
                reason: "Sau động từ khuyết thiếu 'should' là động từ nguyên thể không to (should + Vo)."
            });
        }
    }

    if (/\bwould\s+be\s+a\s+good\s+idea\s+(try|stay|visit|wear|bring|go|ask|join)\b/gi.test(rawText)) {
        const m = rawText.match(/\bwould\s+be\s+a\s+good\s+idea\s+([a-z]+)\b/i);
        if (m) {
            errors.push({
                type: "Cấu trúc khuyên bảo",
                category: "grammar",
                wrong: m[0],
                correct: `would be a good idea to ${m[1]}`,
                reason: "Cấu trúc chuẩn: 'It would be a good idea TO + Vo'."
            });
        }
    }

    if (/\bIf\s+I\s+was\s+you\b/gi.test(rawText)) {
        errors.push({
            type: "Câu điều kiện loại 2",
            category: "grammar",
            wrong: "If I was you",
            correct: "If I were you",
            reason: "Trong câu điều kiện loại 2 giả định lời khuyên, to be luôn dùng 'were' cho tất cả các ngôi."
        });
    }

    // --- H. SENTENCE STRUCTURE & CONJUNCTIONS ---
    if (/the weather in Can Tho can be very pleasant in December and an ideal time/i.test(rawText)) {
        errors.push({
            type: "Cấu trúc câu (Sentence Structure)",
            category: "grammar",
            wrong: "...because the weather in Can Tho can be very pleasant in December and an ideal time for tourism.",
            correct: "...because the weather in Can Tho is very pleasant in December, making it an ideal time for tourism (hoặc: and December is an ideal time for tourism).",
            reason: "Lỗi cấu trúc câu không song hành: 'weather' (thời tiết) không thể là 'an ideal time' (khoảng thời gian). Cần dùng mệnh đề phân từ 'making it an ideal time' hoặc tách mệnh đề."
        });
    }

    if (/\bAlthough\b[^.!?\n]+,\s*but\b/gi.test(rawText)) {
        errors.push({
            type: "Cấu trúc liên từ kép",
            category: "grammar",
            wrong: "Although ..., but ...",
            correct: "Although ... [không dùng 'but'] (hoặc chỉ dùng '... but ...')",
            reason: "Trong tiếng Anh không dùng song song 'Although' và 'but' trong cùng một câu."
        });
    }

    if (/\bBecause\b[^.!?\n]+,\s*so\b/gi.test(rawText)) {
        errors.push({
            type: "Cấu trúc liên từ kép",
            category: "grammar",
            wrong: "Because ..., so ...",
            correct: "Because ... [không dùng 'so'] (hoặc chỉ dùng '... so ...')",
            reason: "Trong tiếng Anh không dùng song song 'Because' và 'so' trong cùng một câu."
        });
    }

    // Missing comma after transition words
    const transitions = [
        "Firstly", "Secondly", "Finally", "Moreover", "Besides",
        "Furthermore", "In addition", "Therefore", "For example", "However", "First of all"
    ];
    transitions.forEach(tr => {
        const reg = new RegExp(`(^|[.!?]\\s+)${tr}\\s+([a-zA-Z])`, 'g');
        let match;
        while ((match = reg.exec(rawText)) !== null) {
            errors.push({
                type: "Dấu câu sau liên từ nối",
                category: "punctuation",
                wrong: `${tr} ${match[2]}...`,
                correct: `${tr}, ${match[2]}...`,
                reason: `Sau trạng từ/liên từ chuyển ý đứng đầu câu '${tr}' bắt buộc phải có dấu phẩy.`
            });
        }
    });

    // --- I. SUBJECT-VERB AGREEMENT & COMMON SPELLINGS ---
    if (/\b(places|dishes|clothes|teachers|skills|topics)\s+is\b/gi.test(rawText)) {
        const m = rawText.match(/\b(places|dishes|clothes|teachers|skills|topics)\s+is\b/i);
        if (m) {
            errors.push({
                type: "Hòa hợp Chủ - Vị",
                category: "grammar",
                wrong: m[0],
                correct: m[0].replace('is', 'are'),
                reason: `Chủ ngữ số nhiều '${m[1]}' phải đi kèm động từ to be 'are'.`
            });
        }
    }

    const rLowerI = /(^|\s)i\s+(am|hope|think|want|would|will|can|suggest|recommend|need|also)\b/g;
    let mLowerI;
    while ((mLowerI = rLowerI.exec(rawText)) !== null) {
        errors.push({
            type: "Chính tả / Viết hoa",
            category: "spelling",
            wrong: `i ${mLowerI[2]}`,
            correct: `I ${mLowerI[2]}`,
            reason: "Đại từ nhân xưng 'I' (tôi) luôn luôn phải viết hoa trong tiếng Anh."
        });
    }

    const spellingDict = {
        "recieve": "receive",
        "untill": "until",
        "beautifull": "beautiful",
        "restuarant": "restaurant",
        "resturant": "restaurant",
        "delicous": "delicious",
        "alot": "a lot",
        "convinient": "convenient",
        "unconvinient": "inconvenient",
        "differnt": "different",
        "informashun": "information",
        "tomorow": "tomorrow",
        "seperate": "separate",
        "truely": "truly",
        "writting": "writing",
        "succesful": "successful",
        "enviroment": "environment",
        "trafic": "traffic",
        "oppurtunity": "opportunity",
        "definitly": "definitely",
        "pleasent": "pleasant",
        "floting": "floating",
        "villige": "village",
        "tutition": "tuition",
        "tution": "tuition",
        "schedul": "schedule",
        "materiels": "materials",
        "curiculum": "curriculum"
    };

    Object.keys(spellingDict).forEach(wrongWord => {
        const rWord = new RegExp(`\\b${wrongWord}\\b`, 'gi');
        let mW;
        while ((mW = rWord.exec(rawText)) !== null) {
            errors.push({
                type: "Lỗi chính tả (Spelling)",
                category: "spelling",
                wrong: mW[0],
                correct: spellingDict[wrongWord],
                reason: `Viết sai chính tả từ '${mW[0]}'. Cách viết đúng là '${spellingDict[wrongWord]}'.`
            });
        }
    });

    const punctSpacingErrors = rawText.match(/[a-zA-Z0-9]+[.,!?:;][a-zA-Z]+/g);
    if (punctSpacingErrors && punctSpacingErrors.length > 0) {
        punctSpacingErrors.forEach(pe => {
            errors.push({
                type: "Quy cách dấu câu",
                category: "punctuation",
                wrong: pe,
                correct: pe.replace(/([.,!?:;])/, '$1 '),
                reason: "Sau dấu câu bắt buộc phải có 1 khoảng trắng (dấu cách) trước khi viết từ tiếp theo."
            });
        });
    }

    const spaceBeforePunct = rawText.match(/[a-zA-Z0-9]+\s+[.,!?:;]/g);
    if (spaceBeforePunct && spaceBeforePunct.length > 0) {
        spaceBeforePunct.forEach(se => {
            errors.push({
                type: "Quy cách dấu câu",
                category: "punctuation",
                wrong: se,
                correct: se.replace(/\s+([.,!?:;])/, '$1'),
                reason: "Không đặt dấu cách trước các dấu chấm, phẩy, chấm hỏi, chấm than."
            });
        });
    }

    return errors;
}

// Construct inline annotated essay HTML
function buildAnnotatedEssayHtml(rawText, errors) {
    if (!rawText) return '';
    let annotated = rawText;

    const sortedErrors = [...errors].sort((a, b) => (b.wrong ? b.wrong.length : 0) - (a.wrong ? a.wrong.length : 0));

    sortedErrors.forEach(err => {
        if (!err.wrong || err.wrong.length < 2) return;
        const escaped = err.wrong.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
        const reg = new RegExp(escaped, 'gi');
        annotated = annotated.replace(reg, `<span class="annotated-box"><del class="annotated-wrong">${err.wrong}</del> <ins class="annotated-correct"><i class="fa-solid fa-arrow-right"></i> ${err.correct}</ins></span>`);
    });

    const paras = annotated.split(/\n+/).filter(p => p.trim() !== '');
    return paras.map(p => `<p class="annotated-para">${p.trim()}</p>`).join('');
}

// Grade and Evaluate Extra Practice Submission
function gradeExtraPractice(typeId) {
    const writingArea = document.getElementById('extraWritingArea');
    const resultCard = document.getElementById('extraResultCard');
    if (!writingArea || !resultCard) return;

    const rawText = writingArea.value.trim();
    if (!rawText) {
        alert('Vui lòng nhập bài viết của bạn trước khi nộp bài!');
        writingArea.focus();
        return;
    }

    const words = rawText.split(/\s+/).filter(w => w !== '');
    const wordCount = words.length;

    // --- 1. TASK FULFILMENT (Thang 10) ---
    const lower = rawText.toLowerCase();
    let hasReq1 = false, hasReq2 = false, hasReq3 = false, hasReq4 = false;
    let reqLabels = [];

    if (typeId === 'request') {
        hasReq1 = /(address|location|where\s+(is\s+)?the\s+center|near\s+my\s+(house|home)|street|district|easy\s+to\s+get|located)/i.test(lower);
        hasReq2 = /(fee|tuition|cost|price|money|how\s+much|budget|discount|pay)/i.test(lower);
        hasReq3 = /(teacher|teachers|instructor|friendly|experienced|teach|explain)/i.test(lower);
        hasReq4 = /(program|training|course|curriculum|skill|skills|schedule|length|study|practise|practice|topic|topics)/i.test(lower);
        reqLabels = [
            hasReq1 ? '✓ Địa chỉ' : '✗ Địa chỉ',
            hasReq2 ? '✓ Học phí' : '✗ Học phí',
            hasReq3 ? '✓ Giáo viên' : '✗ Giáo viên',
            hasReq4 ? '✓ Chương trình đào tạo' : '✗ Chương trình đào tạo'
        ];
    } else {
        // Default: advice
        hasReq1 = /(stay|hotel|homestay|room|guest\s*house|resort|city\s*cent)/i.test(lower);
        hasReq2 = /(dish|dishes|food|pancake|banh\s*xeo|lau\s*mam|fish|fruit|fruits|eat|taste|try|specialt)/i.test(lower);
        hasReq3 = /(attraction|visit|place|market|ninh\s*kieu|cai\s*rang|floating|ancient\s*house|village|tourist|pagoda|temple)/i.test(lower);
        hasReq4 = /(wear|clothes|cloth|jacket|umbrella|hat|sunglass|shoes|sneaker|raincoat|t-shirt|shorts|dress)/i.test(lower);
        reqLabels = [
            hasReq1 ? '✓ Nơi ở' : '✗ Nơi ở',
            hasReq2 ? '✓ Món ăn' : '✗ Món ăn',
            hasReq3 ? '✓ Điểm tham quan' : '✗ Điểm tham quan',
            hasReq4 ? '✓ Trang phục' : '✗ Trang phục'
        ];
    }

    let bulletsCount = (hasReq1 ? 1 : 0) + (hasReq2 ? 1 : 0) + (hasReq3 ? 1 : 0) + (hasReq4 ? 1 : 0);

    let tfScore = 8.5;
    if (bulletsCount === 4) {
        tfScore = wordCount >= 120 ? 8.5 : 7.0;
    } else if (bulletsCount === 3) {
        tfScore = wordCount >= 120 ? 7.0 : 6.0;
    } else if (bulletsCount === 2) {
        tfScore = 5.5;
    } else {
        tfScore = 4.0;
    }

    // --- 2. ORGANIZATION (Thang 10) ---
    const hasGreeting = /^dear\s+[a-z]+/i.test(rawText.trim());
    const hasOpening = /(thanks?\s+for|hope\s+you|writing\s+to|how\s+are\s+you)/i.test(lower);
    const hasClosingSentence = /(hope\s+my\s+advice|write\s+back|let\s+me\s+know|look\s+forward|hope\s+you\s+can\s+help)/i.test(lower);
    const hasSignOff = /(best\s+wishes|yours|regards|love)/i.test(lower);

    const linkingWords = ["firstly", "secondly", "next", "finally", "moreover", "besides", "furthermore", "in addition", "therefore", "for example", "first of all", "also", "because"];
    let linkCount = 0;
    linkingWords.forEach(lw => {
        if (lower.includes(lw)) linkCount++;
    });

    let orgScore = 8.0;
    if (hasGreeting && hasOpening && hasClosingSentence && hasSignOff && linkCount >= 4) {
        orgScore = 8.5;
    } else if (linkCount >= 3) {
        orgScore = 7.5;
    } else if (linkCount >= 1) {
        orgScore = 6.5;
    } else {
        orgScore = 5.5;
    }

    // --- 3. DIAGNOSE ERRORS FOR VOCABULARY & GRAMMAR ---
    const errors = diagnoseVstepErrors(rawText, extraPracticeData[typeId]);
    const vocabErrors = errors.filter(e => e.category === 'vocab');
    const grammarErrors = errors.filter(e => e.category === 'grammar' || e.category === 'article');

    // --- 4. VOCABULARY (Thang 10) ---
    let vocScore = 7.5;
    if (vocabErrors.length >= 3) {
        vocScore = 5.5;
    } else if (vocabErrors.length === 2) {
        vocScore = 6.0;
    } else if (vocabErrors.length === 1) {
        vocScore = 6.5;
    } else {
        vocScore = 7.5;
    }

    // --- 5. GRAMMAR & ACCURACY (Thang 10) ---
    let gramScore = 7.0;
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

    let convertedScore = Math.round((overallBand / 10.0) * 3.0 * 100) / 100;

    let tfConv = Math.round((tfScore / 10.0) * 0.75 * 100) / 100;
    let orgConv = Math.round((orgScore / 10.0) * 0.75 * 100) / 100;
    let vocConv = Math.round((vocScore / 10.0) * 0.75 * 100) / 100;
    let gramConv = Math.round((gramScore / 10.0) * 0.75 * 100) / 100;

    let vstepLevel = "B1 LEVEL (ĐẠT CHUẨN)";
    let levelDesc = "Bài viết đáp ứng đầy đủ yêu cầu đề bài, cấu trúc đoạn rõ ràng. Tuy nhiên còn một số lỗi ngữ pháp, mạo từ và dùng từ cần lưu ý sửa chữa.";
    if (overallBand >= 8.5) {
        vstepLevel = "B2 LEVEL (XUẤT SẮC - VƯỢT CHUẨN)";
        levelDesc = "Bài viết rất ấn tượng! Bố cục chuẩn mực 5 bước, từ vựng và ngữ pháp đa dạng, hầu như không có lỗi sai.";
    } else if (overallBand < 6.0) {
        vstepLevel = "DƯỚI CHUẨN B1 (CẦN CẢI THIỆN)";
        levelDesc = "Bài viết còn nhiều lỗi ngữ pháp hoặc chưa đủ số từ (yêu cầu ≥ 120 từ). Hãy xem kỹ bảng sửa lỗi và bài mẫu bên dưới nhé!";
    }

    const data = extraPracticeData[typeId];

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
                <td style="font-size: 13.5px; color: var(--text-main); line-height: 1.5;">${err.reason}</td>
            </tr>
        `).join('');

        errorTableHtml = `
            <div class="extra-error-table-wrapper" style="margin-top: 25px;">
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
            <div class="highlight-box" style="margin-top: 25px;">
                <p><i class="fa-solid fa-circle-check" style="color: #10b981;"></i> <strong>Không phát hiện lỗi ngữ pháp hay từ vựng đáng kể nào!</strong> Bài làm của bạn rất chuẩn chỉnh và mạch lạc.</p>
            </div>
        `;
    }

    // Build Results HTML
    resultCard.innerHTML = `
        <h3><i class="fa-solid fa-square-poll-vertical"></i> KẾT QUẢ ĐÁNH GIÁ & CHẤM ĐIỂM CHI TIẾT</h3>

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
                    ${reqLabels.join(' | ')}.
                    Độ dài: ${wordCount >= 120 ? 'Đạt chuẩn (≥120 từ)' : 'Chưa đủ từ'}.
                </div>
            </div>
            <div class="criterion-card">
                <div class="criterion-name">
                    <span>Organization (30%)</span>
                    <span class="criterion-score">${orgConv.toFixed(2)}/0.75 <small style="font-size: 11px; font-weight: normal; color: var(--text-muted);">(${orgScore.toFixed(1)}/10)</small></span>
                </div>
                <div class="criterion-desc">
                    Bố cục 5 phần hoàn chỉnh. Sử dụng linh hoạt các liên từ nối chuyển tiếp câu.
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
                    Áp dụng tốt cấu trúc câu chuẩn B1. ${totalGrammarCount > 0 ? `Bị trừ điểm do mắc ${totalGrammarCount} lỗi ngữ pháp/mạo từ/câu ghép.` : 'Ngữ pháp chuẩn xác.'}
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
        <div class="content-block" style="margin-top: 35px;">
            <h3><i class="fa-solid fa-award"></i> BÀI VIẾT MẪU CHUẨN B1 THAM KHẢO (MODEL LETTER)</h3>
            <div class="sample-letter-box">
                ${data.sampleModel.replace(/\n\n/g, '<br><br>').replace(/\n/g, '<br>')}
            </div>

            <h3 style="margin-top: 25px;">BẢN DỊCH CHI TIẾT</h3>
            <div class="translation-box" style="background-color: var(--bg-main); border: 1px solid var(--border-color); padding: 20px; border-radius: 12px; margin-top: 15px; font-family: var(--font-body); line-height: 1.8; color: var(--text-muted); font-style: italic;">
                ${data.sampleModelVi.replace(/\n\n/g, '<br><br>').replace(/\n/g, '<br>')}
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

    const data = extraPracticeData[typeId];
    const typeTitle = data ? data.title : 'Bài Luyện Tập Thêm';
    const now = new Date().toLocaleString('vi-VN');
    const cleanSnippet = studentText.replace(/\s+/g, ' ').substring(0, 120);

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
    f.write(pure_extra_code.strip() + "\n")

print("Updated Dạng 02 hints to show exact student choice prompt format!")
