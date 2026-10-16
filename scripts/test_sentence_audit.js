// Test sentence segmentation and auditing
function segmentLetterSentences(rawText) {
    if (!rawText) return [];
    let text = rawText.replace(/\r\n/g, '\n').replace(/\r/g, '\n');
    
    const abbrevs = ['mr\\.', 'mrs\\.', 'ms\\.', 'dr\\.', 'prof\\.', 'st\\.', 'e\\.g\\.', 'i\\.e\\.', 'etc\\.', 'vs\\.', 'a\\.m\\.', 'p\\.m\\.', 'no\\.'];
    abbrevs.forEach(abb => {
        const regex = new RegExp(`\\b${abb}`, 'gi');
        text = text.replace(regex, match => match.replace(/\./g, '\uE000'));
    });

    text = text.replace(/(\d+)\.(\d+)/g, '$1\uE000$2');

    // Split on period, exclamation, question mark, or newlines
    const rawSentences = text.split(/(?<=[.!?])\s+|\n+/);

    const sentences = [];
    rawSentences.forEach(s => {
        let clean = s.replace(/\uE000/g, '.').trim();
        if (clean.length > 0) {
            sentences.push(clean);
        }
    });

    return sentences;
}

const sampleLetter = `Dear Emily,
Thank for your letter. I am write this letter to give you some advice about your trip to Can Tho in December.
Firstly, you should staying at a hotel near Ninh Kieu Wharf because it convenient to travel.
Secondly, you must to try banh xeo and fresh fruits. They are very delicious.
In addition, you can visit Cai Rang floating market. You should wear light clothes because weather is warm.
I look forward to see you soon.
Best wishes,
Nguyet`;

const result = segmentLetterSentences(sampleLetter);
console.log("Total sentences segmented:", result.length);
result.forEach((s, i) => {
    console.log(`[${i + 1}] ${s}`);
});
