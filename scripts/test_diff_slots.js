// Test script for slot-aware diffWords
function preProcess(t) {
    return t
        .replace(/…/g, '...')
        .replace(/\.\s*\.\s*\./g, '...')
        .replace(/[’‘]/g, "'")
        .replace(/[“”]/g, '"')
        .replace(/\s*[-‐‑–—−]+\s*/g, ' - ')
        .replace(/\s*\+\s*/g, ' + ')
        .replace(/(^|[^a-zA-Z0-9])([vV][0oO])([^a-zA-Z0-9]|$)/g, '$1Vo$3');
}

function clean(w) {
    let s = w.toLowerCase().trim();
    s = s.replace(/(^|[^a-z0-9])v0([^a-z0-9]|$)/gi, '$1vo$2');
    s = s.replace(/^v0$/, 'vo');
    return s;
}

function diffWords(userText, targetText) {
    const rawUser = preProcess(userText).trim();
    const rawTarget = preProcess(targetText).trim();

    // Check if target has bracketed slots
    const slotMatches = [...rawTarget.matchAll(/\[([^\]]+)\]/g)];
    
    if (slotMatches.length > 0) {
        const slots = slotMatches.map(m => m[1]);
        const parts = rawTarget.split(/\[[^\]]+\]/);

        // 1. Try template regex match (English skeleton matches + slots filled)
        let pattern = '^\\s*';
        for (let i = 0; i < slots.length; i++) {
            const pStr = parts[i].trim();
            if (pStr) {
                const words = pStr.split(/\s+/).map(w => w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'));
                pattern += words.join('\\s*') + '\\s*(.+?)\\s*';
            } else {
                pattern += '(.+?)\\s*';
            }
        }
        const pLast = parts[parts.length - 1].trim();
        if (pLast) {
            const lastWords = pLast.split(/\s+/).map(w => w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'));
            pattern += lastWords.join('\\s*');
        }
        pattern += '\\s*$';

        const templateRegex = new RegExp(pattern, 'i');
        const tm = rawUser.match(templateRegex);

        if (tm) {
            // Perfect match! Every slot is filled and all English words match!
            const diff = [];
            for (let i = 0; i < slots.length; i++) {
                const pWords = parts[i].trim().split(/\s+/).filter(w => w);
                for (const pw of pWords) {
                    diff.push({ word: pw, targetWord: pw, type: 'match' });
                }
                const userSlotVal = tm[i + 1].trim();
                diff.push({
                    word: userSlotVal,
                    targetWord: `[${slots[i]}]`,
                    type: 'match'
                });
            }
            const pLastWords = parts[parts.length - 1].trim().split(/\s+/).filter(w => w);
            for (const pw of pLastWords) {
                diff.push({ word: pw, targetWord: pw, type: 'match' });
            }

            return {
                diff,
                accuracy: 100,
                isPerfect: true
            };
        }

        // 2. Fallback: normalize slots into tokens for LCS alignment
        let uNorm = rawUser;
        let tNorm = rawTarget;
        const slotValues = {};

        // Check if user explicitly used brackets
        const userBrackets = [...rawUser.matchAll(/\[([^\]]+)\]/g)].map(m => m[1]);
        if (userBrackets.length === slots.length) {
            for (let i = 0; i < slots.length; i++) {
                const tok = `__SLOT_${i}__`;
                uNorm = uNorm.replace(`[${userBrackets[i]}]`, ` ${tok} `);
                tNorm = tNorm.replace(`[${slots[i]}]`, ` ${tok} `);
                slotValues[tok] = {
                    user: `[${userBrackets[i]}]`,
                    target: `[${slots[i]}]`
                };
            }
        } else {
            // Try anchor-based slot extraction
            for (let i = 0; i < slots.length; i++) {
                const tok = `__SLOT_${i}__`;
                tNorm = tNorm.replace(`[${slots[i]}]`, ` ${tok} `);

                const beforeWords = parts[i].trim().split(/\s+/).filter(w => w);
                const afterWords = parts[i + 1].trim().split(/\s+/).filter(w => w);
                const anchorB = beforeWords.length > 0 ? beforeWords[beforeWords.length - 1].replace(/[.*+?^${}()|[\]\\]/g, '\\$&') : '';
                const anchorA = afterWords.length > 0 ? afterWords[0].replace(/[.*+?^${}()|[\]\\]/g, '\\$&') : '';

                let extractedUserSlot = '';
                if (anchorB && anchorA) {
                    const subReg = new RegExp(`(\\b${anchorB}\\b\\s*)(.+?)(\\s*${anchorA})`, 'i');
                    const sm = uNorm.match(subReg);
                    if (sm && sm[2].trim()) {
                        extractedUserSlot = sm[2].trim();
                        uNorm = uNorm.replace(subReg, `$1 ${tok} $3`);
                    }
                } else if (anchorB) {
                    const subReg = new RegExp(`(\\b${anchorB}\\b\\s*)(.+?)(\\s*[,.!?]|$)`, 'i');
                    const sm = uNorm.match(subReg);
                    if (sm && sm[2].trim()) {
                        extractedUserSlot = sm[2].trim();
                        uNorm = uNorm.replace(subReg, `$1 ${tok} $3`);
                    }
                }

                slotValues[tok] = {
                    user: extractedUserSlot || `[${slots[i]}]`,
                    target: `[${slots[i]}]`
                };
            }
        }

        // Run LCS on normalized strings
        const uWords = uNorm.trim().split(/\s+/).filter(w => w !== '');
        const tWords = tNorm.trim().split(/\s+/).filter(w => w !== '');

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
                const uW = uWords[i - 1];
                const tW = tWords[j - 1];
                if (slotValues[tW]) {
                    diff.unshift({
                        word: slotValues[tW].user,
                        targetWord: slotValues[tW].target,
                        type: 'match'
                    });
                } else {
                    diff.unshift({ word: uW, targetWord: tW, type: 'match' });
                }
                i--;
                j--;
            } else if (j > 0 && (i === 0 || dp[i][j - 1] >= dp[i - 1][j])) {
                const tW = tWords[j - 1];
                diff.unshift({
                    word: slotValues[tW] ? slotValues[tW].target : tW,
                    targetWord: slotValues[tW] ? slotValues[tW].target : tW,
                    type: 'missing'
                });
                j--;
            } else {
                const uW = uWords[i - 1];
                diff.unshift({
                    word: slotValues[uW] ? slotValues[uW].user : uW,
                    type: 'extra'
                });
                i--;
            }
        }

        const matchCount = diff.filter(d => d.type === 'match').length;
        const maxWords = Math.max(tWords.length, uWords.length);
        const accuracy = maxWords > 0 ? Math.round((matchCount / maxWords) * 100) : 0;

        return {
            diff,
            accuracy,
            isPerfect: matchCount === tWords.length && uWords.length === tWords.length
        };
    }

    // Standard LCS for targets without brackets
    const uWords = rawUser.split(/\s+/).filter(w => w !== '');
    const tWords = rawTarget.split(/\s+/).filter(w => w !== '');
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
            diff.unshift({ word: uWords[i - 1], targetWord: tWords[j - 1], type: 'match' });
            i--;
            j--;
        } else if (j > 0 && (i === 0 || dp[i][j - 1] >= dp[i - 1][j])) {
            diff.unshift({ word: tWords[j - 1], targetWord: tWords[j - 1], type: 'missing' });
            j--;
        } else {
            diff.unshift({ word: uWords[i - 1], type: 'extra' });
            i--;
        }
    }

    const matchCount = diff.filter(d => d.type === 'match').length;
    const maxWords = Math.max(tWords.length, uWords.length);
    const accuracy = maxWords > 0 ? Math.round((matchCount / maxWords) * 100) : 0;

    return {
        diff,
        accuracy,
        isPerfect: matchCount === tWords.length && uWords.length === tWords.length
    };
}

// Run test cases
const tests = [
    { u: 'Dear Helen,', t: 'Dear [tên của người nhận],' },
    { u: 'Dear [tên người nhận],', t: 'Dear [tên của người nhận],' },
    { u: 'Dear tên người nhận,', t: 'Dear [tên của người nhận],' },
    { u: 'Dear [Helen],', t: 'Dear [tên của người nhận],' },
    { u: 'The main problem was that the changing room was dirty.', t: 'The main problem was that [vấn đề 1].' },
    { u: 'The main problem was that phòng thay đồ rất bẩn.', t: 'The main problem was that [vấn đề 1].' },
    { u: 'I am writing to complain about bad service. I recently used your room and was not satisfied with it.',
      t: 'I am writing to complain about [vấn đề cần phàn nàn]. I recently used your [sản phẩm/dịch vụ] and was not satisfied with it.' },
    { u: 'I write to complain about bad service. I recently used your room and was not satisfied with it.',
      t: 'I am writing to complain about [vấn đề cần phàn nàn]. I recently used your [sản phẩm/dịch vụ] and was not satisfied with it.' }
];

tests.forEach((tc, idx) => {
    const res = diffWords(tc.u, tc.t);
    console.log(`Test ${idx + 1}:`);
    console.log(`  User:   "${tc.u}"`);
    console.log(`  Target: "${tc.t}"`);
    console.log(`  Accuracy: ${res.accuracy}% | isPerfect: ${res.isPerfect}`);
    console.log('  Diff items:');
    res.diff.forEach(d => console.log(`    [${d.type}] word="${d.word}" targetWord="${d.targetWord || ''}"`));
    console.log();
});
