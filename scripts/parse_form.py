import urllib.request
import re
import json

url = "https://forms.gle/Pgwmr6GijFwjebaM9"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8')
        print("Final URL:", resp.geturl())
except Exception as e:
    print("Error:", e)
    # read from local saved file
    with open('/Users/nguyetpham/.gemini/antigravity/brain/d546b07e-2dc8-4d1a-8c59-7105c0e9be08/.system_generated/steps/2003/content.md', 'r') as f:
        html = f.read()

# find FB_PUBLIC_LOAD_DATA_
match = re.search(r'FB_PUBLIC_LOAD_DATA_\s*=\s*(.*?);</script>', html)
if match:
    data_str = match.group(1)
    data = json.loads(data_str)
    print("Form Title:", data[1][8] if len(data[1]) > 8 else "Unknown")
    print("Form Description:", data[1][0])
    
    # Items
    items = data[1][1]
    for item in items:
        title = item[1]
        item_id = item[0]
        entry_info = item[4]
        print(f"\nItem: {title} (id: {item_id})")
        if entry_info:
            for entry in entry_info:
                entry_id = entry[0]
                options = entry[1]
                print(f"  entry.{entry_id}")
                if options:
                    print(f"  Options: {[opt[0] for opt in options]}")
else:
    print("Could not find FB_PUBLIC_LOAD_DATA_")
