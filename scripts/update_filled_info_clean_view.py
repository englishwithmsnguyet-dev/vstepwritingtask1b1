# -*- coding: utf-8 -*-
"""
Script to define exact filled-in information highlighting (.sample-filled-info)
for all 7 letter types, remove text-indent, and update the letters.
"""

CLEAN_FILLED_LETTERS = {
    "advice": {
        "en": """
<strong>Dear <span class="sample-filled-info">Helen</span>,</strong>
<p>Thanks for your letter. I hope you are doing well. I’m writing to give you some advice for <span class="sample-filled-info">your trip to Hanoi in June</span>.</p>
<p>Firstly, you should <span class="sample-filled-info">stay in a hotel in the city center because it is very convenient for travelling. Many famous places are also located near this area</span>. Secondly, it would be a good idea to <span class="sample-filled-info">try some traditional Vietnamese dishes such as pho, banh mi, and bun cha. These dishes are very popular and delicious</span>. Next, if I were you, I would <span class="sample-filled-info">visit some famous places in Hanoi such as Hoan Kiem Lake, the Old Quarter, and the Temple of Literature. These places are very beautiful and interesting</span>. Finally, remember to <span class="sample-filled-info">wear light and comfortable clothes because the weather in Hanoi can be quite hot in June</span>.</p>
<p>I hope my advice will be helpful to you. Please let me know how everything turns out. Write back soon.</p>
<strong>Best wishes,</strong>
""".strip(),
        "vi": """
<strong style="color: var(--text-main); display: block; margin-bottom: 14px;"><span class="sample-filled-info">Helen</span> thân mến,</strong>
<p>Cảm ơn thư của cậu. Tớ hy vọng cậu vẫn khỏe. Tớ viết thư này để đưa ra một vài gợi ý cho <span class="sample-filled-info">chuyến đi của cậu đến Hà Nội vào tháng Sáu</span>.</p>
<p>Đầu tiên, cậu nên <span class="sample-filled-info">ở một khách sạn tại trung tâm thành phố vì nó rất thuận tiện cho việc đi lại. Nhiều địa điểm nổi tiếng cũng nằm gần khu vực này</span>. Thứ hai, cậu nên <span class="sample-filled-info">thử một số món ăn truyền thống của Việt Nam như phở, bánh mì và bún chả. Những món ăn này rất phổ biến và ngon miệng</span>. Tiếp theo, nếu tớ là cậu, tớ sẽ <span class="sample-filled-info">tham quan một số địa điểm nổi tiếng ở Hà Nội như hồ Hoàn Kiếm, phố cổ và Văn Miếu Quốc Tử Giám. Những nơi này rất đẹp và thú vị</span>. Cuối cùng, hãy nhớ <span class="sample-filled-info">mặc quần áo mỏng nhẹ và thoải mái vì thời tiết Hà Nội vào tháng Sáu có thể khá nóng</span>.</p>
<p>Tớ hy vọng những lời khuyên của tớ sẽ giúp ích cho cậu. Hãy cho tớ biết chuyến đi diễn ra thế nào nhé. Hãy viết thư lại sớm nhé.</p>
<strong style="color: var(--text-main); display: block; margin-top: 14px;">Chúc cậu mọi điều tốt lành,</strong>
""".strip()
    },

    "request": {
        "en": """
<strong>Dear <span class="sample-filled-info">Moonie</span>,</strong>
<p>How are you? I hope you are doing well. I’m writing to ask for some information about <span class="sample-filled-info">the English course at Rainbow Language Center</span> because <span class="sample-filled-info">I am planning to study English there soon</span>.</p>
<p>First of all, could you tell me <span class="sample-filled-info">the address of the center</span>? I want to know <span class="sample-filled-info">if it is near my house</span>. In addition, I would like to know about <span class="sample-filled-info">the tuition fee for the course</span> so that <span class="sample-filled-info">I can prepare my budget</span>. Furthermore, can you tell me more about <span class="sample-filled-info">the teachers</span>? Are they <span class="sample-filled-info">friendly and experienced</span>? Finally, I was wondering if you could give me some details about <span class="sample-filled-info">the training program and the class schedule</span>.</p>
<p>I hope you can help me with this. Write back soon.</p>
<strong>Best wishes,</strong>
""".strip(),
        "vi": """
<strong style="color: var(--text-main); display: block; margin-bottom: 14px;"><span class="sample-filled-info">Moonie</span> thân mến,</strong>
<p>Cậu dạo này thế nào? Tớ hy vọng cậu vẫn khỏe. Tớ viết thư này để hỏi xin một vài thông tin về <span class="sample-filled-info">khóa học tiếng Anh tại Trung tâm Ngoại ngữ Rainbow</span> vì <span class="sample-filled-info">tớ đang có kế hoạch học tiếng Anh ở đó trong thời gian tới</span>.</p>
<p>Trước hết, cậu có thể cho tớ biết <span class="sample-filled-info">địa chỉ của trung tâm</span> được không? Tớ muốn biết <span class="sample-filled-info">liệu nó có ở gần nhà tớ không</span>. Ngoài ra, tớ cũng muốn biết về <span class="sample-filled-info">mức học phí của khóa học</span> để <span class="sample-filled-info">tớ có thể chuẩn bị ngân sách</span>. Hơn nữa, cậu có thể kể thêm cho tớ về <span class="sample-filled-info">các thầy cô giáo</span> không? Họ có <span class="sample-filled-info">thân thiện và giàu kinh nghiệm</span> không? Cuối cùng, tớ đang băn khoăn không biết cậu có thể chia sẻ cho tớ một vài chi tiết về <span class="sample-filled-info">chương trình đào tạo và lịch học</span> được không.</p>
<p>Tớ hy vọng cậu có thể giúp tớ việc này nhé. Hãy viết thư lại cho tớ sớm nhé.</p>
<strong style="color: var(--text-main); display: block; margin-top: 14px;">Chúc cậu mọi điều tốt lành,</strong>
""".strip()
    },

    "description": {
        "en": """
<strong>Dear <span class="sample-filled-info">Emily</span>,</strong>
<p>How are you? I hope you are doing well. In your letter, you asked me about <span class="sample-filled-info">my friend Hoa</span>, so here is some information.</p>
<p>Firstly, she is <span class="sample-filled-info">a very kind and friendly person. She gets on well with everyone and is always willing to help others</span>. Secondly, in her free time, she likes <span class="sample-filled-info">reading books, cooking traditional Vietnamese food, and listening to music. I think she would be happy to cook some delicious meals for your family</span>. Finally, she is <span class="sample-filled-info">currently studying business at university and works very hard. She is responsible and always keeps her room tidy</span>. Therefore, I believe she will <span class="sample-filled-info">fit in very well with your family</span>.</p>
<p>I hope you will find this information useful. Let me know if you need more details.</p>
<strong>Best wishes,</strong>
""".strip(),
        "vi": """
<strong style="color: var(--text-main); display: block; margin-bottom: 14px;"><span class="sample-filled-info">Emily</span> thân mến,</strong>
<p>Cậu dạo này thế nào? Tớ hy vọng cậu vẫn khỏe. Trong thư trước, cậu có hỏi tớ về <span class="sample-filled-info">bạn Hoa của tớ</span>, vậy nên dưới đây là một số thông tin nhé.</p>
<p>Đầu tiên, cô ấy là <span class="sample-filled-info">một người rất tốt bụng và thân thiện. Cô ấy hòa thuận với tất cả mọi người và luôn sẵn lòng giúp đỡ người khác</span>. Thứ hai, trong thời gian rảnh, cô ấy thích <span class="sample-filled-info">đọc sách, nấu các món ăn truyền thống của Việt Nam và nghe nhạc. Tớ nghĩ cô ấy sẽ rất vui khi được nấu một vài bữa ăn ngon cho gia đình cậu</span>. Cuối cùng, cô ấy hiện <span class="sample-filled-info">đang học ngành kinh doanh tại trường đại học và học tập rất chăm chỉ. Cô ấy là người có trách nhiệm và luôn giữ phòng ngủ ngăn nắp</span>. Vì vậy, tớ tin rằng cô ấy sẽ <span class="sample-filled-info">hòa nhập rất tốt với gia đình cậu</span>.</p>
<p>Tớ hy vọng cậu sẽ thấy những thông tin này hữu ích. Hãy cho tớ biết nếu cậu cần thêm chi tiết nhé.</p>
<strong style="color: var(--text-main); display: block; margin-top: 14px;">Chúc cậu mọi điều tốt lành,</strong>
""".strip()
    },

    "complaint": {
        "en": """
<strong>Dear Sir/Madam,</strong>
<p>I am writing to complain about <span class="sample-filled-info">the condition of the changing room at your sports center</span>. I recently used the facility and was not satisfied with it.</p>
<p>The main problem was that <span class="sample-filled-info">the floor was very dirty and wet, which was quite dangerous for members</span>. Another issue was that <span class="sample-filled-info">several lockers were broken, so I could not safely store my personal belongings</span>. Finally, I also found that <span class="sample-filled-info">some of the showers did not have hot water</span>. I was very disappointed with these problems because I have always enjoyed using your center. Therefore, I would appreciate it if you could <span class="sample-filled-info">clean the changing room more regularly, repair the broken lockers, and fix the showers as soon as possible</span>.</p>
<p>I hope that you will look into these issues soon. I look forward to receiving your reply soon.</p>
<strong>Yours faithfully,</strong>
""".strip(),
        "vi": """
<strong style="color: var(--text-main); display: block; margin-bottom: 14px;">Kính gửi Ông/Bà,</strong>
<p>Tôi viết thư này để phàn nàn về <span class="sample-filled-info">tình trạng của phòng thay đồ tại trung tâm thể thao của ông/bà</span>. Gần đây tôi đã sử dụng cơ sở vật chất này và không hài lòng với nó.</p>
<p>Vấn đề chính là <span class="sample-filled-info">sàn nhà rất bẩn và ẩm ướt, điều này khá nguy hiểm cho các hội viên</span>. Một vấn đề khác là <span class="sample-filled-info">một số tủ đựng đồ bị hỏng, vì vậy tôi không thể cất giữ đồ dùng cá nhân của mình một cách an toàn</span>. Cuối cùng, tôi cũng nhận thấy <span class="sample-filled-info">một số vòi hoa sen không có nước nóng</span>. Tôi rất thất vọng với những vấn đề này vì tôi luôn thích sử dụng trung tâm của ông/bà. Do đó, tôi sẽ rất cảm kích nếu ông/bà có thể <span class="sample-filled-info">dọn dẹp phòng thay đồ thường xuyên hơn, sửa chữa các tủ đựng đồ bị hỏng và sửa lại các vòi hoa sen càng sớm càng tốt</span>.</p>
<p>Tôi hy vọng ông/bà sẽ sớm xem xét các vấn đề này. Tôi rất mong sớm nhận được phản hồi từ ông/bà.</p>
<strong style="color: var(--text-main); display: block; margin-top: 14px;">Trân trọng,</strong>
""".strip()
    },

    "feedback": {
        "en": """
<strong>Dear Sir/Madam,</strong>
<p>I am writing to give you feedback on <span class="sample-filled-info">my recent stay at your hotel</span>. I recently used your services and would like to share my experience.</p>
<p>First of all, I would like to mention some positive points about your hotel. I was very satisfied with <span class="sample-filled-info">the customer service because the staff were polite, friendly, and always ready to assist guests</span>. In addition, <span class="sample-filled-info">the room was spacious and clean</span>. However, there were also some areas that needed improvement. I was disappointed with <span class="sample-filled-info">the Wi-Fi connection because it was slow and unstable</span>. Furthermore, <span class="sample-filled-info">the breakfast menu was quite limited and lacked variety</span>. To enhance the quality of your services, I suggest that you should <span class="sample-filled-info">upgrade the Internet system and offer more options for breakfast</span>.</p>
<p>I hope my feedback will help you improve your service. Please feel free to contact me if you have any further questions.</p>
<strong>Yours faithfully,</strong>
""".strip(),
        "vi": """
<strong style="color: var(--text-main); display: block; margin-bottom: 14px;">Kính gửi Ông/Bà,</strong>
<p>Tôi viết thư này để đưa ra phản hồi về <span class="sample-filled-info">kỳ nghỉ gần đây của tôi tại khách sạn của ông/bà</span>. Gần đây tôi đã sử dụng dịch vụ của ông/bà và muốn chia sẻ trải nghiệm của mình.</p>
<p>Trước hết, tôi muốn đề cập đến một số điểm tích cực về khách sạn của ông/bà. Tôi rất hài lòng với <span class="sample-filled-info">dịch vụ chăm sóc khách hàng vì nhân viên rất lịch sự, thân thiện và luôn sẵn sàng hỗ trợ khách</span>. Ngoài ra, <span class="sample-filled-info">phòng ốc rất rộng rãi và sạch sẽ</span>. Tuy nhiên, cũng có một số khía cạnh cần được cải thiện. Tôi đã thất vọng với <span class="sample-filled-info">kết nối Wi-Fi vì nó chậm và không ổn định</span>. Hơn nữa, <span class="sample-filled-info">thực đơn bữa sáng khá hạn chế và thiếu sự đa dạng</span>. Để nâng cao chất lượng dịch vụ của ông/bà, tôi đề nghị ông/bà nên <span class="sample-filled-info">nâng cấp hệ thống Internet và cung cấp nhiều sự lựa chọn hơn cho bữa sáng</span>.</p>
<p>Tôi hy vọng phản hồi của tôi sẽ giúp ông/bà cải thiện dịch vụ của mình. Xin vui lòng liên hệ với tôi nếu ông/bà có bất kỳ câu hỏi nào thêm.</p>
<strong style="color: var(--text-main); display: block; margin-top: 14px;">Trân trọng,</strong>
""".strip()
    },

    "apology": {
        "en": """
<strong>Dear <span class="sample-filled-info">Helen</span>,</strong>
<p>I’m really sorry for <span class="sample-filled-info">not returning your book earlier</span>. Let me explain what happened so you can understand the situation.</p>
<p>First of all, let me explain why this happened. I’m really sorry that I couldn’t <span class="sample-filled-info">return the book on time because I have been extremely busy preparing for my final exams. During that time, I had several assignments and an important test. As a result, I completely forgot about the book</span>. In addition, <span class="sample-filled-info">I have finished reading the whole book and found it very interesting and helpful</span>. Next, <span class="sample-filled-info">I plan to give it back to you this Saturday. I can come over to your house in the afternoon to return it in person</span>. Finally, let me make it up to you by <span class="sample-filled-info">treating you to a cup of milk tea and some snacks</span>.</p>
<p>Sorry once again. Thanks for taking the time to read this. Write back soon.</p>
<strong>Best wishes,</strong>
""".strip(),
        "vi": """
<strong style="color: var(--text-main); display: block; margin-bottom: 14px;"><span class="sample-filled-info">Helen</span> thân mến,</strong>
<p>Tớ thực sự xin lỗi vì <span class="sample-filled-info">đã không trả sách cho cậu sớm hơn</span>. Hãy để tớ giải thích những gì đã xảy ra để cậu hiểu rõ tình hình nhé.</p>
<p>Trước hết, hãy để tớ giải thích tại sao chuyện này lại xảy ra. Tớ thực sự xin lỗi vì tớ đã không thể <span class="sample-filled-info">trả sách đúng hạn vì tớ quá bận rộn chuẩn bị cho kỳ thi cuối kỳ. Trong thời gian đó, tớ có vài bài tập lớn và một bài kiểm tra quan trọng. Kết quả là tớ hoàn toàn quên mất cuốn sách</span>. Ngoài ra, <span class="sample-filled-info">tớ đã đọc xong toàn bộ cuốn sách và thấy nó rất thú vị và bổ ích</span>. Tiếp theo, <span class="sample-filled-info">tớ dự định sẽ trả lại sách cho cậu vào thứ Bảy tuần này. Tớ có thể ghé qua nhà cậu vào buổi chiều để trực tiếp gửi lại sách</span>. Cuối cùng, hãy để tớ bù đắp cho cậu bằng <span class="sample-filled-info">một chầu trà sữa và đồ ăn vặt nhé</span>.</p>
<p>Xin lỗi cậu một lần nữa nhé. Cảm ơn cậu vì đã dành thời gian đọc thư này. Hãy viết thư lại cho tớ sớm nhé.</p>
<strong style="color: var(--text-main); display: block; margin-top: 14px;">Chúc cậu mọi điều tốt lành,</strong>
""".strip()
    },

    "application": {
        "en": """
<strong>Dear Sir/Madam,</strong>
<p>I am writing to apply for the position of <span class="sample-filled-info">sales assistant</span> which was advertised on <span class="sample-filled-info">your website</span>.</p>
<p>I recently graduated from <span class="sample-filled-info">Can Tho University</span> with a bachelor’s degree in <span class="sample-filled-info">Business Administration</span>. During my studies, I developed a strong understanding of <span class="sample-filled-info">marketing and customer service</span>. I also gained useful knowledge and abilities such as <span class="sample-filled-info">communication and team collaboration</span>.</p>
<p>I am very interested in this position because it matches my interests and career goals. In addition, I enjoy <span class="sample-filled-info">helping customers choose suitable fashion products</span>. Therefore, I believe this job will give me a good opportunity to apply what I have learned during my studies and gain practical experience.</p>
<p>I worked part-time as a <span class="sample-filled-info">sales assistant</span> at a <span class="sample-filled-info">local clothing store</span>. In this job, I was responsible for <span class="sample-filled-info">welcoming customers and arranging products</span>. This experience helped me develop <span class="sample-filled-info">problem-solving skills and customer care skills</span>.</p>
<p>I believe I would be a suitable candidate for this position. This is because I am <span class="sample-filled-info">enthusiastic, honest, and hardworking</span>. Moreover, I am eager to learn and can adapt quickly to new environments.</p>
<p>I would be grateful if you could consider my application. I look forward to receiving your reply soon.</p>
<strong>Yours faithfully,</strong>
""".strip(),
        "vi": """
<strong style="color: var(--text-main); display: block; margin-bottom: 14px;">Kính gửi Ông/Bà,</strong>
<p>Tôi viết thư này để ứng tuyển vào vị trí <span class="sample-filled-info">nhân viên bán hàng</span> được quảng cáo trên <span class="sample-filled-info">trang web của ông/bà</span>.</p>
<p>Tôi vừa tốt nghiệp <span class="sample-filled-info">Đại học Cần Thơ</span> với tấm bằng cử nhân ngành <span class="sample-filled-info">Quản trị Kinh doanh</span>. Trong quá trình học, tôi đã phát triển sự hiểu biết sâu sắc về <span class="sample-filled-info">marketing và dịch vụ khách hàng</span>. Tôi cũng tích lũy được những kiến thức và năng lực hữu ích như <span class="sample-filled-info">giao tiếp và làm việc nhóm</span>.</p>
<p>Tôi rất hứng thú với vị trí này vì nó phù hợp với sở thích và mục tiêu nghề nghiệp của tôi. Ngoài ra, tôi thích <span class="sample-filled-info">giúp đỡ khách hàng lựa chọn những sản phẩm thời trang phù hợp</span>. Vì vậy, tôi tin rằng công việc này sẽ mang lại cho tôi cơ hội tốt để áp dụng những gì đã học trong quá trình học và tích lũy thêm kinh nghiệm thực tế.</p>
<p>Tôi đã từng làm việc bán thời gian với tư cách là <span class="sample-filled-info">nhân viên bán hàng</span> tại một <span class="sample-filled-info">cửa hàng quần áo địa phương</span>. Trong công việc này, tôi chịu trách nhiệm <span class="sample-filled-info">đón tiếp khách hàng và sắp xếp sản phẩm</span>. Kinh nghiệm này đã giúp tôi phát triển <span class="sample-filled-info">kỹ năng giải quyết vấn đề và kỹ năng chăm sóc khách hàng</span>.</p>
<p>Tôi tin rằng mình sẽ là ứng cử viên phù hợp cho vị trí này. Điều này là vì tôi là người <span class="sample-filled-info">nhiệt tình, trung thực và làm việc chăm chỉ</span>. Hơn nữa, tôi rất ham học hỏi và có thể thích nghi nhanh chóng với môi trường mới.</p>
<p>Tôi sẽ rất biết ơn nếu ông/bà có thể xem xét hồ sơ ứng tuyển của tôi. Tôi rất mong sớm nhận được phản hồi từ ông/bà.</p>
<strong style="color: var(--text-main); display: block; margin-top: 14px;">Trân trọng,</strong>
""".strip()
    }
}
