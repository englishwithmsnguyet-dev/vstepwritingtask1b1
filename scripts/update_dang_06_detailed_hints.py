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
    },

    description: {
        title: "DẠNG 03: LETTER OF DESCRIPTION (THƯ CUNG CẤP THÔNG TIN)",
        prompt: `You have received a letter from your friend, Nam. Read part of his letter below:
... I'm planning to study English at Rainbow Language Center next month. Since you have just completed a course there, could you tell me more about it? I'd like to know about the address of the center, the tuition fee, the teachers, and the training program before I decide to enroll...
Write a letter responding to Nam. In your letter, you should provide information about:
• the address of the center
• the tuition fee
• the teachers
• the training program
You should write at least 120 words. Do not include your name or address.`,
        analysis: {
            recipient: "Nam (Bạn bè)",
            purpose: "Cung cấp thông tin chi tiết về khóa học tiếng Anh tại Rainbow Language Center",
            style: "Thân mật (Informal Letter)",
            requirements: "the address of the center, the tuition fee, the teachers, the training program"
        },
        hints: [
            {
                title: "1. The address of the center (Địa chỉ của trung tâm)",
                type: "standard",
                items: [
                    {
                        en: "The center is located in the city center on Tran Phu Street",
                        vi: "Trung tâm nằm ở trung tâm thành phố trên đường Trần Phú",
                        reasonEn: "because it is very convenient and easy to find.",
                        reasonVi: "vì rất thuận tiện và dễ tìm."
                    },
                    {
                        en: "The location is very close to bus stations and supermarkets",
                        vi: "Vị trí rất gần các trạm xe buýt và siêu thị",
                        reasonEn: "so you can get there easily by bus or motorbike.",
                        reasonVi: "nên cậu có thể đến đó dễ dàng bằng xe buýt hoặc xe máy."
                    },
                    {
                        en: "It has a large parking area and modern facilities",
                        vi: "Trung tâm có bãi giữ xe rộng rãi và cơ sở vật chất hiện đại",
                        reasonEn: "which makes your studying experience very comfortable.",
                        reasonVi: "điều này làm cho trải nghiệm học tập của cậu rất thoải mái."
                    }
                ]
            },
            {
                title: "2. The tuition fee (Học phí)",
                type: "standard",
                items: [
                    {
                        en: "The tuition fee is about two million VND for a two-month course",
                        vi: "Học phí khoảng 2 triệu đồng cho khóa học hai tháng",
                        reasonEn: "which is quite reasonable and suitable for students.",
                        reasonVi: "mức giá này khá hợp lý và phù hợp với sinh viên."
                    },
                    {
                        en: "The center offers a 10% discount for early registration",
                        vi: "Trung tâm giảm giá 10% nếu cậu đăng ký sớm",
                        reasonEn: "so you can save some money when enrolling.",
                        reasonVi: "nên cậu có thể tiết kiệm một khoản tiền khi đăng ký."
                    },
                    {
                        en: "Course materials and textbooks are included in the tuition fee",
                        vi: "Tài liệu học tập và giáo trình đã được bao gồm trong học phí",
                        reasonEn: "so you do not need to pay any extra fees.",
                        reasonVi: "nên cậu không cần phải trả thêm bất kỳ khoản phí phụ nào."
                    }
                ]
            },
            {
                title: "3. The teachers (Giáo viên)",
                type: "standard",
                items: [
                    {
                        en: "The teachers are very experienced, friendly, and enthusiastic",
                        vi: "Các giáo viên rất giàu kinh nghiệm, thân thiện và nhiệt tình",
                        reasonEn: "because they always explain difficult grammar points clearly and patiently.",
                        reasonVi: "vì họ luôn giải thích các điểm ngữ pháp khó một cách rõ ràng và kiên nhẫn."
                    },
                    {
                        en: "Both native English speakers and Vietnamese teachers teach the classes",
                        vi: "Cả giáo viên bản xứ và giáo viên Việt Nam đều tham gia giảng dạy",
                        reasonEn: "which helps you improve your pronunciation and listening skills effectively.",
                        reasonVi: "điều này giúp cậu cải thiện phát âm và kỹ năng nghe hiệu quả."
                    },
                    {
                        en: "They always create an engaging and supportive learning atmosphere",
                        vi: "Họ luôn tạo ra một không khí học tập hào hứng và sẵn lòng hỗ trợ",
                        reasonEn: "so you will feel confident when speaking English in class.",
                        reasonVi: "nên cậu sẽ cảm thấy tự tin khi nói tiếng Anh trong lớp."
                    }
                ]
            },
            {
                title: "4. The training program (Chương trình đào tạo)",
                type: "standard",
                items: [
                    {
                        en: "The program focuses on all four skills: Listening, Speaking, Reading, and Writing",
                        vi: "Chương trình tập trung vào cả 4 kỹ năng: Nghe, Nói, Đọc và Viết",
                        reasonEn: "with a lot of practical communicative activities and group discussions.",
                        reasonVi: "với nhiều hoạt động giao tiếp thực tế và thảo luận nhóm."
                    },
                    {
                        en: "The class schedule is flexible with both evening and weekend classes",
                        vi: "Lịch học rất linh hoạt với các lớp học buổi tối và cuối tuần",
                        reasonEn: "so you can easily arrange your study time without affecting your daily routine.",
                        reasonVi: "nên cậu có thể dễ dàng sắp xếp thời gian học mà không ảnh hưởng đến sinh hoạt hàng ngày."
                    },
                    {
                        en: "There are regular progress tests and personalized feedback",
                        vi: "Có các bài kiểm tra tiến độ định kỳ và nhận xét chi tiết",
                        reasonEn: "which help you track your improvement after each module.",
                        reasonVi: "giúp cậu theo dõi sự tiến bộ của mình sau mỗi học phần."
                    }
                ]
            }
        ],
        sampleModel: `Dear Nam,

How are you? I hope you are doing well. In your letter, you asked me about the English course at Rainbow Language Center, so here is some information for you.

Firstly, the center is located on Tran Phu Street in the city center, which is very convenient and easy to find. You can easily get there by bus or motorbike. Secondly, regarding the tuition fee, it is about two million VND for a two-month course. I think the price is quite reasonable and suitable for students. In addition, the center offers a ten percent discount if you register early. Next, the teachers there are very experienced, friendly, and enthusiastic. They always explain grammar points clearly and help students practise pronunciation. Finally, the training program focuses on all four skills, especially speaking and listening. There are many interesting activities and group discussions in class. The schedule is also flexible with evening classes.

I hope you will find this information useful. Let me know if you need more details. Write back soon.

Best wishes,`,
        sampleModelVi: `Nam thân mến,

Cậu khỏe không? Tớ hy vọng cậu vẫn khỏe. Trong thư của cậu, cậu đã hỏi tớ về khóa học tiếng Anh tại Trung tâm Ngoại ngữ Rainbow, vì vậy dưới đây là một số thông tin dành cho cậu.

Đầu tiên, trung tâm nằm trên đường Trần Phú ở trung tâm thành phố, rất thuận tiện và dễ tìm. Cậu có thể dễ dàng đến đó bằng xe buýt hoặc xe máy. Thứ hai, về học phí, khóa học hai tháng có giá khoảng hai triệu đồng. Tớ nghĩ mức giá này khá hợp lý và phù hợp với sinh viên. Ngoài ra, trung tâm còn giảm giá 10% nếu cậu đăng ký sớm. Tiếp theo, các giáo viên ở đó rất giàu kinh nghiệm, thân thiện và nhiệt tình. Họ luôn giải thích các điểm ngữ pháp rõ ràng và giúp học viên luyện phát âm. Cuối cùng, chương trình đào tạo tập trung vào cả bốn kỹ năng, đặc biệt là kỹ năng nói và nghe. Có rất nhiều hoạt động thú vị và thảo luận nhóm trong lớp. Lịch học cũng linh hoạt với các lớp học buổi tối.

Tớ hy vọng cậu sẽ thấy những thông tin này hữu ích. Hãy cho tớ biết nếu cậu cần thêm chi tiết nhé. Hãy viết thư lại sớm nhé.

Chúc cậu mọi điều tốt lành,`
    },

    complaint: {
        title: "DẠNG 04: LETTER OF COMPLAINT (THƯ PHÀN NÀN)",
        prompt: `You recently stayed at a hotel during your holiday. Unfortunately, you were not satisfied with your room. Write a letter to the hotel manager to complain about your stay. In your letter, you should:
• describe the problems with the room
• explain how you felt about the experience
• suggest some improvements
You should write at least 120 words. Do not include your name or address.`,
        analysis: {
            recipient: "Quản lý khách sạn (The Hotel Manager)",
            purpose: "Phàn nàn về chất lượng phòng khách sạn và đề xuất phương án cải thiện",
            style: "Trang trọng (Formal Letter)",
            requirements: "Mô tả vấn đề của phòng, Bày tỏ cảm xúc, Đề xuất cải thiện"
        },
        hints: [
            {
                title: "Broken air conditioner (Máy điều hòa bị hỏng)",
                type: "complaint_triplet",
                items: [
                    {
                        problemEn: "The air conditioner was broken.",
                        problemVi: "Máy điều hòa bị hỏng.",
                        descEn: "It made a very loud noise throughout the night, so I could not sleep.",
                        descVi: "Nó phát ra tiếng ồn rất lớn suốt đêm nên tôi không thể ngủ được.",
                        solEn: "inspect and repair the air conditioner immediately",
                        solVi: "Kiểm tra và sửa chữa máy điều hòa ngay lập tức."
                    },
                    {
                        problemEn: "The air conditioner did not work properly.",
                        problemVi: "Máy điều hòa không hoạt động bình thường.",
                        descEn: "The room was extremely hot and stuffy.",
                        descVi: "Căn phòng vô cùng nóng nực và bí bách.",
                        solEn: "replace the old air conditioning units",
                        solVi: "Thay thế các máy điều hòa cũ."
                    }
                ]
            },
            {
                title: "Dirty bathroom (Phòng tắm không sạch sẽ)",
                type: "complaint_triplet",
                items: [
                    {
                        problemEn: "The bathroom was dirty.",
                        problemVi: "Phòng tắm rất bẩn.",
                        descEn: "The floor was wet and there was a bad smell in the room.",
                        descVi: "Sàn nhà bị ướt và có mùi hôi khó chịu trong phòng.",
                        solEn: "clean and disinfect the bathroom thoroughly",
                        solVi: "Vệ sinh và khử trùng phòng tắm kỹ lưỡng."
                    },
                    {
                        problemEn: "There was no hot water in the shower.",
                        problemVi: "Vòi hoa sen không có nước nóng.",
                        descEn: "I had to take a cold shower after a long journey.",
                        descVi: "Tôi phải tắm bằng nước lạnh sau một chuyến đi dài.",
                        solEn: "fix the hot water system properly",
                        solVi: "Sửa chữa hệ thống nước nóng chu đáo."
                    }
                ]
            },
            {
                title: "Dirty bed sheets and towels (Ga trải giường & khăn tắm bẩn)",
                type: "complaint_triplet",
                items: [
                    {
                        problemEn: "The bed sheets were stained.",
                        problemVi: "Ga trải giường bị ố bẩn.",
                        descEn: "They had yellow stains and looked very old.",
                        descVi: "Chúng có nhiều vết ố vàng và trông rất cũ kỹ.",
                        solEn: "change the bed sheets before guests check in",
                        solVi: "Thay mới ga trải giường trước khi khách nhận phòng."
                    },
                    {
                        problemEn: "The towels were not washed clean.",
                        problemVi: "Khăn tắm giặt không sạch sẽ.",
                        descEn: "There were hairs on the towels, so I could not use them.",
                        descVi: "Có tóc dính trên khăn tắm nên tôi không thể dùng được.",
                        solEn: "provide fresh and hygienic towels daily",
                        solVi: "Cung cấp khăn tắm mới và đảm bảo vệ sinh mỗi ngày."
                    }
                ]
            },
            {
                title: "Noisy environment (Môi trường ồn ào)",
                type: "complaint_triplet",
                items: [
                    {
                        problemEn: "The room was very noisy.",
                        problemVi: "Căn phòng rất ồn ào.",
                        descEn: "There was loud construction noise next to my room early in the morning.",
                        descVi: "Có tiếng thi công công trình ồn ào ngay cạnh phòng tôi vào sáng sớm.",
                        solEn: "avoid doing noisy maintenance during guest rest hours",
                        solVi: "Tránh làm bảo trì ồn ào vào giờ nghỉ ngơi của khách."
                    },
                    {
                        problemEn: "The soundproofing was very poor.",
                        problemVi: "Khả năng cách âm của phòng rất kém.",
                        descEn: "I could clearly hear loud talking and music from the next room.",
                        descVi: "Tôi có thể nghe rõ tiếng nói chuyện lớn và tiếng nhạc từ phòng bên cạnh.",
                        solEn: "improve the soundproofing between guest rooms",
                        solVi: "Cải thiện khả năng cách âm giữa các phòng khách sạn."
                    }
                ]
            },
            {
                title: "Unstable Wi-Fi & TV (Sự cố kết nối Wi-Fi & Tivi)",
                type: "complaint_triplet",
                items: [
                    {
                        problemEn: "The Wi-Fi connection did not work.",
                        problemVi: "Kết nối Wi-Fi không hoạt động.",
                        descEn: "I could not connect to the internet to check my urgent work emails.",
                        descVi: "Tôi không thể kết nối mạng để kiểm tra các email công việc khẩn cấp.",
                        solEn: "upgrade the hotel Wi-Fi network and signal strength",
                        solVi: "Nâng cấp mạng Wi-Fi và độ mạnh đường truyền của khách sạn."
                    },
                    {
                        problemEn: "The television had no signal.",
                        problemVi: "Tivi trong phòng không có tín hiệu.",
                        descEn: "The screen remained blank whenever I turned it on.",
                        descVi: "Màn hình tivi bị tối đen mỗi khi tôi bật lên.",
                        solEn: "check and repair the television cable system",
                        solVi: "Kiểm tra và sửa chữa hệ thống cáp tivi trong phòng."
                    }
                ]
            }
        ],
        sampleModel: `Dear Sir/Madam,

I am writing to complain about the room condition during my recent stay at your hotel from 10th to 12th August. Unfortunately, I was not satisfied with the quality of the accommodation and service.

Firstly, the main problem was that the air conditioner in my room was broken and made a very loud noise throughout the night, which made it impossible for me to sleep. Secondly, the bathroom was not properly cleaned and the shower had no hot water. Finally, the bed sheets and towels were stained and had an unpleasant smell. I was extremely disappointed with these issues because I chose your hotel based on its high reputation. This unpleasant experience completely ruined my holiday. Therefore, I would appreciate it if you could inspect and repair the broken air conditioners immediately, as well as ensure that the housekeeping team cleans the rooms and changes the bed sheets more thoroughly. Furthermore, I hope you will consider offering a partial refund for the inconvenience caused.

I hope you will look into these matters soon. I look forward to receiving your reply.

Yours faithfully,`,
        sampleModelVi: `Kính gửi Ông/Bà,

Tôi viết thư này để phàn nàn về tình trạng phòng ốc trong kỳ nghỉ gần đây của tôi tại khách sạn của quý vị từ ngày 10 đến ngày 12 tháng Tám. Thật không may, tôi đã không hài lòng với chất lượng chỗ ở và dịch vụ.

Đầu tiên, vấn đề chính là máy điều hòa trong phòng tôi bị hỏng và phát ra tiếng ồn rất lớn suốt đêm, khiến tôi không thể nào chợp mắt được. Thứ hai, phòng tắm không được dọn dẹp sạch sẽ và vòi hoa sen hoàn toàn không có nước nóng. Cuối cùng, ga trải giường và khăn tắm bị ố bẩn và có mùi khó chịu. Tôi vô cùng thất vọng với những vấn đề này vì tôi đã chọn khách sạn của quý vị dựa trên danh tiếng cao của khách sạn. Trải nghiệm khó chịu này đã làm hỏng hoàn toàn kỳ nghỉ của tôi. Do đó, tôi sẽ rất cảm kích nếu quý vị có thể kiểm tra và sửa chữa máy điều hòa ngay lập tức, cũng như đảm bảo đội ngũ dọn phòng vệ sinh phòng ốc và thay ga trải giường kỹ lưỡng hơn. Hơn nữa, tôi hy vọng quý vị sẽ xem xét hoàn lại một phần tiền cho sự bất tiện mà tôi đã gặp phải.

Tôi hy vọng quý vị sẽ sớm xem xét các vấn đề này. Tôi rất mong sớm nhận được phản hồi từ quý vị.

Trân trọng,`
    },

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
        feedbackSections: [
            {
                sectionTitle: "GỢI Ý ĐIỂM KHEN (POSITIVE POINTS) – LÝ DO",
                icon: "fa-solid fa-thumbs-up",
                themeColor: "#16a34a",
                bgHeader: "#f0fdf4",
                borderCol: "#bbf7d0",
                categories: [
                    {
                        name: "The food & dishes (Món ăn & Hương vị)",
                        reasons: [
                            { en: "The food was fresh, delicious, and seasoned to perfection.", vi: "Thức ăn rất tươi ngon, đậm đà và được nêm nếm hoàn hảo." },
                            { en: "The dishes were beautifully presented and served hot.", vi: "Các món ăn được trình bày đẹp mắt và phục vụ khi còn nóng sốt." },
                            { en: "There were many unique specialty dishes with authentic local flavors.", vi: "Có nhiều món ăn đặc sản độc đáo mang đậm hương vị truyền thống." },
                            { en: "The portion sizes were generous and well worth the price.", vi: "Khẩu phần ăn đầy đặn và rất xứng đáng với giá tiền." }
                        ]
                    },
                    {
                        name: "The staff & service (Nhân viên & Phục vụ)",
                        reasons: [
                            { en: "The waiters were very polite, attentive, and helpful throughout the dinner.", vi: "Các nhân viên phục vụ rất lịch sự, chu đáo và nhiệt tình suốt bữa tối." },
                            { en: "They welcomed us warmly with bright smiles right when we arrived.", vi: "Họ chào đón chúng tôi nồng nhiệt với nụ cười tươi ngay khi chúng tôi đến." },
                            { en: "They gave great food recommendations and took our orders quickly.", vi: "Họ nhiệt tình gợi ý các món ăn ngon và nhận gọi món rất nhanh." },
                            { en: "They responded to all our requests promptly with a professional attitude.", vi: "Họ đáp ứng mọi yêu cầu của chúng tôi nhanh chóng với thái độ chuyên nghiệp." }
                        ]
                    },
                    {
                        name: "The atmosphere & decor (Không gian & Trang trí)",
                        reasons: [
                            { en: "The restaurant had a cozy, elegant, and modern atmosphere.", vi: "Nhà hàng có không gian ấm cúng, thanh lịch và hiện đại." },
                            { en: "The lighting was warm and the background music was pleasant and relaxing.", vi: "Ánh sáng ấm áp và nhạc nền du dương, mang lại cảm giác thư thái." },
                            { en: "The dining area was clean, spacious, and beautifully decorated.", vi: "Khu vực ăn uống sạch sẽ, rộng rãi và được bài trí đẹp mắt." },
                            { en: "It was an ideal setting for family dinners and friends' gatherings.", vi: "Đây là không gian lý tưởng cho các bữa tối gia đình và tụ họp bạn bè." }
                        ]
                    },
                    {
                        name: "The menu (Thực đơn)",
                        reasons: [
                            { en: "The menu offered a wide variety of delicious dishes and beverages.", vi: "Thực đơn mang đến nhiều món ăn thơm ngon và đồ uống phong phú." },
                            { en: "There were clear descriptions and appealing pictures of each dish.", vi: "Có phần mô tả rõ ràng và hình ảnh minh họa hấp dẫn cho từng món." },
                            { en: "The menu thoughtfully included vegetarian choices and healthy options.", vi: "Thực đơn có sẵn các món chay và lựa chọn thanh đạm tốt cho sức khỏe." },
                            { en: "All the prices were reasonable and clearly listed on the menu.", vi: "Mức giá hợp lý và được niêm yết minh bạch trên thực đơn." }
                        ]
                    },
                    {
                        name: "The cleanliness & hygiene (Vệ sinh & An toàn thực phẩm)",
                        reasons: [
                            { en: "The dining tables, glassware, and cutlery were clean and spotless.", vi: "Bàn ăn, ly uống nước và dao muỗng nĩa đều sạch bóng và tươm tất." },
                            { en: "The entire restaurant was kept neat, tidy, and hygienic.", vi: "Toàn bộ nhà hàng luôn được giữ gìn gọn gàng, sạch sẽ và đảm bảo vệ sinh." },
                            { en: "The open kitchen area looked very clean and well-organized.", vi: "Khu vực bếp mở trông rất sạch sẽ và được sắp xếp ngăn nắp." },
                            { en: "The restrooms were regularly cleaned and fully equipped with hand soap.", vi: "Nhà vệ sinh được dọn dẹp thường xuyên và có đầy đủ xà phòng rửa tay." }
                        ]
                    },
                    {
                        name: "The location & parking (Vị trí & Bãi đỗ xe)",
                        reasons: [
                            { en: "The restaurant is conveniently located in the city center and easy to find.", vi: "Nhà hàng nằm ở vị trí thuận tiện tại trung tâm thành phố và rất dễ tìm." },
                            { en: "There was a spacious and safe parking area for motorbikes and cars.", vi: "Có bãi đỗ xe rộng rãi và an toàn dành cho cả xe máy và ô tô." },
                            { en: "The security staff were courteous and guided us to park easily.", vi: "Các nhân viên bảo vệ rất lịch thiệp và hướng dẫn chúng tôi đỗ xe thuận tiện." },
                            { en: "It was in a great area close to shopping streets and cafes.", vi: "Nhà hàng nằm ở khu vực đắc địa, gần các phố mua sắm và quán cà phê." }
                        ]
                    }
                ]
            },
            {
                sectionTitle: "GỢI Ý ĐIỂM CHÊ (NEGATIVE POINTS) – LÝ DO – GIẢI PHÁP",
                icon: "fa-solid fa-thumbs-down",
                themeColor: "#dc2626",
                bgHeader: "#fef2f2",
                borderCol: "#fecaca",
                categories: [
                    {
                        name: "The waiting time & serving speed (Thời gian chờ & Tốc độ phục vụ)",
                        reasons: [
                            { en: "We had to wait for almost forty minutes for our main courses to arrive.", vi: "Chúng tôi đã phải chờ gần 40 phút mới được phục vụ các món chính." },
                            { en: "The food was served very slowly because the restaurant was overcrowded.", vi: "Món ăn được dọn lên rất chậm do nhà hàng quá đông khách." },
                            { en: "Some dishes arrived lukewarm after a very long waiting time.", vi: "Một số món ăn bị nguội sau thời gian chờ đợi quá lâu." },
                            { en: "The drinks were served much later than the food.", vi: "Đồ uống lại được mang ra muộn hơn rất nhiều so với đồ ăn." }
                        ],
                        solutions: [
                            { en: "hire more kitchen assistants and waiters during peak dining hours", vi: "tuyển thêm phụ bếp và nhân viên phục vụ vào các khung giờ ăn cao điểm" },
                            { en: "speed up order preparation and shorten customer waiting time", vi: "đẩy nhanh tiến độ chuẩn bị món và rút ngắn thời gian chờ của khách" },
                            { en: "serve drinks and complimentary appetizers first while guests wait", vi: "phục vụ đồ uống và món khai vị miễn phí trước trong khi khách chờ món chính" }
                        ]
                    },
                    {
                        name: "The staff & service attitude (Thái độ phục vụ của nhân viên)",
                        reasons: [
                            { en: "The waiters seemed overloaded and were not attentive to our table.", vi: "Nhân viên phục vụ có vẻ bị quá tải và không chú ý chăm sóc bàn của chúng tôi." },
                            { en: "They forgot one of our side dishes and we had to remind them twice.", vi: "Họ quên mất một món phụ của chúng tôi và chúng tôi phải nhắc lại hai lần." },
                            { en: "Some staff members were not very friendly and lacked a welcoming attitude.", vi: "Một số nhân viên không mấy niềm nở và thiếu thái độ chào đón khách." },
                            { en: "It took a long time to get the attention of staff when we requested the bill.", vi: "Mất nhiều thời gian để gọi được nhân viên khi chúng tôi yêu cầu thanh toán." }
                        ],
                        solutions: [
                            { en: "train the service staff in professional communication and customer care", vi: "đào tạo nhân viên phục vụ về kỹ năng giao tiếp chuyên nghiệp và chăm sóc khách" },
                            { en: "remind staff to be more attentive, patient, and polite with customers", vi: "nhắc nhở nhân viên chu đáo, kiên nhẫn và lịch sự hơn với thực khách" },
                            { en: "use an electronic tablet ordering system to avoid missing customer orders", vi: "sử dụng hệ thống máy tính bảng gọi món điện tử để tránh bỏ sót món của khách" }
                        ]
                    },
                    {
                        name: "The food quality & seasoning (Chất lượng & Nêm nếm món ăn)",
                        reasons: [
                            { en: "Some of the dishes were quite salty and contained too much cooking oil.", vi: "Một số món ăn bị nêm khá mặn và có quá nhiều dầu mỡ." },
                            { en: "The beef steak was rather tough and overcooked.", vi: "Món bít tết bò hơi dai và bị nấu quá lửa." },
                            { en: "The seafood dish did not taste as fresh as we had hoped.", vi: "Món hải sản không được tươi ngon như chúng tôi kỳ vọng." },
                            { en: "The food portions were rather small given the relatively high prices.", vi: "Khẩu phần ăn hơi ít so với mức giá tương đối cao của nhà hàng." }
                        ],
                        solutions: [
                            { en: "adjust the seasoning recipes to ensure dishes are not overly salty or greasy", vi: "điều chỉnh công thức gia vị để đảm bảo món ăn không bị quá mặn hay ngấy mỡ" },
                            { en: "ensure all meats and seafood ingredients are sourced fresh daily", vi: "đảm bảo mọi nguyên liệu thịt và hải sản luôn được nhập tươi mới mỗi ngày" },
                            { en: "maintain consistent cooking quality and generous portion sizes", vi: "duy trì chất lượng chế biến ổn định và khẩu phần ăn đầy đặn, tương xứng" }
                        ]
                    },
                    {
                        name: "The noise & dining atmosphere (Tiếng ồn & Không gian nhà hàng)",
                        reasons: [
                            { en: "The dining hall was extremely noisy and crowded during dinner time.", vi: "Sảnh ăn uống vô cùng ồn ào và đông đúc trong khung giờ ăn tối." },
                            { en: "The background music was played too loudly, making conversation difficult.", vi: "Nhạc nền mở quá lớn khiến chúng tôi gặp khó khăn khi trò chuyện." },
                            { en: "The tables were placed too close together, resulting in a lack of privacy.", vi: "Các bàn kê quá sát nhau khiến không gian thiếu sự riêng tư cần thiết." },
                            { en: "The air conditioning was inadequate, making the dining room feel stuffy.", vi: "Hệ thống điều hòa hoạt động yếu khiến phòng ăn có cảm giác ngột ngạt." }
                        ],
                        solutions: [
                            { en: "rearrange the dining tables with wider spacing for greater privacy", vi: "sắp xếp lại bàn ăn với khoảng cách rộng rãi hơn để tăng sự riêng tư" },
                            { en: "lower the background music volume to create a comfortable dining atmosphere", vi: "vặn nhỏ âm lượng nhạc nền để tạo bầu không khí ăn uống dễ chịu" },
                            { en: "upgrade the ventilation and air conditioning systems in the dining hall", vi: "nâng cấp hệ thống thông gió và điều hòa nhiệt độ trong sảnh ăn" }
                        ]
                    },
                    {
                        name: "The menu options & pricing (Thực đơn & Giá cả)",
                        reasons: [
                            { en: "There were very few vegetarian dishes and healthy dining choices.", vi: "Có rất ít món ăn chay và các lựa chọn ăn uống lành mạnh." },
                            { en: "Several popular specialty dishes on the menu were out of stock.", vi: "Một số món ăn đặc sản nổi tiếng trên thực đơn đã bị hết hàng." },
                            { en: "The prices of soft drinks and desserts were quite expensive.", vi: "Giá của các loại nước ngọt và món tráng miệng tương đối đắt." },
                            { en: "The menu lacked clear allergen warnings and detailed ingredient lists.", vi: "Thực đơn thiếu cảnh báo dị ứng rõ ràng và danh sách thành phần chi tiết." }
                        ],
                        solutions: [
                            { en: "expand the menu with a broader range of vegetarian and healthy dishes", vi: "mở rộng thực đơn với nhiều món chay và món ăn tốt cho sức khỏe hơn" },
                            { en: "ensure sufficient ingredients to prepare all menu items throughout the evening", vi: "đảm bảo đủ nguyên liệu để phục vụ mọi món trong thực đơn suốt cả buổi tối" },
                            { en: "introduce attractive set menus and discount vouchers for regular patrons", vi: "áp dụng các set thực đơn ưu đãi và voucher giảm giá cho khách quen" }
                        ]
                    },
                    {
                        name: "The cleanliness & restroom (Vệ sinh & Khu vực rửa tay)",
                        reasons: [
                            { en: "The dining table was not wiped thoroughly before we were seated.", vi: "Bàn ăn chưa được lau chùi kỹ lưỡng trước khi chúng tôi ngồi vào." },
                            { en: "The floor near our table was slippery from food spills.", vi: "Sàn nhà gần bàn của chúng tôi bị trơn trượt do thức ăn vương vãi." },
                            { en: "The restroom was not cleaned frequently and ran out of hand soap.", vi: "Nhà vệ sinh không được dọn thường xuyên và đã bị hết xà phòng rửa tay." },
                            { en: "There was a strong smell of cooking oil lingering in the room.", vi: "Có mùi dầu mỡ nấu nướng nồng nặc ám lâu trong không khí phòng ăn." }
                        ],
                        solutions: [
                            { en: "sanitize and dry dining tables immediately after guests depart", vi: "lau khử trùng và làm khô bàn ăn ngay sau khi khách rời đi" },
                            { en: "inspect and clean the restrooms regularly every hour during business hours", vi: "kiểm tra và dọn dẹp nhà vệ sinh định kỳ mỗi giờ trong thời gian mở cửa" },
                            { en: "install high-powered kitchen exhaust fans to remove food odors", vi: "lắp đặt quạt hút mùi công suất lớn trong bếp để khử sạch mùi thức ăn" }
                        ]
                    }
                ]
            }
        ],
        sampleModel: `Dear Sir/Madam,

Thank you for your email asking for my feedback. I am writing to share my opinion about my recent dinner at your restaurant last Friday evening.

Overall, I had a pleasant dining experience, although there were a few minor issues that could be improved. Regarding the positive points, the food was delicious, fresh, and beautifully presented, especially the grilled seafood and beef steak. In addition, the restaurant had an elegant atmosphere with lovely background music, making it an ideal place for family gatherings. However, I was slightly disappointed with the long waiting time. We had to wait for almost forty minutes before our main courses were served because the restaurant was extremely crowded. In addition, the waiters seemed overloaded and forgot one of our drink orders. Therefore, I would suggest hiring more kitchen staff and waiters during peak hours to speed up the service. Furthermore, it would be wonderful if you could add more vegetarian options to your menu.

I hope you will find my feedback constructive. I look forward to visiting your restaurant again in the future.

Yours faithfully,`,
        sampleModelVi: `Kính gửi Ban Quản lý Nhà hàng,

Cảm ơn quý vị đã gửi email xin ý kiến phản hồi của tôi. Tôi viết thư này để chia sẻ cảm nhận về bữa tối gần đây của tôi tại nhà hàng của quý vị vào tối thứ Sáu tuần trước.

Nhìn chung, tôi đã có một trải nghiệm ăn uống thú vị, mặc dù vẫn có một vài vấn đề nhỏ có thể cải thiện. Về những điểm tích cực, các món ăn rất thơm ngon, tươi mới và được trình bày đẹp mắt, đặc biệt là món hải sản nướng và bít tết bò. Ngoài ra, nhà hàng có không gian trang nhã cùng âm nhạc du dương, là địa điểm lý tưởng cho các buổi tụ họp gia đình. Tuy nhiên, tôi hơi thất vọng một chút về thời gian chờ đợi khá lâu. Chúng tôi đã phải đợi gần 40 phút mới được phục vụ món chính do nhà hàng quá đông khách. Thêm vào đó, nhân viên phục vụ có vẻ bị quá tải và đã quên mất một phần đồ uống của chúng tôi. Do đó, tôi xin đề xuất nhà hàng nên tuyển thêm nhân viên bếp và phục vụ vào giờ cao điểm để đẩy nhanh tốc độ phục vụ. Hơn nữa, sẽ rất tuyệt nếu quý vị bổ sung thêm các món chay vào thực đơn.

Tôi hy vọng quý vị sẽ thấy những đóng góp của tôi mang tính xây dựng. Tôi rất mong sẽ sớm ghé thăm lại nhà hàng của quý vị trong tương lai.

Trân trọng,`
    },

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
        apologyOutlineSections: [
            {
                sectionNumber: "1",
                sectionTitle: "Apologize for submitting your assignment late (Xin lỗi vì nộp bài muộn)",
                themeColor: "#dc2626",
                type: "phrase_list",
                description: "Các cụm từ xin lỗi thông dụng để ghép vào câu mở đầu:",
                phrases: [
                    { en: "submitting my assignment late", vi: "nộp bài tập muộn" },
                    { en: "not submitting my assignment earlier / on time", vi: "không nộp bài tập sớm hơn / đúng hạn" },
                    { en: "missing the deadline last Friday", vi: "lỡ hạn chót vào thứ Sáu tuần trước" },
                    { en: "the delay in submitting my coursework", vi: "sự chậm trễ trong việc nộp bài tập học phần" }
                ]
            },
            {
                sectionNumber: "2",
                sectionTitle: "Explain why you could not submit on time (Giải thích lý do không thể nộp đúng hạn)",
                themeColor: "#2563eb",
                type: "scenario_list",
                scenarios: [
                    {
                        name: "Gợi ý 1: Bị ốm nặng / Sốt và cảm cúm (Severe illness & fever)",
                        mainSent: {
                            en: "I am really sorry that I could not submit my assignment on time because I was severely ill.",
                            vi: "Em rất xin lỗi vì đã không thể nộp bài tập đúng hạn do em bị ốm nặng."
                        },
                        explainSents: [
                            {
                                en: "I caught a high fever and a bad flu early last week.",
                                vi: "Em bị sốt cao và cảm cúm nặng vào đầu tuần trước."
                            },
                            {
                                en: "The doctor advised me to rest completely in bed for several days, so I could not concentrate on studying.",
                                vi: "Bác sĩ khuyên em phải nghỉ ngơi tĩnh dưỡng trên giường vài ngày nên em không thể tập trung học tập."
                            }
                        ]
                    },
                    {
                        name: "Gợi ý 2: Máy tính bị hỏng / Mất dữ liệu bài làm (Laptop technical crash & data loss)",
                        mainSent: {
                            en: "I sincerely apologize for the delay because my laptop had a serious technical problem.",
                            vi: "Em chân thành xin lỗi về sự chậm trễ vì máy tính xách tay của em gặp sự cố kỹ thuật nghiêm trọng."
                        },
                        explainSents: [
                            {
                                en: "My laptop suddenly crashed and would not turn on while I was writing the assignment.",
                                vi: "Máy tính của em đột nhiên bị sập nguồn và không thể khởi động lại khi em đang làm bài."
                            },
                            {
                                en: "I had to take it to the repair shop and unfortunately lost some of my research notes.",
                                vi: "Em phải mang máy đi sửa và không may bị mất một số ghi chú nghiên cứu."
                            }
                        ]
                    },
                    {
                        name: "Gợi ý 3: Gia đình có việc đột xuất / Người thân bị bệnh (Unexpected family emergency)",
                        mainSent: {
                            en: "I am very sorry for the late submission because I had an urgent family emergency.",
                            vi: "Em vô cùng xin lỗi vì nộp bài muộn do gia đình em gặp việc khẩn cấp đột xuất."
                        },
                        explainSents: [
                            {
                                en: "My mother suddenly fell ill, so I had to travel back to my hometown to take care of her.",
                                vi: "Mẹ em đột ngột đổ bệnh nên em phải về quê để chăm sóc mẹ."
                            },
                            {
                                en: "I only returned to the university yesterday, and everything at home is much better now.",
                                vi: "Em chỉ mới quay lại trường đại học hôm qua, và hiện tại mọi việc ở nhà đã ổn hơn nhiều."
                            }
                        ]
                    }
                ]
            },
            {
                sectionNumber: "3",
                sectionTitle: "Say your current progress on the assignment (Nêu tiến độ hoàn thành bài tập)",
                themeColor: "#8b5cf6",
                type: "case_list",
                cases: [
                    {
                        name: "Trường hợp 1: Đã hoàn thành bản thảo và đang rà soát lại (Almost finished / Reviewing final draft)",
                        mainSent: {
                            en: "I have now finished the final draft of my assignment.",
                            vi: "Hiện em đã hoàn thành xong bản thảo cuối cùng của bài tập."
                        },
                        expandSents: [
                            {
                                en: "I have revised all the main arguments and checked the references carefully.",
                                vi: "Em đã chỉnh sửa lại các luận điểm chính và kiểm tra tài liệu tham khảo cẩn thận."
                            },
                            {
                                en: "I am confident that the quality of my paper meets your academic requirements.",
                                vi: "Em tin tưởng rằng chất lượng bài viết đáp ứng đúng các yêu cầu học thuật của Thầy/Cô."
                            },
                            {
                                en: "Thank you very much for giving me more time to finalize it.",
                                vi: "Em chân thành cảm ơn Thầy/Cô đã cho em thêm thời gian để hoàn thiện bài."
                            }
                        ]
                    },
                    {
                        name: "Trường hợp 2: Đang hoàn thiện những phần cuối cùng (Completing the last section)",
                        mainSent: {
                            en: "I am currently putting the finishing touches on the conclusion and reference list.",
                            vi: "Hiện em đang hoàn thiện nốt phần kết luận và danh mục tài liệu tham khảo."
                        },
                        expandSents: [
                            {
                                en: "I have done most of the research and only need a few more hours to review everything.",
                                vi: "Em đã làm xong hầu hết phần nghiên cứu và chỉ cần thêm vài giờ để rà soát lại tất cả."
                            },
                            {
                                en: "I am very sorry that I could not finish it before the deadline.",
                                vi: "Em rất tiếc vì đã không thể hoàn thành bài trước hạn chót."
                            },
                            {
                                en: "I promise to deliver a well-written assignment as soon as possible.",
                                vi: "Em xin hứa sẽ nộp một bài viết chỉn chu trong thời gian sớm nhất."
                            }
                        ]
                    }
                ]
            },
            {
                sectionNumber: "4",
                sectionTitle: "Say when and how you will submit your assignment (Nêu rõ thời gian & cách thức nộp)",
                themeColor: "#059669",
                type: "scenario_list",
                scenarios: [
                    {
                        name: "Gợi ý 1: Nộp qua cổng sinh viên và gửi email vào chiều mai (Online portal & email tomorrow afternoon)",
                        mainSent: {
                            en: "I will submit my completed assignment by 5 PM tomorrow afternoon.",
                            vi: "Em sẽ nộp bài tập hoàn chỉnh trước 5 giờ chiều mai."
                        },
                        explainSents: [
                            {
                                en: "I will upload the Word and PDF files to the student portal and also send a copy directly to your email.",
                                vi: "Em sẽ tải các tệp Word và PDF lên cổng sinh viên và gửi một bản trực tiếp vào email của Thầy/Cô."
                            },
                            {
                                en: "Please let me know if you receive the files successfully.",
                                vi: "Xin Thầy/Cô vui lòng báo cho em biết nếu đã nhận được tệp thành công."
                            }
                        ]
                    },
                    {
                        name: "Gợi ý 2: Nộp bản in trực tiếp tại văn phòng khoa vào sáng thứ Tư (In-person at faculty office on Wednesday morning)",
                        mainSent: {
                            en: "I will hand in my printed assignment directly to your office on Wednesday morning.",
                            vi: "Em sẽ nộp bản in bài tập trực tiếp tại văn phòng của Thầy/Cô vào sáng thứ Tư."
                        },
                        explainSents: [
                            {
                                en: "I will bring the hard copy to your office room at 9 AM after my morning class.",
                                vi: "Em sẽ mang bản in đến phòng làm việc của Thầy/Cô lúc 9 giờ sáng sau giờ học buổi sáng."
                            },
                            {
                                en: "I hope I can meet you briefly to explain my situation in person.",
                                vi: "Em hy vọng có thể gặp Thầy/Cô trong giây lát để giải thích trực tiếp hoàn cảnh của mình."
                            }
                        ]
                    },
                    {
                        name: "Gợi ý 3: Nộp đính kèm giấy chứng nhận y tế/khám bệnh (Submit with attached medical certificate)",
                        mainSent: {
                            en: "I will send my completed assignment via email tonight before 10 PM.",
                            vi: "Em sẽ gửi bài tập hoàn chỉnh qua email tối nay trước 10 giờ tối."
                        },
                        explainSents: [
                            {
                                en: "I have also attached the hospital medical certificate to this email for your verification.",
                                vi: "Em cũng đã đính kèm giấy chứng nhận khám bệnh của bệnh viện vào email này để Thầy/Cô tiện xác nhận."
                            },
                            {
                                en: "I sincerely assure you that this delay will never happen again in future courses.",
                                vi: "Em xin chân thành cam đoan rằng sự chậm trễ này sẽ không bao giờ tái diễn trong các học phần sau."
                            }
                        ]
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
    },

    application: {
        title: "DẠNG 07: LETTER OF APPLICATION (THƯ ỨNG TUYỂN / XIN VIỆC)",
        prompt: `You saw a job advertisement for a receptionist at a small hotel in your city. You are interested in the position and would like to apply for the job. Write an email to apply for the position. In your email, you should:
• Introduce yourself and your current situation
• Say why you are interested in the position
• Mention any experience you have working with customers or guests
• Explain why you are a suitable candidate for the job
You should write at least 120 words. Do not include your name or address. Your response will be evaluated in terms of Task Fulfillment, Organization, Vocabulary, and Grammar.`,
        analysis: {
            recipient: "Quản lý tuyển dụng (The Hiring Manager)",
            purpose: "Ứng tuyển vào vị trí Nhân viên lễ tân (Receptionist) tại khách sạn",
            style: "Trang trọng / Chuyên nghiệp (Formal Job Application Email)",
            requirements: "Giới thiệu bản thân, Nêu lý do quan tâm, Kinh nghiệm với khách hàng, Giải thích độ phù hợp"
        },
        hints: [
            {
                title: "1. Introduce yourself and your current situation (Giới thiệu bản thân & hoàn cảnh)",
                type: "standard",
                items: [
                    {
                        en: "I am writing to apply for the receptionist position advertised on your hotel website",
                        vi: "Tôi viết thư này để ứng tuyển vào vị trí nhân viên lễ tân được đăng tuyển trên trang web của khách sạn",
                        reasonEn: "and I believe my skills and qualifications make me a strong candidate.",
                        reasonVi: "và tôi tin rằng kỹ năng cùng trình độ của tôi giúp tôi trở thành một ứng viên sáng giá."
                    },
                    {
                        en: "I am currently a final-year student majoring in Tourism and Hospitality Management",
                        vi: "Hiện tôi là sinh viên năm cuối chuyên ngành Quản trị Du lịch và Khách sạn",
                        reasonEn: "at Can Tho University.",
                        reasonVi: "tại Trường Đại học Cần Thơ."
                    },
                    {
                        en: "I am eager to gain practical working experience in a professional hospitality environment",
                        vi: "Tôi rất khao khát tích lũy kinh nghiệm làm việc thực tế trong môi trường khách sạn chuyên nghiệp",
                        reasonEn: "to apply my academic knowledge into real-world practice.",
                        reasonVi: "để vận dụng kiến thức đã học vào thực tế."
                    }
                ]
            },
            {
                title: "2. Say why you are interested in the position (Nêu lý do quan tâm đến vị trí)",
                type: "standard",
                items: [
                    {
                        en: "I have always been deeply passionate about customer service and hospitality",
                        vi: "Tôi luôn có niềm đam mê sâu sắc với ngành dịch vụ chăm sóc khách hàng và khách sạn",
                        reasonEn: "which drives me to pursue this career path.",
                        reasonVi: "điều này thôi thúc tôi theo đuổi con đường sự nghiệp này."
                    },
                    {
                        en: "Your hotel has an excellent reputation for exceptional service and friendly staff",
                        vi: "Khách sạn của quý vị có danh tiếng tuyệt vời về dịch vụ vượt trội và đội ngũ nhân viên thân thiện",
                        reasonEn: "which makes it an ideal place for me to develop my skills.",
                        reasonVi: "khiến nơi đây trở thành địa điểm lý tưởng để tôi phát triển kỹ năng của mình."
                    },
                    {
                        en: "I am excited about the opportunity to contribute to your hotel's continued success",
                        vi: "Tôi rất hào hứng với cơ hội được đóng góp vào sự thành công liên tục của khách sạn",
                        reasonEn: "while delivering high satisfaction to your guests.",
                        reasonVi: "đồng thời mang lại sự hài lòng cao nhất cho các thực khách."
                    }
                ]
            },
            {
                title: "3. Mention your customer service experience (Kinh nghiệm làm việc với khách hàng)",
                type: "standard",
                items: [
                    {
                        en: "I worked as a part-time receptionist at a boutique hotel for six months",
                        vi: "Tôi từng làm việc bán thời gian ở vị trí tiếp tân tại một khách sạn nhỏ trong 6 tháng",
                        reasonEn: "where I was responsible for greeting guests, handling check-ins, and answering inquiries.",
                        reasonVi: "nơi tôi chịu trách nhiệm đón tiếp khách, làm thủ tục nhận phòng và giải đáp thắc mắc."
                    },
                    {
                        en: "This role helped me develop strong communication skills and solve unexpected guest issues calmly",
                        vi: "Công việc này đã giúp tôi rèn luyện kỹ năng giao tiếp tốt và xử lý các vấn đề phát sinh của khách một cách bình tĩnh",
                        reasonEn: "ensuring that every guest felt welcomed and valued.",
                        reasonVi: "đảm bảo mọi du khách đều cảm thấy được chào đón và trân trọng."
                    },
                    {
                        en: "I also have experience managing phone calls, email correspondence, and booking systems",
                        vi: "Tôi cũng có kinh nghiệm xử lý các cuộc gọi điện thoại, trả lời email và sử dụng hệ thống đặt phòng",
                        reasonEn: "with high accuracy and attention to detail.",
                        reasonVi: "với độ chính xác cao và sự cẩn thận tỉ mỉ."
                    }
                ]
            },
            {
                title: "4. Explain why you are a suitable candidate (Giải thích tại sao bạn phù hợp)",
                type: "standard",
                items: [
                    {
                        en: "I can communicate fluently in English and have good basic computer skills",
                        vi: "Tôi có thể giao tiếp tiếng Anh trôi chảy và có kỹ năng tin học văn phòng cơ bản tốt",
                        reasonEn: "which allows me to interact easily with international guests.",
                        reasonVi: "cho phép tôi tương tác dễ dàng với các du khách quốc tế."
                    },
                    {
                        en: "I am hard-working, punctual, and capable of working flexible shifts including weekends",
                        vi: "Tôi chăm chỉ, đúng giờ và có khả năng làm việc linh hoạt theo ca bao gồm cả cuối tuần",
                        reasonEn: "to support the hotel team whenever needed.",
                        reasonVi: "để hỗ trợ đội ngũ khách sạn bất cứ khi nào cần thiết."
                    },
                    {
                        en: "I have attached my resume (CV) to this email for your further consideration",
                        vi: "Tôi đã đính kèm sơ yếu lý lịch (CV) vào email này để quý vị tiện xem xét thêm",
                        reasonEn: "and I would welcome the opportunity to attend an interview at your convenience.",
                        reasonVi: "và tôi rất mong có cơ hội tham gia buổi phỏng vấn vào thời gian thuận tiện của quý vị."
                    }
                ]
            }
        ],
        sampleModel: `Dear Hiring Manager,

I am writing to apply for the receptionist position at your hotel, which was recently advertised on your website. I believe that my academic background and skills make me a suitable candidate for this job.

I am a final-year student majoring in Tourism and Hospitality Management at Can Tho University. I am extremely interested in this position because your hotel is well-known for its excellent customer service and welcoming environment. Regarding my experience, I worked as a part-time receptionist at a boutique hotel for six months. During this time, I was responsible for checking in guests, handling reservations, and answering phone inquiries. This role helped me improve my communication and problem-solving skills when dealing with various customer requests. Furthermore, I can communicate fluently in English, and I am proficient in using basic computer software. I am enthusiastic, reliable, and able to work flexible shifts, including weekends.

I have attached my resume to this email for your consideration. I would be very grateful for the opportunity to attend an interview. Thank you for your time and consideration.

Yours faithfully,`,
        sampleModelVi: `Kính gửi Người phụ trách Tuyển dụng,

Tôi viết thư này để ứng tuyển vào vị trí nhân viên lễ tân tại khách sạn của quý vị, vị trí vừa được đăng tuyển trên trang web của khách sạn gần đây. Tôi tin rằng nền tảng học vấn và kỹ năng của tôi giúp tôi trở thành một ứng viên phù hợp cho công việc này.

Tôi là sinh viên năm cuối chuyên ngành Quản trị Du lịch và Khách sạn tại Đại học Cần Thơ. Tôi vô cùng quan tâm đến vị trí này vì khách sạn của quý vị rất nổi tiếng về dịch vụ khách hàng xuất sắc và môi trường thân thiện. Về kinh nghiệm, tôi từng làm nhân viên lễ tân bán thời gian tại một khách sạn nhỏ trong sáu tháng. Trong thời gian này, tôi chịu trách nhiệm làm thủ tục nhận phòng cho khách, xử lý việc đặt phòng và trả lời các thắc mắc qua điện thoại. Công việc này đã giúp tôi cải thiện kỹ năng giao tiếp và giải quyết vấn đề khi tiếp nhận các yêu cầu khác nhau từ khách hàng. Hơn nữa, tôi có thể giao tiếp tiếng Anh trôi chảy và thành thạo sử dụng các phần mềm máy tính cơ bản. Tôi là người nhiệt huyết, đáng tin cậy và có thể làm việc theo ca linh hoạt, bao gồm cả cuối tuần.

Tôi đã đính kèm sơ yếu lý lịch vào email này để quý vị xem xét. Tôi sẽ rất biết ơn nếu có cơ hội tham gia buổi phỏng vấn. Xin chân thành cảm ơn quý vị đã dành thời gian và sự quan tâm.

Trân trọng,`
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
                <p style="color: var(--text-muted);">Vui lòng chọn từ <strong>Dạng 01</strong> đến <strong>Dạng 07</strong> để làm bài luyện tập.</p>
            </div>
        `;
        return;
    }

    let hintsHtml = '';

    if (data.apologyOutlineSections) {
        hintsHtml = data.apologyOutlineSections.map(sec => {
            let bodyHtml = '';

            if (sec.type === 'phrase_list') {
                let phrasesHtml = sec.phrases.map(p => `
                    <div style="margin-bottom: 8px; padding-left: 12px;">
                        <span style="font-weight: 600; color: var(--text-main);">• ${p.en}</span>
                        <span style="color: var(--text-muted); font-size: 13.5px; font-style: italic;"> (${p.vi})</span>
                    </div>
                `).join('');

                bodyHtml = `
                    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px 16px;">
                        <p style="font-weight: 600; color: var(--primary-color); margin-bottom: 10px; font-size: 14px;">
                            ${sec.description}
                        </p>
                        ${phrasesHtml}
                    </div>
                `;
            } else if (sec.type === 'scenario_list') {
                bodyHtml = sec.scenarios.map(sc => {
                    let explainHtml = sc.explainSents.map(st => `
                        <div style="margin-bottom: 6px; padding-left: 12px;">
                            <p style="margin-bottom: 2px; color: var(--text-main); font-weight: 500;">• ${st.en}</p>
                            <p style="margin-bottom: 0; color: var(--text-muted); font-size: 13.5px; font-style: italic; padding-left: 8px;">(${st.vi})</p>
                        </div>
                    `).join('');

                    return `
                        <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px 16px; margin-bottom: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
                            <h5 style="color: ${sec.themeColor}; font-size: 15px; margin-bottom: 10px; font-weight: 700;">
                                ${sc.name}
                            </h5>
                            <div style="margin-bottom: 10px; padding-left: 4px;">
                                <span style="font-weight: 700; color: var(--text-main); font-size: 13.5px; display: block; margin-bottom: 3px;">
                                    <i class="fa-solid fa-star" style="color: #f59e0b; font-size: 12px;"></i> Câu chính:
                                </span>
                                <p style="margin-bottom: 2px; padding-left: 12px; font-weight: 600; color: #1e293b;">${sc.mainSent.en}</p>
                                <p style="margin-bottom: 0; padding-left: 12px; color: var(--text-muted); font-size: 13.5px; font-style: italic;">(${sc.mainSent.vi})</p>
                            </div>
                            <div style="padding-left: 4px; border-top: 1px dashed #e2e8f0; padding-top: 8px;">
                                <span style="font-weight: 700; color: var(--text-main); font-size: 13.5px; display: block; margin-bottom: 4px;">
                                    <i class="fa-solid fa-circle-info" style="color: ${sec.themeColor}; font-size: 12px;"></i> Câu giải thích / mở rộng:
                                </span>
                                ${explainHtml}
                            </div>
                        </div>
                    `;
                }).join('');
            } else if (sec.type === 'case_list') {
                bodyHtml = sec.cases.map(cs => {
                    let expandHtml = cs.expandSents.map(st => `
                        <div style="margin-bottom: 6px; padding-left: 12px;">
                            <p style="margin-bottom: 2px; color: var(--text-main); font-weight: 500;">• ${st.en}</p>
                            <p style="margin-bottom: 0; color: var(--text-muted); font-size: 13.5px; font-style: italic; padding-left: 8px;">(${st.vi})</p>
                        </div>
                    `).join('');

                    return `
                        <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px 16px; margin-bottom: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
                            <h5 style="color: ${sec.themeColor}; font-size: 15px; margin-bottom: 10px; font-weight: 700;">
                                ${cs.name}
                            </h5>
                            <div style="margin-bottom: 10px; padding-left: 4px;">
                                <span style="font-weight: 700; color: var(--text-main); font-size: 13.5px; display: block; margin-bottom: 3px;">
                                    <i class="fa-solid fa-star" style="color: #f59e0b; font-size: 12px;"></i> Câu chính:
                                </span>
                                <p style="margin-bottom: 2px; padding-left: 12px; font-weight: 600; color: #1e293b;">${cs.mainSent.en}</p>
                                <p style="margin-bottom: 0; padding-left: 12px; color: var(--text-muted); font-size: 13.5px; font-style: italic;">(${cs.mainSent.vi})</p>
                            </div>
                            <div style="padding-left: 4px; border-top: 1px dashed #e2e8f0; padding-top: 8px;">
                                <span style="font-weight: 700; color: var(--text-main); font-size: 13.5px; display: block; margin-bottom: 4px;">
                                    <i class="fa-solid fa-circle-info" style="color: ${sec.themeColor}; font-size: 12px;"></i> Câu mở rộng:
                                </span>
                                ${expandHtml}
                            </div>
                        </div>
                    `;
                }).join('');
            }

            return `
                <div class="outline-step" style="margin-bottom: 20px; border-left: 4px solid ${sec.themeColor};">
                    <h4 style="margin-bottom: 14px; color: ${sec.themeColor}; font-size: 16.5px; font-weight: 700;">
                        ${sec.sectionNumber}. ${sec.sectionTitle}
                    </h4>
                    ${bodyHtml}
                </div>
            `;
        }).join('');
    } else if (data.feedbackSections) {
        hintsHtml = data.feedbackSections.map(sec => {
            let catCardsHtml = sec.categories.map(cat => {
                let reasonsHtml = cat.reasons.map(r => `
                    <div style="margin-bottom: 6px; padding-left: 12px;">
                        <p style="margin-bottom: 2px; color: var(--text-main); font-weight: 500;">• ${r.en}</p>
                        <p style="margin-bottom: 0; color: var(--text-muted); font-size: 13.5px; font-style: italic; padding-left: 10px;">(${r.vi})</p>
                    </div>
                `).join('');

                let solHtml = '';
                if (cat.solutions && cat.solutions.length > 0) {
                    let solItems = cat.solutions.map(s => `
                        <div style="margin-bottom: 4px; padding-left: 12px;">
                            <span style="color: #059669; font-weight: 600;">➔ ${s.en}</span>
                            <span style="color: var(--text-muted); font-size: 13px; font-style: italic;"> (${s.vi})</span>
                        </div>
                    `).join('');

                    solHtml = `
                        <div style="margin-top: 10px; padding-top: 8px; border-top: 1px dashed #e2e8f0;">
                            <span style="font-weight: 700; color: #059669; font-size: 13.5px; display: block; margin-bottom: 4px;">
                                <i class="fa-solid fa-lightbulb"></i> Giải pháp đề xuất:
                            </span>
                            ${solItems}
                        </div>
                    `;
                }

                return `
                    <div style="background: #ffffff; border: 1px solid ${sec.borderCol}; border-radius: 8px; padding: 14px 16px; margin-bottom: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
                        <h5 style="color: ${sec.themeColor}; font-size: 15.5px; margin-bottom: 8px; font-weight: 700;">
                            ${cat.name}
                        </h5>
                        <div style="margin-bottom: 4px;">
                            <span style="font-weight: 700; color: var(--text-main); font-size: 13.5px; display: block; margin-bottom: 4px;">
                                <i class="fa-solid fa-angles-right" style="color: ${sec.themeColor};"></i> Lý do:
                            </span>
                            ${reasonsHtml}
                        </div>
                        ${solHtml}
                    </div>
                `;
            }).join('');

            return `
                <div class="outline-step" style="margin-bottom: 22px; border-left: 4px solid ${sec.themeColor};">
                    <h4 style="margin-bottom: 14px; color: ${sec.themeColor}; font-size: 17px; display: flex; align-items: center; gap: 8px;">
                        <i class="${sec.icon}"></i> ${sec.sectionTitle}
                    </h4>
                    ${catCardsHtml}
                </div>
            `;
        }).join('');
    } else if (data.hints) {
        hintsHtml = data.hints.map((hint, idx) => {
            if (hint.type === "complaint_triplet") {
                let itemsHtml = hint.items.map((item, itemIdx) => `
                    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px 16px; margin-bottom: 12px;">
                        <div style="margin-bottom: 8px;">
                            <span style="font-weight: 700; color: #dc2626; display: block; margin-bottom: 2px;">
                                ${itemIdx + 1}. Vấn đề phàn nàn:
                            </span>
                            <strong style="color: var(--text-main); font-size: 15px; padding-left: 12px; display: block;">${item.problemEn}</strong>
                            <span style="color: var(--text-muted); font-size: 13.5px; padding-left: 12px; display: block; font-style: italic;">(${item.problemVi})</span>
                        </div>

                        <div style="margin-bottom: 8px; padding-left: 12px; border-left: 3px solid #3b82f6; margin-left: 4px;">
                            <span style="font-weight: 700; color: #2563eb; display: block; margin-bottom: 2px;">
                                → Mô tả chi tiết:
                            </span>
                            <span style="color: var(--text-main); font-weight: 600; display: block;">${item.descEn}</span>
                            <span style="color: var(--text-muted); font-size: 13.5px; display: block; font-style: italic;">(${item.descVi})</span>
                        </div>

                        <div style="padding-left: 12px; border-left: 3px solid #10b981; margin-left: 4px;">
                            <span style="font-weight: 700; color: #059669; display: block; margin-bottom: 2px;">
                                → Đề xuất giải pháp:
                            </span>
                            <span style="color: #047857; font-weight: 600; display: block;">${item.solEn}</span>
                            <span style="color: var(--text-muted); font-size: 13.5px; display: block; font-style: italic;">(${item.solVi})</span>
                        </div>
                    </div>
                `).join('');

                return `
                    <div class="outline-step" style="margin-bottom: 18px;">
                        <h4 style="margin-bottom: 14px; color: var(--accent-red); font-size: 17px; display: flex; align-items: center; gap: 8px;">
                            <i class="fa-solid fa-circle-exclamation" style="color: #dc2626; font-size: 15px;"></i> ${hint.title}
                        </h4>
                        ${itemsHtml}
                    </div>
                `;
            } else if (hint.type === "custom_outline_choice") {
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
    }

    const promptBullets = data.prompt.split('\n').filter(l => l.startsWith('•')).map(l => `<li>${l.replace('•', '').trim()}</li>`).join('');
    const promptIntro = data.prompt.substring(0, data.prompt.indexOf('•')).trim();

    container.innerHTML = `
        <!-- Prompt Card (Using standard website style) -->
        <div class="sample-prompt-container">
            <div class="sample-prompt-header">
                <i class="fa-solid fa-file-circle-question"></i> ĐỀ BÀI (TOPIC PROMPT) - ${data.title}
            </div>
            <div class="sample-prompt-text">
                <p>${promptIntro.replace(/\n+/g, '<br>')}</p>
                <ul style="margin-top: 8px;">
                    ${promptBullets}
                </ul>
                <p style="margin-top: 10px; font-style: italic; color: var(--text-muted);">
                    <i class="fa-solid fa-triangle-exclamation" style="color: #f59e0b;"></i> You should write at least 120 words. Do not include your name or address. Your response will be evaluated in terms of Task Fulfillment, Organization, Vocabulary, and Grammar.
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
                <textarea id="extraWritingArea" placeholder="Dear Professor Smith,&#10;&#10;I am writing this email to sincerely apologize for..." rows="12"></textarea>
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
    if (/\b(complain\s+with)\b/gi.test(rawText)) {
        errors.push({
            type: "Giới từ đi kèm động từ",
            category: "grammar",
            wrong: "complain with",
            correct: "complain about",
            reason: "Phàn nàn về điều gì dùng 'complain about', không dùng 'complain with'."
        });
    }

    if (/\b(was|were)\s+not\s+satisfy\b/gi.test(rawText)) {
        errors.push({
            type: "Từ loại / Thể bị động",
            category: "grammar",
            wrong: "was not satisfy",
            correct: "was not satisfied",
            reason: "Sau to be diễn tả cảm xúc/tình trạng không hài lòng phải dùng tính từ/quá khứ phân từ 'satisfied'."
        });
    }

    if (/\blook\s+forward\s+to\s+(hear|receive)\b/gi.test(rawText)) {
        const m = rawText.match(/\blook\s+forward\s+to\s+(hear|receive)\b/i);
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
    if (/\b(places|dishes|clothes|teachers|skills|topics|lockers|showers|lights|hooks)\s+is\b/gi.test(rawText)) {
        const m = rawText.match(/\b(places|dishes|clothes|teachers|skills|topics|lockers|showers|lights|hooks)\s+is\b/i);
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

    if (typeId === 'application') {
        hasReq1 = /(apply|application|position|receptionist|student|major|graduate|advertis|looking|myself)/i.test(lower);
        hasReq2 = /(interest|passion|reputation|hotel|inspire|career|environment|why|passion)/i.test(lower);
        hasReq3 = /(experience|work|worked|part-time|customer|guest|receptionist|hotel|greet|call|booking|reservation)/i.test(lower);
        hasReq4 = /(suitable|candidate|skill|skills|fluent|english|computer|punctual|hard-working|cv|resume|interview)/i.test(lower);
        reqLabels = [
            hasReq1 ? '✓ Giới thiệu bản thân' : '✗ Giới thiệu bản thân',
            hasReq2 ? '✓ Lý do quan tâm' : '✗ Lý do quan tâm',
            hasReq3 ? '✓ Kinh nghiệm với khách hàng' : '✗ Kinh nghiệm với khách hàng',
            hasReq4 ? '✓ Giải thích độ phù hợp' : '✗ Giải thích độ phù hợp'
        ];
    } else if (typeId === 'apology') {
        hasReq1 = /(apologiz|apologise|sorry|apology|forgive|regret|excuse)/i.test(lower);
        hasReq2 = /(sick|ill|flu|fever|health|doctor|hospital|medical|break\s*down|broke\s*down|laptop|computer|error|accident|emergency|reason|because)/i.test(lower);
        hasReq3 = /(submit|send|email|portal|tomorrow|by|attach|certificate|hand\s+in|upload|tuesday|wednesday|pm)/i.test(lower);
        hasReq4 = true;
        reqLabels = [
            hasReq1 ? '✓ Lời xin lỗi chân thành' : '✗ Lời xin lỗi chân thành',
            hasReq2 ? '✓ Giải thích lý do chính đáng' : '✗ Giải thích lý do chính đáng',
            hasReq3 ? '✓ Nêu thời gian & cách thức nộp' : '✗ Nêu thời gian & cách thức nộp'
        ];
    } else if (typeId === 'feedback') {
        hasReq1 = /(satisf|dissatisf|overall|enjoy|opinion|pleas|feedback|impression|feel)/i.test(lower);
        hasReq2 = /(food|dish|dishes|fresh|delicious|atmosphere|music|decor|staff|wait|waiting|service|serve|dinner|restaurant|meal)/i.test(lower);
        hasReq3 = /(suggest|improve|service|hire|staff|waiter|faster|speed\s*up|menu|vegetarian|discount|loyalty|option|recommend|seasoning|clean)/i.test(lower);
        hasReq4 = true;
        reqLabels = [
            hasReq1 ? '✓ Mức độ hài lòng' : '✗ Mức độ hài lòng',
            hasReq2 ? '✓ Mô tả trải nghiệm' : '✗ Mô tả trải nghiệm',
            hasReq3 ? '✓ Đề xuất cải thiện dịch vụ' : '✗ Đề xuất cải thiện dịch vụ'
        ];
    } else if (typeId === 'complaint') {
        hasReq1 = /(problem|problems|room|condition|air\s*conditioner|ac|dirty|bathroom|shower|noise|noisy|broken|stained|towel|bed|sheet|water|wifi|tv)/i.test(lower);
        hasReq2 = /(feel|felt|disappoint|unhappy|annoyed|upset|ruin|ruined|terrible|bad\s*experience|frustrated|unpleasant|uncomfortable)/i.test(lower);
        hasReq3 = /(suggest|improvement|improve|repair|replace|clean|fix|refund|discount|compensation|service|better)/i.test(lower);
        hasReq4 = true;
        reqLabels = [
            hasReq1 ? '✓ Mô tả vấn đề của phòng' : '✗ Mô tả vấn đề của phòng',
            hasReq2 ? '✓ Bày tỏ cảm xúc' : '✗ Bày tỏ cảm xúc',
            hasReq3 ? '✓ Đề xuất cải thiện' : '✗ Đề xuất cải thiện'
        ];
    } else if (typeId === 'request' || typeId === 'description') {
        hasReq1 = /(address|location|where\s+(is\s+)?the\s+center|near\s+my\s+(house|home)|street|district|easy\s+to\s+(get|find)|located|tran\s+phu)/i.test(lower);
        hasReq2 = /(fee|tuition|cost|price|money|how\s+much|budget|discount|pay|million|vnd)/i.test(lower);
        hasReq3 = /(teacher|teachers|instructor|friendly|experienced|enthusiastic|native|teach|explain|helpful)/i.test(lower);
        hasReq4 = /(program|training|course|curriculum|skill|skills|schedule|length|study|practise|practice|topic|topics|activities)/i.test(lower);
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
    const hasOpening = /(thanks?\s+for|hope\s+you|writing\s+to|how\s+are\s+you|in\s+your\s+letter|i\s+am\s+writing)/i.test(lower);
    const hasClosingSentence = /(hope\s+my\s+advice|write\s+back|let\s+me\s+know|look\s+forward|hope\s+you\s+(can\s+help|will\s+find|will\s+look)|thank\s+you\s+for)/i.test(lower);
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

print("Updated Dạng 06 with rich detailed multi-scenario apology outline successfully!")
