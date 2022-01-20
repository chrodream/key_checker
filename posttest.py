#!/usr/bin/env python3
from tabnanny import check
import urllib.request
import urllib.parse
import random

roomlist = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111,
            201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 214]

room = random.choice(roomlist)
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