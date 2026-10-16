# -*- coding: utf-8 -*-
"""
Generates multi-colored filled-in content (.sample-filled-info with .filled-c1 through .filled-c6),
sets line-height to 2.25, and removes all text underlines.
"""

CLEAN_FILLED_LETTERS_MULTICOLOR = {
    "advice": {
        "en": """
<strong>Dear <span class="sample-filled-info filled-c1">Helen</span>,</strong>
<p>Thanks for your letter. I hope you are doing well. I’m writing to give you some advice for <span class="sample-filled-info filled-c2">your trip to Hanoi in June</span>.</p>
<p>Firstly, you should <span class="sample-filled-info filled-c3">stay in a hotel in the city center because it is very convenient for travelling. Many famous places are also located near this area</span>. Secondly, it would be a good idea to <span class="sample-filled-info filled-c4">try some traditional Vietnamese dishes such as pho, banh mi, and bun cha. These dishes are very popular and delicious</span>. Next, if I were you, I would <span class="sample-filled-info filled-c5">visit some famous places in Hanoi such as Hoan Kiem Lake, the Old Quarter, and the Temple of Literature. These places are very beautiful and interesting</span>. Finally, remember to <span class="sample-filled-info filled-c6">wear light and comfortable clothes because the weather in Hanoi can be quite hot in June</span>.</p>
<p>I hope my advice will be helpful to you. Please let me know how everything turns out. Write back soon.</p>
<strong>Best wishes,</strong>
""".strip(),
        "vi": """
<strong style="color: var(--text-main); display: block; margin-bottom: 14px;"><span class="sample-filled-info filled-c1">Helen</span> thân mến,</strong>
<p>Cảm ơn thư của cậu. Tớ hy vọng cậu vẫn khỏe. Tớ viết thư này để đưa ra một vài gợi ý cho <span class="sample-filled-info filled-c2">chuyến đi của cậu đến Hà Nội vào tháng Sáu</span>.</p>
<p>Đầu tiên, cậu nên <span class="sample-filled-info filled-c3">ở một khách sạn tại trung tâm thành phố vì nó rất thuận tiện cho việc đi lại. Nhiều địa điểm nổi tiếng cũng nằm gần khu vực này</span>. Thứ hai, cậu nên <span class="sample-filled-info filled-c4">thử một số món ăn truyền thống của Việt Nam như phở, bánh mì và bún chả. Những món ăn này rất phổ biến và ngon miệng</span>. Tiếp theo, nếu tớ là cậu, tớ sẽ <span class="sample-filled-info filled-c5">tham quan một số địa điểm nổi tiếng ở Hà Nội như hồ Hoàn Kiếm, phố cổ và Văn Miếu Quốc Tử Giám. Những nơi này rất đẹp và thú vị</span>. Cuối cùng, hãy nhớ <span class="sample-filled-info filled-c6">mặc quần áo mỏng nhẹ và thoải mái vì thời tiết Hà Nội vào tháng Sáu có thể khá nóng</span>.</p>
<p>Tớ hy vọng những lời khuyên của tớ sẽ giúp ích cho cậu. Hãy cho tớ biết chuyến đi diễn ra thế nào nhé. Hãy viết thư lại sớm nhé.</p>
<strong style="color: var(--text-main); display: block; margin-top: 14px;">Chúc cậu mọi điều tốt lành,</strong>
""".strip()
    },

    "request": {
        "en": """
<strong>Dear <span class="sample-filled-info filled-c1">Moonie</span>,</strong>
<p>How are you? I hope you are doing well. I’m writing to ask for some information about <span class="sample-filled-info filled-c2">the English course at Rainbow Language Center</span> because <span class="sample-filled-info filled-c2">I am planning to study English there soon</span>.</p>
<p>First of all, could you tell me <span class="sample-filled-info filled-c3">the address of the center</span>? I want to know <span class="sample-filled-info filled-c3">if it is near my house</span>. In addition, I would like to know about <span class="sample-filled-info filled-c4">the tuition fee for the course</span> so that <span class="sample-filled-info filled-c4">I can prepare my budget</span>. Furthermore, can you tell me more about <span class="sample-filled-info filled-c5">the teachers</span>? Are they <span class="sample-filled-info filled-c5">friendly and experienced</span>? Finally, I was wondering if you could give me some details about <span class="sample-filled-info filled-c6">the training program and the class schedule</span>.</p>
<p>I hope you can help me with this. Write back soon.</p>
<strong>Best wishes,</strong>
""".strip(),
        "vi": """
<strong style="color: var(--text-main); display: block; margin-bottom: 14px;"><span class="sample-filled-info filled-c1">Moonie</span> thân mến,</strong>
<p>Cậu dạo này thế nào? Tớ hy vọng cậu vẫn khỏe. Tớ viết thư này để hỏi xin một vài thông tin về <span class="sample-filled-info filled-c2">khóa học tiếng Anh tại Trung tâm Ngoại ngữ Rainbow</span> vì <span class="sample-filled-info filled-c2">tớ đang có kế hoạch học tiếng Anh ở đó trong thời gian tới</span>.</p>
<p>Trước hết, cậu có thể cho tớ biết <span class="sample-filled-info filled-c3">địa chỉ của trung tâm</span> được không? Tớ muốn biết <span class="sample-filled-info filled-c3">liệu nó có ở gần nhà tớ không</span>. Ngoài ra, tớ cũng muốn biết về <span class="sample-filled-info filled-c4">mức học phí của khóa học</span> để <span class="sample-filled-info filled-c4">tớ có thể chuẩn bị ngân sách</span>. Hơn nữa, cậu có thể kể thêm cho tớ về <span class="sample-filled-info filled-c5">các thầy cô giáo</span> không? Họ có <span class="sample-filled-info filled-c5">thân thiện và giàu kinh nghiệm</span> không? Cuối cùng, tớ đang băn khoăn không biết cậu có thể chia sẻ cho tớ một vài chi tiết về <span class="sample-filled-info filled-c6">chương trình đào tạo và lịch học</span> được không.</p>
<p>Tớ hy vọng cậu có thể giúp tớ việc này nhé. Hãy viết thư lại cho tớ sớm nhé.</p>
<strong style="color: var(--text-main); display: block; margin-top: 14px;">Chúc cậu mọi điều tốt lành,</strong>
""".strip()
    },

    "description": {
        "en": """
<strong>Dear <span class="sample-filled-info filled-c1">Emily</span>,</strong>
<p>How are you? I hope you are doing well. In your letter, you asked me about <span class="sample-filled-info filled-c2">my friend Hoa</span>, so here is some information.</p>
<p>Firstly, she is <span class="sample-filled-info filled-c3">a very kind and friendly person. She gets on well with everyone and is always willing to help others</span>. Secondly, in her free time, she likes <span class="sample-filled-info filled-c4">reading books, cooking traditional Vietnamese food, and listening to music. I think she would be happy to cook some delicious meals for your family</span>. Finally, she is <span class="sample-filled-info filled-c5">currently studying business at university and works very hard. She is responsible and always keeps her room tidy</span>. Therefore, I believe she will <span class="sample-filled-info filled-c6">fit in very well with your family</span>.</p>
<p>I hope you will find this information useful. Let me know if you need more details.</p>
<strong>Best wishes,</strong>
""".strip(),
        "vi": """
<strong style="color: var(--text-main); display: block; margin-bottom: 14px;"><span class="sample-filled-info filled-c1">Emily</span> thân mến,</strong>
<p>Cậu dạo này thế nào? Tớ hy vọng cậu vẫn khỏe. Trong thư trước, cậu có hỏi tớ về <span class="sample-filled-info filled-c2">bạn Hoa của tớ</span>, vậy nên dưới đây là một số thông tin nhé.</p>
<p>Đầu tiên, cô ấy là <span class="sample-filled-info filled-c3">một người rất tốt bụng và thân thiện. Cô ấy hòa thuận với tất cả mọi người và luôn sẵn lòng giúp đỡ người khác</span>. Thứ hai, trong thời gian rảnh, cô ấy thích <span class="sample-filled-info filled-c4">đọc sách, nấu các món ăn truyền thống của Việt Nam và nghe nhạc. Tớ nghĩ cô ấy sẽ rất vui khi được nấu một vài bữa ăn ngon cho gia đình cậu</span>. Cuối cùng, cô ấy hiện <span class="sample-filled-info filled-c5">đang học ngành kinh doanh tại trường đại học và học tập rất chăm chỉ. Cô ấy là người có trách nhiệm và luôn giữ phòng ngủ ngăn nắp</span>. Vì vậy, tớ tin rằng cô ấy sẽ <span class="sample-filled-info filled-c6">hòa nhập rất tốt với gia đình cậu</span>.</p>
<p>Tớ hy vọng cậu sẽ thấy những thông tin này hữu ích. Hãy cho tớ biết nếu cậu cần thêm chi tiết nhé.</p>
<strong style="color: var(--text-main); display: block; margin-top: 14px;">Chúc cậu mọi điều tốt lành,</strong>
""".strip()
    },

    "complaint": {
        "en": """
<strong>Dear Sir/Madam,</strong>
<p>I am writing to complain about <span class="sample-filled-info filled-c2">the condition of the changing room at your sports center</span>. I recently used the facility and was not satisfied with it.</p>
<p>The main problem was that <span class="sample-filled-info filled-c3">the floor was very dirty and wet, which was quite dangerous for members</span>. Another issue was that <span class="sample-filled-info filled-c4">several lockers were broken, so I could not safely store my personal belongings</span>. Finally, I also found that <span class="sample-filled-info filled-c5">some of the showers did not have hot water</span>. I was very disappointed with these problems because I have always enjoyed using your center. Therefore, I would appreciate it if you could <span class="sample-filled-info filled-c6">clean the changing room more regularly, repair the broken lockers, and fix the showers as soon as possible</span>.</p>
<p>I hope that you will look into these issues soon. I look forward to receiving your reply soon.</p>
<strong>Yours faithfully,</strong>
""".strip(),
        "vi": """
<strong style="color: var(--text-main); display: block; margin-bottom: 14px;">Kính gửi Ông/Bà,</strong>
<p>Tôi viết thư này để phàn nàn về <span class="sample-filled-info filled-c2">tình trạng của phòng thay đồ tại trung tâm thể thao của ông/bà</span>. Gần đây tôi đã sử dụng cơ sở vật chất này và không hài lòng với nó.</p>
<p>Vấn đề chính là <span class="sample-filled-info filled-c3">sàn nhà rất bẩn và ẩm ướt, điều này khá nguy hiểm cho các hội viên</span>. Một vấn đề khác là <span class="sample-filled-info filled-c4">một số tủ đựng đồ bị hỏng, vì vậy tôi không thể cất giữ đồ dùng cá nhân của mình một cách an toàn</span>. Cuối cùng, tôi cũng nhận thấy <span class="sample-filled-info filled-c5">một số vòi hoa sen không có nước nóng</span>. Tôi rất thất vọng với những vấn đề này vì tôi luôn thích sử dụng trung tâm của ông/bà. Do đó, tôi sẽ rất cảm kích nếu ông/bà có thể <span class="sample-filled-info filled-c6">dọn dẹp phòng thay đồ thường xuyên hơn, sửa chữa các tủ đựng đồ bị hỏng và sửa lại các vòi hoa sen càng sớm càng tốt</span>.</p>
<p>Tôi hy vọng ông/bà sẽ sớm xem xét các vấn đề này. Tôi rất mong sớm nhận được phản hồi từ ông/bà.</p>
<strong style="color: var(--text-main); display: block; margin-top: 14px;">Trân trọng,</strong>
""".strip()
    },

    "feedback": {
        "en": """
<strong>Dear Sir/Madam,</strong>
<p>I am writing to give you feedback on <span class="sample-filled-info filled-c2">my recent stay at your hotel</span>. I recently used your services and would like to share my experience.</p>
<p>First of all, I would like to mention some positive points about your hotel. I was very satisfied with <span class="sample-filled-info filled-c3">the customer service because the staff were polite, friendly, and always ready to assist guests</span>. In addition, <span class="sample-filled-info filled-c4">the room was spacious and clean</span>. However, there were also some areas that needed improvement. I was disappointed with <span class="sample-filled-info filled-c5">the Wi-Fi connection because it was slow and unstable</span>. Furthermore, <span class="sample-filled-info filled-c5">the breakfast menu was quite limited and lacked variety</span>. To enhance the quality of your services, I suggest that you should <span class="sample-filled-info filled-c6">upgrade the Internet system and offer more options for breakfast</span>.</p>
<p>I hope my feedback will help you improve your service. Please feel free to contact me if you have any further questions.</p>
<strong>Yours faithfully,</strong>
""".strip(),
        "vi": """
<strong style="color: var(--text-main); display: block; margin-bottom: 14px;">Kính gửi Ông/Bà,</strong>
<p>Tôi viết thư này để đưa ra phản hồi về <span class="sample-filled-info filled-c2">kỳ nghỉ gần đây của tôi tại khách sạn của ông/bà</span>. Gần đây tôi đã sử dụng dịch vụ của ông/bà và muốn chia sẻ trải nghiệm của mình.</p>
<p>Trước hết, tôi muốn đề cập đến một số điểm tích cực về khách sạn của ông/bà. Tôi rất hài lòng với <span class="sample-filled-info filled-c3">dịch vụ chăm sóc khách hàng vì nhân viên rất lịch sự, thân thiện và luôn sẵn sàng hỗ trợ khách</span>. Ngoài ra, <span class="sample-filled-info filled-c4">phòng ốc rất rộng rãi và sạch sẽ</span>. Tuy nhiên, cũng có một số khía cạnh cần được cải thiện. Tôi đã thất vọng với <span class="sample-filled-info filled-c5">kết nối Wi-Fi vì nó chậm và không ổn định</span>. Hơn nữa, <span class="sample-filled-info filled-c5">thực đơn bữa sáng khá hạn chế và thiếu sự đa dạng</span>. Để nâng cao chất lượng dịch vụ của ông/bà, tôi đề nghị ông/bà nên <span class="sample-filled-info filled-c6">nâng cấp hệ thống Internet và cung cấp nhiều sự lựa chọn hơn cho bữa sáng</span>.</p>
<p>Tôi hy vọng phản hồi của tôi sẽ giúp ông/bà cải thiện dịch vụ của mình. Xin vui lòng liên hệ với tôi nếu ông/bà có bất kỳ câu hỏi nào thêm.</p>
<strong style="color: var(--text-main); display: block; margin-top: 14px;">Trân trọng,</strong>
""".strip()
    },

    "apology": {
        "en": """
<strong>Dear <span class="sample-filled-info filled-c1">Helen</span>,</strong>
<p>I’m really sorry for <span class="sample-filled-info filled-c2">not returning your book earlier</span>. Let me explain what happened so you can understand the situation.</p>
<p>First of all, let me explain why this happened. I’m really sorry that I couldn’t <span class="sample-filled-info filled-c3">return the book on time because I have been extremely busy preparing for my final exams. During that time, I had several assignments and an important test. As a result, I completely forgot about the book</span>. In addition, <span class="sample-filled-info filled-c4">I have finished reading the whole book and found it very interesting and helpful</span>. Next, <span class="sample-filled-info filled-c5">I plan to give it back to you this Saturday. I can come over to your house in the afternoon to return it in person</span>. Finally, let me make it up to you by <span class="sample-filled-info filled-c6">treating you to a cup of milk tea and some snacks</span>.</p>
<p>Sorry once again. Thanks for taking the time to read this. Write back soon.</p>
<strong>Best wishes,</strong>
""".strip(),
        "vi": """
<strong style="color: var(--text-main); display: block; margin-bottom: 14px;"><span class="sample-filled-info filled-c1">Helen</span> thân mến,</strong>
<p>Tớ thực sự xin lỗi vì <span class="sample-filled-info filled-c2">đã không trả sách cho cậu sớm hơn</span>. Hãy để tớ giải thích những gì đã xảy ra để cậu hiểu rõ tình hình nhé.</p>
<p>Trước hết, hãy để tớ giải thích tại sao chuyện này lại xảy ra. Tớ thực sự xin lỗi vì tớ đã không thể <span class="sample-filled-info filled-c3">trả sách đúng hạn vì tớ quá bận rộn chuẩn bị cho kỳ thi cuối kỳ. Trong thời gian đó, tớ có vài bài tập lớn và một bài kiểm tra quan trọng. Kết quả là tớ hoàn toàn quên mất cuốn sách</span>. Ngoài ra, <span class="sample-filled-info filled-c4">tớ đã đọc xong toàn bộ cuốn sách và thấy nó rất thú vị và bổ ích</span>. Tiếp theo, <span class="sample-filled-info filled-c5">tớ dự định sẽ trả lại sách cho cậu vào thứ Bảy tuần này. Tớ có thể ghé qua nhà cậu vào buổi chiều để trực tiếp gửi lại sách</span>. Cuối cùng, hãy để tớ bù đắp cho cậu bằng <span class="sample-filled-info filled-c6">một chầu trà sữa và đồ ăn vặt nhé</span>.</p>
<p>Xin lỗi cậu một lần nữa nhé. Cảm ơn cậu vì đã dành thời gian đọc thư này. Hãy viết thư lại cho tớ sớm nhé.</p>
<strong style="color: var(--text-main); display: block; margin-top: 14px;">Chúc cậu mọi điều tốt lành,</strong>
""".strip()
    },

    "application": {
        "en": """
<strong>Dear Sir/Madam,</strong>
<p>I am writing to apply for the position of <span class="sample-filled-info filled-c1">sales assistant</span> which was advertised on <span class="sample-filled-info filled-c2">your website</span>.</p>
<p>I recently graduated from <span class="sample-filled-info filled-c3">Can Tho University</span> with a bachelor’s degree in <span class="sample-filled-info filled-c3">Business Administration</span>. During my studies, I developed a strong understanding of <span class="sample-filled-info filled-c3">marketing and customer service</span>. I also gained useful knowledge and abilities such as <span class="sample-filled-info filled-c3">communication and team collaboration</span>.</p>
<p>I am very interested in this position because it matches my interests and career goals. In addition, I enjoy <span class="sample-filled-info filled-c4">helping customers choose suitable fashion products</span>. Therefore, I believe this job will give me a good opportunity to apply what I have learned during my studies and gain practical experience.</p>
<p>I worked part-time as a <span class="sample-filled-info filled-c5">sales assistant</span> at a <span class="sample-filled-info filled-c5">local clothing store</span>. In this job, I was responsible for <span class="sample-filled-info filled-c5">welcoming customers and arranging products</span>. This experience helped me develop <span class="sample-filled-info filled-c5">problem-solving skills and customer care skills</span>.</p>
<p>I believe I would be a suitable candidate for this position. This is because I am <span class="sample-filled-info filled-c6">enthusiastic, honest, and hardworking</span>. Moreover, I am eager to learn and can adapt quickly to new environments.</p>
<p>I would be grateful if you could consider my application. I look forward to receiving your reply soon.</p>
<strong>Yours faithfully,</strong>
""".strip(),
        "vi": """
<strong style="color: var(--text-main); display: block; margin-bottom: 14px;">Kính gửi Ông/Bà,</strong>
<p>Tôi viết thư này để ứng tuyển vào vị trí <span class="sample-filled-info filled-c1">nhân viên bán hàng</span> được quảng cáo trên <span class="sample-filled-info filled-c2">trang web của ông/bà</span>.</p>
<p>Tôi vừa tốt nghiệp <span class="sample-filled-info filled-c3">Đại học Cần Thơ</span> với tấm bằng cử nhân ngành <span class="sample-filled-info filled-c3">Quản trị Kinh doanh</span>. Trong quá trình học, tôi đã phát triển sự hiểu biết sâu sắc về <span class="sample-filled-info filled-c3">marketing và dịch vụ khách hàng</span>. Tôi cũng tích lũy được những kiến thức và năng lực hữu ích như <span class="sample-filled-info filled-c3">giao tiếp và làm việc nhóm</span>.</p>
<p>Tôi rất hứng thú với vị trí này vì nó phù hợp với sở thích và mục tiêu nghề nghiệp của tôi. Ngoài ra, tôi thích <span class="sample-filled-info filled-c4">giúp đỡ khách hàng lựa chọn những sản phẩm thời trang phù hợp</span>. Vì vậy, tôi tin rằng công việc này sẽ mang lại cho tôi cơ hội tốt để áp dụng những gì đã học trong quá trình học và tích lũy thêm kinh nghiệm thực tế.</p>
<p>Tôi đã từng làm việc bán thời gian với tư cách là <span class="sample-filled-info filled-c5">nhân viên bán hàng</span> tại một <span class="sample-filled-info filled-c5">cửa hàng quần áo địa phương</span>. Trong công việc này, tôi chịu trách nhiệm <span class="sample-filled-info filled-c5">đón tiếp khách hàng và sắp xếp sản phẩm</span>. Kinh nghiệm này đã giúp tôi phát triển <span class="sample-filled-info filled-c5">kỹ năng giải quyết vấn đề và kỹ năng chăm sóc khách hàng</span>.</p>
<p>Tôi tin rằng mình sẽ là ứng cử viên phù hợp cho vị trí này. Điều này là vì tôi là người <span class="sample-filled-info filled-c6">nhiệt tình, trung thực và làm việc chăm chỉ</span>. Hơn nữa, tôi rất ham học hỏi và có thể thích nghi nhanh chóng với môi trường mới.</p>
<p>Tôi sẽ rất biết ơn nếu ông/bà có thể xem xét hồ sơ ứng tuyển của tôi. Tôi rất mong sớm nhận được phản hồi từ ông/bà.</p>
<strong style="color: var(--text-main); display: block; margin-top: 14px;">Trân trọng,</strong>
""".strip()
    }
}

# 1. Update generate_enhanced_sample_writings.py
gen_path = "/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/generate_enhanced_sample_writings.py"
with open(gen_path, "r", encoding="utf-8") as f:
    gen_code = f.read()

# Replace CLEAN_FILLED_LETTERS with CLEAN_FILLED_LETTERS_MULTICOLOR
idx_start = gen_code.find("CLEAN_FILLED_LETTERS = {")
idx_end = gen_code.find("def generate_sample_html(")

import pprint
import json

dict_py = "CLEAN_FILLED_LETTERS = " + json.dumps(CLEAN_FILLED_LETTERS_MULTICOLOR, ensure_ascii=False, indent=4) + "\n\n"

if idx_start != -1 and idx_end != -1:
    gen_code = gen_code[:idx_start] + dict_py + gen_code[idx_end:]
    print("Replaced CLEAN_FILLED_LETTERS with multicolor version in generate_enhanced_sample_writings.py")
else:
    print("Warning: could not find CLEAN_FILLED_LETTERS range")

with open(gen_path, "w", encoding="utf-8") as f:
    f.write(gen_code)

# 2. Update style.css
css_path = "/Users/nguyetpham/Desktop/WEBSITE/writing-letters-b1level/style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

# Make line-height wider and paragraph margin more spacious
# In .sample-letter-box
import re
css_content = re.sub(
    r'\.sample-letter-box\s*\{[^}]*line-height:\s*[^;]+;[^}]*\}',
    lambda m: re.sub(r'line-height:\s*[^;]+;', 'line-height: 2.3;', m.group(0)),
    css_content
)

# In .sample-letter-box p
css_content = re.sub(
    r'\.sample-letter-box p\s*\{[^}]*\}',
    '''.sample-letter-box p {
    margin: 0 0 22px 0;
    line-height: 2.3;
    text-indent: 0 !important;
}''',
    css_content
)

# In .translation-box and .translation-box p
css_content = re.sub(
    r'\.translation-box p\s*\{[^}]*\}',
    '''.translation-box p {
    margin: 0 0 20px 0;
    line-height: 2.2;
    text-indent: 0 !important;
}''',
    css_content
)

# Replace .sample-filled-info and add color variations (c1 to c6) WITHOUT underline
sample_filled_styles = """
/* Highlight for Filled-in Information (Thông tin đã thế vào - Không gạch chân, đa màu sắc, dãn dòng thoáng) */
.sample-filled-info {
    font-weight: 700;
    padding: 3px 8px;
    border-radius: 6px;
    display: inline;
    border: none !important;
    border-bottom: none !important;
    text-decoration: none !important;
    box-shadow: none !important;
    line-height: inherit;
    margin: 0 2px;
}

/* Color 1: Sapphire Blue */
.sample-filled-info.filled-c1 {
    color: #1e40af;
    background-color: rgba(219, 234, 254, 0.85);
}
[data-theme="dark"] .sample-filled-info.filled-c1 {
    color: #93c5fd;
    background-color: rgba(30, 58, 138, 0.45);
}

/* Color 2: Emerald Green */
.sample-filled-info.filled-c2 {
    color: #065f46;
    background-color: rgba(209, 250, 229, 0.85);
}
[data-theme="dark"] .sample-filled-info.filled-c2 {
    color: #6ee7b7;
    background-color: rgba(6, 78, 59, 0.45);
}

/* Color 3: Warm Amber / Golden */
.sample-filled-info.filled-c3 {
    color: #92400e;
    background-color: rgba(254, 243, 199, 0.9);
}
[data-theme="dark"] .sample-filled-info.filled-c3 {
    color: #fcd34d;
    background-color: rgba(120, 53, 15, 0.45);
}

/* Color 4: Rich Violet / Purple */
.sample-filled-info.filled-c4 {
    color: #5b21b6;
    background-color: rgba(237, 233, 254, 0.85);
}
[data-theme="dark"] .sample-filled-info.filled-c4 {
    color: #c4b5fd;
    background-color: rgba(76, 29, 149, 0.45);
}

/* Color 5: Rose Coral */
.sample-filled-info.filled-c5 {
    color: #9f1239;
    background-color: rgba(255, 228, 230, 0.9);
}
[data-theme="dark"] .sample-filled-info.filled-c5 {
    color: #fda4af;
    background-color: rgba(136, 19, 55, 0.45);
}

/* Color 6: Deep Teal / Ocean */
.sample-filled-info.filled-c6 {
    color: #155e75;
    background-color: rgba(207, 250, 254, 0.9);
}
[data-theme="dark"] .sample-filled-info.filled-c6 {
    color: #67e8f9;
    background-color: rgba(22, 78, 99, 0.45);
}
"""

# Replace old .sample-filled-info in style.css
css_content = re.sub(
    r'/\* Highlight for Filled-in Information.*?\n\[data-theme="dark"\] \.sample-filled-info \{[^}]*\}',
    sample_filled_styles.strip(),
    css_content,
    flags=re.DOTALL
)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css_content)

print("Updated style.css with wider line-height and multi-colored filled-in styles successfully!")
