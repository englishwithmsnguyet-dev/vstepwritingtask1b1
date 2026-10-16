# -*- coding: utf-8 -*-
import json

transcript_path = "/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/.system_generated/logs/transcript_full.jsonl"

with open(transcript_path, "r", encoding="utf-8") as f:
    for idx, line in enumerate(f, 1):
        if idx == 587:
            obj = json.loads(line)
            tool_calls = obj.get("tool_calls", [])
            for tc in tool_calls:
                args = tc.get("args", {})
                repl = args.get("ReplacementContent", "")
                if repl:
                    with open("/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/scratch/dom_logic_full.js", "w", encoding="utf-8") as out:
                        out.write(repl)
                    print(f"Extracted dom_logic_full.js! Length: {len(repl)}")
                    break
