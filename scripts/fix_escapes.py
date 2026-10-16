# -*- coding: utf-8 -*-
with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/full_extra_logic.js", "r", encoding="utf-8") as f:
    code = f.read()

# Replace promptText with concatenated strings or escaped newlines
old_p = 'promptText: "You have received a letter from a friend, Emily. She is going to visit Can Tho in December. Write a letter to give her some suggestions. You should tell her:\\n• Where to stay\\n• What dishes to try\\n• Which tourist attractions to visit\\n• What to wear\\nYou should write at least 120 words. Do not include your name. Your response will be evaluated in terms of Task Fulfillment, Organization, Vocabulary, and Grammar.",'

new_p = 'promptText: "You have received a letter from a friend, Emily. She is going to visit Can Tho in December. Write a letter to give her some suggestions. You should tell her:\\\\n• Where to stay\\\\n• What dishes to try\\\\n• Which tourist attractions to visit\\\\n• What to wear\\\\nYou should write at least 120 words. Do not include your name. Your response will be evaluated in terms of Task Fulfillment, Organization, Vocabulary, and Grammar.",'

code = code.replace(old_p, new_p)

# Also for sampleModel and sampleModelVi:
code = code.replace('sampleModel: "Dear Emily,\\n\\n', 'sampleModel: "Dear Emily,\\\\n\\\\n')
code = code.replace('sampleModelVi: "Emily thân mến,\\n\\n', 'sampleModelVi: "Emily thân mến,\\\\n\\\\n')
code = code.replace('\\n\\n', '\\\\n\\\\n')

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/full_extra_logic.js", "w", encoding="utf-8") as f:
    f.write(code)

print("Fixed full_extra_logic.js escapes!")
