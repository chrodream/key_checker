import os
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

PORT = 2001


class StubHttpRequestHandler(BaseHTTPRequestHandler):
    server_version = "HTTP Stub/0.1"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do_GET(self):
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

    def do_POST(self):
        enc = sys.getfilesystemencoding()

        length = self.headers.get('content-length')
        nbytes = int(length)
        rawPostData = self.rfile.read(nbytes)
        decodedPostData = rawPostData.decode(enc)
        postData = urllib.parse.parse_qs(decodedPostData)

        pan = postData["205"]
        print(pan[0])
        resultData = []
        resultData.append(pan[0])

        encoded = '\n'.join(resultData).encode(enc)
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "text/plain; charset=%s" % enc)
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()

        self.wfile.write(encoded)

        data = re.findall(r'\d+', pan[0])  # strをリストに振り分け
        for i in range(3):
            data[i] = int(data[i])  # 本来数値のデータはint化
            if data[i] <= 1:
                if data[i] == 1:
                    print("ON")
                    data[i] = "ON"
                else:
                    print("OFF")
                    data[i] = "OFF"
            else:
                print(data[i])

        dt_now = datetime.datetime.now()
        with open('./roomlog.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([dt_now.year, dt_now.month,
                            dt_now.day, dt_now.hour, dt_now.minute, data[0], data[1], data[2]])


handler = StubHttpRequestHandler
httpd = HTTPServer(('', PORT), handler)
httpd.serve_forever()
