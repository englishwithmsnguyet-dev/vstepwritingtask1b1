# -*- coding: utf-8 -*-
import json

transcript_path = "/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/.system_generated/logs/transcript.jsonl"

with open(transcript_path, "r", encoding="utf-8") as f:
    for idx, line in enumerate(f, 1):
        if idx == 1934:
            obj = json.loads(line)
            content = obj.get("content", "")
            idx_rq = content.find("const recitationQuestions = {")
            print("Content snippet from idx_rq:")
            print(content[idx_rq:idx_rq+1000])
            print("...")
            print(content[idx_rq+len(content)-idx_rq-1000:])
            break
