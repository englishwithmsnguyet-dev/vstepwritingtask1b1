css_extra_practice = """
/* ==========================================================================
   BÀI LUYỆN TẬP THÊM (EXTRA PRACTICE) STYLES
   ========================================================================== */
.tab-btn.extra-practice-tab {
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.08), rgba(5, 150, 105, 0.15));
    border-color: rgba(16, 185, 129, 0.35);
    color: #047857;
}

[data-theme="dark"] .tab-btn.extra-practice-tab {
    background: rgba(6, 78, 59, 0.35);
    border-color: rgba(16, 185, 129, 0.4);
    color: #34d399;
}

.tab-btn.extra-practice-tab.active {
    background: linear-gradient(135deg, #10b981, #059669) !important;
    color: #ffffff !important;
    border-color: #059669 !important;
    box-shadow: 0 4px 12px rgba(16, 185, 129, 0.35);
}

.extra-practice-container {
    display: flex;
    flex-direction: column;
    gap: 24px;
}

/* Prompt Card */
.extra-prompt-box {
    background: var(--bg-card);
    border: 1.5px solid rgba(79, 70, 229, 0.2);
    border-radius: 16px;
    padding: 24px 28px;
    box-shadow: var(--shadow-sm);
    position: relative;
    overflow: hidden;
}

.extra-prompt-box::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 6px;
    height: 100%;
    background: linear-gradient(to bottom, var(--primary-color), var(--secondary-color));
}

.extra-prompt-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    margin-bottom: 14px;
}

.extra-prompt-title {
    font-size: 17px;
    font-weight: 700;
    color: var(--primary-color);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.extra-b1-badge {
    background: rgba(79, 70, 229, 0.1);
    color: var(--primary-color);
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 700;
    border: 1px solid rgba(79, 70, 229, 0.25);
}

.extra-prompt-body {
    font-size: 15.5px;
    line-height: 1.8;
    color: var(--text-main);
    background: var(--bg-main);
    padding: 18px 22px;
    border-radius: 12px;
    border: 1px solid var(--border-color);
}

.extra-prompt-body ul {
    margin: 10px 0 10px 24px;
    padding: 0;
}

.extra-prompt-body ul li {
    margin-bottom: 6px;
    font-weight: 600;
    color: var(--accent-red);
}

.extra-prompt-footer-note {
    margin-top: 10px;
    font-size: 13.5px;
    color: var(--text-muted);
    font-style: italic;
}

/* Hints Toggle & Box */
.extra-hints-card {
    background: var(--bg-card);
    border: 1px dashed var(--accent-yellow, #eab308);
    border-radius: 14px;
    padding: 16px 20px;
    background-color: rgba(234, 179, 8, 0.04);
}

.btn-toggle-hints {
    width: 100%;
    background: transparent;
    border: none;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-family: var(--font-heading);
    font-size: 15px;
    font-weight: 700;
    color: #b45309;
    padding: 6px 0;
}

[data-theme="dark"] .btn-toggle-hints {
    color: #fbbf24;
}

.btn-toggle-hints i.chevron-icon {
    transition: transform 0.3s ease;
}

.btn-toggle-hints.expanded i.chevron-icon {
    transform: rotate(180deg);
}

.hints-content {
    margin-top: 16px;
    display: flex;
    flex-direction: column;
    gap: 16px;
    animation: fadeIn 0.3s ease;
}

.hint-section-block {
    background: var(--bg-main);
    border: 1px solid var(--border-color);
    border-radius: 10px;
    padding: 14px 18px;
}

.hint-section-title {
    font-weight: 700;
    font-size: 14.5px;
    color: var(--primary-color);
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    gap: 6px;
}

.hint-items-list {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.hint-item-card {
    background: var(--bg-card);
    padding: 10px 14px;
    border-radius: 8px;
    border-left: 3px solid var(--secondary-color);
    font-size: 14px;
    line-height: 1.6;
}

.hint-item-en {
    font-weight: 600;
    color: var(--text-main);
}

.hint-item-vi {
    color: var(--text-muted);
    font-size: 13px;
    margin-bottom: 4px;
}

.hint-item-reason {
    color: #047857;
    font-size: 13px;
    margin-top: 2px;
}

[data-theme="dark"] .hint-item-reason {
    color: #34d399;
}

/* Editor Section */
.extra-editor-card {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 16px;
    padding: 22px 24px;
    box-shadow: var(--shadow-sm);
    display: flex;
    flex-direction: column;
    gap: 16px;
}

.extra-editor-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.extra-editor-title {
    font-size: 16px;
    font-weight: 700;
    color: var(--text-main);
    display: flex;
    align-items: center;
    gap: 8px;
}

.extra-word-badge {
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 700;
    background: rgba(239, 68, 68, 0.1);
    color: #ef4444;
    border: 1px solid rgba(239, 68, 68, 0.3);
    transition: all 0.3s ease;
}

.extra-word-badge.valid {
    background: rgba(16, 185, 129, 0.12);
    color: #059669;
    border-color: rgba(16, 185, 129, 0.4);
}

.extra-textarea {
    width: 100%;
    min-height: 280px;
    padding: 20px;
    border: 1.5px solid var(--border-color);
    border-radius: 12px;
    font-family: var(--font-body);
    font-size: 16px;
    line-height: 1.8;
    background-color: var(--bg-main);
    color: var(--text-main);
    resize: vertical;
    outline: none;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

.extra-textarea:focus {
    border-color: var(--primary-color);
    box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.15);
}

.extra-editor-actions {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    gap: 12px;
}

/* Diagnostic & Result Section */
.extra-result-card {
    background: var(--bg-card);
    border: 1.5px solid rgba(16, 185, 129, 0.3);
    border-radius: 16px;
    padding: 28px;
    box-shadow: var(--shadow-md);
    display: flex;
    flex-direction: column;
    gap: 22px;
    animation: slideUp 0.4s ease;
}

.extra-score-banner {
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 16px;
    background: linear-gradient(135deg, rgba(79, 70, 229, 0.08), rgba(16, 185, 129, 0.1));
    padding: 20px 24px;
    border-radius: 14px;
    border: 1px solid rgba(79, 70, 229, 0.2);
}

.score-main-group {
    display: flex;
    align-items: center;
    gap: 16px;
}

.score-circle-badge {
    width: 65px;
    height: 65px;
    border-radius: 50%;
    background: var(--primary-color);
    color: #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    font-weight: 800;
    box-shadow: 0 4px 12px rgba(79, 70, 229, 0.4);
}

.score-text-info h4 {
    margin: 0 0 4px 0;
    font-size: 18px;
    color: var(--text-main);
}

.score-text-info p {
    margin: 0;
    font-size: 13.5px;
    color: var(--text-muted);
}

.criteria-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 14px;
}

.criterion-card {
    background: var(--bg-main);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    padding: 16px;
    display: flex;
    flex-direction: column;
    gap: 6px;
}

.criterion-name {
    font-size: 13px;
    font-weight: 700;
    text-transform: uppercase;
    color: var(--primary-color);
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.criterion-score {
    font-size: 14px;
    font-weight: 800;
    color: var(--secondary-color);
}

.criterion-desc {
    font-size: 13px;
    color: var(--text-muted);
    line-height: 1.5;
}

.extra-feedback-box {
    background: var(--bg-main);
    border-radius: 12px;
    padding: 18px 20px;
    border: 1px solid var(--border-color);
}

.feedback-title {
    font-size: 15px;
    font-weight: 700;
    margin-bottom: 12px;
    color: var(--text-main);
    display: flex;
    align-items: center;
    gap: 8px;
}

.feedback-items-list {
    margin: 0;
    padding-left: 20px;
    font-size: 14px;
    line-height: 1.7;
    color: var(--text-main);
}

.feedback-items-list li {
    margin-bottom: 8px;
}

.feedback-items-list li.strength {
    color: #059669;
}

.feedback-items-list li.correction {
    color: #dc2626;
}

[data-theme="dark"] .feedback-items-list li.correction {
    color: #f87171;
}

/* Sample Model Unlocked */
.extra-model-wrapper {
    margin-top: 10px;
    border-top: 1px dashed var(--border-color);
    padding-top: 20px;
}

.extra-model-title {
    font-size: 17px;
    font-weight: 700;
    color: #059669;
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 14px;
}

.extra-model-letter {
    font-family: "Georgia", "Times New Roman", serif;
    background: #fdfbf7;
    color: #2d2621;
    border: 1px solid #e5dfd3;
    border-radius: 12px;
    padding: 30px 35px;
    line-height: 1.9;
    font-size: 15.5px;
}

[data-theme="dark"] .extra-model-letter {
    background: #1a202c;
    color: #e2e8f0;
    border-color: #2d3748;
}

.extra-model-trans {
    background: var(--bg-main);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    padding: 20px 24px;
    margin-top: 14px;
    font-style: italic;
    font-size: 14.5px;
    line-height: 1.8;
    color: var(--text-muted);
}
"""

style_css_path = "/Users/nguyetpham/Desktop/WEBSITE/writing-letters-b1level/style.css"
with open(style_css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

if "BÀI LUYỆN TẬP THÊM (EXTRA PRACTICE) STYLES" not in css_content:
    css_content = css_content.strip() + "\n\n" + css_extra_practice
    with open(style_css_path, "w", encoding="utf-8") as f:
        f.write(css_content)
    print("Added Extra Practice CSS to style.css!")
else:
    print("CSS already present.")
