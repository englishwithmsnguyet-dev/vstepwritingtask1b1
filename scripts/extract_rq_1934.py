# -*- coding: utf-8 -*-
import json

transcript_path = "/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/.system_generated/logs/transcript.jsonl"

with open(transcript_path, "r", encoding="utf-8") as f:
    for idx, line in enumerate(f, 1):
        if idx == 1934:
            obj = json.loads(line)
            content = obj.get("content", "")
            idx_rq = content.find("const recitationQuestions = {")
            # Find ending
            idx_dom = content.find("// DOM Elements", idx_rq)
            if idx_dom != -1:
                rq_text = content[idx_rq:idx_dom].strip()
                if rq_text.endswith(";"):
                    pass
                with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/recitation_questions.js", "w", encoding="utf-8") as out:
                    out.write(rq_text + "\n")
                print("Saved recitation_questions.js! Length:", len(rq_text))
            else:
                print("Could not find // DOM Elements after const recitationQuestions")
            break
