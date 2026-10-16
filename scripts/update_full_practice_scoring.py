# -*- coding: utf-8 -*-
import os

dom_path = "/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/dom_logic_full.js"

with open(dom_path, "r", encoding="utf-8") as f:
    dom_code = f.read()

# The Official VSTEP Rubric Descriptors and Evaluation Code
scoring_engine_code = r'''
// =========================================================================
// OFFICIAL VSTEP WRITING TASK 1 SCORING GUIDE & EVALUATION ENGINE
// (Based on Ministry of Education and Training Rating Scale - media_1787637818545.jpg)
// =========================================================================

const VSTEP_OFFICIAL_RUBRIC = {
    taskFulfilment: {
        10: {
            en: "Covers all the requirements of the task effectively; effectively fulfills all communicative purpose(s), with tone consistent and appropriate; fully develops key points with all the details relevant.",
            vi: "Đáp ứng xuất sắc và toàn diện mọi yêu cầu của đề bài; đạt trọn vẹn mục đích giao tiếp với văn phong hoàn toàn nhất quán, phù hợp; phát triển đầy đủ các ý chính với chi tiết xác đáng."
        },
        9: {
            en: "Covers all the requirements of the task effectively; effectively fulfills all communicative purpose(s), with tone consistent and appropriate; fully develops key points with all the details generally relevant.",
            vi: "Đáp ứng hiệu quả tất cả yêu cầu của đề; thực hiện tốt mục đích giao tiếp, văn phong nhất quán và chuẩn mực; phát triển đầy đủ các ý chính với các chi tiết nhìn chung rất phù hợp."
        },
        8: {
            en: "Covers all the requirements of the task; presents generally clear communicative purpose(s), with one or two minor inconsistencies and inappropriacies in tone; develops key points with most of the detail generally relevant; one/two of the points could be more fully extended.",
            vi: "Đáp ứng đầy đủ các yêu cầu của đề; mục đích giao tiếp rõ ràng, chỉ có 1-2 điểm nhỏ chưa hoàn toàn nhất quán về giọng văn; phát triển các ý chính với chi tiết phù hợp."
        },
        7: {
            en: "Covers all the requirements of the tasks; the format may be inappropriate in places; presents generally clear communicative purpose(s), with some inconsistencies and inappropriacies in tone; adequately presents key points, but one or two details may be inappropriate.",
            vi: "Bao quát được các yêu cầu của đề; thể thức có thể chưa thật chuẩn ở một vài chỗ; mục đích giao tiếp tương đối rõ ràng; trình bày đầy đủ các ý chính nhưng có thể có 1-2 chi tiết chưa tối ưu."
        },
        6: {
            en: "Covers almost all the requirements of the tasks; the format may be inappropriate in places; presents generally clear communicative purpose(s), with some inconsistencies and inappropriacies in tone; adequately presents key points, but a few details may be inappropriate.",
            vi: "Đáp ứng hầu hết các yêu cầu của đề; mục đích giao tiếp cơ bản rõ ràng nhưng văn phong còn đôi chỗ chưa chuẩn; nêu được các ý chính nhưng một vài chi tiết chưa thật sát."
        },
        5: {
            en: "Partially covers the requirements of the tasks; presents communicative purpose(s), which are unclear in places; there are some inconsistencies and inappropriacies in tone; inadequately presents key points; there may be a tendency to focus on details.",
            vi: "Chỉ đáp ứng được một phần yêu cầu của đề; mục đích giao tiếp chưa rõ ràng ở một số vị trí; chưa phát triển đầy đủ các ý chính hoặc tập trung quá nhiều vào chi tiết phụ."
        },
        4: {
            en: "Partially covers the requirements of the tasks; fails to clearly presents communicative purpose(s); the tone may be inappropriate; may confuse key points; some parts may be unclear, irrelevant or repetitive.",
            vi: "Chỉ giải quyết được một phần đề; chưa làm rõ mục đích giao tiếp; giọng văn chưa phù hợp; các ý chính bị nhầm lẫn hoặc lặp ý, thiếu mạch lạc."
        },
        3: {
            en: "Does not address any part of the task; presents limited ideas which may be largely irrelevant/repetitive.",
            vi: "Hầu như không giải quyết được yêu cầu đề bài; ý tưởng rất hạn chế, lặp lại hoặc lạc đề."
        },
        2: {
            en: "Does not address any part of the task.",
            vi: "Không giải quyết được phần nào của đề bài."
        },
        1: {
            en: "Answer is totally irrelevant or incomprehensible.",
            vi: "Bài viết hoàn toàn lạc đề hoặc không thể hiểu được."
        },
        0: {
            en: "Does not attend the exam / does not write any words / writes only a memorized response.",
            vi: "Không làm bài / không có nội dung hoặc chỉ chép lại đoạn văn học vẹt không liên quan."
        }
    },
    organization: {
        10: {
            en: "Organizes information and ideas logically; uses a variety as well as a range of cohesive devices and organizational patterns flexibly; uses paragraphing sufficiently and appropriately.",
            vi: "Tổ chức thông tin và ý tưởng hoàn toàn logic; sử dụng đa dạng và linh hoạt các phương tiện liên kết và mô thức tổ chức đoạn; phân đoạn chuẩn mực, hợp lý."
        },
        9: {
            en: "Organizes information and ideas coherently; uses a variety as well as a range of cohesive devices and organizational patterns effectively; uses paragraphing sufficiently and appropriately.",
            vi: "Tổ chức thông tin mạch lạc, rõ ràng; vận dụng hiệu quả nhiều phương tiện liên kết và cấu trúc đoạn; phân chia đoạn văn hợp lý."
        },
        8: {
            en: "Organizes information and ideas coherently; uses a range of linking words and cohesive devices appropriately, though there may be some under/over use.",
            vi: "Tổ chức ý tưởng mạch lạc; sử dụng tương đối tốt các từ nối và phương tiện liên kết, dù đôi khi còn dùng hơi ít hoặc hơi lạm dụng."
        },
        7: {
            en: "Organizes information and ideas coherently; uses a variety of linking words appropriately and a number of cohesive devices accurately within and across sentences, but there may be occasional inappropriacies.",
            vi: "Bố cục mạch lạc; sử dụng chuẩn xác nhiều từ nối trong câu và giữa các câu, dù đôi khi còn một vài liên từ dùng chưa tự nhiên."
        },
        6: {
            en: "Organizes information and ideas generally coherently; uses linking words and a limited number of cohesive devices within and across sentences accurately, but there are some inappropriacies.",
            vi: "Ý tưởng nhìn chung có tính liên kết; sử dụng được các từ nối cơ bản trong và giữa các câu, nhưng số lượng từ liên kết còn hạn chế."
        },
        5: {
            en: "Organizes information and ideas fairly coherently; uses linking words and some familiar cohesive devices within and across sentences accurately, though there may be inaccuracies.",
            vi: "Bố cục tương đối mạch lạc; sử dụng một số từ nối quen thuộc nhưng đôi chỗ còn thiếu chính xác hoặc thiếu tự nhiên."
        },
        4: {
            en: "Presents information and ideas with some organization; uses linking words accurately and attempts a few familiar cohesive devices within and across sentences though there are repetitions and inaccuracies.",
            vi: "Có cố gắng tổ chức ý nhưng còn rời rạc; từ nối dùng lặp lại nhiều lần hoặc chưa chuẩn xác."
        },
        3: {
            en: "Presents information and ideas in a series of simple sentences linked by only basic, high frequency linking words.",
            vi: "Trình bày thông tin dưới dạng các câu đơn rời rạc, chỉ dùng các từ nối quá cơ bản (and, but, so)."
        },
        2: {
            en: "Has very little control of organizational features.",
            vi: "Rất ít hoặc không kiểm soát được cấu trúc và bố cục bài viết."
        },
        1: {
            en: "Has no organizational features.",
            vi: "Hoàn toàn không có tính tổ chức hay bố cục đoạn."
        },
        0: {
            en: "Does not attend / no response.",
            vi: "Không có bài làm."
        }
    },
    vocabulary: {
        10: {
            en: "Uses a wide range of vocabulary including some less common lexis precisely and flexibly; shows full control of style and collocation, but there may be occasional inaccuracies; errors are very rare with just one or two minor slips.",
            vi: "Vốn từ rất phong phú, sử dụng chính xác và linh hoạt các từ vựng nâng cao; kiểm soát tốt phong cách và kết hợp từ (collocations); lỗi sai cực kỳ hiếm gặp."
        },
        9: {
            en: "Uses a wide range of vocabulary including some less common lexis precisely; shows good control of style and collocation, but there may be some inaccuracies; errors, if present, are non-systematic and non-impeding.",
            vi: "Vốn từ rộng, dùng chính xác từ vựng theo chủ đề; kiểm soát tốt kết hợp từ; nếu có lỗi thì chỉ là lỗi nhỏ, không mang tính hệ thống và không cản trở việc hiểu."
        },
        8: {
            en: "Uses a good range of vocabulary including some less common lexis appropriately; shows some control of style and collocation; errors, if present, are non-systematic and non-impeding.",
            vi: "Sử dụng vốn từ tốt, dùng đúng ngữ cảnh một số từ vựng nâng cao; có kiểm soát phong cách từ; lỗi từ vựng không gây khó hiểu cho người đọc."
        },
        7: {
            en: "Uses a sufficient range of vocabulary; attempts less common lexis with occasional inappropriacies; errors do not impede communication.",
            vi: "Vốn từ đầy đủ đáp ứng yêu cầu đề; có nỗ lực dùng từ vựng theo chủ đề dù đôi khi còn dùng chưa chuẩn; các lỗi từ vựng không cản trở giao tiếp."
        },
        6: {
            en: "Uses a sufficient range of vocabulary; attempts less common lexis but most are faulty; errors do not impede communication.",
            vi: "Vốn từ đủ dùng cho B1; có thử dùng từ nâng cao nhưng phần lớn chưa chính xác; tuy vậy lỗi không cản trở việc truyền đạt thông điệp chính."
        },
        5: {
            en: "Uses an adequate range of vocabulary but tends to overuse certain lexical items; errors occur and may impede comprehension at times.",
            vi: "Vốn từ ở mức vừa phải nhưng lặp từ nhiều; mắc một số lỗi dùng từ đôi khi làm người đọc khó hiểu."
        },
        4: {
            en: "Uses basic vocabulary and acceptable control; errors are noticeable and impede comprehension at times.",
            vi: "Chỉ dùng từ vựng sơ cấp; lỗi dùng từ và chính tả xuất hiện rõ rệt, cản trở việc đọc hiểu ở nhiều chỗ."
        },
        3: {
            en: "Uses a limited range of basic vocabulary; errors are frequent and distort the meaning.",
            vi: "Vốn từ rất hạn hẹp; lỗi từ vựng xuất hiện liên tục và làm sai lệch ý nghĩa muốn diễn đạt."
        },
        2: {
            en: "Uses a very limited range of words and phrases; errors are dominant and distort the meaning.",
            vi: "Vốn từ cực kỳ nghèo nàn; lỗi sai chiếm ưu thế và làm sai lệch hoàn toàn nội dung."
        },
        1: {
            en: "Uses only a few isolated words.",
            vi: "Chỉ viết được một vài từ rời rạc."
        },
        0: {
            en: "Does not attend / no response.",
            vi: "Không có bài làm."
        }
    },
    grammar: {
        10: {
            en: "Uses a wide range of simple and complex structures precisely and flexibly; errors are very rare with just one or two minor slips.",
            vi: "Sử dụng rất đa dạng, chính xác và linh hoạt cả câu đơn và câu phức; lỗi ngữ pháp cực kỳ hiếm, chỉ là sơ suất nhỏ."
        },
        9: {
            en: "Uses a wide range of simple and complex structures precisely; the majority of the sentences are error-free; errors, if present, are non-systematic and non-impeding.",
            vi: "Vận dụng chuẩn xác nhiều cấu trúc câu đơn và câu phức; phần lớn các câu hoàn toàn không có lỗi; nếu có lỗi chỉ là không đáng kể."
        },
        8: {
            en: "Uses a variety of simple and complex structures with good control; the majority of the sentences are error-free; errors, if present, are non-systematic and non-impeding.",
            vi: "Kết hợp tốt câu đơn và câu phức; đa số các câu đúng ngữ pháp; các lỗi nhỏ không mang tính hệ thống và không cản trở việc hiểu."
        },
        7: {
            en: "Uses both simple and complex structures in a relatively effective way; errors occur but they rarely lead to misunderstanding.",
            vi: "Sử dụng tương đối hiệu quả cả câu đơn và câu phức; có lỗi ngữ pháp xuất hiện nhưng hiếm khi gây hiểu lầm."
        },
        6: {
            en: "Uses simple structures and attempts some complex structures; errors occur but they rarely lead to misunderstanding.",
            vi: "Kiểm soát tốt câu đơn và có cố gắng viết câu phức; có mắc lỗi ngữ pháp nhưng nhìn chung không cản trở việc hiểu nội dung."
        },
        5: {
            en: "Shows good control of simple structures; attempts complex structures, but most are faulty; errors occur but normally they do not impede comprehension.",
            vi: "Kiểm soát tốt các câu đơn giản; có thử viết câu phức nhưng hầu hết bị sai cấu trúc; lỗi không cản trở hoàn toàn việc đọc hiểu."
        },
        4: {
            en: "Shows adequate control of simple structures; attempts complex structures, but unsuccessfully; errors occur frequently and impede comprehension at times.",
            vi: "Chỉ kiểm soát được câu đơn giản ở mức vừa phải; câu phức hầu như thất bại; lỗi ngữ pháp xuất hiện thường xuyên, đôi khi gây khó hiểu."
        },
        3: {
            en: "Uses some simple structures correctly; frequently makes basic errors that distort the meaning.",
            vi: "Chỉ đúng được một vài câu đơn giản; thường xuyên mắc các lỗi ngữ pháp cơ bản làm bóp méo ý nghĩa."
        },
        2: {
            en: "Can only use some memorized structures; errors are dominant and distort the meaning.",
            vi: "Chỉ dùng được một vài mẫu câu học vẹt; lỗi ngữ pháp bao trùm bài viết và làm sai lệch ý nghĩa."
        },
        1: {
            en: "Cannot use sentence forms at all.",
            vi: "Hoàn toàn không thể tạo thành câu hoàn chỉnh."
        },
        0: {
            en: "Does not attend / no response.",
            vi: "Không có bài làm."
        }
    }
};

function getRubricDescriptor(criterion, bandScore) {
    const bandInt = Math.max(0, Math.min(10, Math.round(bandScore)));
    const critObj = VSTEP_OFFICIAL_RUBRIC[criterion];
    if (!critObj) return { en: "", vi: "" };
    return critObj[bandInt] || critObj[0];
}

// Function to render full comprehensive VSTEP evaluation
function renderFullPracticeEvaluationResult(rawText, typeId, timeSpentStr) {
    if (!fullPracticeResultBox) return;

    const words = rawText ? rawText.split(/\s+/).filter(w => w !== '') : [];
    const wordCount = words.length;
    const lower = rawText ? rawText.toLowerCase() : '';

    const typeData = letterTypes.find(t => t.id === typeId) || letterTypes[0];
    const letterTitle = typeData ? `${typeData.titleEn} (${typeData.titleVi})` : 'VSTEP Task 1';

    // Model sample letter extraction
    const tempDiv = document.createElement('div');
    tempDiv.innerHTML = typeData ? typeData.sampleWriting : '';
    const sampleContent = tempDiv.querySelector('.content-block') ? tempDiv.querySelector('.content-block').innerHTML : (typeData ? typeData.sampleWriting : '');

    if (wordCount === 0) {
        fullPracticeResultBox.innerHTML = `
            <div class="practice-summary-card">
                <div class="practice-summary-header" style="color: #ef4444;">
                    <i class="fa-solid fa-triangle-exclamation"></i> BÀI NỘP CHƯA CÓ NỘI DUNG
                </div>
                <p style="color: var(--text-muted); font-size: 15px;">Bạn chưa nhập nội dung bài viết trước khi nộp bài. Vui lòng bấm nút bên dưới để viết bài!</p>
                <div style="margin-top: 20px;">
                    <button class="btn btn-primary" id="btnRestartFullPractice" style="padding: 12px 32px; font-weight: 700; border-radius: 10px;">
                        <i class="fa-solid fa-rotate-left"></i> Viết lại bài này
                    </button>
                </div>
            </div>
        `;
        const btnRestart = document.getElementById('btnRestartFullPractice');
        if (btnRestart) btnRestart.addEventListener('click', resetFullPracticeUI);
        return;
    }

    // --- 1. TASK FULFILMENT (0 - 10) ---
    let hasReq1 = false, hasReq2 = false, hasReq3 = false, hasReq4 = false;
    let reqLabels = [];

    if (typeId === 'advice') {
        hasReq1 = /(stay|hotel|homestay|room|guest\s*house|resort|city\s*cent|old\s*quarter)/i.test(lower);
        hasReq2 = /(dish|dishes|food|pancake|pho|banh\s*mi|bun\s*cha|spring\s*roll|fruit|eat|taste|try|specialt|noodle)/i.test(lower);
        hasReq3 = /(attraction|visit|place|places|lake|hoan\s*kiem|temple|literature|old\s*quarter|museum|market|cai\s*rang|ninh\s*kieu)/i.test(lower);
        hasReq4 = /(wear|clothes|cloth|jacket|umbrella|hat|sunglass|shoes|sneaker|raincoat|t-shirt|shorts|dress|weather|hot|warm)/i.test(lower);
        reqLabels = [
            hasReq1 ? '✓ Nơi ở (Where to stay)' : '✗ Nơi ở (Where to stay)',
            hasReq2 ? '✓ Món ăn nên thử (What dishes to try)' : '✗ Món ăn nên thử (What dishes to try)',
            hasReq3 ? '✓ Địa điểm tham quan (Places to visit)' : '✗ Địa điểm tham quan (Places to visit)',
            hasReq4 ? '✓ Trang phục phù hợp (What to wear)' : '✗ Trang phục phù hợp (What to wear)'
        ];
    } else if (typeId === 'request') {
        hasReq1 = /(address|location|where\s+(is\s+)?the\s+center|near\s+my\s+(house|home)|street|district|located)/i.test(lower);
        hasReq2 = /(fee|tuition|cost|price|money|how\s+much|budget|pay|discount|million|vnd)/i.test(lower);
        hasReq3 = /(teacher|teachers|instructor|friendly|experienced|enthusiastic|native|teach|helpful)/i.test(lower);
        hasReq4 = /(program|training|course|curriculum|skill|schedule|length|study|practise|practice|topic)/i.test(lower);
        reqLabels = [
            hasReq1 ? '✓ Địa chỉ trung tâm (Address)' : '✗ Địa chỉ trung tâm (Address)',
            hasReq2 ? '✓ Học phí khóa học (Tuition fee)' : '✗ Học phí khóa học (Tuition fee)',
            hasReq3 ? '✓ Đội ngũ giáo viên (Teachers)' : '✗ Đội ngũ giáo viên (Teachers)',
            hasReq4 ? '✓ Chương trình đào tạo (Training program)' : '✗ Chương trình đào tạo (Training program)'
        ];
    } else if (typeId === 'description') {
        hasReq1 = /(kind|friendly|helpful|nice|polite|humorous|cheerful|personality|honest|generous|sociable)/i.test(lower);
        hasReq2 = /(hobby|hobbies|free\s*time|leisure|reading|books|cooking|music|sport|sports|swimming|singing)/i.test(lower);
        hasReq3 = /(study|studying|work|working|university|college|student|business|major|job|company)/i.test(lower);
        hasReq4 = /(fit|get\s*on|stay\s*with|live\s*with|adapt|tidy|clean|responsible|family)/i.test(lower);
        reqLabels = [
            hasReq1 ? '✓ Tính cách (Personality)' : '✗ Tính cách (Personality)',
            hasReq2 ? '✓ Sở thích (Hobbies)' : '✗ Sở thích (Hobbies)',
            hasReq3 ? '✓ Việc học/làm hiện tại (Current work/study)' : '✗ Việc học/làm hiện tại (Current work/study)',
            hasReq4 ? '✓ Khả năng hòa nhập gia đình (Fit in family)' : '✗ Khả năng hòa nhập gia đình (Fit in family)'
        ];
    } else if (typeId === 'complaint') {
        hasReq1 = /(problem|problems|room|condition|floor|dirty|wet|locker|lockers|broken|shower|showers|water|ac|air\s*con|facility)/i.test(lower);
        hasReq2 = /(feel|felt|disappoint|unhappy|annoyed|upset|ruin|terrible|bad\s*experience|frustrated|dangerous)/i.test(lower);
        hasReq3 = /(suggest|improve|repair|replace|clean|fix|solution|facility|better|manager)/i.test(lower);
        hasReq4 = true;
        reqLabels = [
            hasReq1 ? '✓ Mô tả sự cố/vấn đề (Problems)' : '✗ Mô tả sự cố/vấn đề (Problems)',
            hasReq2 ? '✓ Cảm xúc của bản thân (Feelings)' : '✗ Cảm xúc của bản thân (Feelings)',
            hasReq3 ? '✓ Đề xuất biện pháp cải thiện (Suggestions)' : '✗ Đề xuất biện pháp cải thiện (Suggestions)'
        ];
    } else if (typeId === 'feedback') {
        hasReq1 = /(satisf|dissatisf|overall|enjoy|opinion|pleas|feedback|impression|feel|experience)/i.test(lower);
        hasReq2 = /(food|dish|room|service|staff|atmosphere|decor|view|breakfast|stay|hotel|restaurant)/i.test(lower);
        hasReq3 = /(suggest|improve|service|staff|speed\s*up|faster|clean|price|discount|training)/i.test(lower);
        hasReq4 = true;
        reqLabels = [
            hasReq1 ? '✓ Mức độ hài lòng (Satisfaction)' : '✗ Mức độ hài lòng (Satisfaction)',
            hasReq2 ? '✓ Mô tả trải nghiệm thực tế (Experience)' : '✗ Mô tả trải nghiệm thực tế (Experience)',
            hasReq3 ? '✓ Gợi ý cải tiến chất lượng (Improvement)' : '✗ Gợi ý cải tiến chất lượng (Improvement)'
        ];
    } else if (typeId === 'apology') {
        hasReq1 = /(apologiz|apologise|sorry|apology|forgive|regret|excuse)/i.test(lower);
        hasReq2 = /(busy|exam|work|sick|ill|situation|finish|finished|reading|book|reason|because)/i.test(lower);
        hasReq3 = /(return|give\s*back|send|meet|tomorrow|next\s*week|by\s*hand|post)/i.test(lower);
        hasReq4 = true;
        reqLabels = [
            hasReq1 ? '✓ Lời xin lỗi chân thành (Apology)' : '✗ Lời xin lỗi chân thành (Apology)',
            hasReq2 ? '✓ Giải thích tình huống & tình trạng đọc sách' : '✗ Giải thích tình huống & tình trạng đọc sách',
            hasReq3 ? '✓ Thời gian và cách thức trả sách (When & How)' : '✗ Thời gian và cách thức trả sách (When & How)'
        ];
    } else if (typeId === 'application') {
        hasReq1 = /(apply|application|position|sales\s*assistant|job|advertis|student|myself)/i.test(lower);
        hasReq2 = /(interest|interested|passion|clothing|store|fashion|career|environment|why)/i.test(lower);
        hasReq3 = /(experience|work|worked|part-time|customer|customers|friendly|communicat|skills|suit)/i.test(lower);
        hasReq4 = true;
        reqLabels = [
            hasReq1 ? '✓ Giới thiệu bản thân & Vị trí ứng tuyển' : '✗ Giới thiệu bản thân & Vị trí ứng tuyển',
            hasReq2 ? '✓ Lý do quan tâm công việc' : '✗ Lý do quan tâm công việc',
            hasReq3 ? '✓ Kinh nghiệm làm việc với khách hàng' : '✗ Kinh nghiệm làm việc với khách hàng'
        ];
    } else {
        hasReq1 = true; hasReq2 = true; hasReq3 = true; hasReq4 = true;
        reqLabels = ['✓ Đáp ứng đầy đủ các yêu cầu cốt lõi'];
    }

    let coveredCount = [hasReq1, hasReq2, hasReq3, hasReq4].filter(Boolean).length;
    let tfScore = 8.5;
    if (coveredCount === 4) {
        tfScore = wordCount >= 140 ? 9.0 : (wordCount >= 120 ? 8.5 : 7.5);
    } else if (coveredCount === 3) {
        tfScore = wordCount >= 120 ? 7.5 : 6.5;
    } else if (coveredCount === 2) {
        tfScore = 5.5;
    } else {
        tfScore = 3.5;
    }
    if (wordCount < 100) tfScore = Math.max(2.0, tfScore - 2.0);
    if (wordCount < 60) tfScore = Math.max(1.0, tfScore - 3.0);

    // --- 2. ORGANIZATION (0 - 10) ---
    const hasGreeting = /^dear\s+[a-z]+/i.test(rawText.trim()) || /dear\s+(mr|ms|mrs|sir|madam)/i.test(rawText.trim());
    const hasOpening = /(thanks?\s+for|hope\s+you|writing\s+to|how\s+are\s+you|in\s+your\s+letter|i\s+am\s+writing)/i.test(lower);
    const hasClosing = /(hope\s+(my\s+advice|you\s+can|you\s+will|this\s+helps)|write\s+back|let\s+me\s+know|look\s+forward|thank\s+you\s+for\s+your\s+time)/i.test(lower);
    const hasSignoff = /(best\s+wishes|yours\s+(sincerely|faithfully)|warm\s+regards|love)/i.test(lower);

    const linkingWordsList = [
        "firstly", "secondly", "next", "finally", "moreover", "besides",
        "furthermore", "in addition", "therefore", "however", "for example", "first of all", "also", "because"
    ];
    let linkCount = 0;
    linkingWordsList.forEach(lw => {
        if (lower.includes(lw)) linkCount++;
    });

    const hasParagraphs = (rawText.split(/\n+/).filter(p => p.trim() !== '').length) >= 3;

    let orgScore = 8.0;
    let orgPartsCount = [hasGreeting, hasOpening, hasClosing, hasSignoff].filter(Boolean).length;
    if (orgPartsCount === 4 && linkCount >= 4 && hasParagraphs) {
        orgScore = 9.0;
    } else if (orgPartsCount === 4 && linkCount >= 3) {
        orgScore = 8.0;
    } else if (orgPartsCount >= 3 && linkCount >= 2) {
        orgScore = 7.0;
    } else if (orgPartsCount >= 2) {
        orgScore = 5.5;
    } else {
        orgScore = 4.0;
    }

    // --- 3. DIAGNOSE ERRORS (VOCABULARY & GRAMMAR) ---
    const promptDummyData = { bulletPoints: [] };
    const errors = (typeof diagnoseVstepErrors === 'function') 
        ? diagnoseVstepErrors(rawText, promptDummyData)
        : [];

    const vocabErrors = errors.filter(e => e.category === 'vocab' || e.category === 'word_form');
    const grammarErrors = errors.filter(e => e.category === 'grammar' || e.category === 'article' || e.category === 'preposition');
    const mechanicsErrors = errors.filter(e => e.category === 'punctuation' || e.category === 'spelling');

    // --- 4. VOCABULARY (0 - 10) ---
    let vocScore = 8.5;
    if (vocabErrors.length >= 3) {
        vocScore = 6.0;
    } else if (vocabErrors.length === 2) {
        vocScore = 6.5;
    } else if (vocabErrors.length === 1) {
        vocScore = 7.5;
    }
    if (wordCount < 120) vocScore = Math.max(4.0, vocScore - 1.0);

    // --- 5. GRAMMAR & ACCURACY (0 - 10) ---
    let gramScore = 8.5;
    const totalGrammarImpact = grammarErrors.length + (mechanicsErrors.length > 0 ? 1 : 0);
    if (totalGrammarImpact >= 6) {
        gramScore = 5.5;
    } else if (totalGrammarImpact >= 4) {
        gramScore = 6.0;
    } else if (totalGrammarImpact >= 2) {
        gramScore = 7.0;
    } else if (totalGrammarImpact === 1) {
        gramScore = 8.0;
    }

    // --- TOTAL VSTEP SCORES & 30% EXAM CONVERSION ---
    let overallBand = (tfScore + orgScore + vocScore + gramScore) / 4.0;
    overallBand = Math.round(overallBand * 10) / 10;

    // Converted to 30% of VSTEP Writing exam (Max 3.00 points)
    let convertedScore = Math.round((overallBand / 10.0) * 3.0 * 100) / 100;

    // 4 Criteria converted to 0.75 points each (0.75 x 4 = 3.00 points)
    let tfConv = Math.round((tfScore / 10.0) * 0.75 * 100) / 100;
    let orgConv = Math.round((orgScore / 10.0) * 0.75 * 100) / 100;
    let vocConv = Math.round((vocScore / 10.0) * 0.75 * 100) / 100;
    let gramConv = Math.round((gramScore / 10.0) * 0.75 * 100) / 100;

    let vstepLevel = "B1 LEVEL (ĐẠT CHUẨN)";
    let levelBadgeStyle = "background: #10b981; color: #ffffff;";
    let levelSummary = "Bài viết đạt chuẩn yêu cầu VSTEP B1. Bố cục đầy đủ và nội dung bám sát đề thi. Cần xem lại các lỗi nhỏ được đánh dấu bên dưới để tối ưu điểm số.";

    if (overallBand >= 8.5) {
        vstepLevel = "B2 LEVEL (XUẤT SẮC - VƯỢT CHUẨN)";
        levelBadgeStyle = "background: #6366f1; color: #ffffff;";
        levelSummary = "Bài viết xuất sắc! Độ hoàn thành cao, câu văn tự nhiên, từ vựng phong phú và cấu trúc chuẩn mực B2.";
    } else if (overallBand < 6.0) {
        vstepLevel = "DƯỚI CHUẨN B1 (CẦN CẢI THIỆN)";
        levelBadgeStyle = "background: #ef4444; color: #ffffff;";
        levelSummary = "Bài viết còn nhiều lỗi ngữ pháp hoặc chưa đủ độ dài quy định (tối thiểu 120 từ). Hãy nghiên cứu kỹ bài mẫu và bảng sửa lỗi bên dưới nhé!";
    }

    // Official Rubric Descriptors Lookup
    const tfDesc = getRubricDescriptor('taskFulfilment', tfScore);
    const orgDesc = getRubricDescriptor('organization', orgScore);
    const vocDesc = getRubricDescriptor('vocabulary', vocScore);
    const gramDesc = getRubricDescriptor('grammar', gramScore);

    // Build Inline Annotated Essay HTML
    const annotatedEssayHtml = (typeof buildAnnotatedEssayHtml === 'function')
        ? buildAnnotatedEssayHtml(rawText, errors)
        : escapeHtml(rawText);

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
                    DANH SÁCH ${errors.length} LỖI CẦN SỬA CHI TIẾT (NGỮ PHÁP, MẠO TỪ, TỪ LOẠI, DÙNG TỪ, CHÍNH TẢ, DẤU CÂU):
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

    // Render HTML in fullPracticeResultBox
    fullPracticeResultBox.innerHTML = `
        <!-- VSTEP Overall Score Banner -->
        <div class="extra-score-banner">
            <div class="score-main-group">
                <div class="score-circle-badge">
                    ${convertedScore.toFixed(2)}
                    <span style="font-size: 13px; display: block; font-weight: 500; opacity: 0.9;">/ 3.00</span>
                </div>
                <div class="score-text-info">
                    <h4>${vstepLevel} • ${convertedScore.toFixed(2)} / 3.00 ĐIỂM (30% BÀI THI WRITING)</h4>
                    <p>Tương đương <strong>Band ${overallBand.toFixed(1)} / 10.0</strong> theo khung chấm chuẩn VSTEP Writing Task 1 của Bộ GD&ĐT.</p>
                    <div style="margin-top: 6px; font-size: 13.5px; opacity: 0.95;">
                        <span><i class="fa-solid fa-user-graduate"></i> ${currentStudentName || 'Học viên'} (Lớp ${currentStudentClass || 'CB206'})</span> • 
                        <span><i class="fa-solid fa-pen-nib"></i> ${wordCount} từ (${wordCount >= 120 ? '✓ Đạt độ dài' : '⚠️ Chưa đủ từ'})</span> • 
                        <span><i class="fa-solid fa-clock"></i> Thời gian: ${timeSpentStr} / 20:00</span>
                    </div>
                </div>
            </div>
            <div class="extra-b1-badge" style="background: #ffffff; color: var(--primary-color); font-weight: 800;">
                TASK 1 = 30% ĐIỂM WRITING
            </div>
        </div>

        <div class="recitation-report-status" style="margin-top: 15px; margin-bottom: 20px;">
            <i class="fa-solid fa-circle-check report-status-icon"></i>
            <span>Đã ghi nhận toàn bộ kết quả bài làm của học viên và tự động báo cáo lên hệ thống của giáo viên!</span>
        </div>

        <!-- 4 Criteria Rubric Grid based on VSTEP SCORING GUIDE (media_1787637818545.jpg) -->
        <div style="margin-top: 25px; margin-bottom: 12px; font-weight: 800; font-size: 17px; color: var(--text-main); display: flex; align-items: center; gap: 8px;">
            <i class="fa-solid fa-scale-balanced" style="color: var(--primary-color);"></i>
            ĐÁNH GIÁ CHI TIẾT THEO 4 TIÊU CHÍ (RATING SCALE FOR VSTEP WRITING TASK 1):
        </div>

        <div class="criteria-grid">
            <!-- 1. Task Fulfilment -->
            <div class="criterion-card">
                <div class="criterion-name">
                    <span>Task Fulfilment (30%)</span>
                    <span class="criterion-score">${tfConv.toFixed(2)}/0.75 <small style="font-size: 11px; font-weight: normal; color: var(--text-muted);">(${tfScore.toFixed(1)}/10)</small></span>
                </div>
                <div class="criterion-desc">
                    <div style="margin-bottom: 6px; font-weight: 600; color: var(--text-main);">
                        ${reqLabels.join(' | ')}.
                    </div>
                    <div>Độ dài: <strong>${wordCount} từ</strong> (${wordCount >= 120 ? 'Đạt chuẩn ≥120 từ' : 'Chưa đủ độ dài'}).</div>
                </div>
                <div class="vstep-official-descriptor-box">
                    <span class="descriptor-tag"><i class="fa-solid fa-stamp"></i> Chuẩn VSTEP Band ${Math.round(tfScore)}:</span>
                    <p class="descriptor-text">"${tfDesc.en}"</p>
                    <p style="margin: 4px 0 0 0; font-size: 12px; color: var(--text-muted);">↳ <em>${tfDesc.vi}</em></p>
                </div>
            </div>

            <!-- 2. Organization -->
            <div class="criterion-card">
                <div class="criterion-name">
                    <span>Organization (30%)</span>
                    <span class="criterion-score">${orgConv.toFixed(2)}/0.75 <small style="font-size: 11px; font-weight: normal; color: var(--text-muted);">(${orgScore.toFixed(1)}/10)</small></span>
                </div>
                <div class="criterion-desc">
                    <div style="margin-bottom: 6px; font-weight: 600; color: var(--text-main);">
                        Bố cục 5 phần chuẩn mực (${orgPartsCount}/4 phần cốt lõi: Greeting, Opening, Closing, Sign-off).
                    </div>
                    <div>Sử dụng <strong>${linkCount} liên từ nối</strong> chuyển tiếp câu mạch lạc.</div>
                </div>
                <div class="vstep-official-descriptor-box">
                    <span class="descriptor-tag"><i class="fa-solid fa-stamp"></i> Chuẩn VSTEP Band ${Math.round(orgScore)}:</span>
                    <p class="descriptor-text">"${orgDesc.en}"</p>
                    <p style="margin: 4px 0 0 0; font-size: 12px; color: var(--text-muted);">↳ <em>${orgDesc.vi}</em></p>
                </div>
            </div>

            <!-- 3. Vocabulary -->
            <div class="criterion-card">
                <div class="criterion-name">
                    <span>Vocabulary (30%)</span>
                    <span class="criterion-score">${vocConv.toFixed(2)}/0.75 <small style="font-size: 11px; font-weight: normal; color: var(--text-muted);">(${vocScore.toFixed(1)}/10)</small></span>
                </div>
                <div class="criterion-desc">
                    <div style="margin-bottom: 6px; font-weight: 600; color: var(--text-main);">
                        Vốn từ vựng theo chủ đề ${letterTitle}.
                    </div>
                    <div>${vocabErrors.length > 0 ? `Bị trừ điểm do mắc <strong>${vocabErrors.length} lỗi</strong> từ vựng / từ loại.` : 'Sử dụng từ vựng chính xác, linh hoạt.'}</div>
                </div>
                <div class="vstep-official-descriptor-box">
                    <span class="descriptor-tag"><i class="fa-solid fa-stamp"></i> Chuẩn VSTEP Band ${Math.round(vocScore)}:</span>
                    <p class="descriptor-text">"${vocDesc.en}"</p>
                    <p style="margin: 4px 0 0 0; font-size: 12px; color: var(--text-muted);">↳ <em>${vocDesc.vi}</em></p>
                </div>
            </div>

            <!-- 4. Grammar & Accuracy -->
            <div class="criterion-card">
                <div class="criterion-name">
                    <span>Grammar & Accuracy (30%)</span>
                    <span class="criterion-score">${gramConv.toFixed(2)}/0.75 <small style="font-size: 11px; font-weight: normal; color: var(--text-muted);">(${gramScore.toFixed(1)}/10)</small></span>
                </div>
                <div class="criterion-desc">
                    <div style="margin-bottom: 6px; font-weight: 600; color: var(--text-main);">
                        Cấu trúc câu đơn & câu phức B1.
                    </div>
                    <div>${totalGrammarImpact > 0 ? `Bị trừ điểm do phát hiện <strong>${grammarErrors.length} lỗi</strong> ngữ pháp/mạo từ và lỗi dấu câu/chính tả.` : 'Ngữ pháp chuẩn xác, câu văn trôi chảy.'}</div>
                </div>
                <div class="vstep-official-descriptor-box">
                    <span class="descriptor-tag"><i class="fa-solid fa-stamp"></i> Chuẩn VSTEP Band ${Math.round(gramScore)}:</span>
                    <p class="descriptor-text">"${gramDesc.en}"</p>
                    <p style="margin: 4px 0 0 0; font-size: 12px; color: var(--text-muted);">↳ <em>${gramDesc.vi}</em></p>
                </div>
            </div>
        </div>

        <!-- Section: Bản sửa lỗi trực tiếp trên bài viết của học viên -->
        <div class="annotated-essay-card" style="margin-top: 30px;">
            <div class="annotated-essay-header">
                <i class="fa-solid fa-pen-to-square"></i> BẢN SỬA LỖI TRỰC TIẾP TRÊN BÀI VIẾT CỦA BẠN (INLINE CORRECTIONS):
            </div>
            <div class="annotated-essay-body">
                ${annotatedEssayHtml}
            </div>
        </div>

        <!-- Detailed Error Table -->
        ${errorTableHtml}

        <!-- Side-by-Side Comparison with Model Letter -->
        <div class="practice-comparison-section" style="margin-top: 35px;">
            <div class="practice-comparison-col">
                <div class="practice-col-header student-col">
                    <i class="fa-solid fa-user-pen"></i> BÀI VIẾT GỐC CỦA BẠN (${wordCount} TỪ)
                </div>
                <div class="practice-paper-view">${escapeHtml(rawText)}</div>
            </div>
            <div class="practice-comparison-col">
                <div class="practice-col-header sample-col">
                    <i class="fa-solid fa-file-circle-check"></i> BÀI MẪU CHUẨN THAM KHẢO & DỊCH NGHĨA
                </div>
                <div class="sample-model-wrapper">
                    ${sampleContent}
                </div>
            </div>
        </div>

        <!-- Restart Button -->
        <div style="text-align: center; margin-top: 30px; margin-bottom: 20px;">
            <button class="btn btn-primary" id="btnRestartFullPractice" style="padding: 12px 36px; font-weight: 700; border-radius: 10px; font-size: 15px;">
                <i class="fa-solid fa-rotate-left"></i> Viết lại bài này
            </button>
        </div>
    `;

    // Attach restart listener
    const btnRestart = document.getElementById('btnRestartFullPractice');
    if (btnRestart) btnRestart.addEventListener('click', resetFullPracticeUI);

    // Send Google Form report to Teacher
    const now = new Date().toLocaleString('vi-VN');
    const excerpt = rawText.length > 200 ? rawText.substring(0, 200) + '...' : rawText;
    const payload = `[THỰC HÀNH VIẾT BÀI]: Học viên: ${currentStudentName || 'Học viên'} | Lớp: ${currentStudentClass || 'CB206'} | Dạng bài: ${letterTitle} | Điểm 30%: ${convertedScore.toFixed(2)}/3.00 (Band ${overallBand.toFixed(1)}/10) | TF: ${tfConv.toFixed(2)}/0.75 | ORG: ${orgConv.toFixed(2)}/0.75 | VOC: ${vocConv.toFixed(2)}/0.75 | GRAM: ${gramConv.toFixed(2)}/0.75 | Lỗi: ${errors.length} | Số từ: ${wordCount} | Thời gian: ${timeSpentStr}/20:00 | Thời điểm: ${now} | Trích đoạn: "${excerpt}"`;

    reportResultToGoogleForm(payload);
}
'''

# New submitFullPractice function that calls renderFullPracticeEvaluationResult
new_submit_full_practice = r'''
function submitFullPractice(isAutoTimeUp = false) {
    const userText = fullPracticeInput ? fullPracticeInput.value.trim() : '';
    const wordCount = countWords(userText);

    if (!isAutoTimeUp) {
        let confirmMsg = 'BẠN CÓ CHẮC CHẮN MUỐN NỘP BÀI THỰC HÀNH KHÔNG?\n\n';
        if (wordCount < 120) {
            confirmMsg += `⚠️ Chú ý: Bài viết của bạn hiện có ${wordCount} từ (chưa đạt chuẩn tối thiểu 120 từ).\n\n`;
        } else {
            confirmMsg += `✓ Số từ đạt: ${wordCount} từ (đạt chuẩn độ dài VSTEP B1).\n\n`;
        }
        confirmMsg += 'Hệ thống sẽ chấm điểm chi tiết theo 4 tiêu chí VSTEP của Bộ GD&ĐT, chỉ ra từng lỗi sai ngữ pháp, và hiển thị bài mẫu đối chiếu!';
        if (!confirm(confirmMsg)) return;
    }

    stopFullPracticeTimer();
    unlockNavigationAfterFullPractice();

    const timeSpentSeconds = Math.max(0, FULL_PRACTICE_TIME_LIMIT - fullPracticeTimeRemaining);
    const timeSpentStr = formatTimerString(timeSpentSeconds);

    if (fullPracticeWritingBox) fullPracticeWritingBox.classList.add('hidden');
    if (fullPracticeResultBox) {
        fullPracticeResultBox.classList.remove('hidden');
        renderFullPracticeEvaluationResult(userText, activeLetterTypeId, timeSpentStr);
    }
}
'''

# Find submitFullPractice in dom_code and replace it
idx_submit = dom_code.find("function submitFullPractice(isAutoTimeUp = false) {")
idx_submit_early = dom_code.find("function submitFullPracticeEarly() {")

if idx_submit == -1 or idx_submit_early == -1:
    raise Exception("Could not find submitFullPractice boundaries")

dom_code_new = (
    dom_code[:idx_submit] +
    scoring_engine_code.strip() + "\n\n" +
    new_submit_full_practice.strip() + "\n\n" +
    dom_code[idx_submit_early:]
)

with open(dom_path, "w", encoding="utf-8") as f:
    f.write(dom_code_new)

print("Updated dom_logic_full.js successfully! New size:", len(dom_code_new))
