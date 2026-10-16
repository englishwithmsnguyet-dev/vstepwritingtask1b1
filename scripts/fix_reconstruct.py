with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Line 4 was "code = '''import json\n"
# Lines 5 to 1031 is the actual python code for letter_types
# Line 1054 starts dom_and_logic_code = """ up to line 2307

# Let's extract the clean lines:
# 1. Start with imports and path
# 2. Add letter_types definition
# 3. Add dom_and_logic_code definition
# 4. Write full_content to app.js

letter_types_part = "".join(lines[4:1031])
dom_and_logic_part = "".join(lines[1053:])

clean_script = f"""import json

app_js_path = "/Users/nguyetpham/Desktop/WEBSITE/writing-letters-b1level/app.js"

{letter_types_part}

js_array_code = "const letterTypes = " + json.dumps(letter_types, ensure_ascii=False, indent=4) + ";\\n"

{dom_and_logic_part}
"""

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "w", encoding="utf-8") as f:
    f.write(clean_script)

print("Saved clean reconstruct_app.py!")
