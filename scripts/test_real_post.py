import urllib.request
import urllib.parse

form_url = "https://docs.google.com/forms/d/e/1FAIpQLSes7cy3Z9Wxr_QQRuJcohfqFycoc0_i5JNEt05FFBBGod2f5A/formResponse"

payload_data = {
    "entry.388968236": "Nguyễn Văn A - Lớp CB201 - Đăng nhập",
    "fvv": "1",
    "pageHistory": "0"
}

encoded = urllib.parse.urlencode(payload_data).encode('utf-8')
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded'
}

req = urllib.request.Request(form_url, data=encoded, headers=headers)

try:
    with urllib.request.urlopen(req) as resp:
        print("Status code:", resp.getcode())
        content = resp.read().decode('utf-8')
        if "formResponse" in resp.geturl() or resp.getcode() == 200:
            print("Successfully submitted response to Google Form!")
            # Check if confirmation text exists
            print("Response length:", len(content))
except Exception as e:
    print("Error submitting:", e)
