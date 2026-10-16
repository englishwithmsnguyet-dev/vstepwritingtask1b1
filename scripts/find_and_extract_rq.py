# -*- coding: utf-8 -*-
import json

transcript_path = "/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/.system_generated/logs/transcript_full.jsonl"

found = False
with open(transcript_path, "r", encoding="utf-8") as f:
    for line in f:
        if "const recitationQuestions = {" in line and "complaint:" in line and "feedback:" in line and "apology:" in line:
            obj = json.loads(line)
            # Find in tool_calls or content
            text_sources = [obj.get("content", "")]
            for tc in obj.get("tool_calls", []):
                args = tc.get("args", {})
                for k, v in args.items():
                    if isinstance(v, str):
                        text_sources.append(v)
            
            for text in text_sources:
                if "const recitationQuestions = {" in text and "apology:" in text:
                    idx = text.find("const recitationQuestions = {")
                    idx_end = text.find("};\n\n// DOM Elements", idx)
                    if idx_end == -1:
                        idx_end = text.find("};\n// DOM Elements", idx_rq if 'idx_rq' in locals() else idx)
                    if idx_end == -1:
                        # find application closing:
                        idx_app = text.find("application: [", idx)
                        if idx_app != -1:
                            idx_end = text.find("\n    ]\n};", idx_app)
                            if idx_end != -1:
                                idx_end += len("\n    ]\n};")
                    
                    if idx_end != -1 and idx_end > idx:
                        rq = text[idx:idx_end]
                        with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/recitation_questions.js", "w", encoding="utf-8") as out:
                            out.write(rq.strip() + "\n")
                        print("Successfully extracted recitation_questions.js! Length:", len(rq))
                        found = True
                        break
            if found:
                break

if not found:
    print("Could not find complete recitationQuestions")
