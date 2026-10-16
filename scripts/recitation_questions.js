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
