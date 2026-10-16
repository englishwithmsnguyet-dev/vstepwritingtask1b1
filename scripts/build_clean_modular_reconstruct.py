# -*- coding: utf-8 -*-
with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "r", encoding="utf-8") as f:
    code = f.read()

# Extract js_array_code part (up to where dom_and_logic_code starts)
array_end_idx = code.find('dom_and_logic_code = """')
if array_end_idx == -1:
    raise Exception("Could not find dom_and_logic_code start")

array_section = code[:array_end_idx]

# Now let's extract the clean base dom_and_logic_code (starting from function selectLetterType(id) {)
select_idx = code.find("function selectLetterType(id) {")
if select_idx == -1:
    raise Exception("Could not find selectLetterType")

dom_part = code[select_idx:]
# Find where dom_and_logic_code ends (where triple quotes end)
quote_idx = dom_part.rfind('"""')
if quote_idx != -1:
    clean_dom = dom_part[:quote_idx]
else:
    clean_dom = dom_part

new_reconstruct = array_section + '\nwith open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/pure_extra_logic.js", "r", encoding="utf-8") as f:\n    extra_logic_code = f.read()\n\ndom_and_logic_code = """\n' + clean_dom.strip() + '\n"""\n\nfull_content = js_array_code + "\\n\\n" + extra_logic_code + "\\n\\n" + dom_and_logic_code\n\nwith open(app_js_path, "w", encoding="utf-8") as f:\n    f.write(full_content)\nprint("Reconstructed app.js completely and correctly with modular VSTEP engine.")\n'

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "w", encoding="utf-8") as f:
    f.write(new_reconstruct)

print("Modular reconstruct_app.py built successfully!")
