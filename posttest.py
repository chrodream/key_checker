#!/usr/bin/env python3
import urllib.request
import urllib.parse

data = urllib.parse.urlencode({"205": "205,1,1"})
data = data.encode('utf-8')

req = urllib.request.Request("http://localhost:2001", data)

with urllib.request.urlopen(req) as f:
    print(f.read().decode('utf-8'))