# -*- coding: utf-8 -*-
import json

transcript_path = "/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/.system_generated/logs/transcript_full.jsonl"

with open(transcript_path, "r", encoding="utf-8") as f:
    for idx, line in enumerate(f, 1):
        if idx == 197:
            obj = json.loads(line)
            content = obj.get("content", "")
            idx_rq = content.find("const recitationQuestions = {")
            idx_rq_end = content.find("};\n\n// DOM Elements", idx_rq)
            if idx_rq_end == -1:
                idx_rq_end = content.find("};\n// DOM Elements", idx_rq)
            if idx_rq_end == -1:
                # Find matching closing brace
                idx_rq_end = content.find("\n};\n", idx_rq) + 3

            rq_code = content[idx_rq:idx_rq_end]
            with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/recitation_questions.js", "w", encoding="utf-8") as out:
                out.write(rq_code.strip() + "\n")
            print("Extracted recitation_questions.js! Length:", len(rq_code))
            break
