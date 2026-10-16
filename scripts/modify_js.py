import re

app_js_path = "/Users/nguyetpham/Desktop/WEBSITE/writing-letters/app.js"
index_html_path = "/Users/nguyetpham/Desktop/WEBSITE/writing-letters/index.html"

# Sample letters html content
samples = {
    "advice": """`
            <div class="content-block">
                <h3>Bài Viết Mẫu (Sample Letter - B1 Level)</h3>
                <div class="sample-letter-box" style="background-color: var(--bg-main); border: 1px solid var(--border-color); padding: 20px; border-radius: 12px; margin-top: 15px; font-family: var(--font-body); line-height: 1.8;">
                    <strong>Dear Helen,</strong><br><br>
                    Thanks for your letter. I am so excited to hear that you are going to visit Hanoi in June! It is a wonderful city with many interesting things to discover.<br><br>
                    First, about accommodation, it would be a good idea to stay in a hotel in the Old Quarter. It is very convenient for walking around and exploring the city life. Second, you should definitely try some local dishes such as Pho (noodle soup) and Bun Cha (grilled pork with noodles). They are incredibly delicious and popular here. Next, you can visit Hoan Kiem Lake, the Temple of Literature, and Ba Dinh Square, which are historic and beautiful places. Finally, because June is very hot and rainy in Hanoi, you should wear light, comfortable clothes like T-shirts and shorts. Do not forget to bring an umbrella or a raincoat.<br><br>
                    I hope my advice will be helpful to you. Write back soon!<br><br>
                    <strong>Best wishes,</strong><br>
                    [Your Name]
                </div>
                <div class="highlight-box" style="margin-top: 20px;">
                    <p><i class="fa-solid fa-lightbulb"></i> Số từ: ~145 từ. Bài viết sử dụng các từ nối rõ ràng: First, Second, Next, Finally và các cấu trúc lời khuyên chuẩn B1.</p>
                </div>
            </div>
        `""",
    "request": """`
            <div class="content-block">
                <h3>Bài Viết Mẫu (Sample Letter - B1 Level)</h3>
                <div class="sample-letter-box" style="background-color: var(--bg-main); border: 1px solid var(--border-color); padding: 20px; border-radius: 12px; margin-top: 15px; font-family: var(--font-body); line-height: 1.8;">
                    <strong>Dear Sir/Madam,</strong><br><br>
                    I am writing to request a room in the university campus accommodation for the upcoming academic year. I am an international student and will be studying at your university starting this September.<br><br>
                    My course begins on September 15th, 2026, and I would like to book a room from September 10th, 2026, to June 30th, 2027. Regarding my room preferences, I would prefer a single room with a private bathroom and access to a shared kitchen. This would help me study quietly while still being able to cook my own meals. Additionally, could you please provide me with more information about the tuition or accommodation payment process? I would like to know if I can pay the rent monthly or if I need to pay for the whole term in advance.<br><br>
                    Thank you in advance for your assistance. I look forward to hearing from you soon.<br><br>
                    <strong>Yours faithfully,</strong><br>
                    [Your Name]
                </div>
                <div class="highlight-box" style="margin-top: 20px;">
                    <p><i class="fa-solid fa-lightbulb"></i> Số từ: ~140 từ. Bài viết sử dụng văn phong trang trọng (formal) phù hợp cho thư yêu cầu gửi tổ chức/nhà trường.</p>
                </div>
            </div>
        `""",
    "description": """`
            <div class="content-block">
                <h3>Bài Viết Mẫu (Sample Letter - B1 Level)</h3>
                <div class="sample-letter-box" style="background-color: var(--bg-main); border: 1px solid var(--border-color); padding: 20px; border-radius: 12px; margin-top: 15px; font-family: var(--font-body); line-height: 1.8;">
                    <strong>Dear Emily,</strong><br><br>
                    How have you been? I am writing to tell you all about my recent holiday to Da Nang, a beautiful coastal city in Vietnam. It was an absolutely amazing trip!<br><br>
                    The scenery was stunning. The first thing that caught my eye was the long sandy beach with clear blue water and beautiful mountains in the background. The weather was sunny and warm, which was perfect for swimming. During my trip, I did many exciting activities. I went swimming in the sea, built sandcastles, and tried delicious fresh seafood at local restaurants. I also visited the famous Golden Bridge and took many photos. I felt extremely relaxed and happy during my stay. It was a great break from my busy study schedule.<br><br>
                    I can't wait to show you all the photos. Write back soon and tell me your news!<br><br>
                    <strong>Love,</strong><br>
                    [Your Name]
                </div>
                <div class="highlight-box" style="margin-top: 20px;">
                    <p><i class="fa-solid fa-lightbulb"></i> Số từ: ~140 từ. Bài viết sử dụng văn phong thân mật (informal) và nhiều tính từ miêu tả sinh động (stunning, amazing, relaxed).</p>
                </div>
            </div>
        `""",
    "complaint": """`
            <div class="content-block">
                <h3>Bài Viết Mẫu (Sample Letter - B1 Level)</h3>
                <div class="sample-letter-box" style="background-color: var(--bg-main); border: 1px solid var(--border-color); padding: 20px; border-radius: 12px; margin-top: 15px; font-family: var(--font-body); line-height: 1.8;">
                    <strong>Dear Sir/Madam,</strong><br><br>
                    I am writing to express my strong dissatisfaction with a laptop that I recently purchased from your online store. I ordered the laptop (Order Number #98765) on June 1st, and it was delivered to my house yesterday, June 10th.<br><br>
                    However, when I opened the package, I discovered several serious problems. First of all, the laptop screen was scratched badly in the upper left corner. Furthermore, when I turned on the device to test it, I realized that the keyboard did not work properly. Several keys, including the spacebar and the enter key, did not respond at all. Because of these issues, I am unable to use the laptop for my work. I would appreciate it if you could send me a replacement laptop as soon as possible, or issue a full refund.<br><br>
                    I look forward to your prompt response and resolving this matter.<br><br>
                    <strong>Yours faithfully,</strong><br>
                    [Your Name]
                </div>
                <div class="highlight-box" style="margin-top: 20px;">
                    <p><i class="fa-solid fa-lightbulb"></i> Số từ: ~150 từ. Thư phàn nàn sử dụng từ ngữ lịch sự nhưng kiên quyết, cung cấp đầy đủ thông tin mã đơn hàng, ngày mua và lỗi cụ thể.</p>
                </div>
            </div>
        `""",
    "feedback": """`
            <div class="content-block">
                <h3>Bài Viết Mẫu (Sample Letter - B1 Level)</h3>
                <div class="sample-letter-box" style="background-color: var(--bg-main); border: 1px solid var(--border-color); padding: 20px; border-radius: 12px; margin-top: 15px; font-family: var(--font-body); line-height: 1.8;">
                    <strong>Dear Sir/Madam,</strong><br><br>
                    I am writing to provide some feedback regarding my experience at the 3-day language workshop that I attended last weekend. Overall, it was a very useful event, but there are a few areas that could be improved.<br><br>
                    First of all, I was highly impressed by the quality of the speakers. The lessons were very interesting, and the group activities helped me practice my speaking skills and meet other students. However, I would like to point out one thing that was not satisfactory. The daily schedule was extremely tight, with very short breaks between sessions. This made it difficult to relax or network. It would be better if you could extend the lunch break to one hour next time. I hope my comments will be taken into consideration for future workshops.<br><br>
                    Thank you for organizing such a helpful event.<br><br>
                    <strong>Yours faithfully,</strong><br>
                    [Your Name]
                </div>
                <div class="highlight-box" style="margin-top: 20px;">
                    <p><i class="fa-solid fa-lightbulb"></i> Số từ: ~145 từ. Bài viết phản hồi nêu bật được cả điểm tốt (khen ngợi) và điểm chưa tốt (góp ý xây dựng) một cách khách quan.</p>
                </div>
            </div>
        `""",
    "apology": """`
            <div class="content-block">
                <h3>Bài Viết Mẫu (Sample Letter - B1 Level)</h3>
                <div class="sample-letter-box" style="background-color: var(--bg-main); border: 1px solid var(--border-color); padding: 20px; border-radius: 12px; margin-top: 15px; font-family: var(--font-body); line-height: 1.8;">
                    <strong>Dear Helen,</strong><br><br>
                    I am writing to sincerely apologize because I have to cancel our plan to meet this weekend. I was really looking forward to catching up with you, but unfortunately, an unexpected family event has come up.<br><br>
                    My grandparents are celebrating their 50th wedding anniversary this Sunday, and my parents want me to join the family gathering. Since my grandparents live in another town, I will have to travel there on Saturday and stay until Monday. I am very sorry for any inconvenience this may cause you. To make up for this, I would like to rearrange our meeting. Are you free to meet next Saturday afternoon instead? We could go to our favorite coffee shop.<br><br>
                    Once again, please accept my sincere apologies. Hope to see you soon!<br><br>
                    <strong>Best wishes,</strong><br>
                    [Your Name]
                </div>
                <div class="highlight-box" style="margin-top: 20px;">
                    <p><i class="fa-solid fa-lightbulb"></i> Số từ: ~135 từ. Bài viết xin lỗi bạn bè chân thành, giải thích lý do hợp lý và đề xuất rõ ràng phương án bù đắp.</p>
                </div>
            </div>
        `""",
    "application": """`
            <div class="content-block">
                <h3>Bài Viết Mẫu (Sample Letter - B1 Level)</h3>
                <div class="sample-letter-box" style="background-color: var(--bg-main); border: 1px solid var(--border-color); padding: 20px; border-radius: 12px; margin-top: 15px; font-family: var(--font-body); line-height: 1.8;">
                    <strong>Dear Hiring Manager,</strong><br><br>
                    I am writing to apply for the part-time tour guide position at your travel agency, which was advertised on your website yesterday. I am a university student majoring in English and am very interested in this job.<br><br>
                    I believe I am well-qualified for this role because I have excellent English speaking skills, which allows me to communicate confidently with international tourists. Furthermore, having lived in this city for over ten years, I possess deep knowledge of the local area, including its history, culture, and famous tourist attractions. I also worked part-time as a volunteer guide for a student club last year, which helped me develop good communication and problem-solving skills. I am reliable, energetic, and eager to learn.<br><br>
                    I have attached my CV for your consideration. I am available for an interview at your convenience.<br><br>
                    <strong>Yours sincerely,</strong><br>
                    [Your Name]
                </div>
                <div class="highlight-box" style="margin-top: 20px;">
                    <p><i class="fa-solid fa-lightbulb"></i> Số từ: ~150 từ. Thư xin việc trang trọng, nêu bật được thế mạnh về tiếng Anh, sự hiểu biết địa phương và kinh nghiệm liên quan.</p>
                </div>
            </div>
        `"""
}

# Read app.js
with open(app_js_path, "r", encoding="utf-8") as f:
    js_content = f.read()

# Insert sampleWriting into each letterTypes object in app.js
for key, sample_html in samples.items():
    # We find where id: 'key' is, and then find the next practicePrompt: '...'
    # Then we replace it to include sampleWriting property.
    # Note: id: 'advice', id: 'request', etc.
    pattern = rf"(id:\s*'{key}',.*?(practicePrompt:\s*'.*?'))"
    match = re.search(pattern, js_content, re.DOTALL)
    if match:
        original_block = match.group(1)
        replacement = original_block + ",\n        sampleWriting: " + sample_html
        js_content = js_content.replace(original_block, replacement)
        print(f"Injected sampleWriting for {key} in app.js")
    else:
        print(f"Could not find block for {key} in app.js")

# Write modified app.js
with open(app_js_path, "w", encoding="utf-8") as f:
    f.write(js_content)

print("app.js modification completed.")
