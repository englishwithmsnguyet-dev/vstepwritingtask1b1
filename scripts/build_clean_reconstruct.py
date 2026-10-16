with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/update_reconstruct.py", "r", encoding="utf-8") as f:
    top_code = f.read()

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "r", encoding="utf-8") as f:
    cur = f.read()

idx = cur.find('dom_and_logic_code = """')
if idx == -1:
    raise Exception("dom_and_logic_code not found")

bottom_code = cur[idx:]

clean_code = top_code.strip() + """

js_array_code = "const letterTypes = " + json.dumps(letter_types, ensure_ascii=False, indent=4) + ";\\n"
""" + bottom_code

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "w", encoding="utf-8") as f:
    f.write(clean_code)

print("Saved clean reconstruct_app.py!")
