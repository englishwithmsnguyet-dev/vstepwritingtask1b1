// DOM Elements
let letterNav;
let mainTitle;
let welcomeScreen;
let letterContent;
let themeToggle;
let isDarkMode = false;

// Auth & Student Information
const ALLOWED_CLASSES = ['CB201', 'CB202', 'B209'];
const GOOGLE_FORM_ACTION_URL = "https://docs.google.com/forms/d/e/1FAIpQLSes7cy3Z9Wxr_QQRuJcohfqFycoc0_i5JNEt05FFBBGod2f5A/formResponse";
const GOOGLE_FORM_ENTRY_ID = "entry.388968236";

let currentStudentName = '';
let currentStudentClass = '';

let loginModalOverlay;
let studentNameInput;
let studentClassSelect;
let btnLoginSubmit;
let loginErrorMsg;
let loginErrorText;

let studentProfileCard;
let studentNameDisplay;
let studentClassDisplay;
let btnEditStudent;

let questStudentGreeting;
let greetingStudentName;
let greetingStudentClass;

let reportStatusBox;
let reportStatusIcon;
let reportStatusText;
let btnResendReport;

// Recitation DOM Elements
let recitationInput;
let btnPrevQuestion;
let btnShowAnswer;
let btnCheckAnswer;
let btnNextQuestion;
let currentQuestionNum;
let totalQuestionsNum;
let progressBarFill;
let questionCueText;
let recitationFeedback;
let feedbackStatus;
let userDiffResult;
let correctTextResult;
let questionHintBox;
let questionHintText;

// Evaluation DOM Elements
let recitationQuizBox;
let recitationResultBox;
let scorePercentageVal;
let resultStatusVal;
let resultMessageVal;
let btnRestartRecitation;
let evaluationIcon;

// Recitation State & Tab Locking
let activeLetterTypeId = 'advice';
let currentQuestionIndex = 0;
let activeQuestions = [];
let questionScores = [];
let questionHintsUsed = [];
let isRecitationInProgress = false;
let btnSubmitRecitationEarly = null;

// Timer DOM Elements & State (20-minute Recitation Timer)
let recitationTimerBadge;
let recitationCountdown;
let timeSpentVal;
let evaluationTimeSpent;
let recitationTimerInterval = null;
const RECITATION_TIME_LIMIT = 20 * 60; // 20 minutes = 1200 seconds
let recitationTimeRemaining = RECITATION_TIME_LIMIT;
let isRecitationTimerRunning = false;

// Full Practice (THỰC HÀNH) DOM Elements & State
let fullPracticePanel;
let fullPracticeTimerBadge;
let fullPracticeCountdown;
let fullPracticeWordBadge;
let fullPracticeWordCount;
let fullPracticePromptBox;
let fullPracticeWritingBox;
let fullPracticeInput;
let btnSubmitFullPractice;
let btnSubmitFullPracticeEarly;
let fullPracticeResultBox;
let fullPracticeLockedBanner;

let isFullPracticeInProgress = false;
let fullPracticeTimerInterval = null;
const FULL_PRACTICE_TIME_LIMIT = 20 * 60; // 20 minutes = 1200 seconds
let fullPracticeTimeRemaining = FULL_PRACTICE_TIME_LIMIT;
let isFullPracticeTimerRunning = false;

function formatTimerString(totalSeconds) {
    const mins = Math.floor(totalSeconds / 60);
    const secs = totalSeconds % 60;
    const pad = (n) => (n < 10 ? '0' + n : n);
    return `${pad(mins)}:${pad(secs)}`;
}

function updateRecitationTimerDisplay() {
    if (recitationCountdown) {
        recitationCountdown.textContent = formatTimerString(recitationTimeRemaining);
    }

    if (recitationTimerBadge) {
        recitationTimerBadge.classList.remove('timer-normal', 'timer-warning', 'timer-urgent');
        if (recitationTimeRemaining > 300) {
            recitationTimerBadge.classList.add('timer-normal');
        } else if (recitationTimeRemaining > 60) {
            recitationTimerBadge.classList.add('timer-warning');
        } else {
            recitationTimerBadge.classList.add('timer-urgent');
        }
    }
}

function startRecitationTimer() {
    if (isRecitationTimerRunning) return;
    if (recitationTimeRemaining <= 0) {
        recitationTimeRemaining = RECITATION_TIME_LIMIT;
    }
    isRecitationTimerRunning = true;
    updateRecitationTimerDisplay();

    if (recitationTimerInterval) clearInterval(recitationTimerInterval);
    recitationTimerInterval = setInterval(() => {
        if (recitationTimeRemaining > 0) {
            recitationTimeRemaining--;
            updateRecitationTimerDisplay();
        } else {
            handleRecitationTimeUp();
        }
    }, 1000);
}

function stopRecitationTimer() {
    if (recitationTimerInterval) {
        clearInterval(recitationTimerInterval);
        recitationTimerInterval = null;
    }
    isRecitationTimerRunning = false;
}

function resetRecitationTimer() {
    stopRecitationTimer();
    recitationTimeRemaining = RECITATION_TIME_LIMIT;
    updateRecitationTimerDisplay();
}

function handleRecitationTimeUp() {
    stopRecitationTimer();
    if (recitationInput) recitationInput.disabled = true;

    // Check current question if student typed something but hasn't submitted yet
    const userAns = recitationInput ? recitationInput.value.trim() : '';
    if (userAns && (!recitationFeedback || recitationFeedback.classList.contains('hidden'))) {
        const q = activeQuestions[currentQuestionIndex];
        if (q) {
            const diffResult = diffWords(userAns, q.target);
            questionScores[currentQuestionIndex] = diffResult.accuracy;
        }
    }

    alert('⏰ ĐÃ HẾT THỜI GIAN 20 PHÚT LÀM BÀI!\nHệ thống tự động nộp bài và hiển thị kết quả đánh giá trả bài của bạn.');
    showEvaluationResult();
}

// Toast Notification System
let toastNoticeTimeout = null;
function showToastNotice(message, iconClass = 'fa-solid fa-lock') {
    let toast = document.getElementById('antiCopyToast');
    if (!toast) {
        toast = document.createElement('div');
        toast.id = 'antiCopyToast';
        toast.className = 'anti-copy-toast';
        toast.innerHTML = `<i id="antiCopyToastIcon" class="${iconClass}"></i> <span id="antiCopyToastMsg"></span>`;
        document.body.appendChild(toast);
    }

    const msgSpan = document.getElementById('antiCopyToastMsg');
    const iconEl = toast.querySelector('i') || document.getElementById('antiCopyToastIcon');
    if (msgSpan) {
        msgSpan.textContent = message;
    }
    if (iconEl && iconClass) {
        iconEl.className = iconClass;
    }

    toast.classList.add('show');

    if (toastNoticeTimeout) clearTimeout(toastNoticeTimeout);
    toastNoticeTimeout = setTimeout(() => {
        toast.classList.remove('show');
    }, 2800);
}

function showAntiCopyToast(message) {
    showToastNotice(message || 'Không được phép Sao chép hoặc Dán (Copy/Paste)! Vui lòng tự gõ phím để rèn luyện.', 'fa-solid fa-ban');
}

// Unified Navigation Locking System for TRẢ BÀI & THỰC HÀNH
function applyNavigationLock(activeTab) {
    document.querySelectorAll('.tab-btn').forEach(btn => {
        if (btn.dataset.tab !== activeTab) {
            btn.classList.add('tab-locked');
            btn.setAttribute('title', 'Đã bị khóa trong lúc làm bài');
        } else {
            btn.classList.remove('tab-locked');
            btn.removeAttribute('title');
        }
    });

    document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.add('nav-locked');
        item.setAttribute('title', 'Đã bị khóa trong lúc làm bài');
    });

    if (btnEditStudent) btnEditStudent.classList.add('btn-locked');
    const btnReset = document.getElementById('btnResetProgress');
    if (btnReset) btnReset.classList.add('btn-locked');
}

function removeNavigationLock() {
    if (!isRecitationInProgress && !isFullPracticeInProgress) {
        document.querySelectorAll('.tab-btn').forEach(btn => {
            btn.classList.remove('tab-locked');
            btn.removeAttribute('title');
        });

        document.querySelectorAll('.nav-item').forEach(item => {
            item.classList.remove('nav-locked');
            item.removeAttribute('title');
        });

        if (btnEditStudent) btnEditStudent.classList.remove('btn-locked');
        const btnReset = document.getElementById('btnResetProgress');
        if (btnReset) btnReset.classList.remove('btn-locked');
    }
}

// Lock / Unlock Navigation during Recitation (TRẢ BÀI)
function lockNavigationDuringRecitation() {
    isRecitationInProgress = true;
    applyNavigationLock('writingPractice');

    const banner = document.getElementById('recitationLockedBanner');
    if (banner) banner.classList.remove('hidden');
}

function unlockNavigationAfterRecitation() {
    isRecitationInProgress = false;
    const banner = document.getElementById('recitationLockedBanner');
    if (banner) banner.classList.add('hidden');

    removeNavigationLock();
}

// Lock / Unlock Navigation during Full Practice (THỰC HÀNH)
function lockNavigationDuringFullPractice() {
    isFullPracticeInProgress = true;
    applyNavigationLock('fullPractice');

    const banner = document.getElementById('fullPracticeLockedBanner');
    if (banner) banner.classList.remove('hidden');
}

function unlockNavigationAfterFullPractice() {
    isFullPracticeInProgress = false;
    const banner = document.getElementById('fullPracticeLockedBanner');
    if (banner) banner.classList.add('hidden');

    removeNavigationLock();
}

// Full Practice Timer
function updateFullPracticeTimerDisplay() {
    if (fullPracticeCountdown) {
        fullPracticeCountdown.textContent = formatTimerString(fullPracticeTimeRemaining);
    }

    if (fullPracticeTimerBadge) {
        fullPracticeTimerBadge.classList.remove('timer-normal', 'timer-warning', 'timer-urgent');
        if (fullPracticeTimeRemaining > 300) {
            fullPracticeTimerBadge.classList.add('timer-normal');
        } else if (fullPracticeTimeRemaining > 60) {
            fullPracticeTimerBadge.classList.add('timer-warning');
        } else {
            fullPracticeTimerBadge.classList.add('timer-urgent');
        }
    }
}

function startFullPracticeTimer() {
    if (isFullPracticeTimerRunning) return;
    if (fullPracticeTimeRemaining <= 0) {
        fullPracticeTimeRemaining = FULL_PRACTICE_TIME_LIMIT;
    }
    isFullPracticeTimerRunning = true;
    updateFullPracticeTimerDisplay();

    if (fullPracticeTimerInterval) clearInterval(fullPracticeTimerInterval);
    fullPracticeTimerInterval = setInterval(() => {
        if (fullPracticeTimeRemaining > 0) {
            fullPracticeTimeRemaining--;
            updateFullPracticeTimerDisplay();
        } else {
            handleFullPracticeTimeUp();
        }
    }, 1000);
}

function stopFullPracticeTimer() {
    if (fullPracticeTimerInterval) {
        clearInterval(fullPracticeTimerInterval);
        fullPracticeTimerInterval = null;
    }
    isFullPracticeTimerRunning = false;
}

function resetFullPracticeTimer() {
    stopFullPracticeTimer();
    fullPracticeTimeRemaining = FULL_PRACTICE_TIME_LIMIT;
    updateFullPracticeTimerDisplay();
}

function handleFullPracticeTimeUp() {
    stopFullPracticeTimer();
    alert('⏰ ĐÃ HẾT THỜI GIAN 20 PHÚT LÀM BÀI!\nHệ thống tự động nộp bài thực hành viết thư của bạn và mở khóa các tab để bạn đối chiếu với bài mẫu.');
    submitFullPractice(true);
}

function submitRecitationEarly() {
    if (!isRecitationInProgress) return;

    const confirmEarly = confirm(
        '⚠️ BẠN CÓ CHẮC CHẮN MUỐN NỘP BÀI SỚM KHÔNG?\n\n' +
        '• Các câu hỏi chưa làm sẽ được tính 0 điểm.\n' +
        '• Hệ thống sẽ tự động tổng kết điểm và MỞ KHÓA lại các tab cho bạn.\n\n' +
        'Bấm OK để nộp bài sớm ngay, hoặc Hủy để tiếp tục làm bài.'
    );

    if (!confirmEarly) return;

    // Grade current question if user entered something
    const userAns = recitationInput ? recitationInput.value.trim() : '';
    if (userAns && (!recitationFeedback || recitationFeedback.classList.contains('hidden'))) {
        const q = activeQuestions[currentQuestionIndex];
        if (q) {
            const diffResult = diffWords(userAns, q.target);
            const hintUsed = questionHintsUsed[currentQuestionIndex];
            const finalScore = hintUsed ? Math.round(diffResult.accuracy * 0.5) : diffResult.accuracy;
            questionScores[currentQuestionIndex] = finalScore;
        }
    }

    showEvaluationResult();
}

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

function countWords(str) {
    if (!str) return 0;
    const words = str.trim().split(/\s+/).filter(w => w.length > 0);
    return words.length;
}

function escapeHtml(str) {
    if (!str) return '';
    return str
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
}

// Word-by-word diff algorithm using LCS with flexible bracket placeholder support
function diffWords(userText, targetText) {
    const isPunctOrSignOnly = (w) => /^[+\-–—−.,!?;:()\[\]\s]+$/.test(w);

    const preProcess = (t) => t
        .replace(/…/g, '...')
        .replace(/\.\s*\.\s*\./g, '...')
        .replace(/[’‘]/g, "'")
        .replace(/[“”]/g, '"')
        // Strip leading bullet marks (+, -, *, etc.)
        .replace(/^[\s+\-–—−*•]+/, '')
        // Normalize V-ing and V-o notation variations first
        .replace(/(^|[^a-zA-Z0-9])([vV])\s*[-_–—−]\s*(ing\b|[0oO]\b)/gi, '$1$2$3')
        // Normalize hành động slot delimiters (+, -, –, —, :, /, or space)
        .replace(/(hành\s*động)\s*([+\-:–—−/]|->)?\s*/gi, '$1 ')
        // Normalize hyphens between English words (e.g. part-time -> part time)
        .replace(/([a-zA-Z0-9])\s*[-–—−]\s*([a-zA-Z0-9])/g, '$1 $2')
        .replace(/[–—−]/g, '-')
        .replace(/\s*\+\s*/g, ' + ')
        .replace(/\s*-\s*/g, ' - ');
        
    const clean = (w) => {
        let s = w.toLowerCase().trim();
        s = s.replace(/^[.,!?;:()+\[\]\s\-–—−/]+|[.,!?;:()+\[\]\s\-–—−/]+$/g, '');
        s = s.replace(/^[vV]\s*[-_]?ing$/i, 'ving');
        s = s.replace(/^[vV]\s*[-_]?[0oO]$/i, 'vo');
        return s;
    };

    // If target has alternate options separated by ' / ' (e.g. 'Remember to + Vo. / Don’t forget to + Vo.')
    if (targetText.includes(' / ') && (targetText.includes('+ Vo') || targetText.includes('+ Ving') || targetText.includes('Don’t forget') || targetText.includes('quite unhappy'))) {
        const altTargets = targetText.split(' / ');
        let bestDiff = null;
        for (const alt of altTargets) {
            const curDiff = diffWordsSingle(userText, alt.trim(), preProcess, clean, isPunctOrSignOnly);
            if (!bestDiff || curDiff.accuracy > bestDiff.accuracy) {
                bestDiff = curDiff;
            }
        }
        // Also compare against full targetText
        const fullDiff = diffWordsSingle(userText, targetText, preProcess, clean, isPunctOrSignOnly);
        if (fullDiff.accuracy > bestDiff.accuracy) {
            bestDiff = fullDiff;
        }
        return bestDiff;
    }

    return diffWordsSingle(userText, targetText, preProcess, clean, isPunctOrSignOnly);
}

function diffWordsSingle(userText, targetText, preProcess, clean, isPunctOrSignOnly) {
    if (!isPunctOrSignOnly) {
        isPunctOrSignOnly = (w) => /^[+\-–—−.,!?;:()\[\]\s]+$/.test(w);
    }
    const rawUser = preProcess(userText).trim();
    const rawTarget = preProcess(targetText).trim();

    // If target has "+ Vo", "- Vo", or "Vo", or "+ Ving", "- Ving", or "Ving" without brackets, treat as bracket slot [+ Vo] or [+ Ving]
    // This allows template matching to accept any user notation (+/-, V-ing, ving, + Ving, (+ Ving), actual verb, etc.)
    let adjustedTarget = rawTarget;
    if (!adjustedTarget.includes('[') && !adjustedTarget.includes(']')) {
        adjustedTarget = adjustedTarget.replace(/(^|[^a-zA-Z0-9])[+\-–—−]?\s*Vo\b/g, '$1[+ Vo]');
        adjustedTarget = adjustedTarget.replace(/(^|[^a-zA-Z0-9])[+\-–—−]?\s*Ving\b/g, '$1[+ Ving]');
    }

    // Check if target has bracketed slots [ ... ]
    const slotMatches = [...adjustedTarget.matchAll(/\[([^\]]+)\]/g)];

    if (slotMatches.length > 0) {
        const slots = slotMatches.map(m => m[1]);
        const parts = adjustedTarget.split(/\[[^\]]+\]/);

        // 1. Try template regex match (English skeleton matches + slots filled with any text)
        let pattern = '^\\s*';
        for (let i = 0; i < slots.length; i++) {
            const pStr = parts[i].trim();
            if (pStr) {
                const words = pStr.split(/\s+/).filter(w => !isPunctOrSignOnly(w) || w === '.' || w === '!' || w === '?').map(w => w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'));
                pattern += words.join('[\\s+\\-–—−]*') + '[\\s+\\-–—−]*(.+?)[\\s+\\-–—−]*';
            } else {
                pattern += '(.+?)[\\s+\\-–—−]*';
            }
        }
        const pLast = parts[parts.length - 1].trim();
        if (pLast) {
            const lastWords = pLast.split(/\s+/).filter(w => !isPunctOrSignOnly(w) || w === '.' || w === '!' || w === '?').map(w => w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'));
            if (/^[.,!?;:]+$/.test(pLast)) {
                pattern += '(?:[\\s+\\-–—−]*[' + pLast.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '])?';
            } else {
                pattern += lastWords.join('[\\s+\\-–—−]*');
            }
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
                const targetSlotDisplay = slots[i].startsWith('+ ') ? slots[i] : `[${slots[i]}]`;
                diff.push({
                    word: userSlotVal,
                    targetWord: targetSlotDisplay,
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
        let tNorm = adjustedTarget;
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
                    target: slots[i].startsWith('+ ') ? slots[i] : `[${slots[i]}]`
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
                    user: extractedUserSlot || (slots[i].startsWith('+ ') ? slots[i] : `[${slots[i]}]`),
                    target: slots[i].startsWith('+ ') ? slots[i] : `[${slots[i]}]`
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

        const meaningfulUserWords = uWords.filter(w => !isPunctOrSignOnly(w));
        const meaningfulTargetWords = tWords.filter(w => !isPunctOrSignOnly(w));
        const matchCount = diff.filter(d => d.type === 'match' && !isPunctOrSignOnly(d.word)).length;
        const maxWords = Math.max(meaningfulTargetWords.length, meaningfulUserWords.length);
        const accuracy = maxWords > 0 ? Math.round((matchCount / maxWords) * 100) : 0;

        return {
            diff,
            accuracy,
            isPerfect: matchCount === meaningfulTargetWords.length && meaningfulUserWords.length === meaningfulTargetWords.length
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

    const meaningfulUserWords = uWords.filter(w => !isPunctOrSignOnly(w));
    const meaningfulTargetWords = tWords.filter(w => !isPunctOrSignOnly(w));
    const matchCount = diff.filter(d => d.type === 'match' && !isPunctOrSignOnly(d.word)).length;
    const maxWords = Math.max(meaningfulTargetWords.length, meaningfulUserWords.length);
    const accuracy = maxWords > 0 ? Math.round((matchCount / maxWords) * 100) : 0;

    return {
        diff,
        accuracy,
        isPerfect: matchCount === meaningfulTargetWords.length && meaningfulUserWords.length === meaningfulTargetWords.length
    };
}

// Global Learning Progress Management
function getCompletedLetters() {
    try {
        const saved = localStorage.getItem('vstep_completed_letters');
        return saved ? JSON.parse(saved) : [];
    } catch (e) {
        return [];
    }
}

function markLetterCompleted(letterId) {
    let completed = getCompletedLetters();
    if (!completed.includes(letterId)) {
        completed.push(letterId);
        try {
            localStorage.setItem('vstep_completed_letters', JSON.stringify(completed));
        } catch (e) {
            console.error('Error saving completed letters', e);
        }
    }
    updateGlobalProgress();
    renderNav();
}

function resetLearningProgress() {
    if (isRecitationInProgress || isFullPracticeInProgress) {
        showToastNotice('🔒 Đang trong thời gian làm bài kiểm tra / thực hành! Không thể làm mới tiến độ lúc này.', 'fa-solid fa-lock');
        return;
    }
    if (confirm('Bạn có chắc chắn muốn làm mới toàn bộ tiến độ học tập không?')) {
        try {
            localStorage.removeItem('vstep_completed_letters');
        } catch (e) {
            console.error('Error clearing progress', e);
        }
        updateGlobalProgress();
        renderNav();
    }
}

function updateGlobalProgress() {
    const completed = getCompletedLetters();
    const total = letterTypes.length;
    const count = completed.length;
    const percentage = total > 0 ? Math.round((count / total) * 100) : 0;

    // Sidebar Progress
    const sidebarText = document.getElementById('sidebarProgressText');
    const sidebarFill = document.getElementById('sidebarProgressFill');
    if (sidebarText) sidebarText.textContent = `${count}/${total} ĐẠT`;
    if (sidebarFill) sidebarFill.style.width = `${percentage}%`;

    // Dashboard Card Progress
    const dashPercent = document.getElementById('dashboardProgressPercent');
    const dashFill = document.getElementById('dashboardProgressFill');
    const dashStatus = document.getElementById('dashboardProgressStatus');
    
    if (dashPercent) dashPercent.textContent = `${percentage}%`;
    if (dashFill) dashFill.style.width = `${percentage}%`;
    if (dashStatus) {
        if (count === 0) {
            dashStatus.textContent = 'Chưa hoàn thành dạng thư nào. Hãy bắt đầu học tập!';
        } else if (count < total) {
            dashStatus.textContent = `Đã hoàn thành ${count}/${total} dạng thư. Tiếp tục phát huy!`;
        } else {
            dashStatus.textContent = '🎉 Xuất sắc! Bạn đã chinh phục toàn bộ 7 dạng thư VSTEP Task 01!';
        }
    }
}

// Reset recitation UI
function resetRecitationUI() {
    currentQuestionIndex = 0;
    activeQuestions = recitationQuestions[activeLetterTypeId] || [];
    questionScores = new Array(activeQuestions.length).fill(0);
    questionHintsUsed = new Array(activeQuestions.length).fill(false);

    if (totalQuestionsNum) totalQuestionsNum.textContent = activeQuestions.length;

    // Reset Recitation 20-minute Timer
    resetRecitationTimer();
    const practicePanel = document.getElementById('writingPracticePanel');
    if (practicePanel && practicePanel.classList.contains('active')) {
        lockNavigationDuringRecitation();
        startRecitationTimer();
    } else {
        unlockNavigationAfterRecitation();
    }

    // Reset UI Visibility
    if (recitationQuizBox) recitationQuizBox.classList.remove('hidden');
    if (recitationFeedback) recitationFeedback.classList.add('hidden');
    if (recitationResultBox) recitationResultBox.classList.add('hidden');
    if (reportStatusBox) reportStatusBox.classList.add('hidden');
    
    // Restore header and progress bar
    const recitationHeader = document.querySelector('.recitation-header');
    if (recitationHeader) recitationHeader.classList.remove('hidden');
    
    const progressWrapper = document.querySelector('.recitation-progress-wrapper');
    if (progressWrapper) progressWrapper.style.display = 'flex';

    showRecitationQuestion();
}

// Display active recitation question
function showRecitationQuestion() {
    if (activeQuestions.length === 0) return;

    const q = activeQuestions[currentQuestionIndex];
    if (currentQuestionNum) currentQuestionNum.textContent = currentQuestionIndex + 1;
    
    // Update progress bar
    const progressPct = ((currentQuestionIndex + 1) / activeQuestions.length) * 100;
    if (progressBarFill) progressBarFill.style.width = `${progressPct}%`;

    if (questionCueText) questionCueText.textContent = q.cue;
    if (recitationInput) {
        recitationInput.value = '';
        recitationInput.disabled = false;
        recitationInput.focus();
    }

    // Reset feedback and hint box
    if (recitationFeedback) recitationFeedback.classList.add('hidden');
    if (questionHintBox) questionHintBox.classList.add('hidden');
    if (questionHintText) questionHintText.textContent = '';

    // If hint was already used on this question, restore it
    if (questionHintsUsed[currentQuestionIndex]) {
        if (questionHintText) questionHintText.textContent = getHintText(q.target);
        if (questionHintBox) questionHintBox.classList.remove('hidden');
    }

    // Button states
    if (btnPrevQuestion) btnPrevQuestion.disabled = (currentQuestionIndex === 0);
    if (btnShowAnswer) btnShowAnswer.classList.remove('hidden');
    if (btnCheckAnswer) btnCheckAnswer.classList.remove('hidden');
    if (btnNextQuestion) btnNextQuestion.classList.add('hidden');
}

// Check user recitation answer
function checkRecitationAnswer() {
    if (activeQuestions.length === 0) return;
    const q = activeQuestions[currentQuestionIndex];
    const userAns = recitationInput ? recitationInput.value.trim() : '';

    if (!userAns) {
        alert('Vui lòng nhập câu trả lời của bạn trước khi kiểm tra!');
        return;
    }

    const diffResult = diffWords(userAns, q.target);
    const hintUsed = questionHintsUsed[currentQuestionIndex] || false;
    
    // Apply 50% penalty if hint was used
    let finalScore = diffResult.accuracy;
    if (hintUsed) {
        finalScore = Math.round(diffResult.accuracy * 0.5);
    }
    questionScores[currentQuestionIndex] = finalScore;

    // Build diff HTML for User Diff Result
    if (userDiffResult) {
        userDiffResult.innerHTML = '';
        diffResult.diff.forEach(d => {
            if (d.type === 'match') {
                const span = document.createElement('span');
                span.className = 'diff-word-match';
                span.textContent = d.word + ' ';
                userDiffResult.appendChild(span);
            } else if (d.type === 'extra') {
                const span = document.createElement('span');
                span.className = 'diff-word-extra';
                span.textContent = d.word + ' ';
                userDiffResult.appendChild(span);
            }
        });
        if (userDiffResult.innerHTML === '') {
            userDiffResult.innerHTML = '<span style="color:var(--text-muted);font-style:italic;">(Bỏ trống)</span>';
        }
    }

    // Build diff HTML for Correct Text Result
    if (correctTextResult) {
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
    }

    // Show Feedback Status
    if (feedbackStatus) {
        if (diffResult.isPerfect) {
            feedbackStatus.className = 'feedback-status status-success';
            if (hintUsed) {
                feedbackStatus.innerHTML = `<i class="fa-solid fa-circle-check"></i> <strong>Chính xác tuyệt đối!</strong> (Độ khớp: 100% - Điểm tính: 50% do dùng gợi ý)`;
            } else {
                feedbackStatus.innerHTML = `<i class="fa-solid fa-circle-check"></i> <strong>Chính xác tuyệt đối!</strong> (Độ chính xác: 100%)`;
            }
        } else {
            feedbackStatus.className = 'feedback-status status-error';
            if (hintUsed) {
                feedbackStatus.innerHTML = `<i class="fa-solid fa-triangle-exclamation"></i> <strong>Chưa chính xác!</strong> (Độ khớp: ${diffResult.accuracy}% - Điểm tính: ${finalScore}% do dùng gợi ý). Xem chi tiết bên dưới.`;
            } else {
                feedbackStatus.innerHTML = `<i class="fa-solid fa-triangle-exclamation"></i> <strong>Chưa chính xác! Độ chính xác: ${diffResult.accuracy}%. Xem so sánh bên dưới.</strong>`;
            }
        }
    }

    if (recitationFeedback) recitationFeedback.classList.remove('hidden');
    if (btnCheckAnswer) btnCheckAnswer.classList.add('hidden');
    if (btnNextQuestion) btnNextQuestion.classList.remove('hidden');
    if (recitationInput) recitationInput.disabled = true;
}

// Show hint inline
function showRecitationAnswer() {
    if (activeQuestions.length === 0) return;
    const q = activeQuestions[currentQuestionIndex];
    
    // Mark as hint used for this question
    questionHintsUsed[currentQuestionIndex] = true;
    
    // Generate masked hint text
    const hintText = getHintText(q.target);
    
    if (questionHintText) {
        questionHintText.textContent = hintText;
    }
    if (questionHintBox) {
        questionHintBox.classList.remove('hidden');
    }
}

// Next recitation question
function nextRecitationQuestion() {
    if (currentQuestionIndex < activeQuestions.length - 1) {
        currentQuestionIndex++;
        showRecitationQuestion();
    } else {
        showEvaluationResult();
    }
}

// Show evaluation result screen
function showEvaluationResult() {
    // Hide quiz box and feedback panel
    if (recitationQuizBox) recitationQuizBox.classList.add('hidden');
    if (recitationFeedback) recitationFeedback.classList.add('hidden');
    
    // Hide header and progress bar wrapper during evaluation results
    const recitationHeader = document.querySelector('.recitation-header');
    if (recitationHeader) recitationHeader.classList.add('hidden');
    
    const progressWrapper = document.querySelector('.recitation-progress-wrapper');
    if (progressWrapper) progressWrapper.style.display = 'none';
    
    // Stop 20-minute countdown timer and compute time spent
    stopRecitationTimer();
    unlockNavigationAfterRecitation();
    const timeSpentSeconds = Math.max(0, RECITATION_TIME_LIMIT - recitationTimeRemaining);
    if (timeSpentVal) {
        timeSpentVal.textContent = formatTimerString(timeSpentSeconds);
    }

    // Calculate average score
    const totalQuestions = activeQuestions.length;
    const totalScore = questionScores.reduce((sum, s) => sum + s, 0);
    const averageScore = totalQuestions > 0 ? Math.round(totalScore / totalQuestions) : 0;
    
    // Update score text
    if (scorePercentageVal) scorePercentageVal.textContent = averageScore;
    
    // Get active letter type data for dynamic title
    const typeData = letterTypes.find(t => t.id === activeLetterTypeId);
    const letterTitleEn = typeData ? typeData.titleEn : 'Letter of Advice';
    
    const evalCard = document.querySelector('.evaluation-card');
    let statusText = 'KHÔNG ĐẠT';
    
    if (averageScore >= 90) {
        // Passed state
        statusText = 'ĐẠT';
        if (resultStatusVal) {
            resultStatusVal.textContent = 'ĐẠT';
        }
        if (resultMessageVal) {
            const questNames = {
                advice: 'NHIỆM VỤ HỆ THỐNG ĐẦU TIÊN',
                request: 'NHIỆM VỤ HỆ THỐNG THỨ HAI',
                description: 'NHIỆM VỤ HỆ THỐNG THỨ BA',
                complaint: 'NHIỆM VỤ HỆ THỐNG THỨ TƯ',
                feedback: 'NHIỆM VỤ HỆ THỐNG THỨ NĂM',
                apology: 'NHIỆM VỤ HỆ THỐNG THỨ SÁU',
                application: 'NHIỆM VỤ HỆ THỐNG THỨ BẢY'
            };
            const questName = questNames[activeLetterTypeId] || 'NHIỆM VỤ HỆ THỐNG';
            resultMessageVal.textContent = `Chúc mừng bạn đã chinh phục được ${letterTitleEn}. ${questName} đã được hoàn thành, hãy tiếp tục với nhiệm vụ tiếp theo.`;
        }
        if (evaluationIcon) {
            evaluationIcon.innerHTML = '<i class="fa-solid fa-circle-check"></i>';
        }
        if (evalCard) {
            evalCard.classList.remove('failed');
            evalCard.classList.add('passed');
        }
        markLetterCompleted(activeLetterTypeId);
    } else {
        // Failed state
        statusText = 'KHÔNG ĐẠT';
        if (resultStatusVal) {
            resultStatusVal.textContent = 'KHÔNG ĐẠT';
        }
        if (resultMessageVal) {
            resultMessageVal.textContent = 'Xin vui lòng ôn lại bài thật kỹ và trả bài lại một lần nữa.';
        }
        if (evaluationIcon) {
            evaluationIcon.innerHTML = '<i class="fa-solid fa-triangle-exclamation"></i>';
        }
        if (evalCard) {
            evalCard.classList.remove('passed');
            evalCard.classList.add('failed');
        }
    }
    
    // Show result box
    if (recitationResultBox) recitationResultBox.classList.remove('hidden');

    // Automatically report result to Google Form
    reportResultToGoogleForm();
}

// Prev recitation question
function prevRecitationQuestion() {
    if (currentQuestionIndex > 0) {
        currentQuestionIndex--;
        showRecitationQuestion();
    }
}

// Show Welcome Screen
function showWelcomeScreen() {
    if (isRecitationInProgress) {
        showToastNotice('🔒 Đang trong quá trình trả bài! Bạn không thể rời khỏi bài cho đến khi hoàn thành hoặc nộp bài sớm.', 'fa-solid fa-lock');
        return;
    }
    if (isFullPracticeInProgress) {
        showToastNotice('🔒 Đang trong thời gian thực hành viết bài (20 phút)! Bạn không thể rời khỏi bài cho đến khi nộp bài.', 'fa-solid fa-lock');
        return;
    }
    activeLetterTypeId = null;
    
    // Update active nav
    document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.remove('active');
    });
    const homeItem = document.querySelector('.home-nav-item');
    if (homeItem) homeItem.classList.add('active');

    // Show welcome, hide content
    if (welcomeScreen) welcomeScreen.style.display = 'flex';
    if (letterContent) letterContent.classList.add('hidden');

    // Reset Title
    if (mainTitle) {
        mainTitle.innerHTML = `
            <div class="main-title-en placeholder-blink">Chọn một dạng thư để bắt đầu NHIỆM VỤ HỆ THỐNG của bạn!</div>
        `;
    }
}

// Render Navigation
function renderNav() {
    if (!letterNav) return;
    letterNav.innerHTML = ''; // Clear existing
    
    // Add Home button first
    const homeItem = document.createElement('div');
    homeItem.className = 'nav-item home-nav-item active';
    homeItem.innerHTML = `
        <i class="fa-solid fa-house"></i>
        <div class="nav-text">
            <div class="nav-title-en" style="font-weight: bold;">TRANG CHỦ</div>
            <div class="nav-title-vi">Màn hình khởi đầu</div>
        </div>
    `;
    homeItem.addEventListener('click', showWelcomeScreen);
    letterNav.appendChild(homeItem);

    const completed = getCompletedLetters();

    letterTypes.forEach(type => {
        const isCompleted = completed.includes(type.id);
        const navItem = document.createElement('div');
        navItem.className = 'nav-item';
        navItem.dataset.id = type.id;
        navItem.innerHTML = `
            <i class="fa-solid ${type.icon}"></i>
            <div class="nav-text">
                <div class="nav-title-en">${type.titleEn}</div>
                <div class="nav-title-vi">${type.titleVi}</div>
            </div>
            ${isCompleted ? '<span class="nav-completed-badge" title="Đã chinh phục"><i class="fa-solid fa-circle-check"></i></span>' : ''}
        `;
        
        navItem.addEventListener('click', () => selectLetterType(type.id));
        letterNav.appendChild(navItem);
    });
}

// Select a Letter Type
function selectLetterType(id) {
    if (typeof stopSampleAudio === 'function') stopSampleAudio();
    if (isRecitationInProgress) {
        showToastNotice('🔒 Đang trong quá trình trả bài! Bạn không thể rời khỏi bài cho đến khi hoàn thành hoặc nộp bài sớm.', 'fa-solid fa-lock');
        return;
    }
    if (isFullPracticeInProgress) {
        showToastNotice('🔒 Đang trong thời gian thực hành viết bài (20 phút)! Bạn không thể rời khỏi bài cho đến khi nộp bài.', 'fa-solid fa-lock');
        return;
    }
    activeLetterTypeId = id;
    
    // Update active nav
    document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.remove('active');
        if (item.dataset.id === id) item.classList.add('active');
    });

    const typeData = letterTypes.find(t => t.id === id);
    if (!typeData) return;

    // Hide welcome, show content
    if (welcomeScreen) welcomeScreen.style.display = 'none';
    if (letterContent) letterContent.classList.remove('hidden');

    // Set Title
    if (mainTitle) {
        mainTitle.innerHTML = `
            <div class="main-title-en">${typeData.titleEn}</div>
            <div class="main-title-vi">${typeData.titleVi}</div>
        `;
    }

    // Populate Content
    const basicInfoPanel = document.getElementById('basicInfoPanel');
    const identifyingSignsPanel = document.getElementById('identifyingSignsPanel');
    const detailedOutlinePanel = document.getElementById('detailedOutlinePanel');
    const sampleWritingPanel = document.getElementById('sampleWritingPanel');

    if (basicInfoPanel) basicInfoPanel.innerHTML = typeData.basicInfo;
    if (identifyingSignsPanel) identifyingSignsPanel.innerHTML = typeData.identifyingSigns;
    if (detailedOutlinePanel) {
        detailedOutlinePanel.innerHTML = typeData.detailedOutline.replace(/\[([^\]]+)\]/g, '[<strong>$1</strong>]');
    }
    if (sampleWritingPanel) sampleWritingPanel.innerHTML = typeData.sampleWriting;

    // Render Full Practice Panel
    renderFullPracticePanel(id);

    // Reset recitation for this type
    resetRecitationUI();

    // Reset tabs to first tab
    const firstTab = document.querySelector('.tab-btn[data-tab="basicInfo"]');
    if (firstTab) firstTab.click();
}

// --- Full Practice (THỰC HÀNH) System ---
function renderFullPracticePanel(letterId) {
    const typeData = letterTypes.find(t => t.id === letterId);
    if (!typeData) return;

    const promptBox = document.getElementById('fullPracticePromptBox');
    if (promptBox) {
        const tempDiv = document.createElement('div');
        tempDiv.innerHTML = typeData.sampleWriting;
        const promptContainer = tempDiv.querySelector('.sample-prompt-container');
        if (promptContainer) {
            promptBox.innerHTML = promptContainer.outerHTML;
        } else {
            promptBox.innerHTML = `<div class="sample-prompt-container"><div class="sample-prompt-header"><i class="fa-solid fa-file-circle-question"></i> ĐỀ BÀI (TOPIC PROMPT)</div><div class="sample-prompt-text"><p>${typeData.practicePrompt || ''}</p></div></div>`;
        }
    }

    resetFullPracticeUI();
}

function updateFullPracticeWordCount() {
    const text = fullPracticeInput ? fullPracticeInput.value : '';
    const count = countWords(text);
    if (fullPracticeWordCount) fullPracticeWordCount.textContent = count;

    if (fullPracticeWordBadge) {
        fullPracticeWordBadge.classList.remove('word-count-pass', 'word-count-warn');
        if (count >= 120) {
            fullPracticeWordBadge.classList.add('word-count-pass');
        } else if (count > 0) {
            fullPracticeWordBadge.classList.add('word-count-warn');
        }
    }
    return count;
}

function resetFullPracticeUI() {
    resetFullPracticeTimer();

    if (fullPracticeInput) {
        fullPracticeInput.value = '';
        fullPracticeInput.disabled = false;
    }
    updateFullPracticeWordCount();

    if (fullPracticeWritingBox) fullPracticeWritingBox.classList.remove('hidden');
    if (fullPracticeResultBox) {
        fullPracticeResultBox.classList.add('hidden');
        fullPracticeResultBox.innerHTML = '';
    }

    const panel = document.getElementById('fullPracticePanel');
    if (panel && panel.classList.contains('active')) {
        lockNavigationDuringFullPractice();
        startFullPracticeTimer();
    } else {
        unlockNavigationAfterFullPractice();
    }
}

// =========================================================================
// OFFICIAL VSTEP WRITING TASK 1 SCORING GUIDE & EVALUATION ENGINE
// (Based on Ministry of Education and Training Rating Scale - media_1787637818545.jpg)
// =========================================================================

const VSTEP_OFFICIAL_RUBRIC = {
    taskFulfilment: {
        10: {
            en: "Covers all the requirements of the task effectively; effectively fulfills all communicative purpose(s), with tone consistent and appropriate; fully develops key points with all the details relevant.",
            vi: "Đáp ứng xuất sắc và toàn diện mọi yêu cầu của đề bài; đạt trọn vẹn mục đích giao tiếp với văn phong hoàn toàn nhất quán, phù hợp; phát triển đầy đủ các ý chính với chi tiết xác đáng."
        },
        9: {
            en: "Covers all the requirements of the task effectively; effectively fulfills all communicative purpose(s), with tone consistent and appropriate; fully develops key points with all the details generally relevant.",
            vi: "Đáp ứng hiệu quả tất cả yêu cầu của đề; thực hiện tốt mục đích giao tiếp, văn phong nhất quán và chuẩn mực; phát triển đầy đủ các ý chính với các chi tiết nhìn chung rất phù hợp."
        },
        8: {
            en: "Covers all the requirements of the task; presents generally clear communicative purpose(s), with one or two minor inconsistencies and inappropriacies in tone; develops key points with most of the detail generally relevant; one/two of the points could be more fully extended.",
            vi: "Đáp ứng đầy đủ các yêu cầu của đề; mục đích giao tiếp rõ ràng, chỉ có 1-2 điểm nhỏ chưa hoàn toàn nhất quán về giọng văn; phát triển các ý chính với chi tiết phù hợp."
        },
        7: {
            en: "Covers all the requirements of the tasks; the format may be inappropriate in places; presents generally clear communicative purpose(s), with some inconsistencies and inappropriacies in tone; adequately presents key points, but one or two details may be inappropriate.",
            vi: "Bao quát được các yêu cầu của đề; thể thức có thể chưa thật chuẩn ở một vài chỗ; mục đích giao tiếp tương đối rõ ràng; trình bày đầy đủ các ý chính nhưng có thể có 1-2 chi tiết chưa tối ưu."
        },
        6: {
            en: "Covers almost all the requirements of the tasks; the format may be inappropriate in places; presents generally clear communicative purpose(s), with some inconsistencies and inappropriacies in tone; adequately presents key points, but a few details may be inappropriate.",
            vi: "Đáp ứng hầu hết các yêu cầu của đề; mục đích giao tiếp cơ bản rõ ràng nhưng văn phong còn đôi chỗ chưa chuẩn; nêu được các ý chính nhưng một vài chi tiết chưa thật sát."
        },
        5: {
            en: "Partially covers the requirements of the tasks; presents communicative purpose(s), which are unclear in places; there are some inconsistencies and inappropriacies in tone; inadequately presents key points; there may be a tendency to focus on details.",
            vi: "Chỉ đáp ứng được một phần yêu cầu của đề; mục đích giao tiếp chưa rõ ràng ở một số vị trí; chưa phát triển đầy đủ các ý chính hoặc tập trung quá nhiều vào chi tiết phụ."
        },
        4: {
            en: "Partially covers the requirements of the tasks; fails to clearly presents communicative purpose(s); the tone may be inappropriate; may confuse key points; some parts may be unclear, irrelevant or repetitive.",
            vi: "Chỉ giải quyết được một phần đề; chưa làm rõ mục đích giao tiếp; giọng văn chưa phù hợp; các ý chính bị nhầm lẫn hoặc lặp ý, thiếu mạch lạc."
        },
        3: {
            en: "Does not address any part of the task; presents limited ideas which may be largely irrelevant/repetitive.",
            vi: "Hầu như không giải quyết được yêu cầu đề bài; ý tưởng rất hạn chế, lặp lại hoặc lạc đề."
        },
        2: {
            en: "Does not address any part of the task.",
            vi: "Không giải quyết được phần nào của đề bài."
        },
        1: {
            en: "Answer is totally irrelevant or incomprehensible.",
            vi: "Bài viết hoàn toàn lạc đề hoặc không thể hiểu được."
        },
        0: {
            en: "Does not attend the exam / does not write any words / writes only a memorized response.",
            vi: "Không làm bài / không có nội dung hoặc chỉ chép lại đoạn văn học vẹt không liên quan."
        }
    },
    organization: {
        10: {
            en: "Organizes information and ideas logically; uses a variety as well as a range of cohesive devices and organizational patterns flexibly; uses paragraphing sufficiently and appropriately.",
            vi: "Tổ chức thông tin và ý tưởng hoàn toàn logic; sử dụng đa dạng và linh hoạt các phương tiện liên kết và mô thức tổ chức đoạn; phân đoạn chuẩn mực, hợp lý."
        },
        9: {
            en: "Organizes information and ideas coherently; uses a variety as well as a range of cohesive devices and organizational patterns effectively; uses paragraphing sufficiently and appropriately.",
            vi: "Tổ chức thông tin mạch lạc, rõ ràng; vận dụng hiệu quả nhiều phương tiện liên kết và cấu trúc đoạn; phân chia đoạn văn hợp lý."
        },
        8: {
            en: "Organizes information and ideas coherently; uses a range of linking words and cohesive devices appropriately, though there may be some under/over use.",
            vi: "Tổ chức ý tưởng mạch lạc; sử dụng tương đối tốt các từ nối và phương tiện liên kết, dù đôi khi còn dùng hơi ít hoặc hơi lạm dụng."
        },
        7: {
            en: "Organizes information and ideas coherently; uses a variety of linking words appropriately and a number of cohesive devices accurately within and across sentences, but there may be occasional inappropriacies.",
            vi: "Bố cục mạch lạc; sử dụng chuẩn xác nhiều từ nối trong câu và giữa các câu, dù đôi khi còn một vài liên từ dùng chưa tự nhiên."
        },
        6: {
            en: "Organizes information and ideas generally coherently; uses linking words and a limited number of cohesive devices within and across sentences accurately, but there are some inappropriacies.",
            vi: "Ý tưởng nhìn chung có tính liên kết; sử dụng được các từ nối cơ bản trong và giữa các câu, nhưng số lượng từ liên kết còn hạn chế."
        },
        5: {
            en: "Organizes information and ideas fairly coherently; uses linking words and some familiar cohesive devices within and across sentences accurately, though there may be inaccuracies.",
            vi: "Bố cục tương đối mạch lạc; sử dụng một số từ nối quen thuộc nhưng đôi chỗ còn thiếu chính xác hoặc thiếu tự nhiên."
        },
        4: {
            en: "Presents information and ideas with some organization; uses linking words accurately and attempts a few familiar cohesive devices within and across sentences though there are repetitions and inaccuracies.",
            vi: "Có cố gắng tổ chức ý nhưng còn rời rạc; từ nối dùng lặp lại nhiều lần hoặc chưa chuẩn xác."
        },
        3: {
            en: "Presents information and ideas in a series of simple sentences linked by only basic, high frequency linking words.",
            vi: "Trình bày thông tin dưới dạng các câu đơn rời rạc, chỉ dùng các từ nối quá cơ bản (and, but, so)."
        },
        2: {
            en: "Has very little control of organizational features.",
            vi: "Rất ít hoặc không kiểm soát được cấu trúc và bố cục bài viết."
        },
        1: {
            en: "Has no organizational features.",
            vi: "Hoàn toàn không có tính tổ chức hay bố cục đoạn."
        },
        0: {
            en: "Does not attend / no response.",
            vi: "Không có bài làm."
        }
    },
    vocabulary: {
        10: {
            en: "Uses a wide range of vocabulary including some less common lexis precisely and flexibly; shows full control of style and collocation, but there may be occasional inaccuracies; errors are very rare with just one or two minor slips.",
            vi: "Vốn từ rất phong phú, sử dụng chính xác và linh hoạt các từ vựng nâng cao; kiểm soát tốt phong cách và kết hợp từ (collocations); lỗi sai cực kỳ hiếm gặp."
        },
        9: {
            en: "Uses a wide range of vocabulary including some less common lexis precisely; shows good control of style and collocation, but there may be some inaccuracies; errors, if present, are non-systematic and non-impeding.",
            vi: "Vốn từ rộng, dùng chính xác từ vựng theo chủ đề; kiểm soát tốt kết hợp từ; nếu có lỗi thì chỉ là lỗi nhỏ, không mang tính hệ thống và không cản trở việc hiểu."
        },
        8: {
            en: "Uses a good range of vocabulary including some less common lexis appropriately; shows some control of style and collocation; errors, if present, are non-systematic and non-impeding.",
            vi: "Sử dụng vốn từ tốt, dùng đúng ngữ cảnh một số từ vựng nâng cao; có kiểm soát phong cách từ; lỗi từ vựng không gây khó hiểu cho người đọc."
        },
        7: {
            en: "Uses a sufficient range of vocabulary; attempts less common lexis with occasional inappropriacies; errors do not impede communication.",
            vi: "Vốn từ đầy đủ đáp ứng yêu cầu đề; có nỗ lực dùng từ vựng theo chủ đề dù đôi khi còn dùng chưa chuẩn; các lỗi từ vựng không cản trở giao tiếp."
        },
        6: {
            en: "Uses a sufficient range of vocabulary; attempts less common lexis but most are faulty; errors do not impede communication.",
            vi: "Vốn từ đủ dùng cho B1; có thử dùng từ nâng cao nhưng phần lớn chưa chính xác; tuy vậy lỗi không cản trở việc truyền đạt thông điệp chính."
        },
        5: {
            en: "Uses an adequate range of vocabulary but tends to overuse certain lexical items; errors occur and may impede comprehension at times.",
            vi: "Vốn từ ở mức vừa phải nhưng lặp từ nhiều; mắc một số lỗi dùng từ đôi khi làm người đọc khó hiểu."
        },
        4: {
            en: "Uses basic vocabulary and acceptable control; errors are noticeable and impede comprehension at times.",
            vi: "Chỉ dùng từ vựng sơ cấp; lỗi dùng từ và chính tả xuất hiện rõ rệt, cản trở việc đọc hiểu ở nhiều chỗ."
        },
        3: {
            en: "Uses a limited range of basic vocabulary; errors are frequent and distort the meaning.",
            vi: "Vốn từ rất hạn hẹp; lỗi từ vựng xuất hiện liên tục và làm sai lệch ý nghĩa muốn diễn đạt."
        },
        2: {
            en: "Uses a very limited range of words and phrases; errors are dominant and distort the meaning.",
            vi: "Vốn từ cực kỳ nghèo nàn; lỗi sai chiếm ưu thế và làm sai lệch hoàn toàn nội dung."
        },
        1: {
            en: "Uses only a few isolated words.",
            vi: "Chỉ viết được một vài từ rời rạc."
        },
        0: {
            en: "Does not attend / no response.",
            vi: "Không có bài làm."
        }
    },
    grammar: {
        10: {
            en: "Uses a wide range of simple and complex structures precisely and flexibly; errors are very rare with just one or two minor slips.",
            vi: "Sử dụng rất đa dạng, chính xác và linh hoạt cả câu đơn và câu phức; lỗi ngữ pháp cực kỳ hiếm, chỉ là sơ suất nhỏ."
        },
        9: {
            en: "Uses a wide range of simple and complex structures precisely; the majority of the sentences are error-free; errors, if present, are non-systematic and non-impeding.",
            vi: "Vận dụng chuẩn xác nhiều cấu trúc câu đơn và câu phức; phần lớn các câu hoàn toàn không có lỗi; nếu có lỗi chỉ là không đáng kể."
        },
        8: {
            en: "Uses a variety of simple and complex structures with good control; the majority of the sentences are error-free; errors, if present, are non-systematic and non-impeding.",
            vi: "Kết hợp tốt câu đơn và câu phức; đa số các câu đúng ngữ pháp; các lỗi nhỏ không mang tính hệ thống và không cản trở việc hiểu."
        },
        7: {
            en: "Uses both simple and complex structures in a relatively effective way; errors occur but they rarely lead to misunderstanding.",
            vi: "Sử dụng tương đối hiệu quả cả câu đơn và câu phức; có lỗi ngữ pháp xuất hiện nhưng hiếm khi gây hiểu lầm."
        },
        6: {
            en: "Uses simple structures and attempts some complex structures; errors occur but they rarely lead to misunderstanding.",
            vi: "Kiểm soát tốt câu đơn và có cố gắng viết câu phức; có mắc lỗi ngữ pháp nhưng nhìn chung không cản trở việc hiểu nội dung."
        },
        5: {
            en: "Shows good control of simple structures; attempts complex structures, but most are faulty; errors occur but normally they do not impede comprehension.",
            vi: "Kiểm soát tốt các câu đơn giản; có thử viết câu phức nhưng hầu hết bị sai cấu trúc; lỗi không cản trở hoàn toàn việc đọc hiểu."
        },
        4: {
            en: "Shows adequate control of simple structures; attempts complex structures, but unsuccessfully; errors occur frequently and impede comprehension at times.",
            vi: "Chỉ kiểm soát được câu đơn giản ở mức vừa phải; câu phức hầu như thất bại; lỗi ngữ pháp xuất hiện thường xuyên, đôi khi gây khó hiểu."
        },
        3: {
            en: "Uses some simple structures correctly; frequently makes basic errors that distort the meaning.",
            vi: "Chỉ đúng được một vài câu đơn giản; thường xuyên mắc các lỗi ngữ pháp cơ bản làm bóp méo ý nghĩa."
        },
        2: {
            en: "Can only use some memorized structures; errors are dominant and distort the meaning.",
            vi: "Chỉ dùng được một vài mẫu câu học vẹt; lỗi ngữ pháp bao trùm bài viết và làm sai lệch ý nghĩa."
        },
        1: {
            en: "Cannot use sentence forms at all.",
            vi: "Hoàn toàn không thể tạo thành câu hoàn chỉnh."
        },
        0: {
            en: "Does not attend / no response.",
            vi: "Không có bài làm."
        }
    }
};

function getRubricDescriptor(criterion, bandScore) {
    const bandInt = Math.max(0, Math.min(10, Math.round(bandScore)));
    const critObj = VSTEP_OFFICIAL_RUBRIC[criterion];
    if (!critObj) return { en: "", vi: "" };
    return critObj[bandInt] || critObj[0];
}

// Function to render full comprehensive VSTEP evaluation

// ==========================================================================
// VSTEP B1 WRITING TASK 1 - SENTENCE-BY-SENTENCE AUDIT & DIAGNOSTIC ENGINE
// ==========================================================================

function segmentLetterSentences(rawText) {
    if (!rawText) return [];
    let text = rawText.replace(/\r\n/g, '\n').replace(/\r/g, '\n');
    
    // Protect common abbreviations from premature sentence splitting
    const abbrevs = ['mr\\.', 'mrs\\.', 'ms\\.', 'dr\\.', 'prof\\.', 'st\\.', 'e\\.g\\.', 'i\\.e\\.', 'etc\\.', 'vs\\.', 'a\\.m\\.', 'p\\.m\\.', 'no\\.'];
    abbrevs.forEach(abb => {
        const regex = new RegExp(`\\b${abb}`, 'gi');
        text = text.replace(regex, match => match.replace(/\./g, '\uE000'));
    });

    // Protect decimal numbers
    text = text.replace(/(\d+)\.(\d+)/g, '$1\uE000$2');

    // Split on sentence terminals (. ! ?) followed by whitespace or line break
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

function auditIndividualSentence(sentence, index, totalSentences, typeId, globalErrors = []) {
    const sTrim = sentence.trim();
    const sLower = sTrim.toLowerCase();

    // 1. Determine Section & Role
    let roleName = "Thân bài (Body)";
    let roleIcon = "fa-pencil";
    let isSalutation = false;
    let isSignOff = false;

    if (index === 0 && /^dear\s+[a-z]+/i.test(sTrim)) {
        roleName = "Lời chào mở đầu (Salutation)";
        roleIcon = "fa-envelope-open-text";
        isSalutation = true;
    } else if (index <= 2 && /(thanks?\s+for|hope\s+you|writing\s+this\s+letter|in\s+your\s+letter|how\s+are\s+you|glad\s+to\s+hear|i\s+am\s+writing)/i.test(sLower)) {
        roleName = "Mở đầu thư (Opening & Purpose)";
        roleIcon = "fa-book-open";
    } else if (index >= totalSentences - 2 && /(best\s+wishes|yours\s+(sincerely|faithfully)|warm\s+regards|love|cheers|sincerely)\b/i.test(sLower)) {
        roleName = "Lời chào kết thúc (Sign-off)";
        roleIcon = "fa-signature";
        isSignOff = true;
    } else if (index === totalSentences - 1 && sTrim.split(/\s+/).length <= 3 && !/[.!?]$/.test(sTrim)) {
        roleName = "Ký tên người gửi (Signature)";
        roleIcon = "fa-user-pen";
        isSignOff = true;
    } else if (index >= totalSentences - 3 && /(look\s+forward|hope\s+(my\s+advice|to\s+hear|you\s+can|this\s+helps)|let\s+me\s+know|see\s+you\s+soon|write\s+back)/i.test(sLower)) {
        roleName = "Câu kết thư (Closing)";
        roleIcon = "fa-paper-plane";
    }

    // 2. Identify sentence-specific errors
    const sentenceErrors = [];
    let rewrite = sTrim;

    // Check matched errors from global detector
    if (Array.isArray(globalErrors)) {
        globalErrors.forEach(err => {
            if (err.wrong && sLower.includes(err.wrong.toLowerCase())) {
                if (!sentenceErrors.some(e => e.wrong.toLowerCase() === err.wrong.toLowerCase())) {
                    sentenceErrors.push({
                        type: err.type || "Lỗi ngữ pháp",
                        wrong: err.wrong,
                        correct: err.correct,
                        reason: err.reason || "Cần điều chỉnh theo cấu trúc chuẩn."
                    });
                }
                const re = new RegExp(err.wrong.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'i');
                rewrite = rewrite.replace(re, err.correct);
            }
        });
    }

    // Modal + V-ing or Modal + to V
    const modalRule = /\b(should|can|could|will|would|must|may|might)\s+(to\s+([a-z]+)|([a-z]+ing))\b/i;
    const mModal = sTrim.match(modalRule);
    if (mModal) {
        const full = mModal[0];
        const modal = mModal[1];
        let correctV = '';
        if (mModal[2].startsWith('to ')) {
            correctV = mModal[3];
        } else {
            correctV = mModal[4].replace(/ing$/, '');
            if (mModal[4] === 'staying') correctV = 'stay';
            else if (mModal[4] === 'trying') correctV = 'try';
            else if (mModal[4] === 'going') correctV = 'go';
            else if (mModal[4] === 'visiting') correctV = 'visit';
            else if (mModal[4] === 'taking') correctV = 'take';
            else if (mModal[4] === 'eating') correctV = 'eat';
            else if (mModal[4] === 'wearing') correctV = 'wear';
        }
        if (!sentenceErrors.some(e => e.wrong.toLowerCase() === full.toLowerCase())) {
            sentenceErrors.push({
                type: "Động từ khuyết thiếu (Modal Verb)",
                wrong: full,
                correct: `${modal} ${correctV}`,
                reason: `Sau động từ khuyết thiếu '${modal}', động từ luôn ở dạng nguyên mẫu không 'to' (V-bare), không dùng 'to V' hay 'V-ing'.`
            });
            rewrite = rewrite.replace(new RegExp(full, 'i'), `${modal} ${correctV}`);
        }
    }

    // Missing 'to be' before adjectives
    const adjMissingBe = /\b(it|this|that|they|weather|food|room)\s+(convenient|delicious|hot|warm|cold|cheap|affordable|expensive|dirty|noisy|quiet|clean|important|necessary)\b/i;
    const mAdj = sTrim.match(adjMissingBe);
    if (mAdj) {
        const subj = mAdj[1];
        const adj = mAdj[2];
        const be = (subj.toLowerCase() === 'they') ? 'are' : 'is';
        if (!sentenceErrors.some(e => e.wrong.toLowerCase() === mAdj[0].toLowerCase())) {
            sentenceErrors.push({
                type: "Cấu trúc câu (Thiếu động từ 'to be')",
                wrong: mAdj[0],
                correct: `${subj} ${be} ${adj}`,
                reason: `Sau chủ ngữ '${subj}' đi kèm tính từ '${adj}' bắt buộc phải có liên động từ '${be}'.`
            });
            rewrite = rewrite.replace(new RegExp(mAdj[0], 'i'), `${subj} ${be} ${adj}`);
        }
    }

    // "look forward to + Vo"
    if (/\blook\s+forward\s+to\s+([a-z]+)\b/i.test(sTrim) && !/\blook\s+forward\s+to\s+[a-z]+ing\b/i.test(sTrim)) {
        const mLF = sTrim.match(/\blook\s+forward\s+to\s+([a-z]+)\b/i);
        if (mLF && mLF[1] !== 'hearing' && mLF[1] !== 'seeing' && mLF[1] !== 'meeting' && mLF[1] !== 'receiving') {
            const wrongW = mLF[1];
            let correctW = wrongW.replace(/e$/, '') + 'ing';
            if (wrongW === 'see') correctW = 'seeing';
            const fullW = mLF[0];
            const fixedW = `look forward to ${correctW}`;
            if (!sentenceErrors.some(e => e.wrong.toLowerCase() === fullW.toLowerCase())) {
                sentenceErrors.push({
                    type: "Cấu trúc câu (Look forward to + V-ing)",
                    wrong: fullW,
                    correct: fixedW,
                    reason: "Sau cụm cố định 'look forward to', động từ theo sau luôn chia ở dạng V-ing."
                });
                rewrite = rewrite.replace(new RegExp(fullW, 'i'), fixedW);
            }
        }
    }

    // "Thank for" -> "Thanks for / Thank you for"
    if (/\bThank\s+for\b/i.test(sTrim) && !/\bThanks\s+for\b/i.test(sTrim) && !/\bThank\s+you\s+for\b/i.test(sTrim)) {
        if (!sentenceErrors.some(e => e.wrong.toLowerCase().includes('thank for'))) {
            sentenceErrors.push({
                type: "Ngữ pháp mở thư",
                wrong: "Thank for",
                correct: "Thanks for / Thank you for",
                reason: "Cụm từ cảm ơn đúng phải có 's' ('Thanks for...') hoặc đầy đủ 'Thank you for...'."
            });
            rewrite = rewrite.replace(/\bThank\s+for\b/i, 'Thank you for');
        }
    }

    // "I am write" -> "I am writing"
    if (/\bI\s+(am|'m)\s+write\b/i.test(sTrim)) {
        if (!sentenceErrors.some(e => e.wrong.toLowerCase().includes('write'))) {
            sentenceErrors.push({
                type: "Thì hiện tại tiếp diễn",
                wrong: "I am write",
                correct: "I am writing",
                reason: "Sau 'am/is/are' trong thì hiện tại tiếp diễn, động từ phải thêm đuôi -ing: 'I am writing'."
            });
            rewrite = rewrite.replace(/\bI\s+(am|'m)\s+write\b/i, 'I am writing');
        }
    }

    // Missing articles before singular places/items
    const mStayArt = sTrim.match(/\bstay\s+(in|at)\s+(hotel|homestay)\b/i);
    if (mStayArt) {
        if (!sentenceErrors.some(e => e.wrong.toLowerCase() === mStayArt[0].toLowerCase())) {
            sentenceErrors.push({
                type: "Mạo từ (Articles)",
                wrong: mStayArt[0],
                correct: `stay ${mStayArt[1]} a ${mStayArt[2]}`,
                reason: `Danh từ đếm được số ít '${mStayArt[2]}' cần có mạo từ 'a' phía trước.`
            });
            rewrite = rewrite.replace(new RegExp(mStayArt[0], 'i'), `stay ${mStayArt[1]} a ${mStayArt[2]}`);
        }
    }

    // Capitalization of first letter
    if (/^[a-z]/.test(sTrim)) {
        sentenceErrors.push({
            type: "Chính tả (Viết hoa đầu câu)",
            wrong: sTrim.slice(0, 1),
            correct: sTrim.slice(0, 1).toUpperCase(),
            reason: "Chữ cái đầu tiên của câu bắt buộc phải viết hoa."
        });
        rewrite = rewrite.charAt(0).toUpperCase() + rewrite.slice(1);
    }

    // Punctuation at end of sentence (skip salutation / signoff)
    if (!isSalutation && !isSignOff && !/[.!?]$/.test(sTrim)) {
        sentenceErrors.push({
            type: "Dấu câu (Thiếu dấu kết câu)",
            wrong: sTrim.slice(-5),
            correct: sTrim.slice(-5) + '.',
            reason: "Câu kết thúc hoàn chỉnh cần có dấu chấm câu (.)."
        });
        rewrite = rewrite + '.';
    }

    // Determine sentence status
    let status = "success";
    let statusLabel = "✓ Câu viết chuẩn xác";
    let statusBadgeClass = "badge-success";

    if (sentenceErrors.length > 0) {
        status = "warning";
        statusLabel = `⚠️ Có ${sentenceErrors.length} lỗi cần khắc phục`;
        statusBadgeClass = "badge-warning";
    } else {
        // If no errors, suggest stylistic upgrade
        if (roleName.includes("Opening") && sLower.includes("give you some advice")) {
            rewrite = "I am writing this letter to share some useful recommendations for your upcoming trip to Can Tho in December.";
            status = "upgrade";
            statusLabel = "💡 Gợi ý nâng cấp B2 tự nhiên hơn";
            statusBadgeClass = "badge-upgrade";
        } else if (roleName.includes("Closing") && sLower.includes("see you soon")) {
            rewrite = "I hope these suggestions are helpful, and I cannot wait to see you in Can Tho!";
            status = "upgrade";
            statusLabel = "💡 Gợi ý nâng cấp B2 ấn tượng hơn";
            statusBadgeClass = "badge-upgrade";
        } else if (sLower.includes("they are very delicious")) {
            rewrite = "Not only are these local dishes incredibly delicious, but they are also very affordable.";
            status = "upgrade";
            statusLabel = "💡 Gợi ý cấu trúc nâng Band (Đảo ngữ)";
            statusBadgeClass = "badge-upgrade";
        }
    }

    // Highlight errors in original text
    let highlightedHtml = escapeHtml(sTrim);
    sentenceErrors.forEach(err => {
        const re = new RegExp(`(${err.wrong.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'gi');
        highlightedHtml = highlightedHtml.replace(re, '<span class="audit-err-highlight">$1</span>');
    });

    return {
        sentenceIndex: index + 1,
        totalSentences,
        originalText: sTrim,
        highlightedHtml,
        roleName,
        roleIcon,
        status,
        statusLabel,
        statusBadgeClass,
        errors: sentenceErrors,
        rewrite: rewrite.trim()
    };
}

function renderSentenceAuditSectionHtml(sentenceAudits) {
    if (!sentenceAudits || sentenceAudits.length === 0) return '';

    const correctCount = sentenceAudits.filter(s => s.status === 'success').length;
    const warningCount = sentenceAudits.filter(s => s.status === 'warning').length;
    const upgradeCount = sentenceAudits.filter(s => s.status === 'upgrade').length;

    return `
        <div class="sentence-audit-wrapper" style="margin-top: 30px;">
            <div class="sentence-audit-header">
                <div class="sentence-audit-title">
                    <i class="fa-solid fa-list-check" style="color: var(--primary-color, #6366f1);"></i>
                    <span>BẢNG RÀ SOÁT CHI TIẾT TỪNG CÂU HỌC VIÊN ĐÃ VIẾT (${sentenceAudits.length} CÂU)</span>
                </div>
                <div class="sentence-audit-stats">
                    <span class="stat-pill success"><i class="fa-solid fa-circle-check"></i> ${correctCount} câu chuẩn</span>
                    ${warningCount > 0 ? `<span class="stat-pill warning"><i class="fa-solid fa-triangle-exclamation"></i> ${warningCount} câu có lỗi</span>` : ''}
                    ${upgradeCount > 0 ? `<span class="stat-pill upgrade"><i class="fa-solid fa-wand-magic-sparkles"></i> ${upgradeCount} câu gợi ý nâng Band</span>` : ''}
                </div>
            </div>
            <p class="sentence-audit-sub">
                Hệ thống bóc tách tỉ mỉ từng câu trong bài viết của bạn, đối chiếu ngữ pháp, chỉ ra lỗi cụ thể và cung cấp câu viết lại chuẩn B1/B2 để bạn học hỏi và cải thiện:
            </p>

            <div class="sentence-cards-list">
                ${sentenceAudits.map(s => `
                    <div class="sentence-audit-card ${s.status}">
                        <div class="sentence-card-head">
                            <div class="sentence-head-left">
                                <span class="sentence-index-badge">CÂU ${s.sentenceIndex}/${s.totalSentences}</span>
                                <span class="sentence-role-badge"><i class="fa-solid ${s.roleIcon}"></i> ${s.roleName}</span>
                            </div>
                            <span class="sentence-status-pill ${s.statusBadgeClass}">${s.statusLabel}</span>
                        </div>

                        <div class="sentence-card-content">
                            <div class="sentence-row original-row">
                                <span class="row-tag original-tag">Học viên viết:</span>
                                <div class="sentence-text original-text">"${s.highlightedHtml}"</div>
                            </div>

                            ${s.errors.length > 0 ? `
                                <div class="sentence-errors-box">
                                    <strong style="color: #dc2626; font-size: 13.5px;"><i class="fa-solid fa-circle-xmark"></i> Các lỗi cần khắc phục trong câu này:</strong>
                                    <ul class="sentence-error-items">
                                        ${s.errors.map(err => `
                                            <li>
                                                <span class="err-sub-type">[${escapeHtml(err.type)}]</span> 
                                                Viết sai: <span class="err-strike">"${escapeHtml(err.wrong)}"</span> 
                                                ➔ Sửa đúng: <strong class="err-fix">"${escapeHtml(err.correct)}"</strong>
                                                <div class="err-reason-note">💡 ${escapeHtml(err.reason)}</div>
                                            </li>
                                        `).join('')}
                                    </ul>
                                </div>
                            ` : ''}

                            <div class="sentence-row rewrite-row">
                                <span class="row-tag rewrite-tag"><i class="fa-solid fa-wand-magic-sparkles"></i> ${s.errors.length > 0 ? 'Viết lại đúng chuẩn:' : 'Gợi ý câu chuẩn B1/B2 mượt mà hơn:'}</span>
                                <div class="sentence-text rewrite-text">"${escapeHtml(s.rewrite)}"</div>
                            </div>
                        </div>
                    </div>
                `).join('')}
            </div>
        </div>
    `;
}


function renderFullPracticeEvaluationResult(rawText, typeId, timeSpentStr) {
    if (!fullPracticeResultBox) fullPracticeResultBox = document.getElementById('fullPracticeResultBox');
    if (!fullPracticeResultBox) return;

    const words = rawText ? rawText.split(/\s+/).filter(w => w !== '') : [];
    const wordCount = words.length;
    const lower = rawText ? rawText.toLowerCase() : '';

    const typeData = letterTypes.find(t => t.id === typeId) || letterTypes[0];
    const letterTitle = typeData ? `${typeData.titleEn} (${typeData.titleVi})` : 'VSTEP Task 1';

    // Model sample letter extraction
    const tempDiv = document.createElement('div');
    tempDiv.innerHTML = typeData ? typeData.sampleWriting : '';
    const sampleContent = tempDiv.querySelector('.content-block') ? tempDiv.querySelector('.content-block').innerHTML : (typeData ? typeData.sampleWriting : '');

    if (wordCount === 0) {
        fullPracticeResultBox.innerHTML = `
            <div class="practice-summary-card">
                <div class="practice-summary-header" style="color: #ef4444;">
                    <i class="fa-solid fa-triangle-exclamation"></i> BÀI NỘP CHƯA CÓ NỘI DUNG
                </div>
                <p style="color: var(--text-muted); font-size: 15px;">Bạn chưa nhập nội dung bài viết trước khi nộp bài. Vui lòng bấm nút bên dưới để viết bài!</p>
                <div style="margin-top: 20px;">
                    <button class="btn btn-primary" id="btnRestartFullPractice" style="padding: 12px 32px; font-weight: 700; border-radius: 10px;">
                        <i class="fa-solid fa-rotate-left"></i> Viết lại bài này
                    </button>
                </div>
            </div>
        `;
        const btnRestart = document.getElementById('btnRestartFullPractice');
        if (btnRestart) btnRestart.addEventListener('click', resetFullPracticeUI);
        return;
    }

    // --- 1. TASK FULFILMENT (0 - 10) ---
    let hasReq1 = false, hasReq2 = false, hasReq3 = false, hasReq4 = false;
    let reqLabels = [];

    if (typeId === 'advice') {
        hasReq1 = /(stay|hotel|homestay|room|guest\s*house|resort|city\s*cent|old\s*quarter)/i.test(lower);
        hasReq2 = /(dish|dishes|food|pancake|pho|banh\s*mi|bun\s*cha|spring\s*roll|fruit|eat|taste|try|specialt|noodle)/i.test(lower);
        hasReq3 = /(attraction|visit|place|places|lake|hoan\s*kiem|temple|literature|old\s*quarter|museum|market|cai\s*rang|ninh\s*kieu)/i.test(lower);
        hasReq4 = /(wear|clothes|cloth|jacket|umbrella|hat|sunglass|shoes|sneaker|raincoat|t-shirt|shorts|dress|weather|hot|warm)/i.test(lower);
        reqLabels = [
            hasReq1 ? '✓ Nơi ở (Where to stay)' : '✗ Nơi ở (Where to stay)',
            hasReq2 ? '✓ Món ăn nên thử (What dishes to try)' : '✗ Món ăn nên thử (What dishes to try)',
            hasReq3 ? '✓ Địa điểm tham quan (Places to visit)' : '✗ Địa điểm tham quan (Places to visit)',
            hasReq4 ? '✓ Trang phục phù hợp (What to wear)' : '✗ Trang phục phù hợp (What to wear)'
        ];
    } else if (typeId === 'request') {
        hasReq1 = /(address|location|where\s+(is\s+)?the\s+center|near\s+my\s+(house|home)|street|district|located)/i.test(lower);
        hasReq2 = /(fee|tuition|cost|price|money|how\s+much|budget|pay|discount|million|vnd)/i.test(lower);
        hasReq3 = /(teacher|teachers|instructor|friendly|experienced|enthusiastic|native|teach|helpful)/i.test(lower);
        hasReq4 = /(program|training|course|curriculum|skill|schedule|length|study|practise|practice|topic)/i.test(lower);
        reqLabels = [
            hasReq1 ? '✓ Địa chỉ trung tâm (Address)' : '✗ Địa chỉ trung tâm (Address)',
            hasReq2 ? '✓ Học phí khóa học (Tuition fee)' : '✗ Học phí khóa học (Tuition fee)',
            hasReq3 ? '✓ Đội ngũ giáo viên (Teachers)' : '✗ Đội ngũ giáo viên (Teachers)',
            hasReq4 ? '✓ Chương trình đào tạo (Training program)' : '✗ Chương trình đào tạo (Training program)'
        ];
    } else if (typeId === 'description') {
        hasReq1 = /(kind|friendly|helpful|nice|polite|humorous|cheerful|personality|honest|generous|sociable)/i.test(lower);
        hasReq2 = /(hobby|hobbies|free\s*time|leisure|reading|books|cooking|music|sport|sports|swimming|singing)/i.test(lower);
        hasReq3 = /(study|studying|work|working|university|college|student|business|major|job|company)/i.test(lower);
        hasReq4 = /(fit|get\s*on|stay\s*with|live\s*with|adapt|tidy|clean|responsible|family)/i.test(lower);
        reqLabels = [
            hasReq1 ? '✓ Tính cách (Personality)' : '✗ Tính cách (Personality)',
            hasReq2 ? '✓ Sở thích (Hobbies)' : '✗ Sở thích (Hobbies)',
            hasReq3 ? '✓ Việc học/làm hiện tại (Current work/study)' : '✗ Việc học/làm hiện tại (Current work/study)',
            hasReq4 ? '✓ Khả năng hòa nhập gia đình (Fit in family)' : '✗ Khả năng hòa nhập gia đình (Fit in family)'
        ];
    } else if (typeId === 'complaint') {
        hasReq1 = /(problem|problems|room|condition|floor|dirty|wet|locker|lockers|broken|shower|showers|water|ac|air\s*con|facility)/i.test(lower);
        hasReq2 = /(feel|felt|disappoint|unhappy|annoyed|upset|ruin|terrible|bad\s*experience|frustrated|dangerous)/i.test(lower);
        hasReq3 = /(suggest|improve|repair|replace|clean|fix|solution|facility|better|manager)/i.test(lower);
        hasReq4 = true;
        reqLabels = [
            hasReq1 ? '✓ Mô tả sự cố/vấn đề (Problems)' : '✗ Mô tả sự cố/vấn đề (Problems)',
            hasReq2 ? '✓ Cảm xúc của bản thân (Feelings)' : '✗ Cảm xúc của bản thân (Feelings)',
            hasReq3 ? '✓ Đề xuất biện pháp cải thiện (Suggestions)' : '✗ Đề xuất biện pháp cải thiện (Suggestions)'
        ];
    } else if (typeId === 'feedback') {
        hasReq1 = /(satisf|dissatisf|overall|enjoy|opinion|pleas|feedback|impression|feel|experience)/i.test(lower);
        hasReq2 = /(food|dish|room|service|staff|atmosphere|decor|view|breakfast|stay|hotel|restaurant)/i.test(lower);
        hasReq3 = /(suggest|improve|service|staff|speed\s*up|faster|clean|price|discount|training)/i.test(lower);
        hasReq4 = true;
        reqLabels = [
            hasReq1 ? '✓ Mức độ hài lòng (Satisfaction)' : '✗ Mức độ hài lòng (Satisfaction)',
            hasReq2 ? '✓ Mô tả trải nghiệm thực tế (Experience)' : '✗ Mô tả trải nghiệm thực tế (Experience)',
            hasReq3 ? '✓ Gợi ý cải tiến chất lượng (Improvement)' : '✗ Gợi ý cải tiến chất lượng (Improvement)'
        ];
    } else if (typeId === 'apology') {
        hasReq1 = /(apologiz|apologise|sorry|apology|forgive|regret|excuse)/i.test(lower);
        hasReq2 = /(busy|exam|work|sick|ill|situation|finish|finished|reading|book|reason|because)/i.test(lower);
        hasReq3 = /(return|give\s*back|send|meet|tomorrow|next\s*week|by\s*hand|post)/i.test(lower);
        hasReq4 = true;
        reqLabels = [
            hasReq1 ? '✓ Lời xin lỗi chân thành (Apology)' : '✗ Lời xin lỗi chân thành (Apology)',
            hasReq2 ? '✓ Giải thích tình huống & tình trạng đọc sách' : '✗ Giải thích tình huống & tình trạng đọc sách',
            hasReq3 ? '✓ Thời gian và cách thức trả sách (When & How)' : '✗ Thời gian và cách thức trả sách (When & How)'
        ];
    } else if (typeId === 'application') {
        hasReq1 = /(apply|application|position|sales\s*assistant|job|advertis|student|myself)/i.test(lower);
        hasReq2 = /(interest|interested|passion|clothing|store|fashion|career|environment|why)/i.test(lower);
        hasReq3 = /(experience|work|worked|part-time|customer|customers|friendly|communicat|skills|suit)/i.test(lower);
        hasReq4 = true;
        reqLabels = [
            hasReq1 ? '✓ Giới thiệu bản thân & Vị trí ứng tuyển' : '✗ Giới thiệu bản thân & Vị trí ứng tuyển',
            hasReq2 ? '✓ Lý do quan tâm công việc' : '✗ Lý do quan tâm công việc',
            hasReq3 ? '✓ Kinh nghiệm làm việc với khách hàng' : '✗ Kinh nghiệm làm việc với khách hàng'
        ];
    } else {
        hasReq1 = true; hasReq2 = true; hasReq3 = true; hasReq4 = true;
        reqLabels = ['✓ Đáp ứng đầy đủ các yêu cầu cốt lõi'];
    }

    let coveredCount = [hasReq1, hasReq2, hasReq3, hasReq4].filter(Boolean).length;
    const isCompletelyOffTopic = (coveredCount === 0);
    const isPartiallyOffTopic = (coveredCount === 1);

    let tfScore = 8.5;
    if (coveredCount === 4) {
        tfScore = wordCount >= 140 ? 9.0 : (wordCount >= 120 ? 8.5 : 7.5);
    } else if (coveredCount === 3) {
        tfScore = wordCount >= 120 ? 7.5 : 6.5;
    } else if (coveredCount === 2) {
        tfScore = 5.5;
    } else if (coveredCount === 1) {
        tfScore = wordCount >= 120 ? 4.0 : 3.0;
    } else {
        tfScore = 1.5; // Completely off-topic (0 bullet points met)
    }
    if (wordCount < 100 && !isCompletelyOffTopic) tfScore = Math.max(2.0, tfScore - 2.0);
    if (wordCount < 60 && !isCompletelyOffTopic) tfScore = Math.max(1.0, tfScore - 3.0);

    // --- 2. ORGANIZATION (0 - 10) ---
    const hasGreeting = /^dear\s+[a-z]+/i.test(rawText.trim()) || /dear\s+(mr|ms|mrs|sir|madam)/i.test(rawText.trim());
    const hasOpening = /(thanks?\s+for|hope\s+you|writing\s+to|how\s+are\s+you|in\s+your\s+letter|i\s+am\s+writing)/i.test(lower);
    const hasClosing = /(hope\s+(my\s+advice|you\s+can|you\s+will|this\s+helps)|write\s+back|let\s+me\s+know|look\s+forward|thank\s+you\s+for\s+your\s+time)/i.test(lower);
    const hasSignoff = /(best\s+wishes|yours\s+(sincerely|faithfully)|warm\s+regards|love)/i.test(lower);

    const linkingWordsList = [
        "firstly", "secondly", "next", "finally", "moreover", "besides",
        "furthermore", "in addition", "therefore", "however", "for example", "first of all", "also", "because"
    ];
    let linkCount = 0;
    linkingWordsList.forEach(lw => {
        if (lower.includes(lw)) linkCount++;
    });

    const hasParagraphs = (rawText.split(/\n+/).filter(p => p.trim() !== '').length) >= 3;

    let orgScore = 8.0;
    let orgPartsCount = [hasGreeting, hasOpening, hasClosing, hasSignoff].filter(Boolean).length;
    if (orgPartsCount === 4 && linkCount >= 4 && hasParagraphs) {
        orgScore = 9.0;
    } else if (orgPartsCount === 4 && linkCount >= 3) {
        orgScore = 8.0;
    } else if (orgPartsCount >= 3 && linkCount >= 2) {
        orgScore = 7.0;
    } else if (orgPartsCount >= 2) {
        orgScore = 5.5;
    } else {
        orgScore = 4.0;
    }

    // --- 3. DIAGNOSE ERRORS (VOCABULARY & GRAMMAR) ---
    const promptDummyData = { bulletPoints: [] };
    const errors = (typeof diagnoseVstepErrors === 'function') 
        ? diagnoseVstepErrors(rawText, promptDummyData)
        : [];

    const vocabErrors = errors.filter(e => e.category === 'vocab' || e.category === 'word_form');
    const grammarErrors = errors.filter(e => e.category === 'grammar' || e.category === 'article' || e.category === 'preposition');
    const mechanicsErrors = errors.filter(e => e.category === 'punctuation' || e.category === 'spelling');

    // --- 4. VOCABULARY (0 - 10) ---
    let vocScore = 8.5;
    if (vocabErrors.length >= 3) {
        vocScore = 6.0;
    } else if (vocabErrors.length === 2) {
        vocScore = 6.5;
    } else if (vocabErrors.length === 1) {
        vocScore = 7.5;
    }
    if (wordCount < 120) vocScore = Math.max(4.0, vocScore - 1.0);

    // --- 5. GRAMMAR & ACCURACY (0 - 10) ---
    let gramScore = 8.5;
    const totalGrammarImpact = grammarErrors.length + (mechanicsErrors.length > 0 ? 1 : 0);
    if (totalGrammarImpact >= 6) {
        gramScore = 5.5;
    } else if (totalGrammarImpact >= 4) {
        gramScore = 6.0;
    } else if (totalGrammarImpact >= 2) {
        gramScore = 7.0;
    } else if (totalGrammarImpact === 1) {
        gramScore = 8.0;
    }

    // --- TOTAL VSTEP SCORES & 30% EXAM CONVERSION ---
    let overallBand = (tfScore + orgScore + vocScore + gramScore) / 4.0;
    overallBand = Math.round(overallBand * 10) / 10;

    // Converted to 30% of VSTEP Writing exam (Max 3.00 points)
    let convertedScore = Math.round((overallBand / 10.0) * 3.0 * 100) / 100;

    // 4 Criteria converted to 0.75 points each (0.75 x 4 = 3.00 points)
    let tfConv = Math.round((tfScore / 10.0) * 0.75 * 100) / 100;
    let orgConv = Math.round((orgScore / 10.0) * 0.75 * 100) / 100;
    let vocConv = Math.round((vocScore / 10.0) * 0.75 * 100) / 100;
    let gramConv = Math.round((gramScore / 10.0) * 0.75 * 100) / 100;

    let vstepLevel = "B1 LEVEL (ĐẠT CHUẨN)";
    let levelBadgeStyle = "background: #10b981; color: #ffffff;";
    let levelSummary = "Bài viết đạt chuẩn yêu cầu VSTEP B1. Bố cục đầy đủ và nội dung bám sát đề thi. Cần xem lại các lỗi nhỏ được đánh dấu bên dưới để tối ưu điểm số.";

    if (isCompletelyOffTopic) {
        vstepLevel = "LẠC ĐỀ HOÀN TOÀN (OFF-TOPIC)";
        levelBadgeStyle = "background: #dc2626; color: #ffffff;";
        levelSummary = "Cảnh báo nghiêm trọng: Bài viết hoàn toàn không bám sát yêu cầu đề bài! Bị chấm điểm liệt Task Fulfilment (1.5/10) và khống chế điểm toàn bài.";
    } else if (isPartiallyOffTopic) {
        vstepLevel = "NGUY CƠ LẠC ĐỀ (PARTIALLY OFF-TOPIC)";
        levelBadgeStyle = "background: #d97706; color: #ffffff;";
        levelSummary = "Cảnh báo: Bài viết chỉ chạm vào 1 ý nhỏ và bỏ sót hầu hết các yêu cầu cốt lõi của đề bài. Điểm Task Fulfilment bị trừ rất nặng.";
    } else if (overallBand >= 8.5) {
        vstepLevel = "B2 LEVEL (XUẤT SẮC - VƯỢT CHUẨN)";
        levelBadgeStyle = "background: #6366f1; color: #ffffff;";
        levelSummary = "Bài viết xuất sắc! Độ hoàn thành cao, câu văn tự nhiên, từ vựng phong phú và cấu trúc chuẩn mực B2.";
    } else if (overallBand < 6.0) {
        vstepLevel = "DƯỚI CHUẨN B1 (CẦN CẢI THIỆN)";
        levelBadgeStyle = "background: #ef4444; color: #ffffff;";
        levelSummary = "Bài viết còn nhiều lỗi ngữ pháp hoặc chưa đủ độ dài quy định (tối thiểu 120 từ). Hãy nghiên cứu kỹ bài mẫu và bảng sửa lỗi bên dưới nhé!";
    }

    // Official Rubric Descriptors Lookup
    const tfDesc = getRubricDescriptor('taskFulfilment', tfScore);
    const orgDesc = getRubricDescriptor('organization', orgScore);
    const vocDesc = getRubricDescriptor('vocabulary', vocScore);
    const gramDesc = getRubricDescriptor('grammar', gramScore);

    // Build Inline Annotated Essay HTML
    // Segment and audit every single sentence
    const segmentedSentences = segmentLetterSentences(rawText);
    const sentenceAudits = segmentedSentences.map((s, idx) => 
        auditIndividualSentence(s, idx, segmentedSentences.length, typeId, errors)
    );
    const sentenceAuditSectionHtml = renderSentenceAuditSectionHtml(sentenceAudits);

    const annotatedEssayHtml = (typeof buildAnnotatedEssayHtml === 'function')
        ? buildAnnotatedEssayHtml(rawText, errors)
        : escapeHtml(rawText);

    // Build Error Table HTML
    let errorTableHtml = '';
    if (errors.length > 0) {
        let rowsHtml = errors.map((err, idx) => `
            <tr>
                <td style="font-weight: 700; color: var(--primary-color); text-align: center;">${idx + 1}</td>
                <td><span class="err-badge-type">${err.type}</span></td>
                <td><span class="err-text-wrong">${err.wrong}</span></td>
                <td><span class="err-text-correct"><i class="fa-solid fa-arrow-right"></i> ${err.correct}</span></td>
                <td style="font-size: 13.5px; color: var(--text-main); line-height: 1.5;">${err.reason}</td>
            </tr>
        `).join('');

        errorTableHtml = `
            <div class="extra-error-table-wrapper" style="margin-top: 25px;">
                <div class="error-table-title">
                    <i class="fa-solid fa-triangle-exclamation" style="color: #ef4444;"></i>
                    DANH SÁCH ${errors.length} LỖI CẦN SỬA CHI TIẾT (NGỮ PHÁP, MẠO TỪ, TỪ LOẠI, DÙNG TỪ, CHÍNH TẢ, DẤU CÂU):
                </div>
                <div class="table-responsive">
                    <table class="error-table">
                        <thead>
                            <tr>
                                <th style="width: 40px; text-align: center;">#</th>
                                <th style="width: 170px;">Phân loại lỗi</th>
                                <th style="width: 190px;">Học viên viết</th>
                                <th style="width: 220px;">Đề xuất sửa đúng</th>
                                <th>Giải thích ngữ pháp chi tiết</th>
                            </tr>
                        </thead>
                        <tbody>
                            ${rowsHtml}
                        </tbody>
                    </table>
                </div>
            </div>
        `;
    } else {
        errorTableHtml = `
            <div class="highlight-box" style="margin-top: 25px;">
                <p><i class="fa-solid fa-circle-check" style="color: #10b981;"></i> <strong>Không phát hiện lỗi ngữ pháp hay từ vựng đáng kể nào!</strong> Bài làm của bạn rất chuẩn chỉnh và mạch lạc.</p>
            </div>
        `;
    }

    // Build Off-Topic Alert Box if essay fails core prompts
    let offTopicAlertHtml = '';
    if (isCompletelyOffTopic) {
        offTopicAlertHtml = `
            <div class="off-topic-alert-box" style="background: #fef2f2; border: 2.5px solid #ef4444; border-radius: 14px; padding: 20px 24px; margin-bottom: 24px; box-shadow: 0 4px 14px rgba(239, 68, 68, 0.15);">
                <div style="display: flex; align-items: center; gap: 12px; color: #b91c1c; font-size: 19px; font-weight: 800;">
                    <i class="fa-solid fa-triangle-exclamation" style="font-size: 26px; color: #ef4444;"></i>
                    <span>CẢNH BÁO NGUY HIỂM: BÀI VIẾT LẠC ĐỀ HOÀN TOÀN (OFF-TOPIC)!</span>
                </div>
                <p style="margin: 12px 0 8px 0; color: #991b1b; font-size: 15px; line-height: 1.6;">
                    ⚠️ Bài viết của bạn <strong>hoàn toàn không bám sát yêu cầu đề bài ${letterTitle}</strong>! Bạn không trả lời được ý nào trong 4 ý hỏi cốt lõi của đề bài. Theo quy định chấm thi VSTEP của Bộ GD&ĐT, bài viết lạc đề sẽ bị chấm điểm liệt (Band 1.0 - 2.0) ở tiêu chí Task Fulfilment và khống chế tối đa điểm toàn bài.
                </p>
                <div style="margin-top: 12px; background: rgba(239, 68, 68, 0.08); padding: 14px 18px; border-radius: 10px; font-size: 14px; color: #7f1d1d;">
                    <strong>Các yêu cầu cốt lõi đề bài bắt buộc phải có:</strong>
                    <ul style="margin: 8px 0 0 20px; line-height: 1.7;">
                        ${reqLabels.map(l => `<li>${l}</li>`).join('')}
                    </ul>
                </div>
            </div>
        `;
    } else if (isPartiallyOffTopic) {
        offTopicAlertHtml = `
            <div class="off-topic-alert-box" style="background: #fffbeb; border: 2px solid #f59e0b; border-radius: 14px; padding: 18px 22px; margin-bottom: 24px;">
                <div style="display: flex; align-items: center; gap: 10px; color: #b45309; font-size: 18px; font-weight: 800;">
                    <i class="fa-solid fa-circle-exclamation" style="font-size: 24px; color: #f59e0b;"></i>
                    <span>CẢNH BÁO: BÀI VIẾT CÓ DẤU HIỆU LẠC ĐỀ / THIẾU Ý TRỌNG TÂM!</span>
                </div>
                <p style="margin: 10px 0 6px 0; color: #92400e; font-size: 14.5px; line-height: 1.6;">
                    ⚠️ Bài viết chỉ mới chạm vào <strong>1/${reqLabels.length} yêu cầu</strong> của đề bài và bỏ sót các trọng tâm còn lại. Điểm Task Fulfilment bị trừ rất nặng.
                </p>
                <div style="margin-top: 8px; font-size: 13.5px; color: #78350f;">
                    <strong>Kiểm tra lại các ý cần có trong bài:</strong>
                    <ul style="margin: 6px 0 0 20px; line-height: 1.7;">
                        ${reqLabels.map(l => `<li>${l}</li>`).join('')}
                    </ul>
                </div>
            </div>
        `;
    }

    // Render HTML in fullPracticeResultBox
    fullPracticeResultBox.innerHTML = `
        ${offTopicAlertHtml}

        <!-- VSTEP Overall Score Banner -->
        <div class="extra-score-banner">
            <div class="score-main-group">
                <div class="score-circle-badge">
                    ${convertedScore.toFixed(2)}
                    <span style="font-size: 13px; display: block; font-weight: 500; opacity: 0.9;">/ 3.00</span>
                </div>
                <div class="score-text-info">
                    <h4>${vstepLevel} • ${convertedScore.toFixed(2)} / 3.00 ĐIỂM (30% BÀI THI WRITING)</h4>
                    <p>Tương đương <strong>Band ${overallBand.toFixed(1)} / 10.0</strong> theo khung chấm chuẩn VSTEP Writing Task 1 của Bộ GD&ĐT.</p>
                    <div style="margin-top: 6px; font-size: 13.5px; opacity: 0.95;">
                        <span><i class="fa-solid fa-user-graduate"></i> ${currentStudentName || 'Học viên'} (Lớp ${currentStudentClass || 'CB206'})</span> • 
                        <span><i class="fa-solid fa-pen-nib"></i> ${wordCount} từ (${wordCount >= 120 ? '✓ Đạt độ dài' : '⚠️ Chưa đủ từ'})</span> • 
                        <span><i class="fa-solid fa-clock"></i> Thời gian: ${timeSpentStr} / 20:00</span>
                    </div>
                </div>
            </div>
            <div class="extra-b1-badge" style="background: #ffffff; color: var(--primary-color); font-weight: 800;">
                TASK 1 = 30% ĐIỂM WRITING
            </div>
        </div>

        <div class="recitation-report-status" style="margin-top: 15px; margin-bottom: 20px; background: #ecfdf5; border: 1.5px solid #10b981; border-radius: 12px; padding: 14px 18px; color: #065f46;">
            <i class="fa-solid fa-circle-check report-status-icon" style="color: #10b981; font-size: 18px;"></i>
            <span><strong>BẢN ĐÁNH GIÁ VÀ SỬA BÀI CHI TIẾT DÀNH CHO HỌC VIÊN:</strong> Dưới đây là điểm số 4 tiêu chí chuẩn VSTEP, bản sửa lỗi từng câu từ trên bài viết của bạn và bài mẫu đối chiếu để bạn học hỏi và cải thiện ngay lập tức! (Đồng thời kết quả cũng đã tự động gửi lưu về hệ thống quản lý của giáo viên).</span>
        </div>

        <!-- 4 Criteria Rubric Grid based on VSTEP SCORING GUIDE (media_1787637818545.jpg) -->
        <div style="margin-top: 25px; margin-bottom: 12px; font-weight: 800; font-size: 17px; color: var(--text-main); display: flex; align-items: center; gap: 8px;">
            <i class="fa-solid fa-scale-balanced" style="color: var(--primary-color);"></i>
            ĐÁNH GIÁ CHI TIẾT THEO 4 TIÊU CHÍ (RATING SCALE FOR VSTEP WRITING TASK 1):
        </div>

        <div class="criteria-grid">
            <!-- 1. Task Fulfilment -->
            <div class="criterion-card">
                <div class="criterion-name">
                    <span>Task Fulfilment (30%)</span>
                    <span class="criterion-score">${tfConv.toFixed(2)}/0.75 <small style="font-size: 11px; font-weight: normal; color: var(--text-muted);">(${tfScore.toFixed(1)}/10)</small></span>
                </div>
                <div class="criterion-desc">
                    <div style="margin-bottom: 6px; font-weight: 600; color: var(--text-main);">
                        ${reqLabels.join(' | ')}.
                    </div>
                    <div>Độ dài: <strong>${wordCount} từ</strong> (${wordCount >= 120 ? 'Đạt chuẩn ≥120 từ' : 'Chưa đủ độ dài'}).</div>
                </div>
                <div class="vstep-official-descriptor-box">
                    <span class="descriptor-tag"><i class="fa-solid fa-stamp"></i> Chuẩn VSTEP Band ${Math.round(tfScore)}:</span>
                    <p class="descriptor-text">"${tfDesc.en}"</p>
                    <p style="margin: 4px 0 0 0; font-size: 12px; color: var(--text-muted);">↳ <em>${tfDesc.vi}</em></p>
                </div>
            </div>

            <!-- 2. Organization -->
            <div class="criterion-card">
                <div class="criterion-name">
                    <span>Organization (30%)</span>
                    <span class="criterion-score">${orgConv.toFixed(2)}/0.75 <small style="font-size: 11px; font-weight: normal; color: var(--text-muted);">(${orgScore.toFixed(1)}/10)</small></span>
                </div>
                <div class="criterion-desc">
                    <div style="margin-bottom: 6px; font-weight: 600; color: var(--text-main);">
                        Bố cục 5 phần chuẩn mực (${orgPartsCount}/4 phần cốt lõi: Greeting, Opening, Closing, Sign-off).
                    </div>
                    <div>Sử dụng <strong>${linkCount} liên từ nối</strong> chuyển tiếp câu mạch lạc.</div>
                </div>
                <div class="vstep-official-descriptor-box">
                    <span class="descriptor-tag"><i class="fa-solid fa-stamp"></i> Chuẩn VSTEP Band ${Math.round(orgScore)}:</span>
                    <p class="descriptor-text">"${orgDesc.en}"</p>
                    <p style="margin: 4px 0 0 0; font-size: 12px; color: var(--text-muted);">↳ <em>${orgDesc.vi}</em></p>
                </div>
            </div>

            <!-- 3. Vocabulary -->
            <div class="criterion-card">
                <div class="criterion-name">
                    <span>Vocabulary (30%)</span>
                    <span class="criterion-score">${vocConv.toFixed(2)}/0.75 <small style="font-size: 11px; font-weight: normal; color: var(--text-muted);">(${vocScore.toFixed(1)}/10)</small></span>
                </div>
                <div class="criterion-desc">
                    <div style="margin-bottom: 6px; font-weight: 600; color: var(--text-main);">
                        Vốn từ vựng theo chủ đề ${letterTitle}.
                    </div>
                    <div>${vocabErrors.length > 0 ? `Bị trừ điểm do mắc <strong>${vocabErrors.length} lỗi</strong> từ vựng / từ loại.` : 'Sử dụng từ vựng chính xác, linh hoạt.'}</div>
                </div>
                <div class="vstep-official-descriptor-box">
                    <span class="descriptor-tag"><i class="fa-solid fa-stamp"></i> Chuẩn VSTEP Band ${Math.round(vocScore)}:</span>
                    <p class="descriptor-text">"${vocDesc.en}"</p>
                    <p style="margin: 4px 0 0 0; font-size: 12px; color: var(--text-muted);">↳ <em>${vocDesc.vi}</em></p>
                </div>
            </div>

            <!-- 4. Grammar & Accuracy -->
            <div class="criterion-card">
                <div class="criterion-name">
                    <span>Grammar & Accuracy (30%)</span>
                    <span class="criterion-score">${gramConv.toFixed(2)}/0.75 <small style="font-size: 11px; font-weight: normal; color: var(--text-muted);">(${gramScore.toFixed(1)}/10)</small></span>
                </div>
                <div class="criterion-desc">
                    <div style="margin-bottom: 6px; font-weight: 600; color: var(--text-main);">
                        Cấu trúc câu đơn & câu phức B1.
                    </div>
                    <div>${totalGrammarImpact > 0 ? `Bị trừ điểm do phát hiện <strong>${grammarErrors.length} lỗi</strong> ngữ pháp/mạo từ và lỗi dấu câu/chính tả.` : 'Ngữ pháp chuẩn xác, câu văn trôi chảy.'}</div>
                </div>
                <div class="vstep-official-descriptor-box">
                    <span class="descriptor-tag"><i class="fa-solid fa-stamp"></i> Chuẩn VSTEP Band ${Math.round(gramScore)}:</span>
                    <p class="descriptor-text">"${gramDesc.en}"</p>
                    <p style="margin: 4px 0 0 0; font-size: 12px; color: var(--text-muted);">↳ <em>${gramDesc.vi}</em></p>
                </div>
            </div>
        </div>

        <!-- Section: Bản sửa lỗi trực tiếp trên bài viết của học viên -->
        <div class="annotated-essay-card" style="margin-top: 30px;">
            <div class="annotated-essay-header">
                <i class="fa-solid fa-pen-to-square"></i> BẢN SỬA LỖI TRỰC TIẾP TRÊN BÀI VIẾT CỦA BẠN (INLINE CORRECTIONS):
            </div>
            <div class="annotated-essay-body">
                ${annotatedEssayHtml}
            </div>
        </div>

        ${sentenceAuditSectionHtml}

        <!-- Detailed Error Table -->
        ${errorTableHtml}

        <!-- Side-by-Side Comparison with Model Letter -->
        <div class="practice-comparison-section" style="margin-top: 35px;">
            <div class="practice-comparison-col">
                <div class="practice-col-header student-col">
                    <i class="fa-solid fa-user-pen"></i> BÀI VIẾT GỐC CỦA BẠN (${wordCount} TỪ)
                </div>
                <div class="practice-paper-view">${escapeHtml(rawText)}</div>
            </div>
            <div class="practice-comparison-col">
                <div class="practice-col-header sample-col">
                    <i class="fa-solid fa-file-circle-check"></i> BÀI MẪU CHUẨN THAM KHẢO & DỊCH NGHĨA
                </div>
                <div class="sample-model-wrapper">
                    ${sampleContent}
                </div>
            </div>
        </div>

        <!-- Restart Button -->
        <div style="text-align: center; margin-top: 30px; margin-bottom: 20px;">
            <button class="btn btn-primary" id="btnRestartFullPractice" style="padding: 12px 36px; font-weight: 700; border-radius: 10px; font-size: 15px;">
                <i class="fa-solid fa-rotate-left"></i> Viết lại bài này
            </button>
        </div>
    `;

    // Attach restart listener
    const btnRestart = document.getElementById('btnRestartFullPractice');
    if (btnRestart) btnRestart.addEventListener('click', resetFullPracticeUI);

    // Send Google Form report to Teacher
    const now = new Date().toLocaleString('vi-VN');
    const excerpt = rawText.length > 200 ? rawText.substring(0, 200) + '...' : rawText;
    const offTopicStatusStr = isCompletelyOffTopic ? '⚠️ LẠC ĐỀ HOÀN TOÀN (0/4 ý)' : (isPartiallyOffTopic ? '⚠️ NGUY CƠ LẠC ĐỀ (1/4 ý)' : '✓ ĐÚNG ĐỀ');
    const payload = `[THỰC HÀNH VIẾT BÀI]: Học viên: ${currentStudentName || 'Học viên'} | Lớp: ${currentStudentClass || 'CB206'} | Dạng bài: ${letterTitle} | [CHỦ ĐỀ]: ${offTopicStatusStr} | Điểm 30%: ${convertedScore.toFixed(2)}/3.00 (Band ${overallBand.toFixed(1)}/10) | TF: ${tfConv.toFixed(2)}/0.75 | ORG: ${orgConv.toFixed(2)}/0.75 | VOC: ${vocConv.toFixed(2)}/0.75 | GRAM: ${gramConv.toFixed(2)}/0.75 | Lỗi: ${errors.length} | Số từ: ${wordCount} | Thời gian: ${timeSpentStr}/20:00 | Thời điểm: ${now} | Trích đoạn: "${excerpt}"`;

    reportResultToGoogleForm(payload);
}

function submitFullPractice(isAutoTimeUp = false) {
    const userText = fullPracticeInput ? fullPracticeInput.value.trim() : '';
    const wordCount = countWords(userText);

    if (!isAutoTimeUp) {
        let confirmMsg = 'BẠN CÓ CHẮC CHẮN MUỐN NỘP BÀI THỰC HÀNH KHÔNG?\n\n';
        if (wordCount < 120) {
            confirmMsg += `⚠️ Chú ý: Bài viết của bạn hiện có ${wordCount} từ (chưa đạt chuẩn tối thiểu 120 từ).\n\n`;
        } else {
            confirmMsg += `✓ Số từ đạt: ${wordCount} từ (đạt chuẩn độ dài VSTEP B1).\n\n`;
        }
        confirmMsg += 'Hệ thống sẽ chấm điểm chi tiết theo 4 tiêu chí VSTEP (30%), chỉ ra từng lỗi sai ngữ pháp, và hiển thị bài mẫu đối chiếu trực tiếp trên màn hình của bạn!';
        if (!confirm(confirmMsg)) return;
    }

    stopFullPracticeTimer();
    unlockNavigationAfterFullPractice();

    const timeSpentSeconds = Math.max(0, FULL_PRACTICE_TIME_LIMIT - fullPracticeTimeRemaining);
    const timeSpentStr = formatTimerString(timeSpentSeconds);

    if (fullPracticeWritingBox) fullPracticeWritingBox.classList.add('hidden');
    if (fullPracticeResultBox) {
        fullPracticeResultBox.classList.remove('hidden');
        renderFullPracticeEvaluationResult(userText, activeLetterTypeId, timeSpentStr);
        setTimeout(() => {
            fullPracticeResultBox.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }, 100);
    }
}

function submitFullPracticeEarly() {
    if (!isFullPracticeInProgress) return;
    submitFullPractice(false);
}

// --- Authentication & Student Profile Management ---
function initAuthSystem() {
    const savedName = localStorage.getItem('vstep_student_name');
    const savedClass = localStorage.getItem('vstep_student_class');

    if (savedName && savedClass && ALLOWED_CLASSES.includes(savedClass.trim().toUpperCase())) {
        currentStudentName = savedName.trim();
        currentStudentClass = savedClass.trim().toUpperCase();
        updateStudentProfileUI(currentStudentName, currentStudentClass);
        if (loginModalOverlay) loginModalOverlay.classList.add('hidden');
    } else {
        openLoginModal();
    }
}

function openLoginModal() {
    if (!loginModalOverlay) return;
    if (studentNameInput) studentNameInput.value = currentStudentName || '';
    if (studentClassSelect) studentClassSelect.value = currentStudentClass || '';
    if (loginErrorMsg) loginErrorMsg.classList.add('hidden');
    loginModalOverlay.classList.remove('hidden');
    setTimeout(() => {
        if (studentNameInput) studentNameInput.focus();
    }, 150);
}

function handleLoginSubmit() {
    const nameVal = studentNameInput ? studentNameInput.value.trim() : '';
    const classVal = studentClassSelect ? studentClassSelect.value.trim().toUpperCase() : '';

    if (!nameVal || nameVal.length < 2) {
        showLoginError('Vui lòng nhập đầy đủ Họ và tên (tối thiểu 2 ký tự).');
        if (studentNameInput) studentNameInput.focus();
        return;
    }

    if (!classVal || !ALLOWED_CLASSES.includes(classVal)) {
        showLoginError('Hệ thống chỉ tiếp nhận học viên thuộc các lớp: CB201, CB202, B209.');
        if (studentClassSelect) studentClassSelect.focus();
        return;
    }

    currentStudentName = nameVal;
    currentStudentClass = classVal;

    localStorage.setItem('vstep_student_name', currentStudentName);
    localStorage.setItem('vstep_student_class', currentStudentClass);
    localStorage.setItem('vstep_student_login_time', new Date().toISOString());

    updateStudentProfileUI(currentStudentName, currentStudentClass);

    if (loginErrorMsg) loginErrorMsg.classList.add('hidden');
    if (loginModalOverlay) loginModalOverlay.classList.add('hidden');
}

function showLoginError(msg) {
    if (loginErrorText) loginErrorText.textContent = msg;
    if (loginErrorMsg) loginErrorMsg.classList.remove('hidden');
}

function updateStudentProfileUI(name, cls) {
    if (studentNameDisplay) studentNameDisplay.textContent = name || 'Chưa đăng nhập';
    if (studentClassDisplay) studentClassDisplay.textContent = cls ? `Lớp: ${cls}` : 'Lớp: --';

    if (greetingStudentName) greetingStudentName.textContent = name || 'Bạn';
    if (greetingStudentClass) greetingStudentClass.textContent = cls ? `Lớp ${cls}` : 'Lớp --';
}

// --- Google Form Reporting System ---
function reportResultToGoogleForm(customPayload) {
    const name = currentStudentName || localStorage.getItem('vstep_student_name') || 'Học viên';
    const cls = currentStudentClass || localStorage.getItem('vstep_student_class') || 'Chưa rõ';

    let payload = customPayload;
    if (!payload) {
        const typeData = letterTypes.find(t => t.id === activeLetterTypeId);
        const letterTitle = typeData ? `${typeData.titleEn} (${typeData.titleVi})` : 'VSTEP Task 1';
        const score = scorePercentageVal ? scorePercentageVal.textContent : '0';
        const status = resultStatusVal ? resultStatusVal.textContent : '';
        const now = new Date().toLocaleString('vi-VN');
        const timeSpentSeconds = Math.max(0, RECITATION_TIME_LIMIT - recitationTimeRemaining);
        const timeSpentStr = formatTimerString(timeSpentSeconds);

        payload = `[HỌC VIÊN]: ${name} | [LỚP]: ${cls} | [DẠNG BÀI]: ${letterTitle} | [ĐIỂM]: ${score}% (${status}) | [THỜI GIAN LÀM]: ${timeSpentStr}/20:00 | [THỜI ĐIỂM NỘP]: ${now}`;
    }

    console.log("Submitting result report to Google Form:", payload);

    if (reportStatusBox) reportStatusBox.classList.remove('hidden');
    if (reportStatusIcon) {
        reportStatusIcon.className = 'fa-solid fa-spinner fa-spin report-status-icon';
    }
    if (reportStatusText) {
        reportStatusText.textContent = 'Đang gửi kết quả lên hệ thống của giáo viên...';
    }

    // Method 1: Fetch POST (no-cors)
    try {
        const formData = new URLSearchParams();
        formData.append(GOOGLE_FORM_ENTRY_ID, payload);

        fetch(GOOGLE_FORM_ACTION_URL, {
            method: 'POST',
            mode: 'no-cors',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: formData.toString()
        }).catch(err => console.log('Handled fetch status:', err));
    } catch (e) {
        console.log('Fetch exception:', e);
    }

    // Method 2: Hidden iframe fallback
    try {
        let iframe = document.getElementById('gform_hidden_iframe');
        if (!iframe) {
            iframe = document.createElement('iframe');
            iframe.id = 'gform_hidden_iframe';
            iframe.name = 'gform_hidden_iframe';
            iframe.style.display = 'none';
            document.body.appendChild(iframe);
        }

        let form = document.getElementById('gform_hidden_form');
        if (!form) {
            form = document.createElement('form');
            form.id = 'gform_hidden_form';
            form.action = GOOGLE_FORM_ACTION_URL;
            form.method = 'POST';
            form.target = 'gform_hidden_iframe';
            form.style.display = 'none';

            const input = document.createElement('input');
            input.type = 'hidden';
            input.name = GOOGLE_FORM_ENTRY_ID;
            input.id = 'gform_hidden_input';
            form.appendChild(input);
            document.body.appendChild(form);
        }

        const input = document.getElementById('gform_hidden_input');
        if (input) {
            input.value = payload;
            form.submit();
        }
    } catch (e) {
        console.log('Iframe submit error:', e);
    }

    setTimeout(() => {
        if (reportStatusIcon) {
            reportStatusIcon.className = 'fa-solid fa-circle-check report-status-icon';
        }
        if (reportStatusText) {
            reportStatusText.innerHTML = `Đã tự động báo cáo kết quả của học viên <strong>${name}</strong> (<strong>${cls}</strong>) lên hệ thống!`;
        }
    }, 700);
}

// Initialize application on DOM ready
document.addEventListener('DOMContentLoaded', () => {
    // Query DOM Elements
    letterNav = document.getElementById('letterNav');
    mainTitle = document.getElementById('mainTitle');
    welcomeScreen = document.getElementById('welcomeScreen');
    letterContent = document.getElementById('letterContent');
    themeToggle = document.getElementById('themeToggle');

    // Query Auth Elements
    loginModalOverlay = document.getElementById('loginModalOverlay');
    studentNameInput = document.getElementById('studentNameInput');
    studentClassSelect = document.getElementById('studentClassSelect');
    btnLoginSubmit = document.getElementById('btnLoginSubmit');
    loginErrorMsg = document.getElementById('loginErrorMsg');
    loginErrorText = document.getElementById('loginErrorText');

    studentProfileCard = document.getElementById('studentProfileCard');
    studentNameDisplay = document.getElementById('studentNameDisplay');
    studentClassDisplay = document.getElementById('studentClassDisplay');
    btnEditStudent = document.getElementById('btnEditStudent');

    questStudentGreeting = document.getElementById('questStudentGreeting');
    greetingStudentName = document.getElementById('greetingStudentName');
    greetingStudentClass = document.getElementById('greetingStudentClass');

    reportStatusBox = document.getElementById('reportStatusBox');
    reportStatusIcon = document.getElementById('reportStatusIcon');
    reportStatusText = document.getElementById('reportStatusText');
    btnResendReport = document.getElementById('btnResendReport');

    // Query Full Practice Elements
    fullPracticePanel = document.getElementById('fullPracticePanel');
    fullPracticeTimerBadge = document.getElementById('fullPracticeTimerBadge');
    fullPracticeCountdown = document.getElementById('fullPracticeCountdown');
    fullPracticeWordBadge = document.getElementById('fullPracticeWordBadge');
    fullPracticeWordCount = document.getElementById('fullPracticeWordCount');
    fullPracticePromptBox = document.getElementById('fullPracticePromptBox');
    fullPracticeWritingBox = document.getElementById('fullPracticeWritingBox');
    fullPracticeInput = document.getElementById('fullPracticeInput');
    btnSubmitFullPractice = document.getElementById('btnSubmitFullPractice');
    btnSubmitFullPracticeEarly = document.getElementById('btnSubmitFullPracticeEarly');
    fullPracticeResultBox = document.getElementById('fullPracticeResultBox');
    fullPracticeLockedBanner = document.getElementById('fullPracticeLockedBanner');

    // Query Recitation Elements
    btnSubmitRecitationEarly = document.getElementById('btnSubmitRecitationEarly');
    recitationTimerBadge = document.getElementById('recitationTimerBadge');
    recitationCountdown = document.getElementById('recitationCountdown');
    evaluationTimeSpent = document.getElementById('evaluationTimeSpent');
    timeSpentVal = document.getElementById('timeSpentVal');
    recitationInput = document.getElementById('recitationInput');
    btnPrevQuestion = document.getElementById('btnPrevQuestion');
    btnShowAnswer = document.getElementById('btnShowAnswer');
    btnCheckAnswer = document.getElementById('btnCheckAnswer');
    btnNextQuestion = document.getElementById('btnNextQuestion');
    currentQuestionNum = document.getElementById('currentQuestionNum');
    totalQuestionsNum = document.getElementById('totalQuestionsNum');
    progressBarFill = document.getElementById('progressBarFill');
    questionCueText = document.getElementById('questionCueText');
    recitationFeedback = document.getElementById('recitationFeedback');
    feedbackStatus = document.getElementById('feedbackStatus');
    userDiffResult = document.getElementById('userDiffResult');
    correctTextResult = document.getElementById('correctTextResult');
    questionHintBox = document.getElementById('questionHintBox');
    questionHintText = document.getElementById('questionHintText');

    // Query Evaluation Elements
    recitationQuizBox = document.getElementById('recitationQuizBox');
    recitationResultBox = document.getElementById('recitationResultBox');
    scorePercentageVal = document.getElementById('scorePercentageVal');
    resultStatusVal = document.getElementById('resultStatusVal');
    resultMessageVal = document.getElementById('resultMessageVal');
    btnRestartRecitation = document.getElementById('btnRestartRecitation');
    evaluationIcon = document.getElementById('evaluationIcon');

    // Render navigation
    renderNav();

    // Update global progress on load
    updateGlobalProgress();

    // Initialize Student Authentication
    initAuthSystem();

    // Auth Listeners
    if (btnLoginSubmit) btnLoginSubmit.addEventListener('click', handleLoginSubmit);
    if (btnEditStudent) btnEditStudent.addEventListener('click', openLoginModal);
    if (studentNameInput) {
        studentNameInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') handleLoginSubmit();
        });
    }
    if (btnResendReport) {
        btnResendReport.addEventListener('click', () => reportResultToGoogleForm());
    }

    // Reset progress button listener
    const btnResetProgress = document.getElementById('btnResetProgress');
    if (btnResetProgress) btnResetProgress.addEventListener('click', resetLearningProgress);

    // Handle Tabs
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            if (typeof stopSampleAudio === 'function') stopSampleAudio();
            const tabId = e.currentTarget.dataset.tab;

            // Block tab switching if recitation is currently in progress
            if (isRecitationInProgress && tabId !== 'writingPractice') {
                e.preventDefault();
                e.stopPropagation();
                showToastNotice('🔒 Đang trong quá trình trả bài! Bạn không thể chuyển sang tab khác cho đến khi hoàn thành hoặc nộp bài sớm.', 'fa-solid fa-lock');
                return false;
            }

            // Block tab switching if full practice is currently in progress
            if (isFullPracticeInProgress && tabId !== 'fullPractice') {
                e.preventDefault();
                e.stopPropagation();
                showToastNotice('🔒 Đang trong thời gian thực hành viết bài (20 phút)! Bạn không thể chuyển sang tab khác cho đến khi nộp bài.', 'fa-solid fa-lock');
                return false;
            }

            // Remove active class from all buttons and panels
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));

            // Add active class to clicked button
            e.currentTarget.classList.add('active');

            // Show corresponding panel
            const panel = document.getElementById(`${tabId}Panel`);
            if (panel) panel.classList.add('active');

            // Handle 20-minute timer and tab locking for TRẢ BÀI
            if (tabId === 'writingPractice') {
                const isResultShown = recitationResultBox && !recitationResultBox.classList.contains('hidden');
                if (!isResultShown) {
                    lockNavigationDuringRecitation();
                    startRecitationTimer();
                }
            } else {
                stopRecitationTimer();
            }

            // Handle 20-minute timer and tab locking for THỰC HÀNH
            if (tabId === 'fullPractice') {
                const isFullResultShown = fullPracticeResultBox && !fullPracticeResultBox.classList.contains('hidden');
                if (!isFullResultShown) {
                    lockNavigationDuringFullPractice();
                    startFullPracticeTimer();
                }
            } else {
                stopFullPracticeTimer();
            }
        });
    });

    // Recitation Button Listeners
    if (btnPrevQuestion) btnPrevQuestion.addEventListener('click', prevRecitationQuestion);
    if (btnShowAnswer) btnShowAnswer.addEventListener('click', showRecitationAnswer);
    if (btnCheckAnswer) btnCheckAnswer.addEventListener('click', checkRecitationAnswer);
    if (btnNextQuestion) btnNextQuestion.addEventListener('click', nextRecitationQuestion);
    if (btnRestartRecitation) btnRestartRecitation.addEventListener('click', resetRecitationUI);
    if (btnSubmitRecitationEarly) btnSubmitRecitationEarly.addEventListener('click', submitRecitationEarly);

    // Full Practice Listeners
    if (fullPracticeInput) {
        fullPracticeInput.addEventListener('input', updateFullPracticeWordCount);
    }
    if (btnSubmitFullPractice) {
        btnSubmitFullPractice.addEventListener('click', () => submitFullPractice(false));
    }
    if (btnSubmitFullPracticeEarly) {
        btnSubmitFullPracticeEarly.addEventListener('click', submitFullPracticeEarly);
    }

    // Theme Toggle
    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            isDarkMode = !isDarkMode;
            if (isDarkMode) {
                document.documentElement.setAttribute('data-theme', 'dark');
                themeToggle.innerHTML = '<i class="fa-solid fa-sun"></i>';
            } else {
                document.documentElement.removeAttribute('data-theme');
                themeToggle.innerHTML = '<i class="fa-solid fa-moon"></i>';
            }
        });
    }

    // Initialize Anti-Copy / Anti-Paste Protection
    initAntiCopyProtection();
});

// --- Anti Copy/Paste Protection System ---
function initAntiCopyProtection() {
    // Warn before leaving page during active recitation or full practice
    window.addEventListener('beforeunload', (e) => {
        if (isRecitationInProgress || isFullPracticeInProgress) {
            e.preventDefault();
            e.returnValue = 'Bạn đang trong quá trình làm bài! Nếu rời khỏi trang, nội dung bài làm sẽ bị hủy.';
            return e.returnValue;
        }
    });

    // Check if element is inside allowed practice zones (THỰC HÀNH & BÀI LUYỆN TẬP THÊM)
    function isAllowedPasteTarget(el) {
        if (!el) return false;
        // Direct ID check
        if (el.id === 'fullPracticeInput' || el.id === 'extraWritingArea' || el.id === 'extraWritingInput') {
            return true;
        }
        // Class check
        if (el.classList && (el.classList.contains('extra-textarea') || el.classList.contains('practice-textarea'))) {
            return true;
        }
        // Ancestor container check
        if (el.closest) {
            const panel = el.closest('#fullPracticePanel, #extraPracticePanel, .full-practice-writing-box, .extra-practice-container');
            if (panel && (el.tagName === 'TEXTAREA' || (el.tagName === 'INPUT' && !['button', 'submit', 'radio', 'checkbox'].includes(el.type)))) {
                return true;
            }
        }
        return false;
    }

    // Block Copy Event (Allowed inside THỰC HÀNH & BÀI LUYỆN TẬP THÊM textareas)
    document.addEventListener('copy', (e) => {
        if (isAllowedPasteTarget(e.target) || isAllowedPasteTarget(document.activeElement)) {
            return;
        }
        e.preventDefault();
        showAntiCopyToast('Chức năng Sao chép (Copy) đã bị khóa trên hệ thống!');
    });

    // Block Cut Event (Allowed inside THỰC HÀNH & BÀI LUYỆN TẬP THÊM textareas)
    document.addEventListener('cut', (e) => {
        if (isAllowedPasteTarget(e.target) || isAllowedPasteTarget(document.activeElement)) {
            return;
        }
        e.preventDefault();
        showAntiCopyToast('Chức năng Cắt (Cut) đã bị khóa trên hệ thống!');
    });

    // Block Paste Event (Allowed inside THỰC HÀNH & BÀI LUYỆN TẬP THÊM textareas)
    document.addEventListener('paste', (e) => {
        if (isAllowedPasteTarget(e.target) || isAllowedPasteTarget(document.activeElement)) {
            const target = isAllowedPasteTarget(e.target) ? e.target : document.activeElement;
            setTimeout(() => {
                if (target) {
                    target.dispatchEvent(new Event('input', { bubbles: true }));
                    target.dispatchEvent(new Event('change', { bubbles: true }));
                }
            }, 30);
            return;
        }
        e.preventDefault();
        showAntiCopyToast('Không được phép Dán (Paste)! Vui lòng tự gõ phím để học thuộc và nhớ bài lâu hơn.');
    });

    // Block Context Menu (Right Click) - Allowed inside practice textareas for pasting/editing
    document.addEventListener('contextmenu', (e) => {
        if (isAllowedPasteTarget(e.target) || isAllowedPasteTarget(document.activeElement)) {
            return;
        }
        e.preventDefault();
        showAntiCopyToast('Chuột phải đã bị vô hiệu hóa để bảo vệ nội dung học tập!');
    });

    // Block Drag and Drop text
    document.addEventListener('dragstart', (e) => {
        if (isAllowedPasteTarget(e.target) || isAllowedPasteTarget(document.activeElement)) {
            return;
        }
        e.preventDefault();
    });
    document.addEventListener('drop', (e) => {
        if (isAllowedPasteTarget(e.target) || isAllowedPasteTarget(document.activeElement)) {
            const target = isAllowedPasteTarget(e.target) ? e.target : document.activeElement;
            setTimeout(() => {
                if (target) {
                    target.dispatchEvent(new Event('input', { bubbles: true }));
                }
            }, 30);
            return;
        }
        e.preventDefault();
    });

    // Block Keyboard Shortcuts (Ctrl+C, Ctrl+V, Ctrl+X, Ctrl+U, Cmd+C, Cmd+V, Cmd+X, Cmd+U)
    // Permitted: Ctrl/Cmd+V, Ctrl/Cmd+C, Ctrl/Cmd+X inside THỰC HÀNH & BÀI LUYỆN TẬP THÊM
    document.addEventListener('keydown', (e) => {
        const isCtrlOrCmd = e.ctrlKey || e.metaKey;
        const key = e.key ? e.key.toLowerCase() : '';

        if (isCtrlOrCmd && ['c', 'v', 'x', 'u', 's'].includes(key)) {
            if (['c', 'v', 'x'].includes(key) && (isAllowedPasteTarget(e.target) || isAllowedPasteTarget(document.activeElement))) {
                return;
            }
            e.preventDefault();
            e.stopPropagation();
            if (['c', 'x'].includes(key)) {
                showAntiCopyToast('Chức năng Sao chép (Copy) đã bị vô hiệu hóa!');
            } else if (key === 'v') {
                showAntiCopyToast('Chức năng Dán (Paste) đã bị vô hiệu hóa! Vui lòng tự gõ bài viết.');
            }
            return false;
        }
    }, true);
}

// ===================================================
// --- INTERACTIVE SAMPLE WRITING CONTROLLER ---
// ===================================================
let currentSampleUtterance = null;
let currentSampleSpeechRate = 1.0;

function switchSampleView(viewId, btnEl) {
    const parent = btnEl.closest('.content-block');
    if (!parent) return;

    if (typeof stopSampleAudio === 'function') stopSampleAudio();

    // Toggle Tab Buttons
    parent.querySelectorAll('.sample-view-tab-btn').forEach(b => b.classList.remove('active'));
    btnEl.classList.add('active');

    // Toggle View Panels
    const panels = parent.querySelectorAll('.sample-view-content');
    panels.forEach(p => {
        if (p.id === viewId) {
            p.classList.add('active');
            p.style.display = 'block';
        } else {
            p.classList.remove('active');
            p.style.display = 'none';
        }
    });
}

function toggleSampleHighlight(type) {
    const container = document.getElementById('sampleViewAnnotated');
    if (!container) return;

    const eventTarget = window.event ? window.event.currentTarget : null;

    if (type === 'connectors') {
        const isHidden = container.classList.toggle('hide-connectors');
        if (eventTarget) {
            eventTarget.classList.toggle('dimmed', isHidden);
            const icon = eventTarget.querySelector('i');
            if (icon) icon.className = isHidden ? 'fa-solid fa-xmark' : 'fa-solid fa-check';
        }
    } else if (type === 'structures') {
        const isHidden = container.classList.toggle('hide-structures');
        if (eventTarget) {
            eventTarget.classList.toggle('dimmed', isHidden);
            const icon = eventTarget.querySelector('i');
            if (icon) icon.className = isHidden ? 'fa-solid fa-xmark' : 'fa-solid fa-check';
        }
    } else if (type === 'vocabs') {
        const isHidden = container.classList.toggle('hide-vocabs');
        if (eventTarget) {
            eventTarget.classList.toggle('dimmed', isHidden);
            const icon = eventTarget.querySelector('i');
            if (icon) icon.className = isHidden ? 'fa-solid fa-xmark' : 'fa-solid fa-check';
        }
    }
}

function speakText(text) {
    if (!('speechSynthesis' in window)) {
        if (typeof showToastNotice === 'function') {
            showToastNotice('Trình duyệt không hỗ trợ Web Speech API!', 'fa-solid fa-circle-exclamation');
        } else {
            alert('Trình duyệt không hỗ trợ Web Speech API!');
        }
        return;
    }

    stopSampleAudio();

    const cleanText = text.replace(/<[^>]*>/g, '').trim();
    if (!cleanText) return;

    const utterance = new SpeechSynthesisUtterance(cleanText);
    utterance.lang = 'en-US';
    utterance.rate = currentSampleSpeechRate || 1.0;

    const voices = window.speechSynthesis.getVoices();
    const enVoice = voices.find(v => v.lang.startsWith('en') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Samantha') || v.name.includes('Daniel') || v.name.includes('US') || v.name.includes('GB'))) || voices.find(v => v.lang.startsWith('en'));
    if (enVoice) utterance.voice = enVoice;

    currentSampleUtterance = utterance;
    window.speechSynthesis.speak(utterance);
}

function playCurrentSampleLetter() {
    if (!('speechSynthesis' in window)) {
        if (typeof showToastNotice === 'function') {
            showToastNotice('Trình duyệt không hỗ trợ Web Speech API!', 'fa-solid fa-circle-exclamation');
        } else {
            alert('Trình duyệt không hỗ trợ Web Speech API!');
        }
        return;
    }

    stopSampleAudio();

    const cleanBox = document.querySelector('#sampleViewClean .sample-letter-box');
    let fullText = '';
    if (cleanBox) {
        fullText = cleanBox.innerText;
    } else {
        const typeData = (typeof letterTypes !== 'undefined') ? letterTypes.find(t => t.id === activeLetterTypeId) : null;
        if (typeData && typeData.sampleWriting) {
            const tmp = document.createElement('div');
            tmp.innerHTML = typeData.sampleWriting;
            const cb = tmp.querySelector('.sample-letter-box');
            if (cb) fullText = cb.innerText;
        }
    }

    if (!fullText) return;

    const utterance = new SpeechSynthesisUtterance(fullText);
    utterance.lang = 'en-US';
    utterance.rate = currentSampleSpeechRate || 1.0;

    const voices = window.speechSynthesis.getVoices();
    const enVoice = voices.find(v => v.lang.startsWith('en') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Samantha') || v.name.includes('Daniel') || v.name.includes('US') || v.name.includes('GB'))) || voices.find(v => v.lang.startsWith('en'));
    if (enVoice) utterance.voice = enVoice;

    const btnPlay = document.getElementById('btnPlaySampleAudio');
    const btnStop = document.getElementById('btnStopSampleAudio');
    const audioStatus = document.getElementById('sampleAudioStatus');

    utterance.onstart = () => {
        if (btnPlay) btnPlay.style.display = 'none';
        if (btnStop) btnStop.style.display = 'inline-flex';
        if (audioStatus) audioStatus.style.display = 'inline-flex';
    };

    utterance.onend = () => {
        if (btnPlay) btnPlay.style.display = 'inline-flex';
        if (btnStop) btnStop.style.display = 'none';
        if (audioStatus) audioStatus.style.display = 'none';
        currentSampleUtterance = null;
    };

    utterance.onerror = () => {
        if (btnPlay) btnPlay.style.display = 'inline-flex';
        if (btnStop) btnStop.style.display = 'none';
        if (audioStatus) audioStatus.style.display = 'none';
        currentSampleUtterance = null;
    };

    currentSampleUtterance = utterance;
    window.speechSynthesis.speak(utterance);
}

function stopSampleAudio() {
    if ('speechSynthesis' in window && window.speechSynthesis.speaking) {
        window.speechSynthesis.cancel();
    }
    const btnPlay = document.getElementById('btnPlaySampleAudio');
    const btnStop = document.getElementById('btnStopSampleAudio');
    const audioStatus = document.getElementById('sampleAudioStatus');
    if (btnPlay) btnPlay.style.display = 'inline-flex';
    if (btnStop) btnStop.style.display = 'none';
    if (audioStatus) audioStatus.style.display = 'none';
    currentSampleUtterance = null;
}

function updateSampleAudioSpeed(speed) {
    currentSampleSpeechRate = parseFloat(speed) || 1.0;
    if (currentSampleUtterance && window.speechSynthesis.speaking) {
        playCurrentSampleLetter();
    }
}

// Expose globally for HTML onclick handlers
window.switchSampleView = switchSampleView;
window.toggleSampleHighlight = toggleSampleHighlight;
window.speakText = speakText;
window.playCurrentSampleLetter = playCurrentSampleLetter;
window.stopSampleAudio = stopSampleAudio;
window.updateSampleAudioSpeed = updateSampleAudioSpeed;
