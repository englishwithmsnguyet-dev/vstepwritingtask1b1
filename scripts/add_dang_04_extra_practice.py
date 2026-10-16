# -*- coding: utf-8 -*-
with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/pure_extra_logic.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# Let's find where description ends and insert complaint before the closing of extraPracticeData
idx_desc_end = js_code.find("        sampleModelVi: `Nam thân mến,")
idx_bracket_end = js_code.find("    }\n};", idx_desc_end)

complaint_data = r"""
    complaint: {
        title: "DẠNG 04: LETTER OF COMPLAINT (THƯ PHÀN NÀN)",
        prompt: `You recently stayed at a hotel during your holiday. Unfortunately, you were not satisfied with your room. Write a letter to the hotel manager to complain about your stay. In your letter, you should:
• describe the problems with the room
• explain how you felt about the experience
• suggest some improvements
You should write at least 120 words. Do not include your name or address.`,
        analysis: {
            recipient: "Quản lý khách sạn (The Hotel Manager)",
            purpose: "Phàn nàn về chất lượng phòng và đề xuất phương án cải thiện",
            style: "Trang trọng (Formal Letter)",
            requirements: "Mô tả vấn đề của phòng, Bày tỏ cảm xúc, Đề xuất cải thiện"
        },
        hints: [
            {
                title: "1. Describe the problems with the room (Mô tả các vấn đề của phòng)",
                type: "standard",
                items: [
                    {
                        en: "The air conditioner was broken and made a very loud noise all night",
                        vi: "Máy điều hòa bị hỏng và phát ra tiếng ồn rất lớn suốt đêm",
                        reasonEn: "which made it impossible for me to sleep well.",
                        reasonVi: "khiến tôi không thể nào ngủ ngon được."
                    },
                    {
                        en: "The bathroom was not properly cleaned and the shower had no hot water",
                        vi: "Phòng tắm không được dọn dẹp sạch sẽ và vòi sen không có nước nóng",
                        reasonEn: "which was extremely inconvenient and uncomfortable.",
                        reasonVi: "điều này cực kỳ bất tiện và gây khó chịu."
                    },
                    {
                        en: "The bed sheets and towels were stained and looked old",
                        vi: "Ga trải giường và khăn tắm bị ố bẩn và trông đã cũ",
                        reasonEn: "so I had to ask the housekeeping staff to replace them.",
                        reasonVi: "nên tôi đã phải yêu cầu nhân viên dọn phòng thay mới."
                    }
                ]
            },
            {
                title: "2. Explain how you felt about the experience (Bày tỏ cảm xúc về trải nghiệm)",
                type: "standard",
                items: [
                    {
                        en: "I was extremely disappointed with the poor quality of the room",
                        vi: "Tôi vô cùng thất vọng với chất lượng kém của căn phòng",
                        reasonEn: "because I chose your hotel based on its high ratings and reputation.",
                        reasonVi: "vì tôi đã chọn khách sạn của quý vị dựa trên đánh giá cao và danh tiếng."
                    },
                    {
                        en: "This unpleasant experience completely ruined my holiday with my family",
                        vi: "Trải nghiệm không mấy dễ chịu này đã làm hỏng hoàn toàn kỳ nghỉ của tôi với gia đình",
                        reasonEn: "as we could not relax and enjoy our stay.",
                        reasonVi: "vì chúng tôi không thể thư giãn và tận hưởng kỳ nghỉ."
                    },
                    {
                        en: "I felt quite frustrated with the slow response from the reception desk",
                        vi: "Tôi cảm thấy khá bực bội với sự hỗ trợ chậm chạp từ quầy lễ tân",
                        reasonEn: "when I reported these issues to the staff.",
                        reasonVi: "khi tôi phản ánh những vấn đề này với nhân viên."
                    }
                ]
            },
            {
                title: "3. Suggest some improvements (Đề xuất giải pháp cải thiện)",
                type: "standard",
                items: [
                    {
                        en: "I would appreciate it if you could inspect and repair the broken air conditioners",
                        vi: "Tôi sẽ rất cảm kích nếu quý vị có thể kiểm tra và sửa chữa các máy điều hòa bị hỏng",
                        reasonEn: "to ensure future guests do not experience the same problem.",
                        reasonVi: "để đảm bảo các khách hàng sau không gặp phải vấn đề tương tự."
                    },
                    {
                        en: "The housekeeping team should clean the rooms and bathrooms more thoroughly",
                        vi: "Đội ngũ dọn phòng nên vệ sinh phòng ốc và phòng tắm kỹ lưỡng hơn",
                        reasonEn: "to maintain high hygiene standards throughout the hotel.",
                        reasonVi: "để duy trì tiêu chuẩn vệ sinh cao trong toàn bộ khách sạn."
                    },
                    {
                        en: "I hope you will consider offering a partial refund or compensation for the inconvenience",
                        vi: "Tôi hy vọng quý vị sẽ xem xét hoàn lại một phần tiền hoặc bồi thường cho sự bất tiện này",
                        reasonEn: "which would show your commitment to customer satisfaction.",
                        reasonVi: "điều này sẽ thể hiện sự cam kết của quý vị đối với sự hài lòng của khách hàng."
                    }
                ]
            }
        ],
        sampleModel: `Dear Sir/Madam,

I am writing to complain about the room condition during my recent stay at your hotel from 10th to 12th August. Unfortunately, I was not satisfied with the quality of the accommodation and service.

Firstly, the main problem was that the air conditioner in my room was broken and made a very loud noise throughout the night, which made it impossible for me to sleep. Secondly, the bathroom was not properly cleaned and the shower did not have any hot water. Finally, the bed sheets and towels were stained and looked very old. I was extremely disappointed with these issues because I chose your hotel based on its high reputation. This unpleasant experience completely ruined my holiday. Therefore, I would appreciate it if you could inspect and repair the air conditioners immediately, as well as ensure that the housekeeping team cleans the rooms more thoroughly. Furthermore, I hope you will consider offering a partial refund for the inconvenience caused.

I hope you will look into these matters soon. I look forward to receiving your reply.

Yours faithfully,`,
        sampleModelVi: `Kính gửi Ông/Bà,

Tôi viết thư này để phàn nàn về tình trạng phòng ốc trong kỳ nghỉ gần đây của tôi tại khách sạn của quý vị từ ngày 10 đến ngày 12 tháng Tám. Thật không may, tôi đã không hài lòng với chất lượng chỗ ở và dịch vụ.

Đầu tiên, vấn đề chính là máy điều hòa trong phòng tôi bị hỏng và phát ra tiếng ồn rất lớn suốt đêm, khiến tôi không thể nào chợp mắt được. Thứ hai, phòng tắm không được dọn dẹp sạch sẽ và vòi hoa sen hoàn toàn không có nước nóng. Cuối cùng, ga trải giường và khăn tắm bị ố bẩn và trông rất cũ. Tôi vô cùng thất vọng với những vấn đề này vì tôi đã chọn khách sạn của quý vị dựa trên danh tiếng cao của khách sạn. Trải nghiệm khó chịu này đã làm hỏng hoàn toàn kỳ nghỉ của tôi. Do đó, tôi sẽ rất cảm kích nếu quý vị có thể kiểm tra và sửa chữa máy điều hòa ngay lập tức, cũng như đảm bảo đội ngũ dọn phòng vệ sinh phòng ốc kỹ lưỡng hơn. Hơn nữa, tôi hy vọng quý vị sẽ xem xét hoàn lại một phần tiền cho sự bất tiện mà tôi đã gặp phải.

Tôi hy vọng quý vị sẽ sớm xem xét các vấn đề này. Tôi rất mong sớm nhận được phản hồi từ quý vị.

Trân trọng,`
    }
"""

# Let's insert complaint_data before };
js_code = js_code[:idx_bracket_end + 5] + ",\n" + complaint_data.strip() + js_code[idx_bracket_end + 5:]

# Update prompt placeholder to say Dạng 01, Dạng 02, Dạng 03, hoặc Dạng 04
js_code = js_code.replace(
    "Vui lòng chọn <strong>Dạng 01</strong>, <strong>Dạng 02</strong> hoặc <strong>Dạng 03</strong> để làm bài luyện tập.",
    "Vui lòng chọn <strong>Dạng 01</strong>, <strong>Dạng 02</strong>, <strong>Dạng 03</strong> hoặc <strong>Dạng 04</strong> để làm bài luyện tập."
)

# Update gradeExtraPractice for complaint type
idx_req_check = js_code.find("if (typeId === 'request' || typeId === 'description') {")
if idx_req_check != -1:
    complaint_req_logic = """if (typeId === 'complaint') {
        hasReq1 = /(problem|problems|air\s*conditioner|ac|dirty|bathroom|shower|noise|noisy|broken|stained|towel|bed|sheet|issue|water)/i.test(lower);
        hasReq2 = /(feel|felt|disappoint|unhappy|annoyed|upset|ruin|ruined|terrible|bad\s*experience|frustrated)/i.test(lower);
        hasReq3 = /(suggest|improvement|improve|repair|replace|clean|refund|discount|train|service|better|compensation)/i.test(lower);
        hasReq4 = true; // 3 core prompts in complaint
        reqLabels = [
            hasReq1 ? '✓ Mô tả vấn đề phòng' : '✗ Mô tả vấn đề phòng',
            hasReq2 ? '✓ Bày tỏ cảm xúc' : '✗ Bày tỏ cảm xúc',
            hasReq3 ? '✓ Đề xuất cải thiện' : '✗ Đề xuất cải thiện'
        ];
    } else if (typeId === 'request' || typeId === 'description') {"""
    js_code = js_code[:idx_req_check] + complaint_req_logic + js_code[idx_req_check + len("if (typeId === 'request' || typeId === 'description') {"):]

# Update diagnostic rules for formal letters:
diag_rules_addition = """
    if (/\\b(complain\\s+with)\\b/gi.test(rawText)) {
        errors.push({
            type: "Giới từ đi kèm động từ",
            category: "grammar",
            wrong: "complain with",
            correct: "complain about",
            reason: "Phàn nàn về điều gì dùng 'complain about', không dùng 'complain with'."
        });
    }

    if (/\\b(was|were)\\s+not\\s+satisfy\\b/gi.test(rawText)) {
        errors.push({
            type: "Từ loại / Thể bị động",
            category: "grammar",
            wrong: "was not satisfy",
            correct: "was not satisfied",
            reason: "Sau to be diễn tả cảm xúc/tình trạng không hài lòng phải dùng tính từ/quá khứ phân từ 'satisfied'."
        });
    }

    if (/\\blook\\s+forward\\s+to\\s+(hear|receive)\\b/gi.test(rawText)) {
        const m = rawText.match(/\\blook\\s+forward\\s+to\\s+(hear|receive)\\b/i);
        if (m) {
            errors.push({
                type: "Dạng động từ sau giới từ",
                category: "grammar",
                wrong: m[0],
                correct: m[0].replace(m[1], m[1] === 'hear' ? 'hearing' : 'receiving'),
                reason: "Sau cụm 'look forward to' (to là giới từ) bắt buộc phải dùng V-ing ('look forward to hearing/receiving...')."
            });
        }
    }
"""

idx_diag_end = js_code.find("return errors;")
if idx_diag_end != -1:
    js_code = js_code[:idx_diag_end] + diag_rules_addition.strip() + "\n\n    " + js_code[idx_diag_end:]

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/pure_extra_logic.js", "w", encoding="utf-8") as f:
    f.write(js_code)

print("Added Dạng 04 (Letter of Complaint) to pure_extra_logic.js successfully!")
