# -*- coding: utf-8 -*-
import json
import re

transcript_full = "/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/.system_generated/logs/transcript_full.jsonl"

with open(transcript_full, "r", encoding="utf-8") as f:
    for idx, line in enumerate(f, 1):
        if idx == 197:
            obj = json.loads(line)
            content = obj.get("content", "")
            # The content has line numbers like "842: const recitationQuestions = {\n843: ...\n"
            # Let's strip line numbers: r'^\d+:\s*' on each line
            clean_lines = []
            capture = False
            for l in content.split("\n"):
                clean_l = re.sub(r'^\d+:\s*', '', l)
                if "const recitationQuestions = {" in clean_l:
                    capture = True
                if capture:
                    clean_lines.append(clean_l)
                    if clean_l.strip() == "};" and len(clean_lines) > 20:
                        break
            
            rq_clean = "\n".join(clean_lines)
            with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/recitation_questions.js", "w", encoding="utf-8") as out:
                out.write(rq_clean.strip() + "\n")
            print("Successfully extracted recitation_questions.js! Total lines:", len(clean_lines), "Length:", len(rq_clean))
            break
