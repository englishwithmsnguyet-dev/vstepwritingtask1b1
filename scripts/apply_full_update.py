import re

# Read letter_types from update_reconstruct.py
with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/update_reconstruct.py", "r", encoding="utf-8") as f:
    update_text = f.read()

# Read reconstruct_app.py to get dom_and_logic_code
with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "r", encoding="utf-8") as f:
    reconstruct_text = f.read()

dom_and_logic_index = reconstruct_text.find("dom_and_logic_code =")
if dom_and_logic_index == -1:
    raise Exception("Could not find dom_and_logic_code in reconstruct_app.py")

dom_and_logic = reconstruct_text[dom_and_logic_index:]

full_code = update_text.strip() + "\n\n" + dom_and_logic

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "w", encoding="utf-8") as f:
    f.write(full_code)

print("Updated reconstruct_app.py successfully!")
