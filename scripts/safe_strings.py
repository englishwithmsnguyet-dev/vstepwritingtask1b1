with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the formatLetterParagraphs function
old_func = """function formatLetterParagraphs(str) {
    if (!str) return '';
    return str.split('\n\n').join('<br><br>');
}"""

new_func = """function formatLetterParagraphs(str) {
    if (!str) return '';
    const doubleNewline = String.fromCharCode(10) + String.fromCharCode(10);
    return str.split(doubleNewline).join('<br><br>');
}"""

content = content.replace(old_func, new_func)

# Also in promptText:
content = content.replace("promptText: `You have received a letter from a friend, Emily. She is going to visit Can Tho in December. Write a letter to give her some suggestions. You should tell her:\n• Where to stay\n• What dishes to try\n• Which tourist attractions to visit\n• What to wear\nYou should write at least 120 words. Do not include your name. Your response will be evaluated in terms of Task Fulfillment, Organization, Vocabulary, and Grammar.`",
'promptText: "You have received a letter from a friend, Emily. She is going to visit Can Tho in December. Write a letter to give her some suggestions. You should tell her:" + String.fromCharCode(10) + "• Where to stay" + String.fromCharCode(10) + "• What dishes to try" + String.fromCharCode(10) + "• Which tourist attractions to visit" + String.fromCharCode(10) + "• What to wear" + String.fromCharCode(10) + "You should write at least 120 words. Do not include your name. Your response will be evaluated in terms of Task Fulfillment, Organization, Vocabulary, and Grammar."')

# Also in sampleModel and sampleModelVi, use String.fromCharCode(10) or standard strings
sample_model_en = """`Dear Emily,` + String.fromCharCode(10) + String.fromCharCode(10) +
`Thanks for your letter. I hope you are doing well. I’m writing to give you some advice for your trip to Can Tho in December.` + String.fromCharCode(10) + String.fromCharCode(10) +
`Firstly, you should stay at a hotel near Ninh Kieu Wharf because it is very convenient to travel around the city. In addition, you can easily visit many famous restaurants and cafes in the evening. Secondly, it would be a good idea to try some delicious local dishes such as banh xeo, grilled snakehead fish, and fresh tropical fruits. These dishes are very famous in the Mekong Delta and can help you learn more about Vietnamese food culture. Next, if I were you, I would take a boat trip to Cai Rang Floating Market early in the morning and visit Binh Thuy Ancient House. These are the most popular tourist attractions in Can Tho. Finally, remember to wear light clothes and comfortable shoes because you will walk and explore a lot. You should also bring a hat and sunglasses to protect yourself from the sunlight.` + String.fromCharCode(10) + String.fromCharCode(10) +
`I hope my advice will be helpful to you. Please let me know how everything turns out. Write back soon.` + String.fromCharCode(10) + String.fromCharCode(10) +
`Best wishes,`"""

sample_model_vi = """`Emily thân mến,` + String.fromCharCode(10) + String.fromCharCode(10) +
`Cảm ơn thư của cậu. Tớ hy vọng cậu vẫn khỏe. Tớ viết thư này để đưa ra một vài gợi ý cho chuyến đi của cậu đến Cần Thơ vào tháng Mười Hai.` + String.fromCharCode(10) + String.fromCharCode(10) +
`Đầu tiên, cậu nên ở một khách sạn gần Bến Ninh Kiều vì nó rất thuận tiện cho việc đi lại quanh thành phố. Ngoài ra, cậu có thể dễ dàng ghé thăm nhiều nhà hàng và quán cà phê nổi tiếng vào buổi tối. Thứ hai, cậu nên thử một số món ăn địa phương thơm ngon như bánh xèo, cá lóc nướng và trái cây nhiệt đới tươi. Những món ăn này rất nổi tiếng ở miền Tây và giúp cậu hiểu thêm về văn hóa ẩm thực Việt Nam. Tiếp theo, nếu tớ là cậu, tớ sẽ đi thuyền tham quan Chợ nổi Cái Răng vào sáng sớm và ghé thăm Nhà cổ Bình Thủy. Đây là những điểm du lịch nổi tiếng nhất ở Cần Thơ. Cuối cùng, hãy nhớ mặc quần áo mỏng nhẹ và đi giày thoải mái vì cậu sẽ đi bộ và khám phá rất nhiều. Cậu cũng nên mang theo mũ và kính râm để bảo vệ bản thân khỏi ánh nắng mặt trời.` + String.fromCharCode(10) + String.fromCharCode(10) +
`Tớ hy vọng những lời khuyên của tớ sẽ giúp ích cho cậu. Hãy cho tớ biết chuyến đi diễn ra thế nào nhé. Hãy viết thư lại sớm nhé.` + String.fromCharCode(10) + String.fromCharCode(10) +
`Chúc cậu mọi điều tốt lành,`"""

# Replace sampleModel and sampleModelVi
import re
content = re.sub(r'sampleModel:\s*`Dear Emily,.*?`Best wishes,`', 'sampleModel: ' + sample_model_en, content, flags=re.DOTALL)
content = re.sub(r'sampleModelVi:\s*`Emily thân mến,.*?`Chúc cậu mọi điều tốt lành,`', 'sampleModelVi: ' + sample_model_vi, content, flags=re.DOTALL)

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated reconstruct_app.py with safe string concatenation!")
