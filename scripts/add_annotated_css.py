# -*- coding: utf-8 -*-
css_additions = """
/* --- Inline Annotated Essay & Correction Styles --- */
.annotated-essay-card {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 16px;
    padding: 24px;
    margin-top: 24px;
    box-shadow: var(--shadow-sm);
    transition: all 0.3s ease;
}

.annotated-essay-header {
    font-family: var(--font-heading);
    font-size: 16px;
    font-weight: 700;
    color: var(--primary-color);
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 18px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

[data-theme="dark"] .annotated-essay-header {
    color: var(--primary-light);
}

.annotated-essay-body {
    background-color: var(--bg-main);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    padding: 20px 24px;
    font-family: var(--font-body);
    font-size: 15.5px;
    line-height: 2.1;
    color: var(--text-main);
}

.annotated-para {
    margin-bottom: 14px;
}

.annotated-para:last-child {
    margin-bottom: 0;
}

.annotated-box {
    display: inline-flex;
    align-items: baseline;
    gap: 4px;
    margin: 0 3px;
    padding: 2px 6px;
    border-radius: 6px;
    background: rgba(239, 68, 68, 0.04);
    border: 1px dashed rgba(239, 68, 68, 0.3);
}

.annotated-wrong {
    color: #dc2626;
    background: rgba(239, 68, 68, 0.12);
    padding: 1px 6px;
    border-radius: 4px;
    font-weight: 600;
    text-decoration: line-through;
}

[data-theme="dark"] .annotated-wrong {
    color: #fca5a5;
    background: rgba(239, 68, 68, 0.25);
}

.annotated-correct {
    color: #059669;
    background: rgba(16, 185, 129, 0.12);
    padding: 1px 7px;
    border-radius: 4px;
    font-weight: 700;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 4px;
    border: 1px solid rgba(16, 185, 129, 0.3);
}

[data-theme="dark"] .annotated-correct {
    color: #34d399;
    background: rgba(16, 185, 129, 0.25);
}
"""

style_css_path = "/Users/nguyetpham/Desktop/WEBSITE/writing-letters-b1level/style.css"
with open(style_css_path, "r", encoding="utf-8") as f:
    current_css = f.read()

if ".annotated-essay-card" not in current_css:
    current_css += "\n" + css_additions.strip() + "\n"
    with open(style_css_path, "w", encoding="utf-8") as f:
        f.write(current_css)
    print("Appended annotated essay styles to style.css!")
else:
    print("annotated essay styles already present.")
