# -*- coding: utf-8 -*-
with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/pure_extra_logic.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# Let's see where to inject the spelling and additional punctuation rules
spell_rules = r"""
    // H. Common Spelling Errors
    const spellDict = {
        'recieve': 'receive',
        'untill': 'until',
        'beautifull': 'beautiful',
        'restuarant': 'restaurant',
        'resturant': 'restaurant',
        'delicous': 'delicious',
        'deliciouse': 'delicious',
        'traditionel': 'traditional',
        'conveniant': 'convenient',
        'intresting': 'interesting',
        'recommand': 'recommend',
        'cloths': 'clothes',
        'comfortible': 'comfortable',
        'pleasent': 'pleasant',
        'attact': 'attract',
        'attaction': 'attraction',
        'attractions': 'attractions',
        'floting': 'floating',
        'villige': 'village',
        'touristm': 'tourism',
        'adviced': 'advised',
        'helpfull': 'helpful',
        'alot': 'a lot'
    };

    for (const [wrongSp, correctSp] of Object.entries(spellDict)) {
        const regexSp = new RegExp('\\b' + wrongSp + '\\b', 'gi');
        if (regexSp.test(rawText)) {
            errors.push({
                type: "Chính tả (Spelling)",
                wrong: wrongSp,
                correct: correctSp,
                reason: `Lỗi chính tả từ '${wrongSp}'. Từ đúng chuẩn là '${correctSp}'.`
            });
        }
    }

    // I. Punctuation Spacing Errors (e.g. "word.Word" or "word ,word")
    const punctSpacingErrors = rawText.match(/[a-zA-Z][,\.?!][a-zA-Z]/g);
    if (punctSpacingErrors && punctSpacingErrors.length > 0) {
        errors.push({
            type: "Dấu câu / Khoảng trắng",
            wrong: punctSpacingErrors.slice(0, 3).join(', '),
            correct: "Thêm dấu cách sau dấu câu",
            reason: "Cần có một dấu cách sau dấu phẩy (,), dấu chấm (.) hoặc dấu chấm hỏi (?)."
        });
    }
"""

# Insert before "// --- 2. VSTEP SCORING ON 10.0 SCALE"
target = "// --- 2. VSTEP SCORING ON 10.0 SCALE"
if "Common Spelling Errors" not in js_code:
    js_code = js_code.replace(target, spell_rules.strip() + "\n\n    " + target)

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/pure_extra_logic.js", "w", encoding="utf-8") as f:
    f.write(js_code)

print("Added spelling and punctuation rules to pure_extra_logic.js!")
