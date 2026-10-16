import re

with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "r", encoding="utf-8") as f:
    text = f.read()

# Let's inspect each letter type block
import sys

# We can execute the python file up to letter_types definition
# Let's write a script that loads letter_types directly
namespace = {}
code_to_exec = text[:text.find("dom_and_logic_code =")]
exec(code_to_exec, namespace)

letter_types = namespace['letter_types']
for idx, lt in enumerate(letter_types, 1):
    print("="*70)
    print(f"TYPE {idx}: {lt['id']} - {lt['titleEn']} ({lt['titleVi']})")
    print("="*70)
    print("--- DETAILED OUTLINE ---")
    print(lt['detailedOutline'][:300] + "...")
    print("--- SAMPLE WRITING ---")
    print(lt['sampleWriting'][:400] + "...")
    print("\n")
