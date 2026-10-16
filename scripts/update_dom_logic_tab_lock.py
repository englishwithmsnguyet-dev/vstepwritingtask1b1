# -*- coding: utf-8 -*-
with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/dom_logic_full.js", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update Recitation State variables
target_state = """// Recitation State
let activeLetterTypeId = 'advice';
let currentQuestionIndex = 0;
let activeQuestions = [];
let questionScores = [];
let questionHintsUsed = [];"""

replacement_state = """// Recitation State & Tab Locking
let activeLetterTypeId = 'advice';
let currentQuestionIndex = 0;
let activeQuestions = [];
let questionScores = [];
let questionHintsUsed = [];
let isRecitationInProgress = false;
let btnSubmitRecitationEarly = null;"""

assert target_state in code, "target_state not found"
code = code.replace(target_state, replacement_state, 1)

# 2. Add Toast Notification & Lock Helpers after handleRecitationTimeUp
target_timer_func = """    alert('⏰ ĐÃ HẾT THỜI GIAN 20 PHÚT LÀM BÀI!\\nHệ thống tự động nộp bài và hiển thị kết quả đánh giá trả bài của bạn.');
    showEvaluationResult();
}"""

replacement_helpers = """    alert('⏰ ĐÃ HẾT THỜI GIAN 20 PHÚT LÀM BÀI!\\nHệ thống tự động nộp bài và hiển thị kết quả đánh giá trả bài của bạn.');
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

// Lock / Unlock Navigation during Recitation
function lockNavigationDuringRecitation() {
    isRecitationInProgress = true;

    // Lock all tab buttons except writingPractice
    document.querySelectorAll('.tab-btn').forEach(btn => {
        if (btn.dataset.tab !== 'writingPractice') {
            btn.classList.add('tab-locked');
            btn.setAttribute('title', 'Đã bị khóa trong lúc trả bài');
        } else {
            btn.classList.remove('tab-locked');
            btn.removeAttribute('title');
        }
    });

    // Lock all sidebar navigation items
    document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.add('nav-locked');
        item.setAttribute('title', 'Đã bị khóa trong lúc trả bài');
    });

    if (btnEditStudent) {
        btnEditStudent.classList.add('btn-locked');
    }
    const btnResetProgress = document.getElementById('btnResetProgress');
    if (btnResetProgress) {
        btnResetProgress.classList.add('btn-locked');
    }

    const banner = document.getElementById('recitationLockedBanner');
    if (banner) {
        banner.classList.remove('hidden');
    }
}

function unlockNavigationAfterRecitation() {
    isRecitationInProgress = false;

    // Unlock all tab buttons
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('tab-locked');
        btn.removeAttribute('title');
    });

    // Unlock all sidebar navigation items
    document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.remove('nav-locked');
        item.removeAttribute('title');
    });

    if (btnEditStudent) {
        btnEditStudent.classList.remove('btn-locked');
    }
    const btnResetProgress = document.getElementById('btnResetProgress');
    if (btnResetProgress) {
        btnResetProgress.classList.remove('btn-locked');
    }

    const banner = document.getElementById('recitationLockedBanner');
    if (banner) {
        banner.classList.add('hidden');
    }
}

function submitRecitationEarly() {
    if (!isRecitationInProgress) return;

    const confirmEarly = confirm(
        '⚠️ BẠN CÓ CHẮC CHẮN MUỐN NỘP BÀI SỚM KHÔNG?\\n\\n' +
        '• Các câu hỏi chưa làm sẽ được tính 0 điểm.\\n' +
        '• Hệ thống sẽ tự động tổng kết điểm và MỞ KHÓA lại các tab cho bạn.\\n\\n' +
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
}"""

assert target_timer_func in code, "target_timer_func not found"
code = code.replace(target_timer_func, replacement_helpers, 1)

# 3. Update resetLearningProgress to check isRecitationInProgress
target_reset_prog = """function resetLearningProgress() {
    if (confirm('Bạn có chắc chắn muốn làm mới toàn bộ tiến độ học tập không?')) {"""

replacement_reset_prog = """function resetLearningProgress() {
    if (isRecitationInProgress) {
        showToastNotice('🔒 Đang trong quá trình trả bài! Không thể làm mới tiến độ lúc này.', 'fa-solid fa-lock');
        return;
    }
    if (confirm('Bạn có chắc chắn muốn làm mới toàn bộ tiến độ học tập không?')) {"""

assert target_reset_prog in code, "target_reset_prog not found"
code = code.replace(target_reset_prog, replacement_reset_prog, 1)

# 4. Update resetRecitationUI to lock/unlock appropriately
target_reset_ui = """    // Reset Recitation 20-minute Timer
    resetRecitationTimer();
    const practicePanel = document.getElementById('writingPracticePanel');
    if (practicePanel && practicePanel.classList.contains('active')) {
        startRecitationTimer();
    }"""

replacement_reset_ui = """    // Reset Recitation 20-minute Timer
    resetRecitationTimer();
    const practicePanel = document.getElementById('writingPracticePanel');
    if (practicePanel && practicePanel.classList.contains('active')) {
        lockNavigationDuringRecitation();
        startRecitationTimer();
    } else {
        unlockNavigationAfterRecitation();
    }"""

assert target_reset_ui in code, "target_reset_ui not found"
code = code.replace(target_reset_ui, replacement_reset_ui, 1)

# 5. Update showEvaluationResult to call unlockNavigationAfterRecitation
target_show_eval = """    // Stop 20-minute countdown timer and compute time spent
    stopRecitationTimer();
    const timeSpentSeconds = Math.max(0, RECITATION_TIME_LIMIT - recitationTimeRemaining);"""

replacement_show_eval = """    // Stop 20-minute countdown timer and compute time spent
    stopRecitationTimer();
    unlockNavigationAfterRecitation();
    const timeSpentSeconds = Math.max(0, RECITATION_TIME_LIMIT - recitationTimeRemaining);"""

assert target_show_eval in code, "target_show_eval not found"
code = code.replace(target_show_eval, replacement_show_eval, 1)

# 6. Update showWelcomeScreen to check isRecitationInProgress
target_welcome = """// Show Welcome Screen
function showWelcomeScreen() {
    activeLetterTypeId = null;"""

replacement_welcome = """// Show Welcome Screen
function showWelcomeScreen() {
    if (isRecitationInProgress) {
        showToastNotice('🔒 Đang trong quá trình trả bài! Bạn không thể rời khỏi bài cho đến khi hoàn thành hoặc nộp bài sớm.', 'fa-solid fa-lock');
        return;
    }
    activeLetterTypeId = null;"""

assert target_welcome in code, "target_welcome not found"
code = code.replace(target_welcome, replacement_welcome, 1)

# 7. Update selectLetterType to check isRecitationInProgress
target_select = """// Select a Letter Type
function selectLetterType(id) {
    activeLetterTypeId = id;"""

replacement_select = """// Select a Letter Type
function selectLetterType(id) {
    if (isRecitationInProgress) {
        showToastNotice('🔒 Đang trong quá trình trả bài! Bạn không thể rời khỏi bài cho đến khi hoàn thành hoặc nộp bài sớm.', 'fa-solid fa-lock');
        return;
    }
    activeLetterTypeId = id;"""

assert target_select in code, "target_select not found"
code = code.replace(target_select, replacement_select, 1)

# 8. Update tab click handler
target_tabs = """    // Handle Tabs
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            // Remove active class from all buttons and panels
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));

            // Add active class to clicked button
            e.currentTarget.classList.add('active');

            // Show corresponding panel
            const tabId = e.currentTarget.dataset.tab;
            const panel = document.getElementById(`${tabId}Panel`);
            if (panel) panel.classList.add('active');

            // Handle 20-minute timer based on active tab
            if (tabId === 'writingPractice') {
                startRecitationTimer();
            } else {
                stopRecitationTimer();
            }
        });
    });"""

replacement_tabs = """    // Handle Tabs
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const tabId = e.currentTarget.dataset.tab;

            // Block tab switching if recitation is currently in progress
            if (isRecitationInProgress && tabId !== 'writingPractice') {
                e.preventDefault();
                e.stopPropagation();
                showToastNotice('🔒 Đang trong quá trình trả bài! Bạn không thể chuyển sang tab khác cho đến khi hoàn thành hoặc nộp bài sớm.', 'fa-solid fa-lock');
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

            // Handle 20-minute timer and tab locking based on active tab
            if (tabId === 'writingPractice') {
                const isResultShown = recitationResultBox && !recitationResultBox.classList.contains('hidden');
                if (!isResultShown) {
                    lockNavigationDuringRecitation();
                    startRecitationTimer();
                }
            } else {
                stopRecitationTimer();
            }
        });
    });"""

assert target_tabs in code, "target_tabs not found"
code = code.replace(target_tabs, replacement_tabs, 1)

# 9. Query btnSubmitRecitationEarly & add listeners in DOMContentLoaded
target_recit_query = """    // Query Recitation Elements
    recitationTimerBadge = document.getElementById('recitationTimerBadge');"""

replacement_recit_query = """    // Query Recitation Elements
    btnSubmitRecitationEarly = document.getElementById('btnSubmitRecitationEarly');
    recitationTimerBadge = document.getElementById('recitationTimerBadge');"""

assert target_recit_query in code, "target_recit_query not found"
code = code.replace(target_recit_query, replacement_recit_query, 1)

target_recit_listeners = """    // Recitation Button Listeners
    if (btnPrevQuestion) btnPrevQuestion.addEventListener('click', prevRecitationQuestion);
    if (btnShowAnswer) btnShowAnswer.addEventListener('click', showRecitationAnswer);
    if (btnCheckAnswer) btnCheckAnswer.addEventListener('click', checkRecitationAnswer);
    if (btnNextQuestion) btnNextQuestion.addEventListener('click', nextRecitationQuestion);
    if (btnRestartRecitation) btnRestartRecitation.addEventListener('click', resetRecitationUI);"""

replacement_recit_listeners = """    // Recitation Button Listeners
    if (btnPrevQuestion) btnPrevQuestion.addEventListener('click', prevRecitationQuestion);
    if (btnShowAnswer) btnShowAnswer.addEventListener('click', showRecitationAnswer);
    if (btnCheckAnswer) btnCheckAnswer.addEventListener('click', checkRecitationAnswer);
    if (btnNextQuestion) btnNextQuestion.addEventListener('click', nextRecitationQuestion);
    if (btnRestartRecitation) btnRestartRecitation.addEventListener('click', resetRecitationUI);
    if (btnSubmitRecitationEarly) btnSubmitRecitationEarly.addEventListener('click', submitRecitationEarly);"""

assert target_recit_listeners in code, "target_recit_listeners not found"
code = code.replace(target_recit_listeners, replacement_recit_listeners, 1)

# 10. Clean up initAntiCopyProtection to avoid duplicate showAntiCopyToast, and add beforeunload
target_anticopy = """// --- Anti Copy/Paste Protection System ---
function initAntiCopyProtection() {
    let toastTimeout = null;

    function showAntiCopyToast(message) {
        let toast = document.getElementById('antiCopyToast');
        if (!toast) {
            toast = document.createElement('div');
            toast.id = 'antiCopyToast';
            toast.className = 'anti-copy-toast';
            toast.innerHTML = `<i class="fa-solid fa-ban"></i> <span id="antiCopyToastMsg"></span>`;
            document.body.appendChild(toast);
        }

        const msgSpan = document.getElementById('antiCopyToastMsg');
        if (msgSpan) {
            msgSpan.textContent = message || 'Không được phép Sao chép hoặc Dán (Copy/Paste)! Vui lòng tự gõ phím để rèn luyện.';
        }

        toast.classList.add('show');

        if (toastTimeout) clearTimeout(toastTimeout);
        toastTimeout = setTimeout(() => {
            toast.classList.remove('show');
        }, 2500);
    }"""

replacement_anticopy = """// --- Anti Copy/Paste Protection System ---
function initAntiCopyProtection() {
    // Warn before leaving page during active recitation
    window.addEventListener('beforeunload', (e) => {
        if (isRecitationInProgress) {
            e.preventDefault();
            e.returnValue = 'Bạn đang trong quá trình trả bài! Nếu rời khỏi trang, tiến độ trả bài sẽ bị hủy.';
            return e.returnValue;
        }
    });"""

assert target_anticopy in code, "target_anticopy not found"
code = code.replace(target_anticopy, replacement_anticopy, 1)

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/dom_logic_full.js", "w", encoding="utf-8") as f:
    f.write(code)

print("Successfully updated scratch/dom_logic_full.js!")
