# -*- coding: utf-8 -*-
"""
Integrates interactive sample writing controller into scratch/dom_logic_full.js
and appends styling to style.css.
"""

# 1. Update scratch/dom_logic_full.js
dom_path = "/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/dom_logic_full.js"
with open(dom_path, "r", encoding="utf-8") as f:
    dom_code = f.read()

# Make sure stopSampleAudio() is called in selectLetterType
if "stopSampleAudio();" not in dom_code:
    dom_code = dom_code.replace(
        "function selectLetterType(id) {",
        "function selectLetterType(id) {\n    if (typeof stopSampleAudio === 'function') stopSampleAudio();"
    )

# Make sure stopSampleAudio() is called when clicking tab buttons
if "if (typeof stopSampleAudio === 'function') stopSampleAudio();" not in dom_code.split("btn.addEventListener('click', (e) => {")[1][:200]:
    dom_code = dom_code.replace(
        "btn.addEventListener('click', (e) => {\n            const tabId = e.currentTarget.dataset.tab;",
        "btn.addEventListener('click', (e) => {\n            if (typeof stopSampleAudio === 'function') stopSampleAudio();\n            const tabId = e.currentTarget.dataset.tab;"
    )

# Add Sample Writing Controller code if not already present
sample_controller_js = """
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
"""

if "function switchSampleView" not in dom_code:
    dom_code += "\n\n" + sample_controller_js.strip() + "\n"

with open(dom_path, "w", encoding="utf-8") as f:
    f.write(dom_code)

print("Updated scratch/dom_logic_full.js successfully!")

# 2. Append enhanced styles to style.css
css_path = "/Users/nguyetpham/Desktop/WEBSITE/writing-letters-b1level/style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

enhanced_css = """
/* ===================================================
   ENHANCED SAMPLE WRITING (BÀI MẪU NÂNG CAO V44.0)
   =================================================== */

/* Header Action & Metrics Bar */
.sample-toolbar-card {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 14px;
    padding: 16px 20px;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03);
    margin-top: 15px;
}

.sample-metrics-group {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 10px;
}

.sample-metric-chip {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 600;
    background: var(--bg-main);
    color: var(--text-main);
    border: 1px solid var(--border-color);
}

.sample-metric-chip.accent-words {
    background: #ecfdf5;
    color: #065f46;
    border-color: #a7f3d0;
}
[data-theme="dark"] .sample-metric-chip.accent-words {
    background: rgba(16, 185, 129, 0.15);
    color: #6ee7b7;
    border-color: rgba(16, 185, 129, 0.3);
}

.sample-metric-chip.accent-tone {
    background: #eff6ff;
    color: #1e40af;
    border-color: #bfdbfe;
}
[data-theme="dark"] .sample-metric-chip.accent-tone {
    background: rgba(59, 130, 246, 0.15);
    color: #93c5fd;
    border-color: rgba(59, 130, 246, 0.3);
}

.sample-metric-chip.accent-band {
    background: #fef3c7;
    color: #92400e;
    border-color: #fde68a;
}
[data-theme="dark"] .sample-metric-chip.accent-band {
    background: rgba(245, 158, 11, 0.15);
    color: #fcd34d;
    border-color: rgba(245, 158, 11, 0.3);
}

/* Audio Player Controls */
.sample-audio-controls {
    display: flex;
    align-items: center;
    gap: 8px;
    background: var(--bg-main);
    padding: 5px 8px;
    border-radius: 12px;
    border: 1px solid var(--border-color);
}

.btn-sample-audio {
    border: none;
    outline: none;
    cursor: pointer;
    padding: 7px 14px;
    border-radius: 8px;
    font-size: 13px;
    font-weight: 600;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    transition: all 0.2s ease;
    background: var(--primary-color);
    color: #ffffff;
}

.btn-sample-audio:hover {
    filter: brightness(1.1);
    transform: translateY(-1px);
}

.btn-sample-audio.btn-stop {
    background: #ef4444;
}

.sample-speed-select {
    padding: 6px 8px;
    border-radius: 8px;
    border: 1px solid var(--border-color);
    background: var(--bg-card);
    color: var(--text-main);
    font-size: 12px;
    font-weight: 600;
    cursor: pointer;
}

.sample-audio-status {
    font-size: 12px;
    font-weight: 600;
    color: var(--primary-color);
    margin-left: 4px;
    display: inline-flex;
    align-items: center;
    gap: 5px;
}

/* View Mode Nav (Tabs) */
.sample-view-nav {
    display: flex;
    gap: 10px;
    border-bottom: 2px solid var(--border-color);
    padding-bottom: 12px;
    overflow-x: auto;
}

.sample-view-tab-btn {
    border: none;
    outline: none;
    background: var(--bg-main);
    color: var(--text-muted);
    font-size: 14.5px;
    font-weight: 600;
    padding: 10px 18px;
    border-radius: 10px;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    transition: all 0.2s ease;
    white-space: nowrap;
    border: 1px solid transparent;
}

.sample-view-tab-btn:hover {
    color: var(--text-main);
    background: var(--bg-card);
}

.sample-view-tab-btn.active {
    background: var(--primary-color);
    color: #ffffff;
    box-shadow: 0 4px 12px rgba(220, 38, 38, 0.25);
}

/* Highlighter Filter Bar in Annotated View */
.sample-filter-bar {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    background: rgba(243, 244, 246, 0.7);
    padding: 12px 16px;
    border-radius: 12px;
    margin-bottom: 16px;
    border: 1px solid var(--border-color);
}
[data-theme="dark"] .sample-filter-bar {
    background: rgba(30, 41, 59, 0.7);
}

.sample-filter-title {
    font-size: 13px;
    font-weight: 700;
    color: var(--text-main);
    display: inline-flex;
    align-items: center;
    gap: 6px;
}

.sample-filter-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}

.filter-pill {
    font-size: 12px;
    font-weight: 600;
    padding: 5px 12px;
    border-radius: 6px;
    cursor: pointer;
    user-select: none;
    transition: all 0.2s;
    border: 1px solid transparent;
    display: inline-flex;
    align-items: center;
    gap: 5px;
}

.filter-pill.pill-connector {
    background: #fef3c7;
    color: #92400e;
    border-color: #fde68a;
}
.filter-pill.pill-connector.dimmed {
    opacity: 0.4;
    background: var(--bg-card);
    color: var(--text-muted);
}

.filter-pill.pill-structure {
    background: #d1fae5;
    color: #065f46;
    border-color: #a7f3d0;
}
.filter-pill.pill-structure.dimmed {
    opacity: 0.4;
    background: var(--bg-card);
    color: var(--text-muted);
}

.filter-pill.pill-vocab {
    background: #e0e7ff;
    color: #3730a3;
    border-color: #c7d2fe;
}
.filter-pill.pill-vocab.dimmed {
    opacity: 0.4;
    background: var(--bg-card);
    color: var(--text-muted);
}

/* Annotated Highlight Styles inside Text */
.sample-hl-connector {
    background-color: #fef08a;
    color: #854d0e;
    font-weight: 700;
    padding: 2px 6px;
    border-radius: 4px;
    border-bottom: 2px solid #eab308;
    transition: all 0.2s;
}
[data-theme="dark"] .sample-hl-connector {
    background-color: rgba(234, 179, 8, 0.25);
    color: #fde047;
    border-bottom-color: #eab308;
}

.sample-hl-structure {
    background-color: #d1fae5;
    color: #065f46;
    font-weight: 600;
    padding: 2px 6px;
    border-radius: 4px;
    border-bottom: 2px solid #10b981;
    transition: all 0.2s;
}
[data-theme="dark"] .sample-hl-structure {
    background-color: rgba(16, 185, 129, 0.25);
    color: #6ee7b7;
    border-bottom-color: #10b981;
}

.sample-hl-vocab {
    background-color: #e0e7ff;
    color: #3730a3;
    font-weight: 600;
    padding: 2px 6px;
    border-radius: 4px;
    border-bottom: 2px solid #6366f1;
    transition: all 0.2s;
}
[data-theme="dark"] .sample-hl-vocab {
    background-color: rgba(99, 102, 241, 0.25);
    color: #a5b4fc;
    border-bottom-color: #6366f1;
}

/* Dimmed state when toggled off */
.hide-connectors .sample-hl-connector {
    background-color: transparent !important;
    color: inherit !important;
    font-weight: inherit !important;
    border-bottom: none !important;
    padding: 0 !important;
}
.hide-structures .sample-hl-structure {
    background-color: transparent !important;
    color: inherit !important;
    font-weight: inherit !important;
    border-bottom: none !important;
    padding: 0 !important;
}
.hide-vocabs .sample-hl-vocab {
    background-color: transparent !important;
    color: inherit !important;
    font-weight: inherit !important;
    border-bottom: none !important;
    padding: 0 !important;
}

/* Annotated Cards Layout */
.sample-section-card {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    margin-bottom: 16px;
    overflow: hidden;
    transition: transform 0.2s, box-shadow 0.2s;
}

.sample-section-card:hover {
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.04);
}

.sample-section-header {
    background: rgba(243, 244, 246, 0.6);
    padding: 10px 18px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid var(--border-color);
}
[data-theme="dark"] .sample-section-header {
    background: rgba(30, 41, 59, 0.6);
}

.sample-section-badge {
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    color: var(--primary-color);
}

.sample-section-btn-audio {
    background: none;
    border: none;
    color: var(--text-muted);
    font-size: 13px;
    cursor: pointer;
    padding: 4px 8px;
    border-radius: 6px;
    transition: color 0.2s;
}
.sample-section-btn-audio:hover {
    color: var(--primary-color);
}

.sample-section-body {
    padding: 18px 20px;
    font-size: 15.5px;
    line-height: 1.85;
    color: var(--text-main);
}

.sample-section-body p {
    margin: 0 0 10px 0;
}

.sample-section-note {
    margin-top: 10px;
    padding: 8px 12px;
    border-radius: 8px;
    background: #f8fafc;
    border-left: 3px solid #3b82f6;
    font-size: 13px;
    color: #475569;
    font-style: italic;
    display: flex;
    align-items: flex-start;
    gap: 8px;
}
[data-theme="dark"] .sample-section-note {
    background: rgba(30, 41, 59, 0.5);
    border-left-color: #60a5fa;
    color: #94a3b8;
}

/* Body Section 4 Points Container */
.sample-body-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 14px;
}

.sample-point-card {
    background: var(--bg-main);
    border: 1px solid var(--border-color);
    border-radius: 10px;
    padding: 14px 16px;
    border-left: 4px solid var(--primary-color);
}

.sample-point-tag {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 12px;
    font-weight: 700;
    color: var(--primary-color);
    margin-bottom: 6px;
    text-transform: uppercase;
}

.sample-point-text {
    font-size: 15px;
    line-height: 1.8;
}

/* Bilingual View */
.bilingual-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    padding: 14px 18px;
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    margin-bottom: 12px;
    align-items: start;
}

@media (max-width: 768px) {
    .bilingual-row {
        grid-template-columns: 1fr;
        gap: 8px;
    }
}

.bilingual-col-en {
    font-size: 15px;
    line-height: 1.8;
    color: var(--text-main);
    border-right: 1px dashed var(--border-color);
    padding-right: 16px;
}
@media (max-width: 768px) {
    .bilingual-col-en {
        border-right: none;
        border-bottom: 1px dashed var(--border-color);
        padding-right: 0;
        padding-bottom: 10px;
    }
}

.bilingual-col-vi {
    font-size: 14.5px;
    line-height: 1.8;
    color: #4b5563;
    font-style: italic;
}
[data-theme="dark"] .bilingual-col-vi {
    color: #9ca3af;
}

.bilingual-header-tag {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 6px;
    font-size: 11.5px;
    font-weight: 700;
    text-transform: uppercase;
    color: var(--primary-color);
}

/* Examiner's Takeaways Card */
.examiner-card {
    background: linear-gradient(135deg, rgba(254, 242, 242, 0.6) 0%, rgba(255, 255, 255, 0.9) 100%);
    border: 1.5px solid rgba(239, 68, 68, 0.25);
    border-radius: 14px;
    padding: 22px 24px;
    margin-top: 24px;
    box-shadow: 0 8px 24px rgba(220, 38, 38, 0.05);
}
[data-theme="dark"] .examiner-card {
    background: linear-gradient(135deg, rgba(45, 15, 15, 0.4) 0%, rgba(20, 24, 33, 0.9) 100%);
    border-color: rgba(239, 68, 68, 0.35);
}

.examiner-header {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 16px;
    font-weight: 700;
    color: var(--primary-color);
    margin-bottom: 16px;
    padding-bottom: 10px;
    border-bottom: 1px dashed rgba(239, 68, 68, 0.25);
}

.examiner-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
}
@media (max-width: 768px) {
    .examiner-grid {
        grid-template-columns: 1fr;
    }
}

.examiner-item {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 10px;
    padding: 14px 16px;
}

.examiner-item-title {
    font-size: 13.5px;
    font-weight: 700;
    color: var(--text-main);
    display: flex;
    align-items: center;
    gap: 6px;
    margin-bottom: 6px;
}

.examiner-item-desc {
    font-size: 13px;
    line-height: 1.6;
    color: var(--text-muted);
    margin: 0;
}

/* Clean Letter Box Paragraphs */
.sample-letter-box p {
    margin: 0 0 16px 0;
    text-indent: 24px;
}
.sample-letter-box p:last-of-type {
    margin-bottom: 16px;
}
.sample-letter-box strong {
    display: block;
    margin-bottom: 14px;
}
.sample-letter-box strong:last-child {
    margin-top: 14px;
    margin-bottom: 0;
}
"""

if "ENHANCED SAMPLE WRITING (BÀI MẪU NÂNG CAO V44.0)" not in css_content:
    with open(css_path, "a", encoding="utf-8") as f:
        f.write("\n\n" + enhanced_css.strip() + "\n")
    print("Appended enhanced sample writing CSS to style.css!")
else:
    print("CSS already present in style.css.")
