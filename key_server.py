#!/usr/bin/env python3
import os
from ssl import OPENSSL_VERSION_NUMBER
import sys
import urllib.parse
import html
import re
import datetime
import csv
import pprint
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from http import HTTPStatus
import tkinter
PORT = 2001

room_stat = [[101, 0, 0],
            [102, 0, 0],
            [103, 0, 0],
            [104, 0, 0],
            [105, 0, 0],
            [106, 0, 0],
            [107, 0, 0],
            [108, 0, 0],
            [109, 0, 0],
            [110, 0, 0],
            [111, 0, 0],
            [201, 0, 0],
            [201, 0, 0],
            [202, 0, 0],
            [203, 0, 0],
            [204, 0, 0],
            [205, 0, 0],
            [206, 0, 0],
            [207, 0, 0],
            [208, 0, 0],
            [209, 0, 0],
            [210, 0, 0],
            [211, 0, 0],
            [212, 0, 0],
            [214, 0, 0],]


class StubHttpRequestHandler(BaseHTTPRequestHandler):
    server_version = "HTTP Stub/0.1"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do_GET(self):
        print("======================================================================")
        enc = sys.getfilesystemencoding()
        title = "Key Checker"

        r = []
        r.append('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" '
                 '"http://www.w3.org/TR/html4/strict.dtd">')
        r.append('<html>\n<head>')
        r.append('<meta http-equiv="Content-Type" '
                 'content="text/html; charset=%s">' % enc)
        r.append('<title>%s</title>\n</head>' % title)
        r.append('<body>\n<h1>%s</h1>' % title)
        r.append('<hr>\n<ul>')
        r.append("Key Checker is runnig now!")
        r.append('</ul>\n<hr>\n</body>\n</html>\n')
        encoded = '\n'.join(r).encode(enc, 'surrogateescape')

        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "text/html; charset=%s" % enc)
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

        print("======================================================================")

    def do_POST(self):
        print("======================================================================")
        enc = sys.getfilesystemencoding()

        length = self.headers.get('content-length')
        nbytes = int(length)
        rawPostData = self.rfile.read(nbytes)
        decodedPostData = rawPostData.decode(enc)
        postData = urllib.parse.parse_qs(decodedPostData)
        print(decodedPostData)
        pan = postData["room_num"]
        roomnum = postData["room_num"]
        keystat = postData["key_stat"]
        lightstat = postData["light_stat"]
        print(postData.items)
        resultData = []
        resultData.append(pan[0])

        encoded = '\n'.join(resultData).encode(enc)
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "text/plain; charset=%s" % enc)
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()

        self.wfile.write(encoded)
        print("POST data from "+roomnum[0])
        if keystat[0] == "1":
            print("Key  : Locked")
        else:
            print("Key  : Unlocked")
        
        if lightstat[0] == "1":
            print("Light: ON")
        else:
            print("Light: OFF")

        dt_now = datetime.datetime.now()

        for i in range(len(room_stat)):
            if roomnum[0] == room_stat[i][0]:
                room_stat[i][1] = keystat[0]
                room_stat[i][2] = lightstat[0]

        with open('./roomlog.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([dt_now.year, dt_now.month,
                             dt_now.day, dt_now.hour, dt_now.minute, roomnum[0], keystat[0], lightstat[0]])

        print("======================================================================")
        for i in range(len(room_stat)):
            print(str(room_stat[i][0]) + "  " + str(room_stat[i][1]) + "  " + str(room_stat[i][2]))


handler = StubHttpRequestHandler
httpd = HTTPServer(('', PORT), handler)
httpd.serve_forever()
