import urllib.request
import urllib.parse

form_url = "https://docs.google.com/forms/d/e/1FAIpQLSes7cy3Z9Wxr_QQRuJcohfqFycoc0_i5JNEt05FFBBGod2f5A/formResponse"
entry_id = "entry.388968236"
test_val = "TEST - Nguyễn Văn A - Lớp CB201 - Test kết nối hệ thống"

data = urllib.parse.urlencode({entry_id: test_val}).encode('utf-8')
req = urllib.request.Request(form_url, data=data, headers={'User-Agent': 'Mozilla/5.0'})

try:
    with urllib.request.urlopen(req) as response:
        print("Status code:", response.getcode())
        print("Success!")
except Exception as e:
    print("Error during test:", e)
