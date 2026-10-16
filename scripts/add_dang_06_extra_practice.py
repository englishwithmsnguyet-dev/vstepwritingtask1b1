# -*- coding: utf-8 -*-
with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/pure_extra_logic.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# Let's find where feedback ends and insert apology
idx_feedback_end = js_code.find("        sampleModelVi: `Kính gửi Ông/Bà,")
idx_bracket_end = js_code.find("    }\n};", idx_feedback_end)

apology_data = r"""
    apology: {
        title: "DẠNG 06: LETTER OF APOLOGY (THƯ XIN LỖI)",
        prompt: `You have received an email from your professor.
... I noticed that you haven't submitted your assignment yet. The deadline was last Friday, but I still haven't received your work. Could you explain why your assignment was late? Also, when will you submit it? I hope to hear from you soon. ...
Write a letter responding to your professor. In your letter, you should:
• apologize for submitting your assignment late
• explain why you could not submit it on time
• say when and how you will submit your assignment
You should write at least 120 words. Do not include your name or address. Your response will be evaluated in terms of Task Fulfillment, Organization, Vocabulary, and Grammar.`,
        analysis: {
            recipient: "Giáo sư / Giảng viên (Professor / Dr. Smith)",
            purpose: "Xin lỗi về việc nộp bài tập muộn, giải thích lý do và hẹn thời gian/cách thức nộp bài",
            style: "Trang trọng / Lịch sự (Formal Letter)",
            requirements: "Xin lỗi vì nộp muộn, Giải thích lý do chính đáng, Nêu rõ thời gian và cách thức nộp bài"
        },
        hints: [
            {
                title: "1. Apologize for submitting your assignment late (Xin lỗi vì nộp bài muộn)",
                type: "standard",
                items: [
                    {
                        en: "I am writing this email to sincerely apologize for submitting my assignment late",
                        vi: "Em viết email này để chân thành xin lỗi Thầy/Cô vì nộp bài tập muộn",
                        reasonEn: "and I am very sorry for any inconvenience this delay may have caused you.",
                        reasonVi: "và em vô cùng xin lỗi vì sự bất tiện mà sự chậm trễ này đã gây ra cho Thầy/Cô."
                    },
                    {
                        en: "I understand that the deadline was last Friday and submitting on time is extremely important",
                        vi: "Em hiểu rằng hạn chót là thứ Sáu tuần trước và việc nộp bài đúng hạn là vô cùng quan trọng",
                        reasonEn: "which is why I feel very regretful about this situation.",
                        reasonVi: "đó là lý do em cảm thấy rất hối lỗi về tình huống này."
                    },
                    {
                        en: "I take full responsibility for not informing you about my delay earlier",
                        vi: "Em xin nhận hoàn toàn trách nhiệm vì đã không thông báo cho Thầy/Cô về sự chậm trễ sớm hơn",
                        reasonEn: "due to my unexpected personal circumstances.",
                        reasonVi: "do hoàn cảnh cá nhân đột xuất của em."
                    }
                ]
            },
            {
                title: "2. Explain why you could not submit on time (Giải thích lý do không thể nộp đúng hạn)",
                type: "standard",
                items: [
                    {
                        en: "The reason for my delay is that I caught a severe fever and flu early last week",
                        vi: "Lý do của sự chậm trễ là vì em bị sốt cao và cảm cúm nặng vào đầu tuần trước",
                        reasonEn: "so the doctor advised me to rest completely in bed for a few days.",
                        reasonVi: "nên bác sĩ khuyên em phải nghỉ ngơi tĩnh dưỡng hoàn toàn trong vài ngày."
                    },
                    {
                        en: "My laptop suddenly had a serious technical malfunction and shut down unexpectedly",
                        vi: "Máy tính xách tay của em đột nhiên bị lỗi kỹ thuật nghiêm trọng và sập nguồn",
                        reasonEn: "which caused me to lose some of my research notes and draft outlines.",
                        reasonVi: "khiến em bị mất một số ghi chú nghiên cứu và dàn ý bản thảo."
                    },
                    {
                        en: "Because of my illness and computer issues, I was unable to concentrate and finish the work",
                        vi: "Vì bị bệnh và gặp sự cố máy tính, em đã không thể tập trung và hoàn thành bài kịp hạn",
                        reasonEn: "despite my best efforts to meet the deadline.",
                        reasonVi: "mặc dù em đã rất cố gắng để kịp hạn chót."
                    }
                ]
            },
            {
                title: "3. Say when and how you will submit your assignment (Nêu thời gian & cách thức nộp)",
                type: "standard",
                items: [
                    {
                        en: "I have almost finished the final draft and am reviewing it carefully",
                        vi: "Hiện em đã gần hoàn thành bản thảo cuối cùng và đang rà soát lại cẩn thận",
                        reasonEn: "to ensure the highest quality of my research paper.",
                        reasonVi: "để đảm bảo chất lượng bài viết tốt nhất."
                    },
                    {
                        en: "I promise to email the completed assignment to you and upload it to the student portal by 5 PM tomorrow",
                        vi: "Em xin hứa sẽ gửi bài tập hoàn chỉnh qua email và nộp lên cổng thông tin sinh viên trước 5 giờ chiều ngày mai",
                        reasonEn: "so that you can evaluate my work.",
                        reasonVi: "để Thầy/Cô có thể chấm bài giúp em."
                    },
                    {
                        en: "I have attached my medical certificate to this email for your verification",
                        vi: "Em xin đính kèm giấy khám bệnh vào email này để Thầy/Cô tiện xác nhận",
                        reasonEn: "and I assure you that this mistake will not happen again in the future.",
                        reasonVi: "và em xin cam đoan rằng sự cố này sẽ không tái diễn trong tương lai."
                    }
                ]
            }
        ],
        sampleModel: `Dear Professor Smith,

I am writing this email to sincerely apologize for submitting my English assignment late. I understand that the deadline was last Friday, and I am very sorry for any inconvenience this delay may have caused you.

The reason for my late submission is that I caught a severe fever and flu early last week. My doctor advised me to rest completely for a few days, which made it impossible for me to concentrate and complete my assignment on time. In addition, my laptop had a technical error, and I lost some of my research notes. Fortunately, my health has now recovered, and I have resumed working on the paper. I have almost completed the final draft and am revising it thoroughly. I promise to send the completed assignment to your email address and upload it to the student portal by 5 PM tomorrow, Tuesday. I have also attached my medical certificate to this email for your verification.

I truly hope you will understand my situation and accept my late submission. Thank you very much for your time and understanding.

Yours sincerely,`,
        sampleModelVi: `Kính gửi Giáo sư Smith,

Em viết email này để chân thành xin lỗi Thầy vì đã nộp bài tập tiếng Anh muộn. Em hiểu rằng hạn chót là thứ Sáu tuần trước, và em vô cùng xin lỗi về bất kỳ sự bất tiện nào mà sự chậm trễ này đã gây ra cho Thầy.

Lý do em nộp bài trễ là vì em bị sốt cao và cảm cúm nặng vào đầu tuần trước. Bác sĩ đã khuyên em nên nghỉ ngơi tĩnh dưỡng hoàn toàn trong vài ngày, điều đó khiến em không thể tập trung và hoàn thành bài tập đúng hạn. Ngoài ra, máy tính của em gặp sự cố kỹ thuật và em đã bị mất một số ghi chú nghiên cứu. May mắn là hiện tại sức khỏe của em đã hồi phục và em đã tiếp tục làm bài. Em đã gần hoàn thành bản thảo cuối cùng và đang rà soát lại cẩn thận. Em xin hứa sẽ gửi bài hoàn chỉnh vào địa chỉ email của Thầy và tải lên cổng sinh viên trước 5 giờ chiều ngày mai, thứ Ba. Em cũng đã đính kèm giấy khám bệnh vào email này để Thầy tiện xác nhận.

Em rất mong Thầy sẽ thông cảm cho hoàn cảnh của em và chấp nhận bài nộp muộn này. Em xin chân thành cảm ơn Thầy vì đã dành thời gian và thấu hiểu.

Kính thư,`
    }
"""

# Let's insert apology_data before };
js_code = js_code[:idx_bracket_end + 5] + ",\n" + apology_data.strip() + js_code[idx_bracket_end + 5:]

# Update prompt placeholder to include Dạng 06
js_code = js_code.replace(
    "Vui lòng chọn từ <strong>Dạng 01</strong> đến <strong>Dạng 05</strong> để làm bài luyện tập.",
    "Vui lòng chọn từ <strong>Dạng 01</strong> đến <strong>Dạng 06</strong> để làm bài luyện tập."
)

# Update gradeExtraPractice for apology type
idx_feedback_check = js_code.find("if (typeId === 'feedback') {")
if idx_feedback_check != -1:
    apology_req_logic = """if (typeId === 'apology') {
        hasReq1 = /(apologiz|apologise|sorry|apology|forgive|regret|excuse)/i.test(lower);
        hasReq2 = /(sick|ill|flu|fever|health|doctor|hospital|medical|break\s*down|broke\s*down|laptop|computer|error|accident|emergency|reason|because)/i.test(lower);
        hasReq3 = /(submit|send|email|portal|tomorrow|by|attach|certificate|hand\s+in|upload|tuesday|wednesday|pm)/i.test(lower);
        hasReq4 = true; // 3 core prompts in apology
        reqLabels = [
            hasReq1 ? '✓ Lời xin lỗi chân thành' : '✗ Lời xin lỗi chân thành',
            hasReq2 ? '✓ Giải thích lý do chính đáng' : '✗ Giải thích lý do chính đáng',
            hasReq3 ? '✓ Nêu thời gian & cách thức nộp' : '✗ Nêu thời gian & cách thức nộp'
        ];
    } else if (typeId === 'feedback') {"""
    js_code = js_code[:idx_feedback_check] + apology_req_logic + js_code[idx_feedback_check + len("if (typeId === 'feedback') {"):]

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/pure_extra_logic.js", "w", encoding="utf-8") as f:
    f.write(js_code)

print("Added Dạng 06 (Letter of Apology) to pure_extra_logic.js successfully!")
