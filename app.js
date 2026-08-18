const letterTypes = [
    {
        id: 'advice',
        icon: 'fa-lightbulb',
        titleEn: 'Letter of Advice',
        titleVi: 'Thư Cho Lời Khuyên',
        basicInfo: `
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
        `,
        identifyingSigns: `
            <div class="content-block">
                <h3>Các từ khóa thường xuất hiện trong đề bài:</h3>
                <ul>
                    <li>advice / give me some advice / ask for advice</li>
                    <li>suggestions / recommendations</li>
                    <li>what should I do...? / what would you suggest...?</li>
                    <li>I need your advice with...</li>
                </ul>
            </div>
        `,
        detailedOutline: `
            <div class="outline-note">
                <p><strong>LƯU Ý:</strong> Thư cho lời khuyên thường là thư thân mật.</p>
            </div>
            <div class="outline-step">
                <h4>1. Lời chào mở đầu</h4>
                <p>↳ <span class="outline-phrase">Dear [tên của người nhận],</span></p>
            </div>
            <div class="outline-step">
                <h4>2. Mở thư</h4>
                <p>↳ <span class="outline-phrase">Thanks for your letter. I hope you are doing well. I’m writing to give you some advice about your situation.</span></p>
            </div>
            <div class="outline-step">
                <h4>3. Thân thư</h4>
                <p>Lần lượt đưa ra lời khuyên/gợi ý phù hợp với tình huống của đề.</p>
                <div class="outline-structures">
                    <h5>CẤU TRÚC CHO LỜI KHUYÊN:</h5>
                    <ul>
                        <li><span class="outline-phrase">You should + Vo.</span></li>
                        <li><span class="outline-phrase">It would be a good idea to + Vo.</span></li>
                        <li><span class="outline-phrase">If I were you, I would + Vo.</span></li>
                        <li><span class="outline-phrase">You can try + Ving.</span></li>
                        <li><span class="outline-phrase">Remember to + Vo. / Don’t forget to + Vo.</span></li>
                    </ul>
                </div>
                <p>Từ liên kết gợi ý: ↳ <em>First, … → Second, … → Next, … → Finally, …</em></p>
            </div>
            <div class="outline-step">
                <h4>4. Kết thư</h4>
                <p>↳ <span class="outline-phrase">I hope my advice will be helpful to you. Please let me know how everything turns out. Write back soon.</span></p>
            </div>
            <div class="outline-step">
                <h4>5. Lời chào kết thúc</h4>
                <p>↳ <span class="outline-phrase">Best wishes,</span></p>
            </div>
        `,
        practicePrompt: 'You have received a letter from an English friend, Helen. She is going to visit Hanoi in June. Write a letter to give her some suggestions. In your letter, you should tell her: Where to stay, What dishes to try, Which places to visit, and What to wear when visiting Hanoi. You should write at least 120 words. Do not include your name or address.',
        sampleWriting: `
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
                    <p><i class="fa-solid fa-lightbulb"></i> Số từ: 155 words. Bài viết chia đoạn và sử dụng các liên từ nối cùng các mẫu câu khuyên bảo chuẩn B1.</p>
                </div>
            </div>
        `
    },
    {
        id: 'request',
        icon: 'fa-hand-holding-hand',
        titleEn: 'Letter of Request',
        titleVi: 'Thư Yêu Cầu',
        basicInfo: `
            <div class="content-block">
                <h3>Mục đích (Purpose)</h3>
                <p>Yêu cầu hoặc xin thông tin, sự giúp đỡ, dịch vụ hoặc sự cho phép từ người nhận.</p>
            </div>
            <div class="content-block">
                <h3>Phong cách thư (Style)</h3>
                <p>Thường là thư bán trang trọng hoặc trang trọng (Semi-formal/Formal Letter).</p>
            </div>
            <div class="content-block">
                <h3>Văn phong (Tone)</h3>
                <p>Lịch sự, tôn trọng và rõ ràng.</p>
            </div>
        `,
        identifyingSigns: `
            <div class="content-block">
                <h3>Các từ khóa thường xuất hiện:</h3>
                <ul>
                    <li>request / ask for / demand</li>
                    <li>could you please provide...</li>
                    <li>write a letter to request...</li>
                </ul>
            </div>
        `,
        detailedOutline: `
            <div class="outline-note">
                <p><strong>LƯU Ý:</strong> Thư yêu cầu thường được dùng để xin thông tin, xin giúp đỡ hoặc đề nghị điều gì đó. Thư có thể là thư thân mật, bán trang trọng hoặc trang trọng.</p>
            </div>
            <div class="outline-step">
                <h4>1. Lời chào mở đầu</h4>
                <ul>
                    <li><strong>Thân mật:</strong> ↳ <span class="outline-phrase">Dear [tên của người nhận],</span></li>
                    <li><strong>Trang trọng:</strong>
                        <ul>
                            <li>↳ <span class="outline-phrase">Dear Sir,</span> (nếu biết chắc chắn người nhận là nam)</li>
                            <li>↳ <span class="outline-phrase">Dear Madam,</span> (nếu biết chắc chắn người nhận là nữ)</li>
                            <li>↳ <span class="outline-phrase">Dear Sir/Madam,</span> (nếu không biết chắc chắn)</li>
                        </ul>
                    </li>
                    <li><strong>Bán trang trọng:</strong> ↳ <span class="outline-phrase">Dear Mr. / Ms. / Mrs. [họ của người nhận],</span></li>
                </ul>
            </div>
            <div class="outline-step">
                <h4>2. Mở thư</h4>
                <ul>
                    <li><strong>Thân mật:</strong> ↳ <span class="outline-phrase">How are you? I hope you are doing well. I’m writing to ask for some information about [thứ cần xin thông tin] because [lý do].</span></li>
                    <li><strong>Trang trọng & Bán trang trọng:</strong> ↳ <span class="outline-phrase">I am writing to request some information about [thứ cần xin thông tin] because [lý do].</span></li>
                </ul>
            </div>
            <div class="outline-step">
                <h4>3. Thân thư</h4>
                <p>Lần lượt xin các thông tin cần thiết phù hợp với tình huống của đề.</p>
                <div class="outline-structures">
                    <h5>CẤU TRÚC XIN THÔNG TIN:</h5>
                    <p><strong>Thân mật:</strong></p>
                    <ul>
                        <li><span class="outline-phrase">Can you give me more information about …?</span></li>
                        <li><span class="outline-phrase">Can you tell me more about …?</span></li>
                        <li><span class="outline-phrase">Can you let me know more about …?</span></li>
                        <li><span class="outline-phrase">I want to know more about …</span></li>
                        <li><span class="outline-phrase">I want more information about …</span></li>
                    </ul>
                    <p><strong>Trang trọng & Bán trang trọng:</strong></p>
                    <ul>
                        <li><span class="outline-phrase">Could you provide me with more information about …?</span></li>
                        <li><span class="outline-phrase">Could you give me more details about …?</span></li>
                        <li><span class="outline-phrase">I would like to know more about …</span></li>
                        <li><span class="outline-phrase">I would like to inquire about …</span></li>
                        <li><span class="outline-phrase">I am also wondering about …</span></li>
                    </ul>
                </div>
                <div class="outline-subnote">
                    <p><strong>LƯU Ý:</strong> Sau mỗi yêu cầu xin thông tin, nên kèm 1 câu ngắn nêu lý do.</p>
                </div>
                <p>Từ liên kết gợi ý: ↳ <em>First, … → Second, … → Next, … → Finally, …</em></p>
            </div>
            <div class="outline-step">
                <h4>4. Kết thư</h4>
                <ul>
                    <li><strong>Thân mật:</strong> ↳ <span class="outline-phrase">I hope you can help me with this. Write back soon.</span></li>
                    <li><strong>Trang trọng & Bán trang trọng:</strong> ↳ <span class="outline-phrase">Thank you for your time. I look forward to your reply.</span></li>
                </ul>
            </div>
            <div class="outline-step">
                <h4>5. Lời chào kết thúc</h4>
                <ul>
                    <li><strong>Thân mật:</strong> ↳ <span class="outline-phrase">Best wishes,</span></li>
                    <li><strong>Trang trọng:</strong> ↳ <span class="outline-phrase">Yours faithfully,</span></li>
                    <li><strong>Bán trang trọng:</strong> ↳ <span class="outline-phrase">Yours sincerely,</span></li>
                </ul>
            </div>
        `,
        practicePrompt: 'Your friend has just completed an English course at Rainbow Language Center and had a great experience. You are planning to study English as well and would like to know more about the course. Write a letter to your friend asking for more information about the course. In your email, you should ask about: The address of the center, The tuition fee, The teachers, and The training program. You should write at least 120 words. Do not include your name or address.',
        sampleWriting: `
            <div class="content-block">
                <h3>BÀI VIẾT MẪU (SAMPLE LETTER - B1 LEVEL)</h3>
                <div class="sample-letter-box">
                    <strong>Dear Moonie,</strong><br><br>
                    How are you? I hope you are doing well. I’m writing to ask for some information about the English course at Rainbow Language Center because I am planning to study English there next month.<br><br>
                    Firstly, can you tell me the address of the center? This is because I want to know if it is convenient for me to travel there by motorbike. Secondly, I want to get more details about the tuition fee. In fact, I need to prepare my budget before enrolling in the course. Next, can you give me more information about the teachers? I want to make sure that they are experienced and friendly so that I can feel more confident when studying there. Finally, can you let me know more about the training program? I want to know what skills students will learn during the course.<br><br>
                    I hope you can help me with this. Write back soon.<br><br>
                    <strong>Best wishes,</strong>
                </div>
                
                <h3 style="margin-top: 25px;">BẢN DỊCH CHI TIẾT</h3>
                <div class="translation-box" style="background-color: var(--bg-main); border: 1px solid var(--border-color); padding: 20px; border-radius: 12px; margin-top: 15px; font-family: var(--font-body); line-height: 1.8; color: var(--text-muted); font-style: italic;">
                    <strong>Moonie thân mến,</strong><br><br>
                    Cậu khỏe không? Tớ hy vọng cậu vẫn khỏe. Tớ viết thư này để hỏi một vài thông tin về khóa học tiếng Anh tại Trung tâm Ngoại ngữ Rainbow vì tớ có kế hoạch học tiếng Anh ở đó vào tháng tới.<br><br>
                    Đầu tiên, cậu có thể cho tớ biết địa chỉ của trung tâm không? Điều này là vì tớ muốn biết liệu đi xe máy đến đó có thuận tiện cho tớ hay không. Thứ hai, tớ muốn biết thêm chi tiết về học phí. Thực tế là tớ cần chuẩn bị ngân sách trước khi đăng ký khóa học. Tiếp theo, cậu có thể cho tớ thêm thông tin về các giáo viên không? Tớ muốn chắc chắn rằng họ có kinh nghiệm và thân thiện để tớ cảm thấy tự tin hơn khi học ở đó. Cuối cùng, cậu có thể cho tớ biết thêm về chương trình đào tạo không? Tớ muốn biết học viên sẽ được học những kỹ năng gì trong suốt khóa học.<br><br>
                    Tớ hy vọng cậu có thể giúp tớ việc này. Hãy trả lời thư sớm nhé.<br><br>
                    <strong>Chúc cậu mọi điều tốt lành,</strong>
                </div>
                
                <div class="highlight-box" style="margin-top: 20px;">
                    <p><i class="fa-solid fa-lightbulb"></i> Số từ: 151 words. Bài viết hỏi thông tin với văn phong tự nhiên, sử dụng đa dạng các câu hỏi gián tiếp và liên từ phù hợp.</p>
                </div>
            </div>
        `
    },
    {
        id: 'description',
        icon: 'fa-image',
        titleEn: 'Letter of Description',
        titleVi: 'Thư Miêu Tả',
        basicInfo: `
            <div class="content-block">
                <h3>Mục đích (Purpose)</h3>
                <p>Cung cấp thông tin hoặc mô tả về một người, địa điểm, sự kiện, trải nghiệm hoặc tình huống cụ thể.</p>
            </div>
            <div class="content-block">
                <h3>Phong cách thư (Style)</h3>
                <p>Chủ yếu là thư thân mật (Informal Letter).</p>
            </div>
            <div class="content-block">
                <h3>Văn phong (Tone)</h3>
                <p>Thân thiện, tự nhiên và mang tính chia sẻ.</p>
            </div>
        `,
        identifyingSigns: `
            <div class="content-block">
                <h3>Các từ khóa thường xuất hiện:</h3>
                <ul>
                    <li>describe / tell me about</li>
                    <li>what was it like...?</li>
                    <li>write a letter to describe your trip / event...</li>
                </ul>
            </div>
        `,
        detailedOutline: `
            <div class="outline-note">
                <p><strong>LƯU Ý:</strong> Thư mô tả dùng để cung cấp thông tin hoặc mô tả đặc điểm của một người, địa điểm, sự việc hoặc chương trình. Dạng thư này có thể là thư thân mật, bán trang trọng hoặc trang trọng.</p>
            </div>
            <div class="outline-step">
                <h4>1. Lời chào mở đầu</h4>
                <ul>
                    <li><strong>Thân mật:</strong> ↳ <span class="outline-phrase">Dear [tên của người nhận],</span></li>
                    <li><strong>Trang trọng:</strong>
                        <ul>
                            <li>↳ <span class="outline-phrase">Dear Sir,</span> (nếu chắc chắn là nam)</li>
                            <li>↳ <span class="outline-phrase">Dear Madam,</span> (nếu chắc chắn là nữ)</li>
                            <li>↳ <span class="outline-phrase">Dear Sir/Madam,</span> (nếu không chắc chắn)</li>
                        </ul>
                    </li>
                    <li><strong>Bán trang trọng:</strong> ↳ <span class="outline-phrase">Dear Mr. / Ms. / Mrs. [họ của người nhận],</span></li>
                </ul>
            </div>
            <div class="outline-step">
                <h4>2. Mở thư</h4>
                <div class="outline-substep">
                    <h5>Khi thư yêu cầu CUNG CẤP THÔNG TIN:</h5>
                    <ul>
                        <li><strong>Thân mật:</strong> ↳ <span class="outline-phrase">How are you? I hope you are doing well. In your letter, you asked me about [thứ cần mô tả thông tin], so here is some information.</span></li>
                        <li><strong>Trang trọng & Bán trang trọng:</strong> ↳ <span class="outline-phrase">In your letter, you asked me about [thứ cần mô tả thông tin], so I am writing to provide you with some information.</span></li>
                    </ul>
                </div>
                <div class="outline-substep" style="margin-top: 10px;">
                    <h5>Khi thư yêu cầu MÔ TẢ MỘT ĐỐI TƯỢNG / SỰ VIỆC:</h5>
                    <ul>
                        <li><strong>Thân mật:</strong> ↳ <span class="outline-phrase">How are you? I hope you are doing well. In your letter, you asked me to describe [thứ cần mô tả], so here are some details.</span></li>
                        <li><strong>Trang trọng & Bán trang trọng:</strong> ↳ <span class="outline-phrase">In your letter, you asked me to describe [thứ cần mô tả], so I am writing to provide you with some details.</span></li>
                    </ul>
                </div>
            </div>
            <div class="outline-step">
                <h4>3. Thân thư</h4>
                <p>Cung cấp thông tin hoặc mô tả đối tượng, sự việc theo yêu cầu của người nhận.</p>
                <div class="outline-subnote">
                    <p><strong>LƯU Ý:</strong> Trong thân thư, chỉ mô tả hoặc cung cấp thông tin, không đặt câu hỏi, không đưa lời khuyên.</p>
                </div>
                <p>Từ liên kết gợi ý: ↳ <em>First, … → Second, … → Next, … → Finally, …</em></p>
            </div>
            <div class="outline-step">
                <h4>4. Kết thư</h4>
                <ul>
                    <li><strong>Thân mật:</strong> ↳ <span class="outline-phrase">I hope you will find this information useful. Let me know if you need more details.</span></li>
                    <li><strong>Trang trọng & Bán trang trọng:</strong> ↳ <span class="outline-phrase">I hope the information above will be helpful to you. Please feel free to contact me if you need more details.</span></li>
                </ul>
            </div>
            <div class="outline-step">
                <h4>5. Lời chào kết thúc</h4>
                <ul>
                    <li><strong>Thân mật:</strong> ↳ <span class="outline-phrase">Best wishes,</span></li>
                    <li><strong>Trang trọng:</strong> ↳ <span class="outline-phrase">Yours faithfully,</span></li>
                    <li><strong>Bán trang trọng:</strong> ↳ <span class="outline-phrase">Yours sincerely,</span></li>
                </ul>
            </div>
        `,
        practicePrompt: 'You have received a letter from your English friend, Emily. Read part of her letter below:\n... I have received a letter from your friend, Hoa. She is going to do a course in London, so she asked me if she could stay with me and my family until she finds an apartment. Could you tell me some information about her? (things like her personality, her hobbies, her current work or study). I need to know whether she will fit in my family or not ...\nWrite a letter responding to Emily. You should write at least 120 words. Do not include your name or address.',
        sampleWriting: `
            <div class="content-block">
                <h3>BÀI VIẾT MẪU (SAMPLE LETTER - B1 LEVEL)</h3>
                <div class="sample-letter-box">
                    <strong>Dear Emily,</strong><br><br>
                    How are you? I hope you are doing well. In your letter, you asked me about my friend Hoa, so here is some information.<br><br>
                    Firstly, she is a very friendly and helpful person. Therefore, she gets along well with people around her and always tries to help them when they need support. Secondly, she enjoys quiet activities such as reading books and listening to music, so she will not disturb anyone in the house. She also likes cooking, so she can help with preparing meals at home. Next, she is currently a second-year student at Can Tho University, majoring in Business Administration. The course in London is part of her study program, so she will stay there for a short time to complete it. Finally, I believe she will fit in well with your family because she always respects family rules and has a well-organized lifestyle.<br><br>
                    I hope you will find this information useful. Let me know if you need more details.<br><br>
                    <strong>Best wishes,</strong>
                </div>
                
                <h3 style="margin-top: 25px;">BẢN DỊCH CHI TIẾT</h3>
                <div class="translation-box" style="background-color: var(--bg-main); border: 1px solid var(--border-color); padding: 20px; border-radius: 12px; margin-top: 15px; font-family: var(--font-body); line-height: 1.8; color: var(--text-muted); font-style: italic;">
                    <strong>Emily thân mến,</strong><br><br>
                    Cậu khỏe không? Tớ hy vọng cậu vẫn khỏe. Trong thư của cậu, cậu có hỏi tớ về Hoa, bạn của tớ, vì vậy dưới đây là một số thông tin về cô ấy.<br><br>
                    Đầu tiên, cô ấy là một người rất thân thiện và hay giúp đỡ. Do đó, cô ấy hòa đồng với mọi người xung quanh và luôn cố gắng giúp đỡ họ khi họ cần hỗ trợ. Thứ hai, cô ấy thích các hoạt động yên tĩnh như đọc sách và nghe nhạc, vì vậy cô ấy sẽ không làm phiền ai trong nhà. Cô ấy cũng thích nấu ăn, nên cô ấy có thể giúp chuẩn bị bữa ăn ở nhà. Tiếp theo, cô ấy hiện là sinh viên năm thứ hai Đại học Cần Thơ, chuyên ngành Quản trị Kinh doanh. Khóa học ở Luân Đôn là một phần trong chương trình học của cô ấy, vì vậy cô ấy sẽ ở đó một thời gian ngắn để hoàn thành nó. Cuối cùng, tớ tin rằng cô ấy sẽ hòa nhập tốt với gia đình cậu vì cô ấy luôn tôn trọng các quy tắc gia đình và có lối sống rất ngăn nắp.<br><br>
                    Tớ hy vọng cậu sẽ thấy những thông tin này hữu ích. Hãy cho tớ biết nếu cậu cần thêm chi tiết nhé.<br><br>
                    <strong>Chúc cậu mọi điều tốt lành,</strong>
                </div>
                
                <div class="highlight-box" style="margin-top: 20px;">
                    <p><i class="fa-solid fa-lightbulb"></i> Số từ: 166 words. Bài viết tập trung mô tả tính cách, sở thích và thông tin học tập của người được giới thiệu.</p>
                </div>
            </div>
        `
    },
    {
        id: 'complaint',
        icon: 'fa-thumbs-down',
        titleEn: 'Letter of Complaint',
        titleVi: 'Thư Phàn Nàn',
        basicInfo: `
            <div class="content-block">
                <h3>Mục đích (Purpose)</h3>
                <p>Phàn nàn về một sản phẩm, dịch vụ hoặc tình huống không hài lòng, đồng thời yêu cầu giải quyết vấn đề.</p>
            </div>
            <div class="content-block">
                <h3>Phong cách thư (Style)</h3>
                <p>Chủ yếu là thư trang trọng (Formal Letter).</p>
            </div>
            <div class="content-block">
                <h3>Văn phong (Tone)</h3>
                <p>Nghiêm túc, lịch sự, khách quan và mang tính xây dựng.</p>
            </div>
        `,
        identifyingSigns: `
            <div class="content-block">
                <h3>Các từ khóa thường xuất hiện:</h3>
                <ul>
                    <li>complain / make a complaint / express dissatisfaction</li>
                    <li>you bought a product but it is faulty</li>
                    <li>bad service / poor quality</li>
                </ul>
            </div>
        `,
        detailedOutline: `
            <div class="outline-note">
                <p><strong>LƯU Ý:</strong> Thư phàn nàn thường là thư bán trang trọng hoặc trang trọng.</p>
            </div>
            <div class="outline-step">
                <h4>1. Lời chào mở đầu</h4>
                <ul>
                    <li><strong>Trang trọng:</strong>
                        <ul>
                            <li>↳ <span class="outline-phrase">Dear Sir,</span> (nếu chắc chắn là nam)</li>
                            <li>↳ <span class="outline-phrase">Dear Madam,</span> (nếu chắc chắn là nữ)</li>
                            <li>↳ <span class="outline-phrase">Dear Sir/Madam,</span> (nếu không chắc chắn)</li>
                        </ul>
                    </li>
                    <li><strong>Bán trang trọng:</strong> ↳ <span class="outline-phrase">Dear Mr. / Ms. / Mrs. [họ của người nhận],</span></li>
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
                    <p>↳ <span class="outline-phrase">The main problem was that [vấn đề 1].</span> → Trình bày cụ thể.</p>
                    <p>↳ <span class="outline-phrase">Another issue was that [vấn đề 2].</span> → Trình bày cụ thể.</p>
                    <p>↳ <span class="outline-phrase">Finally, I also found that [vấn đề 3].</span> → Trình bày cụ thể.</p>
                </div>
                <div class="outline-substep" style="margin-top: 10px;">
                    <h5>Thân thư 2: Cảm xúc với trải nghiệm và đề xuất giải pháp</h5>
                    <p>↳ <span class="outline-phrase">I was very disappointed / quite unhappy with these problems. Therefore, I would appreciate it if you could [giải pháp cụ thể để giải quyết vấn đề].</span></p>
                </div>
            </div>
            <div class="outline-step">
                <h4>4. Kết thư</h4>
                <p>Yêu cầu xem xét vấn đề: ↳ <span class="outline-phrase">I hope that you will look into these issues soon.</span></p>
                <p>Mong đợi hồi âm: ↳ <span class="outline-phrase">I look forward to receiving your reply soon.</span></p>
            </div>
            <div class="outline-step">
                <h4>5. Lời chào kết thúc</h4>
                <ul>
                    <li><strong>Trang trọng:</strong> ↳ <span class="outline-phrase">Yours faithfully,</span></li>
                    <li><strong>Bán trang trọng:</strong> ↳ <span class="outline-phrase">Yours sincerely,</span></li>
                </ul>
            </div>
        `,
        practicePrompt: 'You are a member of a local sports center. You have recently used the changing room and were not satisfied with its condition. Write an email to the manager of the sports center. In your email, you should: Describe the problems you found in the changing room, Explain how the situation made you feel, and Suggest what should be done to improve the facility. You should write at least 120 words. Do not include your name or address.',
        sampleWriting: `
            <div class="content-block">
                <h3>Bài Viết Mẫu (Sample Letter - B1 Level)</h3>
                <div class="sample-letter-box">
                    <strong>Dear Sir/Madam,</strong><br><br>
                    I am writing to complain about the condition of the changing room at your sports center. I recently used the facility and had an unpleasant experience.<br><br>
                    The main problem was that the changing room was very dirty. In fact, the floor was wet, and there were used towels left on the benches. Another issue was that several lockers were broken and could not be locked properly. This made it difficult for members to store their belongings safely. Finally, I also found that the room had a strong unpleasant smell. Therefore, the air in the room felt uncomfortable.<br><br>
                    I was very disappointed with these problems. Therefore, I would appreciate it if you could clean the changing room more regularly, repair the lockers, and improve the ventilation in the room.<br><br>
                    I hope that you will look into this issue soon. I look forward to receiving your reply soon.<br><br>
                    <strong>Yours faithfully,</strong>
                </div>
                
                <h3 style="margin-top: 25px;">BẢN DỊCH CHI TIẾT</h3>
                <div class="translation-box" style="background-color: var(--bg-main); border: 1px solid var(--border-color); padding: 20px; border-radius: 12px; margin-top: 15px; font-family: var(--font-body); line-height: 1.8; color: var(--text-muted); font-style: italic;">
                    <strong>Kính gửi Ông/Bà,</strong><br><br>
                    Tôi viết thư này để phàn nàn về tình trạng của phòng thay đồ tại trung tâm thể thao của ông/bà. Gần đây tôi đã sử dụng cơ sở này và có một trải nghiệm không mấy dễ chịu.<br><br>
                    Vấn đề chính là phòng thay đồ rất bẩn. Thực tế, sàn nhà bị ướt, và có nhiều khăn tắm đã qua sử dụng bị bỏ lại trên băng ghế. Một vấn đề khác là một vài tủ đồ bị hỏng và không thể khóa đúng cách. Điều này gây khó khăn cho các thành viên trong việc cất giữ đồ đạc cá nhân an toàn. Cuối cùng, tôi cũng nhận thấy căn phòng có mùi khó chịu nồng nặc. Vì vậy, không khí trong phòng tạo cảm giác rất ngột ngạt.<br><br>
                    Tôi rất thất vọng với những vấn đề này. Do đó, tôi sẽ rất cảm kích nếu ông/bà có thể cho dọn dẹp phòng thay đồ thường xuyên hơn, sửa chữa các tủ khóa và cải thiện hệ thống thông gió trong phòng.<br><br>
                    Tôi hy vọng ông/bà sẽ sớm xem xét vấn đề này. Tôi rất mong sớm nhận được phản hồi từ ông/bà.<br><br>
                    <strong>Trân trọng,</strong>
                </div>
                
                <div class="highlight-box" style="margin-top: 20px;">
                    <p><i class="fa-solid fa-lightbulb"></i> Số từ: 145 words. Thư sử dụng ngôn từ trang trọng để phàn nàn, trình bày rõ vấn đề, cảm xúc và giải pháp gợi ý.</p>
                </div>
            </div>
        `
    },
    {
        id: 'feedback',
        icon: 'fa-comments',
        titleEn: 'Letter of Feedback',
        titleVi: 'Thư Phản Hồi/Đánh Giá',
        basicInfo: `
            <div class="content-block">
                <h3>Mục đích (Purpose)</h3>
                <p>Đưa ra nhận xét, đánh giá hoặc góp ý về một sản phẩm, dịch vụ, khóa học, sự kiện hoặc trải nghiệm.</p>
            </div>
            <div class="content-block">
                <h3>Phong cách thư (Style)</h3>
                <p>Thường là thư bán trang trọng (Semi-formal Letter).</p>
            </div>
            <div class="content-block">
                <h3>Văn phong (Tone)</h3>
                <p>Lịch sự, khách quan và mang tính xây dựng.</p>
            </div>
        `,
        identifyingSigns: `
            <div class="content-block">
                <h3>Các từ khóa thường xuất hiện:</h3>
                <ul>
                    <li>give feedback / review / share your opinion</li>
                    <li>how was your experience?</li>
                    <li>what could be improved?</li>
                </ul>
            </div>
        `,
        detailedOutline: `
            <div class="outline-note">
                <p><strong>LƯU Ý:</strong> Thư cho phản hồi đánh giá thường là thư bán trang trọng hoặc trang trọng.</p>
            </div>
            <div class="outline-step">
                <h4>1. Lời chào mở đầu</h4>
                <ul>
                    <li><strong>Trang trọng:</strong>
                        <ul>
                            <li>↳ <span class="outline-phrase">Dear Sir,</span> (nếu chắc chắn là nam)</li>
                            <li>↳ <span class="outline-phrase">Dear Madam,</span> (nếu chắc chắn là nữ)</li>
                            <li>↳ <span class="outline-phrase">Dear Sir/Madam,</span> (nếu không chắc chắn)</li>
                        </ul>
                    </li>
                    <li><strong>Bán trang trọng:</strong> ↳ <span class="outline-phrase">Dear Mr. / Ms. / Mrs. [họ của người nhận],</span></li>
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
                    <p>↳ <em>First of all, I would like to mention some positive points about your [sản phẩm/dịch vụ].</em></p>
                    <ul>
                        <li><span class="outline-phrase">I was very satisfied with [điểm khen] because [lý do].</span></li>
                        <li><span class="outline-phrase">I really liked [điểm khen] because [lý do].</span></li>
                        <li><span class="outline-phrase">I was impressed with [điểm khen] as [lý do].</span></li>
                        <li><span class="outline-phrase">One thing I liked most was [điểm khen] since [lý do].</span></li>
                    </ul>
                    
                    <h5 style="margin-top: 10px;">CÁC CẤU TRÚC PHẢN ÁNH ĐIỂM CHƯA HÀI LÒNG [CHÊ]:</h5>
                    <p>↳ <em>However, there were also some areas that needed improvement.</em></p>
                    <ul>
                        <li><span class="outline-phrase">I was disappointed with [điểm chê] because [lý do].</span></li>
                        <li><span class="outline-phrase">One thing that disappointed me was [điểm chê] since [lý do].</span></li>
                        <li><span class="outline-phrase">I was not satisfied with [điểm chê] as [lý do].</span></li>
                        <li><span class="outline-phrase">The quality of [điểm chê] was not as good as I expected because [lý do].</span></li>
                    </ul>
                    
                    <h5 style="margin-top: 10px;">CÁC CẤU TRÚC ĐỀ XUẤT GIẢI PHÁP:</h5>
                    <p>↳ <em>To enhance the quality of your [sản phẩm/dịch vụ], I have a few suggestions.</em></p>
                    <ul>
                        <li><span class="outline-phrase">I suggest that you should [hành động – Vo].</span></li>
                        <li><span class="outline-phrase">I think you should [hành động – Vo].</span></li>
                        <li><span class="outline-phrase">It would be better if you could [hành động – Vo].</span></li>
                        <li><span class="outline-phrase">I hope you will consider [hành động – Ving].</span></li>
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
                    <li><strong>Trang trọng:</strong> ↳ <span class="outline-phrase">Yours faithfully,</span></li>
                    <li><strong>Bán trang trọng:</strong> ↳ <span class="outline-phrase">Yours sincerely,</span></li>
                </ul>
            </div>
        `,
        practicePrompt: 'You recently stayed at a hotel and received an email from the hotel manager asking for feedback about your stay. Write an email to give your opinion. In your email, you should: Say whether you were satisfied or dissatisfied with the service, Describe your experience, and Suggest ways the hotel can improve its service. You should write at least 120 words. Do not include your name or address.',
        sampleWriting: `
            <div class="content-block">
                <h3>Bài Viết Mẫu (Sample Letter - B1 Level)</h3>
                <div class="sample-letter-box">
                    <strong>Dear Sir/Madam,</strong><br><br>
                    I am writing to give you feedback about my recent stay at your hotel. I recently used your services and would like to share my experience.<br><br>
                    First of all, I would like to mention some positive points about your hotel. I was very satisfied with the room because it was clean and comfortable. I was also impressed with the hotel location as it was close to many tourist attractions. In addition, one thing I liked most was the staff since they were friendly and helpful.<br><br>
                    However, there were also some areas that needed improvement. I was disappointed with the breakfast because there were not many food options. I was also not satisfied with the Wi-Fi service as the connection was very slow.<br><br>
                    To enhance the quality of your service, I have a few suggestions. I suggest that you improve the breakfast menu and provide more food choices. It would also be better if you could upgrade the internet service.<br><br>
                    I hope my feedback will help you improve your service. Please feel free to contact me if you have any further questions.<br><br>
                    <strong>Yours faithfully,</strong>
                </div>
                
                <h3 style="margin-top: 25px;">BẢN DỊCH CHI TIẾT</h3>
                <div class="translation-box" style="background-color: var(--bg-main); border: 1px solid var(--border-color); padding: 20px; border-radius: 12px; margin-top: 15px; font-family: var(--font-body); line-height: 1.8; color: var(--text-muted); font-style: italic;">
                    <strong>Kính gửi Ông/Bà,</strong><br><br>
                    Tôi viết thư này để phản hồi về kỳ nghỉ gần đây của tôi tại khách sạn của ông/bà. Gần đây tôi đã sử dụng dịch vụ của ông/bà và muốn chia sẻ trải nghiệm của mình.<br><br>
                    Trước hết, tôi muốn đề cập đến một số điểm tích cực về khách sạn của ông/bà. Tôi rất hài lòng với căn phòng vì nó sạch sẽ và thoải mái. Tôi cũng ấn tượng với vị trí của khách sạn vì nó nằm gần nhiều điểm thu hút khách du lịch. Ngoài ra, điều tôi thích nhất là đội ngũ nhân viên vì họ rất thân thiện và nhiệt tình giúp đỡ.<br><br>
                    Tuy nhiên, cũng có một số lĩnh vực cần được cải thiện. Tôi thấy thất vọng về bữa sáng vì không có nhiều lựa chọn món ăn. Tôi cũng không hài lòng với dịch vụ Wi-Fi vì kết nối rất chậm.<br><br>
                    Để nâng cao chất lượng dịch vụ của ông/bà, tôi có một vài đề xuất. Tôi đề nghị ông/bà cải thiện thực đơn bữa sáng và cung cấp nhiều lựa chọn thức ăn hơn. Sẽ tốt hơn nếu ông/bà có thể nâng cấp dịch vụ internet.<br><br>
                    Tôi hy vọng những phản hồi của tôi sẽ giúp ông/bà cải thiện dịch vụ của mình. Xin vui lòng liên hệ với tôi nếu ông/bà có thêm bất kỳ câu hỏi nào.<br><br>
                    <strong>Trân trọng,</strong>
                </div>
                
                <div class="highlight-box" style="margin-top: 20px;">
                    <p><i class="fa-solid fa-lightbulb"></i> Số từ: 179 words. Bài viết chia làm 3 đoạn tương ứng với các yêu cầu của đề: Ưu điểm, Nhược điểm và Kiến nghị.</p>
                </div>
            </div>
        `
    },
    {
        id: 'apology',
        icon: 'fa-face-frown',
        titleEn: 'Letter of Apology',
        titleVi: 'Thư Xin Lỗi',
        basicInfo: `
            <div class="content-block">
                <h3>Mục đích (Purpose)</h3>
                <p>Xin lỗi về một lỗi lầm, sự bất tiện hoặc việc không thể thực hiện một cam kết nào đó.</p>
            </div>
            <div class="content-block">
                <h3>Phong cách thư (Style)</h3>
                <p>Chủ yếu là thư thân mật (Informal Letter).</p>
            </div>
            <div class="content-block">
                <h3>Văn phong (Tone)</h3>
                <p>Chân thành, lịch sự và thể hiện sự hối tiếc.</p>
            </div>
        `,
        identifyingSigns: `
            <div class="content-block">
                <h3>Các từ khóa thường xuất hiện:</h3>
                <ul>
                    <li>apologize / say sorry / make an apology</li>
                    <li>you cannot attend... / you lost something...</li>
                    <li>write a letter to explain and apologize</li>
                </ul>
            </div>
        `,
        detailedOutline: `
            <div class="outline-note">
                <p><strong>LƯU Ý:</strong> Thư xin lỗi có thể là thư thân mật, bán trang trọng hoặc trang trọng.</p>
            </div>
            <div class="outline-step">
                <h4>1. Lời chào mở đầu</h4>
                <ul>
                    <li><strong>Thân mật:</strong> ↳ <span class="outline-phrase">Dear [tên của người nhận],</span></li>
                    <li><strong>Trang trọng:</strong>
                        <ul>
                            <li>↳ <span class="outline-phrase">Dear Sir,</span> (nếu chắc chắn là nam)</li>
                            <li>↳ <span class="outline-phrase">Dear Madam,</span> (nếu chắc chắn là nữ)</li>
                            <li>↳ <span class="outline-phrase">Dear Sir/Madam,</span> (nếu không chắc chắn)</li>
                        </ul>
                    </li>
                    <li><strong>Bán trang trọng:</strong> ↳ <span class="outline-phrase">Dear Mr. / Ms. / Mrs. [họ của người nhận],</span></li>
                </ul>
            </div>
            <div class="outline-step">
                <h4>2. Mở thư</h4>
                <ul>
                    <li><strong>Thân mật:</strong> ↳ <span class="outline-phrase">I’m really sorry for [vấn đề cần xin lỗi]. Let me explain what happened so you can understand the situation.</span></li>
                    <li><strong>Trang trọng & Bán trang trọng:</strong> ↳ <span class="outline-phrase">I am writing to apologize for [vấn đề cần xin lỗi]. I understand that this may have caused some inconvenience, and I would like to explain the situation.</span></li>
                </ul>
            </div>
            <div class="outline-step">
                <h4>3. Thân thư</h4>
                <p>Lần lượt giải thích lý do và nêu hành động bù đắp phù hợp.</p>
                <div class="outline-structures">
                    <h5>CẤU TRÚC GIẢI THÍCH LÝ DO:</h5>
                    <p><strong>Thân mật:</strong></p>
                    <p>↳ <em>First of all, let me explain why this happened.</em></p>
                    <ul>
                        <li><span class="outline-phrase">I’m really sorry that I couldn’t [hành động – Vo] because [lý do].</span></li>
                        <li><span class="outline-phrase">I missed [sự kiện] because [lý do].</span></li>
                        <li><span class="outline-phrase">I felt bad about not [hành động – Ving] because [lý do].</span></li>
                        <li><span class="outline-phrase">I didn’t mean to [hành động – Vo], but [lý do].</span></li>
                    </ul>
                    
                    <p><strong>Trang trọng & Bán trang trọng:</strong></p>
                    <p>↳ <em>First of all, I would like to explain why this happened.</em></p>
                    <ul>
                        <li><span class="outline-phrase">I was unable to [hành động – Vo] because [lý do].</span></li>
                        <li><span class="outline-phrase">I regret that I was unable to [hành động – Vo] because [lý do].</span></li>
                        <li><span class="outline-phrase">Because [lý do], I was unable to [hành động – Vo].</span></li>
                        <li><span class="outline-phrase">Unfortunately, I could not [hành động – Vo] because [lý do].</span></li>
                    </ul>
                </div>
                <div class="outline-subnote">
                    <p><strong>LƯU Ý:</strong> Sau khi nêu lý do, nên thêm 1-3 câu mô tả cụ thể tình huống để người đọc hiểu rõ hơn. Sử dụng thì QUÁ KHỨ ĐƠN để mô tả những sự việc đã xảy ra.</p>
                </div>
                <div class="outline-structures" style="margin-top: 10px;">
                    <h5>CẤU TRÚC NÊU HÀNH ĐỘNG BÙ ĐẮP:</h5>
                    <ul>
                        <li><strong>Thân mật:</strong> ↳ <span class="outline-phrase">Finally, let me make it up to you by [hành động – Ving].</span></li>
                        <li><strong>Trang trọng & Bán trang trọng:</strong> ↳ <span class="outline-phrase">To make up for my mistake, I would like to [hành động – Vo].</span></li>
                    </ul>
                </div>
            </div>
            <div class="outline-step">
                <h4>4. Kết thư</h4>
                <ul>
                    <li><strong>Thân mật:</strong> ↳ <span class="outline-phrase">Sorry once again. Thanks for taking the time to read this. Write back soon.</span></li>
                    <li><strong>Trang trọng & Bán trang trọng:</strong> ↳ <span class="outline-phrase">I would like to apologize once again for the inconvenience. Thank you for taking the time to read my letter. I look forward to receiving your reply soon.</span></li>
                </ul>
            </div>
            <div class="outline-step">
                <h4>5. Lời chào kết thúc</h4>
                <ul>
                    <li><strong>Thân mật:</strong> ↳ <span class="outline-phrase">Best wishes,</span></li>
                    <li><strong>Trang trọng:</strong> ↳ <span class="outline-phrase">Yours faithfully,</span></li>
                    <li><strong>Bán trang trọng:</strong> ↳ <span class="outline-phrase">Yours sincerely,</span></li>
                </ul>
            </div>
        `,
        practicePrompt: 'You borrowed a book from your friend Helen, but forgot to return it. Read part of her letter below:\n… Hey! How have you been lately? By the way, have you finished reading the book you borrowed from me? I was wondering why you haven’t returned it yet. When do you plan to give it back, and how will you return it? …\nWrite a letter to reply to Helen. In your letter, you should: apologize for not returning the book, explain your current situation and whether you’ve finished the book, and say when and how you will return it. You should write at least 120 words. Do not include your name or address.',
        sampleWriting: `
            <div class="content-block">
                <h3>Bài Viết Mẫu (Sample Letter - B1 Level)</h3>
                <div class="sample-letter-box">
                    <strong>Dear Helen,</strong><br><br>
                    I’m really sorry for not returning your book earlier. Let me explain what happened so you can understand the situation.<br><br>
                    First of all, here is the reason for this. I couldn’t return the book because I have been very busy with my studies for the past few months. During that time, I had several assignments and an important exam to prepare for. As a result, I completely forgot about the book. Next, I have finished reading the book, and I really enjoyed it. It was very interesting. Finally, I promise I will return the book to you next Friday after I finish my exams. I will bring it to your house in the afternoon so you can get it back soon. Let me make it up to you by inviting you to watch a movie together next week.<br><br>
                    Sorry once again. I really appreciate you taking the time to read this. Write back soon.<br><br>
                    <strong>Best wishes,</strong>
                </div>
                
                <h3 style="margin-top: 25px;">BẢN DỊCH CHI TIẾT</h3>
                <div class="translation-box" style="background-color: var(--bg-main); border: 1px solid var(--border-color); padding: 20px; border-radius: 12px; margin-top: 15px; font-family: var(--font-body); line-height: 1.8; color: var(--text-muted); font-style: italic;">
                    <strong>Helen thân mến,</strong><br><br>
                    Tớ thực sự xin lỗi vì đã không trả sách cho cậu sớm hơn. Hãy để tớ giải thích những gì đã xảy ra để cậu hiểu rõ tình hình nhé.<br><br>
                    Trước hết, đây là lý do. Tớ đã không thể trả sách vì tớ quá bận rộn với việc học trong vài tháng qua. Trong thời gian đó, tớ có vài bài tập lớn và một kỳ thi quan trọng cần chuẩn bị. Kết quả là tớ hoàn toàn quên mất cuốn sách. Tiếp theo, tớ đã đọc xong cuốn sách và tớ thực sự thích nó. Nó rất thú vị. Cuối cùng, tớ hứa sẽ trả sách cho cậu vào thứ Sáu tới sau khi tớ thi xong. Tớ sẽ mang nó đến nhà cậu vào buổi chiều để cậu sớm nhận lại sách. Để bù đắp cho lỗi này, tớ muốn mời cậu đi xem phim cùng nhau vào tuần tới nhé.<br><br>
                    Xin lỗi cậu một lần nữa nhé. Tớ rất trân trọng việc cậu đã dành thời gian đọc thư này. Hãy viết thư lại cho tớ sớm nhé.<br><br>
                    <strong>Chúc cậu mọi điều tốt lành,</strong>
                </div>
                
                <div class="highlight-box" style="margin-top: 20px;">
                    <p><i class="fa-solid fa-lightbulb"></i> Số từ: 155 words. Thư xin lỗi bạn bè thân mật, đưa ra nguyên nhân thuyết phục cùng hành động đền bù đáng yêu.</p>
                </div>
            </div>
        `
    },
    {
        id: 'application',
        icon: 'fa-briefcase',
        titleEn: 'Letter of Application',
        titleVi: 'Thư Ứng Tuyển',
        basicInfo: `
            <div class="content-block">
                <h3>Mục đích (Purpose)</h3>
                <p>Ứng tuyển hoặc đăng ký tham gia một vị trí, khóa học, chương trình hoặc hoạt động nào đó.</p>
            </div>
            <div class="content-block">
                <h3>Phong cách thư (Style)</h3>
                <p>Chủ yếu là thư trang trọng (Formal Letter).</p>
            </div>
            <div class="content-block">
                <h3>Văn phong (Tone)</h3>
                <p>Trang trọng, chuyên nghiệp và thuyết phục.</p>
            </div>
        `,
        identifyingSigns: `
            <div class="content-block">
                <h3>Các từ khóa thường xuất hiện:</h3>
                <ul>
                    <li>apply for / application</li>
                    <li>job vacancy / volunteer position</li>
                    <li>write a letter to apply for...</li>
                </ul>
            </div>
        `,
        detailedOutline: `
            <div class="outline-note">
                <p><strong>LƯU Ý:</strong> Thư ứng tuyển thường gặp nhất là thư xin việc và luôn là thư trang trọng.</p>
            </div>
            <div class="outline-step">
                <h4>1. Lời chào mở đầu</h4>
                <ul>
                    <li><strong>Trang trọng:</strong>
                        <ul>
                            <li>↳ <span class="outline-phrase">Dear Sir,</span> (nếu chắc chắn là nam)</li>
                            <li>↳ <span class="outline-phrase">Dear Madam,</span> (nếu chắc chắn là nữ)</li>
                            <li>↳ <span class="outline-phrase">Dear Sir/Madam,</span> (nếu không chắc chắn)</li>
                        </ul>
                    </li>
                </ul>
            </div>
            <div class="outline-step">
                <h4>2. Mở thư</h4>
                <ul>
                    <li><strong>Trang trọng:</strong> ↳ <span class="outline-phrase">I am writing to apply for the position of [vị trí công việc] which was advertised on/in [nguồn tuyển dụng].</span></li>
                </ul>
            </div>
            <div class="outline-step">
                <h4>3. Thân thư</h4>
                <p>Lần lượt trình bày lý do có hứng thú với vị trí công việc này, đề cập trình độ học vấn và năng lực chuyên môn, kinh nghiệm làm việc đã có, sau đó nêu lý do mình là ứng cử viên phù hợp cho vị trí này.</p>
                <div class="outline-structures">
                    <h5>LÝ DO CÓ HỨNG THÚ VỚI VỊ TRÍ CÔNG VIỆC NÀY:</h5>
                    <p>↳ <span class="outline-phrase">I am very interested in this position because it matches my interests and career goals. In addition, I enjoy [hoạt động liên quan đến công việc]. Therefore, I believe this job will give me a good opportunity to apply what I have learned during my studies and gain practical experience.</span></p>
                    
                    <h5 style="margin-top: 10px;">TRÌNH ĐỘ HỌC VẤN VÀ NĂNG LỰC CHUYÊN MÔN:</h5>
                    <p>↳ <span class="outline-phrase">I recently graduated from [tên trường] with a bachelor’s degree in [chuyên ngành]. During my studies, I developed a strong understanding of [lĩnh vực]. I also gained useful knowledge and abilities such as [kiến thức/năng lực học thuật 1] and [kiến thức/năng lực học thuật 2].</span></p>
                    
                    <h5 style="margin-top: 10px;">KINH NGHIỆM LÀM VIỆC ĐÃ CÓ:</h5>
                    <p>↳ <span class="outline-phrase">I worked part-time as a [vị trí công việc] at [nơi làm việc]. In this job, I was responsible for [nhiệm vụ]. This experience helped me develop skills such as [kỹ năng mềm 1] and [kỹ năng mềm 2].</span></p>
                    
                    <h5 style="margin-top: 10px;">KHẲNG ĐỊNH LÀ ỨNG CỬ VIÊN PHÙ HỢP:</h5>
                    <p>↳ <span class="outline-phrase">I believe I would be a suitable candidate for this position. This is because I am [đặc điểm tính cách]. Moreover, I am eager to learn and can adapt quickly to new environments.</span></p>
                </div>
            </div>
            <div class="outline-step">
                <h4>4. Kết thư</h4>
                <ul>
                    <li><strong>Trang trọng:</strong> ↳ <span class="outline-phrase">I would be grateful if you could consider my application. I look forward to receiving your reply soon.</span></li>
                </ul>
            </div>
            <div class="outline-step">
                <h4>5. Lời chào kết thúc</h4>
                <ul>
                    <li><strong>Trang trọng:</strong> ↳ <span class="outline-phrase">Yours faithfully,</span></li>
                </ul>
            </div>
        `,
        practicePrompt: 'You saw a job advertisement for a sales assistant at a clothing store in your city. Write an email to apply for the job. In your email, you should: Introduce yourself and your current situation, Say why you are interested in the position, and Mention any experience you have working with customers. You should write at least 120 words. Do not include your name or address.',
        sampleWriting: `
            <div class="content-block">
                <h3>Bài Viết Mẫu (Sample Letter - B1 Level)</h3>
                <div class="sample-letter-box">
                    <strong>Dear Sir/Madam,</strong><br><br>
                    I am writing to apply for the position of sales assistant which was advertised in a local newspaper.<br><br>
                    I recently graduated from Can Tho University with a bachelor’s degree in Business Administration. During my studies, I developed a strong understanding of marketing and customer service. I also gained useful skills such as sales strategies and product promotion.<br><br>
                    I am very interested in this position because it matches my interests and career goals. In addition, I enjoy taking care of customers and helping them choose suitable products. Therefore, I believe this job will give me a good opportunity to apply what I have learned at university and gain practical experience.<br><br>
                    I worked part-time as a shop assistant at a small clothing store. In this job, I was responsible for assisting customers and arranging products. This experience helped me develop communication and customer service skills.<br><br>
                    I believe I would be a suitable candidate for this position because I am responsible and hardworking. Moreover, I am eager to learn and can adapt quickly to new environments.<br><br>
                    I would be grateful if you could consider my application. I look forward to receiving your reply soon.<br><br>
                    <strong>Yours faithfully,</strong>
                </div>
                
                <h3 style="margin-top: 25px;">BẢN DỊCH CHI TIẾT</h3>
                <div class="translation-box" style="background-color: var(--bg-main); border: 1px solid var(--border-color); padding: 20px; border-radius: 12px; margin-top: 15px; font-family: var(--font-body); line-height: 1.8; color: var(--text-muted); font-style: italic;">
                    <strong>Kính gửi Ông/Bà,</strong><br><br>
                    Tôi viết thư này để ứng tuyển vào vị trí nhân viên bán hàng được quảng cáo trên một tờ báo địa phương.<br><br>
                    Tôi vừa tốt nghiệp Đại học Cần Thơ với tấm bằng cử nhân ngành Quản trị Kinh doanh. Trong quá trình học, tôi đã phát triển sự hiểu biết sâu sắc về marketing và dịch vụ khách hàng. Tôi cũng tích lũy được những kỹ năng hữu ích như chiến lược bán hàng và quảng bá sản phẩm.<br><br>
                    Tôi rất hứng thú với vị trí này vì nó phù hợp với sở thích và mục tiêu nghề nghiệp của tôi. Ngoài ra, tôi thích việc chăm sóc khách hàng và giúp họ lựa chọn sản phẩm phù hợp. Vì vậy, tôi tin rằng công việc này sẽ mang lại cho tôi cơ hội tốt để áp dụng những gì đã học ở trường đại học và tích lũy thêm kinh nghiệm thực tế.<br><br>
                    Tôi đã từng làm việc bán thời gian với tư cách là nhân viên bán hàng tại một cửa hàng quần áo nhỏ. Trong công việc này, tôi chịu trách nhiệm hỗ trợ khách hàng và sắp xếp sản phẩm. Kinh nghiệm này đã giúp tôi phát triển các kỹ năng giao tiếp và dịch vụ khách hàng.<br><br>
                    Tôi tin rằng mình sẽ là ứng cử viên phù hợp cho vị trí này vì tôi là người có trách nhiệm và làm việc chăm chỉ. Hơn nữa, tôi rất ham học hỏi và có thể thích nghi nhanh chóng với môi trường mới.<br><br>
                    Tôi rất biết ơn nếu ông/bà có thể xem xét hồ sơ ứng tuyển của tôi. Tôi rất mong sớm nhận được phản hồi từ ông/bà.<br><br>
                    <strong>Trân trọng,</strong>
                </div>
                
                <div class="highlight-box" style="margin-top: 20px;">
                    <p><i class="fa-solid fa-lightbulb"></i> Số từ: 188 words. Thư xin việc chỉn chu, nêu bật được thế mạnh học vấn, sở thích định hướng nghề nghiệp và kinh nghiệm thực tế.</p>
                </div>
            </div>
        `
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

// DOM Elements
let letterNav;
let mainTitle;
let welcomeScreen;
let letterContent;
let themeToggle;
let isDarkMode = false;

// Auth & Student Information
const ALLOWED_CLASSES = ['CB201', 'CB202', 'B209'];
const GOOGLE_FORM_ACTION_URL = "https://docs.google.com/forms/d/e/1FAIpQLSes7cy3Z9Wxr_QQRuJcohfqFycoc0_i5JNEt05FFBBGod2f5A/formResponse";
const GOOGLE_FORM_ENTRY_ID = "entry.388968236";

let currentStudentName = '';
let currentStudentClass = '';

let loginModalOverlay;
let studentNameInput;
let studentClassInput;
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
    
    if (averageScore >= 90) {
        // Passed state
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
    if (loginErrorMsg) loginErrorMsg.classList.add('hidden');
    loginModalOverlay.classList.remove('hidden');
    setTimeout(() => {
        if (studentNameInput) studentNameInput.focus();
    }, 150);
}

function handleLoginSubmit() {
    const nameVal = studentNameInput ? studentNameInput.value.trim() : '';
    const rawClassVal = studentClassInput ? studentClassInput.value.trim().toUpperCase().replace(/\s+/g, '') : '';

    if (!nameVal || nameVal.length < 2) {
        showLoginError('Vui lòng điền đầy đủ Họ và tên.');
        if (studentNameInput) studentNameInput.focus();
        return;
    }

    if (!rawClassVal || !ALLOWED_CLASSES.includes(rawClassVal)) {
        showLoginError('Lớp học không đúng. Vui lòng kiểm tra lại tên lớp!');
        if (studentClassInput) studentClassInput.focus();
        return;
    }

    currentStudentName = nameVal;
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
