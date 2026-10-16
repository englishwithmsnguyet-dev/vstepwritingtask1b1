with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace double quoted promptText with backticks
old_prompt = 'promptText: "You have received a letter from a friend, Emily. She is going to visit Can Tho in December. Write a letter to give her some suggestions. You should tell her:\\n• Where to stay\\n• What dishes to try\\n• Which tourist attractions to visit\\n• What to wear\\nYou should write at least 120 words. Do not include your name. Your response will be evaluated in terms of Task Fulfillment, Organization, Vocabulary, and Grammar.",'

new_prompt = '''promptText: `You have received a letter from a friend, Emily. She is going to visit Can Tho in December. Write a letter to give her some suggestions. You should tell her:
• Where to stay
• What dishes to try
• Which tourist attractions to visit
• What to wear
You should write at least 120 words. Do not include your name. Your response will be evaluated in terms of Task Fulfillment, Organization, Vocabulary, and Grammar.`,'''

if old_prompt in content:
    content = content.replace(old_prompt, new_prompt)
else:
    # Also check if it was formatted with literal newlines
    content = re.sub(r'promptText:\s*"You have received.*?"', new_prompt, content, flags=re.DOTALL)

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated reconstruct_app.py promptText with backticks!")
