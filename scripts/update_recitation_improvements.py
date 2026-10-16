# -*- coding: utf-8 -*-
import os

dom_path = "/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/dom_logic_full.js"

with open(dom_path, "r", encoding="utf-8") as f:
    dom_code = f.read()

# 1. Subtle Hint Generation Function
new_get_hint_text = r'''
// Generate subtle hint: triggers recall with starting phrases without being overly revealing
function getHintText(target) {
    if (!target) return '';
    target = target.trim();

    // Handle alternative structure targets like 'Remember to + Vo. / Don’t forget to + Vo.'
    if (target.includes(' / ') && (target.includes('+ Vo') || target.includes('+ Ving') || target.includes('Don’t forget'))) {
        const options = target.split(' / ');
        const hintOpts = options.map(opt => getHintText(opt));
        return hintOpts.join(' / ');
    }

    const targetClean = target
        .replace(/\s*\/\s*quite unhappy/i, '')
        .replace(/on\/in/g, 'on/in');

    const sentences = targetClean.split(/(?<=[.?!;])\s+/);
    const cues = [];

    for (const s of sentences) {
        const sTrim = s.trim();
        if (!sTrim) continue;

        const hasVo = /\+\s*vo\b/i.test(sTrim);
        const hasVing = /\+\s*ving\b/i.test(sTrim);

        // Replace bracket descriptions with subtle placeholder [tên...]
        const sDisplay = sTrim.replace(/\[([^\]\s]+)[^\]]*\]/g, '[$1...]');
        const words = sDisplay.split(/\s+/);

        if (words.length <= 2) {
            if (words[0].toLowerCase() === 'best' && words.length >= 2) {
                cues.push(`${words[0]} ${words[1][0]}...,`);
            } else if (words[0].toLowerCase() === 'yours' && words.length >= 2) {
                cues.push(`${words[0]} ${words[1][0]}...,`);
            } else {
                cues.push(words.join(' '));
            }
        } else {
            const lowerS = sTrim.toLowerCase();
            let num = 2;
            if (lowerS.startsWith('i would like to')) {
                num = 5; // e.g. "I would like to know..." / "I would like to inquire..."
            } else if (lowerS.startsWith('could you') || lowerS.startsWith('can you')) {
                num = 4; // e.g. "Could you provide me..." / "Can you give me..."
            } else if (lowerS.startsWith('i want to') || lowerS.startsWith('i want more')) {
                num = 4; // e.g. "I want to know..." / "I want more information..."
            } else if (lowerS.startsWith('the quality of') || lowerS.startsWith('one thing that') || lowerS.startsWith('to enhance the')) {
                num = 4;
            } else if (words.length >= 7) {
                num = 3;
            } else {
                num = 2;
            }

            let prefix = words.slice(0, num).join(' ');
            prefix = prefix.replace(/[,.?!…]+$/, '');

            let suffix = '';
            if (hasVo && !prefix.includes('+ Vo')) {
                suffix = ' (+ Vo.)';
            } else if (hasVing && !prefix.includes('+ Ving')) {
                suffix = ' (+ Ving)';
            }

            cues.push(prefix + '...' + suffix);
        }
    }

    return cues.join(' / ');
}
'''

# 2. Smart diffWords supporting flexible Vietnamese bracket placeholders
new_diff_words = r'''
// Word-by-word diff algorithm using LCS with flexible bracket placeholder support
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

    // If target has alternate options separated by ' / ' (e.g. 'Remember to + Vo. / Don’t forget to + Vo.')
    if (targetText.includes(' / ') && (targetText.includes('+ Vo') || targetText.includes('+ Ving') || targetText.includes('Don’t forget') || targetText.includes('quite unhappy'))) {
        const altTargets = targetText.split(' / ');
        let bestDiff = null;
        for (const alt of altTargets) {
            const curDiff = diffWordsSingle(userText, alt.trim(), preProcess, clean);
            if (!bestDiff || curDiff.accuracy > bestDiff.accuracy) {
                bestDiff = curDiff;
            }
        }
        // Also compare against full targetText
        const fullDiff = diffWordsSingle(userText, targetText, preProcess, clean);
        if (fullDiff.accuracy > bestDiff.accuracy) {
            bestDiff = fullDiff;
        }
        return bestDiff;
    }

    return diffWordsSingle(userText, targetText, preProcess, clean);
}

function diffWordsSingle(userText, targetText, preProcess, clean) {
    const rawUser = preProcess(userText).trim();
    const rawTarget = preProcess(targetText).trim();

    // Check if target has bracketed slots [ ... ]
    const slotMatches = [...rawTarget.matchAll(/\[([^\]]+)\]/g)];

    if (slotMatches.length > 0) {
        const slots = slotMatches.map(m => m[1]);
        const parts = rawTarget.split(/\[[^\]]+\]/);

        // 1. Try template regex match (English skeleton matches + slots filled with any text)
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

        // 2. Fallback: normalize slots into unique tokens for LCS alignment
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
            // Anchor-based slot extraction
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
'''

# Find getHintText in dom_code and replace up to end of diffWords
idx_get_hint = dom_code.find("// Generate hint: obfuscates alternating words using asterisks")
if idx_get_hint == -1:
    idx_get_hint = dom_code.find("function getHintText(target) {")

idx_count_words = dom_code.find("function countWords(str) {")
idx_diff_words = dom_code.find("// Word-by-word diff algorithm using LCS")
if idx_diff_words == -1:
    idx_diff_words = dom_code.find("function diffWords(userText, targetText) {")

idx_learning_prog = dom_code.find("// Global Learning Progress Management")

if idx_get_hint == -1 or idx_count_words == -1 or idx_diff_words == -1 or idx_learning_prog == -1:
    raise Exception("Could not find function boundaries in dom_logic_full.js")

count_words_block = dom_code[idx_count_words:idx_diff_words]

dom_code_new = (
    dom_code[:idx_get_hint] +
    new_get_hint_text.strip() + "\n\n" +
    count_words_block.strip() + "\n\n" +
    new_diff_words.strip() + "\n\n" +
    dom_code[idx_learning_prog:]
)

# Also ensure correctTextResult uses d.targetWord || d.word
dom_code_new = dom_code_new.replace(
    "span.textContent = d.word + ' '; // correctTextResult match",
    "span.textContent = (d.targetWord || d.word) + ' ';"
)

# In checkRecitationAnswer:
old_correct_block = """    if (correctTextResult) {
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
    }"""

new_correct_block = """    if (correctTextResult) {
        correctTextResult.innerHTML = '';
        diffResult.diff.forEach(d => {
            if (d.type === 'match') {
                const span = document.createElement('span');
                span.className = 'diff-word-match';
                span.textContent = (d.targetWord || d.word) + ' ';
                correctTextResult.appendChild(span);
            } else if (d.type === 'missing') {
                const span = document.createElement('span');
                span.className = 'diff-word-mismatch';
                span.textContent = (d.targetWord || d.word) + ' ';
                correctTextResult.appendChild(span);
            }
        });
    }"""

if old_correct_block in dom_code_new:
    dom_code_new = dom_code_new.replace(old_correct_block, new_correct_block)

with open(dom_path, "w", encoding="utf-8") as f:
    f.write(dom_code_new)

print("Updated dom_logic_full.js with subtle hints and flexible bracket slot matching! Length:", len(dom_code_new))
