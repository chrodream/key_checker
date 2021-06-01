import urllib.request
import urllib.parse

# 特定HEADER送信の例です。このサンプルに未使用
reqAddtionalHeaders = {
    'X-Request=Process': "01"
}

data = urllib.parse.urlencode({"205": "205,0,1"})
data = data.encode('utf-8')

req = urllib.request.Request(
    "http://localhost:2001", data, reqAddtionalHeaders)

with urllib.request.urlopen(req) as f:
    print(f.read().decode('utf-8'))