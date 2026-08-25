const letterTypes = [
    {
        "id": "advice",
        "icon": "fa-lightbulb",
        "titleEn": "Letter of Advice",
        "titleVi": "Thư Cho Lời Khuyên",
        "basicInfo": "\n            <div class=\"content-block\">\n                <h3>Mục đích (Purpose)</h3>\n                <p>Đưa ra lời khuyên, gợi ý hoặc đề xuất để giúp người nhận giải quyết một vấn đề hoặc đưa ra quyết định phù hợp trong một tình huống cụ thể.</p>\n            </div>\n            <div class=\"content-block\">\n                <h3>Phong cách thư (Style)</h3>\n                <p>Chủ yếu là thư thân mật (Informal Letter).</p>\n            </div>\n            <div class=\"content-block\">\n                <h3>Văn phong (Tone)</h3>\n                <p>Thân thiện, quan tâm, hỗ trợ và khích lệ.</p>\n            </div>\n        ",
        "identifyingSigns": "\n            <div class=\"content-block\">\n                <h3>Các từ khóa thường xuất hiện trong đề bài:</h3>\n                <ul>\n                    <li>advice / give me some advice / ask for advice</li>\n                    <li>suggestions / recommendations</li>\n                    <li>what should I do...? / what would you suggest...?</li>\n                    <li>I need your advice with...</li>\n                </ul>\n            </div>\n        ",
        "detailedOutline": "\n            <div class=\"outline-note\">\n                <p><strong>LƯU Ý:</strong> Thư cho lời khuyên thường là thư thân mật.</p>\n            </div>\n            <div class=\"outline-step\">\n                <h4>1. Lời chào mở đầu</h4>\n                <p>- Thân mật: ↳ <span class=\"outline-phrase\">Dear [tên của người nhận],</span></p>\n            </div>\n            <div class=\"outline-step\">\n                <h4>2. Mở thư</h4>\n                <p>- Thân mật: ↳ <span class=\"outline-phrase\">Thanks for your letter. I hope you are doing well. I’m writing to give you some advice about your situation.</span></p>\n            </div>\n            <div class=\"outline-step\">\n                <h4>3. Thân thư</h4>\n                <p>Lần lượt đưa ra lời khuyên/gợi ý phù hợp với tình huống của đề.</p>\n                <div class=\"outline-structures\">\n                    <h5>CẤU TRÚC CHO LỜI KHUYÊN:</h5>\n                    <ul>\n                        <li>↳ <span class=\"outline-phrase\">You should + Vo.</span></li>\n                        <li>↳ <span class=\"outline-phrase\">It would be a good idea to + Vo.</span></li>\n                        <li>↳ <span class=\"outline-phrase\">If I were you, I would + Vo.</span></li>\n                        <li>↳ <span class=\"outline-phrase\">You can try + Ving.</span></li>\n                        <li>↳ <span class=\"outline-phrase\">Remember to + Vo. / Don’t forget to + Vo.</span></li>\n                    </ul>\n                </div>\n                <p>TỪ LIÊN KẾT GỢI Ý: ↳ <em>First, … → Second, … → Next, … → Finally, …</em></p>\n            </div>\n            <div class=\"outline-step\">\n                <h4>4. Kết thư</h4>\n                <p>- Thân mật: ↳ <span class=\"outline-phrase\">I hope my advice will be helpful to you. Please let me know how everything turns out. Write back soon.</span></p>\n            </div>\n            <div class=\"outline-step\">\n                <h4>5. Lời chào kết thúc</h4>\n                <p>- Thân mật: ↳ <span class=\"outline-phrase\">Best wishes,</span></p>\n            </div>\n        ",
        "practicePrompt": "You have received a letter from an English friend, Helen. She is going to visit Hanoi in June. Write a letter to give her some suggestions. In your letter, you should tell her: Where to stay, What dishes to try, Which places to visit, What to wear when visiting Hanoi. You should write at least 120 words. Do not include your name or address.",
        "sampleWriting": "\n            <!-- Prompt Card -->\n            <div class=\"sample-prompt-container\">\n                <div class=\"sample-prompt-header\">\n                    <i class=\"fa-solid fa-file-circle-question\"></i> ĐỀ BÀI (TOPIC PROMPT)\n                </div>\n                <div class=\"sample-prompt-text\">\n                    <p>You have received a letter from an English friend, Helen. She is going to visit Hanoi in June. Write a letter to give her some suggestions. In your letter, you should tell her:</p>\n                    <ul>\n                        <li>Where to stay</li>\n                        <li>What dishes to try</li>\n                        <li>Which places to visit</li>\n                        <li>What to wear when visiting Hanoi</li>\n                    </ul>\n                    <p style=\"margin-top: 8px; font-style: italic; color: var(--text-muted);\">You should write at least 120 words. Do not include your name or address.</p>\n                </div>\n                <div class=\"sample-analysis-grid\">\n                    <div class=\"sample-analysis-item\">\n                        <strong>Người nhận</strong>\n                        <span>Helen (Bạn bè người Anh)</span>\n                    </div>\n                    <div class=\"sample-analysis-item\">\n                        <strong>Mục đích</strong>\n                        <span>Gợi ý cho chuyến du lịch Hà Nội vào tháng 6</span>\n                    </div>\n                    <div class=\"sample-analysis-item\">\n                        <strong>Văn phong</strong>\n                        <span>Thân mật (Informal Letter)</span>\n                    </div>\n                    <div class=\"sample-analysis-item\">\n                        <strong>Yêu cầu cốt lõi</strong>\n                        <span>Nơi ở, món ăn, điểm tham quan, trang phục</span>\n                    </div>\n                </div>\n            </div>\n\n            <div class=\"content-block\">\n                <h3>BÀI VIẾT MẪU (SAMPLE LETTER - B1 LEVEL)</h3>\n                <div class=\"sample-letter-box\">\n                    <strong>Dear Helen,</strong><br><br>\n                    Thanks for your letter. I hope you are doing well. I’m writing to give you some advice for your trip to Hanoi in June.<br><br>\n                    Firstly, you should stay in a hotel in the city center because it is very convenient for travelling. Many famous places are also located near this area. Secondly, it would be a good idea to try some traditional Vietnamese dishes such as pho, banh mi, and bun cha. These dishes are very popular and delicious. Next, if I were you, I would visit some famous places in Hanoi such as Hoan Kiem Lake, the Old Quarter, and the Temple of Literature. These places are very beautiful and interesting. Finally, remember to wear light and comfortable clothes because the weather in Hanoi can be quite hot in June.<br><br>\n                    I hope my advice will be helpful to you. Please let me know how everything turns out. Write back soon.<br><br>\n                    <strong>Best wishes,</strong>\n                </div>\n                \n                <h3 style=\"margin-top: 25px;\">BẢN DỊCH CHI TIẾT</h3>\n                <div class=\"translation-box\" style=\"background-color: var(--bg-main); border: 1px solid var(--border-color); padding: 20px; border-radius: 12px; margin-top: 15px; font-family: var(--font-body); line-height: 1.8; color: var(--text-muted); font-style: italic;\">\n                    <strong>Helen thân mến,</strong><br><br>\n                    Cảm ơn thư của cậu. Tớ hy vọng cậu vẫn khỏe. Tớ viết thư này để đưa ra một vài gợi ý cho chuyến đi của cậu đến Hà Nội vào tháng Sáu.<br><br>\n                    Đầu tiên, cậu nên ở một khách sạn tại trung tâm thành phố vì nó rất thuận tiện cho việc đi lại. Nhiều địa điểm nổi tiếng cũng nằm gần khu vực này. Thứ hai, cậu nên thử một số món ăn truyền thống của Việt Nam như phở, bánh mì và bún chả. Những món ăn này rất phổ biến và ngon miệng. Tiếp theo, nếu tớ là cậu, tớ sẽ tham quan một số địa điểm nổi tiếng ở Hà Nội như hồ Hoàn Kiếm, phố cổ và Văn Miếu Quốc Tử Giám. Những nơi này rất đẹp và thú vị. Cuối cùng, hãy nhớ mặc quần áo mỏng nhẹ và thoải mái vì thời tiết Hà Nội vào tháng Sáu có thể khá nóng.<br><br>\n                    Tớ hy vọng những lời khuyên của tớ sẽ giúp ích cho cậu. Hãy cho tớ biết chuyến đi diễn ra thế nào nhé. Hãy viết thư lại sớm nhé.<br><br>\n                    <strong>Chúc cậu mọi điều tốt lành,</strong>\n                </div>\n                \n                <div class=\"highlight-box\" style=\"margin-top: 20px;\">\n                    <p><i class=\"fa-solid fa-lightbulb\"></i> Số từ: 155 words. Bài viết chia đoạn rõ ràng, đáp ứng đầy đủ 4 yêu cầu của đề và sử dụng linh hoạt các mẫu câu khuyên bảo chuẩn B1.</p>\n                </div>\n            </div>\n        "
    },
    {
        "id": "request",
        "icon": "fa-hand-holding-hand",
        "titleEn": "Letter of Request",
        "titleVi": "Thư Yêu Cầu",
        "basicInfo": "\n            <div class=\"content-block\">\n                <h3>Mục đích (Purpose)</h3>\n                <p>Yêu cầu hoặc xin thông tin, sự giúp đỡ, hoặc đề nghị một hành động cụ thể từ người nhận.</p>\n            </div>\n            <div class=\"content-block\">\n                <h3>Phong cách thư (Style)</h3>\n                <p>Có thể là thư thân mật, bán trang trọng hoặc trang trọng tùy thuộc vào đối tượng người nhận.</p>\n            </div>\n            <div class=\"content-block\">\n                <h3>Văn phong (Tone)</h3>\n                <p>Lịch sự, rõ ràng, trực tiếp và thể hiện sự tôn trọng.</p>\n            </div>\n        ",
        "identifyingSigns": "\n            <div class=\"content-block\">\n                <h3>Các từ khóa thường xuất hiện trong đề bài:</h3>\n                <ul>\n                    <li>ask for information / request details</li>\n                    <li>could you please tell me / I would like to know</li>\n                    <li>write a letter to ask about...</li>\n                    <li>inquire about...</li>\n                </ul>\n            </div>\n        ",
        "detailedOutline": "\n            <div class=\"outline-note\">\n                <p><strong>LƯU Ý:</strong> Thư yêu cầu thường được dùng để xin thông tin, xin giúp đỡ hoặc đề nghị điều gì đó. Thư có thể là thư thân mật, bán trang trọng hoặc trang trọng.</p>\n            </div>\n            <div class=\"outline-step\">\n                <h4>1. Lời chào mở đầu</h4>\n                <ul>\n                    <li>- Thân mật: ↳ <span class=\"outline-phrase\">Dear [tên của người nhận],</span></li>\n                    <li>- Trang trọng:\n                        <ul>\n                            <li>↳ <span class=\"outline-phrase\">Dear Sir,</span> (nếu biết chắc chắn người nhận là nam)</li>\n                            <li>↳ <span class=\"outline-phrase\">Dear Madam,</span> (nếu biết chắc chắn người nhận là nữ)</li>\n                            <li>↳ <span class=\"outline-phrase\">Dear Sir/Madam,</span> (nếu không biết chắc chắn người nhận là nam hay nữ)</li>\n                        </ul>\n                    </li>\n                    <li>- Bán trang trọng: ↳ <span class=\"outline-phrase\">Dear Mr. / Ms. / Mrs. [họ của người nhận],</span></li>\n                </ul>\n            </div>\n            <div class=\"outline-step\">\n                <h4>2. Mở thư</h4>\n                <ul>\n                    <li>- Thân mật: ↳ <span class=\"outline-phrase\">How are you? I hope you are doing well. I’m writing to ask for some information about [thứ cần xin thông tin] because [lý do].</span></li>\n                    <li>- Trang trọng & Bán trang trọng: ↳ <span class=\"outline-phrase\">I am writing to request some information about [thứ cần xin thông tin] because [lý do].</span></li>\n                </ul>\n            </div>\n            <div class=\"outline-step\">\n                <h4>3. Thân thư</h4>\n                <p>Lần lượt đưa ra các yêu cầu xin thông tin theo đề bài.</p>\n                <div class=\"outline-structures\">\n                    <h5>CẤU TRÚC XIN THÔNG TIN (THÂN MẬT):</h5>\n                    <ul>\n                        <li>↳ <span class=\"outline-phrase\">Can you give me more information about …?</span></li>\n                        <li>↳ <span class=\"outline-phrase\">Can you tell me more about …?</span></li>\n                        <li>↳ <span class=\"outline-phrase\">Can you let me know more about …?</span></li>\n                        <li>↳ <span class=\"outline-phrase\">I want to know more about …</span></li>\n                        <li>↳ <span class=\"outline-phrase\">I want more information about …</span></li>\n                    </ul>\n                    <h5>CẤU TRÚC XIN THÔNG TIN (TRANG TRỌNG & BÁN TRANG TRỌNG):</h5>\n                    <ul>\n                        <li>↳ <span class=\"outline-phrase\">Could you provide me with more information about …?</span></li>\n                        <li>↳ <span class=\"outline-phrase\">Could you give me more details about …?</span></li>\n                        <li>↳ <span class=\"outline-phrase\">I would like to know more about …</span></li>\n                        <li>↳ <span class=\"outline-phrase\">I would like to inquire about …</span></li>\n                        <li>↳ <span class=\"outline-phrase\">I am also wondering about …</span></li>\n                    </ul>\n                </div>\n            </div>\n            <div class=\"outline-step\">\n                <h4>4. Kết thư</h4>\n                <ul>\n                    <li>- Thân mật: ↳ <span class=\"outline-phrase\">I hope you can help me with this. Write back soon.</span></li>\n                    <li>- Trang trọng & Bán trang trọng: ↳ <span class=\"outline-phrase\">Thank you for your time. I look forward to your reply.</span></li>\n                </ul>\n            </div>\n            <div class=\"outline-step\">\n                <h4>5. Lời chào kết thúc</h4>\n                <ul>\n                    <li>- Thân mật: ↳ <span class=\"outline-phrase\">Best wishes,</span></li>\n                    <li>- Trang trọng: ↳ <span class=\"outline-phrase\">Yours faithfully,</span></li>\n                    <li>- Bán trang trọng: ↳ <span class=\"outline-phrase\">Yours sincerely,</span></li>\n                </ul>\n            </div>\n        ",
        "practicePrompt": "Your friend has just completed an English course at Rainbow Language Center and had a great experience. You are planning to study English as well and would like to know more about the course. Write a letter to your friend asking for more information about the course. In your email, you should ask about: The address of the center, The tuition fee, The teachers, The training program. You should write at least 120 words. Do not include your name or address.",
        "sampleWriting": "\n            <!-- Prompt Card -->\n            <div class=\"sample-prompt-container\">\n                <div class=\"sample-prompt-header\">\n                    <i class=\"fa-solid fa-file-circle-question\"></i> ĐỀ BÀI (TOPIC PROMPT)\n                </div>\n                <div class=\"sample-prompt-text\">\n                    <p>Your friend has just completed an English course at Rainbow Language Center and had a great experience. You are planning to study English as well and would like to know more about the course. Write a letter to your friend asking for more information about the course. In your email, you should ask about:</p>\n                    <ul>\n                        <li>The address of the center</li>\n                        <li>The tuition fee</li>\n                        <li>The teachers</li>\n                        <li>The training program</li>\n                    </ul>\n                    <p style=\"margin-top: 8px; font-style: italic; color: var(--text-muted);\">You should write at least 120 words. Do not include your name or address.</p>\n                </div>\n                <div class=\"sample-analysis-grid\">\n                    <div class=\"sample-analysis-item\">\n                        <strong>Người nhận</strong>\n                        <span>Bạn của bạn (Moonie)</span>\n                    </div>\n                    <div class=\"sample-analysis-item\">\n                        <strong>Mục đích</strong>\n                        <span>Hỏi xin thông tin về khóa học tiếng Anh tại Rainbow Language Center</span>\n                    </div>\n                    <div class=\"sample-analysis-item\">\n                        <strong>Văn phong</strong>\n                        <span>Thân mật (Informal Letter)</span>\n                    </div>\n                    <div class=\"sample-analysis-item\">\n                        <strong>Yêu cầu cốt lõi</strong>\n                        <span>Địa chỉ trung tâm, học phí, giáo viên, chương trình học</span>\n                    </div>\n                </div>\n            </div>\n\n            <div class=\"content-block\">\n                <h3>BÀI VIẾT MẪU (SAMPLE LETTER - B1 LEVEL)</h3>\n                <div class=\"sample-letter-box\">\n                    <strong>Dear Moonie,</strong><br><br>\n                    How are you? I hope you are doing well. I’m writing to ask for some information about the English course at Rainbow Language Center because I am planning to study English there soon.<br><br>\n                    First of all, could you tell me the address of the center? I want to know if it is near my house. In addition, I would like to know about the tuition fee for the course so that I can prepare my budget. Furthermore, can you tell me more about the teachers? Are they friendly and experienced? Finally, I was wondering if you could give me some details about the training program and the class schedule.<br><br>\n                    I hope you can help me with this. Write back soon.<br><br>\n                    <strong>Best wishes,</strong>\n                </div>\n                \n                <h3 style=\"margin-top: 25px;\">BẢN DỊCH CHI TIẾT</h3>\n                <div class=\"translation-box\" style=\"background-color: var(--bg-main); border: 1px solid var(--border-color); padding: 20px; border-radius: 12px; margin-top: 15px; font-family: var(--font-body); line-height: 1.8; color: var(--text-muted); font-style: italic;\">\n                    <strong>Moonie thân mến,</strong><br><br>\n                    Cậu khỏe không? Tớ hy vọng cậu vẫn khỏe. Tớ viết thư này để hỏi một vài thông tin về khóa học tiếng Anh tại Trung tâm Ngoại ngữ Rainbow vì tớ đang có kế hoạch học tiếng Anh ở đó sắp tới.<br><br>\n                    Trước hết, cậu có thể cho tớ biết địa chỉ của trung tâm không? Tớ muốn biết liệu nó có gần nhà tớ không. Ngoài ra, tớ muốn biết về học phí của khóa học để tớ có thể chuẩn bị ngân sách của mình. Hơn nữa, cậu có thể kể thêm cho tớ về các giáo viên ở đó không? Họ có thân thiện và giàu kinh nghiệm không? Cuối cùng, tớ đang băn khoăn liệu cậu có thể cho tớ biết thêm chi tiết về chương trình đào tạo và lịch học không.<br><br>\n                    Tớ hy vọng cậu có thể giúp tớ việc này. Hãy trả lời thư sớm nhé.<br><br>\n                    <strong>Chúc cậu mọi điều tốt lành,</strong>\n                </div>\n                \n                <div class=\"highlight-box\" style=\"margin-top: 20px;\">\n                    <p><i class=\"fa-solid fa-lightbulb\"></i> Số từ: 142 words. Thư yêu cầu thông tin thân thiện, sử dụng đa dạng các mẫu câu hỏi gián tiếp lịch sự và tự nhiên.</p>\n                </div>\n            </div>\n        "
    },
    {
        "id": "description",
        "icon": "fa-circle-info",
        "titleEn": "Letter of Giving Information",
        "titleVi": "Thư Cung Cấp Thông Tin",
        "basicInfo": "\n            <div class=\"content-block\">\n                <h3>Mục đích (Purpose)</h3>\n                <p>Cung cấp thông tin chi tiết hoặc mô tả về một người, một sự kiện, địa điểm, hoặc một trải nghiệm cụ thể theo yêu cầu của người nhận.</p>\n            </div>\n            <div class=\"content-block\">\n                <h3>Phong cách thư (Style)</h3>\n                <p>Có thể là thư thân mật, bán trang trọng hoặc trang trọng tùy ngữ cảnh đề bài.</p>\n            </div>\n            <div class=\"content-block\">\n                <h3>Văn phong (Tone)</h3>\n                <p>Rõ ràng, chi tiết, khách quan và hữu ích.</p>\n            </div>\n        ",
        "identifyingSigns": "\n            <div class=\"content-block\">\n                <h3>Các từ khóa thường xuất hiện trong đề bài:</h3>\n                <ul>\n                    <li>tell me about / give me information about...</li>\n                    <li>describe your... / describe someone...</li>\n                    <li>could you provide some details on...</li>\n                    <li>let me know what... is like</li>\n                </ul>\n            </div>\n        ",
        "detailedOutline": "\n            <div class=\"outline-note\">\n                <p><strong>LƯU Ý:</strong> Thư cung cấp thông tin/mô tả dùng để cung cấp thông tin hoặc mô tả đặc điểm của một người, địa điểm, sự việc hoặc chương trình. Dạng thư này có thể là thư thân mật, bán trang trọng hoặc trang trọng.</p>\n            </div>\n            <div class=\"outline-step\">\n                <h4>1. Lời chào mở đầu</h4>\n                <ul>\n                    <li>- Thân mật: ↳ <span class=\"outline-phrase\">Dear [tên của người nhận],</span></li>\n                    <li>- Trang trọng:\n                        <ul>\n                            <li>↳ <span class=\"outline-phrase\">Dear Sir,</span> (nếu biết chắc chắn người nhận là nam)</li>\n                            <li>↳ <span class=\"outline-phrase\">Dear Madam,</span> (nếu biết chắc chắn người nhận là nữ)</li>\n                            <li>↳ <span class=\"outline-phrase\">Dear Sir/Madam,</span> (nếu không biết chắc chắn người nhận là nam hay nữ)</li>\n                        </ul>\n                    </li>\n                    <li>- Bán trang trọng: ↳ <span class=\"outline-phrase\">Dear Mr. / Ms. / Mrs. [họ của người nhận],</span></li>\n                </ul>\n            </div>\n            <div class=\"outline-step\">\n                <h4>2. Mở thư</h4>\n                <div class=\"outline-structures\">\n                    <h5>KHI THƯ YÊU CẦU CUNG CẤP THÔNG TIN:</h5>\n                    <ul>\n                        <li>- Thân mật: ↳ <span class=\"outline-phrase\">How are you? I hope you are doing well. In your letter, you asked me about [thứ cần mô tả thông tin], so here is some information.</span></li>\n                        <li>- Trang trọng & Bán trang trọng: ↳ <span class=\"outline-phrase\">In your letter, you asked me about [thứ cần mô tả thông tin], so I am writing to provide you with some information.</span></li>\n                    </ul>\n                    <h5>KHI THƯ YÊU CẦU MÔ TẢ MỘT ĐỐI TƯỢNG (NGƯỜI/VẬT/SỰ VIỆC):</h5>\n                    <ul>\n                        <li>- Thân mật: ↳ <span class=\"outline-phrase\">How are you? I hope you are doing well. In your letter, you asked me to describe [thứ cần mô tả], so here are some details.</span></li>\n                        <li>- Trang trọng & Bán trang trọng: ↳ <span class=\"outline-phrase\">In your letter, you asked me to describe [thứ cần mô tả], so I am writing to provide you with some details.</span></li>\n                    </ul>\n                </div>\n            </div>\n            <div class=\"outline-step\">\n                <h4>3. Thân thư</h4>\n                <p>Lần lượt cung cấp thông tin hoặc miêu tả các khía cạnh theo yêu cầu của đề.</p>\n                <p>TỪ LIÊN KẾT GỢI Ý: ↳ <em>First, … → Second, … → Next, … → Finally, …</em></p>\n            </div>\n            <div class=\"outline-step\">\n                <h4>4. Kết thư</h4>\n                <ul>\n                    <li>- Thân mật: ↳ <span class=\"outline-phrase\">I hope you will find this information useful. Let me know if you need more details.</span></li>\n                    <li>- Trang trọng & Bán trang trọng: ↳ <span class=\"outline-phrase\">I hope the information above will be helpful to you. Please feel free to contact me if you need more details.</span></li>\n                </ul>\n            </div>\n            <div class=\"outline-step\">\n                <h4>5. Lời chào kết thúc</h4>\n                <ul>\n                    <li>- Thân mật: ↳ <span class=\"outline-phrase\">Best wishes,</span></li>\n                    <li>- Trang trọng: ↳ <span class=\"outline-phrase\">Yours faithfully,</span></li>\n                    <li>- Bán trang trọng: ↳ <span class=\"outline-phrase\">Yours sincerely,</span></li>\n                </ul>\n            </div>\n        ",
        "practicePrompt": "You have received a letter from your English friend, Emily. Read part of her letter below: ... I have received a letter from your friend, Hoa. She is going to do a course in London, so she asked me if she could stay with me and my family until she finds an apartment. Could you tell me some information about her? (things like her personality, her hobbies, her current work or study). I need to know whether she will fit in my family or not ... Write a letter responding to Emily. You should write at least 120 words. Do not include your name or address.",
        "sampleWriting": "\n            <!-- Prompt Card -->\n            <div class=\"sample-prompt-container\">\n                <div class=\"sample-prompt-header\">\n                    <i class=\"fa-solid fa-file-circle-question\"></i> ĐỀ BÀI (TOPIC PROMPT)\n                </div>\n                <div class=\"sample-prompt-text\">\n                    <p>You have received a letter from your English friend, Emily. Read part of her letter below:</p>\n                    <p style=\"margin: 10px 0; padding: 10px 14px; background: rgba(0,0,0,0.03); border-left: 3px solid var(--accent-red); font-style: italic;\">\n                        \"... I have received a letter from your friend, Hoa. She is going to do a course in London, so she asked me if she could stay with me and my family until she finds an apartment. Could you tell me some information about her? (things like her personality, her hobbies, her current work or study). I need to know whether she will fit in my family or not ...\"\n                    </p>\n                    <p>Write a letter responding to Emily. You should write at least 120 words. Do not include your name or address.</p>\n                </div>\n                <div class=\"sample-analysis-grid\">\n                    <div class=\"sample-analysis-item\">\n                        <strong>Người nhận</strong>\n                        <span>Emily (Bạn bè người Anh)</span>\n                    </div>\n                    <div class=\"sample-analysis-item\">\n                        <strong>Mục đích</strong>\n                        <span>Cung cấp thông tin và miêu tả về bạn Hoa để xem có phù hợp ở chung không</span>\n                    </div>\n                    <div class=\"sample-analysis-item\">\n                        <strong>Văn phong</strong>\n                        <span>Thân mật (Informal Letter)</span>\n                    </div>\n                    <div class=\"sample-analysis-item\">\n                        <strong>Yêu cầu cốt lõi</strong>\n                        <span>Tính cách, sở thích, việc học/làm hiện tại của Hoa và khả năng hòa nhập</span>\n                    </div>\n                </div>\n            </div>\n\n            <div class=\"content-block\">\n                <h3>BÀI VIẾT MẪU (SAMPLE LETTER - B1 LEVEL)</h3>\n                <div class=\"sample-letter-box\">\n                    <strong>Dear Emily,</strong><br><br>\n                    How are you? I hope you are doing well. In your letter, you asked me about my friend Hoa, so here is some information.<br><br>\n                    Firstly, she is a very kind and friendly person. She gets on well with everyone and is always willing to help others. Secondly, in her free time, she likes reading books, cooking traditional Vietnamese food, and listening to music. I think she would be happy to cook some delicious meals for your family. Finally, she is currently studying business at university and works very hard. She is responsible and always keeps her room tidy. Therefore, I believe she will fit in very well with your family.<br><br>\n                    I hope you will find this information useful. Let me know if you need more details.<br><br>\n                    <strong>Best wishes,</strong>\n                </div>\n                \n                <h3 style=\"margin-top: 25px;\">BẢN DỊCH CHI TIẾT</h3>\n                <div class=\"translation-box\" style=\"background-color: var(--bg-main); border: 1px solid var(--border-color); padding: 20px; border-radius: 12px; margin-top: 15px; font-family: var(--font-body); line-height: 1.8; color: var(--text-muted); font-style: italic;\">\n                    <strong>Emily thân mến,</strong><br><br>\n                    Cậu khỏe không? Tớ hy vọng cậu vẫn khỏe. Trong thư của cậu, cậu đã hỏi tớ về bạn Hoa của tớ, vì vậy dưới đây là một số thông tin.<br><br>\n                    Đầu tiên, cô ấy là một người rất tốt bụng và thân thiện. Cô ấy hòa thuận với tất cả mọi người và luôn sẵn lòng giúp đỡ người khác. Thứ hai, trong thời gian rảnh, cô ấy thích đọc sách, nấu các món ăn truyền thống của Việt Nam và nghe nhạc. Tớ nghĩ cô ấy sẽ rất vui khi được nấu một vài bữa ăn ngon cho gia đình cậu. Cuối cùng, cô ấy hiện đang học ngành kinh doanh tại trường đại học và học tập rất chăm chỉ. Cô ấy là người có trách nhiệm và luôn giữ phòng ngủ ngăn nắp. Vì vậy, tớ tin rằng cô ấy sẽ hòa nhập rất tốt với gia đình cậu.<br><br>\n                    Tớ hy vọng cậu sẽ thấy những thông tin này hữu ích. Hãy cho tớ biết nếu cậu cần thêm chi tiết nhé.<br><br>\n                    <strong>Chúc cậu mọi điều tốt lành,</strong>\n                </div>\n                \n                <div class=\"highlight-box\" style=\"margin-top: 20px;\">\n                    <p><i class=\"fa-solid fa-lightbulb\"></i> Số từ: 145 words. Thư mô tả thông tin người bạn chi tiết, tự nhiên, trả lời trọn vẹn cả 3 khía cạnh tính cách, sở thích và học tập.</p>\n                </div>\n            </div>\n        "
    },
    {
        "id": "complaint",
        "icon": "fa-triangle-exclamation",
        "titleEn": "Letter of Complaint",
        "titleVi": "Thư Phàn Nàn",
        "basicInfo": "\n            <div class=\"content-block\">\n                <h3>Mục đích (Purpose)</h3>\n                <p>Bày tỏ sự không hài lòng về chất lượng sản phẩm, dịch vụ hoặc một tình huống bất tiện, đồng thời yêu cầu phương án giải quyết thỏa đáng.</p>\n            </div>\n            <div class=\"content-block\">\n                <h3>Phong cách thư (Style)</h3>\n                <p>Chủ yếu là thư trang trọng (Formal) hoặc bán trang trọng (Semi-formal).</p>\n            </div>\n            <div class=\"content-block\">\n                <h3>Văn phong (Tone)</h3>\n                <p>Lịch sự nhưng kiên quyết, rõ ràng và có căn cứ.</p>\n            </div>\n        ",
        "identifyingSigns": "\n            <div class=\"content-block\">\n                <h3>Các từ khóa thường xuất hiện trong đề bài:</h3>\n                <ul>\n                    <li>complain about / express dissatisfaction with...</li>\n                    <li>not satisfied with... / report a problem</li>\n                    <li>poor service / bad quality</li>\n                    <li>ask for a refund / replacement / solution</li>\n                </ul>\n            </div>\n        ",
        "detailedOutline": "\n            <div class=\"outline-note\">\n                <p><strong>LƯU Ý:</strong> Thư phàn nàn thường là thư bán trang trọng hoặc trang trọng.</p>\n            </div>\n            <div class=\"outline-step\">\n                <h4>1. Lời chào mở đầu</h4>\n                <ul>\n                    <li>- Trang trọng:\n                        <ul>\n                            <li>↳ <span class=\"outline-phrase\">Dear Sir,</span> (nếu biết chắc chắn người nhận là nam)</li>\n                            <li>↳ <span class=\"outline-phrase\">Dear Madam,</span> (nếu biết chắc chắn người nhận là nữ)</li>\n                            <li>↳ <span class=\"outline-phrase\">Dear Sir/Madam,</span> (nếu không biết chắc chắn người nhận là nam hay nữ)</li>\n                        </ul>\n                    </li>\n                    <li>- Bán trang trọng: ↳ <span class=\"outline-phrase\">Dear Mr. / Ms. / Mrs. [họ của người nhận],</span></li>\n                </ul>\n            </div>\n            <div class=\"outline-step\">\n                <h4>2. Mở thư</h4>\n                <p>↳ <span class=\"outline-phrase\">I am writing to complain about [vấn đề cần phàn nàn]. I recently used your [sản phẩm/dịch vụ] and was not satisfied with it.</span></p>\n            </div>\n            <div class=\"outline-step\">\n                <h4>3. Thân thư</h4>\n                <div class=\"outline-substep\">\n                    <h5>Thân thư 1: Trình bày vấn đề</h5>\n                    <p>↳ <span class=\"outline-phrase\">The main problem was that [vấn đề 1].</span> → Trình bày cụ thể.<br>\n                    ↳ <span class=\"outline-phrase\">Another issue was that [vấn đề 2].</span> → Trình bày cụ thể.<br>\n                    ↳ <span class=\"outline-phrase\">Finally, I also found that [vấn đề 3].</span> → Trình bày cụ thể.</p>\n                </div>\n                <div class=\"outline-substep\" style=\"margin-top: 14px;\">\n                    <h5>Thân thư 2: Cảm xúc với trải nghiệm và đề xuất giải pháp</h5>\n                    <p>↳ <span class=\"outline-phrase\">I was very disappointed / quite unhappy with these problems. Therefore, I would appreciate it if you could [giải pháp cụ thể để giải quyết vấn đề].</span></p>\n                </div>\n            </div>\n            <div class=\"outline-step\">\n                <h4>4. Kết thư</h4>\n                <p>Yêu cầu xem xét vấn đề: ↳ <span class=\"outline-phrase\">I hope that you will look into these issues soon.</span><br>\n                Mong đợi hồi âm: ↳ <span class=\"outline-phrase\">I look forward to receiving your reply soon.</span></p>\n            </div>\n            <div class=\"outline-step\">\n                <h4>5. Lời chào kết thúc</h4>\n                <ul>\n                    <li>- Trang trọng: ↳ <span class=\"outline-phrase\">Yours faithfully,</span></li>\n                    <li>- Bán trang trọng: ↳ <span class=\"outline-phrase\">Yours sincerely,</span></li>\n                </ul>\n            </div>\n        ",
        "practicePrompt": "You are a member of a local sports center. You have recently used the changing room and were not satisfied with its condition. Write an email to the manager of the sports center. In your email, you should: Describe the problems you found in the changing room, Explain how the situation made you feel, Suggest what should be done to improve the facility. You should write at least 120 words. Do not include your name or address.",
        "sampleWriting": "\n            <!-- Prompt Card -->\n            <div class=\"sample-prompt-container\">\n                <div class=\"sample-prompt-header\">\n                    <i class=\"fa-solid fa-file-circle-question\"></i> ĐỀ BÀI (TOPIC PROMPT)\n                </div>\n                <div class=\"sample-prompt-text\">\n                    <p>You are a member of a local sports center. You have recently used the changing room and were not satisfied with its condition. Write an email to the manager of the sports center. In your email, you should:</p>\n                    <ul>\n                        <li>Describe the problems you found in the changing room</li>\n                        <li>Explain how the situation made you feel</li>\n                        <li>Suggest what should be done to improve the facility</li>\n                    </ul>\n                    <p style=\"margin-top: 8px; font-style: italic; color: var(--text-muted);\">You should write at least 120 words. Do not include your name or address.</p>\n                </div>\n                <div class=\"sample-analysis-grid\">\n                    <div class=\"sample-analysis-item\">\n                        <strong>Người nhận</strong>\n                        <span>Quản lý trung tâm thể thao (The manager)</span>\n                    </div>\n                    <div class=\"sample-analysis-item\">\n                        <strong>Mục đích</strong>\n                        <span>Phàn nàn về phòng thay đồ và đề xuất giải pháp cải thiện</span>\n                    </div>\n                    <div class=\"sample-analysis-item\">\n                        <strong>Văn phong</strong>\n                        <span>Trang trọng (Formal Letter)</span>\n                    </div>\n                    <div class=\"sample-analysis-item\">\n                        <strong>Yêu cầu cốt lõi</strong>\n                        <span>Mô tả các vấn đề, bày tỏ cảm xúc, đề xuất giải pháp</span>\n                    </div>\n                </div>\n            </div>\n\n            <div class=\"content-block\">\n                <h3>BÀI VIẾT MẪU (SAMPLE LETTER - B1 LEVEL)</h3>\n                <div class=\"sample-letter-box\">\n                    <strong>Dear Sir/Madam,</strong><br><br>\n                    I am writing to complain about the condition of the changing room at your sports center. I recently used the facility and was not satisfied with it.<br><br>\n                    The main problem was that the floor was very dirty and wet, which was quite dangerous for members. Another issue was that several lockers were broken, so I could not safely store my personal belongings. Finally, I also found that some of the showers did not have hot water. I was very disappointed with these problems because I have always enjoyed using your center. Therefore, I would appreciate it if you could clean the changing room more regularly, repair the broken lockers, and fix the showers as soon as possible.<br><br>\n                    I hope that you will look into these issues soon. I look forward to receiving your reply soon.<br><br>\n                    <strong>Yours faithfully,</strong>\n                </div>\n                \n                <h3 style=\"margin-top: 25px;\">BẢN DỊCH CHI TIẾT</h3>\n                <div class=\"translation-box\" style=\"background-color: var(--bg-main); border: 1px solid var(--border-color); padding: 20px; border-radius: 12px; margin-top: 15px; font-family: var(--font-body); line-height: 1.8; color: var(--text-muted); font-style: italic;\">\n                    <strong>Kính gửi Ông/Bà,</strong><br><br>\n                    Tôi viết thư này để phàn nàn về tình trạng của phòng thay đồ tại trung tâm thể thao của ông/bà. Gần đây tôi đã sử dụng cơ sở vật chất này và không hài lòng với nó.<br><br>\n                    Vấn đề chính là sàn nhà rất bẩn và ẩm ướt, điều này khá nguy hiểm cho các hội viên. Một vấn đề khác là một số tủ đựng đồ bị hỏng, vì vậy tôi không thể cất giữ đồ dùng cá nhân của mình một cách an toàn. Cuối cùng, tôi cũng nhận thấy một số vòi hoa sen không có nước nóng. Tôi rất thất vọng với những vấn đề này vì tôi luôn thích sử dụng trung tâm của ông/bà. Do đó, tôi sẽ rất cảm kích nếu ông/bà có thể dọn dẹp phòng thay đồ thường xuyên hơn, sửa chữa các tủ đựng đồ bị hỏng và sửa lại các vòi hoa sen càng sớm càng tốt.<br><br>\n                    Tôi hy vọng ông/bà sẽ sớm xem xét các vấn đề này. Tôi rất mong sớm nhận được phản hồi từ ông/bà.<br><br>\n                    <strong>Trân trọng,</strong>\n                </div>\n                \n                <div class=\"highlight-box\" style=\"margin-top: 20px;\">\n                    <p><i class=\"fa-solid fa-lightbulb\"></i> Số từ: 150 words. Thư phàn nàn chuẩn mực, phân tách 3 lỗi cụ thể và đưa ra 3 giải pháp tương ứng rất thuyết phục.</p>\n                </div>\n            </div>\n        "
    },
    {
        "id": "feedback",
        "icon": "fa-comment-dots",
        "titleEn": "Letter of Feedback",
        "titleVi": "Thư Phản Hồi, Đánh Giá",
        "basicInfo": "\n            <div class=\"content-block\">\n                <h3>Mục đích (Purpose)</h3>\n                <p>Đưa ra đánh giá, nhận xét (cả điểm hài lòng và điểm chưa hài lòng) về một dịch vụ, sự kiện hoặc sản phẩm đã trải nghiệm, đồng thời đóng góp ý kiến cải thiện.</p>\n            </div>\n            <div class=\"content-block\">\n                <h3>Phong cách thư (Style)</h3>\n                <p>Thường là thư bán trang trọng hoặc trang trọng.</p>\n            </div>\n            <div class=\"content-block\">\n                <h3>Văn phong (Tone)</h3>\n                <p>Khách quan, xây dựng, mang tính đóng góp tích cực.</p>\n            </div>\n        ",
        "identifyingSigns": "\n            <div class=\"content-block\">\n                <h3>Các từ khóa thường xuất hiện trong đề bài:</h3>\n                <ul>\n                    <li>give feedback on / share your opinion about...</li>\n                    <li>write a letter to comment on...</li>\n                    <li>say what you liked or did not like about...</li>\n                    <li>say what you are satisfied or dissatisfied with...</li>\n                </ul>\n            </div>\n        ",
        "detailedOutline": "\n            <div class=\"outline-note\">\n                <p><strong>LƯU Ý:</strong> Thư cho phản hồi đánh giá thường là thư bán trang trọng hoặc trang trọng.</p>\n            </div>\n            <div class=\"outline-step\">\n                <h4>1. Lời chào mở đầu</h4>\n                <ul>\n                    <li>- Trang trọng:\n                        <ul>\n                            <li>↳ <span class=\"outline-phrase\">Dear Sir,</span> (nếu biết chắc chắn người nhận là nam)</li>\n                            <li>↳ <span class=\"outline-phrase\">Dear Madam,</span> (nếu biết chắc chắn người nhận là nữ)</li>\n                            <li>↳ <span class=\"outline-phrase\">Dear Sir/Madam,</span> (nếu không biết chắc chắn người nhận là nam hay nữ)</li>\n                        </ul>\n                    </li>\n                    <li>- Bán trang trọng: ↳ <span class=\"outline-phrase\">Dear Mr. / Ms. / Mrs. [họ của người nhận],</span></li>\n                </ul>\n            </div>\n            <div class=\"outline-step\">\n                <h4>2. Mở thư</h4>\n                <p>↳ <span class=\"outline-phrase\">I am writing to give you feedback on [vấn đề cần phản hồi đánh giá]. I recently used your [sản phẩm/dịch vụ] and would like to share my experience.</span></p>\n            </div>\n            <div class=\"outline-step\">\n                <h4>3. Thân thư</h4>\n                <p>Lần lượt đưa ra phản hồi đánh giá (khen/chê) và sau đó đề xuất giải pháp để cải thiện.</p>\n                <div class=\"outline-structures\">\n                    <h5>CÁC CẤU TRÚC ĐÁNH GIÁ TÍCH CỰC [KHEN]:</h5>\n                    <p>↳ <span class=\"outline-phrase\">First of all, I would like to mention some positive points about your [sản phẩm/dịch vụ].</span></p>\n                    <ul>\n                        <li>↳ <span class=\"outline-phrase\">I was very satisfied with [điểm khen] because [lý do].</span></li>\n                        <li>↳ <span class=\"outline-phrase\">I really liked [điểm khen] because [lý do].</span></li>\n                        <li>↳ <span class=\"outline-phrase\">I was impressed with [điểm khen] as [lý do].</span></li>\n                        <li>↳ <span class=\"outline-phrase\">One thing I liked most was [điểm khen] since [lý do].</span></li>\n                    </ul>\n                    <h5>CÁC CẤU TRÚC PHẢN ÁNH ĐIỂM CHƯA HÀI LÒNG [CHÊ]:</h5>\n                    <p>↳ <span class=\"outline-phrase\">However, there were also some areas that needed improvement.</span></p>\n                    <ul>\n                        <li>↳ <span class=\"outline-phrase\">I was disappointed with [điểm chê] because [lý do].</span></li>\n                        <li>↳ <span class=\"outline-phrase\">One thing that disappointed me was [điểm chê] since [lý do].</span></li>\n                        <li>↳ <span class=\"outline-phrase\">I was not satisfied with [điểm chê] as [lý do].</span></li>\n                        <li>↳ <span class=\"outline-phrase\">The quality of [điểm chê] was not as good as I expected because [lý do].</span></li>\n                    </ul>\n                    <h5>CÁC CẤU TRÚC ĐỀ XUẤT GIẢI PHÁP:</h5>\n                    <p>↳ <span class=\"outline-phrase\">To enhance the quality of your [sản phẩm/dịch vụ], I have a few suggestions.</span></p>\n                    <ul>\n                        <li>↳ <span class=\"outline-phrase\">I suggest that you should [hành động – Vo].</span></li>\n                        <li>↳ <span class=\"outline-phrase\">I think you should [hành động – Vo].</span></li>\n                        <li>↳ <span class=\"outline-phrase\">It would be better if you could [hành động – Vo].</span></li>\n                        <li>↳ <span class=\"outline-phrase\">I hope you will consider [hành động – Ving].</span></li>\n                    </ul>\n                </div>\n            </div>\n            <div class=\"outline-step\">\n                <h4>4. Kết thư</h4>\n                <p>↳ <span class=\"outline-phrase\">I hope my feedback will help you improve your [sản phẩm/dịch vụ]. Please feel free to contact me if you have any further questions.</span></p>\n            </div>\n            <div class=\"outline-step\">\n                <h4>5. Lời chào kết thúc</h4>\n                <ul>\n                    <li>- Trang trọng: ↳ <span class=\"outline-phrase\">Yours faithfully,</span></li>\n                    <li>- Bán trang trọng: ↳ <span class=\"outline-phrase\">Yours sincerely,</span></li>\n                </ul>\n            </div>\n        ",
        "practicePrompt": "You recently stayed at a hotel and received an email from the hotel manager asking for feedback about your stay. Write an email to give your opinion. In your email, you should: Say whether you were satisfied or dissatisfied with the service, Describe your experience, Suggest ways the hotel can improve its service. You should write at least 120 words. Do not include your name or address.",
        "sampleWriting": "\n            <!-- Prompt Card -->\n            <div class=\"sample-prompt-container\">\n                <div class=\"sample-prompt-header\">\n                    <i class=\"fa-solid fa-file-circle-question\"></i> ĐỀ BÀI (TOPIC PROMPT)\n                </div>\n                <div class=\"sample-prompt-text\">\n                    <p>You recently stayed at a hotel and received an email from the hotel manager asking for feedback about your stay. Write an email to give your opinion. In your email, you should:</p>\n                    <ul>\n                        <li>Say whether you were satisfied or dissatisfied with the service</li>\n                        <li>Describe your experience</li>\n                        <li>Suggest ways the hotel can improve its service</li>\n                    </ul>\n                    <p style=\"margin-top: 8px; font-style: italic; color: var(--text-muted);\">You should write at least 120 words. Do not include your name or address.</p>\n                </div>\n                <div class=\"sample-analysis-grid\">\n                    <div class=\"sample-analysis-item\">\n                        <strong>Người nhận</strong>\n                        <span>Quản lý khách sạn (Hotel manager)</span>\n                    </div>\n                    <div class=\"sample-analysis-item\">\n                        <strong>Mục đích</strong>\n                        <span>Đưa ra phản hồi đánh giá về kỳ nghỉ và đề xuất cải thiện dịch vụ</span>\n                    </div>\n                    <div class=\"sample-analysis-item\">\n                        <strong>Văn phong</strong>\n                        <span>Trang trọng / Bán trang trọng (Formal / Semi-formal)</span>\n                    </div>\n                    <div class=\"sample-analysis-item\">\n                        <strong>Yêu cầu cốt lõi</strong>\n                        <span>Mức độ hài lòng, mô tả trải nghiệm (khen/chê), đề xuất giải pháp</span>\n                    </div>\n                </div>\n            </div>\n\n            <div class=\"content-block\">\n                <h3>BÀI VIẾT MẪU (SAMPLE LETTER - B1 LEVEL)</h3>\n                <div class=\"sample-letter-box\">\n                    <strong>Dear Sir/Madam,</strong><br><br>\n                    I am writing to give you feedback on my recent stay at your hotel. I recently used your services and would like to share my experience.<br><br>\n                    First of all, I would like to mention some positive points about your hotel. I was very satisfied with the customer service because the staff were polite, friendly, and always ready to assist guests. In addition, the room was spacious and clean. However, there were also some areas that needed improvement. I was disappointed with the Wi-Fi connection because it was slow and unstable. Furthermore, the breakfast menu was quite limited and lacked variety. To enhance the quality of your services, I suggest that you should upgrade the Internet system and offer more options for breakfast.<br><br>\n                    I hope my feedback will help you improve your service. Please feel free to contact me if you have any further questions.<br><br>\n                    <strong>Yours faithfully,</strong>\n                </div>\n                \n                <h3 style=\"margin-top: 25px;\">BẢN DỊCH CHI TIẾT</h3>\n                <div class=\"translation-box\" style=\"background-color: var(--bg-main); border: 1px solid var(--border-color); padding: 20px; border-radius: 12px; margin-top: 15px; font-family: var(--font-body); line-height: 1.8; color: var(--text-muted); font-style: italic;\">\n                    <strong>Kính gửi Ông/Bà,</strong><br><br>\n                    Tôi viết thư này để đưa ra phản hồi về kỳ nghỉ gần đây của tôi tại khách sạn của ông/bà. Gần đây tôi đã sử dụng dịch vụ của ông/bà và muốn chia sẻ trải nghiệm của mình.<br><br>\n                    Trước hết, tôi muốn đề cập đến một số điểm tích cực về khách sạn của ông/bà. Tôi rất hài lòng với dịch vụ chăm sóc khách hàng vì nhân viên rất lịch sự, thân thiện và luôn sẵn sàng hỗ trợ khách. Ngoài ra, phòng ốc rất rộng rãi và sạch sẽ. Tuy nhiên, cũng có một số khía cạnh cần được cải thiện. Tôi đã thất vọng với kết nối Wi-Fi vì nó chậm và không ổn định. Hơn nữa, thực đơn bữa sáng khá hạn chế và thiếu sự đa dạng. Để nâng cao chất lượng dịch vụ của ông/bà, tôi đề nghị ông/bà nên nâng cấp hệ thống Internet và cung cấp nhiều sự lựa chọn hơn cho bữa sáng.<br><br>\n                    Tôi hy vọng phản hồi của tôi sẽ giúp ông/bà cải thiện dịch vụ của mình. Xin vui lòng liên hệ với tôi nếu ông/bà có bất kỳ câu hỏi nào thêm.<br><br>\n                    <strong>Trân trọng,</strong>\n                </div>\n                \n                <div class=\"highlight-box\" style=\"margin-top: 20px;\">\n                    <p><i class=\"fa-solid fa-lightbulb\"></i> Số từ: 158 words. Thư phản hồi cân bằng giữa khen ngợi và góp ý mang tính xây dựng, bố cục logic và từ vựng chuẩn B1.</p>\n                </div>\n            </div>\n        "
    },
    {
        "id": "apology",
        "icon": "fa-handshake-angle",
        "titleEn": "Letter of Apology",
        "titleVi": "Thư Xin Lỗi",
        "basicInfo": "\n            <div class=\"content-block\">\n                <h3>Mục đích (Purpose)</h3>\n                <p>Gửi lời xin lỗi chân thành về một sai sót, sự cố hoặc việc không thể thực hiện một cam kết, giải thích lý do và đưa ra giải pháp khắc phục/đền bù.</p>\n            </div>\n            <div class=\"content-block\">\n                <h3>Phong cách thư (Style)</h3>\n                <p>Có thể là thư thân mật, bán trang trọng hoặc trang trọng tùy thuộc vào đối tượng người nhận.</p>\n            </div>\n            <div class=\"content-block\">\n                <h3>Văn phong (Tone)</h3>\n                <p>Chân thành, biết lỗi, tôn trọng và thể hiện thiện chí sửa chữa.</p>\n            </div>\n        ",
        "identifyingSigns": "\n            <div class=\"content-block\">\n                <h3>Các từ khóa thường xuất hiện trong đề bài:</h3>\n                <ul>\n                    <li>apologize for / say sorry for...</li>\n                    <li>explain why you (missed, were late, forgot, damaged...)</li>\n                    <li>say how you will make up for it</li>\n                    <li>explain the situation and offer a solution</li>\n                </ul>\n            </div>\n        ",
        "detailedOutline": "\n            <div class=\"outline-note\">\n                <p><strong>LƯU Ý:</strong> Thư xin lỗi có thể là thư thân mật, bán trang trọng hoặc trang trọng.</p>\n            </div>\n            <div class=\"outline-step\">\n                <h4>1. Lời chào mở đầu</h4>\n                <ul>\n                    <li>- Thân mật: ↳ <span class=\"outline-phrase\">Dear [tên của người nhận],</span></li>\n                    <li>- Trang trọng:\n                        <ul>\n                            <li>↳ <span class=\"outline-phrase\">Dear Sir,</span> (nếu biết chắc chắn người nhận là nam)</li>\n                            <li>↳ <span class=\"outline-phrase\">Dear Madam,</span> (nếu biết chắc chắn người nhận là nữ)</li>\n                            <li>↳ <span class=\"outline-phrase\">Dear Sir/Madam,</span> (nếu không biết chắc chắn người nhận là nam hay nữ)</li>\n                        </ul>\n                    </li>\n                    <li>- Bán trang trọng: ↳ <span class=\"outline-phrase\">Dear Mr. / Ms. / Mrs. [họ của người nhận],</span></li>\n                </ul>\n            </div>\n            <div class=\"outline-step\">\n                <h4>2. Mở thư</h4>\n                <ul>\n                    <li>- Thân mật: ↳ <span class=\"outline-phrase\">I’m really sorry for [vấn đề cần xin lỗi]. Let me explain what happened so you can understand the situation.</span></li>\n                    <li>- Trang trọng & Bán trang trọng: ↳ <span class=\"outline-phrase\">I am writing to apologize for [vấn đề cần xin lỗi]. I understand that this may have caused some inconvenience, and I would like to explain the situation.</span></li>\n                </ul>\n            </div>\n            <div class=\"outline-step\">\n                <h4>3. Thân thư</h4>\n                <p>Lần lượt giải thích lý do và nêu hành động bù đắp phù hợp.</p>\n                <div class=\"outline-structures\">\n                    <h5>CẤU TRÚC GIẢI THÍCH LÝ DO:</h5>\n                    <p><strong>- Thân mật:</strong> ↳ <span class=\"outline-phrase\">First of all, let me explain why this happened.</span></p>\n                    <ul>\n                        <li>↳ <span class=\"outline-phrase\">I’m really sorry that I couldn’t [hành động – Vo] because [lý do].</span></li>\n                        <li>↳ <span class=\"outline-phrase\">I missed [sự kiện] because [lý do].</span></li>\n                        <li>↳ <span class=\"outline-phrase\">I felt bad about not [hành động – Ving] because [lý do].</span></li>\n                        <li>↳ <span class=\"outline-phrase\">I didn’t mean to [hành động – Vo], but [lý do].</span></li>\n                    </ul>\n                    <p><strong>- Trang trọng & Bán trang trọng:</strong> ↳ <span class=\"outline-phrase\">First of all, I would like to explain why this happened.</span></p>\n                    <ul>\n                        <li>↳ <span class=\"outline-phrase\">I was unable to [hành động – Vo] because [lý do].</span></li>\n                        <li>↳ <span class=\"outline-phrase\">I regret that I was unable to [hành động – Vo] because [lý do].</span></li>\n                        <li>↳ <span class=\"outline-phrase\">Because [lý do], I was unable to [hành động – Vo].</span></li>\n                        <li>↳ <span class=\"outline-phrase\">Unfortunately, I could not [hành động – Vo] because [lý do].</span></li>\n                    </ul>\n                    <p style=\"margin-top: 10px; font-style: italic; color: var(--text-muted);\">LƯU Ý: Sau khi nêu lý do, nên thêm 1-3 câu mô tả cụ thể tình huống để người đọc hiểu rõ hơn. Sử dụng thì QUÁ KHỨ ĐƠN để mô tả những sự việc đã xảy ra.</p>\n                    <h5 style=\"margin-top: 14px;\">CẤU TRÚC NÊU HÀNH ĐỘNG BÙ ĐẮP:</h5>\n                    <ul>\n                        <li>- Thân mật: ↳ <span class=\"outline-phrase\">Finally, let me make it up to you by [hành động – Ving].</span></li>\n                        <li>- Trang trọng & Bán trang trọng: ↳ <span class=\"outline-phrase\">To make up for my mistake, I would like to [hành động – Vo].</span></li>\n                    </ul>\n                </div>\n            </div>\n            <div class=\"outline-step\">\n                <h4>4. Kết thư</h4>\n                <ul>\n                    <li>- Thân mật: ↳ <span class=\"outline-phrase\">Sorry once again. Thanks for taking the time to read this. Write back soon.</span></li>\n                    <li>- Trang trọng & Bán trang trọng: ↳ <span class=\"outline-phrase\">I would like to apologize once again for the inconvenience. Thank you for taking the time to read my letter. I look forward to receiving your reply soon.</span></li>\n                </ul>\n            </div>\n            <div class=\"outline-step\">\n                <h4>5. Lời chào kết thúc</h4>\n                <ul>\n                    <li>- Thân mật: ↳ <span class=\"outline-phrase\">Best wishes,</span></li>\n                    <li>- Trang trọng: ↳ <span class=\"outline-phrase\">Yours faithfully,</span></li>\n                    <li>- Bán trang trọng: ↳ <span class=\"outline-phrase\">Yours sincerely,</span></li>\n                </ul>\n            </div>\n        ",
        "practicePrompt": "You borrowed a book from your friend Helen, but forgot to return it. Read part of her letter below: … Hey! How have you been lately? By the way, have you finished reading the book you borrowed from me? I was wondering why you haven’t returned it yet. When do you plan to give it back, and how will you return it? … Write a letter to reply to Helen. In your letter, you should: apologize for not returning the book, explain your current situation and whether you’ve finished the book, say when and how you will return it. You should write at least 120 words. Do not include your name or address.",
        "sampleWriting": "\n            <!-- Prompt Card -->\n            <div class=\"sample-prompt-container\">\n                <div class=\"sample-prompt-header\">\n                    <i class=\"fa-solid fa-file-circle-question\"></i> ĐỀ BÀI (TOPIC PROMPT)\n                </div>\n                <div class=\"sample-prompt-text\">\n                    <p>You borrowed a book from your friend Helen, but forgot to return it. Read part of her letter below:</p>\n                    <p style=\"margin: 10px 0; padding: 10px 14px; background: rgba(0,0,0,0.03); border-left: 3px solid var(--accent-red); font-style: italic;\">\n                        \"… Hey! How have you been lately? By the way, have you finished reading the book you borrowed from me? I was wondering why you haven’t returned it yet. When do you plan to give it back, and how will you return it? …\"\n                    </p>\n                    <p>Write a letter to reply to Helen. In your letter, you should:</p>\n                    <ul>\n                        <li>apologize for not returning the book</li>\n                        <li>explain your current situation and whether you’ve finished the book</li>\n                        <li>say when and how you will return it</li>\n                    </ul>\n                    <p style=\"margin-top: 8px; font-style: italic; color: var(--text-muted);\">You should write at least 120 words. Do not include your name or address.</p>\n                </div>\n                <div class=\"sample-analysis-grid\">\n                    <div class=\"sample-analysis-item\">\n                        <strong>Người nhận</strong>\n                        <span>Helen (Bạn bè thân thiết)</span>\n                    </div>\n                    <div class=\"sample-analysis-item\">\n                        <strong>Mục đích</strong>\n                        <span>Xin lỗi vì quên trả sách, giải thích lý do, hẹn ngày trả và đền bù</span>\n                    </div>\n                    <div class=\"sample-analysis-item\">\n                        <strong>Văn phong</strong>\n                        <span>Thân mật (Informal Letter)</span>\n                    </div>\n                    <div class=\"sample-analysis-item\">\n                        <strong>Yêu cầu cốt lõi</strong>\n                        <span>Xin lỗi, giải thích lý do/tình trạng đọc xong, thời gian & cách thức trả sách</span>\n                    </div>\n                </div>\n            </div>\n\n            <div class=\"content-block\">\n                <h3>BÀI VIẾT MẪU (SAMPLE LETTER - B1 LEVEL)</h3>\n                <div class=\"sample-letter-box\">\n                    <strong>Dear Helen,</strong><br><br>\n                    I’m really sorry for not returning your book earlier. Let me explain what happened so you can understand the situation.<br><br>\n                    First of all, let me explain why this happened. I’m really sorry that I couldn’t return the book on time because I have been extremely busy preparing for my final exams. During that time, I had several assignments and an important test. As a result, I completely forgot about the book. In addition, I have finished reading the whole book and found it very interesting and helpful. Next, I plan to give it back to you this Saturday. I can come over to your house in the afternoon to return it in person. Finally, let me make it up to you by treating you to a cup of milk tea and some snacks.<br><br>\n                    Sorry once again. Thanks for taking the time to read this. Write back soon.<br><br>\n                    <strong>Best wishes,</strong>\n                </div>\n                \n                <h3 style=\"margin-top: 25px;\">BẢN DỊCH CHI TIẾT</h3>\n                <div class=\"translation-box\" style=\"background-color: var(--bg-main); border: 1px solid var(--border-color); padding: 20px; border-radius: 12px; margin-top: 15px; font-family: var(--font-body); line-height: 1.8; color: var(--text-muted); font-style: italic;\">\n                    <strong>Helen thân mến,</strong><br><br>\n                    Tớ thực sự xin lỗi vì đã không trả sách cho cậu sớm hơn. Hãy để tớ giải thích những gì đã xảy ra để cậu hiểu rõ tình hình nhé.<br><br>\n                    Trước hết, hãy để tớ giải thích tại sao chuyện này lại xảy ra. Tớ thực sự xin lỗi vì tớ đã không thể trả sách đúng hạn vì tớ quá bận rộn chuẩn bị cho kỳ thi cuối kỳ. Trong thời gian đó, tớ có vài bài tập lớn và một bài kiểm tra quan trọng. Kết quả là tớ hoàn toàn quên mất cuốn sách. Ngoài ra, tớ đã đọc xong toàn bộ cuốn sách và thấy nó rất thú vị và bổ ích. Tiếp theo, tớ dự định sẽ trả lại sách cho cậu vào thứ Bảy tuần này. Tớ có thể ghé qua nhà cậu vào buổi chiều để trực tiếp gửi lại sách. Cuối cùng, hãy để tớ bù đắp cho cậu bằng một chầu trà sữa và đồ ăn vặt nhé.<br><br>\n                    Xin lỗi cậu một lần nữa nhé. Cảm ơn cậu vì đã dành thời gian đọc thư này. Hãy viết thư lại cho tớ sớm nhé.<br><br>\n                    <strong>Chúc cậu mọi điều tốt lành,</strong>\n                </div>\n                \n                <div class=\"highlight-box\" style=\"margin-top: 20px;\">\n                    <p><i class=\"fa-solid fa-lightbulb\"></i> Số từ: 160 words. Thư xin lỗi bạn bè tự nhiên, giải thích thuyết phục, nêu rõ thời gian/cách trả và hành động đền bù đáng yêu.</p>\n                </div>\n            </div>\n        "
    },
    {
        "id": "application",
        "icon": "fa-briefcase",
        "titleEn": "Letter of Application",
        "titleVi": "Thư Ứng Tuyển",
        "basicInfo": "\n            <div class=\"content-block\">\n                <h3>Mục đích (Purpose)</h3>\n                <p>Ứng tuyển vào một vị trí công việc, khóa học, chương trình học bổng hoặc tình nguyện viên, nêu bật trình độ, kinh nghiệm và sự phù hợp của bản thân.</p>\n            </div>\n            <div class=\"content-block\">\n                <h3>Phong cách thư (Style)</h3>\n                <p>Luôn là thư trang trọng (Formal Letter).</p>\n            </div>\n            <div class=\"content-block\">\n                <h3>Văn phong (Tone)</h3>\n                <p>Chuyên nghiệp, tự tin, lịch thiệp và tôn trọng.</p>\n            </div>\n        ",
        "identifyingSigns": "\n            <div class=\"content-block\">\n                <h3>Các từ khóa thường xuất hiện trong đề bài:</h3>\n                <ul>\n                    <li>apply for the position / the job of...</li>\n                    <li>write a letter of application</li>\n                    <li>respond to a job advertisement</li>\n                    <li>apply for a part-time / full-time job</li>\n                </ul>\n            </div>\n        ",
        "detailedOutline": "\n            <div class=\"outline-note\">\n                <p><strong>LƯU Ý:</strong> Thư ứng tuyển thường gặp nhất là thư xin việc và luôn là thư trang trọng.</p>\n            </div>\n            <div class=\"outline-step\">\n                <h4>1. Lời chào mở đầu</h4>\n                <p>- Trang trọng:\n                    <ul>\n                        <li>↳ <span class=\"outline-phrase\">Dear Sir,</span> (nếu biết chắc chắn người nhận là nam)</li>\n                        <li>↳ <span class=\"outline-phrase\">Dear Madam,</span> (nếu biết chắc chắn người nhận là nữ)</li>\n                        <li>↳ <span class=\"outline-phrase\">Dear Sir/Madam,</span> (nếu không biết chắc chắn người nhận là nam hay nữ)</li>\n                    </ul>\n                </p>\n            </div>\n            <div class=\"outline-step\">\n                <h4>2. Mở thư</h4>\n                <p>- Trang trọng: ↳ <span class=\"outline-phrase\">I am writing to apply for the position of [vị trí công việc] which was advertised on/in [nguồn tuyển dụng].</span></p>\n            </div>\n            <div class=\"outline-step\">\n                <h4>3. Thân thư</h4>\n                <p>Lần lượt trình bày lý do có hứng thú với vị trí công việc này, đề cập trình độ học vấn và năng lực chuyên môn, kinh nghiệm làm việc đã có, sau đó nêu lý do mình là ứng cử viên phù hợp cho vị trí này.</p>\n                <div class=\"outline-structures\">\n                    <h5>LÝ DO CÓ HỨNG THÚ VỚI VỊ TRÍ CÔNG VIỆC NÀY:</h5>\n                    <p>↳ <span class=\"outline-phrase\">I am very interested in this position because it matches my interests and career goals. In addition, I enjoy [hoạt động liên quan đến công việc]. Therefore, I believe this job will give me a good opportunity to apply what I have learned during my studies and gain practical experience.</span></p>\n                    \n                    <h5>TRÌNH ĐỘ HỌC VẤN VÀ NĂNG LỰC CHUYÊN MÔN:</h5>\n                    <p>↳ <span class=\"outline-phrase\">I recently graduated from [tên trường] with a bachelor’s degree in [chuyên ngành]. During my studies, I developed a strong understanding of [lĩnh vực]. I also gained useful knowledge and abilities such as [kiến thức/năng lực học thuật 1] and [kiến thức/năng lực học thuật 2].</span></p>\n                    \n                    <h5>KINH NGHIỆM LÀM VIỆC ĐÃ CÓ:</h5>\n                    <p>↳ <span class=\"outline-phrase\">I worked part-time as a [vị trí công việc] at [nơi làm việc]. In this job, I was responsible for [nhiệm vụ]. This experience helped me develop skills such as [kỹ năng mềm 1] and [kỹ năng mềm 2].</span></p>\n                    \n                    <h5>KHẲNG ĐỊNH LÀ ỨNG CỬ VIÊN PHÙ HỢP:</h5>\n                    <p>↳ <span class=\"outline-phrase\">I believe I would be a suitable candidate for this position. This is because I am [đặc điểm tính cách]. Moreover, I am eager to learn and can adapt quickly to new environments.</span></p>\n                </div>\n            </div>\n            <div class=\"outline-step\">\n                <h4>4. Kết thư</h4>\n                <p>- Trang trọng: ↳ <span class=\"outline-phrase\">I would be grateful if you could consider my application. I look forward to receiving your reply soon.</span></p>\n            </div>\n            <div class=\"outline-step\">\n                <h4>5. Lời chào kết thúc</h4>\n                <p>- Trang trọng: ↳ <span class=\"outline-phrase\">Yours faithfully,</span></p>\n            </div>\n        ",
        "practicePrompt": "You saw a job advertisement for a sales assistant at a clothing store in your city. Write an email to apply for the job. In your email, you should: Introduce yourself and your current situation, Say why you are interested in the position, Mention any experience you have working with customers. You should write at least 120 words. Do not include your name or address.",
        "sampleWriting": "\n            <!-- Prompt Card -->\n            <div class=\"sample-prompt-container\">\n                <div class=\"sample-prompt-header\">\n                    <i class=\"fa-solid fa-file-circle-question\"></i> ĐỀ BÀI (TOPIC PROMPT)\n                </div>\n                <div class=\"sample-prompt-text\">\n                    <p>You saw a job advertisement for a sales assistant at a clothing store in your city. Write an email to apply for the job. In your email, you should:</p>\n                    <ul>\n                        <li>Introduce yourself and your current situation</li>\n                        <li>Say why you are interested in the position</li>\n                        <li>Mention any experience you have working with customers</li>\n                    </ul>\n                    <p style=\"margin-top: 8px; font-style: italic; color: var(--text-muted);\">You should write at least 120 words. Do not include your name or address.</p>\n                </div>\n                <div class=\"sample-analysis-grid\">\n                    <div class=\"sample-analysis-item\">\n                        <strong>Người nhận</strong>\n                        <span>Nhà tuyển dụng / Quản lý (Dear Sir/Madam)</span>\n                    </div>\n                    <div class=\"sample-analysis-item\">\n                        <strong>Mục đích</strong>\n                        <span>Ứng tuyển vào vị trí nhân viên bán hàng (Sales Assistant)</span>\n                    </div>\n                    <div class=\"sample-analysis-item\">\n                        <strong>Văn phong</strong>\n                        <span>Trang trọng (Formal Letter)</span>\n                    </div>\n                    <div class=\"sample-analysis-item\">\n                        <strong>Yêu cầu cốt lõi</strong>\n                        <span>Giới thiệu bản thân & học vấn, lý do hứng thú, kinh nghiệm với khách hàng</span>\n                    </div>\n                </div>\n            </div>\n\n            <div class=\"content-block\">\n                <h3>BÀI VIẾT MẪU (SAMPLE LETTER - B1 LEVEL)</h3>\n                <div class=\"sample-letter-box\">\n                    <strong>Dear Sir/Madam,</strong><br><br>\n                    I am writing to apply for the position of sales assistant which was advertised on your website.<br><br>\n                    I recently graduated from Can Tho University with a bachelor’s degree in Business Administration. During my studies, I developed a strong understanding of marketing and customer service. I also gained useful knowledge and abilities such as communication and team collaboration.<br><br>\n                    I am very interested in this position because it matches my interests and career goals. In addition, I enjoy helping customers choose suitable fashion products. Therefore, I believe this job will give me a good opportunity to apply what I have learned during my studies and gain practical experience.<br><br>\n                    I worked part-time as a sales assistant at a local clothing store. In this job, I was responsible for welcoming customers and arranging products. This experience helped me develop problem-solving skills and customer care skills.<br><br>\n                    I believe I would be a suitable candidate for this position. This is because I am enthusiastic, honest, and hardworking. Moreover, I am eager to learn and can adapt quickly to new environments.<br><br>\n                    I would be grateful if you could consider my application. I look forward to receiving your reply soon.<br><br>\n                    <strong>Yours faithfully,</strong>\n                </div>\n                \n                <h3 style=\"margin-top: 25px;\">BẢN DỊCH CHI TIẾT</h3>\n                <div class=\"translation-box\" style=\"background-color: var(--bg-main); border: 1px solid var(--border-color); padding: 20px; border-radius: 12px; margin-top: 15px; font-family: var(--font-body); line-height: 1.8; color: var(--text-muted); font-style: italic;\">\n                    <strong>Kính gửi Ông/Bà,</strong><br><br>\n                    Tôi viết thư này để ứng tuyển vào vị trí nhân viên bán hàng được quảng cáo trên trang web của ông/bà.<br><br>\n                    Tôi vừa tốt nghiệp Đại học Cần Thơ với tấm bằng cử nhân ngành Quản trị Kinh doanh. Trong quá trình học, tôi đã phát triển sự hiểu biết sâu sắc về marketing và dịch vụ khách hàng. Tôi cũng tích lũy được những kiến thức và năng lực hữu ích như giao tiếp và làm việc nhóm.<br><br>\n                    Tôi rất hứng thú với vị trí này vì nó phù hợp với sở thích và mục tiêu nghề nghiệp của tôi. Ngoài ra, tôi thích giúp đỡ khách hàng lựa chọn những sản phẩm thời trang phù hợp. Vì vậy, tôi tin rằng công việc này sẽ mang lại cho tôi cơ hội tốt để áp dụng những gì đã học trong quá trình học và tích lũy thêm kinh nghiệm thực tế.<br><br>\n                    Tôi đã từng làm việc bán thời gian với tư cách là nhân viên bán hàng tại một cửa hàng quần áo địa phương. Trong công việc này, tôi chịu trách nhiệm đón tiếp khách hàng và sắp xếp sản phẩm. Kinh nghiệm này đã giúp tôi phát triển kỹ năng giải quyết vấn đề và kỹ năng chăm sóc khách hàng.<br><br>\n                    Tôi tin rằng mình sẽ là ứng cử viên phù hợp cho vị trí này. Điều này là vì tôi là người nhiệt tình, trung thực và làm việc chăm chỉ. Hơn nữa, tôi rất ham học hỏi và có thể thích nghi nhanh chóng với môi trường mới.<br><br>\n                    Tôi sẽ rất biết ơn nếu ông/bà có thể xem xét hồ sơ ứng tuyển của tôi. Tôi rất mong sớm nhận được phản hồi từ ông/bà.<br><br>\n                    <strong>Trân trọng,</strong>\n                </div>\n                \n                <div class=\"highlight-box\" style=\"margin-top: 20px;\">\n                    <p><i class=\"fa-solid fa-lightbulb\"></i> Số từ: 195 words. Thư xin việc chuyên nghiệp, bám sát cấu trúc dàn ý chuẩn B1, nêu bật trình độ học vấn, kinh nghiệm và phẩm chất nổi bật.</p>\n                </div>\n            </div>\n        "
    }
];



// ==========================================================================
// VSTEP TASK 1 EXTRA PRACTICE & ULTRA-DETAILED DIAGNOSTIC GRADING SYSTEM
// ==========================================================================

const extraPracticeData = {
    advice: {
        title: "BÀI LUYỆN TẬP THÊM - DẠNG 01: LETTER OF ADVICE",
        promptText: "You have received a letter from a friend, Emily. She is going to visit Can Tho in December. Write a letter to give her some suggestions. You should tell her:\n• Where to stay\n• What dishes to try\n• Which tourist attractions to visit\n• What to wear\nYou should write at least 120 words. Do not include your name. Your response will be evaluated in terms of Task Fulfillment, Organization, Vocabulary, and Grammar.",
        bulletPoints: [
            "Where to stay",
            "What dishes to try",
            "Which tourist attractions to visit",
            "What to wear"
        ],
        hints: [
            {
                title: "1. Where to stay (Nơi ở)",
                items: [
                    {
                        en: "stay at a hotel in the city centre",
                        vi: "ở khách sạn tại trung tâm thành phố",
                        reasonEn: "because it is convenient to travel around the city.",
                        reasonVi: "vì thuận tiện để đi lại trong thành phố."
                    },
                    {
                        en: "stay at a homestay near Ninh Kieu Wharf",
                        vi: "ở homestay gần Bến Ninh Kiều",
                        reasonEn: "because you can easily visit many famous places.",
                        reasonVi: "vì bạn có thể dễ dàng tham quan nhiều địa điểm nổi tiếng."
                    },
                    {
                        en: "choose a hotel with good reviews",
                        vi: "chọn khách sạn có đánh giá tốt",
                        reasonEn: "because you are more likely to have a comfortable stay.",
                        reasonVi: "vì bạn sẽ có nhiều khả năng có một kỳ nghỉ thoải mái."
                    },
                    {
                        en: "book your room in advance",
                        vi: "đặt phòng trước",
                        reasonEn: "because it helps you get a better price and avoid fully booked hotels.",
                        reasonVi: "vì giúp bạn có giá tốt hơn và tránh tình trạng hết phòng."
                    }
                ]
            },
            {
                title: "2. What dishes to try (Những món ăn nên thử)",
                items: [
                    {
                        en: "try local dishes such as banh xeo, grilled snakehead fish, and fresh fruits",
                        vi: "thử các món ăn địa phương như bánh xèo, cá lóc nướng và trái cây tươi",
                        reasonEn: "because they are some of the most famous dishes in Can Tho and the Mekong Delta.",
                        reasonVi: "vì đây là những món ăn nổi tiếng nhất ở Cần Thơ và miền Tây."
                    },
                    {
                        en: "try traditional Vietnamese dishes such as noodle soup, spring rolls, and banh cong",
                        vi: "thử các món ăn truyền thống của Việt Nam như bún nước lèo, chả giò và bánh cống",
                        reasonEn: "because they can help you learn more about Vietnamese food culture.",
                        reasonVi: "vì chúng giúp bạn hiểu thêm về văn hóa ẩm thực Việt Nam."
                    },
                    {
                        en: "eat at local restaurants and night markets",
                        vi: "ăn tại các nhà hàng và chợ đêm địa phương",
                        reasonEn: "because you can enjoy authentic local food at reasonable prices.",
                        reasonVi: "vì bạn có thể thưởng thức ẩm thực địa phương chính gốc với giá hợp lý."
                    }
                ]
            },
            {
                title: "3. Which places to visit (Những địa điểm nên tham quan)",
                items: [
                    {
                        en: "visit famous places such as Cai Rang Floating Market, Ninh Kieu Wharf, and Binh Thuy Ancient House",
                        vi: "tham quan những địa điểm nổi tiếng như Chợ nổi Cái Răng, Bến Ninh Kiều và Nhà cổ Bình Thủy",
                        reasonEn: "because they are some of the most famous tourist attractions in Can Tho.",
                        reasonVi: "vì đây là những địa điểm du lịch nổi tiếng nhất ở Cần Thơ."
                    },
                    {
                        en: "take a boat trip to Cai Rang Floating Market early in the morning",
                        vi: "đi thuyền tham quan Chợ nổi Cái Răng vào sáng sớm",
                        reasonEn: "because you can enjoy the lively atmosphere and learn more about river culture.",
                        reasonVi: "vì bạn có thể tận hưởng không khí nhộn nhịp và tìm hiểu thêm về văn hóa sông nước."
                    },
                    {
                        en: "visit local fruit orchards and eco-tourism villages",
                        vi: "tham quan các vườn cây ăn trái và làng du lịch sinh thái",
                        reasonEn: "because you can relax in nature and taste fresh tropical fruits.",
                        reasonVi: "vì bạn có thể thư giãn giữa thiên nhiên và thưởng thức trái cây nhiệt đới tươi ngon."
                    }
                ]
            },
            {
                title: "4. What to wear when visiting Can Tho (Nên mặc gì khi đến Cần Thơ)",
                items: [
                    {
                        en: "wear light clothes and comfortable shoes",
                        vi: "mặc quần áo mỏng, nhẹ và mang giày thoải mái",
                        reasonEn: "because the weather in December is pleasant and you may have to walk a lot.",
                        reasonVi: "vì thời tiết tháng 12 dễ chịu và bạn có thể phải đi bộ nhiều."
                    },
                    {
                        en: "bring a hat, sunglasses, and sunscreen",
                        vi: "mang theo mũ, kính râm và kem chống nắng",
                        reasonEn: "because they can protect you from the strong sunlight during boat tours.",
                        reasonVi: "vì chúng có thể bảo vệ bạn khỏi ánh nắng gay gắt khi đi tour sông nước."
                    },
                    {
                        en: "bring a light jacket for breezy evenings",
                        vi: "mang theo áo khoác mỏng cho buổi tối mát mẻ",
                        reasonEn: "because it can be slightly cool near the river at night.",
                        reasonVi: "vì trời có thể hơi se lạnh gần bờ sông vào ban đêm."
                    }
                ]
            }
        ],
        sampleModel: `Dear Emily,\n\nThanks for your letter. I hope you are doing well. I’m writing to give you some advice for your trip to Can Tho in December.\n\nFirstly, you should stay at a hotel near Ninh Kieu Wharf because it is very convenient to travel around the city. In addition, you can easily visit many famous restaurants and cafes in the evening. Secondly, it would be a good idea to try some delicious local dishes such as banh xeo, grilled snakehead fish, and fresh tropical fruits. These dishes are very famous in the Mekong Delta and can help you learn more about Vietnamese food culture. Next, if I were you, I would take a boat trip to Cai Rang Floating Market early in the morning and visit Binh Thuy Ancient House. These are the most popular tourist attractions in Can Tho. Finally, remember to wear light clothes and comfortable shoes because you will walk and explore a lot. You should also bring a hat and sunglasses to protect yourself from the sunlight.\n\nI hope my advice will be helpful to you. Please let me know how everything turns out. Write back soon.\n\nBest wishes,`,
        sampleModelVi: `Emily thân mến,\n\nCảm ơn thư của cậu. Tớ hy vọng cậu vẫn khỏe. Tớ viết thư này để đưa ra một vài gợi ý cho chuyến đi của cậu đến Cần Thơ vào tháng Mười Hai.\n\nĐầu tiên, cậu nên ở một khách sạn gần Bến Ninh Kiều vì nó rất thuận tiện cho việc đi lại quanh thành phố. Ngoài ra, cậu có thể dễ dàng ghé thăm nhiều nhà hàng và quán cà phê nổi tiếng vào buổi tối. Thứ hai, cậu nên thử một số món ăn địa phương thơm ngon như bánh xèo, cá lóc nướng và trái cây nhiệt đới tươi. Những món ăn này rất nổi tiếng ở miền Tây và giúp cậu hiểu thêm về văn hóa ẩm thực Việt Nam. Tiếp theo, nếu tớ là cậu, tớ sẽ đi thuyền tham quan Chợ nổi Cái Răng vào sáng sớm và ghé thăm Nhà cổ Bình Thủy. Đây là những điểm du lịch nổi tiếng nhất ở Cần Thơ. Cuối cùng, hãy nhớ mặc quần áo mỏng nhẹ và đi giày thoải mái vì cậu sẽ đi bộ và khám phá rất nhiều. Cậu cũng nên mang theo mũ và kính râm để bảo vệ bản thân khỏi ánh nắng mặt trời.\n\nTớ hy vọng những lời khuyên của tớ sẽ giúp ích cho cậu. Hãy cho tớ biết chuyến đi diễn ra thế nào nhé. Hãy viết thư lại sớm nhé.\n\nChúc cậu mọi điều tốt lành,`,
        wordCount: 182
    }
};

function formatLetterParagraphs(str) {
    if (!str) return '';
    return str.split('\n\n').join('<br><br>').split('\n').join('<br>');
}

function renderExtraPracticePanel(typeId) {
    const container = document.getElementById('extraPracticePanel');
    if (!container) return;

    const data = extraPracticeData[typeId];
    if (!data) {
        container.innerHTML = `
            <div class="extra-practice-container">
                <div class="extra-prompt-box">
                    <div class="extra-prompt-header">
                        <span class="extra-prompt-title"><i class="fa-solid fa-pen-to-square"></i> BÀI LUYỆN TẬP THÊM</span>
                        <span class="extra-b1-badge">B1 LEVEL</span>
                    </div>
                    <div class="extra-prompt-body" style="text-align: center; padding: 40px 20px;">
                        <i class="fa-solid fa-clock-rotate-left" style="font-size: 36px; color: var(--text-muted); margin-bottom: 15px;"></i>
                        <h4 style="color: var(--text-main); margin-bottom: 8px;">Đề luyện tập thêm cho dạng thư này đang được cập nhật!</h4>
                        <p style="color: var(--text-muted); font-size: 14px;">Vui lòng chuyển qua <strong>DẠNG 01 (LETTER OF ADVICE)</strong> để trải nghiệm tính năng luyện tập & chấm điểm trực tiếp.</p>
                    </div>
                </div>
            </div>
        `;
        return;
    }

    let hintsHtml = '';
    data.hints.forEach(h => {
        let itemsHtml = '';
        h.items.forEach(it => {
            itemsHtml += `
                <div class="hint-item-card">
                    <div class="hint-item-en">↳ ${it.en}</div>
                    <div class="hint-item-vi">${it.vi}</div>
                    <div class="hint-item-reason">↳ ${it.reasonEn} (${it.reasonVi})</div>
                </div>
            `;
        });
        hintsHtml += `
            <div class="hint-section-block">
                <div class="hint-section-title"><i class="fa-solid fa-angles-right"></i> ${h.title}</div>
                <div class="hint-items-list">
                    ${itemsHtml}
                </div>
            </div>
        `;
    });

    let bulletsHtml = data.bulletPoints.map(b => `<li>${b}</li>`).join('');

    container.innerHTML = `
        <div class="extra-practice-container">
            <!-- Prompt Box -->
            <div class="extra-prompt-box">
                <div class="extra-prompt-header">
                    <span class="extra-prompt-title"><i class="fa-solid fa-file-pen"></i> ${data.title}</span>
                    <span class="extra-b1-badge">VSTEP B1 PRACTICE</span>
                </div>
                <div class="extra-prompt-body">
                    <p>You have received a letter from a friend, Emily. She is going to visit Can Tho in December. Write a letter to give her some suggestions. You should tell her:</p>
                    <ul>
                        ${bulletsHtml}
                    </ul>
                    <div class="extra-prompt-footer-note">
                        <i class="fa-solid fa-circle-info"></i> You should write at least <strong>120 words</strong>. Do not include your name. Your response will be evaluated in terms of Task Fulfillment, Organization, Vocabulary, and Grammar.
                    </div>
                </div>
            </div>

            <!-- Hints Toggle Card -->
            <div class="extra-hints-card">
                <button class="btn-toggle-hints" id="btnToggleHints">
                    <span><i class="fa-solid fa-lightbulb"></i> BẤM ĐỂ XEM GỢI Ý DÀN Ý & TỪ VỰNG CHI TIẾT</span>
                    <i class="fa-solid fa-chevron-down chevron-icon"></i>
                </button>
                <div class="hints-content hidden" id="extraHintsContent">
                    ${hintsHtml}
                </div>
            </div>

            <!-- Editor Card -->
            <div class="extra-editor-card">
                <div class="extra-editor-header">
                    <span class="extra-editor-title"><i class="fa-solid fa-keyboard"></i> KHUNG LÀM BÀI CỦA HỌC VIÊN</span>
                    <span class="extra-word-badge" id="extraWordBadge">0 / 120 words</span>
                </div>
                <textarea class="extra-textarea" id="extraWritingInput" placeholder="Nhập bài viết thư hoàn chỉnh của bạn tại đây (Bao gồm: Lời chào mở đầu, Mở bài, Thân bài 4 ý, Kết bài và Ký tên)..."></textarea>
                <div class="extra-editor-actions">
                    <button class="btn btn-secondary" id="btnClearExtraWriting">
                        <i class="fa-solid fa-rotate-left"></i> Viết lại
                    </button>
                    <button class="btn btn-primary" id="btnSubmitExtraWriting">
                        <i class="fa-solid fa-wand-magic-sparkles"></i> Nộp bài & Chấm điểm VSTEP (30%)
                    </button>
                </div>
            </div>

            <!-- Result & Evaluation Area (Hidden initially) -->
            <div class="extra-result-card hidden" id="extraResultCard">
                <!-- Injected after grading -->
            </div>
        </div>
    `;

    // Attach event listeners for extra practice
    const btnToggle = document.getElementById('btnToggleHints');
    const hintsContent = document.getElementById('extraHintsContent');
    if (btnToggle && hintsContent) {
        btnToggle.addEventListener('click', () => {
            hintsContent.classList.toggle('hidden');
            btnToggle.classList.toggle('expanded');
        });
    }

    const textarea = document.getElementById('extraWritingInput');
    const wordBadge = document.getElementById('extraWordBadge');
    if (textarea && wordBadge) {
        textarea.addEventListener('input', () => {
            const text = textarea.value.trim();
            const words = text ? text.split(/\s+/) : [];
            wordBadge.textContent = `${words.length} / 120 words`;
            if (words.length >= 120) {
                wordBadge.classList.add('valid');
            } else {
                wordBadge.classList.remove('valid');
            }
        });
    }

    const btnClear = document.getElementById('btnClearExtraWriting');
    if (btnClear && textarea) {
        btnClear.addEventListener('click', () => {
            if (textarea.value.trim() && !confirm('Bạn có chắc chắn muốn xóa bài viết để viết lại không?')) return;
            textarea.value = '';
            textarea.dispatchEvent(new Event('input'));
            const resultCard = document.getElementById('extraResultCard');
            if (resultCard) resultCard.classList.add('hidden');
        });
    }

    const btnSubmit = document.getElementById('btnSubmitExtraWriting');
    if (btnSubmit) {
        btnSubmit.addEventListener('click', () => gradeExtraPractice(typeId));
    }
}

function gradeExtraPractice(typeId) {
    const textarea = document.getElementById('extraWritingInput');
    const resultCard = document.getElementById('extraResultCard');
    if (!textarea || !resultCard) return;

    const rawText = textarea.value.trim();
    if (!rawText || rawText.split(/\s+/).length < 20) {
        alert('Vui lòng viết ít nhất một đoạn thư (tối thiểu 20 từ) trước khi nộp bài chấm điểm!');
        textarea.focus();
        return;
    }

    const words = rawText.split(/\s+/);
    const wordCount = words.length;
    const lower = rawText.toLowerCase();

    const errors = [];

    // =========================================================================
    // 1. ULTRA-DETAILED VSTEP TASK 1 ERROR DIAGNOSTIC RULES
    // =========================================================================

    // --- A. GREETINGS, OPENINGS & CLOSINGS ---
    if (/\bDear\s+[a-z]/g.test(rawText)) {
        const m = rawText.match(/\bDear\s+([a-z][a-zA-Z]*)/);
        if (m) {
            errors.push({
                type: "Chính tả / Viết hoa",
                category: "spelling",
                wrong: `Dear ${m[1]}`,
                correct: `Dear ${m[1].charAt(0).toUpperCase() + m[1].slice(1)},`,
                reason: `Tên riêng '${m[1]}' sau 'Dear' bắt buộc phải viết hoa chữ cái đầu và có dấu phẩy ở cuối.`
            });
        }
    }

    if (/\bDear\s+[A-Z][a-zA-Z]*\./g.test(rawText)) {
        errors.push({
            type: "Dấu câu (Punctuation)",
            category: "punctuation",
            wrong: "Dear [Name].",
            correct: "Dear [Name], (dùng dấu phẩy)",
            reason: "Lời chào đầu thư bằng tiếng Anh bắt buộc kết thúc bằng dấu phẩy (,), không dùng dấu chấm (.)."
        });
    }

    if (/\bThank\s+for\b/i.test(rawText)) {
        errors.push({
            type: "Ngữ pháp / Lời mở đầu",
            category: "grammar",
            wrong: "Thank for your letter",
            correct: "Thanks for your letter / Thank you for your letter",
            reason: "Cụm từ cảm ơn mở thư đúng ngữ pháp phải có 's' ('Thanks for...') hoặc dùng 'Thank you for...'."
        });
    }

    if (/\bThanks\s+you\s+for\b/i.test(rawText)) {
        errors.push({
            type: "Ngữ pháp / Lời mở đầu",
            category: "grammar",
            wrong: "Thanks you for",
            correct: "Thank you for / Thanks for",
            reason: "Không dùng 'Thanks you'. Chọn một trong hai: 'Thank you for...' hoặc 'Thanks for...'."
        });
    }

    if (/\b(i\s+am\s+write|i'm\s+write)\b/i.test(rawText)) {
        errors.push({
            type: "Ngữ pháp (Thì HTTD)",
            category: "grammar",
            wrong: "I am write / I'm write",
            correct: "I am writing / I'm writing",
            reason: "Cấu trúc thì hiện tại tiếp diễn: S + am/is/are + V-ing ('I am writing to...')."
        });
    }

    if (/\bI\s+write\s+this\s+letter\s+to\b/i.test(rawText)) {
        errors.push({
            type: "Cách diễn đạt mở thư",
            category: "vocab",
            wrong: "I write this letter to",
            correct: "I am writing this letter to / I am writing to",
            reason: "Trong thư tiếng Anh, chuẩn văn phong tự nhiên là dùng Hiện tại tiếp diễn: 'I am writing to give you some advice...'."
        });
    }

    if (/\bhope\s+you\s+well\b/i.test(rawText) && !/hope\s+you\s+are\s+well/i.test(rawText)) {
        errors.push({
            type: "Ngữ pháp (Thiếu động từ to be)",
            category: "grammar",
            wrong: "hope you well",
            correct: "I hope you are well / I hope you are doing well",
            reason: "Cần có động từ 'are' trước tính từ 'well': 'I hope you are well'."
        });
    }

    if (/\blook\s+forward\s+to\s+hear\b/i.test(rawText)) {
        errors.push({
            type: "Ngữ pháp (V-ing sau giới từ)",
            category: "grammar",
            wrong: "look forward to hear",
            correct: "look forward to hearing from you",
            reason: "Cấu trúc: 'look forward to + V-ing' ('look forward to hearing from you')."
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

    // --- B. ARTICLES (A / AN / THE / ZERO ARTICLE) ---
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

    const rSingularItems = /\b(wear|bring|take|buy|choose|visit|rent|book)\s+(ba\s*ba\s+shirt|shirt|dress|hat|jacket|camera|conical\s+hat|umbrella|raincoat|room|hotel|homestay|taxi|bus|boat|museum|market|temple|pagoda)\b/gi;
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

    if (/\bby\s+a\s+(bus|taxi|car|train|plane|boat)\b/gi.test(rawText)) {
        const m = rawText.match(/\bby\s+a\s+(bus|taxi|car|train|plane|boat)\b/i);
        if (m) {
            errors.push({
                type: "Mạo từ (Zero Article)",
                category: "article",
                wrong: m[0],
                correct: `by ${m[1]}`,
                reason: `Cụm từ 'by + phương tiện giao thông' không dùng mạo từ (ví dụ: by ${m[1]}).`
            });
        }
    }

    // --- C. UNCOUNTABLE NOUNS ---
    if (/\badvices\b/gi.test(rawText)) {
        errors.push({
            type: "Danh từ không đếm được",
            category: "grammar",
            wrong: "advices",
            correct: "some advice / advice",
            reason: "'advice' là danh từ không đếm được trong tiếng Anh, không được thêm 's'."
        });
    }
    if (/\ban\s+advice\b/gi.test(rawText)) {
        errors.push({
            type: "Danh từ không đếm được",
            category: "grammar",
            wrong: "an advice",
            correct: "a piece of advice / some advice",
            reason: "'advice' không dùng với mạo từ 'an'. Hãy dùng 'some advice' hoặc 'a piece of advice'."
        });
    }
    if (/\binformations\b/gi.test(rawText)) {
        errors.push({
            type: "Danh từ không đếm được",
            category: "grammar",
            wrong: "informations",
            correct: "information / some information",
            reason: "'information' là danh từ không đếm được, không có dạng số nhiều 'informations'."
        });
    }
    if (/\bclothings\b/gi.test(rawText)) {
        errors.push({
            type: "Danh từ không đếm được",
            category: "grammar",
            wrong: "clothings",
            correct: "clothes / clothing",
            reason: "'clothing' không thêm 's'. Muốn chỉ quần áo hãy dùng 'clothes'."
        });
    }

    // --- D. PARTS OF SPEECH & COLLOCATIONS ---
    if (/\bthe\s+cultural\s+of\b/gi.test(rawText)) {
        errors.push({
            type: "Từ loại (Part of Speech)",
            category: "word_form",
            wrong: "the cultural of Can Tho",
            correct: "the culture of Can Tho / the cultural identity of Can Tho",
            reason: "'cultural' là tính từ. Đứng sau mạo từ 'the' và trước 'of' bắt buộc phải dùng danh từ 'culture'."
        });
    }

    if (/\bvery\s+beauty\b/gi.test(rawText)) {
        errors.push({
            type: "Từ loại (Part of Speech)",
            category: "word_form",
            wrong: "very beauty",
            correct: "very beautiful",
            reason: "'beauty' là danh từ. Sau trạng từ chỉ mức độ 'very' cần dùng tính từ 'beautiful'."
        });
    }

    if (/\bdeliciously\s+food\b/gi.test(rawText)) {
        errors.push({
            type: "Từ loại (Part of Speech)",
            category: "word_form",
            wrong: "deliciously food",
            correct: "delicious food",
            reason: "Trước danh từ 'food' cần dùng tính từ 'delicious' để bổ nghĩa, không dùng trạng từ 'deliciously'."
        });
    }

    if (/\btradition\s+(dishes|food|culture|clothes)\b/gi.test(rawText)) {
        const m = rawText.match(/\btradition\s+(dishes|food|culture|clothes)\b/i);
        if (m) {
            errors.push({
                type: "Từ loại (Part of Speech)",
                category: "word_form",
                wrong: m[0],
                correct: `traditional ${m[1]}`,
                reason: `Trước danh từ '${m[1]}' cần dùng tính từ 'traditional' (truyền thống).`
            });
        }
    }

    if (/\bfame\s+(places|attractions|restaurants)\b/gi.test(rawText)) {
        const m = rawText.match(/\bfame\s+(places|attractions|restaurants)\b/i);
        if (m) {
            errors.push({
                type: "Từ loại (Part of Speech)",
                category: "word_form",
                wrong: m[0],
                correct: `famous ${m[1]}`,
                reason: `Cần dùng tính từ 'famous' (nổi tiếng) trước danh từ '${m[1]}'.`
            });
        }
    }

    if (/\bgive\s+you\s+some\s+advise\b/gi.test(rawText)) {
        errors.push({
            type: "Nhầm lẫn từ (Confusing words)",
            category: "word_form",
            wrong: "give you some advise",
            correct: "give you some advice",
            reason: "'advise' là động từ (khuyên), còn danh từ lời khuyên là 'advice' (đuôi -ce)."
        });
    }

    // Proper Noun & Collocations
    if (/\bNinh\s+Kieu\s+way\b/gi.test(rawText)) {
        errors.push({
            type: "Dùng từ / Địa danh",
            category: "vocab",
            wrong: "Ninh Kieu way",
            correct: "Ninh Kieu Wharf / Ninh Kieu Pedestrian Bridge",
            reason: "Địa danh Bến Ninh Kiều dùng 'Wharf', Cầu đi bộ dùng 'Pedestrian Bridge', không dùng 'way'."
        });
    }

    // --- E. ADVICE STRUCTURES & VERB PATTERNS ---
    if (/\bshould\s+to\s+[a-z]+/gi.test(rawText)) {
        errors.push({
            type: "Dạng động từ (Verb Form)",
            category: "grammar",
            wrong: "should to + V",
            correct: "should + Vo (không dùng 'to')",
            reason: "Sau modal verb 'should' dùng động từ nguyên mẫu không 'to'."
        });
    }

    if (/\bshould\s+(stays|visits|wears|eats|tries|goes)\b/gi.test(rawText)) {
        const m = rawText.match(/\bshould\s+(stays|visits|wears|eats|tries|goes)\b/i);
        if (m) {
            const vo = m[1].replace(/s$/, '');
            errors.push({
                type: "Dạng động từ (Verb Form)",
                category: "grammar",
                wrong: m[0],
                correct: `should ${vo}`,
                reason: `Sau 'should' luôn là động từ nguyên mẫu không chia 's/es' (should ${vo}).`
            });
        }
    }

    if (/\bwould\s+be\s+a\s+good\s+idea\s+(try|stay|visit|wear|go|eat|book)\b/gi.test(rawText)) {
        const m = rawText.match(/\bwould\s+be\s+a\s+good\s+idea\s+(try|stay|visit|wear|go|eat|book)\b/i);
        if (m) {
            errors.push({
                type: "Cấu trúc khuyên bảo (Advice)",
                category: "grammar",
                wrong: m[0],
                correct: `would be a good idea to ${m[1]}`,
                reason: `Cấu trúc chuẩn: 'It would be a good idea to + Vo' (cần có 'to').`
            });
        }
    }

    if (/\bif\s+i\s+was\s+you\b/gi.test(rawText)) {
        errors.push({
            type: "Câu điều kiện loại 2",
            category: "grammar",
            wrong: "If I was you",
            correct: "If I were you",
            reason: "Trong câu điều kiện loại 2 đưa ra lời khuyên, quy tắc ngữ pháp chuẩn dùng 'were' cho tất cả các ngôi (If I were you, I would...)."
        });
    }

    if (/\bif\s+i\s+were\s+you[,\s]+i\s+will\b/gi.test(rawText)) {
        errors.push({
            type: "Câu điều kiện loại 2",
            category: "grammar",
            wrong: "If I were you, I will",
            correct: "If I were you, I would",
            reason: "Mệnh đề chính của câu điều kiện loại 2 dùng 'would + Vo', không dùng 'will'."
        });
    }

    if (/\bremember\s+(wear|bring|take|try|visit|book|stay)\b/gi.test(rawText)) {
        const m = rawText.match(/\bremember\s+(wear|bring|take|try|visit|book|stay)\b/i);
        if (m) {
            errors.push({
                type: "Dạng động từ (Verb pattern)",
                category: "grammar",
                wrong: m[0],
                correct: `remember to ${m[1]}`,
                reason: `Cấu trúc nhắc nhở ai nhớ làm việc gì: 'Remember to + Vo'.`
            });
        }
    }

    if (/\bdon't\s+forget\s+(bring|wear|take|visit|try|book|stay)\b/gi.test(rawText)) {
        const m = rawText.match(/\bdon't\s+forget\s+(bring|wear|take|visit|try|book|stay)\b/i);
        if (m) {
            errors.push({
                type: "Dạng động từ (Verb pattern)",
                category: "grammar",
                wrong: m[0],
                correct: `don't forget to ${m[1]}`,
                reason: `Cấu trúc: 'Don't forget to + Vo'.`
            });
        }
    }

    if (/\bsuggest\s+you\s+to\b/gi.test(rawText)) {
        errors.push({
            type: "Cấu trúc động từ Suggest",
            category: "grammar",
            wrong: "suggest you to [V]",
            correct: "suggest that you should [V] / suggest [V-ing]",
            reason: "'suggest' không đi với tân ngữ + to-V (không dùng 'suggest you to'). Dùng 'suggest that you (should) + Vo' hoặc 'suggest + V-ing'."
        });
    }

    // --- F. PREPOSITIONS OF TIME & PLACE ---
    if (/\b(on\s+December|at\s+December)\b/gi.test(rawText)) {
        errors.push({
            type: "Giới từ chỉ thời gian",
            category: "preposition",
            wrong: "on December / at December",
            correct: "in December",
            reason: "Với tháng trong năm, bắt buộc dùng giới từ 'in' ('in December')."
        });
    }

    if (/\bin\s+(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\b/gi.test(rawText)) {
        const m = rawText.match(/\bin\s+(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\b/i);
        if (m) {
            errors.push({
                type: "Giới từ chỉ thời gian",
                category: "preposition",
                wrong: m[0],
                correct: `on ${m[1]}`,
                reason: `Với thứ trong tuần, bắt buộc dùng giới từ 'on' (on ${m[1]}).`
            });
        }
    }

    if (/\barrive\s+to\s+Can\s+Tho\b/gi.test(rawText)) {
        errors.push({
            type: "Giới từ (Preposition)",
            category: "preposition",
            wrong: "arrive to Can Tho",
            correct: "arrive in Can Tho",
            reason: "Đến một thành phố/quốc gia dùng 'arrive in', không dùng 'arrive to'."
        });
    }

    if (/\bfamous\s+with\b/gi.test(rawText)) {
        errors.push({
            type: "Giới từ đi với tính từ",
            category: "preposition",
            wrong: "famous with",
            correct: "famous for",
            reason: "Nổi tiếng vì điều gì dùng cấu trúc 'famous for', không dùng 'famous with'."
        });
    }

    // --- G. SENTENCE STRUCTURE & PARALLELISM ---
    if (/weather.*?can be.*?and an ideal time/gi.test(rawText)) {
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

    // Missing Comma after transition words
    const rTransitionNoComma = /(^|[.!?])\s*(Firstly|Secondly|Finally|Moreover|Besides|Furthermore|In addition|Therefore|For example|However)\s+([a-zA-Z])/gi;
    let mTrans;
    while ((mTrans = rTransitionNoComma.exec(rawText)) !== null) {
        errors.push({
            type: "Dấu câu (Punctuation)",
            category: "punctuation",
            wrong: `${mTrans[2]} ${mTrans[3]}`,
            correct: `${mTrans[2]}, ${mTrans[3]}`,
            reason: `Sau liên từ đầu câu '${mTrans[2]}' bắt buộc phải có dấu phẩy (,).`
        });
    }

    // --- H. SUBJECT - VERB AGREEMENT ---
    if (/\b(places|attractions|dishes|hotels|homestays|prices)\s+is\b/gi.test(rawText)) {
        const m = rawText.match(/\b(places|attractions|dishes|hotels|homestays|prices)\s+is\b/i);
        if (m) {
            errors.push({
                type: "Hòa hợp Chủ ngữ - Động từ",
                category: "grammar",
                wrong: m[0],
                correct: `${m[1]} are`,
                reason: `Chủ ngữ số nhiều '${m[1]}' đi với động từ to be số nhiều 'are', không dùng 'is'.`
            });
        }
    }

    // --- I. COMMON SPELLING ERRORS DICTIONARY ---
    const spellDict = {
        'recieve': 'receive',
        'untill': 'until',
        'beautifull': 'beautiful',
        'restuarant': 'restaurant',
        'resturant': 'restaurant',
        'delicous': 'delicious',
        'deliciouse': 'delicious',
        'traditionel': 'traditional',
        'conveniant': 'convenient',
        'intresting': 'interesting',
        'recommand': 'recommend',
        'cloths': 'clothes',
        'comfortible': 'comfortable',
        'pleasent': 'pleasant',
        'attact': 'attract',
        'attaction': 'attraction',
        'attractions': 'attractions',
        'floting': 'floating',
        'villige': 'village',
        'touristm': 'tourism',
        'adviced': 'advised',
        'helpfull': 'helpful',
        'alot': 'a lot',
        'seperate': 'separate',
        'tomorow': 'tomorrow',
        'truely': 'truly',
        'freind': 'friend',
        'exciteing': 'exciting',
        'specialy': 'specially / especially'
    };

    for (const [wrongSp, correctSp] of Object.entries(spellDict)) {
        const regexSp = new RegExp('\\b' + wrongSp + '\\b', 'gi');
        if (regexSp.test(rawText)) {
            errors.push({
                type: "Chính tả (Spelling)",
                category: "spelling",
                wrong: wrongSp,
                correct: correctSp,
                reason: `Lỗi chính tả từ '${wrongSp}'. Từ đúng chuẩn là '${correctSp}'.`
            });
        }
    }

    // Lowercase 'i' as pronoun
    if (/(^|[.\s])i\s+(hope|am|think|suggest|would|was|were|can|will|have)\b/g.test(rawText)) {
        errors.push({
            type: "Viết hoa đại từ 'I'",
            category: "spelling",
            wrong: "i [động từ]",
            correct: "I [viết hoa]",
            reason: "Đại từ nhân xưng ngôi thứ nhất 'I' (tôi) trong tiếng Anh luôn luôn phải viết hoa."
        });
    }

    // Punctuation Spacing Errors (e.g. "word.Word" or "word ,word")
    const punctSpacingErrors = rawText.match(/[a-zA-Z][,\.?!][a-zA-Z]/g);
    if (punctSpacingErrors && punctSpacingErrors.length > 0) {
        errors.push({
            type: "Dấu câu / Khoảng trắng",
            category: "punctuation",
            wrong: punctSpacingErrors.slice(0, 3).join(', '),
            correct: "Thêm dấu cách sau dấu câu",
            reason: "Cần có một dấu cách sau dấu phẩy (,), dấu chấm (.) hoặc dấu chấm hỏi (?)."
        });
    }

    // Space before punctuation: "word ,"
    if (/\s+[,.?!]/g.test(rawText)) {
        errors.push({
            type: "Dấu câu / Khoảng trắng",
            category: "punctuation",
            wrong: "Có dấu cách trước dấu câu (ví dụ: 'từ ,')",
            correct: "Đặt dấu câu liền ngay sau từ (ví dụ: 'từ,')",
            reason: "Không đặt khoảng trắng trước dấu phẩy, dấu chấm hay dấu hỏi."
        });
    }

    // =========================================================================
    // 2. VSTEP SCORING ON 10.0 SCALE (OFFICIAL VSTEP BAND CRITERIA)
    // =========================================================================

    // 1. Task Fulfilment (Thang 10)
    let tfScore = 8.0;
    const hasStay = /stay|hotel|homestay|ninh kieu|city cent|room|book|accommodat/.test(lower);
    const hasDishes = /dish|food|eat|try|banh|fish|fruit|noodle|soup|pork|spring roll|delicio|lau mam|banh cong/.test(lower);
    const hasAttractions = /visit|place|attraction|cai rang|market|floating|ninh kieu|wharf|ancient house|orchard|tour|my khanh/.test(lower);
    const hasWear = /wear|cloth|shoe|hat|sunglass|sunscreen|umbrella|jacket|weather|warm|hot|rain|ba ba/.test(lower);

    let coveredCount = [hasStay, hasDishes, hasAttractions, hasWear].filter(Boolean).length;
    if (coveredCount === 4) {
        tfScore = wordCount >= 140 ? 8.5 : (wordCount >= 120 ? 8.0 : 7.0);
    } else if (coveredCount === 3) {
        tfScore = 6.0;
    } else if (coveredCount === 2) {
        tfScore = 4.5;
    } else {
        tfScore = 3.0;
    }
    if (wordCount < 100) tfScore = Math.max(2.0, tfScore - 2.0);

    // 2. Organization (Thang 10)
    let orgScore = 8.0;
    const hasGreeting = /dear\s+[a-z]+/i.test(rawText);
    const hasOpening = /thank(s)?\s+for|hope you are doing well|give you some advice|writing to/i.test(rawText);
    const hasConnectors = /(firstly|secondly|next|finally|in addition|furthermore|moreover|besides|also)/gi.test(rawText);
    const hasClosing = /hope my advice|helpful|let me know|write back/i.test(rawText);
    const hasSignoff = /(best wishes|yours sincerely|warm regards|love)/i.test(rawText);

    let orgParts = [hasGreeting, hasOpening, hasConnectors, hasClosing, hasSignoff].filter(Boolean).length;
    if (orgParts === 5) {
        orgScore = 8.0;
    } else if (orgParts === 4) {
        orgScore = 7.0;
    } else {
        orgScore = 5.5;
    }

    // 3. Vocabulary (Thang 10)
    let vocScore = 7.5;
    const vocabErrors = errors.filter(e => e.category === 'vocab' || e.category === 'word_form');
    if (vocabErrors.length >= 3) {
        vocScore = 6.0;
    } else if (vocabErrors.length === 2) {
        vocScore = 6.5;
    } else if (vocabErrors.length === 1) {
        vocScore = 7.0;
    }
    if (wordCount < 120) vocScore = Math.max(4.0, vocScore - 1.0);

    // 4. Grammar (Thang 10)
    let gramScore = 8.0;
    const grammarErrors = errors.filter(e => e.category === 'grammar' || e.category === 'article' || e.category === 'preposition');
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

    // Quy đổi Thư (Task 1) chiếm 30% tổng điểm bài thi Writing (Thang 3.0 điểm)
    let convertedScore = Math.round((overallBand / 10.0) * 3.0 * 100) / 100;

    // Quy đổi 4 tiêu chí ra thang 0.75 điểm mỗi tiêu chí (0.75 x 4 = 3.00 điểm)
    let tfConv = Math.round((tfScore / 10.0) * 0.75 * 100) / 100;
    let orgConv = Math.round((orgScore / 10.0) * 0.75 * 100) / 100;
    let vocConv = Math.round((vocScore / 10.0) * 0.75 * 100) / 100;
    let gramConv = Math.round((gramScore / 10.0) * 0.75 * 100) / 100;

    let vstepLevel = "B1 LEVEL (ĐẠT CHUẨN)";
    let levelDesc = "Bài viết đáp ứng đầy đủ yêu cầu đề bài, cấu trúc đoạn rõ ràng. Tuy nhiên còn một số lỗi ngữ pháp, mạo từ và dùng từ cần lưu ý sửa chữa.";
    if (overallBand >= 8.5) {
        vstepLevel = "B2 LEVEL (XUẤT SẮC - VƯỢT CHUẨN)";
        levelDesc = "Bài viết rất ấn tượng! Bố cục chuẩn mực 5 bước, từ vựng và ngữ pháp khuyên bảo đa dạng, hầu như không có lỗi sai.";
    } else if (overallBand < 6.0) {
        vstepLevel = "DƯỚI CHUẨN B1 (CẦN CẢI THIỆN)";
        levelDesc = "Bài viết còn nhiều lỗi ngữ pháp hoặc chưa đủ số từ (yêu cầu ≥ 120 từ). Hãy xem kỹ bảng sửa lỗi và bài mẫu bên dưới nhé!";
    }

    const data = extraPracticeData[typeId];

    // Build Error Table HTML
    let errorTableHtml = '';
    if (errors.length > 0) {
        let rowsHtml = errors.map((err, idx) => `
            <tr>
                <td style="font-weight: 700; color: var(--primary-color); text-align: center;">${idx + 1}</td>
                <td><span class="err-badge-type">${err.type}</span></td>
                <td><span class="err-text-wrong">${err.wrong}</span></td>
                <td><span class="err-text-correct"><i class="fa-solid fa-arrow-right"></i> ${err.correct}</span></td>
                <td style="font-size: 13px; color: var(--text-main); line-height: 1.5;">${err.reason}</td>
            </tr>
        `).join('');

        errorTableHtml = `
            <div class="extra-error-table-wrapper">
                <div class="error-table-title">
                    <i class="fa-solid fa-triangle-exclamation" style="color: #ef4444;"></i>
                    DANH SÁCH ${errors.length} LỖI CẦN SỬA CHI TIẾT (NGỮ PHÁP, MẠO TỪ, TỪ LOẠI, DÙNG TỪ, CHÍNH TẢ):
                </div>
                <div class="table-responsive">
                    <table class="error-table">
                        <thead>
                            <tr>
                                <th style="width: 40px; text-align: center;">#</th>
                                <th style="width: 160px;">Phân loại lỗi</th>
                                <th style="width: 180px;">Học viên viết</th>
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
            <div class="extra-feedback-box" style="background: rgba(16, 185, 129, 0.08); border-color: rgba(16, 185, 129, 0.3);">
                <div class="feedback-title" style="color: #059669;">
                    <i class="fa-solid fa-circle-check"></i> Không phát hiện lỗi ngữ pháp hay chính tả đáng kể nào!
                </div>
                <p style="margin: 0; font-size: 14px; color: var(--text-main);">Bài làm của bạn rất chuẩn chỉnh và mạch lạc.</p>
            </div>
        `;
    }

    // Build Results HTML
    resultCard.innerHTML = `
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
                    ${hasStay ? '✓ Nơi ở ' : '✗ Nơi ở '}| 
                    ${hasDishes ? '✓ Món ăn ' : '✗ Món ăn '}| 
                    ${hasAttractions ? '✓ Điểm tham quan ' : '✗ Điểm tham quan '}| 
                    ${hasWear ? '✓ Trang phục' : '✗ Trang phục'}.
                    Độ dài: ${wordCount >= 120 ? 'Đạt chuẩn (≥120 từ)' : 'Chưa đủ từ'}.
                </div>
            </div>
            <div class="criterion-card">
                <div class="criterion-name">
                    <span>Organization (30%)</span>
                    <span class="criterion-score">${orgConv.toFixed(2)}/0.75 <small style="font-size: 11px; font-weight: normal; color: var(--text-muted);">(${orgScore.toFixed(1)}/10)</small></span>
                </div>
                <div class="criterion-desc">
                    Bố cục 5 phần hoàn chỉnh. Sử dụng linh hoạt các liên từ nối (Firstly, Secondly, Next, Finally, Moreover, Besides).
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
                    Áp dụng tốt cấu trúc khuyên bảo B1. ${totalGrammarCount > 0 ? `Bị trừ điểm do mắc ${totalGrammarCount} lỗi ngữ pháp/mạo từ/câu ghép.` : 'Ngữ pháp chuẩn xác.'}
                </div>
            </div>
        </div>

        <!-- Detailed Error Table -->
        ${errorTableHtml}

        <!-- Unlocked Sample Model Letter -->
        <div class="extra-model-wrapper">
            <div class="extra-model-title">
                <i class="fa-solid fa-award"></i> BÀI VIẾT MẪU CHUẨN B1 THAM KHẢO (MODEL LETTER)
            </div>
            <div class="extra-model-letter">
                ${formatLetterParagraphs(data.sampleModel)}
            </div>
            <div class="extra-model-trans">
                <strong>BẢN DỊCH CHI TIẾT:</strong><br><br>
                ${formatLetterParagraphs(data.sampleModelVi)}
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
    const typeObj = letterTypes.find(t => t.id === typeId);
    const typeTitle = typeObj ? typeObj.titleVi : typeId;
    const now = new Date().toLocaleString('vi-VN');

    const cleanSnippet = studentText.split('\n').join(' ').slice(0, 250);
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



function selectLetterType(id) {
    activeLetterTypeId = id;
    
    // Update active nav
    document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.remove('active');
        if (item.dataset.id === id) item.classList.add('active');
    });

    const typeData = letterTypes.find(t => t.id === id);
    if (!typeData) return;

    // Hide welcome, show content
    if (welcomeScreen) welcomeScreen.style.display = 'none';
    if (letterContent) letterContent.classList.remove('hidden');

    // Set Title
    if (mainTitle) {
        mainTitle.innerHTML = `
            <div class="main-title-en">${typeData.titleEn}</div>
            <div class="main-title-vi">${typeData.titleVi}</div>
        `;
    }

    // Populate Content
    const basicInfoPanel = document.getElementById('basicInfoPanel');
    const identifyingSignsPanel = document.getElementById('identifyingSignsPanel');
    const detailedOutlinePanel = document.getElementById('detailedOutlinePanel');
    const sampleWritingPanel = document.getElementById('sampleWritingPanel');

    if (basicInfoPanel) basicInfoPanel.innerHTML = typeData.basicInfo;
    if (identifyingSignsPanel) identifyingSignsPanel.innerHTML = typeData.identifyingSigns;
    if (detailedOutlinePanel) {
        detailedOutlinePanel.innerHTML = typeData.detailedOutline.replace(/\[([^\]]+)\]/g, '[<strong>$1</strong>]');
    }
    if (sampleWritingPanel) sampleWritingPanel.innerHTML = typeData.sampleWriting;

    // Render Extra Practice
    renderExtraPracticePanel(id);

    // Reset recitation for this type
    resetRecitationUI();

    // Reset tabs to first tab
    const firstTab = document.querySelector('.tab-btn[data-tab="basicInfo"]');
    if (firstTab) firstTab.click();
}

// --- Authentication & Student Profile Management ---
function initAuthSystem() {
    // Luôn luôn yêu cầu đăng nhập lại mỗi khi F5 hoặc mở lại trang web
    currentStudentName = '';
    currentStudentClass = '';
    updateStudentProfileUI('', '');
    openLoginModal();
}

function openLoginModal() {
    if (!loginModalOverlay) return;
    if (studentNameInput) studentNameInput.value = '';
    if (studentClassInput) studentClassInput.value = '';
    if (studentPasswordInput) studentPasswordInput.value = '';
    if (loginErrorMsg) loginErrorMsg.classList.add('hidden');
    loginModalOverlay.classList.remove('hidden');
    setTimeout(() => {
        if (studentNameInput) studentNameInput.focus();
    }, 150);
}

function handleLoginSubmit() {
    const nameVal = studentNameInput ? studentNameInput.value.trim() : '';
    const rawClassVal = studentClassInput ? studentClassInput.value.trim().toUpperCase().replace(/\s+/g, '') : '';
    const passwordVal = studentPasswordInput ? studentPasswordInput.value.trim().toUpperCase() : '';

    if (!nameVal || nameVal.length < 2) {
        showLoginError('Vui lòng điền đầy đủ Họ và tên.');
        if (studentNameInput) studentNameInput.focus();
        return;
    }

    const normalizedInputName = normalizeVietnameseString(nameVal);
    const matchedStudent = ALLOWED_STUDENT_NAMES.find(allowed => 
        normalizeVietnameseString(allowed) === normalizedInputName
    );

    if (!matchedStudent) {
        showLoginError('Họ và tên không thuộc danh sách học viên của lớp!');
        if (studentNameInput) studentNameInput.focus();
        return;
    }

    if (!rawClassVal || !ALLOWED_CLASSES.includes(rawClassVal)) {
        showLoginError('Lớp học không đúng. Vui lòng kiểm tra lại tên lớp!');
        if (studentClassInput) studentClassInput.focus();
        return;
    }

    if (passwordVal !== REQUIRED_PASSWORD) {
        showLoginError('Mật khẩu không chính xác!');
        if (studentPasswordInput) studentPasswordInput.focus();
        return;
    }

    currentStudentName = matchedStudent;
    currentStudentClass = rawClassVal;

    localStorage.setItem('vstep_student_name', currentStudentName);
    localStorage.setItem('vstep_student_class', currentStudentClass);
    localStorage.setItem('vstep_student_login_time', new Date().toISOString());

    updateStudentProfileUI(currentStudentName, currentStudentClass);

    // Gửi báo cáo đăng nhập ngay lập tức về Google Form
    const loginPayload = `[HỌC VIÊN ĐĂNG NHẬP]: ${currentStudentName} | [LỚP]: ${currentStudentClass} | [THỜI GIAN]: ${new Date().toLocaleString('vi-VN')}`;
    reportResultToGoogleForm(loginPayload);

    if (loginErrorMsg) loginErrorMsg.classList.add('hidden');
    if (loginModalOverlay) loginModalOverlay.classList.add('hidden');
}

function showLoginError(msg) {
    if (loginErrorText) loginErrorText.textContent = msg;
    if (loginErrorMsg) loginErrorMsg.classList.remove('hidden');
}

function updateStudentProfileUI(name, cls) {
    if (studentNameDisplay) studentNameDisplay.textContent = name || 'Chưa đăng nhập';
    if (studentClassDisplay) studentClassDisplay.textContent = cls ? `Lớp: ${cls}` : 'Lớp: --';

    if (greetingStudentName) greetingStudentName.textContent = name || 'Bạn';
    if (greetingStudentClass) greetingStudentClass.textContent = cls ? `Lớp ${cls}` : 'Lớp --';
}

// --- Google Form Reporting System ---
function reportResultToGoogleForm(customPayload) {
    const name = currentStudentName || localStorage.getItem('vstep_student_name') || 'Học viên';
    const cls = currentStudentClass || localStorage.getItem('vstep_student_class') || 'Chưa rõ';

    let payload = customPayload;
    if (!payload) {
        const typeData = letterTypes.find(t => t.id === activeLetterTypeId);
        const letterTitle = typeData ? `${typeData.titleEn} (${typeData.titleVi})` : 'VSTEP Task 1';
        const score = scorePercentageVal ? scorePercentageVal.textContent : '0';
        const status = resultStatusVal ? resultStatusVal.textContent : '';
        const now = new Date().toLocaleString('vi-VN');

        payload = `[KẾT QUẢ TRẢ BÀI]: ${name} | [LỚP]: ${cls} | [DẠNG BÀI]: ${letterTitle} | [ĐIỂM]: ${score}% (${status}) | [THỜI GIAN]: ${now}`;
    }

    console.log("Submitting result report to Google Form:", payload);

    if (reportStatusBox) reportStatusBox.classList.remove('hidden');
    if (reportStatusIcon) {
        reportStatusIcon.className = 'fa-solid fa-spinner fa-spin report-status-icon';
    }
    if (reportStatusText) {
        reportStatusText.textContent = 'Đang gửi kết quả lên hệ thống của giáo viên...';
    }

    // Method 1: Submit via Hidden Form & Iframe (Most reliable across all browsers)
    try {
        let form = document.getElementById('gform_hidden_form');
        let input = document.getElementById('gform_hidden_input');

        if (!form) {
            let iframe = document.getElementById('gform_hidden_iframe');
            if (!iframe) {
                iframe = document.createElement('iframe');
                iframe.id = 'gform_hidden_iframe';
                iframe.name = 'gform_hidden_iframe';
                iframe.style.display = 'none';
                document.body.appendChild(iframe);
            }

            form = document.createElement('form');
            form.id = 'gform_hidden_form';
            form.action = GOOGLE_FORM_ACTION_URL;
            form.method = 'POST';
            form.target = 'gform_hidden_iframe';
            form.style.display = 'none';

            input = document.createElement('input');
            input.type = 'hidden';
            input.name = GOOGLE_FORM_ENTRY_ID;
            input.id = 'gform_hidden_input';
            form.appendChild(input);

            const fvvInput = document.createElement('input');
            fvvInput.type = 'hidden';
            fvvInput.name = 'fvv';
            fvvInput.value = '1';
            form.appendChild(fvvInput);

            const pageHistInput = document.createElement('input');
            pageHistInput.type = 'hidden';
            pageHistInput.name = 'pageHistory';
            pageHistInput.value = '0';
            form.appendChild(pageHistInput);

            document.body.appendChild(form);
        }

        if (input && form) {
            input.value = payload;
            form.submit();
            console.log("Submitted via hidden form successfully.");
        }
    } catch (e) {
        console.log('Iframe submit error:', e);
    }

    // Method 2: Fetch POST (no-cors)
    try {
        const formData = new URLSearchParams();
        formData.append(GOOGLE_FORM_ENTRY_ID, payload);
        formData.append('fvv', '1');
        formData.append('pageHistory', '0');

        fetch(GOOGLE_FORM_ACTION_URL, {
            method: 'POST',
            mode: 'no-cors',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: formData.toString()
        }).catch(err => console.log('Handled fetch status:', err));
    } catch (e) {
        console.log('Fetch exception:', e);
    }

    // Method 3: Navigator sendBeacon fallback
    try {
        if (navigator.sendBeacon) {
            const beaconData = new FormData();
            beaconData.append(GOOGLE_FORM_ENTRY_ID, payload);
            beaconData.append('fvv', '1');
            beaconData.append('pageHistory', '0');
            navigator.sendBeacon(GOOGLE_FORM_ACTION_URL, beaconData);
        }
    } catch (e) {
        console.log('Beacon exception:', e);
    }

    setTimeout(() => {
        if (reportStatusIcon) {
            reportStatusIcon.className = 'fa-solid fa-circle-check report-status-icon';
        }
        if (reportStatusText) {
            reportStatusText.innerHTML = `Đã tự động báo cáo kết quả của học viên <strong>${name}</strong> (<strong>${cls}</strong>) lên hệ thống!`;
        }
    }, 700);
}

// Initialize application on DOM ready
document.addEventListener('DOMContentLoaded', () => {
    // Query DOM Elements
    letterNav = document.getElementById('letterNav');
    mainTitle = document.getElementById('mainTitle');
    welcomeScreen = document.getElementById('welcomeScreen');
    letterContent = document.getElementById('letterContent');
    themeToggle = document.getElementById('themeToggle');

    // Query Auth Elements
    loginModalOverlay = document.getElementById('loginModalOverlay');
    studentNameInput = document.getElementById('studentNameInput');
    studentClassInput = document.getElementById('studentClassInput');
    studentPasswordInput = document.getElementById('studentPasswordInput');
    btnLoginSubmit = document.getElementById('btnLoginSubmit');
    loginErrorMsg = document.getElementById('loginErrorMsg');
    loginErrorText = document.getElementById('loginErrorText');

    studentProfileCard = document.getElementById('studentProfileCard');
    studentNameDisplay = document.getElementById('studentNameDisplay');
    studentClassDisplay = document.getElementById('studentClassDisplay');
    btnEditStudent = document.getElementById('btnEditStudent');

    questStudentGreeting = document.getElementById('questStudentGreeting');
    greetingStudentName = document.getElementById('greetingStudentName');
    greetingStudentClass = document.getElementById('greetingStudentClass');

    reportStatusBox = document.getElementById('reportStatusBox');
    reportStatusIcon = document.getElementById('reportStatusIcon');
    reportStatusText = document.getElementById('reportStatusText');
    btnResendReport = document.getElementById('btnResendReport');

    // Query Recitation Elements
    recitationInput = document.getElementById('recitationInput');
    btnPrevQuestion = document.getElementById('btnPrevQuestion');
    btnShowAnswer = document.getElementById('btnShowAnswer');
    btnCheckAnswer = document.getElementById('btnCheckAnswer');
    btnNextQuestion = document.getElementById('btnNextQuestion');
    currentQuestionNum = document.getElementById('currentQuestionNum');
    totalQuestionsNum = document.getElementById('totalQuestionsNum');
    progressBarFill = document.getElementById('progressBarFill');
    questionCueText = document.getElementById('questionCueText');
    recitationFeedback = document.getElementById('recitationFeedback');
    feedbackStatus = document.getElementById('feedbackStatus');
    userDiffResult = document.getElementById('userDiffResult');
    correctTextResult = document.getElementById('correctTextResult');
    questionHintBox = document.getElementById('questionHintBox');
    questionHintText = document.getElementById('questionHintText');

    // Query Evaluation Elements
    recitationQuizBox = document.getElementById('recitationQuizBox');
    recitationResultBox = document.getElementById('recitationResultBox');
    scorePercentageVal = document.getElementById('scorePercentageVal');
    resultStatusVal = document.getElementById('resultStatusVal');
    resultMessageVal = document.getElementById('resultMessageVal');
    btnRestartRecitation = document.getElementById('btnRestartRecitation');
    evaluationIcon = document.getElementById('evaluationIcon');

    // Render navigation
    renderNav();

    // Update global progress on load
    updateGlobalProgress();

    // Initialize Student Authentication
    initAuthSystem();

    // Auth Listeners
    if (btnLoginSubmit) btnLoginSubmit.addEventListener('click', handleLoginSubmit);
    if (btnEditStudent) btnEditStudent.addEventListener('click', openLoginModal);
    if (studentNameInput) {
        studentNameInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') handleLoginSubmit();
        });
    }
    if (studentClassInput) {
        studentClassInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') handleLoginSubmit();
        });
    }
    if (studentPasswordInput) {
        studentPasswordInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') handleLoginSubmit();
        });
    }
    if (btnResendReport) {
        btnResendReport.addEventListener('click', () => reportResultToGoogleForm());
    }

    // Reset progress button listener
    const btnResetProgress = document.getElementById('btnResetProgress');
    if (btnResetProgress) btnResetProgress.addEventListener('click', resetLearningProgress);

    // Handle Tabs
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            // Remove active class from all buttons and panels
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));

            // Add active class to clicked button
            e.currentTarget.classList.add('active');

            // Show corresponding panel
            const tabId = e.currentTarget.dataset.tab;
            const panel = document.getElementById(`${tabId}Panel`);
            if (panel) panel.classList.add('active');
        });
    });

    // Recitation Button Listeners
    if (btnPrevQuestion) btnPrevQuestion.addEventListener('click', prevRecitationQuestion);
    if (btnShowAnswer) btnShowAnswer.addEventListener('click', showRecitationAnswer);
    if (btnCheckAnswer) btnCheckAnswer.addEventListener('click', checkRecitationAnswer);
    if (btnNextQuestion) btnNextQuestion.addEventListener('click', nextRecitationQuestion);
    if (btnRestartRecitation) btnRestartRecitation.addEventListener('click', resetRecitationUI);

    // Theme Toggle
    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            isDarkMode = !isDarkMode;
            if (isDarkMode) {
                document.documentElement.setAttribute('data-theme', 'dark');
                themeToggle.innerHTML = '<i class="fa-solid fa-sun"></i>';
            } else {
                document.documentElement.removeAttribute('data-theme');
                themeToggle.innerHTML = '<i class="fa-solid fa-moon"></i>';
            }
        });
    }
});
