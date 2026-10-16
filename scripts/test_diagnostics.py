import re

student_essay = """Dear Emily,
Thank for your letter. I hope you are doing well. I’m writing to give you some advice for your trip to Can Tho in December.
Firstly, you should stay in hotel in the city center because it’s very convenient for travelling. Many famous places are also located near this area. Moreover, the prices are quite reasonable.
Secondly, it would be a good idea to try some traditional Vietnamese dishes such as lau mam, banh cong, and banh tet la cam. These dishes are very popular and delicious. Both locals and tourists enjoy them.
Next, if I were you, I would visit some famous places in Can Tho such as Ninh Kieu way, Cai Rang Floating Market, and My Khanh Tourist Village. These places are very beautiful and interesting. Besides, you can better understand the cultural of Can Tho.
Finally, remember to wear light and comfortable clothes because the weather in Can Tho can be very pleasant in December and an ideal time for tourism. For example, you can wear Ba Ba shirt. Don't forget to bring conical hat.
I hope my advice will be helpful to you. Please let me know how everything turns out. Write back soon.
Best wishes,"""

def analyze_essay(text):
    errors = []
    
    # 1. Thank for -> Thanks for / Thank you for
    if re.search(r'\bThank\s+for\b', text, re.IGNORECASE):
        errors.append({
            "type": "Grammar / Opening",
            "wrong": "Thank for your letter",
            "correct": "Thanks for your letter / Thank you for your letter",
            "reason": "Cụm từ cảm ơn đúng ngữ pháp phải là 'Thanks for...' (có 's') hoặc 'Thank you for...'."
        })
        
    # 2. Missing articles with singular countable nouns
    # stay in hotel / at hotel
    if re.search(r'\bstay\s+(in|at)\s+hotel\b', text, re.IGNORECASE):
        errors.append({
            "type": "Article (Mạo từ)",
            "wrong": "stay in hotel",
            "correct": "stay in a hotel / stay at a hotel",
            "reason": "Danh từ đếm được số ít 'hotel' bắt buộc phải có mạo từ 'a' phía trước."
        })
        
    # wear Ba Ba shirt / wear shirt
    if re.search(r'\bwear\s+(ba\s*ba\s+)?shirt\b', text, re.IGNORECASE):
        errors.append({
            "type": "Article (Mạo từ)",
            "wrong": "wear Ba Ba shirt",
            "correct": "wear a Ba Ba shirt / wear traditional Ba Ba clothes",
            "reason": "Danh từ số ít 'shirt' cần mạo từ 'a' (a Ba Ba shirt) hoặc dùng danh từ số nhiều 'clothes'."
        })
        
    # bring conical hat / wear conical hat
    if re.search(r'\b(bring|wear)\s+conical\s+hat\b', text, re.IGNORECASE):
        errors.append({
            "type": "Article (Mạo từ)",
            "wrong": "bring conical hat",
            "correct": "bring a conical hat",
            "reason": "Danh từ số ít 'conical hat' (nón lá) bắt buộc phải có mạo từ 'a'."
        })
        
    # 3. Word Choice / Collocation / Proper names
    # Ninh Kieu way
    if re.search(r'\bNinh\s+Kieu\s+way\b', text, re.IGNORECASE):
        errors.append({
            "type": "Vocabulary / Collocation",
            "wrong": "Ninh Kieu way",
            "correct": "Ninh Kieu Wharf / Ninh Kieu Pedestrian Bridge",
            "reason": "Địa danh Bến Ninh Kiều trong tiếng Anh chuẩn là 'Ninh Kieu Wharf' (hoặc Cầu đi bộ là 'Ninh Kieu Pedestrian Bridge'), không dùng 'way'."
        })
        
    # 4. Part of speech error: the cultural of
    if re.search(r'\bthe\s+cultural\s+of\b', text, re.IGNORECASE):
        errors.append({
            "type": "Word Form (Từ loại)",
            "wrong": "the cultural of Can Tho",
            "correct": "the culture of Can Tho / the cultural identity of Can Tho",
            "reason": "'cultural' là tính từ (Adjective). Sau mạo từ 'the' và trước giới từ 'of' cần dùng danh từ 'culture' (Noun)."
        })
        
    # 5. Parallelism / Clause structure error
    if re.search(r'weather.*?can be.*?and an ideal time', text, re.IGNORECASE):
        errors.append({
            "type": "Sentence Structure (Cấu trúc câu)",
            "wrong": "...because the weather in Can Tho can be very pleasant in December and an ideal time for tourism.",
            "correct": "...because the weather in Can Tho is very pleasant in December, making it an ideal time for tourism (hoặc: and December is an ideal time for tourism).",
            "reason": "Lỗi cấu trúc câu không song hành: 'weather' (thời tiết) không thể là 'an ideal time' (một khoảng thời gian lý tưởng). Cần tách mệnh đề hoặc dùng phân từ 'making it an ideal time'."
        })

    return errors

detected = analyze_essay(student_essay)
print(f"Total errors found: {len(detected)}")
for idx, err in enumerate(detected, 1):
    print(f"{idx}. [{err['type']}]")
    print(f"   Wrong:   {err['wrong']}")
    print(f"   Correct: {err['correct']}")
    print(f"   Reason:  {err['reason']}\n")
