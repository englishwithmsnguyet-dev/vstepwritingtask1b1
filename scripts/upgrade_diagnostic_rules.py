# -*- coding: utf-8 -*-
with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/pure_extra_logic.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# Let's inspect where diagnoseVstepErrors starts and ends
idx_start = js_code.find("function diagnoseVstepErrors(rawText, promptData) {")
idx_end = js_code.find("function gradeExtraPractice(typeId) {")

diagnostic_engine_js = """function diagnoseVstepErrors(rawText, promptData) {
    const errors = [];
    const lower = rawText.toLowerCase();

    // --- A. SALUTATION & GREETING ---
    if (/\\bDear\\s+emily\\b/i.test(rawText) && !/\\bDear\\s+Emily\\b/.test(rawText)) {
        errors.push({
            type: "Lời mở đầu (Chính tả)",
            category: "spelling",
            wrong: "Dear emily",
            correct: "Dear Emily,",
            reason: "Tên riêng 'Emily' bắt buộc phải viết hoa chữ cái đầu và có dấu phẩy sau lời chào."
        });
    }

    if (/\\bThank\\s+for\\b/i.test(rawText) && !/\\bThanks\\s+for\\b/i.test(rawText) && !/\\bThank\\s+you\\s+for\\b/i.test(rawText)) {
        errors.push({
            type: "Ngữ pháp / Lời mở đầu",
            category: "grammar",
            wrong: "Thank for your letter",
            correct: "Thanks for your letter / Thank you for your letter",
            reason: "Cụm từ cảm ơn mở thư đúng ngữ pháp phải có 's' ('Thanks for...') hoặc dùng 'Thank you for...'."
        });
    }

    if (/\\bI('m| am)\\s+write\\b/i.test(rawText)) {
        errors.push({
            type: "Thì của động từ (Tenses)",
            category: "grammar",
            wrong: "I am write / I'm write",
            correct: "I am writing / I'm writing",
            reason: "Sau to be (am/is/are) trong thì hiện tại tiếp diễn phải dùng V-ing ('I am writing to...')."
        });
    }

    if (/\\bhope\\s+you\\s+well\\b/i.test(rawText) && !/\\bhope\\s+you\\s+are\\s+well\\b/i.test(rawText) && !/\\bhope\\s+you\\s+are\\s+doing\\s+well\\b/i.test(rawText)) {
        errors.push({
            type: "Cấu trúc câu (Thiếu động từ)",
            category: "grammar",
            wrong: "hope you well",
            correct: "hope you are well / hope you are doing well",
            reason: "Thiếu to be 'are' hoặc trợ động từ: 'I hope you are well' hoặc 'I hope you are doing well'."
        });
    }

    if (/\\bBest\\s+wish\\b/i.test(rawText) && !/\\bBest\\s+wishes\\b/i.test(rawText)) {
        errors.push({
            type: "Lời chào kết thúc",
            category: "spelling",
            wrong: "Best wish",
            correct: "Best wishes,",
            reason: "Lời chào kết thư chuẩn là 'Best wishes,' (danh từ số nhiều có 'es' kèm dấu phẩy)."
        });
    }

    if (/\\bYours\\s+sincere\\b/i.test(rawText)) {
        errors.push({
            type: "Lời chào kết thúc",
            category: "grammar",
            wrong: "Yours sincere",
            correct: "Yours sincerely,",
            reason: "Cần dùng trạng từ: 'Yours sincerely,'."
        });
    }

    // --- B. ARTICLES (A / AN / THE / ZERO ARTICLE) ---
    const rStayHotel = /\\bstay\\s+(in|at)\\s+(hotel|homestay)\\b/gi;
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

    // Catch missing article with singular nouns after verbs
    const rSingularItems = /\\b(wear|bring|take|buy|choose|visit|rent|book)\\s+(ba\\s*ba\\s+shirt|shirt|dress|hat|jacket|camera|conical\\s+hat|umbrella|raincoat|room|hotel|homestay|taxi|bus|boat|museum|market|temple|pagoda)\\b/gi;
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

    // Catch missing article with "and/or + singular noun" (e.g. "a jacket and umbrella" -> "a jacket and an umbrella")
    const rAndSingular = /\\b(and|or)\\s+(umbrella|raincoat|camera|hat|jacket|shirt|conical\\s+hat|map|guide)\\b/gi;
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

    if (/\\bin\\s+city\\s+center\\b/gi.test(rawText) || /\\bin\\s+city\\s+centre\\b/gi.test(rawText)) {
        errors.push({
            type: "Mạo từ (Articles)",
            category: "article",
            wrong: "in city center",
            correct: "in the city center",
            reason: "Cụm từ chỉ trung tâm thành phố cần mạo từ xác định 'the': 'in the city center'."
        });
    }

    if (/\\b(in\\s+morning|in\\s+afternoon|in\\s+evening)\\b/gi.test(rawText)) {
        const m = rawText.match(/\\b(in\\s+morning|in\\s+afternoon|in\\s+evening)\\b/i);
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

    if (/\\bby\\s+a\\s+(bus|taxi|car|train|plane|boat)\\b/gi.test(rawText)) {
        const m = rawText.match(/\\bby\\s+a\\s+(bus|taxi|car|train|plane|boat)\\b/i);
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

    // --- C. UNCOUNTABLE NOUNS ---
    if (/\\b(advices|an\\s+advice)\\b/gi.test(rawText)) {
        const m = rawText.match(/\\b(advices|an\\s+advice)\\b/i);
        errors.push({
            type: "Danh từ không đếm được",
            category: "grammar",
            wrong: m ? m[0] : "advices",
            correct: "some advice / a piece of advice",
            reason: "'advice' là danh từ không đếm được, không thêm 's' và không dùng mạo từ 'an'."
        });
    }

    if (/\\b(informations|an\\s+information)\\b/gi.test(rawText)) {
        const m = rawText.match(/\\b(informations|an\\s+information)\\b/i);
        errors.push({
            type: "Danh từ không đếm được",
            category: "grammar",
            wrong: m ? m[0] : "informations",
            correct: "some information / a piece of information",
            reason: "'information' là danh từ không đếm được, không có dạng số nhiều 'informations'."
        });
    }

    if (/\\bclothings\\b/gi.test(rawText)) {
        errors.push({
            type: "Danh từ không đếm được",
            category: "grammar",
            wrong: "clothings",
            correct: "clothes / clothing",
            reason: "'clothing' không đếm được (không có 's'). Nếu muốn chỉ quần áo nói chung, hãy dùng 'clothes'."
        });
    }

    // --- D. PARTS OF SPEECH & CONFUSING WORDS ---
    if (/\\bthe\\s+cultural\\s+of\\b/gi.test(rawText)) {
        errors.push({
            type: "Từ loại (Part of Speech)",
            category: "vocab",
            wrong: "the cultural of Can Tho",
            correct: "the culture of Can Tho / the cultural identity of Can Tho",
            reason: "'cultural' là tính từ. Đứng sau mạo từ 'the' và trước 'of' bắt buộc phải dùng danh từ 'culture'."
        });
    }

    if (/\\bvery\\s+beauty\\b/gi.test(rawText)) {
        errors.push({
            type: "Từ loại (Part of Speech)",
            category: "vocab",
            wrong: "very beauty",
            correct: "very beautiful",
            reason: "Sau phó từ 'very' bổ nghĩa cho địa điểm/cảnh quan phải dùng tính từ 'beautiful', không dùng danh từ 'beauty'."
        });
    }

    if (/\\bdeliciously\\s+(food|dishes|fruits)\\b/gi.test(rawText)) {
        const m = rawText.match(/\\bdeliciously\\s+(food|dishes|fruits)\\b/i);
        errors.push({
            type: "Từ loại (Part of Speech)",
            category: "vocab",
            wrong: m ? m[0] : "deliciously food",
            correct: m ? m[0].replace('deliciously', 'delicious') : "delicious food",
            reason: "Đứng trước danh từ phải dùng tính từ 'delicious' để bổ nghĩa, không dùng trạng từ 'deliciously'."
        });
    }

    if (/\\btradition\\s+(dishes|food|clothes|costumes)\\b/gi.test(rawText)) {
        const m = rawText.match(/\\btradition\\s+(dishes|food|clothes|costumes)\\b/i);
        errors.push({
            type: "Từ loại (Part of Speech)",
            category: "vocab",
            wrong: m ? m[0] : "tradition dishes",
            correct: m ? m[0].replace('tradition', 'traditional') : "traditional dishes",
            reason: "Cần dùng tính từ 'traditional' để bổ nghĩa cho danh từ, không dùng danh từ 'tradition'."
        });
    }

    if (/\\bfame\\s+places\\b/gi.test(rawText)) {
        errors.push({
            type: "Từ loại (Part of Speech)",
            category: "vocab",
            wrong: "fame places",
            correct: "famous places",
            reason: "Cần dùng tính từ 'famous' trước danh từ 'places', không dùng danh từ 'fame'."
        });
    }

    if (/\\b(give|give you)\\s+some\\s+advise\\b/gi.test(rawText)) {
        errors.push({
            type: "Cặp từ dễ nhầm lẫn",
            category: "vocab",
            wrong: "give you some advise",
            correct: "give you some advice",
            reason: "'advise' là động từ (khuyên bảo). Danh từ 'lời khuyên' phải viết là 'advice' (đuôi -ce)."
        });
    }

    // Specific local collocation
    if (/\\bNinh\\s+Kieu\\s+way\\b/gi.test(rawText)) {
        errors.push({
            type: "Dùng từ / Địa danh",
            category: "vocab",
            wrong: "Ninh Kieu way",
            correct: "Ninh Kieu Wharf / Ninh Kieu Pedestrian Bridge",
            reason: "Địa danh Bến Ninh Kiều dùng 'Wharf', Cầu đi bộ dùng 'Pedestrian Bridge', không dùng 'way'."
        });
    }

    // --- E. ADVICE STRUCTURES & VERB PATTERNS ---
    if (/\\bshould\\s+to\\s+[a-z]+\\b/gi.test(rawText)) {
        const m = rawText.match(/\\bshould\\s+to\\s+([a-z]+)\\b/i);
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

    if (/\\bshould\\s+(stays|wears|brings|tries|visits|goes|buys)\\b/gi.test(rawText)) {
        const m = rawText.match(/\\bshould\\s+([a-z]+)\\b/i);
        if (m) {
            errors.push({
                type: "Cấu trúc động từ khuyết thiếu",
                category: "grammar",
                wrong: m[0],
                correct: `should ${m[1].replace(/s$/, '')}`,
                reason: "Sau 'should' động từ luôn ở dạng nguyên mẫu không chia (Vo)."
            });
        }
    }

    if (/\\bwould\\s+be\\s+a\\s+good\\s+idea\\s+(try|stay|visit|wear|bring|go)\\b/gi.test(rawText)) {
        const m = rawText.match(/\\bwould\\s+be\\s+a\\s+good\\s+idea\\s+([a-z]+)\\b/i);
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

    if (/\\bIf\\s+I\\s+was\\s+you\\b/gi.test(rawText)) {
        errors.push({
            type: "Câu điều kiện loại 2",
            category: "grammar",
            wrong: "If I was you",
            correct: "If I were you",
            reason: "Trong câu điều kiện loại 2 giả định lời khuyên, to be luôn dùng 'were' cho tất cả các ngôi."
        });
    }

    if (/\\bIf\\s+I\\s+were\\s+you,\\s*I\\s+will\\b/gi.test(rawText)) {
        errors.push({
            type: "Câu điều kiện loại 2",
            category: "grammar",
            wrong: "If I were you, I will",
            correct: "If I were you, I would",
            reason: "Mệnh đề chính của câu điều kiện loại 2 phải dùng 'would + Vo' (không dùng 'will')."
        });
    }

    if (/\\b(remember|don't\\s+forget)\\s+(wear|bring|take|try|visit|stay)\\b/gi.test(rawText)) {
        const m = rawText.match(/\\b(remember|don't\\s+forget)\\s+([a-z]+)\\b/i);
        if (m) {
            errors.push({
                type: "Dạng động từ (Verb Patterns)",
                category: "grammar",
                wrong: m[0],
                correct: `${m[1]} to ${m[2]}`,
                reason: `Cấu trúc nhắc nhở làm việc gì: '${m[1]} TO + Vo' (ví dụ: ${m[1]} to ${m[2]}).`
            });
        }
    }

    if (/\\bsuggest\\s+you\\s+to\\s+[a-z]+\\b/gi.test(rawText)) {
        const m = rawText.match(/\\bsuggest\\s+you\\s+to\\s+([a-z]+)\\b/i);
        if (m) {
            errors.push({
                type: "Cấu trúc với 'Suggest'",
                category: "grammar",
                wrong: m[0],
                correct: `suggest that you should ${m[1]} (hoặc: suggest ${m[1]}ing)`,
                reason: "Động từ 'suggest' không đi với 'suggest someone to do sth'. Cần dùng 'suggest (that) you (should) do sth' hoặc 'suggest V-ing'."
            });
        }
    }

    // --- F. PREPOSITIONS ---
    if (/\\b(on\\s+December|at\\s+December|on\\s+January|on\\s+February|on\\s+June|on\\s+July)\\b/gi.test(rawText)) {
        const m = rawText.match(/\\b(on|at)\\s+(December|January|February|March|April|May|June|July|August|September|October|November)\\b/i);
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

    if (/\\bin\\s+(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\\b/gi.test(rawText)) {
        const m = rawText.match(/\\bin\\s+(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\\b/i);
        if (m) {
            errors.push({
                type: "Giới từ chỉ thời gian",
                category: "grammar",
                wrong: m[0],
                correct: `on ${m[1]}`,
                reason: `Trước các thứ trong tuần dùng giới từ 'on' (on ${m[1]}).`
            });
        }
    }

    if (/\\barrive\\s+to\\s+Can\\s+Tho\\b/gi.test(rawText)) {
        errors.push({
            type: "Giới từ chỉ nơi chốn",
            category: "grammar",
            wrong: "arrive to Can Tho",
            correct: "arrive in Can Tho",
            reason: "Đến một thành phố/quốc gia dùng 'arrive in' (arrive in Can Tho), không dùng 'arrive to'."
        });
    }

    if (/\\bfamous\\s+with\\b/gi.test(rawText)) {
        errors.push({
            type: "Giới từ đi kèm tính từ",
            category: "grammar",
            wrong: "famous with",
            correct: "famous for",
            reason: "Nổi tiếng về điều gì dùng cấu trúc 'famous for', không dùng 'famous with'."
        });
    }

    // --- G. SENTENCE STRUCTURE & CONJUNCTIONS ---
    if (/the weather in Can Tho can be very pleasant in December and an ideal time/i.test(rawText)) {
        errors.push({
            type: "Cấu trúc câu (Sentence Structure)",
            category: "grammar",
            wrong: "...because the weather in Can Tho can be very pleasant in December and an ideal time for tourism.",
            correct: "...because the weather in Can Tho is very pleasant in December, making it an ideal time for tourism (hoặc: and December is an ideal time for tourism).",
            reason: "Lỗi cấu trúc câu không song hành: 'weather' (thời tiết) không thể là 'an ideal time' (khoảng thời gian). Cần dùng mệnh đề phân từ 'making it an ideal time' hoặc tách mệnh đề."
        });
    }

    if (/\\bAlthough\\b[^.!?\\n]+,\\s*but\\b/gi.test(rawText)) {
        errors.push({
            type: "Cấu trúc liên từ kép",
            category: "grammar",
            wrong: "Although ..., but ...",
            correct: "Although ... [không dùng 'but'] (hoặc chỉ dùng '... but ...')",
            reason: "Trong tiếng Anh không dùng song song 'Although' và 'but' trong cùng một câu."
        });
    }

    if (/\\bBecause\\b[^.!?\\n]+,\\s*so\\b/gi.test(rawText)) {
        errors.push({
            type: "Cấu trúc liên từ kép",
            category: "grammar",
            wrong: "Because ..., so ...",
            correct: "Because ... [không dùng 'so'] (hoặc chỉ dùng '... so ...')",
            reason: "Trong tiếng Anh không dùng song song 'Because' và 'so' trong cùng một câu."
        });
    }

    // Missing comma after transition words at beginning of sentence
    const transitions = [
        "Firstly", "Secondly", "Finally", "Moreover", "Besides",
        "Furthermore", "In addition", "Therefore", "For example", "However"
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

    // --- H. SUBJECT-VERB AGREEMENT & COMMON SPELLINGS ---
    if (/\\b(places|dishes|clothes)\\s+is\\b/gi.test(rawText)) {
        const m = rawText.match(/\\b(places|dishes|clothes)\\s+is\\b/i);
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

    // Lowercase 'i' as subject pronoun
    const rLowerI = /(^|\\s)i\\s+(am|hope|think|want|would|will|can|suggest|recommend)\\b/g;
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

    // Common spelling errors dictionary
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
        "tourist attraction": "tourist attractions"
    };

    Object.keys(spellingDict).forEach(wrongWord => {
        const rWord = new RegExp(`\\\\b${wrongWord}\\\\b`, 'gi');
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

    // Punctuation spacing errors
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

    const spaceBeforePunct = rawText.match(/[a-zA-Z0-9]+\\s+[.,!?:;]/g);
    if (spaceBeforePunct && spaceBeforePunct.length > 0) {
        spaceBeforePunct.forEach(se => {
            errors.push({
                type: "Quy cách dấu câu",
                category: "punctuation",
                wrong: se,
                correct: se.replace(/\\s+([.,!?:;])/, '$1'),
                reason: "Không đặt dấu cách trước các dấu chấm, phẩy, chấm hỏi, chấm than."
            });
        });
    }

    return errors;
}
"""

js_code = js_code[:idx_start] + diagnostic_engine_js.strip() + "\n\n" + js_code[idx_end:]

# Now let's enhance gradeExtraPractice to build the Annotated Essay View and Actionable Suggestions
with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/pure_extra_logic.js", "w", encoding="utf-8") as f:
    f.write(js_code)

print("Updated pure_extra_logic.js with ultra diagnostic engine!")
