# Script to implement Extra Practice for Dạng 01 and setup the system
import json

extra_practice_data = {
    "advice": {
        "title": "BÀI LUYỆN TẬP THÊM - DẠNG 01: LETTER OF ADVICE",
        "prompt": """You have received a letter from a friend, Emily. She is going to visit Can Tho in December. Write a letter to give her some suggestions. You should tell her:
• Where to stay 
• What dishes to try 
• Which tourist attractions to visit 
• What to wear 
You should write at least 120 words. Do not include your name. Your response will be evaluated in terms of Task Fulfillment, Organization, Vocabulary, and Grammar.""",
        "hints": [
            {
                "title": "1. Where to stay (Nơi ở)",
                "items": [
                    {
                        "en": "stay at a hotel in the city centre",
                        "vi": "ở khách sạn tại trung tâm thành phố",
                        "reasonEn": "because it is convenient to travel around the city.",
                        "reasonVi": "vì thuận tiện để đi lại trong thành phố."
                    },
                    {
                        "en": "stay at a homestay near Ninh Kieu Wharf",
                        "vi": "ở homestay gần Bến Ninh Kiều",
                        "reasonEn": "because you can easily visit many famous places.",
                        "reasonVi": "vì bạn có thể dễ dàng tham quan nhiều địa điểm nổi tiếng."
                    },
                    {
                        "en": "choose a hotel with good reviews",
                        "vi": "chọn khách sạn có đánh giá tốt",
                        "reasonEn": "because you are more likely to have a comfortable stay.",
                        "reasonVi": "vì bạn sẽ có nhiều khả năng có một kỳ nghỉ thoải mái."
                    },
                    {
                        "en": "book your room in advance",
                        "vi": "đặt phòng trước",
                        "reasonEn": "because it helps you get a better price and avoid fully booked hotels.",
                        "reasonVi": "vì giúp bạn có giá tốt hơn và tránh tình trạng hết phòng."
                    }
                ]
            },
            {
                "title": "2. What dishes to try (Những món ăn nên thử)",
                "items": [
                    {
                        "en": "try local dishes such as banh xeo, grilled snakehead fish, and fresh fruits",
                        "vi": "thử các món ăn địa phương như bánh xèo, cá lóc nướng và trái cây tươi",
                        "reasonEn": "because they are some of the most famous dishes in Can Tho and the Mekong Delta.",
                        "reasonVi": "vì đây là những món ăn nổi tiếng nhất ở Cần Thơ và miền Tây."
                    },
                    {
                        "en": "try traditional Vietnamese dishes such as noodle soup, spring rolls, and banh cong",
                        "vi": "thử các món ăn truyền thống của Việt Nam như bún nước lèo, chả giò và bánh cống",
                        "reasonEn": "because they can help you learn more about Vietnamese food culture.",
                        "reasonVi": "vì chúng giúp bạn hiểu thêm về văn hóa ẩm thực Việt Nam."
                    },
                    {
                        "en": "eat at local night markets and try street food",
                        "vi": "ăn tại các chợ đêm địa phương và thử đồ ăn đường phố",
                        "reasonEn": "because you can enjoy authentic local food at reasonable prices.",
                        "reasonVi": "vì bạn có thể thưởng thức ẩm thực địa phương chính gốc với giá hợp lý."
                    }
                ]
            },
            {
                "title": "3. Which tourist attractions to visit (Những địa điểm nên tham quan)",
                "items": [
                    {
                        "en": "visit famous places such as Cai Rang Floating Market, Ninh Kieu Wharf, and Binh Thuy Ancient House",
                        "vi": "tham quan những địa điểm nổi tiếng như Chợ nổi Cái Răng, Bến Ninh Kiều và Nhà cổ Bình Thủy",
                        "reasonEn": "because they are some of the most famous tourist attractions in Can Tho.",
                        "reasonVi": "vì đây là những địa điểm du lịch nổi tiếng nhất ở Cần Thơ."
                    },
                    {
                        "en": "take a boat trip to Cai Rang Floating Market early in the morning",
                        "vi": "đi thuyền tham quan Chợ nổi Cái Răng vào sáng sớm",
                        "reasonEn": "because you can enjoy the lively atmosphere and learn more about river culture.",
                        "reasonVi": "vì bạn có thể tận hưởng không khí nhộn nhịp và tìm hiểu thêm về văn hóa sông nước."
                    },
                    {
                        "en": "visit local fruit orchards and eco-tourism villages",
                        "vi": "tham quan các vườn cây ăn trái địa phương và làng du lịch sinh thái",
                        "reasonEn": "because you can relax in nature and taste fresh tropical fruits.",
                        "reasonVi": "vì bạn có thể thư giãn giữa thiên nhiên và thưởng thức trái cây nhiệt đới tươi ngon."
                    }
                ]
            },
            {
                "title": "4. What to wear when visiting Can Tho (Nên mặc gì khi đến Cần Thơ)",
                "items": [
                    {
                        "en": "wear light clothes and comfortable shoes",
                        "vi": "mặc quần áo mỏng, nhẹ và mang giày thoải mái",
                        "reasonEn": "because the weather in December is pleasantly warm, and you may have to walk a lot.",
                        "reasonVi": "vì thời tiết tháng 12 ấm áp dễ chịu và bạn có thể phải đi bộ nhiều."
                    },
                    {
                        "en": "bring a hat, sunglasses, and sunscreen",
                        "vi": "mang theo mũ, kính râm và kem chống nắng",
                        "reasonEn": "because they can protect you from the strong sunlight when you take a boat tour.",
                        "reasonVi": "vì chúng có thể bảo vệ bạn khỏi ánh nắng gay gắt khi đi thuyền tham quan."
                    },
                    {
                        "en": "bring a light jacket for the cool evenings",
                        "vi": "mang theo áo khoác mỏng cho buổi tối mát mẻ",
                        "reasonEn": "because it can be slightly breezy near the river at night.",
                        "reasonVi": "vì trời có thể hơi lộng gió gần bờ sông vào ban đêm."
                    }
                ]
            }
        ],
        "sampleModel": """Dear Emily,

Thanks for your letter. I hope you are doing well. I’m writing to give you some advice for your trip to Can Tho in December.

Firstly, you should stay at a hotel near Ninh Kieu Wharf because it is very convenient to travel around the city. In addition, you can easily visit many famous restaurants and cafes in the evening. Secondly, it would be a good idea to try some delicious local dishes such as banh xeo, grilled snakehead fish, and fresh tropical fruits. These dishes are very famous in the Mekong Delta and can help you learn more about Vietnamese food culture. Next, if I were you, I would take a boat trip to Cai Rang Floating Market early in the morning and visit Binh Thuy Ancient House. These are the most popular tourist attractions in Can Tho. Finally, remember to wear light clothes and comfortable shoes because you will walk and explore a lot. You should also bring a hat and sunglasses to protect yourself from the sunlight.

I hope my advice will be helpful to you. Please let me know how everything turns out. Write back soon.

Best wishes,""",
        "sampleModelVi": """Emily thân mến,

Cảm ơn thư của cậu. Tớ hy vọng cậu vẫn khỏe. Tớ viết thư này để đưa ra một vài gợi ý cho chuyến đi của cậu đến Cần Thơ vào tháng Mười Hai.

Đầu tiên, cậu nên ở một khách sạn gần Bến Ninh Kiều vì nó rất thuận tiện cho việc đi lại quanh thành phố. Ngoài ra, cậu có thể dễ dàng ghé thăm nhiều nhà hàng và quán cà phê nổi tiếng vào buổi tối. Thứ hai, cậu nên thử một số món ăn địa phương thơm ngon như bánh xèo, cá lóc nướng và trái cây nhiệt đới tươi. Những món ăn này rất nổi tiếng ở miền Tây và giúp cậu hiểu thêm về văn hóa ẩm thực Việt Nam. Tiếp theo, nếu tớ là cậu, tớ sẽ đi thuyền tham quan Chợ nổi Cái Răng vào sáng sớm và ghé thăm Nhà cổ Bình Thủy. Đây là những điểm du lịch nổi tiếng nhất ở Cần Thơ. Cuối cùng, hãy nhớ mặc quần áo mỏng nhẹ và đi giày thoải mái vì cậu sẽ đi bộ và khám phá rất nhiều. Cậu cũng nên mang theo mũ và kính râm để bảo vệ bản thân khỏi ánh nắng mặt trời.

Tớ hy vọng những lời khuyên của tớ sẽ giúp ích cho cậu. Hãy cho tớ biết chuyến đi diễn ra thế nào nhé. Hãy viết thư lại sớm nhé.

Chúc cậu mọi điều tốt lành,""",
        "wordCount": 182
    }
}

print("Extra practice data prepared successfully.")
