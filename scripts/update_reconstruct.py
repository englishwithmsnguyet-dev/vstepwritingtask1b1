# Script to build the updated reconstruct_app.py
import os

code = '''import json

app_js_path = "/Users/nguyetpham/Desktop/WEBSITE/writing-letters-b1level/app.js"

letter_types = [
    {
        "id": "advice",
        "icon": "fa-lightbulb",
        "titleEn": "Letter of Advice",
        "titleVi": "Thư Cho Lời Khuyên",
        "basicInfo": """
            <div class="content-block">
                <h3>Mục đích (Purpose)</h3>
                <p>Đưa ra lời khuyên, gợi ý hoặc đề xuất để giúp người nhận giải quyết một vấn đề hoặc đưa ra quyết định phù hợp trong một tình huống cụ thể.</p>
            </div>
            <div class="content-block">
                <h3>Phong cách thư (Style)</h3>
                <p>Chủ yếu là thư thân mật (Informal Letter).</p>
            </div>
            <div class="content-block">
                <h3>Văn phong (Tone)</h3>
                <p>Thân thiện, quan tâm, hỗ trợ và khích lệ.</p>
            </div>
        """,
        "identifyingSigns": """
            <div class="content-block">
                <h3>Các từ khóa thường xuất hiện trong đề bài:</h3>
                <ul>
                    <li>advice / give me some advice / ask for advice</li>
                    <li>suggestions / recommendations</li>
                    <li>what should I do...? / what would you suggest...?</li>
                    <li>I need your advice with...</li>
                </ul>
            </div>
        """,
        "detailedOutline": """
            <div class="outline-note">
                <p><strong>LƯU Ý:</strong> Thư cho lời khuyên thường là thư thân mật.</p>
            </div>
            <div class="outline-step">
                <h4>1. Lời chào mở đầu</h4>
                <p>- Thân mật: ↳ <span class="outline-phrase">Dear [tên của người nhận],</span></p>
            </div>
            <div class="outline-step">
                <h4>2. Mở thư</h4>
                <p>- Thân mật: ↳ <span class="outline-phrase">Thanks for your letter. I hope you are doing well. I’m writing to give you some advice about your situation.</span></p>
            </div>
            <div class="outline-step">
                <h4>3. Thân thư</h4>
                <p>Lần lượt đưa ra lời khuyên/gợi ý phù hợp với tình huống của đề.</p>
                <div class="outline-structures">
                    <h5>CẤU TRÚC CHO LỜI KHUYÊN:</h5>
                    <ul>
                        <li>↳ <span class="outline-phrase">You should + Vo.</span></li>
                        <li>↳ <span class="outline-phrase">It would be a good idea to + Vo.</span></li>
                        <li>↳ <span class="outline-phrase">If I were you, I would + Vo.</span></li>
                        <li>↳ <span class="outline-phrase">You can try + Ving.</span></li>
                        <li>↳ <span class="outline-phrase">Remember to + Vo. / Don’t forget to + Vo.</span></li>
                    </ul>
                </div>
                <p>TỪ LIÊN KẾT GỢI Ý: ↳ <em>First, … → Second, … → Next, … → Finally, …</em></p>
            </div>
            <div class="outline-step">
                <h4>4. Kết thư</h4>
                <p>- Thân mật: ↳ <span class="outline-phrase">I hope my advice will be helpful to you. Please let me know how everything turns out. Write back soon.</span></p>
            </div>
            <div class="outline-step">
                <h4>5. Lời chào kết thúc</h4>
                <p>- Thân mật: ↳ <span class="outline-phrase">Best wishes,</span></p>
            </div>
        """,
        "practicePrompt": "You have received a letter from an English friend, Helen. She is going to visit Hanoi in June. Write a letter to give her some suggestions. In your letter, you should tell her: Where to stay, What dishes to try, Which places to visit, What to wear when visiting Hanoi. You should write at least 120 words. Do not include your name or address.",
        "sampleWriting": """
            <!-- Prompt Card -->
            <div class="sample-prompt-container">
                <div class="sample-prompt-header">
                    <i class="fa-solid fa-file-circle-question"></i> ĐỀ BÀI (TOPIC PROMPT)
                </div>
                <div class="sample-prompt-text">
                    <p>You have received a letter from an English friend, Helen. She is going to visit Hanoi in June. Write a letter to give her some suggestions. In your letter, you should tell her:</p>
                    <ul>
                        <li>Where to stay</li>
                        <li>What dishes to try</li>
                        <li>Which places to visit</li>
                        <li>What to wear when visiting Hanoi</li>
                    </ul>
                    <p style="margin-top: 8px; font-style: italic; color: var(--text-muted);">You should write at least 120 words. Do not include your name or address.</p>
                </div>
                <div class="sample-analysis-grid">
                    <div class="sample-analysis-item">
                        <strong>Người nhận</strong>
                        <span>Helen (Bạn bè người Anh)</span>
                    </div>
                    <div class="sample-analysis-item">
                        <strong>Mục đích</strong>
                        <span>Gợi ý cho chuyến du lịch Hà Nội vào tháng 6</span>
                    </div>
                    <div class="sample-analysis-item">
                        <strong>Văn phong</strong>
                        <span>Thân mật (Informal Letter)</span>
                    </div>
                    <div class="sample-analysis-item">
                        <strong>Yêu cầu cốt lõi</strong>
                        <span>Nơi ở, món ăn, điểm tham quan, trang phục</span>
                    </div>
                </div>
            </div>

            <div class="content-block">
                <h3>BÀI VIẾT MẪU (SAMPLE LETTER - B1 LEVEL)</h3>
                <div class="sample-letter-box">
                    <strong>Dear Helen,</strong><br><br>
                    Thanks for your letter. I hope you are doing well. I’m writing to give you some advice for your trip to Hanoi in June.<br><br>
                    Firstly, you should stay in a hotel in the city center because it is very convenient for travelling. Many famous places are also located near this area. Secondly, it would be a good idea to try some traditional Vietnamese dishes such as pho, banh mi, and bun cha. These dishes are very popular and delicious. Next, if I were you, I would visit some famous places in Hanoi such as Hoan Kiem Lake, the Old Quarter, and the Temple of Literature. These places are very beautiful and interesting. Finally, remember to wear light and comfortable clothes because the weather in Hanoi can be quite hot in June.<br><br>
                    I hope my advice will be helpful to you. Please let me know how everything turns out. Write back soon.<br><br>
                    <strong>Best wishes,</strong>
                </div>
                
                <h3 style="margin-top: 25px;">BẢN DỊCH CHI TIẾT</h3>
                <div class="translation-box" style="background-color: var(--bg-main); border: 1px solid var(--border-color); padding: 20px; border-radius: 12px; margin-top: 15px; font-family: var(--font-body); line-height: 1.8; color: var(--text-muted); font-style: italic;">
                    <strong>Helen thân mến,</strong><br><br>
                    Cảm ơn thư của cậu. Tớ hy vọng cậu vẫn khỏe. Tớ viết thư này để đưa ra một vài gợi ý cho chuyến đi của cậu đến Hà Nội vào tháng Sáu.<br><br>
                    Đầu tiên, cậu nên ở một khách sạn tại trung tâm thành phố vì nó rất thuận tiện cho việc đi lại. Nhiều địa điểm nổi tiếng cũng nằm gần khu vực này. Thứ hai, cậu nên thử một số món ăn truyền thống của Việt Nam như phở, bánh mì và bún chả. Những món ăn này rất phổ biến và ngon miệng. Tiếp theo, nếu tớ là cậu, tớ sẽ tham quan một số địa điểm nổi tiếng ở Hà Nội như hồ Hoàn Kiếm, phố cổ và Văn Miếu Quốc Tử Giám. Những nơi này rất đẹp và thú vị. Cuối cùng, hãy nhớ mặc quần áo mỏng nhẹ và thoải mái vì thời tiết Hà Nội vào tháng Sáu có thể khá nóng.<br><br>
                    Tớ hy vọng những lời khuyên của tớ sẽ giúp ích cho cậu. Hãy cho tớ biết chuyến đi diễn ra thế nào nhé. Hãy viết thư lại sớm nhé.<br><br>
                    <strong>Chúc cậu mọi điều tốt lành,</strong>
                </div>
                
                <div class="highlight-box" style="margin-top: 20px;">
                    <p><i class="fa-solid fa-lightbulb"></i> Số từ: 155 words. Bài viết chia đoạn rõ ràng, đáp ứng đầy đủ 4 yêu cầu của đề và sử dụng linh hoạt các mẫu câu khuyên bảo chuẩn B1.</p>
                </div>
            </div>
        """
    },
    {
        "id": "request",
        "icon": "fa-hand-holding-hand",
        "titleEn": "Letter of Request",
        "titleVi": "Thư Yêu Cầu",
        "basicInfo": """
            <div class="content-block">
                <h3>Mục đích (Purpose)</h3>
                <p>Yêu cầu hoặc xin thông tin, sự giúp đỡ, hoặc đề nghị một hành động cụ thể từ người nhận.</p>
            </div>
            <div class="content-block">
                <h3>Phong cách thư (Style)</h3>
                <p>Có thể là thư thân mật, bán trang trọng hoặc trang trọng tùy thuộc vào đối tượng người nhận.</p>
            </div>
            <div class="content-block">
                <h3>Văn phong (Tone)</h3>
                <p>Lịch sự, rõ ràng, trực tiếp và thể hiện sự tôn trọng.</p>
            </div>
        """,
        "identifyingSigns": """
            <div class="content-block">
                <h3>Các từ khóa thường xuất hiện trong đề bài:</h3>
                <ul>
                    <li>ask for information / request details</li>
                    <li>could you please tell me / I would like to know</li>
                    <li>write a letter to ask about...</li>
                    <li>inquire about...</li>
                </ul>
            </div>
        """,
        "detailedOutline": """
            <div class="outline-note">
                <p><strong>LƯU Ý:</strong> Thư yêu cầu thường được dùng để xin thông tin, xin giúp đỡ hoặc đề nghị điều gì đó. Thư có thể là thư thân mật, bán trang trọng hoặc trang trọng.</p>
            </div>
            <div class="outline-step">
                <h4>1. Lời chào mở đầu</h4>
                <ul>
                    <li>- Thân mật: ↳ <span class="outline-phrase">Dear [tên của người nhận],</span></li>
                    <li>- Trang trọng:
                        <ul>
                            <li>↳ <span class="outline-phrase">Dear Sir,</span> (nếu biết chắc chắn người nhận là nam)</li>
                            <li>↳ <span class="outline-phrase">Dear Madam,</span> (nếu biết chắc chắn người nhận là nữ)</li>
                            <li>↳ <span class="outline-phrase">Dear Sir/Madam,</span> (nếu không biết chắc chắn người nhận là nam hay nữ)</li>
                        </ul>
                    </li>
                    <li>- Bán trang trọng: ↳ <span class="outline-phrase">Dear Mr. / Ms. / Mrs. [họ của người nhận],</span></li>
                </ul>
            </div>
            <div class="outline-step">
                <h4>2. Mở thư</h4>
                <ul>
                    <li>- Thân mật: ↳ <span class="outline-phrase">How are you? I hope you are doing well. I’m writing to ask for some information about [thứ cần xin thông tin] because [lý do].</span></li>
                    <li>- Trang trọng & Bán trang trọng: ↳ <span class="outline-phrase">I am writing to request some information about [thứ cần xin thông tin] because [lý do].</span></li>
                </ul>
            </div>
            <div class="outline-step">
                <h4>3. Thân thư</h4>
                <p>Lần lượt đưa ra các yêu cầu xin thông tin theo đề bài.</p>
                <div class="outline-structures">
                    <h5>CẤU TRÚC XIN THÔNG TIN (THÂN MẬT):</h5>
                    <ul>
                        <li>↳ <span class="outline-phrase">Can you give me more information about …?</span></li>
                        <li>↳ <span class="outline-phrase">Can you tell me more about …?</span></li>
                        <li>↳ <span class="outline-phrase">Can you let me know more about …?</span></li>
                        <li>↳ <span class="outline-phrase">I want to know more about …</span></li>
                        <li>↳ <span class="outline-phrase">I want more information about …</span></li>
                    </ul>
                    <h5>CẤU TRÚC XIN THÔNG TIN (TRANG TRỌNG & BÁN TRANG TRỌNG):</h5>
                    <ul>
                        <li>↳ <span class="outline-phrase">Could you provide me with more information about …?</span></li>
                        <li>↳ <span class="outline-phrase">Could you give me more details about …?</span></li>
                        <li>↳ <span class="outline-phrase">I would like to know more about …</span></li>
                        <li>↳ <span class="outline-phrase">I would like to inquire about …</span></li>
                        <li>↳ <span class="outline-phrase">I am also wondering about …</span></li>
                    </ul>
                </div>
            </div>
            <div class="outline-step">
                <h4>4. Kết thư</h4>
                <ul>
                    <li>- Thân mật: ↳ <span class="outline-phrase">I hope you can help me with this. Write back soon.</span></li>
                    <li>- Trang trọng & Bán trang trọng: ↳ <span class="outline-phrase">Thank you for your time. I look forward to your reply.</span></li>
                </ul>
            </div>
            <div class="outline-step">
                <h4>5. Lời chào kết thúc</h4>
                <ul>
                    <li>- Thân mật: ↳ <span class="outline-phrase">Best wishes,</span></li>
                    <li>- Trang trọng: ↳ <span class="outline-phrase">Yours faithfully,</span></li>
                    <li>- Bán trang trọng: ↳ <span class="outline-phrase">Yours sincerely,</span></li>
                </ul>
            </div>
        """,
        "practicePrompt": "Your friend has just completed an English course at Rainbow Language Center and had a great experience. You are planning to study English as well and would like to know more about the course. Write a letter to your friend asking for more information about the course. In your email, you should ask about: The address of the center, The tuition fee, The teachers, The training program. You should write at least 120 words. Do not include your name or address.",
        "sampleWriting": """
            <!-- Prompt Card -->
            <div class="sample-prompt-container">
                <div class="sample-prompt-header">
                    <i class="fa-solid fa-file-circle-question"></i> ĐỀ BÀI (TOPIC PROMPT)
                </div>
                <div class="sample-prompt-text">
                    <p>Your friend has just completed an English course at Rainbow Language Center and had a great experience. You are planning to study English as well and would like to know more about the course. Write a letter to your friend asking for more information about the course. In your email, you should ask about:</p>
                    <ul>
                        <li>The address of the center</li>
                        <li>The tuition fee</li>
                        <li>The teachers</li>
                        <li>The training program</li>
                    </ul>
                    <p style="margin-top: 8px; font-style: italic; color: var(--text-muted);">You should write at least 120 words. Do not include your name or address.</p>
                </div>
                <div class="sample-analysis-grid">
                    <div class="sample-analysis-item">
                        <strong>Người nhận</strong>
                        <span>Bạn của bạn (Moonie)</span>
                    </div>
                    <div class="sample-analysis-item">
                        <strong>Mục đích</strong>
                        <span>Hỏi xin thông tin về khóa học tiếng Anh tại Rainbow Language Center</span>
                    </div>
                    <div class="sample-analysis-item">
                        <strong>Văn phong</strong>
                        <span>Thân mật (Informal Letter)</span>
                    </div>
                    <div class="sample-analysis-item">
                        <strong>Yêu cầu cốt lõi</strong>
                        <span>Địa chỉ trung tâm, học phí, giáo viên, chương trình học</span>
                    </div>
                </div>
            </div>

            <div class="content-block">
                <h3>BÀI VIẾT MẪU (SAMPLE LETTER - B1 LEVEL)</h3>
                <div class="sample-letter-box">
                    <strong>Dear Moonie,</strong><br><br>
                    How are you? I hope you are doing well. I’m writing to ask for some information about the English course at Rainbow Language Center because I am planning to study English there soon.<br><br>
                    First of all, could you tell me the address of the center? I want to know if it is near my house. In addition, I would like to know about the tuition fee for the course so that I can prepare my budget. Furthermore, can you tell me more about the teachers? Are they friendly and experienced? Finally, I was wondering if you could give me some details about the training program and the class schedule.<br><br>
                    I hope you can help me with this. Write back soon.<br><br>
                    <strong>Best wishes,</strong>
                </div>
                
                <h3 style="margin-top: 25px;">BẢN DỊCH CHI TIẾT</h3>
                <div class="translation-box" style="background-color: var(--bg-main); border: 1px solid var(--border-color); padding: 20px; border-radius: 12px; margin-top: 15px; font-family: var(--font-body); line-height: 1.8; color: var(--text-muted); font-style: italic;">
                    <strong>Moonie thân mến,</strong><br><br>
                    Cậu khỏe không? Tớ hy vọng cậu vẫn khỏe. Tớ viết thư này để hỏi một vài thông tin về khóa học tiếng Anh tại Trung tâm Ngoại ngữ Rainbow vì tớ đang có kế hoạch học tiếng Anh ở đó sắp tới.<br><br>
                    Trước hết, cậu có thể cho tớ biết địa chỉ của trung tâm không? Tớ muốn biết liệu nó có gần nhà tớ không. Ngoài ra, tớ muốn biết về học phí của khóa học để tớ có thể chuẩn bị ngân sách của mình. Hơn nữa, cậu có thể kể thêm cho tớ về các giáo viên ở đó không? Họ có thân thiện và giàu kinh nghiệm không? Cuối cùng, tớ đang băn khoăn liệu cậu có thể cho tớ biết thêm chi tiết về chương trình đào tạo và lịch học không.<br><br>
                    Tớ hy vọng cậu có thể giúp tớ việc này. Hãy trả lời thư sớm nhé.<br><br>
                    <strong>Chúc cậu mọi điều tốt lành,</strong>
                </div>
                
                <div class="highlight-box" style="margin-top: 20px;">
                    <p><i class="fa-solid fa-lightbulb"></i> Số từ: 142 words. Thư yêu cầu thông tin thân thiện, sử dụng đa dạng các mẫu câu hỏi gián tiếp lịch sự và tự nhiên.</p>
                </div>
            </div>
        """
    },
    {
        "id": "description",
        "icon": "fa-circle-info",
        "titleEn": "Letter of Giving Information",
        "titleVi": "Thư Cung Cấp Thông Tin",
        "basicInfo": """
            <div class="content-block">
                <h3>Mục đích (Purpose)</h3>
                <p>Cung cấp thông tin chi tiết hoặc mô tả về một người, một sự kiện, địa điểm, hoặc một trải nghiệm cụ thể theo yêu cầu của người nhận.</p>
            </div>
            <div class="content-block">
                <h3>Phong cách thư (Style)</h3>
                <p>Có thể là thư thân mật, bán trang trọng hoặc trang trọng tùy ngữ cảnh đề bài.</p>
            </div>
            <div class="content-block">
                <h3>Văn phong (Tone)</h3>
                <p>Rõ ràng, chi tiết, khách quan và hữu ích.</p>
            </div>
        """,
        "identifyingSigns": """
            <div class="content-block">
                <h3>Các từ khóa thường xuất hiện trong đề bài:</h3>
                <ul>
                    <li>tell me about / give me information about...</li>
                    <li>describe your... / describe someone...</li>
                    <li>could you provide some details on...</li>
                    <li>let me know what... is like</li>
                </ul>
            </div>
        """,
        "detailedOutline": """
            <div class="outline-note">
                <p><strong>LƯU Ý:</strong> Thư cung cấp thông tin/mô tả dùng để cung cấp thông tin hoặc mô tả đặc điểm của một người, địa điểm, sự việc hoặc chương trình. Dạng thư này có thể là thư thân mật, bán trang trọng hoặc trang trọng.</p>
            </div>
            <div class="outline-step">
                <h4>1. Lời chào mở đầu</h4>
                <ul>
                    <li>- Thân mật: ↳ <span class="outline-phrase">Dear [tên của người nhận],</span></li>
                    <li>- Trang trọng:
                        <ul>
                            <li>↳ <span class="outline-phrase">Dear Sir,</span> (nếu biết chắc chắn người nhận là nam)</li>
                            <li>↳ <span class="outline-phrase">Dear Madam,</span> (nếu biết chắc chắn người nhận là nữ)</li>
                            <li>↳ <span class="outline-phrase">Dear Sir/Madam,</span> (nếu không biết chắc chắn người nhận là nam hay nữ)</li>
                        </ul>
                    </li>
                    <li>- Bán trang trọng: ↳ <span class="outline-phrase">Dear Mr. / Ms. / Mrs. [họ của người nhận],</span></li>
                </ul>
            </div>
            <div class="outline-step">
                <h4>2. Mở thư</h4>
                <div class="outline-structures">
                    <h5>KHI THƯ YÊU CẦU CUNG CẤP THÔNG TIN:</h5>
                    <ul>
                        <li>- Thân mật: ↳ <span class="outline-phrase">How are you? I hope you are doing well. In your letter, you asked me about [thứ cần mô tả thông tin], so here is some information.</span></li>
                        <li>- Trang trọng & Bán trang trọng: ↳ <span class="outline-phrase">In your letter, you asked me about [thứ cần mô tả thông tin], so I am writing to provide you with some information.</span></li>
                    </ul>
                    <h5>KHI THƯ YÊU CẦU MÔ TẢ MỘT ĐỐI TƯỢNG (NGƯỜI/VẬT/SỰ VIỆC):</h5>
                    <ul>
                        <li>- Thân mật: ↳ <span class="outline-phrase">How are you? I hope you are doing well. In your letter, you asked me to describe [thứ cần mô tả], so here are some details.</span></li>
                        <li>- Trang trọng & Bán trang trọng: ↳ <span class="outline-phrase">In your letter, you asked me to describe [thứ cần mô tả], so I am writing to provide you with some details.</span></li>
                    </ul>
                </div>
            </div>
            <div class="outline-step">
                <h4>3. Thân thư</h4>
                <p>Lần lượt cung cấp thông tin hoặc miêu tả các khía cạnh theo yêu cầu của đề.</p>
                <p>TỪ LIÊN KẾT GỢI Ý: ↳ <em>First, … → Second, … → Next, … → Finally, …</em></p>
            </div>
            <div class="outline-step">
                <h4>4. Kết thư</h4>
                <ul>
                    <li>- Thân mật: ↳ <span class="outline-phrase">I hope you will find this information useful. Let me know if you need more details.</span></li>
                    <li>- Trang trọng & Bán trang trọng: ↳ <span class="outline-phrase">I hope the information above will be helpful to you. Please feel free to contact me if you need more details.</span></li>
                </ul>
            </div>
            <div class="outline-step">
                <h4>5. Lời chào kết thúc</h4>
                <ul>
                    <li>- Thân mật: ↳ <span class="outline-phrase">Best wishes,</span></li>
                    <li>- Trang trọng: ↳ <span class="outline-phrase">Yours faithfully,</span></li>
                    <li>- Bán trang trọng: ↳ <span class="outline-phrase">Yours sincerely,</span></li>
                </ul>
            </div>
        """,
        "practicePrompt": "You have received a letter from your English friend, Emily. Read part of her letter below: ... I have received a letter from your friend, Hoa. She is going to do a course in London, so she asked me if she could stay with me and my family until she finds an apartment. Could you tell me some information about her? (things like her personality, her hobbies, her current work or study). I need to know whether she will fit in my family or not ... Write a letter responding to Emily. You should write at least 120 words. Do not include your name or address.",
        "sampleWriting": """
            <!-- Prompt Card -->
            <div class="sample-prompt-container">
                <div class="sample-prompt-header">
                    <i class="fa-solid fa-file-circle-question"></i> ĐỀ BÀI (TOPIC PROMPT)
                </div>
                <div class="sample-prompt-text">
                    <p>You have received a letter from your English friend, Emily. Read part of her letter below:</p>
                    <p style="margin: 10px 0; padding: 10px 14px; background: rgba(0,0,0,0.03); border-left: 3px solid var(--accent-red); font-style: italic;">
                        "... I have received a letter from your friend, Hoa. She is going to do a course in London, so she asked me if she could stay with me and my family until she finds an apartment. Could you tell me some information about her? (things like her personality, her hobbies, her current work or study). I need to know whether she will fit in my family or not ..."
                    </p>
                    <p>Write a letter responding to Emily. You should write at least 120 words. Do not include your name or address.</p>
                </div>
                <div class="sample-analysis-grid">
                    <div class="sample-analysis-item">
                        <strong>Người nhận</strong>
                        <span>Emily (Bạn bè người Anh)</span>
                    </div>
                    <div class="sample-analysis-item">
                        <strong>Mục đích</strong>
                        <span>Cung cấp thông tin và miêu tả về bạn Hoa để xem có phù hợp ở chung không</span>
                    </div>
                    <div class="sample-analysis-item">
                        <strong>Văn phong</strong>
                        <span>Thân mật (Informal Letter)</span>
                    </div>
                    <div class="sample-analysis-item">
                        <strong>Yêu cầu cốt lõi</strong>
                        <span>Tính cách, sở thích, việc học/làm hiện tại của Hoa và khả năng hòa nhập</span>
                    </div>
                </div>
            </div>

            <div class="content-block">
                <h3>BÀI VIẾT MẪU (SAMPLE LETTER - B1 LEVEL)</h3>
                <div class="sample-letter-box">
                    <strong>Dear Emily,</strong><br><br>
                    How are you? I hope you are doing well. In your letter, you asked me about my friend Hoa, so here is some information.<br><br>
                    Firstly, she is a very kind and friendly person. She gets on well with everyone and is always willing to help others. Secondly, in her free time, she likes reading books, cooking traditional Vietnamese food, and listening to music. I think she would be happy to cook some delicious meals for your family. Finally, she is currently studying business at university and works very hard. She is responsible and always keeps her room tidy. Therefore, I believe she will fit in very well with your family.<br><br>
                    I hope you will find this information useful. Let me know if you need more details.<br><br>
                    <strong>Best wishes,</strong>
                </div>
                
                <h3 style="margin-top: 25px;">BẢN DỊCH CHI TIẾT</h3>
                <div class="translation-box" style="background-color: var(--bg-main); border: 1px solid var(--border-color); padding: 20px; border-radius: 12px; margin-top: 15px; font-family: var(--font-body); line-height: 1.8; color: var(--text-muted); font-style: italic;">
                    <strong>Emily thân mến,</strong><br><br>
                    Cậu khỏe không? Tớ hy vọng cậu vẫn khỏe. Trong thư của cậu, cậu đã hỏi tớ về bạn Hoa của tớ, vì vậy dưới đây là một số thông tin.<br><br>
                    Đầu tiên, cô ấy là một người rất tốt bụng và thân thiện. Cô ấy hòa thuận với tất cả mọi người và luôn sẵn lòng giúp đỡ người khác. Thứ hai, trong thời gian rảnh, cô ấy thích đọc sách, nấu các món ăn truyền thống của Việt Nam và nghe nhạc. Tớ nghĩ cô ấy sẽ rất vui khi được nấu một vài bữa ăn ngon cho gia đình cậu. Cuối cùng, cô ấy hiện đang học ngành kinh doanh tại trường đại học và học tập rất chăm chỉ. Cô ấy là người có trách nhiệm và luôn giữ phòng ngủ ngăn nắp. Vì vậy, tớ tin rằng cô ấy sẽ hòa nhập rất tốt với gia đình cậu.<br><br>
                    Tớ hy vọng cậu sẽ thấy những thông tin này hữu ích. Hãy cho tớ biết nếu cậu cần thêm chi tiết nhé.<br><br>
                    <strong>Chúc cậu mọi điều tốt lành,</strong>
                </div>
                
                <div class="highlight-box" style="margin-top: 20px;">
                    <p><i class="fa-solid fa-lightbulb"></i> Số từ: 145 words. Thư mô tả thông tin người bạn chi tiết, tự nhiên, trả lời trọn vẹn cả 3 khía cạnh tính cách, sở thích và học tập.</p>
                </div>
            </div>
        """
    },
    {
        "id": "complaint",
        "icon": "fa-triangle-exclamation",
        "titleEn": "Letter of Complaint",
        "titleVi": "Thư Phàn Nàn",
        "basicInfo": """
            <div class="content-block">
                <h3>Mục đích (Purpose)</h3>
                <p>Bày tỏ sự không hài lòng về chất lượng sản phẩm, dịch vụ hoặc một tình huống bất tiện, đồng thời yêu cầu phương án giải quyết thỏa đáng.</p>
            </div>
            <div class="content-block">
                <h3>Phong cách thư (Style)</h3>
                <p>Chủ yếu là thư trang trọng (Formal) hoặc bán trang trọng (Semi-formal).</p>
            </div>
            <div class="content-block">
                <h3>Văn phong (Tone)</h3>
                <p>Lịch sự nhưng kiên quyết, rõ ràng và có căn cứ.</p>
            </div>
        """,
        "identifyingSigns": """
            <div class="content-block">
                <h3>Các từ khóa thường xuất hiện trong đề bài:</h3>
                <ul>
                    <li>complain about / express dissatisfaction with...</li>
                    <li>not satisfied with... / report a problem</li>
                    <li>poor service / bad quality</li>
                    <li>ask for a refund / replacement / solution</li>
                </ul>
            </div>
        """,
        "detailedOutline": """
            <div class="outline-note">
                <p><strong>LƯU Ý:</strong> Thư phàn nàn thường là thư bán trang trọng hoặc trang trọng.</p>
            </div>
            <div class="outline-step">
                <h4>1. Lời chào mở đầu</h4>
                <ul>
                    <li>- Trang trọng:
                        <ul>
                            <li>↳ <span class="outline-phrase">Dear Sir,</span> (nếu biết chắc chắn người nhận là nam)</li>
                            <li>↳ <span class="outline-phrase">Dear Madam,</span> (nếu biết chắc chắn người nhận là nữ)</li>
                            <li>↳ <span class="outline-phrase">Dear Sir/Madam,</span> (nếu không biết chắc chắn người nhận là nam hay nữ)</li>
                        </ul>
                    </li>
                    <li>- Bán trang trọng: ↳ <span class="outline-phrase">Dear Mr. / Ms. / Mrs. [họ của người nhận],</span></li>
                </ul>
            </div>
            <div class="outline-step">
                <h4>2. Mở thư</h4>
                <p>↳ <span class="outline-phrase">I am writing to complain about [vấn đề cần phàn nàn]. I recently used your [sản phẩm/dịch vụ] and was not satisfied with it.</span></p>
            </div>
            <div class="outline-step">
                <h4>3. Thân thư</h4>
                <div class="outline-substep">
                    <h5>Thân thư 1: Trình bày vấn đề</h5>
                    <p>↳ <span class="outline-phrase">The main problem was that [vấn đề 1].</span> → Trình bày cụ thể.<br>
                    ↳ <span class="outline-phrase">Another issue was that [vấn đề 2].</span> → Trình bày cụ thể.<br>
                    ↳ <span class="outline-phrase">Finally, I also found that [vấn đề 3].</span> → Trình bày cụ thể.</p>
                </div>
                <div class="outline-substep" style="margin-top: 14px;">
                    <h5>Thân thư 2: Cảm xúc với trải nghiệm và đề xuất giải pháp</h5>
                    <p>↳ <span class="outline-phrase">I was very disappointed / quite unhappy with these problems. Therefore, I would appreciate it if you could [giải pháp cụ thể để giải quyết vấn đề].</span></p>
                </div>
            </div>
            <div class="outline-step">
                <h4>4. Kết thư</h4>
                <p>Yêu cầu xem xét vấn đề: ↳ <span class="outline-phrase">I hope that you will look into these issues soon.</span><br>
                Mong đợi hồi âm: ↳ <span class="outline-phrase">I look forward to receiving your reply soon.</span></p>
            </div>
            <div class="outline-step">
                <h4>5. Lời chào kết thúc</h4>
                <ul>
                    <li>- Trang trọng: ↳ <span class="outline-phrase">Yours faithfully,</span></li>
                    <li>- Bán trang trọng: ↳ <span class="outline-phrase">Yours sincerely,</span></li>
                </ul>
            </div>
        """,
        "practicePrompt": "You are a member of a local sports center. You have recently used the changing room and were not satisfied with its condition. Write an email to the manager of the sports center. In your email, you should: Describe the problems you found in the changing room, Explain how the situation made you feel, Suggest what should be done to improve the facility. You should write at least 120 words. Do not include your name or address.",
        "sampleWriting": """
            <!-- Prompt Card -->
            <div class="sample-prompt-container">
                <div class="sample-prompt-header">
                    <i class="fa-solid fa-file-circle-question"></i> ĐỀ BÀI (TOPIC PROMPT)
                </div>
                <div class="sample-prompt-text">
                    <p>You are a member of a local sports center. You have recently used the changing room and were not satisfied with its condition. Write an email to the manager of the sports center. In your email, you should:</p>
                    <ul>
                        <li>Describe the problems you found in the changing room</li>
                        <li>Explain how the situation made you feel</li>
                        <li>Suggest what should be done to improve the facility</li>
                    </ul>
                    <p style="margin-top: 8px; font-style: italic; color: var(--text-muted);">You should write at least 120 words. Do not include your name or address.</p>
                </div>
                <div class="sample-analysis-grid">
                    <div class="sample-analysis-item">
                        <strong>Người nhận</strong>
                        <span>Quản lý trung tâm thể thao (The manager)</span>
                    </div>
                    <div class="sample-analysis-item">
                        <strong>Mục đích</strong>
                        <span>Phàn nàn về phòng thay đồ và đề xuất giải pháp cải thiện</span>
                    </div>
                    <div class="sample-analysis-item">
                        <strong>Văn phong</strong>
                        <span>Trang trọng (Formal Letter)</span>
                    </div>
                    <div class="sample-analysis-item">
                        <strong>Yêu cầu cốt lõi</strong>
                        <span>Mô tả các vấn đề, bày tỏ cảm xúc, đề xuất giải pháp</span>
                    </div>
                </div>
            </div>

            <div class="content-block">
                <h3>BÀI VIẾT MẪU (SAMPLE LETTER - B1 LEVEL)</h3>
                <div class="sample-letter-box">
                    <strong>Dear Sir/Madam,</strong><br><br>
                    I am writing to complain about the condition of the changing room at your sports center. I recently used the facility and was not satisfied with it.<br><br>
                    The main problem was that the floor was very dirty and wet, which was quite dangerous for members. Another issue was that several lockers were broken, so I could not safely store my personal belongings. Finally, I also found that some of the showers did not have hot water. I was very disappointed with these problems because I have always enjoyed using your center. Therefore, I would appreciate it if you could clean the changing room more regularly, repair the broken lockers, and fix the showers as soon as possible.<br><br>
                    I hope that you will look into these issues soon. I look forward to receiving your reply soon.<br><br>
                    <strong>Yours faithfully,</strong>
                </div>
                
                <h3 style="margin-top: 25px;">BẢN DỊCH CHI TIẾT</h3>
                <div class="translation-box" style="background-color: var(--bg-main); border: 1px solid var(--border-color); padding: 20px; border-radius: 12px; margin-top: 15px; font-family: var(--font-body); line-height: 1.8; color: var(--text-muted); font-style: italic;">
                    <strong>Kính gửi Ông/Bà,</strong><br><br>
                    Tôi viết thư này để phàn nàn về tình trạng của phòng thay đồ tại trung tâm thể thao của ông/bà. Gần đây tôi đã sử dụng cơ sở vật chất này và không hài lòng với nó.<br><br>
                    Vấn đề chính là sàn nhà rất bẩn và ẩm ướt, điều này khá nguy hiểm cho các hội viên. Một vấn đề khác là một số tủ đựng đồ bị hỏng, vì vậy tôi không thể cất giữ đồ dùng cá nhân của mình một cách an toàn. Cuối cùng, tôi cũng nhận thấy một số vòi hoa sen không có nước nóng. Tôi rất thất vọng với những vấn đề này vì tôi luôn thích sử dụng trung tâm của ông/bà. Do đó, tôi sẽ rất cảm kích nếu ông/bà có thể dọn dẹp phòng thay đồ thường xuyên hơn, sửa chữa các tủ đựng đồ bị hỏng và sửa lại các vòi hoa sen càng sớm càng tốt.<br><br>
                    Tôi hy vọng ông/bà sẽ sớm xem xét các vấn đề này. Tôi rất mong sớm nhận được phản hồi từ ông/bà.<br><br>
                    <strong>Trân trọng,</strong>
                </div>
                
                <div class="highlight-box" style="margin-top: 20px;">
                    <p><i class="fa-solid fa-lightbulb"></i> Số từ: 150 words. Thư phàn nàn chuẩn mực, phân tách 3 lỗi cụ thể và đưa ra 3 giải pháp tương ứng rất thuyết phục.</p>
                </div>
            </div>
        """
    },
    {
        "id": "feedback",
        "icon": "fa-comment-dots",
        "titleEn": "Letter of Feedback",
        "titleVi": "Thư Phản Hồi, Đánh Giá",
        "basicInfo": """
            <div class="content-block">
                <h3>Mục đích (Purpose)</h3>
                <p>Đưa ra đánh giá, nhận xét (cả điểm hài lòng và điểm chưa hài lòng) về một dịch vụ, sự kiện hoặc sản phẩm đã trải nghiệm, đồng thời đóng góp ý kiến cải thiện.</p>
            </div>
            <div class="content-block">
                <h3>Phong cách thư (Style)</h3>
                <p>Thường là thư bán trang trọng hoặc trang trọng.</p>
            </div>
            <div class="content-block">
                <h3>Văn phong (Tone)</h3>
                <p>Khách quan, xây dựng, mang tính đóng góp tích cực.</p>
            </div>
        """,
        "identifyingSigns": """
            <div class="content-block">
                <h3>Các từ khóa thường xuất hiện trong đề bài:</h3>
                <ul>
                    <li>give feedback on / share your opinion about...</li>
                    <li>write a letter to comment on...</li>
                    <li>say what you liked or did not like about...</li>
                    <li>say what you are satisfied or dissatisfied with...</li>
                </ul>
            </div>
        """,
        "detailedOutline": """
            <div class="outline-note">
                <p><strong>LƯU Ý:</strong> Thư cho phản hồi đánh giá thường là thư bán trang trọng hoặc trang trọng.</p>
            </div>
            <div class="outline-step">
                <h4>1. Lời chào mở đầu</h4>
                <ul>
                    <li>- Trang trọng:
                        <ul>
                            <li>↳ <span class="outline-phrase">Dear Sir,</span> (nếu biết chắc chắn người nhận là nam)</li>
                            <li>↳ <span class="outline-phrase">Dear Madam,</span> (nếu biết chắc chắn người nhận là nữ)</li>
                            <li>↳ <span class="outline-phrase">Dear Sir/Madam,</span> (nếu không biết chắc chắn người nhận là nam hay nữ)</li>
                        </ul>
                    </li>
                    <li>- Bán trang trọng: ↳ <span class="outline-phrase">Dear Mr. / Ms. / Mrs. [họ của người nhận],</span></li>
                </ul>
            </div>
            <div class="outline-step">
                <h4>2. Mở thư</h4>
                <p>↳ <span class="outline-phrase">I am writing to give you feedback on [vấn đề cần phản hồi đánh giá]. I recently used your [sản phẩm/dịch vụ] and would like to share my experience.</span></p>
            </div>
            <div class="outline-step">
                <h4>3. Thân thư</h4>
                <p>Lần lượt đưa ra phản hồi đánh giá (khen/chê) và sau đó đề xuất giải pháp để cải thiện.</p>
                <div class="outline-structures">
                    <h5>CÁC CẤU TRÚC ĐÁNH GIÁ TÍCH CỰC [KHEN]:</h5>
                    <p>↳ <span class="outline-phrase">First of all, I would like to mention some positive points about your [sản phẩm/dịch vụ].</span></p>
                    <ul>
                        <li>↳ <span class="outline-phrase">I was very satisfied with [điểm khen] because [lý do].</span></li>
                        <li>↳ <span class="outline-phrase">I really liked [điểm khen] because [lý do].</span></li>
                        <li>↳ <span class="outline-phrase">I was impressed with [điểm khen] as [lý do].</span></li>
                        <li>↳ <span class="outline-phrase">One thing I liked most was [điểm khen] since [lý do].</span></li>
                    </ul>
                    <h5>CÁC CẤU TRÚC PHẢN ÁNH ĐIỂM CHƯA HÀI LÒNG [CHÊ]:</h5>
                    <p>↳ <span class="outline-phrase">However, there were also some areas that needed improvement.</span></p>
                    <ul>
                        <li>↳ <span class="outline-phrase">I was disappointed with [điểm chê] because [lý do].</span></li>
                        <li>↳ <span class="outline-phrase">One thing that disappointed me was [điểm chê] since [lý do].</span></li>
                        <li>↳ <span class="outline-phrase">I was not satisfied with [điểm chê] as [lý do].</span></li>
                        <li>↳ <span class="outline-phrase">The quality of [điểm chê] was not as good as I expected because [lý do].</span></li>
                    </ul>
                    <h5>CÁC CẤU TRÚC ĐỀ XUẤT GIẢI PHÁP:</h5>
                    <p>↳ <span class="outline-phrase">To enhance the quality of your [sản phẩm/dịch vụ], I have a few suggestions.</span></p>
                    <ul>
                        <li>↳ <span class="outline-phrase">I suggest that you should [hành động – Vo].</span></li>
                        <li>↳ <span class="outline-phrase">I think you should [hành động – Vo].</span></li>
                        <li>↳ <span class="outline-phrase">It would be better if you could [hành động – Vo].</span></li>
                        <li>↳ <span class="outline-phrase">I hope you will consider [hành động – Ving].</span></li>
                    </ul>
                </div>
            </div>
            <div class="outline-step">
                <h4>4. Kết thư</h4>
                <p>↳ <span class="outline-phrase">I hope my feedback will help you improve your [sản phẩm/dịch vụ]. Please feel free to contact me if you have any further questions.</span></p>
            </div>
            <div class="outline-step">
                <h4>5. Lời chào kết thúc</h4>
                <ul>
                    <li>- Trang trọng: ↳ <span class="outline-phrase">Yours faithfully,</span></li>
                    <li>- Bán trang trọng: ↳ <span class="outline-phrase">Yours sincerely,</span></li>
                </ul>
            </div>
        """,
        "practicePrompt": "You recently stayed at a hotel and received an email from the hotel manager asking for feedback about your stay. Write an email to give your opinion. In your email, you should: Say whether you were satisfied or dissatisfied with the service, Describe your experience, Suggest ways the hotel can improve its service. You should write at least 120 words. Do not include your name or address.",
        "sampleWriting": """
            <!-- Prompt Card -->
            <div class="sample-prompt-container">
                <div class="sample-prompt-header">
                    <i class="fa-solid fa-file-circle-question"></i> ĐỀ BÀI (TOPIC PROMPT)
                </div>
                <div class="sample-prompt-text">
                    <p>You recently stayed at a hotel and received an email from the hotel manager asking for feedback about your stay. Write an email to give your opinion. In your email, you should:</p>
                    <ul>
                        <li>Say whether you were satisfied or dissatisfied with the service</li>
                        <li>Describe your experience</li>
                        <li>Suggest ways the hotel can improve its service</li>
                    </ul>
                    <p style="margin-top: 8px; font-style: italic; color: var(--text-muted);">You should write at least 120 words. Do not include your name or address.</p>
                </div>
                <div class="sample-analysis-grid">
                    <div class="sample-analysis-item">
                        <strong>Người nhận</strong>
                        <span>Quản lý khách sạn (Hotel manager)</span>
                    </div>
                    <div class="sample-analysis-item">
                        <strong>Mục đích</strong>
                        <span>Đưa ra phản hồi đánh giá về kỳ nghỉ và đề xuất cải thiện dịch vụ</span>
                    </div>
                    <div class="sample-analysis-item">
                        <strong>Văn phong</strong>
                        <span>Trang trọng / Bán trang trọng (Formal / Semi-formal)</span>
                    </div>
                    <div class="sample-analysis-item">
                        <strong>Yêu cầu cốt lõi</strong>
                        <span>Mức độ hài lòng, mô tả trải nghiệm (khen/chê), đề xuất giải pháp</span>
                    </div>
                </div>
            </div>

            <div class="content-block">
                <h3>BÀI VIẾT MẪU (SAMPLE LETTER - B1 LEVEL)</h3>
                <div class="sample-letter-box">
                    <strong>Dear Sir/Madam,</strong><br><br>
                    I am writing to give you feedback on my recent stay at your hotel. I recently used your services and would like to share my experience.<br><br>
                    First of all, I would like to mention some positive points about your hotel. I was very satisfied with the customer service because the staff were polite, friendly, and always ready to assist guests. In addition, the room was spacious and clean. However, there were also some areas that needed improvement. I was disappointed with the Wi-Fi connection because it was slow and unstable. Furthermore, the breakfast menu was quite limited and lacked variety. To enhance the quality of your services, I suggest that you should upgrade the Internet system and offer more options for breakfast.<br><br>
                    I hope my feedback will help you improve your service. Please feel free to contact me if you have any further questions.<br><br>
                    <strong>Yours faithfully,</strong>
                </div>
                
                <h3 style="margin-top: 25px;">BẢN DỊCH CHI TIẾT</h3>
                <div class="translation-box" style="background-color: var(--bg-main); border: 1px solid var(--border-color); padding: 20px; border-radius: 12px; margin-top: 15px; font-family: var(--font-body); line-height: 1.8; color: var(--text-muted); font-style: italic;">
                    <strong>Kính gửi Ông/Bà,</strong><br><br>
                    Tôi viết thư này để đưa ra phản hồi về kỳ nghỉ gần đây của tôi tại khách sạn của ông/bà. Gần đây tôi đã sử dụng dịch vụ của ông/bà và muốn chia sẻ trải nghiệm của mình.<br><br>
                    Trước hết, tôi muốn đề cập đến một số điểm tích cực về khách sạn của ông/bà. Tôi rất hài lòng với dịch vụ chăm sóc khách hàng vì nhân viên rất lịch sự, thân thiện và luôn sẵn sàng hỗ trợ khách. Ngoài ra, phòng ốc rất rộng rãi và sạch sẽ. Tuy nhiên, cũng có một số khía cạnh cần được cải thiện. Tôi đã thất vọng với kết nối Wi-Fi vì nó chậm và không ổn định. Hơn nữa, thực đơn bữa sáng khá hạn chế và thiếu sự đa dạng. Để nâng cao chất lượng dịch vụ của ông/bà, tôi đề nghị ông/bà nên nâng cấp hệ thống Internet và cung cấp nhiều sự lựa chọn hơn cho bữa sáng.<br><br>
                    Tôi hy vọng phản hồi của tôi sẽ giúp ông/bà cải thiện dịch vụ của mình. Xin vui lòng liên hệ với tôi nếu ông/bà có bất kỳ câu hỏi nào thêm.<br><br>
                    <strong>Trân trọng,</strong>
                </div>
                
                <div class="highlight-box" style="margin-top: 20px;">
                    <p><i class="fa-solid fa-lightbulb"></i> Số từ: 158 words. Thư phản hồi cân bằng giữa khen ngợi và góp ý mang tính xây dựng, bố cục logic và từ vựng chuẩn B1.</p>
                </div>
            </div>
        """
    },
    {
        "id": "apology",
        "icon": "fa-handshake-angle",
        "titleEn": "Letter of Apology",
        "titleVi": "Thư Xin Lỗi",
        "basicInfo": """
            <div class="content-block">
                <h3>Mục đích (Purpose)</h3>
                <p>Gửi lời xin lỗi chân thành về một sai sót, sự cố hoặc việc không thể thực hiện một cam kết, giải thích lý do và đưa ra giải pháp khắc phục/đền bù.</p>
            </div>
            <div class="content-block">
                <h3>Phong cách thư (Style)</h3>
                <p>Có thể là thư thân mật, bán trang trọng hoặc trang trọng tùy thuộc vào đối tượng người nhận.</p>
            </div>
            <div class="content-block">
                <h3>Văn phong (Tone)</h3>
                <p>Chân thành, biết lỗi, tôn trọng và thể hiện thiện chí sửa chữa.</p>
            </div>
        """,
        "identifyingSigns": """
            <div class="content-block">
                <h3>Các từ khóa thường xuất hiện trong đề bài:</h3>
                <ul>
                    <li>apologize for / say sorry for...</li>
                    <li>explain why you (missed, were late, forgot, damaged...)</li>
                    <li>say how you will make up for it</li>
                    <li>explain the situation and offer a solution</li>
                </ul>
            </div>
        """,
        "detailedOutline": """
            <div class="outline-note">
                <p><strong>LƯU Ý:</strong> Thư xin lỗi có thể là thư thân mật, bán trang trọng hoặc trang trọng.</p>
            </div>
            <div class="outline-step">
                <h4>1. Lời chào mở đầu</h4>
                <ul>
                    <li>- Thân mật: ↳ <span class="outline-phrase">Dear [tên của người nhận],</span></li>
                    <li>- Trang trọng:
                        <ul>
                            <li>↳ <span class="outline-phrase">Dear Sir,</span> (nếu biết chắc chắn người nhận là nam)</li>
                            <li>↳ <span class="outline-phrase">Dear Madam,</span> (nếu biết chắc chắn người nhận là nữ)</li>
                            <li>↳ <span class="outline-phrase">Dear Sir/Madam,</span> (nếu không biết chắc chắn người nhận là nam hay nữ)</li>
                        </ul>
                    </li>
                    <li>- Bán trang trọng: ↳ <span class="outline-phrase">Dear Mr. / Ms. / Mrs. [họ của người nhận],</span></li>
                </ul>
            </div>
            <div class="outline-step">
                <h4>2. Mở thư</h4>
                <ul>
                    <li>- Thân mật: ↳ <span class="outline-phrase">I’m really sorry for [vấn đề cần xin lỗi]. Let me explain what happened so you can understand the situation.</span></li>
                    <li>- Trang trọng & Bán trang trọng: ↳ <span class="outline-phrase">I am writing to apologize for [vấn đề cần xin lỗi]. I understand that this may have caused some inconvenience, and I would like to explain the situation.</span></li>
                </ul>
            </div>
            <div class="outline-step">
                <h4>3. Thân thư</h4>
                <p>Lần lượt giải thích lý do và nêu hành động bù đắp phù hợp.</p>
                <div class="outline-structures">
                    <h5>CẤU TRÚC GIẢI THÍCH LÝ DO:</h5>
                    <p><strong>- Thân mật:</strong> ↳ <span class="outline-phrase">First of all, let me explain why this happened.</span></p>
                    <ul>
                        <li>↳ <span class="outline-phrase">I’m really sorry that I couldn’t [hành động – Vo] because [lý do].</span></li>
                        <li>↳ <span class="outline-phrase">I missed [sự kiện] because [lý do].</span></li>
                        <li>↳ <span class="outline-phrase">I felt bad about not [hành động – Ving] because [lý do].</span></li>
                        <li>↳ <span class="outline-phrase">I didn’t mean to [hành động – Vo], but [lý do].</span></li>
                    </ul>
                    <p><strong>- Trang trọng & Bán trang trọng:</strong> ↳ <span class="outline-phrase">First of all, I would like to explain why this happened.</span></p>
                    <ul>
                        <li>↳ <span class="outline-phrase">I was unable to [hành động – Vo] because [lý do].</span></li>
                        <li>↳ <span class="outline-phrase">I regret that I was unable to [hành động – Vo] because [lý do].</span></li>
                        <li>↳ <span class="outline-phrase">Because [lý do], I was unable to [hành động – Vo].</span></li>
                        <li>↳ <span class="outline-phrase">Unfortunately, I could not [hành động – Vo] because [lý do].</span></li>
                    </ul>
                    <p style="margin-top: 10px; font-style: italic; color: var(--text-muted);">LƯU Ý: Sau khi nêu lý do, nên thêm 1-3 câu mô tả cụ thể tình huống để người đọc hiểu rõ hơn. Sử dụng thì QUÁ KHỨ ĐƠN để mô tả những sự việc đã xảy ra.</p>
                    <h5 style="margin-top: 14px;">CẤU TRÚC NÊU HÀNH ĐỘNG BÙ ĐẮP:</h5>
                    <ul>
                        <li>- Thân mật: ↳ <span class="outline-phrase">Finally, let me make it up to you by [hành động – Ving].</span></li>
                        <li>- Trang trọng & Bán trang trọng: ↳ <span class="outline-phrase">To make up for my mistake, I would like to [hành động – Vo].</span></li>
                    </ul>
                </div>
            </div>
            <div class="outline-step">
                <h4>4. Kết thư</h4>
                <ul>
                    <li>- Thân mật: ↳ <span class="outline-phrase">Sorry once again. Thanks for taking the time to read this. Write back soon.</span></li>
                    <li>- Trang trọng & Bán trang trọng: ↳ <span class="outline-phrase">I would like to apologize once again for the inconvenience. Thank you for taking the time to read my letter. I look forward to receiving your reply soon.</span></li>
                </ul>
            </div>
            <div class="outline-step">
                <h4>5. Lời chào kết thúc</h4>
                <ul>
                    <li>- Thân mật: ↳ <span class="outline-phrase">Best wishes,</span></li>
                    <li>- Trang trọng: ↳ <span class="outline-phrase">Yours faithfully,</span></li>
                    <li>- Bán trang trọng: ↳ <span class="outline-phrase">Yours sincerely,</span></li>
                </ul>
            </div>
        """,
        "practicePrompt": "You borrowed a book from your friend Helen, but forgot to return it. Read part of her letter below: … Hey! How have you been lately? By the way, have you finished reading the book you borrowed from me? I was wondering why you haven’t returned it yet. When do you plan to give it back, and how will you return it? … Write a letter to reply to Helen. In your letter, you should: apologize for not returning the book, explain your current situation and whether you’ve finished the book, say when and how you will return it. You should write at least 120 words. Do not include your name or address.",
        "sampleWriting": """
            <!-- Prompt Card -->
            <div class="sample-prompt-container">
                <div class="sample-prompt-header">
                    <i class="fa-solid fa-file-circle-question"></i> ĐỀ BÀI (TOPIC PROMPT)
                </div>
                <div class="sample-prompt-text">
                    <p>You borrowed a book from your friend Helen, but forgot to return it. Read part of her letter below:</p>
                    <p style="margin: 10px 0; padding: 10px 14px; background: rgba(0,0,0,0.03); border-left: 3px solid var(--accent-red); font-style: italic;">
                        "… Hey! How have you been lately? By the way, have you finished reading the book you borrowed from me? I was wondering why you haven’t returned it yet. When do you plan to give it back, and how will you return it? …"
                    </p>
                    <p>Write a letter to reply to Helen. In your letter, you should:</p>
                    <ul>
                        <li>apologize for not returning the book</li>
                        <li>explain your current situation and whether you’ve finished the book</li>
                        <li>say when and how you will return it</li>
                    </ul>
                    <p style="margin-top: 8px; font-style: italic; color: var(--text-muted);">You should write at least 120 words. Do not include your name or address.</p>
                </div>
                <div class="sample-analysis-grid">
                    <div class="sample-analysis-item">
                        <strong>Người nhận</strong>
                        <span>Helen (Bạn bè thân thiết)</span>
                    </div>
                    <div class="sample-analysis-item">
                        <strong>Mục đích</strong>
                        <span>Xin lỗi vì quên trả sách, giải thích lý do, hẹn ngày trả và đền bù</span>
                    </div>
                    <div class="sample-analysis-item">
                        <strong>Văn phong</strong>
                        <span>Thân mật (Informal Letter)</span>
                    </div>
                    <div class="sample-analysis-item">
                        <strong>Yêu cầu cốt lõi</strong>
                        <span>Xin lỗi, giải thích lý do/tình trạng đọc xong, thời gian & cách thức trả sách</span>
                    </div>
                </div>
            </div>

            <div class="content-block">
                <h3>BÀI VIẾT MẪU (SAMPLE LETTER - B1 LEVEL)</h3>
                <div class="sample-letter-box">
                    <strong>Dear Helen,</strong><br><br>
                    I’m really sorry for not returning your book earlier. Let me explain what happened so you can understand the situation.<br><br>
                    First of all, let me explain why this happened. I’m really sorry that I couldn’t return the book on time because I have been extremely busy preparing for my final exams. During that time, I had several assignments and an important test. As a result, I completely forgot about the book. In addition, I have finished reading the whole book and found it very interesting and helpful. Next, I plan to give it back to you this Saturday. I can come over to your house in the afternoon to return it in person. Finally, let me make it up to you by treating you to a cup of milk tea and some snacks.<br><br>
                    Sorry once again. Thanks for taking the time to read this. Write back soon.<br><br>
                    <strong>Best wishes,</strong>
                </div>
                
                <h3 style="margin-top: 25px;">BẢN DỊCH CHI TIẾT</h3>
                <div class="translation-box" style="background-color: var(--bg-main); border: 1px solid var(--border-color); padding: 20px; border-radius: 12px; margin-top: 15px; font-family: var(--font-body); line-height: 1.8; color: var(--text-muted); font-style: italic;">
                    <strong>Helen thân mến,</strong><br><br>
                    Tớ thực sự xin lỗi vì đã không trả sách cho cậu sớm hơn. Hãy để tớ giải thích những gì đã xảy ra để cậu hiểu rõ tình hình nhé.<br><br>
                    Trước hết, hãy để tớ giải thích tại sao chuyện này lại xảy ra. Tớ thực sự xin lỗi vì tớ đã không thể trả sách đúng hạn vì tớ quá bận rộn chuẩn bị cho kỳ thi cuối kỳ. Trong thời gian đó, tớ có vài bài tập lớn và một bài kiểm tra quan trọng. Kết quả là tớ hoàn toàn quên mất cuốn sách. Ngoài ra, tớ đã đọc xong toàn bộ cuốn sách và thấy nó rất thú vị và bổ ích. Tiếp theo, tớ dự định sẽ trả lại sách cho cậu vào thứ Bảy tuần này. Tớ có thể ghé qua nhà cậu vào buổi chiều để trực tiếp gửi lại sách. Cuối cùng, hãy để tớ bù đắp cho cậu bằng một chầu trà sữa và đồ ăn vặt nhé.<br><br>
                    Xin lỗi cậu một lần nữa nhé. Cảm ơn cậu vì đã dành thời gian đọc thư này. Hãy viết thư lại cho tớ sớm nhé.<br><br>
                    <strong>Chúc cậu mọi điều tốt lành,</strong>
                </div>
                
                <div class="highlight-box" style="margin-top: 20px;">
                    <p><i class="fa-solid fa-lightbulb"></i> Số từ: 160 words. Thư xin lỗi bạn bè tự nhiên, giải thích thuyết phục, nêu rõ thời gian/cách trả và hành động đền bù đáng yêu.</p>
                </div>
            </div>
        """
    },
    {
        "id": "application",
        "icon": "fa-briefcase",
        "titleEn": "Letter of Application",
        "titleVi": "Thư Ứng Tuyển",
        "basicInfo": """
            <div class="content-block">
                <h3>Mục đích (Purpose)</h3>
                <p>Ứng tuyển vào một vị trí công việc, khóa học, chương trình học bổng hoặc tình nguyện viên, nêu bật trình độ, kinh nghiệm và sự phù hợp của bản thân.</p>
            </div>
            <div class="content-block">
                <h3>Phong cách thư (Style)</h3>
                <p>Luôn là thư trang trọng (Formal Letter).</p>
            </div>
            <div class="content-block">
                <h3>Văn phong (Tone)</h3>
                <p>Chuyên nghiệp, tự tin, lịch thiệp và tôn trọng.</p>
            </div>
        """,
        "identifyingSigns": """
            <div class="content-block">
                <h3>Các từ khóa thường xuất hiện trong đề bài:</h3>
                <ul>
                    <li>apply for the position / the job of...</li>
                    <li>write a letter of application</li>
                    <li>respond to a job advertisement</li>
                    <li>apply for a part-time / full-time job</li>
                </ul>
            </div>
        """,
        "detailedOutline": """
            <div class="outline-note">
                <p><strong>LƯU Ý:</strong> Thư ứng tuyển thường gặp nhất là thư xin việc và luôn là thư trang trọng.</p>
            </div>
            <div class="outline-step">
                <h4>1. Lời chào mở đầu</h4>
                <p>- Trang trọng:
                    <ul>
                        <li>↳ <span class="outline-phrase">Dear Sir,</span> (nếu biết chắc chắn người nhận là nam)</li>
                        <li>↳ <span class="outline-phrase">Dear Madam,</span> (nếu biết chắc chắn người nhận là nữ)</li>
                        <li>↳ <span class="outline-phrase">Dear Sir/Madam,</span> (nếu không biết chắc chắn người nhận là nam hay nữ)</li>
                    </ul>
                </p>
            </div>
            <div class="outline-step">
                <h4>2. Mở thư</h4>
                <p>- Trang trọng: ↳ <span class="outline-phrase">I am writing to apply for the position of [vị trí công việc] which was advertised on/in [nguồn tuyển dụng].</span></p>
            </div>
            <div class="outline-step">
                <h4>3. Thân thư</h4>
                <p>Lần lượt trình bày lý do có hứng thú với vị trí công việc này, đề cập trình độ học vấn và năng lực chuyên môn, kinh nghiệm làm việc đã có, sau đó nêu lý do mình là ứng cử viên phù hợp cho vị trí này.</p>
                <div class="outline-structures">
                    <h5>LÝ DO CÓ HỨNG THÚ VỚI VỊ TRÍ CÔNG VIỆC NÀY:</h5>
                    <p>↳ <span class="outline-phrase">I am very interested in this position because it matches my interests and career goals. In addition, I enjoy [hoạt động liên quan đến công việc]. Therefore, I believe this job will give me a good opportunity to apply what I have learned during my studies and gain practical experience.</span></p>
                    
                    <h5>TRÌNH ĐỘ HỌC VẤN VÀ NĂNG LỰC CHUYÊN MÔN:</h5>
                    <p>↳ <span class="outline-phrase">I recently graduated from [tên trường] with a bachelor’s degree in [chuyên ngành]. During my studies, I developed a strong understanding of [lĩnh vực]. I also gained useful knowledge and abilities such as [kiến thức/năng lực học thuật 1] and [kiến thức/năng lực học thuật 2].</span></p>
                    
                    <h5>KINH NGHIỆM LÀM VIỆC ĐÃ CÓ:</h5>
                    <p>↳ <span class="outline-phrase">I worked part-time as a [vị trí công việc] at [nơi làm việc]. In this job, I was responsible for [nhiệm vụ]. This experience helped me develop skills such as [kỹ năng mềm 1] and [kỹ năng mềm 2].</span></p>
                    
                    <h5>KHẲNG ĐỊNH LÀ ỨNG CỬ VIÊN PHÙ HỢP:</h5>
                    <p>↳ <span class="outline-phrase">I believe I would be a suitable candidate for this position. This is because I am [đặc điểm tính cách]. Moreover, I am eager to learn and can adapt quickly to new environments.</span></p>
                </div>
            </div>
            <div class="outline-step">
                <h4>4. Kết thư</h4>
                <p>- Trang trọng: ↳ <span class="outline-phrase">I would be grateful if you could consider my application. I look forward to receiving your reply soon.</span></p>
            </div>
            <div class="outline-step">
                <h4>5. Lời chào kết thúc</h4>
                <p>- Trang trọng: ↳ <span class="outline-phrase">Yours faithfully,</span></p>
            </div>
        """,
        "practicePrompt": "You saw a job advertisement for a sales assistant at a clothing store in your city. Write an email to apply for the job. In your email, you should: Introduce yourself and your current situation, Say why you are interested in the position, Mention any experience you have working with customers. You should write at least 120 words. Do not include your name or address.",
        "sampleWriting": """
            <!-- Prompt Card -->
            <div class="sample-prompt-container">
                <div class="sample-prompt-header">
                    <i class="fa-solid fa-file-circle-question"></i> ĐỀ BÀI (TOPIC PROMPT)
                </div>
                <div class="sample-prompt-text">
                    <p>You saw a job advertisement for a sales assistant at a clothing store in your city. Write an email to apply for the job. In your email, you should:</p>
                    <ul>
                        <li>Introduce yourself and your current situation</li>
                        <li>Say why you are interested in the position</li>
                        <li>Mention any experience you have working with customers</li>
                    </ul>
                    <p style="margin-top: 8px; font-style: italic; color: var(--text-muted);">You should write at least 120 words. Do not include your name or address.</p>
                </div>
                <div class="sample-analysis-grid">
                    <div class="sample-analysis-item">
                        <strong>Người nhận</strong>
                        <span>Nhà tuyển dụng / Quản lý (Dear Sir/Madam)</span>
                    </div>
                    <div class="sample-analysis-item">
                        <strong>Mục đích</strong>
                        <span>Ứng tuyển vào vị trí nhân viên bán hàng (Sales Assistant)</span>
                    </div>
                    <div class="sample-analysis-item">
                        <strong>Văn phong</strong>
                        <span>Trang trọng (Formal Letter)</span>
                    </div>
                    <div class="sample-analysis-item">
                        <strong>Yêu cầu cốt lõi</strong>
                        <span>Giới thiệu bản thân & học vấn, lý do hứng thú, kinh nghiệm với khách hàng</span>
                    </div>
                </div>
            </div>

            <div class="content-block">
                <h3>BÀI VIẾT MẪU (SAMPLE LETTER - B1 LEVEL)</h3>
                <div class="sample-letter-box">
                    <strong>Dear Sir/Madam,</strong><br><br>
                    I am writing to apply for the position of sales assistant which was advertised on your website.<br><br>
                    I recently graduated from Can Tho University with a bachelor’s degree in Business Administration. During my studies, I developed a strong understanding of marketing and customer service. I also gained useful knowledge and abilities such as communication and team collaboration.<br><br>
                    I am very interested in this position because it matches my interests and career goals. In addition, I enjoy helping customers choose suitable fashion products. Therefore, I believe this job will give me a good opportunity to apply what I have learned during my studies and gain practical experience.<br><br>
                    I worked part-time as a sales assistant at a local clothing store. In this job, I was responsible for welcoming customers and arranging products. This experience helped me develop problem-solving skills and customer care skills.<br><br>
                    I believe I would be a suitable candidate for this position. This is because I am enthusiastic, honest, and hardworking. Moreover, I am eager to learn and can adapt quickly to new environments.<br><br>
                    I would be grateful if you could consider my application. I look forward to receiving your reply soon.<br><br>
                    <strong>Yours faithfully,</strong>
                </div>
                
                <h3 style="margin-top: 25px;">BẢN DỊCH CHI TIẾT</h3>
                <div class="translation-box" style="background-color: var(--bg-main); border: 1px solid var(--border-color); padding: 20px; border-radius: 12px; margin-top: 15px; font-family: var(--font-body); line-height: 1.8; color: var(--text-muted); font-style: italic;">
                    <strong>Kính gửi Ông/Bà,</strong><br><br>
                    Tôi viết thư này để ứng tuyển vào vị trí nhân viên bán hàng được quảng cáo trên trang web của ông/bà.<br><br>
                    Tôi vừa tốt nghiệp Đại học Cần Thơ với tấm bằng cử nhân ngành Quản trị Kinh doanh. Trong quá trình học, tôi đã phát triển sự hiểu biết sâu sắc về marketing và dịch vụ khách hàng. Tôi cũng tích lũy được những kiến thức và năng lực hữu ích như giao tiếp và làm việc nhóm.<br><br>
                    Tôi rất hứng thú với vị trí này vì nó phù hợp với sở thích và mục tiêu nghề nghiệp của tôi. Ngoài ra, tôi thích giúp đỡ khách hàng lựa chọn những sản phẩm thời trang phù hợp. Vì vậy, tôi tin rằng công việc này sẽ mang lại cho tôi cơ hội tốt để áp dụng những gì đã học trong quá trình học và tích lũy thêm kinh nghiệm thực tế.<br><br>
                    Tôi đã từng làm việc bán thời gian với tư cách là nhân viên bán hàng tại một cửa hàng quần áo địa phương. Trong công việc này, tôi chịu trách nhiệm đón tiếp khách hàng và sắp xếp sản phẩm. Kinh nghiệm này đã giúp tôi phát triển kỹ năng giải quyết vấn đề và kỹ năng chăm sóc khách hàng.<br><br>
                    Tôi tin rằng mình sẽ là ứng cử viên phù hợp cho vị trí này. Điều này là vì tôi là người nhiệt tình, trung thực và làm việc chăm chỉ. Hơn nữa, tôi rất ham học hỏi và có thể thích nghi nhanh chóng với môi trường mới.<br><br>
                    Tôi sẽ rất biết ơn nếu ông/bà có thể xem xét hồ sơ ứng tuyển của tôi. Tôi rất mong sớm nhận được phản hồi từ ông/bà.<br><br>
                    <strong>Trân trọng,</strong>
                </div>
                
                <div class="highlight-box" style="margin-top: 20px;">
                    <p><i class="fa-solid fa-lightbulb"></i> Số từ: 195 words. Thư xin việc chuyên nghiệp, bám sát cấu trúc dàn ý chuẩn B1, nêu bật trình độ học vấn, kinh nghiệm và phẩm chất nổi bật.</p>
                </div>
            </div>
        """
    }
]
'''

# Let's read the dom_and_logic_code from reconstruct_app.py
with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "r", encoding="utf-8") as f:
    orig = f.read()

dom_and_logic = orig[orig.find("dom_and_logic_code ="):]

full_code = code + "\n" + dom_and_logic

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "w", encoding="utf-8") as f:
    f.write(full_code)

print("Updated reconstruct_app.py successfully!")
'''

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/update_reconstruct.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Saved update_reconstruct.py")
