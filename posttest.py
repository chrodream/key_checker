#!/usr/bin/env python3
from tabnanny import check
import urllib.request
import urllib.parse
import random

room = 101
key = random.randint(0, 1)
light = random.randint(0, 1)
checksum = str(room * 7 + key * 5 + light * 3)

data = urllib.parse.urlencode(
    {
        "room_num": str(room),
        "key_stat": str(key),
        "light_stat": str(light),
        "check_sum": str(checksum)
    }
)
data = data.encode("utf-8")

req = urllib.request.Request("http://localhost:2001", data)

print("Room Number:  ", end='')
with urllib.request.urlopen(req) as f:
    print(f.read().decode("utf-8"))

print("Key Status:   " + str(bool(key)))
print("Light Status: " + str(bool(light)))
print("Check Sum:    " + str(checksum))