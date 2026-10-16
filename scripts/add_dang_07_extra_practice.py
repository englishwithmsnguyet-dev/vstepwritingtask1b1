# -*- coding: utf-8 -*-
with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/pure_extra_logic.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# Let's find where apology ends and insert application
idx_apology_end = js_code.find("        sampleModelVi: `Kính gửi Giáo sư Smith,")
idx_bracket_end = js_code.find("    }\n};", idx_apology_end)

application_data = r"""
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
"""

# Let's insert application_data before };
js_code = js_code[:idx_bracket_end + 5] + ",\n" + application_data.strip() + js_code[idx_bracket_end + 5:]

# Update prompt placeholder to include all 7 types
js_code = js_code.replace(
    "Vui lòng chọn từ <strong>Dạng 01</strong> đến <strong>Dạng 06</strong> để làm bài luyện tập.",
    "Vui lòng chọn từ <strong>Dạng 01</strong> đến <strong>Dạng 07</strong> để làm bài luyện tập."
)

# Update gradeExtraPractice for application type
idx_apology_check = js_code.find("if (typeId === 'apology') {")
if idx_apology_check != -1:
    app_req_logic = """if (typeId === 'application') {
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
    } else if (typeId === 'apology') {"""
    js_code = js_code[:idx_apology_check] + app_req_logic + js_code[idx_apology_check + len("if (typeId === 'apology') {"):]

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/pure_extra_logic.js", "w", encoding="utf-8") as f:
    f.write(js_code)

print("Added Dạng 07 (Letter of Application) to pure_extra_logic.js successfully!")
