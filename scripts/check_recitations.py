with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/reconstruct_app.py", "r", encoding="utf-8") as f:
    text = f.read()

namespace = {}
code_to_exec = text[:text.find("dom_and_logic_code =")]
exec(code_to_exec, namespace)

letter_types = namespace['letter_types']
for idx, lt in enumerate(letter_types, 1):
    print("="*70)
    print(f"TYPE {idx}: {lt['id']} - {lt['titleEn']}")
    print("="*70)
    for q_idx, q in enumerate(lt['recitationQuestions'], 1):
        print(f"  Q{q_idx}: [{q['cue']}] -> {q['target']}")
    print("\n")
