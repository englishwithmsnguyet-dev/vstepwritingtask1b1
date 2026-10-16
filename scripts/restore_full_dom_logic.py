# -*- coding: utf-8 -*-
import json
import re

transcript_path = "/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/.system_generated/logs/transcript_full.jsonl"

found_content = None
with open(transcript_path, "r", encoding="utf-8") as f:
    for line in f:
        if "const recitationQuestions = {" in line and "initAuthSystem" in line:
            obj = json.loads(line)
            content = obj.get("content", "")
            if "const recitationQuestions = {" in content:
                found_content = content
                break

if not found_content:
    # Try searching line by line in transcript.jsonl
    transcript_compact = "/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/.system_generated/logs/transcript.jsonl"
    with open(transcript_compact, "r", encoding="utf-8") as f:
        for line in f:
            if "const recitationQuestions = {" in line and "initAuthSystem" in line:
                obj = json.loads(line)
                found_content = obj.get("content", "")
                break

print("Found content length:", len(found_content) if found_content else "None")

# Let's extract dom_and_logic_code
if found_content:
    idx = found_content.find('dom_and_logic_code = """')
    if idx != -1:
        dom_code = found_content[idx + len('dom_and_logic_code = """'):]
        end_q = dom_code.rfind('"""')
        if end_q != -1:
            dom_code = dom_code[:end_q]
        
        with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/dom_logic_full.js", "w", encoding="utf-8") as f:
            f.write(dom_code.strip())
        print("Saved dom_logic_full.js! Length:", len(dom_code))
