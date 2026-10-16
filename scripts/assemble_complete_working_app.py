# -*- coding: utf-8 -*-
import json

# Read pure_extra_logic.js
with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/pure_extra_logic.js", "r", encoding="utf-8") as f:
    extra_logic_js = f.read()

# Read recitation_questions.js
with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/recitation_questions.js", "r", encoding="utf-8") as f:
    recitation_questions_js = f.read()

# Read reconstruct_app.py to get letter_types array
with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "r", encoding="utf-8") as f:
    rec_code = f.read()

idx_types = rec_code.find("letter_types = [")
idx_types_end = rec_code.find("js_array_code = ")

if idx_types != -1 and idx_types_end != -1:
    exec(rec_code[idx_types:idx_types_end])
    letter_types_json = "const letterTypes = " + json.dumps(letter_types, ensure_ascii=False, indent=4) + ";\n"
else:
    raise Exception("Could not extract letter_types")

# Read dom_logic_full.js
with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/dom_logic_full.js", "r", encoding="utf-8") as f:
    dom_logic = f.read()

# Ensure renderExtraPracticePanel is called in selectLetterType
if "renderExtraPracticePanel(id);" not in dom_logic:
    dom_logic = dom_logic.replace(
        "if (sampleWritingPanel) sampleWritingPanel.innerHTML = typeData.sampleWriting;",
        "if (sampleWritingPanel) sampleWritingPanel.innerHTML = typeData.sampleWriting;\n\n    // Render Extra Practice\n    renderExtraPracticePanel(id);"
    )

# Ensure auth logic has password STUDYHARD, classes CB206, CB210, GV, and student lists + Teacher PTMN
auth_block = """
// Auth & Student Information
const ALLOWED_CLASSES = ['CB206', 'CB210', 'CB211', 'GV'];
const MANDATORY_PASSWORD = 'STUDYHARD';

const STUDENTS_BY_CLASS = {
    'CB206': [
        'Nguyễn Thị Vân Anh',
        'Nguyễn Thị Hồng Duyên',
        'Nguyễn Thị Thúy Hồng',
        'Trương Ngọc Nhi',
        'Nguyễn Phạm Như Quỳnh',
        'Trần Lê Quỳnh',
        'Thị Mỹ Tâm',
        'Ông Lê Thành',
        'Trần Nguyễn Thanh Thảo',
        'Phan Nhật Thiện',
        'Nguyễn Mỹ Tiên',
        'Trần Thị Cẩm Tiên',
        'Võ Trần Bảo Tính',
        'Trương Thanh Toàn',
        'Phạm Ngọc Trâm',
        'Nguyễn Võ Bảo Trân'
    ],
    'CB210': [
        'Lê Huỳnh Thanh Duy',
        'Nguyễn Cao Kỳ Duyên',
        'Nguyễn Võ Thành Đạt',
        'Đào Ngọc Hân',
        'Trần Văn Hữu',
        'Trần Văn Kim Khoa',
        'Nguyễn Thanh Nâng',
        'Huỳnh Kỳ Nguyên',
        'Võ Thị Kim Nguyên',
        'Võ Hùng Sanh',
        'Trần Thị Thanh Thảo',
        'Tiền Thị Thanh Thảo',
        'Đặng Thị Kim Thoa',
        'Trần Thị Tiên Tiên',
        'Lê Kim Tuyền'
    ],
    'CB211': [
        'Hồ Anh Quân',
        'Lê Thành Nghiệp',
        'Lê Khánh Lâm',
        'Huỳnh Thị Ngọc Thắm',
        'Mai Trần Xuân Mai',
        'Lê Thị Uyển Nhi',
        'Nguyễn Thụy Thanh Trúc'
    ]
};

const AUTHORIZED_STUDENTS = [
    ...STUDENTS_BY_CLASS['CB206'],
    ...STUDENTS_BY_CLASS['CB210'],
    ...STUDENTS_BY_CLASS['CB211'],
    'PTMN'
];

function removeVietnameseTones(str) {
    if (!str) return '';
    return str
        .normalize('NFD')
        .replace(/[\u0300-\u036f]/g, '')
        .replace(/đ/g, 'd').replace(/Đ/g, 'D');
}

function normalizeVietnameseName(str) {
    if (!str) return '';
    return str.trim().toLowerCase().replace(/\\s+/g, ' ');
}

function findStudentInfo(name) {
    if (!name) return null;
    const norm = normalizeVietnameseName(name);
    const noTone = removeVietnameseTones(norm);

    if (norm === 'ptmn' || noTone === 'ptmn') {
        return { name: 'Cô Nguyệt (PTMN)', class: 'GV', isTeacher: true };
    }

    for (const [cls, list] of Object.entries(STUDENTS_BY_CLASS)) {
        // Try exact match first
        let found = list.find(s => normalizeVietnameseName(s) === norm);
        // Try without tones if not found
        if (!found) {
            found = list.find(s => removeVietnameseTones(normalizeVietnameseName(s)) === noTone);
        }
        if (found) {
            return { name: found, class: cls, isTeacher: false };
        }
    }
    return null;
}

function isAuthorizedStudent(name) {
    return findStudentInfo(name) !== null;
}

const GOOGLE_FORM_ACTION_URL = "https://docs.google.com/forms/d/e/1FAIpQLSes7cy3Z9Wxr_QQRuJcohfqFycoc0_i5JNEt05FFBBGod2f5A/formResponse";
const GOOGLE_FORM_ENTRY_ID = "entry.388968236";

let currentStudentName = '';
let currentStudentClass = '';

let loginModalOverlay;
let studentNameInput;
let studentClassInput;
let studentClassSelect;
let studentPasswordInput;
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
"""

# Replace top of dom_logic auth vars
idx_auth = dom_logic.find("// Auth & Student Information")
idx_recitation = dom_logic.find("// Recitation DOM Elements")
if idx_auth != -1 and idx_recitation != -1:
    dom_logic = dom_logic[:idx_auth] + auth_block.strip() + "\n\n" + dom_logic[idx_recitation:]

# Replace initAuthSystem and handleLoginSubmit in dom_logic
auth_functions = """
// --- Authentication & Student Profile Management ---
function initAuthSystem() {
    // Luôn luôn yêu cầu đăng nhập lại mỗi khi F5 hoặc mở lại trang web
    currentStudentName = '';
    currentStudentClass = '';
    updateStudentProfileUI('', '');
    openLoginModal();
}

function openLoginModal() {
    if (isRecitationInProgress || isFullPracticeInProgress) {
        showToastNotice('🔒 Đang trong thời gian làm bài! Không thể chỉnh sửa thông tin lúc này.', 'fa-solid fa-lock');
        return;
    }
    if (!loginModalOverlay) return;
    if (studentNameInput) studentNameInput.value = currentStudentName || '';
    if (studentClassInput) studentClassInput.value = currentStudentClass || '';
    if (studentClassSelect) studentClassSelect.value = currentStudentClass || '';
    if (studentPasswordInput) studentPasswordInput.value = '';
    if (loginErrorMsg) loginErrorMsg.classList.add('hidden');
    loginModalOverlay.classList.remove('hidden');
    setTimeout(() => {
        if (studentNameInput) studentNameInput.focus();
    }, 150);
}

function handleLoginSubmit() {
    const nameVal = studentNameInput ? studentNameInput.value.trim() : '';
    const classEl = studentClassInput || studentClassSelect;
    const classVal = classEl ? classEl.value.trim().toUpperCase().replace(/\\s+/g, '') : '';
    const passVal = studentPasswordInput ? studentPasswordInput.value.trim() : '';

    if (!nameVal || nameVal.length < 2) {
        showLoginError('Vui lòng nhập đầy đủ Họ và tên học viên / Giáo viên.');
        if (studentNameInput) studentNameInput.focus();
        return;
    }

    const studentInfo = findStudentInfo(nameVal);

    if (!studentInfo) {
        showLoginError('Họ và tên không nằm trong danh sách học viên (CB206, CB210, CB211) hoặc giáo viên!');
        if (studentNameInput) studentNameInput.focus();
        return;
    }

    if (studentInfo.isTeacher) {
        if (classVal && classVal !== 'GV' && !ALLOWED_CLASSES.includes(classVal)) {
            showLoginError('Giáo viên vui lòng điền Lớp: GV (hoặc để trống)!');
            if (classEl) classEl.focus();
            return;
        }
        currentStudentName = 'Cô Nguyệt (PTMN)';
        currentStudentClass = classVal || 'GV';
    } else {
        // Check student class
        if (classVal !== studentInfo.class) {
            showLoginError('Lớp học không đúng! Học viên ' + studentInfo.name + ' thuộc lớp ' + studentInfo.class + '.');
            if (classEl) classEl.focus();
            return;
        }

        // Check password
        if (passVal !== MANDATORY_PASSWORD) {
            showLoginError('Mật khẩu không chính xác! Vui lòng nhập đúng mật khẩu STUDYHARD.');
            if (studentPasswordInput) {
                studentPasswordInput.value = '';
                studentPasswordInput.focus();
            }
            return;
        }

        currentStudentName = studentInfo.name;
        currentStudentClass = studentInfo.class;
    }

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
"""

idx_auth_func = dom_logic.find("// --- Authentication & Student Profile Management ---")
idx_gform = dom_logic.find("// --- Google Form Reporting System ---")
if idx_auth_func != -1 and idx_gform != -1:
    dom_logic = dom_logic[:idx_auth_func] + auth_functions.strip() + "\n\n" + dom_logic[idx_gform:]

# Ensure element queries in DOMContentLoaded
dom_logic = dom_logic.replace(
    "studentClassSelect = document.getElementById('studentClassSelect');",
    "studentClassInput = document.getElementById('studentClassInput');\n    studentClassSelect = document.getElementById('studentClassSelect');\n    studentPasswordInput = document.getElementById('studentPasswordInput');"
)

# Ensure enter key listener on all fields
enter_listeners = """
    // Auth Listeners
    if (btnLoginSubmit) btnLoginSubmit.addEventListener('click', handleLoginSubmit);
    if (btnEditStudent) btnEditStudent.addEventListener('click', openLoginModal);
    if (studentNameInput) {
        studentNameInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') handleLoginSubmit();
        });
    }
    if (studentClassInput) {
        studentClassInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') handleLoginSubmit();
        });
    }
    if (studentPasswordInput) {
        studentPasswordInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') handleLoginSubmit();
        });
    }
"""

idx_auth_lis = dom_logic.find("// Auth Listeners")
idx_reset_prog = dom_logic.find("// Reset progress button listener")
if idx_auth_lis != -1 and idx_reset_prog != -1:
    dom_logic = dom_logic[:idx_auth_lis] + enter_listeners.strip() + "\n\n" + dom_logic[idx_reset_prog:]

# Combine everything
final_app_js = (
    letter_types_json + "\n\n" +
    recitation_questions_js.strip() + "\n\n" +
    extra_logic_js.strip() + "\n\n" +
    dom_logic.strip() + "\n"
)

# Write app.js
app_js_path = "/Users/nguyetpham/Desktop/WEBSITE/writing-letters-b1level/app.js"
with open(app_js_path, "w", encoding="utf-8") as f:
    f.write(final_app_js)

print("Saved complete app.js with Teacher PTMN / Class GV login! Total length:", len(final_app_js))
