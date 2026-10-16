# -*- coding: utf-8 -*-
with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/pure_extra_logic.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# Let's find where complaint ends and insert feedback
idx_complaint_end = js_code.find("        sampleModelVi: `Kính gửi Ông/Bà,")
idx_bracket_end = js_code.find("    }\n};", idx_complaint_end)

feedback_data = r"""
    feedback: {
        title: "DẠNG 05: LETTER OF FEEDBACK (THƯ PHẢN HỒI / ĐÓNG GÓP Ý KIẾN)",
        prompt: `You recently had dinner at a new restaurant. A few days later, the restaurant manager sent you an email asking for your feedback.
Write an email to give your opinion. In your email, you should:
• say whether you were satisfied or dissatisfied with the restaurant
• describe your experience
• suggest ways the restaurant can improve its service
You should write at least 120 words. Do not include your name or address.`,
        analysis: {
            recipient: "Quản lý nhà hàng (The Restaurant Manager)",
            purpose: "Đóng góp ý kiến phản hồi về trải nghiệm ăn uống tại nhà hàng",
            style: "Trang trọng / Lịch sự (Formal / Semi-formal Email)",
            requirements: "Nêu mức độ hài lòng, Mô tả trải nghiệm, Đề xuất cải thiện dịch vụ"
        },
        hints: [
            {
                title: "1. Say whether you were satisfied or dissatisfied (Nêu mức độ hài lòng)",
                type: "standard",
                items: [
                    {
                        en: "Overall, I had a pleasant dining experience, although there were a few minor issues",
                        vi: "Nhìn chung, tôi đã có một trải nghiệm ăn uống thú vị, dù vẫn còn một vài điểm nhỏ cần cải thiện",
                        reasonEn: "which I would like to share with you honestly.",
                        reasonVi: "mà tôi muốn chia sẻ chân thành với quý vị."
                    },
                    {
                        en: "I was very satisfied with the delicious food and cozy atmosphere",
                        vi: "Tôi rất hài lòng với món ăn ngon miệng và không gian ấm cúng",
                        reasonEn: "which made our family dinner very enjoyable.",
                        reasonVi: "điều này làm cho bữa tối của gia đình tôi rất vui vẻ."
                    },
                    {
                        en: "However, I was slightly dissatisfied with the waiting time for our main courses",
                        vi: "Tuy nhiên, tôi hơi chưa hài lòng về thời gian chờ đợi các món chính",
                        reasonEn: "because we had to wait for almost forty minutes.",
                        reasonVi: "vì chúng tôi đã phải chờ gần bốn mươi phút."
                    }
                ]
            },
            {
                title: "2. Describe your experience (Mô tả trải nghiệm thực tế)",
                type: "standard",
                items: [
                    {
                        en: "The food was fresh, well-seasoned, and beautifully presented",
                        vi: "Thức ăn tươi ngon, nêm nếm vừa miệng và trình bày đẹp mắt",
                        reasonEn: "especially the grilled seafood and homemade desserts.",
                        reasonVi: "đặc biệt là món hải sản nướng và các món tráng miệng nhà làm."
                    },
                    {
                        en: "The restaurant had modern decoration and soft background music",
                        vi: "Nhà hàng có phong cách trang trí hiện đại và nhạc nền nhẹ nhàng",
                        reasonEn: "which created a relaxing and comfortable ambiance for guests.",
                        reasonVi: "tạo nên không gian thư thái và dễ chịu cho thực khách."
                    },
                    {
                        en: "The waiters were very polite and welcoming, but they seemed overloaded during peak hours",
                        vi: "Các nhân viên phục vụ rất lịch sự và niềm nở, nhưng họ có vẻ bị quá tải vào giờ cao điểm",
                        reasonEn: "so it took some time to get their attention when we needed assistance.",
                        reasonVi: "nên mất khá nhiều thời gian để gọi nhân viên khi chúng tôi cần hỗ trợ."
                    }
                ]
            },
            {
                title: "3. Suggest ways the restaurant can improve its service (Đề xuất giải pháp cải thiện)",
                type: "standard",
                items: [
                    {
                        en: "You should hire more service staff and kitchen assistants during weekends and peak hours",
                        vi: "Quý vị nên tuyển thêm nhân viên phục vụ và phụ bếp vào cuối tuần và các khung giờ cao điểm",
                        reasonEn: "to speed up order preparation and reduce customer waiting time.",
                        reasonVi: "để đẩy nhanh việc chuẩn bị món và giảm thời gian chờ đợi của khách."
                    },
                    {
                        en: "It would be wonderful if you could expand the menu with more vegetarian and healthy options",
                        vi: "Sẽ rất tuyệt nếu quý vị mở rộng thực đơn với nhiều món chay và lựa chọn tốt cho sức khỏe",
                        reasonEn: "to satisfy diverse customer preferences.",
                        reasonVi: "nhằm đáp ứng nhu cầu đa dạng của khách hàng."
                    },
                    {
                        en: "You could introduce a customer loyalty program or discount vouchers for repeat visits",
                        vi: "Quý vị có thể áp dụng chương trình tích điểm khách hàng hoặc voucher giảm giá khi quay lại",
                        reasonEn: "to encourage customer loyalty and attract more patrons.",
                        reasonVi: "để khuyến khích khách hàng quay lại và thu hút thêm thực khách."
                    }
                ]
            }
        ],
        sampleModel: `Dear Sir/Madam,

Thank you for your email asking for my feedback. I am writing to share my opinion about my recent dinner at your restaurant last Friday evening.

Overall, I had a pleasant dining experience, although there were a few minor issues that could be improved. Regarding the food, I was very satisfied because the dishes were fresh, delicious, and beautifully presented, especially the grilled seafood. In addition, the restaurant had an elegant atmosphere with lovely background music, making it an ideal place for family gatherings. However, I was slightly disappointed with the long waiting time. We had to wait for almost forty minutes before our main courses were served because the restaurant was extremely crowded. Therefore, I would suggest hiring more kitchen staff and waiters during weekends to speed up the service. Furthermore, it would be wonderful if you could add more vegetarian options to your menu.

I hope you will find my feedback constructive. I look forward to visiting your restaurant again in the future.

Yours faithfully,`,
        sampleModelVi: `Kính gửi Ông/Bà,

Cảm ơn quý vị đã gửi email xin ý kiến phản hồi của tôi. Tôi viết thư này để chia sẻ cảm nhận về bữa tối gần đây của tôi tại nhà hàng của quý vị vào tối thứ Sáu tuần trước.

Nhìn chung, tôi đã có một trải nghiệm ăn uống thú vị, mặc dù vẫn có một vài vấn đề nhỏ có thể cải thiện. Về món ăn, tôi rất hài lòng vì các món đều tươi ngon, đậm đà và được trình bày đẹp mắt, đặc biệt là món hải sản nướng. Ngoài ra, nhà hàng có không gian trang nhã cùng âm nhạc du dương, là địa điểm lý tưởng cho các buổi tụ họp gia đình. Tuy nhiên, tôi hơi thất vọng một chút về thời gian chờ đợi khá lâu. Chúng tôi đã phải đợi gần 40 phút mới được phục vụ món chính do nhà hàng quá đông khách. Do đó, tôi xin đề xuất nhà hàng nên tuyển thêm nhân viên bếp và phục vụ vào cuối tuần để tăng tốc độ phục vụ. Hơn nữa, sẽ rất tuyệt nếu quý vị bổ sung thêm các món chay vào thực đơn.

Tôi hy vọng quý vị sẽ thấy những đóng góp của tôi mang tính xây dựng. Tôi rất mong sẽ sớm ghé thăm lại nhà hàng của quý vị trong tương lai.

Trân trọng,`
    }
"""

# Let's insert feedback_data before };
js_code = js_code[:idx_bracket_end + 5] + ",\n" + feedback_data.strip() + js_code[idx_bracket_end + 5:]

# Update prompt placeholder to include Dạng 05
js_code = js_code.replace(
    "Vui lòng chọn <strong>Dạng 01</strong>, <strong>Dạng 02</strong>, <strong>Dạng 03</strong> hoặc <strong>Dạng 04</strong> để làm bài luyện tập.",
    "Vui lòng chọn từ <strong>Dạng 01</strong> đến <strong>Dạng 05</strong> để làm bài luyện tập."
)

# Update gradeExtraPractice for feedback type
idx_complaint_check = js_code.find("if (typeId === 'complaint') {")
if idx_complaint_check != -1:
    feedback_req_logic = """if (typeId === 'feedback') {
        hasReq1 = /(satisf|dissatisf|overall|enjoy|opinion|pleas|feedback|impression|feel)/i.test(lower);
        hasReq2 = /(food|dish|dishes|fresh|delicious|atmosphere|music|decor|staff|wait|waiting|service|serve|dinner|restaurant|meal)/i.test(lower);
        hasReq3 = /(suggest|improve|service|hire|staff|waiter|faster|speed\s*up|menu|vegetarian|discount|loyalty|option|recommend)/i.test(lower);
        hasReq4 = true; // 3 core prompts in feedback
        reqLabels = [
            hasReq1 ? '✓ Mức độ hài lòng' : '✗ Mức độ hài lòng',
            hasReq2 ? '✓ Mô tả trải nghiệm' : '✗ Mô tả trải nghiệm',
            hasReq3 ? '✓ Đề xuất cải thiện dịch vụ' : '✗ Đề xuất cải thiện dịch vụ'
        ];
    } else if (typeId === 'complaint') {"""
    js_code = js_code[:idx_complaint_check] + feedback_req_logic + js_code[idx_complaint_check + len("if (typeId === 'complaint') {"):]

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/pure_extra_logic.js", "w", encoding="utf-8") as f:
    f.write(js_code)

print("Added Dạng 05 (Letter of Feedback) to pure_extra_logic.js successfully!")
