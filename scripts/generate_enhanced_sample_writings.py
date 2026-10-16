# -*- coding: utf-8 -*-
"""
Generate enhanced, rich pedagogical HTML for BÀI VIẾT MẪU across all 7 letter types:
1. advice
2. request
3. description
4. complaint
5. feedback
6. apology
7. application
"""

SAMPLE_DATA = {
    "advice": {
        "wordCount": 136,
        "tone": "Thân mật (Informal Letter)",
        "toneBadge": "accent-tone",
        "salutation": {
            "en": "Dear Helen,",
            "vi": "Helen thân mến,",
            "tip": "Chào thân mật bằng Dear + First Name, có dấu phẩy ở cuối."
        },
        "opening": {
            "en": "Thanks for your letter. I hope you are doing well. I’m writing to give you some advice for your trip to Hanoi in June.",
            "annotated": "Thanks for your letter. I hope you are doing well. <span class=\"sample-hl-structure\">I’m writing to give you some advice for</span> your trip to Hanoi in June.",
            "vi": "Cảm ơn thư của cậu. Tớ hy vọng cậu vẫn khỏe. Tớ viết thư này để đưa ra một vài gợi ý cho chuyến đi của cậu đến Hà Nội vào tháng Sáu.",
            "tip": "Mở đầu tự nhiên bằng lời cảm ơn & hỏi thăm, sau đó nêu thẳng mục đích viết thư bằng cấu trúc: I’m writing to give you some advice for..."
        },
        "points": [
            {
                "num": "Ý 1",
                "title": "Nơi ở khi đến Hà Nội (Where to stay)",
                "en": "Firstly, you should stay in a hotel in the city center because it is very convenient for travelling. Many famous places are also located near this area.",
                "annotated": "<mark class=\"sample-hl-connector\">Firstly,</mark> <span class=\"sample-hl-structure\">you should stay in</span> a hotel in the city center <span class=\"sample-hl-structure\">because</span> it is <span class=\"sample-hl-vocab\">very convenient for travelling</span>. Many famous places are also located near this area.",
                "vi": "Đầu tiên, cậu nên ở một khách sạn tại trung tâm thành phố vì nó rất thuận tiện cho việc đi lại. Nhiều địa điểm nổi tiếng cũng nằm gần khu vực này.",
                "tip": "Dùng liên từ mở đầu \"Firstly,\", cấu trúc khuyên \"you should + V\" và liên từ \"because\" để giải thích lý do thuyết phục."
            },
            {
                "num": "Ý 2",
                "title": "Món ăn truyền thống nên thử (What dishes to try)",
                "en": "Secondly, it would be a good idea to try some traditional Vietnamese dishes such as pho, banh mi, and bun cha. These dishes are very popular and delicious.",
                "annotated": "<mark class=\"sample-hl-connector\">Secondly,</mark> <span class=\"sample-hl-structure\">it would be a good idea to</span> try some <span class=\"sample-hl-vocab\">traditional Vietnamese dishes</span> such as pho, banh mi, and bun cha. These dishes are <span class=\"sample-hl-vocab\">very popular and delicious</span>.",
                "vi": "Thứ hai, cậu nên thử một số món ăn truyền thống của Việt Nam như phở, bánh mì và bún chả. Những món ăn này rất phổ biến và ngon miệng.",
                "tip": "Ăn điểm cấu trúc đề xuất chuẩn B1 \"it would be a good idea to + V\" và liệt kê món ăn phong phú bằng \"such as\"."
            },
            {
                "num": "Ý 3",
                "title": "Địa điểm tham quan nổi tiếng (Which places to visit)",
                "en": "Next, if I were you, I would visit some famous places in Hanoi such as Hoan Kiem Lake, the Old Quarter, and the Temple of Literature. These places are very beautiful and interesting.",
                "annotated": "<mark class=\"sample-hl-connector\">Next,</mark> <span class=\"sample-hl-structure\">if I were you, I would</span> visit some <span class=\"sample-hl-vocab\">famous places</span> in Hanoi such as Hoan Kiem Lake, the Old Quarter, and the Temple of Literature. These places are <span class=\"sample-hl-vocab\">very beautiful and interesting</span>.",
                "vi": "Tiếp theo, nếu tớ là cậu, tớ sẽ tham quan một số địa điểm nổi tiếng ở Hà Nội như hồ Hoàn Kiếm, phố cổ và Văn Miếu Quốc Tử Giám. Những nơi này rất đẹp và thú vị.",
                "tip": "Ghi điểm Ngữ pháp đa dạng (Grammatical Range) với câu điều kiện loại 2 giả định: \"if I were you, I would + V\"."
            },
            {
                "num": "Ý 4",
                "title": "Trang phục phù hợp thời tiết (What to wear)",
                "en": "Finally, remember to wear light and comfortable clothes because the weather in Hanoi can be quite hot in June.",
                "annotated": "<mark class=\"sample-hl-connector\">Finally,</mark> <span class=\"sample-hl-structure\">remember to</span> wear <span class=\"sample-hl-vocab\">light and comfortable clothes</span> <span class=\"sample-hl-structure\">because</span> the weather in Hanoi can be quite hot in June.",
                "vi": "Cuối cùng, hãy nhớ mặc quần áo mỏng nhẹ và thoải mái vì thời tiết Hà Nội vào tháng Sáu có thể khá nóng.",
                "tip": "Dùng liên từ kết thúc \"Finally,\" cùng cấu trúc nhắc nhở thân mật \"remember to + V\" và lý do thực tế về thời tiết."
            }
        ],
        "closing": {
            "en": "I hope my advice will be helpful to you. Please let me know how everything turns out. Write back soon.",
            "annotated": "<span class=\"sample-hl-structure\">I hope my advice will be helpful to you.</span> Please let me know how everything turns out. <span class=\"sample-hl-structure\">Write back soon.</span>",
            "vi": "Tớ hy vọng những lời khuyên của tớ sẽ giúp ích cho cậu. Hãy cho tớ biết chuyến đi diễn ra thế nào nhé. Hãy viết thư lại sớm nhé.",
            "tip": "Mẫu câu kết thư ấm áp, bày tỏ hy vọng và nhắc bạn phản hồi thường gặp trong thư thân mật."
        },
        "signoff": {
            "en": "Best wishes,",
            "vi": "Chúc cậu mọi điều tốt lành,",
            "tip": "Lời chào kết thân mật chuẩn VSTEP. Không ký tên thật để tuân thủ quy chế thi."
        },
        "takeaways": {
            "task": "Trả lời đầy đủ và chi tiết 4 gợi ý của đề bài (nơi ở, món ăn, địa danh, trang phục); dung lượng 136 từ đạt chuẩn vàng 120-150 từ.",
            "coherence": "Mạch văn tự nhiên, chuyển ý nhịp nhàng qua chuỗi liên từ (Firstly -> Secondly -> Next -> Finally), mỗi ý phát triển thành 2 câu rõ ràng.",
            "lexical": "Vốn từ miêu tả du lịch phong phú: convenient for travelling, traditional dishes, light and comfortable clothes, popular, delicious.",
            "grammar": "Sử dụng linh hoạt câu ghép liên từ 'because', câu điều kiện loại 2 'if I were you, I would', cấu trúc khuyên bảo 'it would be a good idea to'."
        }
    },

    "request": {
        "wordCount": 132,
        "tone": "Thân mật (Informal Letter)",
        "toneBadge": "accent-tone",
        "salutation": {
            "en": "Dear Moonie,",
            "vi": "Moonie thân mến,",
            "tip": "Chào thân mật người bạn thân bằng tên riêng."
        },
        "opening": {
            "en": "How are you? I hope you are doing well. I’m writing to ask for some information about the English course at Rainbow Language Center because I am planning to study English there soon.",
            "annotated": "How are you? I hope you are doing well. <span class=\"sample-hl-structure\">I’m writing to ask for some information about</span> the English course at Rainbow Language Center <span class=\"sample-hl-structure\">because</span> I am planning to study English there soon.",
            "vi": "Cậu dạo này thế nào? Tớ hy vọng cậu vẫn khỏe. Tớ viết thư này để hỏi xin một vài thông tin về khóa học tiếng Anh tại Trung tâm Ngoại ngữ Rainbow vì tớ đang có kế hoạch học tiếng Anh ở đó trong thời gian tới.",
            "tip": "Hỏi thăm tự nhiên, nêu trực diện mục đích viết thư bằng cấu trúc: I’m writing to ask for some information about..."
        },
        "points": [
            {
                "num": "Ý 1",
                "title": "Địa chỉ của trung tâm (The address of the center)",
                "en": "First of all, could you tell me the address of the center? I want to know if it is near my house.",
                "annotated": "<mark class=\"sample-hl-connector\">First of all,</mark> <span class=\"sample-hl-structure\">could you tell me</span> the address of the center? I want to know if it is near my house.",
                "vi": "Trước hết, cậu có thể cho tớ biết địa chỉ của trung tâm được không? Tớ muốn biết liệu nó có ở gần nhà tớ không.",
                "tip": "Mở đầu thân bài bằng \"First of all,\" và câu hỏi lịch sự \"could you tell me...\" kèm câu giải thích lý do."
            },
            {
                "num": "Ý 2",
                "title": "Học phí khóa học (The tuition fee)",
                "en": "In addition, I would like to know about the tuition fee for the course so that I can prepare my budget.",
                "annotated": "<mark class=\"sample-hl-connector\">In addition,</mark> <span class=\"sample-hl-structure\">I would like to know about</span> the <span class=\"sample-hl-vocab\">tuition fee</span> for the course <span class=\"sample-hl-structure\">so that</span> I can prepare my <span class=\"sample-hl-vocab\">budget</span>.",
                "vi": "Ngoài ra, tớ cũng muốn biết về mức học phí của khóa học để tớ có thể chuẩn bị ngân sách.",
                "tip": "Liên từ bổ sung \"In addition,\", mẫu câu \"I would like to know about...\" và mệnh đề chỉ mục đích \"so that...\"."
            },
            {
                "num": "Ý 3",
                "title": "Đội ngũ giáo viên (The teachers)",
                "en": "Furthermore, can you tell me more about the teachers? Are they friendly and experienced?",
                "annotated": "<mark class=\"sample-hl-connector\">Furthermore,</mark> <span class=\"sample-hl-structure\">can you tell me more about</span> the teachers? Are they <span class=\"sample-hl-vocab\">friendly and experienced</span>?",
                "vi": "Hơn nữa, cậu có thể kể thêm cho tớ về các thầy cô giáo không? Họ có thân thiện và giàu kinh nghiệm không?",
                "tip": "Liên từ phát triển ý \"Furthermore,\", hỏi thông tin tính chất giáo viên với cặp tính từ hay \"friendly and experienced\"."
            },
            {
                "num": "Ý 4",
                "title": "Chương trình đào tạo & Lịch học (The training program)",
                "en": "Finally, I was wondering if you could give me some details about the training program and the class schedule.",
                "annotated": "<mark class=\"sample-hl-connector\">Finally,</mark> <span class=\"sample-hl-structure\">I was wondering if you could give me</span> some details about the <span class=\"sample-hl-vocab\">training program</span> and the <span class=\"sample-hl-vocab\">class schedule</span>.",
                "vi": "Cuối cùng, tớ đang băn khoăn không biết cậu có thể chia sẻ cho tớ một vài chi tiết về chương trình đào tạo và lịch học được không.",
                "tip": "Mẫu câu đề nghị gián tiếp lịch sự đỉnh cao chuẩn B1/B2: \"I was wondering if you could give me...\"."
            }
        ],
        "closing": {
            "en": "I hope you can help me with this. Write back soon.",
            "annotated": "<span class=\"sample-hl-structure\">I hope you can help me with this.</span> <span class=\"sample-hl-structure\">Write back soon.</span>",
            "vi": "Tớ hy vọng cậu có thể giúp tớ việc này nhé. Hãy viết thư lại cho tớ sớm nhé.",
            "tip": "Lời kết bày tỏ hy vọng và giục bạn hồi âm nhanh chóng."
        },
        "signoff": {
            "en": "Best wishes,",
            "vi": "Chúc cậu mọi điều tốt lành,",
            "tip": "Lời kết thân mật chuẩn mực."
        },
        "takeaways": {
            "task": "Hỏi trọn vẹn 4 thông tin quan trọng được đề bài yêu cầu: địa chỉ, học phí, giáo viên, chương trình và lịch học.",
            "coherence": "Hệ thống liên từ chuyển tiếp hoàn hảo (First of all -> In addition -> Furthermore -> Finally).",
            "lexical": "Sử dụng đúng thuật ngữ học đường: tuition fee, budget, experienced teachers, training program, class schedule.",
            "grammar": "Đa dạng hóa câu hỏi và yêu cầu: Could you tell me, I would like to know, can you tell me, I was wondering if you could."
        }
    },

    "description": {
        "wordCount": 136,
        "tone": "Thân mật (Informal Letter)",
        "toneBadge": "accent-tone",
        "salutation": {
            "en": "Dear Emily,",
            "vi": "Emily thân mến,",
            "tip": "Chào bạn bằng Dear + First Name."
        },
        "opening": {
            "en": "How are you? I hope you are doing well. In your letter, you asked me about my friend Hoa, so here is some information.",
            "annotated": "How are you? I hope you are doing well. <span class=\"sample-hl-structure\">In your letter, you asked me about</span> my friend Hoa, <span class=\"sample-hl-structure\">so here is some information</span>.",
            "vi": "Cậu dạo này thế nào? Tớ hy vọng cậu vẫn khỏe. Trong thư trước, cậu có hỏi tớ về bạn Hoa của tớ, vậy nên dưới đây là một số thông tin nhé.",
            "tip": "Dẫn dắt trực tiếp từ lá thư của Emily và thông báo nội dung cung cấp."
        },
        "points": [
            {
                "num": "Ý 1",
                "title": "Tính cách của Hoa (Her personality)",
                "en": "Firstly, she is a very kind and friendly person. She gets on well with everyone and is always willing to help others.",
                "annotated": "<mark class=\"sample-hl-connector\">Firstly,</mark> she is a <span class=\"sample-hl-vocab\">very kind and friendly person</span>. She <span class=\"sample-hl-structure\">gets on well with everyone</span> and is <span class=\"sample-hl-structure\">always willing to help others</span>.",
                "vi": "Đầu tiên, cô ấy là một người rất tốt bụng và thân thiện. Cô ấy hòa thuận với tất cả mọi người và luôn sẵn lòng giúp đỡ người khác.",
                "tip": "Phrasal verb ăn điểm \"get on well with someone\" và cụm tính từ \"willing to help others\"."
            },
            {
                "num": "Ý 2",
                "title": "Sở thích lúc rảnh rỗi (Her hobbies)",
                "en": "Secondly, in her free time, she likes reading books, cooking traditional Vietnamese food, and listening to music. I think she would be happy to cook some delicious meals for your family.",
                "annotated": "<mark class=\"sample-hl-connector\">Secondly,</mark> in her free time, she likes <span class=\"sample-hl-vocab\">reading books, cooking traditional Vietnamese food, and listening to music</span>. <span class=\"sample-hl-structure\">I think she would be happy to</span> cook some delicious meals for your family.",
                "vi": "Thứ hai, trong thời gian rảnh, cô ấy thích đọc sách, nấu các món ăn truyền thống của Việt Nam và nghe nhạc. Tớ nghĩ cô ấy sẽ rất vui khi được nấu một vài bữa ăn ngon cho gia đình cậu.",
                "tip": "Cấu trúc song hành với V-ing (reading, cooking, listening) và câu phán đoán thân thiện \"I think she would be happy to...\"."
            },
            {
                "num": "Ý 3",
                "title": "Công việc/Học tập hiện tại (Current work or study)",
                "en": "Finally, she is currently studying business at university and works very hard. She is responsible and always keeps her room tidy.",
                "annotated": "<mark class=\"sample-hl-connector\">Finally,</mark> she is <span class=\"sample-hl-structure\">currently studying</span> business at university and <span class=\"sample-hl-vocab\">works very hard</span>. She is <span class=\"sample-hl-vocab\">responsible</span> and always <span class=\"sample-hl-vocab\">keeps her room tidy</span>.",
                "vi": "Cuối cùng, cô ấy hiện đang học ngành kinh doanh tại trường đại học và học tập rất chăm chỉ. Cô ấy là người có trách nhiệm và luôn giữ phòng ngủ ngăn nắp.",
                "tip": "Mô tả sinh hoạt học tập chuẩn B1 với tính từ trách nhiệm \"responsible\" và nề nếp \"tidy\"."
            },
            {
                "num": "Ý 4",
                "title": "Khả năng hòa nhập với gia đình chủ (Whether she will fit in)",
                "en": "Therefore, I believe she will fit in very well with your family.",
                "annotated": "<mark class=\"sample-hl-connector\">Therefore,</mark> <span class=\"sample-hl-structure\">I believe she will fit in very well with</span> your family.",
                "vi": "Vì vậy, tớ tin rằng cô ấy sẽ hòa nhập rất tốt với gia đình cậu.",
                "tip": "Từ nối kết luận \"Therefore,\" và giải quyết trọn vẹn thắc mắc lớn nhất của Emily bằng cụm từ \"fit in very well with\"."
            }
        ],
        "closing": {
            "en": "I hope you will find this information useful. Let me know if you need more details.",
            "annotated": "<span class=\"sample-hl-structure\">I hope you will find this information useful.</span> <span class=\"sample-hl-structure\">Let me know if you need more details.</span>",
            "vi": "Tớ hy vọng cậu sẽ thấy những thông tin này hữu ích. Hãy cho tớ biết nếu cậu cần thêm chi tiết nhé.",
            "tip": "Câu kết chuẩn mực cho dạng thư cung cấp thông tin (Description/Information Letter)."
        },
        "signoff": {
            "en": "Best wishes,",
            "vi": "Chúc cậu mọi điều tốt lành,",
            "tip": "Lời chào kết thân mật."
        },
        "takeaways": {
            "task": "Miêu tả đầy đủ 4 khía cạnh: tính cách, sở thích, việc học tập và kết luận khẳng định sự hòa nhập.",
            "coherence": "Tổ chức mạch lạc từ tính cách -> sở thích -> học tập -> kết luận với các liên từ Firstly, Secondly, Finally, Therefore.",
            "lexical": "Cụm từ tự nhiên: get on well with, willing to help, keep room tidy, fit in with.",
            "grammar": "Phối hợp thì Hiện tại đơn, Hiện tại tiếp diễn và cấu trúc phỏng đoán giả định với 'would'."
        }
    },

    "complaint": {
        "wordCount": 148,
        "tone": "Trang trọng (Formal Letter)",
        "toneBadge": "accent-tone",
        "salutation": {
            "en": "Dear Sir/Madam,",
            "vi": "Kính gửi Ông/Bà,",
            "tip": "Thư trang trọng gửi người quản lý không rõ tên, bắt buộc dùng 'Dear Sir/Madam,' kèm dấu phẩy."
        },
        "opening": {
            "en": "I am writing to complain about the condition of the changing room at your sports center. I recently used the facility and was not satisfied with it.",
            "annotated": "<span class=\"sample-hl-structure\">I am writing to complain about</span> the condition of the changing room at your sports center. I recently used the facility and <span class=\"sample-hl-structure\">was not satisfied with it</span>.",
            "vi": "Tôi viết thư này để phàn nàn về tình trạng của phòng thay đồ tại trung tâm thể thao của ông/bà. Gần đây tôi đã sử dụng cơ sở vật chất này và không hài lòng với nó.",
            "tip": "Mở đầu thư trang trọng đúng chuẩn VSTEP: \"I am writing to complain about...\" và bày tỏ sự không hài lòng."
        },
        "points": [
            {
                "num": "Ý 1",
                "title": "Vấn đề 1: Sàn nhà bẩn & ẩm ướt (Dirty and wet floor)",
                "en": "The main problem was that the floor was very dirty and wet, which was quite dangerous for members.",
                "annotated": "<mark class=\"sample-hl-connector\">The main problem was that</mark> the floor was <span class=\"sample-hl-vocab\">very dirty and wet</span>, <span class=\"sample-hl-structure\">which was quite dangerous for members</span>.",
                "vi": "Vấn đề chính là sàn nhà rất bẩn và ẩm ướt, điều này khá nguy hiểm cho các hội viên.",
                "tip": "Dùng mệnh đề quan hệ không xác định \", which was...\" để giải thích tác hại nguy hiểm."
            },
            {
                "num": "Ý 2",
                "title": "Vấn đề 2: Tủ khóa đồ bị hỏng (Broken lockers)",
                "en": "Another issue was that several lockers were broken, so I could not safely store my personal belongings.",
                "annotated": "<mark class=\"sample-hl-connector\">Another issue was that</mark> several lockers were <span class=\"sample-hl-vocab\">broken</span>, <span class=\"sample-hl-structure\">so I could not safely store</span> my <span class=\"sample-hl-vocab\">personal belongings</span>.",
                "vi": "Một vấn đề khác là một số tủ đựng đồ bị hỏng, vì vậy tôi không thể cất giữ đồ dùng cá nhân của mình một cách an toàn.",
                "tip": "Cụm nối trang trọng \"Another issue was that...\", mệnh đề kết quả với \"so\" và từ vựng đắt giá \"personal belongings\"."
            },
            {
                "num": "Ý 3",
                "title": "Vấn đề 3: Vòi tắm thiếu nước nóng & Cảm xúc (No hot water & feeling)",
                "en": "Finally, I also found that some of the showers did not have hot water. I was very disappointed with these problems because I have always enjoyed using your center.",
                "annotated": "<mark class=\"sample-hl-connector\">Finally,</mark> I also found that some of the showers did not have hot water. <span class=\"sample-hl-structure\">I was very disappointed with these problems because</span> I have always enjoyed using your center.",
                "vi": "Cuối cùng, tôi cũng nhận thấy một số vòi hoa sen không có nước nóng. Tôi rất thất vọng với những vấn đề này vì tôi luôn thích sử dụng trung tâm của ông/bà.",
                "tip": "Thể hiện cảm xúc chuẩn mực, lịch sự trong thư phàn nàn: \"I was very disappointed with... because...\"."
            },
            {
                "num": "Ý 4",
                "title": "Ý 4: Đề xuất giải pháp khắc phục (Suggestions for improvement)",
                "en": "Therefore, I would appreciate it if you could clean the changing room more regularly, repair the broken lockers, and fix the showers as soon as possible.",
                "annotated": "<mark class=\"sample-hl-connector\">Therefore,</mark> <span class=\"sample-hl-structure\">I would appreciate it if you could</span> clean the changing room more regularly, repair the broken lockers, and fix the showers <span class=\"sample-hl-vocab\">as soon as possible</span>.",
                "vi": "Do đó, tôi sẽ rất cảm kích nếu ông/bà có thể dọn dẹp phòng thay đồ thường xuyên hơn, sửa chữa các tủ đựng đồ bị hỏng và sửa lại các vòi hoa sen càng sớm càng tốt.",
                "tip": "Cấu trúc yêu cầu lịch sự trang trọng bậc nhất trong VSTEP Task 1: \"I would appreciate it if you could + V\"."
            }
        ],
        "closing": {
            "en": "I hope that you will look into these issues soon. I look forward to receiving your reply soon.",
            "annotated": "<span class=\"sample-hl-structure\">I hope that you will look into these issues soon.</span> <span class=\"sample-hl-structure\">I look forward to receiving your reply soon.</span>",
            "vi": "Tôi hy vọng ông/bà sẽ sớm xem xét các vấn đề này. Tôi rất mong sớm nhận được phản hồi từ ông/bà.",
            "tip": "Cụm phrasal verb \"look into\" (xem xét giải quyết) và câu kết kinh điển \"look forward to + V-ing\"."
        },
        "signoff": {
            "en": "Yours faithfully,",
            "vi": "Trân trọng,",
            "tip": "Bắt đầu bằng 'Dear Sir/Madam,' thì kết thúc BẮT BUỘC là 'Yours faithfully,'."
        },
        "takeaways": {
            "task": "Nêu rõ 3 vấn đề cụ thể (sàn bẩn/ướt, tủ hỏng, thiếu nước nóng), bày tỏ cảm xúc thất vọng và đề xuất 3 giải pháp cải thiện cụ thể.",
            "coherence": "Trình bày vấn đề chặt chẽ theo thứ tự: The main problem -> Another issue -> Finally -> Therefore.",
            "lexical": "Từ vựng trang trọng: condition, facility, dangerous, personal belongings, disappointed, look into, as soon as possible.",
            "grammar": "Mệnh đề quan hệ không xác định, mệnh đề nguyên nhân - kết quả, cấu trúc trang trọng 'I would appreciate it if you could'."
        }
    },

    "feedback": {
        "wordCount": 150,
        "tone": "Trang trọng (Formal Letter)",
        "toneBadge": "accent-tone",
        "salutation": {
            "en": "Dear Sir/Madam,",
            "vi": "Kính gửi Ông/Bà,",
            "tip": "Thư trang trọng gửi Quản lý khách sạn (Dear Sir/Madam,)."
        },
        "opening": {
            "en": "I am writing to give you feedback on my recent stay at your hotel. I recently used your services and would like to share my experience.",
            "annotated": "<span class=\"sample-hl-structure\">I am writing to give you feedback on</span> my recent stay at your hotel. I recently used your services and <span class=\"sample-hl-structure\">would like to share my experience</span>.",
            "vi": "Tôi viết thư này để đưa ra phản hồi về kỳ nghỉ gần đây của tôi tại khách sạn của ông/bà. Gần đây tôi đã sử dụng dịch vụ của ông/bà và muốn chia sẻ trải nghiệm của mình.",
            "tip": "Nêu mục đích phản hồi trực tiếp: \"I am writing to give you feedback on...\"."
        },
        "points": [
            {
                "num": "Ý 1",
                "title": "Điểm hài lòng: Dịch vụ khách hàng (Customer service)",
                "en": "First of all, I would like to mention some positive points about your hotel. I was very satisfied with the customer service because the staff were polite, friendly, and always ready to assist guests.",
                "annotated": "<mark class=\"sample-hl-connector\">First of all,</mark> I would like to mention some <span class=\"sample-hl-vocab\">positive points</span> about your hotel. <span class=\"sample-hl-structure\">I was very satisfied with</span> the customer service <span class=\"sample-hl-structure\">because</span> the staff were <span class=\"sample-hl-vocab\">polite, friendly, and always ready to assist guests</span>.",
                "vi": "Trước hết, tôi muốn đề cập đến một số điểm tích cực về khách sạn của ông/bà. Tôi rất hài lòng với dịch vụ chăm sóc khách hàng vì nhân viên rất lịch sự, thân thiện và luôn sẵn sàng hỗ trợ khách.",
                "tip": "Đánh giá công tâm bằng cách khen trước với cấu trúc \"I was very satisfied with... because...\" và bộ 3 tính từ nhân viên."
            },
            {
                "num": "Ý 2",
                "title": "Điểm hài lòng: Phòng ốc (Spacious and clean room)",
                "en": "In addition, the room was spacious and clean.",
                "annotated": "<mark class=\"sample-hl-connector\">In addition,</mark> the room was <span class=\"sample-hl-vocab\">spacious and clean</span>.",
                "vi": "Ngoài ra, phòng ốc rất rộng rãi và sạch sẽ.",
                "tip": "Từ vựng miêu tả phòng khách sạn chuẩn B1: \"spacious and clean\"."
            },
            {
                "num": "Ý 3",
                "title": "Điểm cần cải thiện: Wi-Fi và Bữa sáng (Wi-Fi and Breakfast)",
                "en": "However, there were also some areas that needed improvement. I was disappointed with the Wi-Fi connection because it was slow and unstable. Furthermore, the breakfast menu was quite limited and lacked variety.",
                "annotated": "<mark class=\"sample-hl-connector\">However,</mark> there were also some <span class=\"sample-hl-vocab\">areas that needed improvement</span>. <span class=\"sample-hl-structure\">I was disappointed with</span> the Wi-Fi connection <span class=\"sample-hl-structure\">because</span> it was slow and unstable. <mark class=\"sample-hl-connector\">Furthermore,</mark> the breakfast menu was <span class=\"sample-hl-vocab\">quite limited and lacked variety</span>.",
                "vi": "Tuy nhiên, cũng có một số khía cạnh cần được cải thiện. Tôi đã thất vọng với kết nối Wi-Fi vì nó chậm và không ổn định. Hơn nữa, thực đơn bữa sáng khá hạn chế và thiếu sự đa dạng.",
                "tip": "Chuyển ý tương phản tinh tế với \"However,\", dùng cụm từ khách quan \"needed improvement\", \"lacked variety\"."
            },
            {
                "num": "Ý 4",
                "title": "Đề xuất nâng cấp dịch vụ (Suggestions for improvement)",
                "en": "To enhance the quality of your services, I suggest that you should upgrade the Internet system and offer more options for breakfast.",
                "annotated": "<span class=\"sample-hl-structure\">To enhance the quality of your services, I suggest that you should</span> <span class=\"sample-hl-vocab\">upgrade the Internet system</span> and <span class=\"sample-hl-vocab\">offer more options</span> for breakfast.",
                "vi": "Để nâng cao chất lượng dịch vụ của ông/bà, tôi đề nghị ông/bà nên nâng cấp hệ thống Internet và cung cấp nhiều sự lựa chọn hơn cho bữa sáng.",
                "tip": "Mẫu câu đề xuất chuẩn học thuật: \"To enhance the quality of..., I suggest that you should + V\"."
            }
        ],
        "closing": {
            "en": "I hope my feedback will help you improve your service. Please feel free to contact me if you have any further questions.",
            "annotated": "<span class=\"sample-hl-structure\">I hope my feedback will help you improve your service.</span> <span class=\"sample-hl-structure\">Please feel free to contact me if you have any further questions.</span>",
            "vi": "Tôi hy vọng phản hồi của tôi sẽ giúp ông/bà cải thiện dịch vụ của mình. Xin vui lòng liên hệ với tôi nếu ông/bà có bất kỳ câu hỏi nào thêm.",
            "tip": "Câu kết thể hiện thiện chí và sẵn sàng cung cấp thêm thông tin trong giao tiếp kinh doanh."
        },
        "signoff": {
            "en": "Yours faithfully,",
            "vi": "Trân trọng,",
            "tip": "Ký tên trang trọng chuẩn VSTEP."
        },
        "takeaways": {
            "task": "Đạt chuẩn cấu trúc phản hồi cân bằng: 2 điểm khen (nhân viên, phòng ốc) + 2 điểm chê (Wi-Fi, bữa sáng) + đề xuất cải thiện cụ thể.",
            "coherence": "Tổ chức chuyển đoạn tương phản xuất sắc: First of all -> In addition -> However -> Furthermore -> To enhance...",
            "lexical": "Thuật ngữ ngành dịch vụ khách sạn: customer service, assist guests, spacious, unstable, lacked variety, enhance quality.",
            "grammar": "Sử dụng câu phức mệnh đề quan hệ rút gọn, cấu trúc giả định 'suggest that you should + V'."
        }
    },

    "apology": {
        "wordCount": 140,
        "tone": "Thân mật (Informal Letter)",
        "toneBadge": "accent-tone",
        "salutation": {
            "en": "Dear Helen,",
            "vi": "Helen thân mến,",
            "tip": "Chào bạn thân mật bằng tên riêng."
        },
        "opening": {
            "en": "I’m really sorry for not returning your book earlier. Let me explain what happened so you can understand the situation.",
            "annotated": "<span class=\"sample-hl-structure\">I’m really sorry for not returning your book earlier.</span> <span class=\"sample-hl-structure\">Let me explain what happened so you can understand the situation.</span>",
            "vi": "Tớ thực sự xin lỗi vì đã không trả sách cho cậu sớm hơn. Hãy để tớ giải thích những gì đã xảy ra để cậu hiểu rõ tình hình nhé.",
            "tip": "Xin lỗi ngay ở câu đầu bằng \"I’m really sorry for + V-ing\" và mở lối giải thích chân thành."
        },
        "points": [
            {
                "num": "Ý 1",
                "title": "Lý do chậm trễ - Bận ôn thi (Reason for delay)",
                "en": "First of all, let me explain why this happened. I’m really sorry that I couldn’t return the book on time because I have been extremely busy preparing for my final exams. During that time, I had several assignments and an important test. As a result, I completely forgot about the book.",
                "annotated": "<mark class=\"sample-hl-connector\">First of all,</mark> let me explain why this happened. <span class=\"sample-hl-structure\">I’m really sorry that I couldn’t return</span> the book on time <span class=\"sample-hl-structure\">because I have been extremely busy preparing for</span> my final exams. During that time, I had several assignments and an important test. <mark class=\"sample-hl-connector\">As a result,</mark> <span class=\"sample-hl-vocab\">I completely forgot about the book</span>.",
                "vi": "Trước hết, hãy để tớ giải thích tại sao chuyện này lại xảy ra. Tớ thực sự xin lỗi vì tớ đã không thể trả sách đúng hạn vì tớ quá bận rộn chuẩn bị cho kỳ thi cuối kỳ. Trong thời gian đó, tớ có vài bài tập lớn và một bài kiểm tra quan trọng. Kết quả là tớ hoàn toàn quên mất cuốn sách.",
                "tip": "Thì Hiện tại hoàn thành \"have been extremely busy\" giải thích quá trình bận rộn, liên từ kết quả \"As a result\"."
            },
            {
                "num": "Ý 2",
                "title": "Tình trạng đọc sách & Cảm nhận (Finished reading & feelings)",
                "en": "In addition, I have finished reading the whole book and found it very interesting and helpful.",
                "annotated": "<mark class=\"sample-hl-connector\">In addition,</mark> <span class=\"sample-hl-structure\">I have finished reading the whole book</span> and <span class=\"sample-hl-vocab\">found it very interesting and helpful</span>.",
                "vi": "Ngoài ra, tớ đã đọc xong toàn bộ cuốn sách và thấy nó rất thú vị và bổ ích.",
                "tip": "Trả lời trực diện câu hỏi trong thư của bạn (đã đọc xong chưa?) bằng thì HTHT và cấu trúc \"find something + adj\"."
            },
            {
                "num": "Ý 3",
                "title": "Thời gian & Cách thức trả sách (When & how to return)",
                "en": "Next, I plan to give it back to you this Saturday. I can come over to your house in the afternoon to return it in person.",
                "annotated": "<mark class=\"sample-hl-connector\">Next,</mark> <span class=\"sample-hl-structure\">I plan to give it back to you</span> this Saturday. I can come over to your house in the afternoon to <span class=\"sample-hl-vocab\">return it in person</span>.",
                "vi": "Tiếp theo, tớ dự định sẽ trả lại sách cho cậu vào thứ Bảy tuần này. Tớ có thể ghé qua nhà cậu vào buổi chiều để trực tiếp gửi lại sách.",
                "tip": "Nêu kế hoạch rõ ràng với \"I plan to + V\" và hình thức gặp trực tiếp \"return it in person\"."
            },
            {
                "num": "Ý 4",
                "title": "Đề nghị chuộc lỗi (Make it up to you)",
                "en": "Finally, let me make it up to you by treating you to a cup of milk tea and some snacks.",
                "annotated": "<mark class=\"sample-hl-connector\">Finally,</mark> <span class=\"sample-hl-structure\">let me make it up to you by</span> <span class=\"sample-hl-vocab\">treating you to a cup of milk tea</span> and some snacks.",
                "vi": "Cuối cùng, hãy để tớ bù đắp cho cậu bằng một chầu trà sữa và đồ ăn vặt nhé.",
                "tip": "Idiom tự nhiên xuất sắc trong văn nói/viết thân mật: \"make it up to someone by doing something\"."
            }
        ],
        "closing": {
            "en": "Sorry once again. Thanks for taking the time to read this. Write back soon.",
            "annotated": "<span class=\"sample-hl-structure\">Sorry once again.</span> Thanks for taking the time to read this. <span class=\"sample-hl-structure\">Write back soon.</span>",
            "vi": "Xin lỗi cậu một lần nữa nhé. Cảm ơn cậu vì đã dành thời gian đọc thư này. Hãy viết thư lại cho tớ sớm nhé.",
            "tip": "Khẳng định lại lời xin lỗi \"Sorry once again\" và kết thư ấm áp."
        },
        "signoff": {
            "en": "Best wishes,",
            "vi": "Chúc cậu mọi điều tốt lành,",
            "tip": "Lời chào kết thân mật."
        },
        "takeaways": {
            "task": "Hoàn thành xuất sắc 4 yêu cầu: xin lỗi chân thành, giải thích lý do thi cử, xác nhận đã đọc xong, hẹn ngày giờ và cách chuộc lỗi.",
            "coherence": "Liên kết chặt chẽ qua First of all -> As a result -> In addition -> Next -> Finally.",
            "lexical": "Cụm diễn đạt tự nhiên: on time, extremely busy preparing for, in person, make it up to someone, treat someone to.",
            "grammar": "Sử dụng phối hợp thì Quá khứ đơn, Hiện tại hoàn thành tiếp diễn và cấu trúc dự định 'plan to + V'."
        }
    },

    "application": {
        "wordCount": 175,
        "tone": "Trang trọng (Formal Letter)",
        "toneBadge": "accent-tone",
        "salutation": {
            "en": "Dear Sir/Madam,",
            "vi": "Kính gửi Ông/Bà,",
            "tip": "Thư xin việc trang trọng gửi nhà tuyển dụng (Dear Sir/Madam,)."
        },
        "opening": {
            "en": "I am writing to apply for the position of sales assistant which was advertised on your website.",
            "annotated": "<span class=\"sample-hl-structure\">I am writing to apply for the position of</span> <span class=\"sample-hl-vocab\">sales assistant</span> <span class=\"sample-hl-structure\">which was advertised on your website</span>.",
            "vi": "Tôi viết thư này để ứng tuyển vào vị trí nhân viên bán hàng được quảng cáo trên trang web của ông/bà.",
            "tip": "Mẫu câu mở đầu chuẩn mực kinh điển cho thư xin việc kèm mệnh đề quan hệ chỉ nguồn tin tuyển dụng."
        },
        "points": [
            {
                "num": "Ý 1",
                "title": "Giới thiệu bản thân & Trình độ học vấn (Self-intro & Education)",
                "en": "I recently graduated from Can Tho University with a bachelor’s degree in Business Administration. During my studies, I developed a strong understanding of marketing and customer service. I also gained useful knowledge and abilities such as communication and team collaboration.",
                "annotated": "I <span class=\"sample-hl-vocab\">recently graduated from</span> Can Tho University with a <span class=\"sample-hl-vocab\">bachelor’s degree in Business Administration</span>. During my studies, I <span class=\"sample-hl-structure\">developed a strong understanding of</span> marketing and customer service. I also <span class=\"sample-hl-structure\">gained useful knowledge and abilities such as</span> <span class=\"sample-hl-vocab\">communication and team collaboration</span>.",
                "vi": "Tôi vừa tốt nghiệp Đại học Cần Thơ với tấm bằng cử nhân ngành Quản trị Kinh doanh. Trong quá trình học, tôi đã phát triển sự hiểu biết sâu sắc về marketing và dịch vụ khách hàng. Tôi cũng tích lũy được những kiến thức và năng lực hữu ích như giao tiếp và làm việc nhóm.",
                "tip": "Trình bày học vấn và kỹ năng mềm thiết yếu (communication, team collaboration) bằng ngữ điệu trang trọng."
            },
            {
                "num": "Ý 2",
                "title": "Lý do hứng thú với vị trí (Why interested in the job)",
                "en": "I am very interested in this position because it matches my interests and career goals. In addition, I enjoy helping customers choose suitable fashion products. Therefore, I believe this job will give me a good opportunity to apply what I have learned during my studies and gain practical experience.",
                "annotated": "<span class=\"sample-hl-structure\">I am very interested in this position because</span> it <span class=\"sample-hl-vocab\">matches my interests and career goals</span>. <mark class=\"sample-hl-connector\">In addition,</mark> I enjoy helping customers choose suitable fashion products. <mark class=\"sample-hl-connector\">Therefore,</mark> <span class=\"sample-hl-structure\">I believe this job will give me a good opportunity to</span> apply what I have learned during my studies and <span class=\"sample-hl-vocab\">gain practical experience</span>.",
                "vi": "Tôi rất hứng thú với vị trí này vì nó phù hợp với sở thích và mục tiêu nghề nghiệp của tôi. Ngoài ra, tôi thích giúp đỡ khách hàng lựa chọn những sản phẩm thời trang phù hợp. Vì vậy, tôi tin rằng công việc này sẽ mang lại cho tôi cơ hội tốt để áp dụng những gì đã học trong quá trình học và tích lũy thêm kinh nghiệm thực tế.",
                "tip": "Liên kết lý do với mục tiêu sự nghiệp (career goals) và cơ hội học tập tích lũy thực tế (gain practical experience)."
            },
            {
                "num": "Ý 3",
                "title": "Kinh nghiệm làm việc với khách hàng (Customer experience)",
                "en": "I worked part-time as a sales assistant at a local clothing store. In this job, I was responsible for welcoming customers and arranging products. This experience helped me develop problem-solving skills and customer care skills.",
                "annotated": "I <span class=\"sample-hl-vocab\">worked part-time as a sales assistant</span> at a local clothing store. In this job, <span class=\"sample-hl-structure\">I was responsible for</span> welcoming customers and arranging products. This experience <span class=\"sample-hl-structure\">helped me develop</span> <span class=\"sample-hl-vocab\">problem-solving skills and customer care skills</span>.",
                "vi": "Tôi đã từng làm việc bán thời gian với tư cách là nhân viên bán hàng tại một cửa hàng quần áo địa phương. Trong công việc này, tôi chịu trách nhiệm đón tiếp khách hàng và sắp xếp sản phẩm. Kinh nghiệm này đã giúp tôi phát triển kỹ năng giải quyết vấn đề và kỹ năng chăm sóc khách hàng.",
                "tip": "Mẫu câu miêu tả trách nhiệm công việc: \"was responsible for + V-ing\" và các kỹ năng phát triển được."
            },
            {
                "num": "Ý 4",
                "title": "Phẩm chất nổi bật & Sự phù hợp (Suitability & Qualities)",
                "en": "I believe I would be a suitable candidate for this position. This is because I am enthusiastic, honest, and hardworking. Moreover, I am eager to learn and can adapt quickly to new environments.",
                "annotated": "<span class=\"sample-hl-structure\">I believe I would be a suitable candidate for this position</span>. This is because I am <span class=\"sample-hl-vocab\">enthusiastic, honest, and hardworking</span>. <mark class=\"sample-hl-connector\">Moreover,</mark> I am <span class=\"sample-hl-vocab\">eager to learn</span> and can <span class=\"sample-hl-vocab\">adapt quickly to new environments</span>.",
                "vi": "Tôi tin rằng mình sẽ là ứng cử viên phù hợp cho vị trí này. Điều này là vì tôi là người nhiệt tình, trung thực và làm việc chăm chỉ. Hơn nữa, tôi rất ham học hỏi và có thể thích nghi nhanh chóng với môi trường mới.",
                "tip": "Khẳng định sự phù hợp với các phẩm chất sáng giá: \"enthusiastic, honest, hardworking\", \"eager to learn\", \"adapt quickly\"."
            }
        ],
        "closing": {
            "en": "I would be grateful if you could consider my application. I look forward to receiving your reply soon.",
            "annotated": "<span class=\"sample-hl-structure\">I would be grateful if you could consider my application.</span> <span class=\"sample-hl-structure\">I look forward to receiving your reply soon.</span>",
            "vi": "Tôi sẽ rất biết ơn nếu ông/bà có thể xem xét hồ sơ ứng tuyển của tôi. Tôi rất mong sớm nhận được phản hồi từ ông/bà.",
            "tip": "Cấu trúc đề nghị trang trọng bậc nhất: \"I would be grateful if you could...\" và câu kết chuẩn mực."
        },
        "signoff": {
            "en": "Yours faithfully,",
            "vi": "Trân trọng,",
            "tip": "Ký tên trang trọng chuẩn VSTEP."
        },
        "takeaways": {
            "task": "Bao quát toàn diện 4 tiêu chuẩn thư xin việc: lý do ứng tuyển, bằng cấp và kỹ năng, kinh nghiệm bán hàng thực tế, và phẩm chất cá nhân.",
            "coherence": "Bố cục logic chặt chẽ, đoạn văn mạch lạc, từ nối trang trọng (In addition, Therefore, Moreover).",
            "lexical": "Từ vựng tuyển dụng cao cấp: bachelor’s degree, career goals, practical experience, problem-solving skills, eager to learn, adapt quickly.",
            "grammar": "Mệnh đề quan hệ, câu điều kiện lịch sự 'would be grateful if you could', cấu trúc bị động và thì quá khứ đơn."
        }
    }
}

CLEAN_FILLED_LETTERS = {
    "advice": {
        "en": "<strong>Dear <span class=\"sample-filled-info filled-c1\">Helen</span>,</strong>\n<p>Thanks for your letter. I hope you are doing well. I’m writing to give you some advice for <span class=\"sample-filled-info filled-c2\">your trip to Hanoi in June</span>.</p>\n<p>Firstly, you should <span class=\"sample-filled-info filled-c3\">stay in a hotel in the city center because it is very convenient for travelling. Many famous places are also located near this area</span>. Secondly, it would be a good idea to <span class=\"sample-filled-info filled-c4\">try some traditional Vietnamese dishes such as pho, banh mi, and bun cha. These dishes are very popular and delicious</span>. Next, if I were you, I would <span class=\"sample-filled-info filled-c5\">visit some famous places in Hanoi such as Hoan Kiem Lake, the Old Quarter, and the Temple of Literature. These places are very beautiful and interesting</span>. Finally, remember to <span class=\"sample-filled-info filled-c6\">wear light and comfortable clothes because the weather in Hanoi can be quite hot in June</span>.</p>\n<p>I hope my advice will be helpful to you. Please let me know how everything turns out. Write back soon.</p>\n<strong>Best wishes,</strong>",
        "vi": "<strong style=\"color: var(--text-main); display: block; margin-bottom: 14px;\"><span class=\"sample-filled-info filled-c1\">Helen</span> thân mến,</strong>\n<p>Cảm ơn thư của cậu. Tớ hy vọng cậu vẫn khỏe. Tớ viết thư này để đưa ra một vài gợi ý cho <span class=\"sample-filled-info filled-c2\">chuyến đi của cậu đến Hà Nội vào tháng Sáu</span>.</p>\n<p>Đầu tiên, cậu nên <span class=\"sample-filled-info filled-c3\">ở một khách sạn tại trung tâm thành phố vì nó rất thuận tiện cho việc đi lại. Nhiều địa điểm nổi tiếng cũng nằm gần khu vực này</span>. Thứ hai, cậu nên <span class=\"sample-filled-info filled-c4\">thử một số món ăn truyền thống của Việt Nam như phở, bánh mì và bún chả. Những món ăn này rất phổ biến và ngon miệng</span>. Tiếp theo, nếu tớ là cậu, tớ sẽ <span class=\"sample-filled-info filled-c5\">tham quan một số địa điểm nổi tiếng ở Hà Nội như hồ Hoàn Kiếm, phố cổ và Văn Miếu Quốc Tử Giám. Những nơi này rất đẹp và thú vị</span>. Cuối cùng, hãy nhớ <span class=\"sample-filled-info filled-c6\">mặc quần áo mỏng nhẹ và thoải mái vì thời tiết Hà Nội vào tháng Sáu có thể khá nóng</span>.</p>\n<p>Tớ hy vọng những lời khuyên của tớ sẽ giúp ích cho cậu. Hãy cho tớ biết chuyến đi diễn ra thế nào nhé. Hãy viết thư lại sớm nhé.</p>\n<strong style=\"color: var(--text-main); display: block; margin-top: 14px;\">Chúc cậu mọi điều tốt lành,</strong>"
    },
    "request": {
        "en": "<strong>Dear <span class=\"sample-filled-info filled-c1\">Moonie</span>,</strong>\n<p>How are you? I hope you are doing well. I’m writing to ask for some information about <span class=\"sample-filled-info filled-c2\">the English course at Rainbow Language Center</span> because <span class=\"sample-filled-info filled-c2\">I am planning to study English there soon</span>.</p>\n<p>First of all, could you tell me <span class=\"sample-filled-info filled-c3\">the address of the center</span>? I want to know <span class=\"sample-filled-info filled-c3\">if it is near my house</span>. In addition, I would like to know about <span class=\"sample-filled-info filled-c4\">the tuition fee for the course</span> so that <span class=\"sample-filled-info filled-c4\">I can prepare my budget</span>. Furthermore, can you tell me more about <span class=\"sample-filled-info filled-c5\">the teachers</span>? Are they <span class=\"sample-filled-info filled-c5\">friendly and experienced</span>? Finally, I was wondering if you could give me some details about <span class=\"sample-filled-info filled-c6\">the training program and the class schedule</span>.</p>\n<p>I hope you can help me with this. Write back soon.</p>\n<strong>Best wishes,</strong>",
        "vi": "<strong style=\"color: var(--text-main); display: block; margin-bottom: 14px;\"><span class=\"sample-filled-info filled-c1\">Moonie</span> thân mến,</strong>\n<p>Cậu dạo này thế nào? Tớ hy vọng cậu vẫn khỏe. Tớ viết thư này để hỏi xin một vài thông tin về <span class=\"sample-filled-info filled-c2\">khóa học tiếng Anh tại Trung tâm Ngoại ngữ Rainbow</span> vì <span class=\"sample-filled-info filled-c2\">tớ đang có kế hoạch học tiếng Anh ở đó trong thời gian tới</span>.</p>\n<p>Trước hết, cậu có thể cho tớ biết <span class=\"sample-filled-info filled-c3\">địa chỉ của trung tâm</span> được không? Tớ muốn biết <span class=\"sample-filled-info filled-c3\">liệu nó có ở gần nhà tớ không</span>. Ngoài ra, tớ cũng muốn biết về <span class=\"sample-filled-info filled-c4\">mức học phí của khóa học</span> để <span class=\"sample-filled-info filled-c4\">tớ có thể chuẩn bị ngân sách</span>. Hơn nữa, cậu có thể kể thêm cho tớ về <span class=\"sample-filled-info filled-c5\">các thầy cô giáo</span> không? Họ có <span class=\"sample-filled-info filled-c5\">thân thiện và giàu kinh nghiệm</span> không? Cuối cùng, tớ đang băn khoăn không biết cậu có thể chia sẻ cho tớ một vài chi tiết về <span class=\"sample-filled-info filled-c6\">chương trình đào tạo và lịch học</span> được không.</p>\n<p>Tớ hy vọng cậu có thể giúp tớ việc này nhé. Hãy viết thư lại cho tớ sớm nhé.</p>\n<strong style=\"color: var(--text-main); display: block; margin-top: 14px;\">Chúc cậu mọi điều tốt lành,</strong>"
    },
    "description": {
        "en": "<strong>Dear <span class=\"sample-filled-info filled-c1\">Emily</span>,</strong>\n<p>How are you? I hope you are doing well. In your letter, you asked me about <span class=\"sample-filled-info filled-c2\">my friend Hoa</span>, so here is some information.</p>\n<p>Firstly, she is <span class=\"sample-filled-info filled-c3\">a very kind and friendly person. She gets on well with everyone and is always willing to help others</span>. Secondly, in her free time, she likes <span class=\"sample-filled-info filled-c4\">reading books, cooking traditional Vietnamese food, and listening to music. I think she would be happy to cook some delicious meals for your family</span>. Finally, she is <span class=\"sample-filled-info filled-c5\">currently studying business at university and works very hard. She is responsible and always keeps her room tidy</span>. Therefore, I believe she will <span class=\"sample-filled-info filled-c6\">fit in very well with your family</span>.</p>\n<p>I hope you will find this information useful. Let me know if you need more details.</p>\n<strong>Best wishes,</strong>",
        "vi": "<strong style=\"color: var(--text-main); display: block; margin-bottom: 14px;\"><span class=\"sample-filled-info filled-c1\">Emily</span> thân mến,</strong>\n<p>Cậu dạo này thế nào? Tớ hy vọng cậu vẫn khỏe. Trong thư trước, cậu có hỏi tớ về <span class=\"sample-filled-info filled-c2\">bạn Hoa của tớ</span>, vậy nên dưới đây là một số thông tin nhé.</p>\n<p>Đầu tiên, cô ấy là <span class=\"sample-filled-info filled-c3\">một người rất tốt bụng và thân thiện. Cô ấy hòa thuận với tất cả mọi người và luôn sẵn lòng giúp đỡ người khác</span>. Thứ hai, trong thời gian rảnh, cô ấy thích <span class=\"sample-filled-info filled-c4\">đọc sách, nấu các món ăn truyền thống của Việt Nam và nghe nhạc. Tớ nghĩ cô ấy sẽ rất vui khi được nấu một vài bữa ăn ngon cho gia đình cậu</span>. Cuối cùng, cô ấy hiện <span class=\"sample-filled-info filled-c5\">đang học ngành kinh doanh tại trường đại học và học tập rất chăm chỉ. Cô ấy là người có trách nhiệm và luôn giữ phòng ngủ ngăn nắp</span>. Vì vậy, tớ tin rằng cô ấy sẽ <span class=\"sample-filled-info filled-c6\">hòa nhập rất tốt với gia đình cậu</span>.</p>\n<p>Tớ hy vọng cậu sẽ thấy những thông tin này hữu ích. Hãy cho tớ biết nếu cậu cần thêm chi tiết nhé.</p>\n<strong style=\"color: var(--text-main); display: block; margin-top: 14px;\">Chúc cậu mọi điều tốt lành,</strong>"
    },
    "complaint": {
        "en": "<strong>Dear Sir/Madam,</strong>\n<p>I am writing to complain about <span class=\"sample-filled-info filled-c2\">the condition of the changing room at your sports center</span>. I recently used the facility and was not satisfied with it.</p>\n<p>The main problem was that <span class=\"sample-filled-info filled-c3\">the floor was very dirty and wet, which was quite dangerous for members</span>. Another issue was that <span class=\"sample-filled-info filled-c4\">several lockers were broken, so I could not safely store my personal belongings</span>. Finally, I also found that <span class=\"sample-filled-info filled-c5\">some of the showers did not have hot water</span>. I was very disappointed with these problems because I have always enjoyed using your center. Therefore, I would appreciate it if you could <span class=\"sample-filled-info filled-c6\">clean the changing room more regularly, repair the broken lockers, and fix the showers as soon as possible</span>.</p>\n<p>I hope that you will look into these issues soon. I look forward to receiving your reply soon.</p>\n<strong>Yours faithfully,</strong>",
        "vi": "<strong style=\"color: var(--text-main); display: block; margin-bottom: 14px;\">Kính gửi Ông/Bà,</strong>\n<p>Tôi viết thư này để phàn nàn về <span class=\"sample-filled-info filled-c2\">tình trạng của phòng thay đồ tại trung tâm thể thao của ông/bà</span>. Gần đây tôi đã sử dụng cơ sở vật chất này và không hài lòng với nó.</p>\n<p>Vấn đề chính là <span class=\"sample-filled-info filled-c3\">sàn nhà rất bẩn và ẩm ướt, điều này khá nguy hiểm cho các hội viên</span>. Một vấn đề khác là <span class=\"sample-filled-info filled-c4\">một số tủ đựng đồ bị hỏng, vì vậy tôi không thể cất giữ đồ dùng cá nhân của mình một cách an toàn</span>. Cuối cùng, tôi cũng nhận thấy <span class=\"sample-filled-info filled-c5\">một số vòi hoa sen không có nước nóng</span>. Tôi rất thất vọng với những vấn đề này vì tôi luôn thích sử dụng trung tâm của ông/bà. Do đó, tôi sẽ rất cảm kích nếu ông/bà có thể <span class=\"sample-filled-info filled-c6\">dọn dẹp phòng thay đồ thường xuyên hơn, sửa chữa các tủ đựng đồ bị hỏng và sửa lại các vòi hoa sen càng sớm càng tốt</span>.</p>\n<p>Tôi hy vọng ông/bà sẽ sớm xem xét các vấn đề này. Tôi rất mong sớm nhận được phản hồi từ ông/bà.</p>\n<strong style=\"color: var(--text-main); display: block; margin-top: 14px;\">Trân trọng,</strong>"
    },
    "feedback": {
        "en": "<strong>Dear Sir/Madam,</strong>\n<p>I am writing to give you feedback on <span class=\"sample-filled-info filled-c2\">my recent stay at your hotel</span>. I recently used your services and would like to share my experience.</p>\n<p>First of all, I would like to mention some positive points about your hotel. I was very satisfied with <span class=\"sample-filled-info filled-c3\">the customer service because the staff were polite, friendly, and always ready to assist guests</span>. In addition, <span class=\"sample-filled-info filled-c4\">the room was spacious and clean</span>. However, there were also some areas that needed improvement. I was disappointed with <span class=\"sample-filled-info filled-c5\">the Wi-Fi connection because it was slow and unstable</span>. Furthermore, <span class=\"sample-filled-info filled-c5\">the breakfast menu was quite limited and lacked variety</span>. To enhance the quality of your services, I suggest that you should <span class=\"sample-filled-info filled-c6\">upgrade the Internet system and offer more options for breakfast</span>.</p>\n<p>I hope my feedback will help you improve your service. Please feel free to contact me if you have any further questions.</p>\n<strong>Yours faithfully,</strong>",
        "vi": "<strong style=\"color: var(--text-main); display: block; margin-bottom: 14px;\">Kính gửi Ông/Bà,</strong>\n<p>Tôi viết thư này để đưa ra phản hồi về <span class=\"sample-filled-info filled-c2\">kỳ nghỉ gần đây của tôi tại khách sạn của ông/bà</span>. Gần đây tôi đã sử dụng dịch vụ của ông/bà và muốn chia sẻ trải nghiệm của mình.</p>\n<p>Trước hết, tôi muốn đề cập đến một số điểm tích cực về khách sạn của ông/bà. Tôi rất hài lòng với <span class=\"sample-filled-info filled-c3\">dịch vụ chăm sóc khách hàng vì nhân viên rất lịch sự, thân thiện và luôn sẵn sàng hỗ trợ khách</span>. Ngoài ra, <span class=\"sample-filled-info filled-c4\">phòng ốc rất rộng rãi và sạch sẽ</span>. Tuy nhiên, cũng có một số khía cạnh cần được cải thiện. Tôi đã thất vọng với <span class=\"sample-filled-info filled-c5\">kết nối Wi-Fi vì nó chậm và không ổn định</span>. Hơn nữa, <span class=\"sample-filled-info filled-c5\">thực đơn bữa sáng khá hạn chế và thiếu sự đa dạng</span>. Để nâng cao chất lượng dịch vụ của ông/bà, tôi đề nghị ông/bà nên <span class=\"sample-filled-info filled-c6\">nâng cấp hệ thống Internet và cung cấp nhiều sự lựa chọn hơn cho bữa sáng</span>.</p>\n<p>Tôi hy vọng phản hồi của tôi sẽ giúp ông/bà cải thiện dịch vụ của mình. Xin vui lòng liên hệ với tôi nếu ông/bà có bất kỳ câu hỏi nào thêm.</p>\n<strong style=\"color: var(--text-main); display: block; margin-top: 14px;\">Trân trọng,</strong>"
    },
    "apology": {
        "en": "<strong>Dear <span class=\"sample-filled-info filled-c1\">Helen</span>,</strong>\n<p>I’m really sorry for <span class=\"sample-filled-info filled-c2\">not returning your book earlier</span>. Let me explain what happened so you can understand the situation.</p>\n<p>First of all, let me explain why this happened. I’m really sorry that I couldn’t <span class=\"sample-filled-info filled-c3\">return the book on time because I have been extremely busy preparing for my final exams. During that time, I had several assignments and an important test. As a result, I completely forgot about the book</span>. In addition, <span class=\"sample-filled-info filled-c4\">I have finished reading the whole book and found it very interesting and helpful</span>. Next, <span class=\"sample-filled-info filled-c5\">I plan to give it back to you this Saturday. I can come over to your house in the afternoon to return it in person</span>. Finally, let me make it up to you by <span class=\"sample-filled-info filled-c6\">treating you to a cup of milk tea and some snacks</span>.</p>\n<p>Sorry once again. Thanks for taking the time to read this. Write back soon.</p>\n<strong>Best wishes,</strong>",
        "vi": "<strong style=\"color: var(--text-main); display: block; margin-bottom: 14px;\"><span class=\"sample-filled-info filled-c1\">Helen</span> thân mến,</strong>\n<p>Tớ thực sự xin lỗi vì <span class=\"sample-filled-info filled-c2\">đã không trả sách cho cậu sớm hơn</span>. Hãy để tớ giải thích những gì đã xảy ra để cậu hiểu rõ tình hình nhé.</p>\n<p>Trước hết, hãy để tớ giải thích tại sao chuyện này lại xảy ra. Tớ thực sự xin lỗi vì tớ đã không thể <span class=\"sample-filled-info filled-c3\">trả sách đúng hạn vì tớ quá bận rộn chuẩn bị cho kỳ thi cuối kỳ. Trong thời gian đó, tớ có vài bài tập lớn và một bài kiểm tra quan trọng. Kết quả là tớ hoàn toàn quên mất cuốn sách</span>. Ngoài ra, <span class=\"sample-filled-info filled-c4\">tớ đã đọc xong toàn bộ cuốn sách và thấy nó rất thú vị và bổ ích</span>. Tiếp theo, <span class=\"sample-filled-info filled-c5\">tớ dự định sẽ trả lại sách cho cậu vào thứ Bảy tuần này. Tớ có thể ghé qua nhà cậu vào buổi chiều để trực tiếp gửi lại sách</span>. Cuối cùng, hãy để tớ bù đắp cho cậu bằng <span class=\"sample-filled-info filled-c6\">một chầu trà sữa và đồ ăn vặt nhé</span>.</p>\n<p>Xin lỗi cậu một lần nữa nhé. Cảm ơn cậu vì đã dành thời gian đọc thư này. Hãy viết thư lại cho tớ sớm nhé.</p>\n<strong style=\"color: var(--text-main); display: block; margin-top: 14px;\">Chúc cậu mọi điều tốt lành,</strong>"
    },
    "application": {
        "en": "<strong>Dear Sir/Madam,</strong>\n<p>I am writing to apply for the position of <span class=\"sample-filled-info filled-c1\">sales assistant</span> which was advertised on <span class=\"sample-filled-info filled-c2\">your website</span>.</p>\n<p>I recently graduated from <span class=\"sample-filled-info filled-c3\">Can Tho University</span> with a bachelor’s degree in <span class=\"sample-filled-info filled-c3\">Business Administration</span>. During my studies, I developed a strong understanding of <span class=\"sample-filled-info filled-c3\">marketing and customer service</span>. I also gained useful knowledge and abilities such as <span class=\"sample-filled-info filled-c3\">communication and team collaboration</span>.</p>\n<p>I am very interested in this position because it matches my interests and career goals. In addition, I enjoy <span class=\"sample-filled-info filled-c4\">helping customers choose suitable fashion products</span>. Therefore, I believe this job will give me a good opportunity to apply what I have learned during my studies and gain practical experience.</p>\n<p>I worked part-time as a <span class=\"sample-filled-info filled-c5\">sales assistant</span> at a <span class=\"sample-filled-info filled-c5\">local clothing store</span>. In this job, I was responsible for <span class=\"sample-filled-info filled-c5\">welcoming customers and arranging products</span>. This experience helped me develop <span class=\"sample-filled-info filled-c5\">problem-solving skills and customer care skills</span>.</p>\n<p>I believe I would be a suitable candidate for this position. This is because I am <span class=\"sample-filled-info filled-c6\">enthusiastic, honest, and hardworking</span>. Moreover, I am eager to learn and can adapt quickly to new environments.</p>\n<p>I would be grateful if you could consider my application. I look forward to receiving your reply soon.</p>\n<strong>Yours faithfully,</strong>",
        "vi": "<strong style=\"color: var(--text-main); display: block; margin-bottom: 14px;\">Kính gửi Ông/Bà,</strong>\n<p>Tôi viết thư này để ứng tuyển vào vị trí <span class=\"sample-filled-info filled-c1\">nhân viên bán hàng</span> được quảng cáo trên <span class=\"sample-filled-info filled-c2\">trang web của ông/bà</span>.</p>\n<p>Tôi vừa tốt nghiệp <span class=\"sample-filled-info filled-c3\">Đại học Cần Thơ</span> với tấm bằng cử nhân ngành <span class=\"sample-filled-info filled-c3\">Quản trị Kinh doanh</span>. Trong quá trình học, tôi đã phát triển sự hiểu biết sâu sắc về <span class=\"sample-filled-info filled-c3\">marketing và dịch vụ khách hàng</span>. Tôi cũng tích lũy được những kiến thức và năng lực hữu ích như <span class=\"sample-filled-info filled-c3\">giao tiếp và làm việc nhóm</span>.</p>\n<p>Tôi rất hứng thú với vị trí này vì nó phù hợp với sở thích và mục tiêu nghề nghiệp của tôi. Ngoài ra, tôi thích <span class=\"sample-filled-info filled-c4\">giúp đỡ khách hàng lựa chọn những sản phẩm thời trang phù hợp</span>. Vì vậy, tôi tin rằng công việc này sẽ mang lại cho tôi cơ hội tốt để áp dụng những gì đã học trong quá trình học và tích lũy thêm kinh nghiệm thực tế.</p>\n<p>Tôi đã từng làm việc bán thời gian với tư cách là <span class=\"sample-filled-info filled-c5\">nhân viên bán hàng</span> tại một <span class=\"sample-filled-info filled-c5\">cửa hàng quần áo địa phương</span>. Trong công việc này, tôi chịu trách nhiệm <span class=\"sample-filled-info filled-c5\">đón tiếp khách hàng và sắp xếp sản phẩm</span>. Kinh nghiệm này đã giúp tôi phát triển <span class=\"sample-filled-info filled-c5\">kỹ năng giải quyết vấn đề và kỹ năng chăm sóc khách hàng</span>.</p>\n<p>Tôi tin rằng mình sẽ là ứng cử viên phù hợp cho vị trí này. Điều này là vì tôi là người <span class=\"sample-filled-info filled-c6\">nhiệt tình, trung thực và làm việc chăm chỉ</span>. Hơn nữa, tôi rất ham học hỏi và có thể thích nghi nhanh chóng với môi trường mới.</p>\n<p>Tôi sẽ rất biết ơn nếu ông/bà có thể xem xét hồ sơ ứng tuyển của tôi. Tôi rất mong sớm nhận được phản hồi từ ông/bà.</p>\n<strong style=\"color: var(--text-main); display: block; margin-top: 14px;\">Trân trọng,</strong>"
    }
}

def generate_sample_html(type_id, data, prompt_container_html):
    """
    Generates the complete enhanced HTML for a letter type.
    """
    full_en_text = "\\n\\n".join([
        data["salutation"]["en"],
        data["opening"]["en"],
        "\\n\\n".join([p["en"] for p in data["points"]]),
        data["closing"]["en"],
        data["signoff"]["en"]
    ]).replace('"', '\\"')

    # Build View 1: Annotated Structure
    annotated_html = f'''
        <div id="sampleViewAnnotated" class="sample-view-content active">
            <!-- Quick Link to Clean Letter -->
            <div class="clean-letter-quick-banner" style="background: var(--bg-card); border: 1px dashed var(--primary-color); border-radius: 10px; padding: 12px 18px; margin-bottom: 16px; display: flex; align-items: center; justify-content: space-between; gap: 12px; flex-wrap: wrap;">
                <div style="font-size: 13.5px; font-weight: 600; color: var(--text-main);">
                    <i class="fa-solid fa-book-open-reader" style="color: var(--primary-color); margin-right: 6px;"></i> Bạn muốn đọc hoặc học thuộc trọn vẹn bức thư liền mạch không chú thích?
                </div>
                <button type="button" class="btn btn-outline" onclick="switchSampleView('sampleViewClean', document.querySelector('[data-view=\'sampleViewClean\']'))" style="font-size: 12.5px; padding: 6px 14px; border-radius: 6px; cursor: pointer; border-color: var(--primary-color); color: var(--primary-color); font-weight: 600;">
                    <i class="fa-solid fa-file-lines"></i> Mở Bản Đầy Đủ Không Chú Thích <i class="fa-solid fa-arrow-right"></i>
                </button>
            </div>

            <!-- Filter Bar -->
            <div class="sample-filter-bar">
                <div class="sample-filter-title">
                    <i class="fa-solid fa-highlighter"></i> BẬT / TẮT ĐIỂM SÁNG B1:
                </div>
                <div class="sample-filter-pills">
                    <span class="filter-pill pill-connector" onclick="toggleSampleHighlight('connectors')">
                        <i class="fa-solid fa-check"></i> Từ nối liên kết
                    </span>
                    <span class="filter-pill pill-structure" onclick="toggleSampleHighlight('structures')">
                        <i class="fa-solid fa-check"></i> Cấu trúc ăn điểm B1
                    </span>
                    <span class="filter-pill pill-vocab" onclick="toggleSampleHighlight('vocabs')">
                        <i class="fa-solid fa-check"></i> Từ vựng chủ đề
                    </span>
                </div>
            </div>

            <!-- Section 1: Salutation -->
            <div class="sample-section-card">
                <div class="sample-section-header">
                    <span class="sample-section-badge"><i class="fa-solid fa-handshake"></i> 1. LỜI CHÀO (SALUTATION)</span>
                    <button class="sample-section-btn-audio" onclick="speakText('{data["salutation"]["en"]}')" title="Nghe câu này">
                        <i class="fa-solid fa-volume-high"></i>
                    </button>
                </div>
                <div class="sample-section-body">
                    <strong>{data["salutation"]["en"]}</strong>
                    <div class="sample-section-note">
                        <i class="fa-solid fa-circle-info"></i> {data["salutation"]["tip"]}
                    </div>
                </div>
            </div>

            <!-- Section 2: Opening -->
            <div class="sample-section-card">
                <div class="sample-section-header">
                    <span class="sample-section-badge"><i class="fa-solid fa-compass"></i> 2. MỞ BÀI & MỤC ĐÍCH (OPENING & PURPOSE)</span>
                    <button class="sample-section-btn-audio" onclick="speakText('{data["opening"]["en"]}')" title="Nghe câu này">
                        <i class="fa-solid fa-volume-high"></i>
                    </button>
                </div>
                <div class="sample-section-body">
                    <p>{data["opening"]["annotated"]}</p>
                    <div class="sample-section-note">
                        <i class="fa-solid fa-circle-info"></i> {data["opening"]["tip"]}
                    </div>
                </div>
            </div>

            <!-- Section 3: Body 4 Points -->
            <div class="sample-section-card">
                <div class="sample-section-header">
                    <span class="sample-section-badge"><i class="fa-solid fa-list-check"></i> 3. THÂN BÀI (BODY - 4 Ý ĐỀ BÀI)</span>
                </div>
                <div class="sample-section-body">
                    <div class="sample-body-grid">
    '''

    for p in data["points"]:
        annotated_html += f'''
                        <div class="sample-point-card">
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <div class="sample-point-tag"><i class="fa-solid fa-star"></i> {p["num"]}: {p["title"]}</div>
                                <button class="sample-section-btn-audio" onclick="speakText('{p["en"]}')" title="Nghe đoạn này">
                                    <i class="fa-solid fa-volume-high"></i>
                                </button>
                            </div>
                            <div class="sample-point-text">{p["annotated"]}</div>
                            <div class="sample-section-note" style="margin-top: 8px;">
                                <i class="fa-solid fa-lightbulb"></i> {p["tip"]}
                            </div>
                        </div>
        '''

    annotated_html += f'''
                    </div>
                </div>
            </div>

            <!-- Section 4: Closing -->
            <div class="sample-section-card">
                <div class="sample-section-header">
                    <span class="sample-section-badge"><i class="fa-solid fa-envelope-open-text"></i> 4. KẾT THƯ & HẸN HỒI ĐÁP (CLOSING)</span>
                    <button class="sample-section-btn-audio" onclick="speakText('{data["closing"]["en"]}')" title="Nghe câu này">
                        <i class="fa-solid fa-volume-high"></i>
                    </button>
                </div>
                <div class="sample-section-body">
                    <p>{data["closing"]["annotated"]}</p>
                    <div class="sample-section-note">
                        <i class="fa-solid fa-circle-info"></i> {data["closing"]["tip"]}
                    </div>
                </div>
            </div>

            <!-- Section 5: Sign-off -->
            <div class="sample-section-card">
                <div class="sample-section-header">
                    <span class="sample-section-badge"><i class="fa-solid fa-signature"></i> 5. LỜI CHÀO KẾT THÚC & KÝ TÊN (SIGN-OFF)</span>
                    <button class="sample-section-btn-audio" onclick="speakText('{data["signoff"]["en"]}')" title="Nghe câu này">
                        <i class="fa-solid fa-volume-high"></i>
                    </button>
                </div>
                <div class="sample-section-body">
                    <strong>{data["signoff"]["en"]}</strong>
                    <div class="sample-section-note">
                        <i class="fa-solid fa-circle-info"></i> {data["signoff"]["tip"]}
                    </div>
                </div>
            </div>
        </div>
    '''

    # Build View 2: Clean Letter View (Full Letter with filled-in information highlighted)
    clean_en_content = CLEAN_FILLED_LETTERS[type_id]["en"]
    clean_vi_content = CLEAN_FILLED_LETTERS[type_id]["vi"]

    clean_html = f'''
        <div id="sampleViewClean" class="sample-view-content" style="display: none;">
            <!-- Header for English Clean Letter -->
            <div class="clean-view-header" style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; flex-wrap: wrap; gap: 10px;">
                <div style="font-size: 15px; font-weight: 700; color: var(--primary-color); display: flex; align-items: center; gap: 8px;">
                    <i class="fa-solid fa-envelope-open-text"></i> TOÀN VĂN LÁ THƯ TIẾNG ANH (BẢN CHUẨN THI - THÔNG TIN THẾ VÀO ĐƯỢC LÀM NỔI BẬT)
                </div>
                <button class="btn-sample-audio" onclick="playCurrentSampleLetter()" title="Nghe đọc toàn bộ bức thư này" style="padding: 6px 14px; font-size: 12.5px;">
                    <i class="fa-solid fa-volume-high"></i> Nghe đọc bản này
                </button>
            </div>

            <!-- Authentic Stationery Box (Clean English Letter) -->
            <div class="sample-letter-box">
                {clean_en_content}
            </div>

            <!-- Header for Vietnamese Clean Translation -->
            <div class="clean-view-header" style="display: flex; align-items: center; justify-content: space-between; margin-top: 28px; margin-bottom: 12px;">
                <div style="font-size: 15px; font-weight: 700; color: #059669; display: flex; align-items: center; gap: 8px;">
                    <i class="fa-solid fa-language"></i> BẢN DỊCH TIẾNG VIỆT HOÀN CHỈNH (THÔNG TIN THẾ VÀO ĐƯỢC LÀM NỔI BẬT)
                </div>
            </div>

            <!-- Clean Translation Box (Clean Vietnamese Letter) -->
            <div class="translation-box" style="background-color: var(--bg-card); border: 1px solid var(--border-color); padding: 25px 32px; border-radius: 12px; font-family: var(--font-body); line-height: 1.85; color: var(--text-main); box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03);">
                {clean_vi_content}
            </div>
        </div>
    '''

    # Build View 3: Bilingual View
    bilingual_html = f'''
        <div id="sampleViewBilingual" class="sample-view-content" style="display: none;">
            <!-- Salutation Row -->
            <div class="bilingual-row">
                <div class="bilingual-col-en">
                    <div class="bilingual-header-tag">
                        <span>LỜI CHÀO</span>
                        <button class="sample-section-btn-audio" onclick="speakText('{data["salutation"]["en"]}')"><i class="fa-solid fa-volume-high"></i></button>
                    </div>
                    <strong>{data["salutation"]["en"]}</strong>
                </div>
                <div class="bilingual-col-vi">
                    <div class="bilingual-header-tag"><span>TIẾNG VIỆT</span></div>
                    <strong>{data["salutation"]["vi"]}</strong>
                </div>
            </div>

            <!-- Opening Row -->
            <div class="bilingual-row">
                <div class="bilingual-col-en">
                    <div class="bilingual-header-tag">
                        <span>MỞ BÀI & MỤC ĐÍCH</span>
                        <button class="sample-section-btn-audio" onclick="speakText('{data["opening"]["en"]}')"><i class="fa-solid fa-volume-high"></i></button>
                    </div>
                    {data["opening"]["en"]}
                </div>
                <div class="bilingual-col-vi">
                    <div class="bilingual-header-tag"><span>TIẾNG VIỆT</span></div>
                    {data["opening"]["vi"]}
                </div>
            </div>
    '''

    for p in data["points"]:
        bilingual_html += f'''
            <!-- Point Row -->
            <div class="bilingual-row">
                <div class="bilingual-col-en">
                    <div class="bilingual-header-tag">
                        <span>{p["num"]}: {p["title"]}</span>
                        <button class="sample-section-btn-audio" onclick="speakText('{p["en"]}')"><i class="fa-solid fa-volume-high"></i></button>
                    </div>
                    {p["en"]}
                </div>
                <div class="bilingual-col-vi">
                    <div class="bilingual-header-tag"><span>TIẾNG VIỆT</span></div>
                    {p["vi"]}
                </div>
            </div>
        '''

    bilingual_html += f'''
            <!-- Closing Row -->
            <div class="bilingual-row">
                <div class="bilingual-col-en">
                    <div class="bilingual-header-tag">
                        <span>KẾT THƯ</span>
                        <button class="sample-section-btn-audio" onclick="speakText('{data["closing"]["en"]}')"><i class="fa-solid fa-volume-high"></i></button>
                    </div>
                    {data["closing"]["en"]}
                </div>
                <div class="bilingual-col-vi">
                    <div class="bilingual-header-tag"><span>TIẾNG VIỆT</span></div>
                    {data["closing"]["vi"]}
                </div>
            </div>

            <!-- Sign-off Row -->
            <div class="bilingual-row">
                <div class="bilingual-col-en">
                    <div class="bilingual-header-tag">
                        <span>KÝ TÊN</span>
                        <button class="sample-section-btn-audio" onclick="speakText('{data["signoff"]["en"]}')"><i class="fa-solid fa-volume-high"></i></button>
                    </div>
                    <strong>{data["signoff"]["en"]}</strong>
                </div>
                <div class="bilingual-col-vi">
                    <div class="bilingual-header-tag"><span>TIẾNG VIỆT</span></div>
                    <strong>{data["signoff"]["vi"]}</strong>
                </div>
            </div>
        </div>
    '''

    # Build Examiner's Takeaways Card
    takeaways_html = f'''
        <div class="examiner-card">
            <div class="examiner-header">
                <i class="fa-solid fa-award"></i> BÍ QUYẾT GIÁM KHẢO: PHÂN TÍCH ĐIỂM CAO 4 TIÊU CHÍ VSTEP
            </div>
            <div class="examiner-grid">
                <div class="examiner-item">
                    <div class="examiner-item-title" style="color: #2563eb;">
                        <i class="fa-solid fa-bullseye"></i> 1. Task Fulfillment (Hoàn thành nhiệm vụ)
                    </div>
                    <p class="examiner-item-desc">{data["takeaways"]["task"]}</p>
                </div>
                <div class="examiner-item">
                    <div class="examiner-item-title" style="color: #059669;">
                        <i class="fa-solid fa-link"></i> 2. Coherence & Cohesion (Mạch lạc & Liên kết)
                    </div>
                    <p class="examiner-item-desc">{data["takeaways"]["coherence"]}</p>
                </div>
                <div class="examiner-item">
                    <div class="examiner-item-title" style="color: #d97706;">
                        <i class="fa-solid fa-book-bookmark"></i> 3. Lexical Resource (Vốn từ vựng)
                    </div>
                    <p class="examiner-item-desc">{data["takeaways"]["lexical"]}</p>
                </div>
                <div class="examiner-item">
                    <div class="examiner-item-title" style="color: #dc2626;">
                        <i class="fa-solid fa-pen-ruler"></i> 4. Grammatical Range (Ngữ pháp đa dạng)
                    </div>
                    <p class="examiner-item-desc">{data["takeaways"]["grammar"]}</p>
                </div>
            </div>
        </div>
    '''

    # Complete Template
    final_html = f'''
        {prompt_container_html}

        <div class="content-block">
            <!-- Toolbar Card -->
            <div class="sample-toolbar-card">
                <div class="sample-metrics-group">
                    <span class="sample-metric-chip accent-words">
                        <i class="fa-solid fa-file-lines"></i> {data["wordCount"]} từ (Đạt chuẩn 120-150 từ)
                    </span>
                    <span class="sample-metric-chip {data["toneBadge"]}">
                        <i class="fa-solid fa-tag"></i> {data["tone"]}
                    </span>
                    <span class="sample-metric-chip accent-band">
                        <i class="fa-solid fa-medal"></i> Chuẩn VSTEP B1+
                    </span>
                    <span class="sample-metric-chip">
                        <i class="fa-solid fa-clock"></i> 20 Phút
                    </span>
                </div>
                <div class="sample-audio-controls">
                    <button class="btn-sample-audio" id="btnPlaySampleAudio" onclick="playCurrentSampleLetter()" title="Nghe toàn bộ bức thư">
                        <i class="fa-solid fa-volume-high"></i> Nghe bài mẫu
                    </button>
                    <button class="btn-sample-audio btn-stop" id="btnStopSampleAudio" onclick="stopSampleAudio()" title="Dừng đọc" style="display: none;">
                        <i class="fa-solid fa-stop"></i> Dừng
                    </button>
                    <select class="sample-speed-select" id="sampleAudioRate" onchange="updateSampleAudioSpeed(this.value)">
                        <option value="0.85">0.85x Chậm</option>
                        <option value="1.0" selected>1.0x Chuẩn</option>
                        <option value="1.15">1.15x Nhanh</option>
                    </select>
                    <span class="sample-audio-status" id="sampleAudioStatus" style="display: none;">
                        <i class="fa-solid fa-headphones fa-bounce"></i> Đang đọc...
                    </span>
                </div>
            </div>

            <!-- View Switcher Tabs -->
            <div class="sample-view-nav" style="margin-top: 18px;">
                <button class="sample-view-tab-btn active" data-view="sampleViewAnnotated" onclick="switchSampleView('sampleViewAnnotated', this)">
                    <i class="fa-solid fa-shapes"></i> 🎨 Phân tích Cấu trúc & Bí quyết B1
                </button>
                <button class="sample-view-tab-btn" data-view="sampleViewClean" onclick="switchSampleView('sampleViewClean', this)">
                    <i class="fa-solid fa-file-lines"></i> 📄 Toàn văn lá thư đầy đủ (Không chú thích)
                </button>
                <button class="sample-view-tab-btn" data-view="sampleViewBilingual" onclick="switchSampleView('sampleViewBilingual', this)">
                    <i class="fa-solid fa-language"></i> 🇻🇳 Đối chiếu Song ngữ Anh - Việt
                </button>
            </div>

            <!-- 3 Dynamic View Panels -->
            <div class="sample-view-container" style="margin-top: 16px;">
                {annotated_html}
                {clean_html}
                {bilingual_html}
            </div>

            <!-- Examiner Takeaways Card -->
            {takeaways_html}
        </div>
    '''
    return final_html
