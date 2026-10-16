
function diffWords(userText, targetText) {
    const preProcess = (t) => t
        .replace(/…/g, '...')
        .replace(/\.\s*\.\s*\./g, '...')
        .replace(/[’‘]/g, "'")
        .replace(/[“”]/g, '"')
        .replace(/\s*[-‐‑–—−]+\s*/g, ' - ')
        .replace(/\s*\+\s*/g, ' + ')
        .replace(/(^|[^a-zA-Z0-9])([vV][0oO])([^a-zA-Z0-9]|$)/g, '$1Vo$3');
        
    const clean = (w) => {
        let s = w.toLowerCase().trim();
        s = s.replace(/(^|[^a-z0-9])v0([^a-z0-9]|$)/gi, '$1vo$2');
        s = s.replace(/^v0$/, 'vo');
        return s;
    };
    
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

const tests = [
    { target: "You should + Vo.", user: "You should + Vo." },
    { target: "You should + Vo.", user: "You should + V0." },
    { target: "You should + Vo.", user: "You should + VO." },
    { target: "You should + Vo.", user: "You should + v0." },
    { target: "You should + Vo.", user: "You should + vo." },
    { target: "You should + Vo.", user: "You should +V0." },
    { target: "I’m really sorry that I couldn’t [hành động – Vo] because [lý do].", user: "I'm really sorry that I couldn't [hành động - V0] because [lý do]." },
    { target: "I’m really sorry that I couldn’t [hành động – Vo] because [lý do].", user: "I’m really sorry that I couldn’t [hành động – VO] because [lý do]." },
    { target: "If I were you, I would + Vo.", user: "If I were you, I would + v0." }
];

tests.forEach((t, idx) => {
    const res = diffWords(t.user, t.target);
    console.log(`Test ${idx + 1}: isPerfect=${res.isPerfect}, accuracy=${res.accuracy}%`);
    if (!res.isPerfect) {
        console.log("  Diff:", JSON.stringify(res.diff));
    }
});
