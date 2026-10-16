# -*- coding: utf-8 -*-
with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/dom_logic_full.js", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Add Full Practice DOM element variables & state
target_timer_vars = """// Timer DOM Elements & State (20-minute Recitation Timer)
let recitationTimerBadge;
let recitationCountdown;
let timeSpentVal;
let evaluationTimeSpent;
let recitationTimerInterval = null;
const RECITATION_TIME_LIMIT = 20 * 60; // 20 minutes = 1200 seconds
let recitationTimeRemaining = RECITATION_TIME_LIMIT;
let isRecitationTimerRunning = false;"""

replacement_timer_vars = """// Timer DOM Elements & State (20-minute Recitation Timer)
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
let isFullPracticeTimerRunning = false;"""

assert target_timer_vars in code, "target_timer_vars not found"
code = code.replace(target_timer_vars, replacement_timer_vars, 1)

# 2. Add Full Practice Timer functions & unified locking helpers
target_lock_funcs = """// Lock / Unlock Navigation during Recitation
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
}"""

replacement_lock_funcs = """// Unified Navigation Locking System for TRẢ BÀI & THỰC HÀNH
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
    alert('⏰ ĐÃ HẾT THỜI GIAN 20 PHÚT LÀM BÀI!\\nHệ thống tự động nộp bài thực hành viết thư của bạn và mở khóa các tab để bạn đối chiếu với bài mẫu.');
    submitFullPractice(true);
}"""

assert target_lock_funcs in code, "target_lock_funcs not found"
code = code.replace(target_lock_funcs, replacement_lock_funcs, 1)

# 3. Add helper word counter & escapeHtml
target_diff_words = """// Word-by-word diff algorithm using LCS"""
helpers_code = """function countWords(str) {
    if (!str) return 0;
    const words = str.trim().split(/\\s+/).filter(w => w.length > 0);
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

// Word-by-word diff algorithm using LCS"""

assert target_diff_words in code, "target_diff_words not found"
code = code.replace(target_diff_words, helpers_code, 1)

# 4. Add Full Practice Logic (render, word count, submit, reset)
target_auth_system = """// --- Authentication & Student Profile Management ---"""
full_practice_logic = """// --- Full Practice (THỰC HÀNH) System ---
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

function submitFullPractice(isAutoTimeUp = false) {
    const userText = fullPracticeInput ? fullPracticeInput.value.trim() : '';
    const wordCount = countWords(userText);

    if (!isAutoTimeUp) {
        let confirmMsg = 'BẠN CÓ CHẮC CHẮN MUỐN NỘP BÀI THỰC HÀNH KHÔNG?\\n\\n';
        if (wordCount < 120) {
            confirmMsg += `⚠️ Chú ý: Bài viết của bạn hiện có ${wordCount} từ (chưa đạt tối thiểu 120 từ).\\n\\n`;
        } else {
            confirmMsg += `✓ Số từ đạt: ${wordCount} từ (đạt chuẩn độ dài).\\n\\n`;
        }
        confirmMsg += 'Hệ thống sẽ tổng kết bài làm, gửi báo cáo và mở khóa bài mẫu chuẩn để bạn đối chiếu!';
        if (!confirm(confirmMsg)) return;
    }

    stopFullPracticeTimer();
    unlockNavigationAfterFullPractice();

    const timeSpentSeconds = Math.max(0, FULL_PRACTICE_TIME_LIMIT - fullPracticeTimeRemaining);
    const timeSpentStr = formatTimerString(timeSpentSeconds);

    if (fullPracticeWritingBox) fullPracticeWritingBox.classList.add('hidden');
    if (fullPracticeResultBox) {
        fullPracticeResultBox.classList.remove('hidden');

        const typeData = letterTypes.find(t => t.id === activeLetterTypeId);
        const letterTitle = typeData ? `${typeData.titleEn} (${typeData.titleVi})` : 'VSTEP Task 1';

        const tempDiv = document.createElement('div');
        tempDiv.innerHTML = typeData ? typeData.sampleWriting : '';
        const sampleContent = tempDiv.querySelector('.content-block') ? tempDiv.querySelector('.content-block').innerHTML : (typeData ? typeData.sampleWriting : '');

        const isWordPass = wordCount >= 120;
        const wordBadgeHtml = isWordPass 
            ? `<span class="practice-stat-badge badge-success"><i class="fa-solid fa-circle-check"></i> Đạt chuẩn (≥ 120 từ)</span>`
            : `<span class="practice-stat-badge badge-warning"><i class="fa-solid fa-triangle-exclamation"></i> Chưa đủ (cần ≥ 120 từ)</span>`;

        fullPracticeResultBox.innerHTML = `
            <div class="practice-summary-card">
                <div class="practice-summary-header">
                    <i class="fa-solid fa-award" style="color: #2563eb;"></i> KẾT QUẢ THỰC HÀNH VIẾT THƯ HOÀN CHỈNH
                </div>
                <div class="practice-stats-grid">
                    <div class="practice-stat-box">
                        <div class="practice-stat-label">Học viên</div>
                        <div class="practice-stat-value" style="font-size: 18px;">${currentStudentName || 'Học viên'}</div>
                        <span class="practice-stat-badge" style="background: var(--bg-card); color: var(--text-muted);">${currentStudentClass || 'CB206'}</span>
                    </div>
                    <div class="practice-stat-box">
                        <div class="practice-stat-label">Độ dài bài viết</div>
                        <div class="practice-stat-value">${wordCount} từ</div>
                        ${wordBadgeHtml}
                    </div>
                    <div class="practice-stat-box">
                        <div class="practice-stat-label">Thời gian làm bài</div>
                        <div class="practice-stat-value">${timeSpentStr}</div>
                        <span class="practice-stat-badge" style="background: var(--bg-card); color: var(--text-muted);">Giới hạn: 20:00</span>
                    </div>
                </div>
                <div class="recitation-report-status" style="margin-top: 10px;">
                    <i class="fa-solid fa-circle-check report-status-icon"></i>
                    <span>Đã ghi nhận bài làm của học viên và tự động báo cáo lên hệ thống của giáo viên!</span>
                </div>
            </div>

            <!-- Side-by-Side Comparison -->
            <div class="practice-comparison-section">
                <div class="practice-comparison-col">
                    <div class="practice-col-header student-col">
                        <i class="fa-solid fa-user-pen"></i> BÀI VIẾT CỦA BẠN (${wordCount} TỪ)
                    </div>
                    <div class="practice-paper-view">${userText ? escapeHtml(userText) : '<em>(Không có nội dung bài viết)</em>'}</div>
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

            <div style="text-align: center; margin-top: 25px;">
                <button class="btn btn-primary" id="btnRestartFullPractice" style="padding: 12px 32px; font-weight: 700; border-radius: 10px;">
                    <i class="fa-solid fa-rotate-left"></i> Viết lại bài này
                </button>
            </div>
        `;

        const btnRestart = document.getElementById('btnRestartFullPractice');
        if (btnRestart) {
            btnRestart.addEventListener('click', resetFullPracticeUI);
        }
    }

    // Report to Google Form
    const now = new Date().toLocaleString('vi-VN');
    const typeData = letterTypes.find(t => t.id === activeLetterTypeId);
    const letterTitle = typeData ? `${typeData.titleEn} (${typeData.titleVi})` : 'VSTEP Task 1';
    const excerpt = userText.length > 250 ? userText.substring(0, 250) + '...' : userText;
    const payload = `[THỰC HÀNH VIẾT BÀI]: Học viên: ${currentStudentName || 'Học viên'} | Lớp: ${currentStudentClass || 'CB206'} | Dạng bài: ${letterTitle} | Số từ: ${wordCount} từ (${wordCount >= 120 ? 'ĐẠT ĐỘ DÀI' : 'CHƯA ĐỦ ĐỘ DÀI'}) | Thời gian: ${timeSpentStr}/20:00 | Thời điểm: ${now} | Trích đoạn: "${excerpt}"`;

    reportResultToGoogleForm(payload);
}

function submitFullPracticeEarly() {
    if (!isFullPracticeInProgress) return;
    submitFullPractice(false);
}

// --- Authentication & Student Profile Management ---"""

assert target_auth_system in code, "target_auth_system not found"
code = code.replace(target_auth_system, full_practice_logic, 1)

# 5. Update selectLetterType, showWelcomeScreen, resetLearningProgress to check isFullPracticeInProgress
target_welcome = """function showWelcomeScreen() {
    if (isRecitationInProgress) {
        showToastNotice('🔒 Đang trong quá trình trả bài! Bạn không thể rời khỏi bài cho đến khi hoàn thành hoặc nộp bài sớm.', 'fa-solid fa-lock');
        return;
    }"""

replacement_welcome = """function showWelcomeScreen() {
    if (isRecitationInProgress) {
        showToastNotice('🔒 Đang trong quá trình trả bài! Bạn không thể rời khỏi bài cho đến khi hoàn thành hoặc nộp bài sớm.', 'fa-solid fa-lock');
        return;
    }
    if (isFullPracticeInProgress) {
        showToastNotice('🔒 Đang trong thời gian thực hành viết bài (20 phút)! Bạn không thể rời khỏi bài cho đến khi nộp bài.', 'fa-solid fa-lock');
        return;
    }"""

assert target_welcome in code, "target_welcome not found"
code = code.replace(target_welcome, replacement_welcome, 1)

target_select = """function selectLetterType(id) {
    if (isRecitationInProgress) {
        showToastNotice('🔒 Đang trong quá trình trả bài! Bạn không thể rời khỏi bài cho đến khi hoàn thành hoặc nộp bài sớm.', 'fa-solid fa-lock');
        return;
    }"""

replacement_select = """function selectLetterType(id) {
    if (isRecitationInProgress) {
        showToastNotice('🔒 Đang trong quá trình trả bài! Bạn không thể rời khỏi bài cho đến khi hoàn thành hoặc nộp bài sớm.', 'fa-solid fa-lock');
        return;
    }
    if (isFullPracticeInProgress) {
        showToastNotice('🔒 Đang trong thời gian thực hành viết bài (20 phút)! Bạn không thể rời khỏi bài cho đến khi nộp bài.', 'fa-solid fa-lock');
        return;
    }"""

assert target_select in code, "target_select not found"
code = code.replace(target_select, replacement_select, 1)

target_reset_prog = """function resetLearningProgress() {
    if (isRecitationInProgress) {
        showToastNotice('🔒 Đang trong quá trình trả bài! Không thể làm mới tiến độ lúc này.', 'fa-solid fa-lock');
        return;
    }"""

replacement_reset_prog = """function resetLearningProgress() {
    if (isRecitationInProgress || isFullPracticeInProgress) {
        showToastNotice('🔒 Đang trong thời gian làm bài kiểm tra / thực hành! Không thể làm mới tiến độ lúc này.', 'fa-solid fa-lock');
        return;
    }"""

assert target_reset_prog in code, "target_reset_prog not found"
code = code.replace(target_reset_prog, replacement_reset_prog, 1)

# 6. Call renderFullPracticePanel(id) in selectLetterType
target_call_render = """    if (sampleWritingPanel) sampleWritingPanel.innerHTML = typeData.sampleWriting;

    // Reset recitation for this type
    resetRecitationUI();"""

replacement_call_render = """    if (sampleWritingPanel) sampleWritingPanel.innerHTML = typeData.sampleWriting;

    // Render Full Practice Panel
    renderFullPracticePanel(id);

    // Reset recitation for this type
    resetRecitationUI();"""

assert target_call_render in code, "target_call_render not found"
code = code.replace(target_call_render, replacement_call_render, 1)

# 7. Update tab click handler to handle fullPractice
target_tabs = """            // Block tab switching if recitation is currently in progress
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
            }"""

replacement_tabs = """            // Block tab switching if recitation is currently in progress
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
            }"""

assert target_tabs in code, "target_tabs not found"
code = code.replace(target_tabs, replacement_tabs, 1)

# 8. Query Full Practice DOM elements & attach listeners in DOMContentLoaded
target_dom_queries = """    // Query Recitation Elements
    btnSubmitRecitationEarly = document.getElementById('btnSubmitRecitationEarly');"""

replacement_dom_queries = """    // Query Full Practice Elements
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
    btnSubmitRecitationEarly = document.getElementById('btnSubmitRecitationEarly');"""

assert target_dom_queries in code, "target_dom_queries not found"
code = code.replace(target_dom_queries, replacement_dom_queries, 1)

target_listeners = """    if (btnSubmitRecitationEarly) btnSubmitRecitationEarly.addEventListener('click', submitRecitationEarly);"""

replacement_listeners = """    if (btnSubmitRecitationEarly) btnSubmitRecitationEarly.addEventListener('click', submitRecitationEarly);

    // Full Practice Listeners
    if (fullPracticeInput) {
        fullPracticeInput.addEventListener('input', updateFullPracticeWordCount);
    }
    if (btnSubmitFullPractice) {
        btnSubmitFullPractice.addEventListener('click', () => submitFullPractice(false));
    }
    if (btnSubmitFullPracticeEarly) {
        btnSubmitFullPracticeEarly.addEventListener('click', submitFullPracticeEarly);
    }"""

assert target_listeners in code, "target_listeners not found"
code = code.replace(target_listeners, replacement_listeners, 1)

# 9. Update beforeunload to check isFullPracticeInProgress
target_beforeunload = """    // Warn before leaving page during active recitation
    window.addEventListener('beforeunload', (e) => {
        if (isRecitationInProgress) {
            e.preventDefault();
            e.returnValue = 'Bạn đang trong quá trình trả bài! Nếu rời khỏi trang, tiến độ trả bài sẽ bị hủy.';
            return e.returnValue;
        }
    });"""

replacement_beforeunload = """    // Warn before leaving page during active recitation or full practice
    window.addEventListener('beforeunload', (e) => {
        if (isRecitationInProgress || isFullPracticeInProgress) {
            e.preventDefault();
            e.returnValue = 'Bạn đang trong quá trình làm bài! Nếu rời khỏi trang, nội dung bài làm sẽ bị hủy.';
            return e.returnValue;
        }
    });"""

assert target_beforeunload in code, "target_beforeunload not found"
code = code.replace(target_beforeunload, replacement_beforeunload, 1)

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/dom_logic_full.js", "w", encoding="utf-8") as f:
    f.write(code)

print("Successfully updated dom_logic_full.js with Full Practice logic!")
