# -*- coding: utf-8 -*-
css_error_table = """
/* Detailed Error Breakdown Table */
.extra-error-table-wrapper {
    background: var(--bg-card);
    border: 1.5px solid rgba(239, 68, 68, 0.3);
    border-radius: 14px;
    padding: 20px 24px;
    box-shadow: 0 4px 14px rgba(239, 68, 68, 0.08);
}

.error-table-title {
    font-size: 15.5px;
    font-weight: 700;
    color: #dc2626;
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 16px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

[data-theme="dark"] .error-table-title {
    color: #f87171;
}

.table-responsive {
    width: 100%;
    overflow-x: auto;
}

.error-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13.5px;
    text-align: left;
}

.error-table th {
    background-color: var(--bg-main);
    color: var(--text-main);
    font-weight: 700;
    padding: 12px 14px;
    border-bottom: 2px solid var(--border-color);
    text-transform: uppercase;
    font-size: 12px;
    letter-spacing: 0.5px;
}

.error-table td {
    padding: 14px 14px;
    border-bottom: 1px solid var(--border-color);
    vertical-align: middle;
}

.error-table tbody tr:hover {
    background-color: rgba(79, 70, 229, 0.03);
}

.err-badge-type {
    display: inline-block;
    background: rgba(79, 70, 229, 0.1);
    color: var(--primary-color);
    padding: 3px 8px;
    border-radius: 6px;
    font-weight: 600;
    font-size: 12px;
    border: 1px solid rgba(79, 70, 229, 0.2);
}

.err-text-wrong {
    color: #dc2626;
    background: rgba(239, 68, 68, 0.08);
    padding: 3px 8px;
    border-radius: 4px;
    font-family: monospace;
    font-weight: 600;
    display: inline-block;
    text-decoration: line-through;
}

[data-theme="dark"] .err-text-wrong {
    color: #fca5a5;
    background: rgba(239, 68, 68, 0.2);
}

.err-text-correct {
    color: #059669;
    background: rgba(16, 185, 129, 0.1);
    padding: 3px 8px;
    border-radius: 4px;
    font-family: monospace;
    font-weight: 700;
    display: inline-block;
    border: 1px solid rgba(16, 185, 129, 0.25);
}

[data-theme="dark"] .err-text-correct {
    color: #34d399;
    background: rgba(16, 185, 129, 0.2);
}
"""

style_path = "/Users/nguyetpham/Desktop/WEBSITE/writing-letters-b1level/style.css"
with open(style_path, "r", encoding="utf-8") as f:
    cur_css = f.read()

if "Detailed Error Breakdown Table" not in cur_css:
    cur_css = cur_css.strip() + "\n\n" + css_error_table
    with open(style_path, "w", encoding="utf-8") as f:
        f.write(cur_css)
    print("Added error table styles to style.css!")
else:
    print("Error table styles already exist.")
