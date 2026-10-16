const fs = require('fs');

const testStudentEssay = `Dear Emily,
Thank for your letter. I hope you are doing well. I’m writing to give you some advice for your trip to Can Tho in December.
Firstly, you should stay in hotel in the city center because it’s very convenient for travelling. Many famous places are also located near this area. Moreover, the prices are quite reasonable.
Secondly, it would be a good idea to try some traditional Vietnamese dishes such as lau mam, banh cong, and banh tet la cam. These dishes are very popular and delicious. Both locals and tourists enjoy them.
Next, if I were you, I would visit some famous places in Can Tho such as Ninh Kieu way, Cai Rang Floating Market, and My Khanh Tourist Village. These places are very beautiful and interesting. Besides, you can better understand the cultural of Can Tho.
Finally, remember to wear light and comfortable clothes because the weather in Can Tho can be very pleasant in December. For example, you can wear T-shirts and shorts. Don't forget to bring a light jacket and umbrella in case it rains.
I hope my advice will be helpful to you. Please let me know how everything turns out. Write back soon.
Best wishes,`;

// Extract diagnoseVstepErrors and buildAnnotatedEssayHtml from pure_extra_logic.js
const code = fs.readFileSync('/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/pure_extra_logic.js', 'utf8');

eval(code.substring(code.indexOf('function buildAnnotatedEssayHtml'), code.indexOf('function sendExtraPracticeReport')));
eval(code.substring(code.indexOf('function diagnoseVstepErrors'), code.indexOf('function buildAnnotatedEssayHtml')));

const errors = diagnoseVstepErrors(testStudentEssay, {});
console.log("Total errors detected:", errors.length);
errors.forEach((e, i) => {
    console.log(`${i+1}. [${e.type}] ${e.wrong} -> ${e.correct}`);
});

const annotated = buildAnnotatedEssayHtml(testStudentEssay, errors);
console.log("\nAnnotated HTML snippet:\n", annotated);
