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


const recitationQuestions = {
advice: [
{
cue: "Viết lời chào mở đầu thân mật: 'Kính gửi [tên của người nhận],'",
target: "Dear [tên của người nhận],"
},
{
cue: "Viết câu mở thư khuyên bảo thân mật: 'Cảm ơn thư của cậu. Tớ hy vọng cậu vẫn khỏe. Tớ viết thư này để đưa ra một vài lời khuyên về tình huống của cậu.'",
target: "Thanks for your letter. I hope you are doing well. I’m writing to give you some advice about your situation."
},
{
cue: "Viết cấu trúc đưa ra lời khuyên số 1: 'Bạn nên + Vo.'",
target: "You should + Vo."
},
{
cue: "Viết cấu trúc đưa ra lời khuyên số 2: 'Sẽ là một ý kiến hay nếu + Vo.'",
target: "It would be a good idea to + Vo."
},
{
cue: "Viết cấu trúc đưa ra lời khuyên số 3: 'Nếu tôi là bạn, tôi sẽ + Vo.'",
target: "If I were you, I would + Vo."
},
{
cue: "Viết cấu trúc đưa ra lời khuyên số 4: 'Bạn có thể thử + Ving.'",
target: "You can try + Ving."
},
{
cue: "Viết cấu trúc đưa ra lời khuyên số 5: 'Hãy nhớ + Vo. / Đừng quên + Vo.'",
target: "Remember to + Vo. / Don’t forget to + Vo."
},
{
cue: "Viết câu kết thư: 'Tớ hy vọng những lời khuyên của tớ sẽ giúp ích cho cậu. Hãy cho tớ biết chuyến đi diễn ra thế nào nhé. Hãy viết thư lại sớm nhé.'",
target: "I hope my advice will be helpful to you. Please let me know how everything turns out. Write back soon."
},
{
cue: "Viết lời chào kết thúc thân mật: 'Lời chúc tốt đẹp nhất,'",
target: "Best wishes,"
}
],
request: [
{
cue: "Viết câu mở thư yêu cầu (Thân mật): 'Cậu khỏe không? Tớ hy vọng cậu vẫn khỏe. Tớ viết thư này để hỏi một vài thông tin về [thứ cần xin thông tin] vì [lý do].'",
target: "How are you? I hope you are doing well. I’m writing to ask for some information about [thứ cần xin thông tin] because [lý do]."
},
{
cue: "Viết câu mở thư yêu cầu (Trang trọng & Bán trang trọng): 'Tôi viết thư này để yêu cầu một số thông tin về [thứ cần xin thông tin] vì [lý do].'",
target: "I am writing to request some information about [thứ cần xin thông tin] because [lý do]."
},
{
cue: "Viết cấu trúc xin thông tin thân mật 1: 'Bạn có thể cho tôi thêm thông tin về...?'",
target: "Can you give me more information about …?"
},
{
cue: "Viết cấu trúc xin thông tin thân mật 2: 'Bạn có thể nói cho tôi biết thêm về...?'",
target: "Can you tell me more about …?"
},
{
cue: "Viết cấu trúc xin thông tin thân mật 3: 'Bạn có thể cho tôi biết thêm về...?'",
target: "Can you let me know more about …?"
},
{
cue: "Viết cấu trúc xin thông tin thân mật 4: 'Tôi muốn biết thêm về...'",
target: "I want to know more about …"
},
{
cue: "Viết cấu trúc xin thông tin thân mật 5: 'Tôi muốn có thêm thông tin về...'",
target: "I want more information about …"
},
{
cue: "Viết cấu trúc xin thông tin trang trọng 1: 'Bạn có thể cung cấp thêm thông tin...?'",
target: "Could you provide me with more information about …?"
},
{
cue: "Viết cấu trúc xin thông tin trang trọng 2: 'Bạn có thể cho tôi biết thêm chi tiết...?'",
target: "Could you give me more details about …?"
},
{
cue: "Viết cấu trúc xin thông tin trang trọng 3: 'Tôi muốn biết thêm về...'",
target: "I would like to know more about …"
},
{
cue: "Viết cấu trúc xin thông tin trang trọng 4: 'Tôi muốn hỏi thăm về...'",
target: "I would like to inquire about …"
},
{
cue: "Viết cấu trúc xin thông tin trang trọng 5: 'Tôi cũng đang băn khoăn về...'",
target: "I am also wondering about …"
},
{
cue: "Viết câu kết thư (Thân mật): 'Tớ hy vọng cậu có thể giúp tớ việc này. Hãy trả lời thư sớm nhé.'",
target: "I hope you can help me with this. Write back soon."
},
{
cue: "Viết câu kết thư (Trang trọng & Bán trang trọng): 'Cảm ơn vì thời gian của ông/bà. Tôi rất mong đợi phản hồi từ ông/bà.'",
target: "Thank you for your time. I look forward to your reply."
}
],
description: [
{
cue: "Viết câu mở đầu khi thư yêu cầu CUNG CẤP THÔNG TIN (Thân mật): 'Cậu khỏe không? Tớ hy vọng cậu vẫn khỏe. Trong thư của cậu, cậu đã hỏi tớ về [thứ cần mô tả thông tin], vì vậy dưới đây là một số thông tin.'",
target: "How are you? I hope you are doing well. In your letter, you asked me about [thứ cần mô tả thông tin], so here is some information."
},
{
cue: "Viết câu mở đầu khi thư yêu cầu CUNG CẤP THÔNG TIN (Trang trọng & Bán trang trọng): 'Trong thư của ông/bà, ông/bà đã hỏi tôi về [thứ cần mô tả thông tin], vì vậy tôi viết thư này để cung cấp cho ông/bà một số thông tin.'",
target: "In your letter, you asked me about [thứ cần mô tả thông tin], so I am writing to provide you with some information."
},
{
cue: "Viết câu mở đầu khi thư yêu cầu MÔ TẢ MỘT ĐỐI TƯỢNG (Thân mật): 'Cậu khỏe không? Tớ hy vọng cậu vẫn khỏe. Trong thư của cậu, cậu đã hỏi tớ mô tả [thứ cần mô tả], vì vậy dưới đây là một số chi tiết.'",
target: "How are you? I hope you are doing well. In your letter, you asked me to describe [thứ cần mô tả], so here are some details."
},
{
cue: "Viết câu mở đầu khi thư yêu cầu MÔ TẢ MỘT ĐỐI TƯỢNG (Trang trọng & Bán trang trọng): 'Trong thư của ông/bà, ông/bà đã hỏi tôi mô tả [thứ cần mô tả], vì vậy tôi viết thư này để cung cấp cho ông/bà một số chi tiết.'",
target: "In your letter, you asked me to describe [thứ cần mô tả], so I am writing to provide you with some details."
},
{
cue: "Viết câu kết thư mô tả (Thân mật): 'Tớ hy vọng cậu sẽ thấy những thông tin này hữu ích. Hãy cho tớ biết nếu cậu cần thêm chi tiết nhé.'",
target: "I hope you will find this information useful. Let me know if you need more details."
},
{
cue: "Viết câu kết thư mô tả (Trang trọng & Bán trang trọng): 'Tôi hy vọng thông tin trên sẽ giúp ích cho ông/bà. Xin vui lòng liên hệ với tôi nếu ông/bà cần thêm chi tiết.'",
target: "I hope the information above will be helpful to you. Please feel free to contact me if you need more details."
}
],
complaint: [
{
cue: "Viết câu mở thư phàn nàn: 'Tôi viết thư này để phàn nàn về [vấn đề cần phàn nàn]. Gần đây tôi đã sử dụng [sản phẩm/dịch vụ] của ông/bà và không hài lòng với nó.'",
target: "I am writing to complain about [vấn đề cần phàn nàn]. I recently used your [sản phẩm/dịch vụ] and was not satisfied with it."
},
{
cue: "Viết câu nêu vấn đề chính trong Thân thư 1: 'Vấn đề chính là [vấn đề 1].'",
target: "The main problem was that [vấn đề 1]."
},
{
cue: "Viết câu nêu vấn đề phụ thứ hai trong Thân thư 1: 'Một vấn đề khác là [vấn đề 2].'",
target: "Another issue was that [vấn đề 2]."
},
{
cue: "Viết câu nêu vấn đề phụ thứ ba trong Thân thư 1: 'Cuối cùng, tôi cũng nhận thấy [vấn đề 3].'",
target: "Finally, I also found that [vấn đề 3]."
},
{
cue: "Viết câu bày tỏ cảm xúc & đề xuất giải pháp trong Thân thư 2: 'Tôi rất thất vọng / khá không vui với các vấn đề này. Do đó, tôi sẽ rất cảm kích nếu ông/bà có thể [giải pháp cụ thể để giải quyết vấn đề].'",
target: "I was very disappointed / quite unhappy with these problems. Therefore, I would appreciate it if you could [giải pháp cụ thể để giải quyết vấn đề]."
},
{
cue: "Viết câu kết thư yêu cầu xem xét vấn đề: 'Tôi hy vọng ông/bà sẽ sớm xem xét các vấn đề này.'",
target: "I hope that you will look into these issues soon."
},
{
cue: "Viết câu kết thư thể hiện sự mong chờ phản hồi: 'Tôi rất mong sớm nhận được phản hồi từ ông/bà.'",
target: "I look forward to receiving your reply soon."
}
],
feedback: [
{
cue: "Viết câu mở thư phản hồi: 'Tôi viết thư này để đưa ra phản hồi về [vấn đề cần phản hồi đánh giá]. Gần đây tôi đã sử dụng [sản phẩm/dịch vụ] của ông/bà và muốn chia sẻ trải nghiệm của mình.'",
target: "I am writing to give you feedback on [vấn đề cần phản hồi đánh giá]. I recently used your [sản phẩm/dịch vụ] and would like to share my experience."
},
{
cue: "Viết câu dẫn dắt điểm khen: 'Trước hết, tôi muốn đề cập đến một số điểm tích cực về [sản phẩm/dịch vụ] của ông/bà.'",
target: "First of all, I would like to mention some positive points about your [sản phẩm/dịch vụ]."
},
{
cue: "Viết cấu trúc khen số 1 (satisfied): 'Tôi rất hài lòng với [điểm khen] vì [lý do].'",
target: "I was very satisfied with [điểm khen] because [lý do]."
},
{
cue: "Viết cấu trúc khen số 2 (liked): 'Tôi thực sự thích [điểm khen] vì [lý do].'",
target: "I really liked [điểm khen] because [lý do]."
},
{
cue: "Viết cấu trúc khen số 3 (impressed): 'Tôi đã ấn tượng với [điểm khen] vì [lý do].'",
target: "I was impressed with [điểm khen] as [lý do]."
},
{
cue: "Viết cấu trúc khen số 4 (liked most): 'Một điều tôi thích nhất là [điểm khen] vì [lý do].'",
target: "One thing I liked most was [điểm khen] since [lý do]."
},
{
cue: "Viết câu dẫn dắt điểm chê: 'Tuy nhiên, cũng có một số khía cạnh cần được cải thiện.'",
target: "However, there were also some areas that needed improvement."
},
{
cue: "Viết cấu trúc chê số 1 (disappointed): 'Tôi thấy thất vọng về [điểm chê] vì [lý do].'",
target: "I was disappointed with [điểm chê] because [lý do]."
},
{
cue: "Viết cấu trúc chê số 2 (thing that disappointed me): 'Một điều làm tôi thất vọng là [điểm chê] vì [lý do].'",
target: "One thing that disappointed me was [điểm chê] since [lý do]."
},
{
cue: "Viết cấu trúc chê số 3 (not satisfied): 'Tôi đã không hài lòng với [điểm chê] vì [lý do].'",
target: "I was not satisfied with [điểm chê] as [lý do]."
},
{
cue: "Viết cấu trúc chê số 4 (quality of): 'Chất lượng của [điểm chê] không tốt như tôi kỳ vọng vì [lý do].'",
target: "The quality of [điểm chê] was not as good as I expected because [lý do]."
},
{
cue: "Viết câu dẫn dắt đề xuất gợi ý: 'Để nâng cao chất lượng [sản phẩm/dịch vụ] của ông/bà, tôi có một vài gợi ý.'",
target: "To enhance the quality of your [sản phẩm/dịch vụ], I have a few suggestions."
},
{
cue: "Viết cấu trúc gợi ý số 1 (suggest that you should): 'Tôi đề nghị rằng ông/bà nên [hành động – Vo].'",
target: "I suggest that you should [hành động – Vo]."
},
{
cue: "Viết cấu trúc gợi ý số 2 (think you should): 'Tôi nghĩ ông/bà nên [hành động – Vo].'",
target: "I think you should [hành động – Vo]."
},
{
cue: "Viết cấu trúc gợi ý số 3 (better if you could): 'Sẽ tốt hơn nếu ông/bà có thể [hành động – Vo].'",
target: "It would be better if you could [hành động – Vo]."
},
{
cue: "Viết cấu trúc gợi ý số 4 (hope you will consider): 'Tôi hy vọng ông/bà sẽ cân nhắc [hành động – Ving].'",
target: "I hope you will consider [hành động – Ving]."
},
{
cue: "Viết câu kết thư phản hồi: 'Tôi hy vọng phản hồi của mình sẽ giúp ông/bà cải thiện [sản phẩm/dịch vụ]. Xin vui lòng liên hệ với tôi nếu có thêm câu hỏi nào.'",
target: "I hope my feedback will help you improve your [sản phẩm/dịch vụ]. Please feel free to contact me if you have any further questions."
}
],
apology: [
{
cue: "Viết câu mở thư xin lỗi (Thân mật): 'Tớ thực sự xin lỗi vì [vấn đề cần xin lỗi]. Hãy để tớ giải thích những gì đã xảy ra để cậu hiểu rõ tình hình nhé.'",
target: "I’m really sorry for [vấn đề cần xin lỗi]. Let me explain what happened so you can understand the situation."
},
{
cue: "Viết câu mở thư xin lỗi (Trang trọng & Bán trang trọng): 'Tôi viết thư này để xin lỗi vì [vấn đề cần xin lỗi]. Tôi hiểu rằng điều này có thể gây ra một số bất tiện, và tôi muốn giải thích tình hình.'",
target: "I am writing to apologize for [vấn đề cần xin lỗi]. I understand that this may have caused some inconvenience, and I would like to explain the situation."
},
{
cue: "Viết câu dẫn dắt lý do thân mật: 'Trước hết, hãy để tớ giải thích tại sao chuyện này lại xảy ra.'",
target: "First of all, let me explain why this happened."
},
{
cue: "Viết cấu trúc lý do thân mật 1 (couldn't): 'Tớ thực sự xin lỗi vì tớ đã không thể [hành động – Vo] vì [lý do].'",
target: "I’m really sorry that I couldn’t [hành động – Vo] because [lý do]."
},
{
cue: "Viết cấu trúc lý do thân mật 2 (missed): 'Tớ đã bỏ lỡ [sự kiện] vì [lý do].'",
target: "I missed [sự kiện] because [lý do]."
},
{
cue: "Viết cấu trúc lý do thân mật 3 (felt bad about not): 'Tớ cảm thấy tệ vì đã không [hành động – Ving] vì [lý do].'",
target: "I felt bad about not [hành động – Ving] because [lý do]."
},
{
cue: "Viết cấu trúc lý do thân mật 4 (didn't mean to): 'Tớ không cố ý [hành động – Vo], nhưng [lý do].'",
target: "I didn’t mean to [hành động – Vo], but [lý do]."
},
{
cue: "Viết câu dẫn dắt lý do trang trọng: 'Trước hết, tôi muốn giải thích tại sao điều này lại xảy ra.'",
target: "First of all, I would like to explain why this happened."
},
{
cue: "Viết cấu trúc lý do trang trọng 1 (unable to): 'Tôi đã không thể [hành động – Vo] vì [lý do].'",
target: "I was unable to [hành động – Vo] because [lý do]."
},
{
cue: "Viết cấu trúc lý do trang trọng 2 (regret that): 'Tôi lấy làm tiếc vì tôi đã không thể [hành động – Vo] vì [lý do].'",
target: "I regret that I was unable to [hành động – Vo] because [lý do]."
},
{
cue: "Viết cấu trúc lý do trang trọng 3 (because..., unable to): 'Vì [lý do], tôi đã không thể [hành động – Vo].'",
target: "Because [lý do], I was unable to [hành động – Vo]."
},
{
cue: "Viết cấu trúc lý do trang trọng 4 (unfortunately): 'Thật không may, tôi không thể [hành động – Vo] vì [lý do].'",
target: "Unfortunately, I could not [hành động – Vo] because [lý do]."
},
{
cue: "Viết cấu trúc đền bù thân mật: 'Cuối cùng, hãy để tớ bù đắp cho cậu bằng cách [hành động – Ving].'",
target: "Finally, let me make it up to you by [hành động – Ving]."
},
{
cue: "Viết cấu trúc đền bù trang trọng: 'Để bù đắp cho lỗi của mình, tôi muốn [hành động – Vo].'",
target: "To make up for my mistake, I would like to [hành động – Vo]."
},
{
cue: "Viết câu kết thư xin lỗi thân mật: 'Xin lỗi cậu một lần nữa nhé. Tớ rất trân trọng việc cậu đã dành thời gian đọc thư này. Hãy viết thư lại cho tớ sớm nhé.'",
target: "Sorry once again. Thanks for taking the time to read this. Write back soon."
},
{
cue: "Viết câu kết thư xin lỗi trang trọng: 'Tôi muốn xin lỗi một lần nữa vì sự bất tiện này. Cảm ơn vì đã dành thời gian đọc thư của tôi. Tôi rất mong nhận được hồi âm sớm.'",
target: "I would like to apologize once again for the inconvenience. Thank you for taking the time to read my letter. I look forward to receiving your reply soon."
}
],
application: [
{
cue: "Viết câu mở thư ứng tuyển: 'Tôi viết thư này để ứng tuyển vào vị trí [vị trí công việc] được quảng cáo trên/trong [nguồn tuyển dụng].'",
target: "I am writing to apply for the position of [vị trí công việc] which was advertised on/in [nguồn tuyển dụng]."
},
{
cue: "Viết câu bày tỏ hứng thú với công việc: 'Tôi rất hứng thú với vị trí này vì nó phù hợp với sở thích và mục tiêu nghề nghiệp của tôi. Ngoài ra, tôi thích [hoạt động liên quan đến công việc]. Vì vậy, tôi tin rằng công việc này sẽ mang lại cho tôi cơ hội tốt để áp dụng những gì đã học trong quá trình học và tích lũy thêm kinh nghiệm thực tế.'",
target: "I am very interested in this position because it matches my interests and career goals. In addition, I enjoy [hoạt động liên quan đến công việc]. Therefore, I believe this job will give me a good opportunity to apply what I have learned during my studies and gain practical experience."
},
{
cue: "Viết câu trình bày học vấn & chuyên môn: 'Tôi vừa tốt nghiệp từ [tên trường] với tấm bằng cử nhân ngành [chuyên ngành]. Trong quá trình học, tôi đã phát triển sự hiểu biết sâu sắc về [lĩnh vực]. Tôi cũng tích lũy được những kiến thức và năng lực hữu ích như [kiến thức/năng lực học thuật 1] và [kiến thức/năng lực học thuật 2].'",
target: "I recently graduated from [tên trường] with a bachelor’s degree in [chuyên ngành]. During my studies, I developed a strong understanding of [lĩnh vực]. I also gained useful knowledge and abilities such as [kiến thức/năng lực học thuật 1] and [kiến thức/năng lực học thuật 2]."
},
{
cue: "Viết câu trình bày kinh nghiệm làm việc: 'Tôi đã từng làm việc bán thời gian với tư cách là [vị trí công việc] tại [nơi làm việc]. Trong công việc này, tôi chịu trách nhiệm về [nhiệm vụ]. Kinh nghiệm này đã giúp tôi phát triển các kỹ năng như [kỹ năng mềm 1] và [kỹ năng mềm 2].'",
target: "I worked part-time as a [vị trí công việc] at [nơi làm việc]. In this job, I was responsible for [nhiệm vụ]. This experience helped me develop skills such as [kỹ năng mềm 1] and [kỹ năng mềm 2]."
},
{
cue: "Viết câu khẳng định ứng viên phù hợp: 'Tôi tin rằng mình sẽ là ứng cử viên phù hợp cho vị trí này. Điều này là vì tôi là người [đặc điểm tính cách]. Hơn nữa, tôi rất ham học hỏi và có thể thích nghi nhanh chóng với môi trường mới.'",
target: "I believe I would be a suitable candidate for this position. This is because I am [đặc điểm tính cách]. Moreover, I am eager to learn and can adapt quickly to new environments."
},
{
cue: "Viết câu kết thư ứng tuyển: 'Tôi sẽ rất biết ơn nếu ông/bà có thể xem xét hồ sơ ứng tuyển của tôi. Tôi rất mong sớm nhận được phản hồi từ ông/bà.'",
target: "I would be grateful if you could consider my application. I look forward to receiving your reply soon."
}
]
};

// ==========================================
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
                type: "structures_and_sentences",
                structures: [
                    "Can you tell me the address of the center?",
                    "Could you let me know where the center is located?",
                    "I would like to know the exact address of the center."
                ],
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
                type: "structures_and_sentences",
                structures: [
                    "Can you tell me how much the tuition fee is?",
                    "Could you give me more information about the course fee?",
                    "I want to know about the cost of the course."
                ],
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
                        en: "I also want to know if there are any discounts for students or group registration.",
                        vi: "Mình cũng muốn biết liệu có giảm giá cho sinh viên hoặc đăng ký nhóm không."
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
                type: "structures_and_sentences",
                structures: [
                    "Can you tell me more about the teachers at the center?",
                    "Could you let me know what the teachers are like?",
                    "I was wondering if the teachers are friendly and helpful."
                ],
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
                type: "structures_and_sentences",
                structures: [
                    "Could you give me some details about the training program?",
                    "Can you tell me what the curriculum includes?",
                    "I would like to know more about the course schedule and materials."
                ],
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
                <p style="color: var(--text-muted);">Vui lòng chọn <strong>Dạng 01: Letter of Advice</strong> hoặc <strong>Dạng 02: Letter of Request</strong> để làm bài luyện tập.</p>
            </div>
        `;
        return;
    }

    let hintsHtml = data.hints.map(hint => {
        if (hint.type === "structures_and_sentences") {
            let structHtml = hint.structures.map(st => `
                <p style="margin-bottom: 4px; color: var(--primary-color); padding-left: 14px;">↳ <span class="outline-phrase">${st}</span></p>
            `).join('');

            let sentHtml = hint.sentences.map(st => `
                <div style="margin-bottom: 8px; padding-left: 14px;">
                    <p style="margin-bottom: 2px;">• <strong>${st.en}</strong></p>
                    <p style="margin-bottom: 0; color: var(--text-muted); font-size: 13.5px; font-style: italic;">(${st.vi})</p>
                </div>
            `).join('');

            return `
                <div class="outline-step" style="margin-bottom: 18px;">
                    <h4 style="margin-bottom: 10px; color: var(--accent-red); font-size: 17px;">${hint.title}</h4>
                    <div style="margin-bottom: 12px;">
                        <p style="font-weight: 700; color: var(--text-main); margin-bottom: 6px;"><i class="fa-solid fa-code-fork" style="color: var(--primary-color);"></i> Cấu trúc hỏi thông tin (Tự chọn 1 cấu trúc ghép vô):</p>
                        ${structHtml}
                    </div>
                    <div>
                        <p style="font-weight: 700; color: var(--text-main); margin-bottom: 6px;"><i class="fa-solid fa-angles-right" style="color: var(--secondary-color);"></i> Câu mở rộng (Lựa chọn câu phù hợp):</p>
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

    const promptBullets = data.prompt.split('\n').filter(l => l.startsWith('•')).map(l => `<li>${l.replace('•', '').trim()}</li>`).join('');
    const promptIntro = data.prompt.substring(0, data.prompt.indexOf('•')).trim();

    container.innerHTML = `
        <!-- Prompt Card (Using standard website style) -->
        <div class="sample-prompt-container">
            <div class="sample-prompt-header">
                <i class="fa-solid fa-file-circle-question"></i> ĐỀ BÀI (TOPIC PROMPT) - ${data.title}
            </div>
            <div class="sample-prompt-text">
                <p>${promptIntro.replace(/\n+/g, ' ')}</p>
                <ul>
                    ${promptBullets}
                </ul>
                <p style="margin-top: 10px; font-style: italic; color: var(--text-muted);">
                    <i class="fa-solid fa-triangle-exclamation" style="color: #f59e0b;"></i> You should write at least 120 words. Do not include your name. Your response will be evaluated in terms of Task Fulfillment, Organization, Vocabulary, and Grammar.
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
                <textarea id="extraWritingArea" placeholder="Dear friend,&#10;&#10;How are you? I hope you are doing well..." rows="12"></textarea>
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
    if (/\b(places|dishes|clothes|teachers|skills|topics)\s+is\b/gi.test(rawText)) {
        const m = rawText.match(/\b(places|dishes|clothes|teachers|skills|topics)\s+is\b/i);
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

    if (typeId === 'request') {
        hasReq1 = /(address|location|where\s+(is\s+)?the\s+center|near\s+my\s+(house|home)|street|district|easy\s+to\s+get|located)/i.test(lower);
        hasReq2 = /(fee|tuition|cost|price|money|how\s+much|budget|discount|pay)/i.test(lower);
        hasReq3 = /(teacher|teachers|instructor|friendly|experienced|teach|explain)/i.test(lower);
        hasReq4 = /(program|training|course|curriculum|skill|skills|schedule|length|study|practise|practice|topic|topics)/i.test(lower);
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
    const hasOpening = /(thanks?\s+for|hope\s+you|writing\s+to|how\s+are\s+you)/i.test(lower);
    const hasClosingSentence = /(hope\s+my\s+advice|write\s+back|let\s+me\s+know|look\s+forward|hope\s+you\s+can\s+help)/i.test(lower);
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

// DOM Elements
let letterNav;
let mainTitle;
let welcomeScreen;
let letterContent;
let themeToggle;
let isDarkMode = false;

// Auth & Student Information
const ALLOWED_CLASSES = ['CB206', 'GV'];
const MANDATORY_PASSWORD = 'STUDYHARD';

const AUTHORIZED_STUDENTS = [
    'Nguyễn Thị Vân Anh',
    'Nguyễn Thị Hồng Duyên',
    'Nguyễn Thị Thúy Hồng',
    'Trương Ngọc Nhi',
    'Nguyễn Phạm Như Quỳnh',
    'Trần Lê Quỳnh',
    'Thị Mỹ Tâm',
    'Ông Lê Thành',
    'Trần Nguyễn Thanh Thảo',
    'Phan Nhật Thiện',
    'Nguyễn Mỹ Tiên',
    'Trần Thị Cẩm Tiên',
    'Võ Trần Bảo Tính',
    'Trương Thanh Toàn',
    'Phạm Ngọc Trâm',
    'Nguyễn Võ Bảo Trân',
    'PTMN'
];

function normalizeVietnameseName(str) {
    if (!str) return '';
    return str.trim().toLowerCase().replace(/\s+/g, ' ');
}

function isAuthorizedStudent(name) {
    const norm = normalizeVietnameseName(name);
    if (norm === 'ptmn') return true;
    return AUTHORIZED_STUDENTS.some(auth => normalizeVietnameseName(auth) === norm);
}

const GOOGLE_FORM_ACTION_URL = "https://docs.google.com/forms/d/e/1FAIpQLSes7cy3Z9Wxr_QQRuJcohfqFycoc0_i5JNEt05FFBBGod2f5A/formResponse";
const GOOGLE_FORM_ENTRY_ID = "entry.388968236";

let currentStudentName = '';
let currentStudentClass = '';

let loginModalOverlay;
let studentNameInput;
let studentClassInput;
let studentClassSelect;
let studentPasswordInput;
let btnLoginSubmit;
let loginErrorMsg;
let loginErrorText;

let studentProfileCard;
let studentNameDisplay;
let studentClassDisplay;
let btnEditStudent;

let questStudentGreeting;
let greetingStudentName;
let greetingStudentClass;

let reportStatusBox;
let reportStatusIcon;
let reportStatusText;
let btnResendReport;

// Recitation DOM Elements
let recitationInput;
let btnPrevQuestion;
let btnShowAnswer;
let btnCheckAnswer;
let btnNextQuestion;
let currentQuestionNum;
let totalQuestionsNum;
let progressBarFill;
let questionCueText;
let recitationFeedback;
let feedbackStatus;
let userDiffResult;
let correctTextResult;
let questionHintBox;
let questionHintText;

// Evaluation DOM Elements
let recitationQuizBox;
let recitationResultBox;
let scorePercentageVal;
let resultStatusVal;
let resultMessageVal;
let btnRestartRecitation;
let evaluationIcon;

// Recitation State
let activeLetterTypeId = 'advice';
let currentQuestionIndex = 0;
let activeQuestions = [];
let questionScores = [];
let questionHintsUsed = [];

// Generate hint: obfuscates alternating words using asterisks, matching the B2 letters system
function getHintText(target) {
    if (!target) return '';
    const words = target.trim().split(/\s+/);
    const obfuscated = words.map((w, i) => {
        if (i % 2 !== 0 && w.length > 2) {
            return w[0] + '*'.repeat(w.length - 1);
        }
        return w;
    });
    return obfuscated.join(' ');
}

// Word-by-word diff algorithm using LCS
function diffWords(userText, targetText) {
    const preProcess = (t) => t
        .replace(/…/g, '...')
        .replace(/\.\s*\.\s*\./g, '...')
        .replace(/[’‘]/g, "'")
        .replace(/[“”]/g, '"')
        .replace(/\s*[-‐‑–—−]+\s*/g, ' - ');
        
    const clean = (w) => w.toLowerCase().trim();
    
    const uWords = preProcess(userText).trim().split(/\s+/).filter(w => w !== "");
    const tWords = preProcess(targetText).trim().split(/\s+/).filter(w => w !== "");
    
    const n = uWords.length;
    const m = tWords.length;
    const dp = Array(n + 1).fill(null).map(() => Array(m + 1).fill(0));
    
    for (let i = 1; i <= n; i++) {
        for (let j = 1; j <= m; j++) {
            if (clean(uWords[i - 1]) === clean(tWords[j - 1])) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    
    let i = n, j = m;
    const diff = [];
    
    while (i > 0 || j > 0) {
        if (i > 0 && j > 0 && clean(uWords[i - 1]) === clean(tWords[j - 1])) {
            diff.unshift({ word: uWords[i - 1], type: 'match' });
            i--;
            j--;
        } else if (j > 0 && (i === 0 || dp[i][j - 1] >= dp[i - 1][j])) {
            diff.unshift({ word: tWords[j - 1], type: 'missing' });
            j--;
        } else {
            diff.unshift({ word: uWords[i - 1], type: 'extra' });
            i--;
        }
    }
    
    let matchCount = diff.filter(d => d.type === 'match').length;
    let maxWords = Math.max(tWords.length, uWords.length);
    let accuracy = maxWords > 0 ? Math.round((matchCount / maxWords) * 100) : 0;
    
    return {
        diff,
        accuracy,
        isPerfect: matchCount === tWords.length && uWords.length === tWords.length
    };
}

// Global Learning Progress Management
function getCompletedLetters() {
    try {
        const saved = localStorage.getItem('vstep_completed_letters');
        return saved ? JSON.parse(saved) : [];
    } catch (e) {
        return [];
    }
}

function markLetterCompleted(letterId) {
    let completed = getCompletedLetters();
    if (!completed.includes(letterId)) {
        completed.push(letterId);
        try {
            localStorage.setItem('vstep_completed_letters', JSON.stringify(completed));
        } catch (e) {
            console.error('Error saving completed letters', e);
        }
    }
    updateGlobalProgress();
    renderNav();
}

function resetLearningProgress() {
    if (confirm('Bạn có chắc chắn muốn làm mới toàn bộ tiến độ học tập không?')) {
        try {
            localStorage.removeItem('vstep_completed_letters');
        } catch (e) {
            console.error('Error clearing progress', e);
        }
        updateGlobalProgress();
        renderNav();
    }
}

function updateGlobalProgress() {
    const completed = getCompletedLetters();
    const total = letterTypes.length;
    const count = completed.length;
    const percentage = total > 0 ? Math.round((count / total) * 100) : 0;

    // Sidebar Progress
    const sidebarText = document.getElementById('sidebarProgressText');
    const sidebarFill = document.getElementById('sidebarProgressFill');
    if (sidebarText) sidebarText.textContent = `${count}/${total} ĐẠT`;
    if (sidebarFill) sidebarFill.style.width = `${percentage}%`;

    // Dashboard Card Progress
    const dashPercent = document.getElementById('dashboardProgressPercent');
    const dashFill = document.getElementById('dashboardProgressFill');
    const dashStatus = document.getElementById('dashboardProgressStatus');
    
    if (dashPercent) dashPercent.textContent = `${percentage}%`;
    if (dashFill) dashFill.style.width = `${percentage}%`;
    if (dashStatus) {
        if (count === 0) {
            dashStatus.textContent = 'Chưa hoàn thành dạng thư nào. Hãy bắt đầu học tập!';
        } else if (count < total) {
            dashStatus.textContent = `Đã hoàn thành ${count}/${total} dạng thư. Tiếp tục phát huy!`;
        } else {
            dashStatus.textContent = '🎉 Xuất sắc! Bạn đã chinh phục toàn bộ 7 dạng thư VSTEP Task 01!';
        }
    }
}

// Reset recitation UI
function resetRecitationUI() {
    currentQuestionIndex = 0;
    activeQuestions = recitationQuestions[activeLetterTypeId] || [];
    questionScores = new Array(activeQuestions.length).fill(0);
    questionHintsUsed = new Array(activeQuestions.length).fill(false);

    if (totalQuestionsNum) totalQuestionsNum.textContent = activeQuestions.length;

    // Reset UI Visibility
    if (recitationQuizBox) recitationQuizBox.classList.remove('hidden');
    if (recitationFeedback) recitationFeedback.classList.add('hidden');
    if (recitationResultBox) recitationResultBox.classList.add('hidden');
    if (reportStatusBox) reportStatusBox.classList.add('hidden');
    
    // Restore header and progress bar
    const recitationHeader = document.querySelector('.recitation-header');
    if (recitationHeader) recitationHeader.classList.remove('hidden');
    
    const progressWrapper = document.querySelector('.recitation-progress-wrapper');
    if (progressWrapper) progressWrapper.style.display = 'flex';

    showRecitationQuestion();
}

// Display active recitation question
function showRecitationQuestion() {
    if (activeQuestions.length === 0) return;

    const q = activeQuestions[currentQuestionIndex];
    if (currentQuestionNum) currentQuestionNum.textContent = currentQuestionIndex + 1;
    
    // Update progress bar
    const progressPct = ((currentQuestionIndex + 1) / activeQuestions.length) * 100;
    if (progressBarFill) progressBarFill.style.width = `${progressPct}%`;

    if (questionCueText) questionCueText.textContent = q.cue;
    if (recitationInput) {
        recitationInput.value = '';
        recitationInput.disabled = false;
        recitationInput.focus();
    }

    // Reset feedback and hint box
    if (recitationFeedback) recitationFeedback.classList.add('hidden');
    if (questionHintBox) questionHintBox.classList.add('hidden');
    if (questionHintText) questionHintText.textContent = '';

    // If hint was already used on this question, restore it
    if (questionHintsUsed[currentQuestionIndex]) {
        if (questionHintText) questionHintText.textContent = getHintText(q.target);
        if (questionHintBox) questionHintBox.classList.remove('hidden');
    }

    // Button states
    if (btnPrevQuestion) btnPrevQuestion.disabled = (currentQuestionIndex === 0);
    if (btnShowAnswer) btnShowAnswer.classList.remove('hidden');
    if (btnCheckAnswer) btnCheckAnswer.classList.remove('hidden');
    if (btnNextQuestion) btnNextQuestion.classList.add('hidden');
}

// Check user recitation answer
function checkRecitationAnswer() {
    if (activeQuestions.length === 0) return;
    const q = activeQuestions[currentQuestionIndex];
    const userAns = recitationInput ? recitationInput.value.trim() : '';

    if (!userAns) {
        alert('Vui lòng nhập câu trả lời của bạn trước khi kiểm tra!');
        return;
    }

    const diffResult = diffWords(userAns, q.target);
    const hintUsed = questionHintsUsed[currentQuestionIndex] || false;
    
    // Apply 50% penalty if hint was used
    let finalScore = diffResult.accuracy;
    if (hintUsed) {
        finalScore = Math.round(diffResult.accuracy * 0.5);
    }
    questionScores[currentQuestionIndex] = finalScore;

    // Build diff HTML for User Diff Result
    if (userDiffResult) {
        userDiffResult.innerHTML = '';
        diffResult.diff.forEach(d => {
            if (d.type === 'match') {
                const span = document.createElement('span');
                span.className = 'diff-word-match';
                span.textContent = d.word + ' ';
                userDiffResult.appendChild(span);
            } else if (d.type === 'extra') {
                const span = document.createElement('span');
                span.className = 'diff-word-extra';
                span.textContent = d.word + ' ';
                userDiffResult.appendChild(span);
            }
        });
        if (userDiffResult.innerHTML === '') {
            userDiffResult.innerHTML = '<span style="color:var(--text-muted);font-style:italic;">(Bỏ trống)</span>';
        }
    }

    // Build diff HTML for Correct Text Result
    if (correctTextResult) {
        correctTextResult.innerHTML = '';
        diffResult.diff.forEach(d => {
            if (d.type === 'match') {
                const span = document.createElement('span');
                span.className = 'diff-word-match';
                span.textContent = d.word + ' ';
                correctTextResult.appendChild(span);
            } else if (d.type === 'missing') {
                const span = document.createElement('span');
                span.className = 'diff-word-mismatch';
                span.textContent = d.word + ' ';
                correctTextResult.appendChild(span);
            }
        });
    }

    // Show Feedback Status
    if (feedbackStatus) {
        if (diffResult.isPerfect) {
            feedbackStatus.className = 'feedback-status status-success';
            if (hintUsed) {
                feedbackStatus.innerHTML = `<i class="fa-solid fa-circle-check"></i> <strong>Chính xác tuyệt đối!</strong> (Độ khớp: 100% - Điểm tính: 50% do dùng gợi ý)`;
            } else {
                feedbackStatus.innerHTML = `<i class="fa-solid fa-circle-check"></i> <strong>Chính xác tuyệt đối!</strong> (Độ chính xác: 100%)`;
            }
        } else {
            feedbackStatus.className = 'feedback-status status-error';
            if (hintUsed) {
                feedbackStatus.innerHTML = `<i class="fa-solid fa-triangle-exclamation"></i> <strong>Chưa chính xác!</strong> (Độ khớp: ${diffResult.accuracy}% - Điểm tính: ${finalScore}% do dùng gợi ý). Xem chi tiết bên dưới.`;
            } else {
                feedbackStatus.innerHTML = `<i class="fa-solid fa-triangle-exclamation"></i> <strong>Chưa chính xác! Độ chính xác: ${diffResult.accuracy}%. Xem so sánh bên dưới.</strong>`;
            }
        }
    }

    if (recitationFeedback) recitationFeedback.classList.remove('hidden');
    if (btnCheckAnswer) btnCheckAnswer.classList.add('hidden');
    if (btnNextQuestion) btnNextQuestion.classList.remove('hidden');
    if (recitationInput) recitationInput.disabled = true;
}

// Show hint inline
function showRecitationAnswer() {
    if (activeQuestions.length === 0) return;
    const q = activeQuestions[currentQuestionIndex];
    
    // Mark as hint used for this question
    questionHintsUsed[currentQuestionIndex] = true;
    
    // Generate masked hint text
    const hintText = getHintText(q.target);
    
    if (questionHintText) {
        questionHintText.textContent = hintText;
    }
    if (questionHintBox) {
        questionHintBox.classList.remove('hidden');
    }
}

// Next recitation question
function nextRecitationQuestion() {
    if (currentQuestionIndex < activeQuestions.length - 1) {
        currentQuestionIndex++;
        showRecitationQuestion();
    } else {
        showEvaluationResult();
    }
}

// Show evaluation result screen
function showEvaluationResult() {
    // Hide quiz box and feedback panel
    if (recitationQuizBox) recitationQuizBox.classList.add('hidden');
    if (recitationFeedback) recitationFeedback.classList.add('hidden');
    
    // Hide header and progress bar wrapper during evaluation results
    const recitationHeader = document.querySelector('.recitation-header');
    if (recitationHeader) recitationHeader.classList.add('hidden');
    
    const progressWrapper = document.querySelector('.recitation-progress-wrapper');
    if (progressWrapper) progressWrapper.style.display = 'none';
    
    // Calculate average score
    const totalQuestions = activeQuestions.length;
    const totalScore = questionScores.reduce((sum, s) => sum + s, 0);
    const averageScore = totalQuestions > 0 ? Math.round(totalScore / totalQuestions) : 0;
    
    // Update score text
    if (scorePercentageVal) scorePercentageVal.textContent = averageScore;
    
    // Get active letter type data for dynamic title
    const typeData = letterTypes.find(t => t.id === activeLetterTypeId);
    const letterTitleEn = typeData ? typeData.titleEn : 'Letter of Advice';
    
    const evalCard = document.querySelector('.evaluation-card');
    let statusText = 'KHÔNG ĐẠT';
    
    if (averageScore >= 90) {
        // Passed state
        statusText = 'ĐẠT';
        if (resultStatusVal) {
            resultStatusVal.textContent = 'ĐẠT';
        }
        if (resultMessageVal) {
            const questNames = {
                advice: 'NHIỆM VỤ HỆ THỐNG ĐẦU TIÊN',
                request: 'NHIỆM VỤ HỆ THỐNG THỨ HAI',
                description: 'NHIỆM VỤ HỆ THỐNG THỨ BA',
                complaint: 'NHIỆM VỤ HỆ THỐNG THỨ TƯ',
                feedback: 'NHIỆM VỤ HỆ THỐNG THỨ NĂM',
                apology: 'NHIỆM VỤ HỆ THỐNG THỨ SÁU',
                application: 'NHIỆM VỤ HỆ THỐNG THỨ BẢY'
            };
            const questName = questNames[activeLetterTypeId] || 'NHIỆM VỤ HỆ THỐNG';
            resultMessageVal.textContent = `Chúc mừng bạn đã chinh phục được ${letterTitleEn}. ${questName} đã được hoàn thành, hãy tiếp tục với nhiệm vụ tiếp theo.`;
        }
        if (evaluationIcon) {
            evaluationIcon.innerHTML = '<i class="fa-solid fa-circle-check"></i>';
        }
        if (evalCard) {
            evalCard.classList.remove('failed');
            evalCard.classList.add('passed');
        }
        markLetterCompleted(activeLetterTypeId);
    } else {
        // Failed state
        statusText = 'KHÔNG ĐẠT';
        if (resultStatusVal) {
            resultStatusVal.textContent = 'KHÔNG ĐẠT';
        }
        if (resultMessageVal) {
            resultMessageVal.textContent = 'Xin vui lòng ôn lại bài thật kỹ và trả bài lại một lần nữa.';
        }
        if (evaluationIcon) {
            evaluationIcon.innerHTML = '<i class="fa-solid fa-triangle-exclamation"></i>';
        }
        if (evalCard) {
            evalCard.classList.remove('passed');
            evalCard.classList.add('failed');
        }
    }
    
    // Show result box
    if (recitationResultBox) recitationResultBox.classList.remove('hidden');

    // Automatically report result to Google Form
    reportResultToGoogleForm();
}

// Prev recitation question
function prevRecitationQuestion() {
    if (currentQuestionIndex > 0) {
        currentQuestionIndex--;
        showRecitationQuestion();
    }
}

// Show Welcome Screen
function showWelcomeScreen() {
    activeLetterTypeId = null;
    
    // Update active nav
    document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.remove('active');
    });
    const homeItem = document.querySelector('.home-nav-item');
    if (homeItem) homeItem.classList.add('active');

    // Show welcome, hide content
    if (welcomeScreen) welcomeScreen.style.display = 'flex';
    if (letterContent) letterContent.classList.add('hidden');

    // Reset Title
    if (mainTitle) {
        mainTitle.innerHTML = `
            <div class="main-title-en placeholder-blink">Chọn một dạng thư để bắt đầu NHIỆM VỤ HỆ THỐNG của bạn!</div>
        `;
    }
}

// Render Navigation
function renderNav() {
    if (!letterNav) return;
    letterNav.innerHTML = ''; // Clear existing
    
    // Add Home button first
    const homeItem = document.createElement('div');
    homeItem.className = 'nav-item home-nav-item active';
    homeItem.innerHTML = `
        <i class="fa-solid fa-house"></i>
        <div class="nav-text">
            <div class="nav-title-en" style="font-weight: bold;">TRANG CHỦ</div>
            <div class="nav-title-vi">Màn hình khởi đầu</div>
        </div>
    `;
    homeItem.addEventListener('click', showWelcomeScreen);
    letterNav.appendChild(homeItem);

    const completed = getCompletedLetters();

    letterTypes.forEach(type => {
        const isCompleted = completed.includes(type.id);
        const navItem = document.createElement('div');
        navItem.className = 'nav-item';
        navItem.dataset.id = type.id;
        navItem.innerHTML = `
            <i class="fa-solid ${type.icon}"></i>
            <div class="nav-text">
                <div class="nav-title-en">${type.titleEn}</div>
                <div class="nav-title-vi">${type.titleVi}</div>
            </div>
            ${isCompleted ? '<span class="nav-completed-badge" title="Đã chinh phục"><i class="fa-solid fa-circle-check"></i></span>' : ''}
        `;
        
        navItem.addEventListener('click', () => selectLetterType(type.id));
        letterNav.appendChild(navItem);
    });
}

// Select a Letter Type
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
    if (studentNameInput) studentNameInput.value = currentStudentName || '';
    if (studentClassInput) studentClassInput.value = currentStudentClass || '';
    if (studentClassSelect) studentClassSelect.value = currentStudentClass || '';
    if (studentPasswordInput) studentPasswordInput.value = '';
    if (loginErrorMsg) loginErrorMsg.classList.add('hidden');
    loginModalOverlay.classList.remove('hidden');
    setTimeout(() => {
        if (studentNameInput) studentNameInput.focus();
    }, 150);
}

function handleLoginSubmit() {
    const nameVal = studentNameInput ? studentNameInput.value.trim() : '';
    const classEl = studentClassInput || studentClassSelect;
    const classVal = classEl ? classEl.value.trim().toUpperCase().replace(/\s+/g, '') : '';
    const passVal = studentPasswordInput ? studentPasswordInput.value.trim() : '';

    if (!nameVal || nameVal.length < 2) {
        showLoginError('Vui lòng nhập đầy đủ Họ và tên học viên / Giáo viên.');
        if (studentNameInput) studentNameInput.focus();
        return;
    }

    const isTeacher = normalizeVietnameseName(nameVal) === 'ptmn' || nameVal.toUpperCase() === 'PTMN';

    if (!isAuthorizedStudent(nameVal)) {
        showLoginError('Họ và tên không nằm trong danh sách học viên hoặc giáo viên được cấp quyền truy cập!');
        if (studentNameInput) studentNameInput.focus();
        return;
    }

    if (isTeacher) {
        if (classVal !== 'GV' && classVal !== 'CB206') {
            showLoginError('Giáo viên vui lòng điền Lớp: GV (hoặc CB206)!');
            if (classEl) classEl.focus();
            return;
        }
    } else {
        if (classVal !== 'CB206') {
            showLoginError('Lớp học không đúng. Hệ thống chỉ tiếp nhận học viên thuộc lớp CB206!');
            if (classEl) classEl.focus();
            return;
        }
    }

    if (passVal !== MANDATORY_PASSWORD) {
        showLoginError('Mật khẩu không chính xác! Vui lòng nhập đúng mật khẩu STUDYHARD.');
        if (studentPasswordInput) {
            studentPasswordInput.value = '';
            studentPasswordInput.focus();
        }
        return;
    }

    if (isTeacher) {
        currentStudentName = 'Cô Nguyệt (PTMN)';
        currentStudentClass = classVal || 'GV';
    } else {
        // Match exact name from whitelist
        const matched = AUTHORIZED_STUDENTS.find(auth => normalizeVietnameseName(auth) === normalizeVietnameseName(nameVal));
        currentStudentName = matched || nameVal;
        currentStudentClass = 'CB206';
    }

    updateStudentProfileUI(currentStudentName, currentStudentClass);

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

        payload = `[HỌC VIÊN]: ${name} | [LỚP]: ${cls} | [DẠNG BÀI]: ${letterTitle} | [ĐIỂM]: ${score}% (${status}) | [THỜI GIAN]: ${now}`;
    }

    console.log("Submitting result report to Google Form:", payload);

    if (reportStatusBox) reportStatusBox.classList.remove('hidden');
    if (reportStatusIcon) {
        reportStatusIcon.className = 'fa-solid fa-spinner fa-spin report-status-icon';
    }
    if (reportStatusText) {
        reportStatusText.textContent = 'Đang gửi kết quả lên hệ thống của giáo viên...';
    }

    // Method 1: Fetch POST (no-cors)
    try {
        const formData = new URLSearchParams();
        formData.append(GOOGLE_FORM_ENTRY_ID, payload);

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

    // Method 2: Hidden iframe fallback
    try {
        let iframe = document.getElementById('gform_hidden_iframe');
        if (!iframe) {
            iframe = document.createElement('iframe');
            iframe.id = 'gform_hidden_iframe';
            iframe.name = 'gform_hidden_iframe';
            iframe.style.display = 'none';
            document.body.appendChild(iframe);
        }

        let form = document.getElementById('gform_hidden_form');
        if (!form) {
            form = document.createElement('form');
            form.id = 'gform_hidden_form';
            form.action = GOOGLE_FORM_ACTION_URL;
            form.method = 'POST';
            form.target = 'gform_hidden_iframe';
            form.style.display = 'none';

            const input = document.createElement('input');
            input.type = 'hidden';
            input.name = GOOGLE_FORM_ENTRY_ID;
            input.id = 'gform_hidden_input';
            form.appendChild(input);
            document.body.appendChild(form);
        }

        const input = document.getElementById('gform_hidden_input');
        if (input) {
            input.value = payload;
            form.submit();
        }
    } catch (e) {
        console.log('Iframe submit error:', e);
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
    studentClassSelect = document.getElementById('studentClassSelect');
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
