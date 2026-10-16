import re
import json

with open('/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/.system_generated/steps/2003/content.md', 'r') as f:
    html = f.read()

match = re.search(r'FB_PUBLIC_LOAD_DATA_\s*=\s*(.*?);</script>', html)
if match:
    data = json.loads(match.group(1))
    print("Form action/id info:", data[14]) # or check form response url
    print("Form Title:", data[1][8] if len(data[1]) > 8 else "Unknown")
    print("Items count:", len(data[1][1]))
    for idx, item in enumerate(data[1][1]):
        print(f"--- Item {idx} ---")
        print("Title:", item[1])
        print("Desc:", item[2])
        print("Type:", item[3])
        print("Item ID:", item[0])
        if item[4]:
            for entry in item[4]:
                print(f"  Entry ID: entry.{entry[0]}")
                if entry[1]:
                    print(f"  Options: {[opt[0] for opt in entry[1]]}")
                print(f"  Validation/Type: {entry[3] if len(entry)>3 else None}")
