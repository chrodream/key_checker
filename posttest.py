#!/usr/bin/env python3
import urllib.request
import urllib.parse
import random

data = urllib.parse.urlencode({"room_num":"205", "key_stat":str(random.randint(0, 1)), "light_stat":str(random.randint(0, 1))})
data = data.encode('utf-8')

req = urllib.request.Request("http://localhost:2001", data)

with urllib.request.urlopen(req) as f:
    print(f.read().decode('utf-8'))