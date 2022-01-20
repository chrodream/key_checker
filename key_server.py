#!/usr/bin/env python3
from calendar import c
from http import server
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from ssl import OPENSSL_VERSION_NUMBER, SOCK_STREAM
import csv
import datetime as dt
import html
import netifaces as ni
import os
import pprint
import psutil
import re
import socket
import sys
import time
import urllib.parse

PORT = 2001
m5resend = 999
listen_num = 5
buffer_size = 1024

# Check IP address
if os.name == 'nt':
    # Windows
    ip = socket.gethostbyname_ex(socket.gethostname())[2]
    os.system('cls')
    pass
else:
    # Linux, Mac
    result = []
    address_list = psutil.net_if_addrs()
    for nic in address_list.keys():
        ni.ifaddresses(nic)
        try:
            ip = ni.ifaddresses(nic)[ni.AF_INET][0]['addr']
            if ip not in ['127.0.0.1']:
                result.append(ip)
        except KeyError as err:
            pass
    os.system('clear')
    ip = result[0]

# Rooms status
room_stat = [
    ['101', '1', '0'],
    ['102', '1', '0'],
    ['103', '1', '0'],
    ['104', '1', '0'],
    ['105', '1', '0'],
    ['106', '1', '0'],
    ['107', '1', '0'],
    ['108', '1', '0'],
    ['109', '1', '0'],
    ['110', '1', '0'],
    ['111', '1', '0'],
    ['201', '1', '0'],
    ['202', '1', '0'],
    ['203', '1', '0'],
    ['204', '1', '0'],
    ['205', '1', '0'],
    ['206', '1', '0'],
    ['207', '1', '0'],
    ['208', '1', '0'],
    ['209', '1', '0'],
    ['210', '1', '0'],
    ['211', '1', '0'],
    ['212', '1', '0'],
    ['214', '1', '0'],
]

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# tcp_server.bind((ip, PORT))
# tcp_server.listen(listen_num)


print('======================================================================')
print('Key Checker v1.0 (work on ' + os.name + ')')
print('Currently IP address: ' + '\033[32m' + '\033[1m' + ip + '\033[0m')
print('======================================================================')
print('Waiting data from clients...')
print('======================================================================')


class StubHttpRequestHandler(BaseHTTPRequestHandler):
    server_version = 'HTTP Stub/0.1'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do_GET(self):
        enc = sys.getfilesystemencoding()
        title = 'Key Checker'
        dt_now_get = dt.datetime.now()
        now_time = str(dt_now_get.year) + "-" + str(dt_now_get.month) + "-" + str(
            dt_now_get.day) + " " + str(dt_now_get.hour) + ":" + str(dt_now_get.minute)
        r = []
        r.append('<!DOCTYPE html>')
        r.append('<html lang="en">\n<head>')
        r.append('<meta charset="UTF-8">')
        # auto reload
        r.append('<meta http-equiv="refresh" content="60"; URL=">')
        r.append(
            '<meta name="description" content="ネットワーク上から鍵がどこにあるか, 明かりがついているかがわかります。">')
        r.append('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@500&display=swap" rel="stylesheet">')
        r.append('<title>%s</title>\n</head>' % title)
        r.append(
            '<style type="text/css">body {\nfont-family:"Noto Sans JP", "monospace" \n}</style>')
        r.append('<body>\n<h1>%s</h1>' % title)
        r.append('<hr>\n<ul>')
        r.append('Key Checker is runnig now!')
        r.append('</ul>\n<ul>')

        r.append('Update time: %s' % now_time)
        r.append('</ul>\n<hr>\n')
        r.append('<table border="3">\n')
        r.append('<tr><th>Room</th><th>Key</th><th>Light</th></tr>\n')
        for count_room in range(24):
            if room_stat[count_room][1] == '1' and room_stat[count_room][2] == '1':
                # print(room_stat[count_room][0])
                r.append('<tr><td><font color="orange">' + str(room_stat[count_room][0]) + '</font></td>')
                r.append('<td><font color="orange">' + 'LOCK🔒' + '</font></td>')
                r.append('<td><font color="orange">' + 'ON💡' + '</font></td>')
                r.append('</tr></font>')
            
            else:
                r.append('<tr><td>' + str(room_stat[count_room][0]) + '</td>')
                if room_stat[count_room][1] == '0':
                    r.append('<td>' + 'UNLOCK' + '</td>')
                else:
                    r.append('<td>' + 'LOCK🔒' + '</td>')

                if room_stat[count_room][2] == '0':
                    r.append('<td>' + 'OFF' + '</td>')
                else:
                    r.append('<td>' + 'ON💡' + '</td></tr>')

        r.append('</table>\n')
        r.append('</body>\n</html>\n')
        encoded = '\n'.join(r).encode(enc, 'surrogateescape')

        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type', 'text/html; charset=%s' % enc)
        self.send_header('Content-Length', str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

        print('======================================================================')

    def do_POST(self):
        enc = sys.getfilesystemencoding()
        length = self.headers.get('content-length')
        nbytes = int(length)
        rawPostData = self.rfile.read(nbytes)
        decodedPostData = rawPostData.decode(enc)
        postData = urllib.parse.parse_qs(decodedPostData)
        print(decodedPostData)
        pan = postData['room_num']
        roomnum = postData['room_num']
        keystat = postData['key_stat']
        lightstat = postData['light_stat']
        chk_sum = postData['check_sum']
        # print(chk_sum[0])
        # print(postData.items)
        resultData = []
        resultData.append(pan[0])

        encoded = '\n'.join(resultData).encode(enc)
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type', 'text/plain; charset=%s' % enc)
        self.send_header('Content-Length', str(len(encoded)))
        self.end_headers()

        self.wfile.write(encoded)

        if int(chk_sum[0]) != (int(roomnum[0]) * 7) + (int(keystat[0]) * 5) + (int(lightstat[0]) * 3):
            print('\033[31m\033[1mArguments Error!\033[0m')

        else:
            if roomnum[0] == m5resend:
                print('data from M5.')
                client, address = tcp_server.accept()
                print('[*] Connected!! [ Source : {}]'.format(address))

            else:
                print('POST data from ' + '\033[32m\033[1m' + roomnum[0] + '\033[0m')
                if keystat[0] == '0':
                    print('Key  : \033[32m\033[1mUnlocked\033[0m')
                else:
                    print('Key  : \033[32m\033[1mLocked\033[0m')

                if lightstat[0] == '0':
                    print('Light: \033[32m\033[1mOFF\033[0m')
                else:
                    print('Light: \033[32m\033[1mON\033[0m')

                dt_now_post = dt.datetime.now()

                for i in range(len(room_stat)):
                    if roomnum[0] == room_stat[i][0]:
                        room_stat[i][1] = keystat[0]
                        room_stat[i][2] = lightstat[0]
                        break

                with open(
                    './roomlog_'
                    + str(dt_now_post.year)
                    + '_'
                    + str(dt_now_post.month)
                    + '_'
                    + str(dt_now_post.day)
                    + '.csv',
                    'a',
                ) as f:
                    writer = csv.writer(f)
                    writer.writerow(
                        [dt_now_post.hour, dt_now_post.minute, roomnum[0],
                            keystat[0], lightstat[0]]
                    )
        print('======================================================================')


try:
    handler = StubHttpRequestHandler
    httpd = HTTPServer(('', PORT), handler)
    httpd.serve_forever()

except KeyboardInterrupt:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print('======================================================================')
    print('Keyboard interrupt detected.')
    print('Exiting Key Checker......')
    print('======================================================================')