#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter as tk
import time
import threading
from tkinter import *

# GUI設定
flg = 0
root = tk.Tk()
root.title("Key Checker")
root.geometry("1920x1080")

# 角丸長方形の定義
def round_rectangle(x1, y1, x2, y2, r, **kwargs):
    points = (
        x1 + r,
        y1,
        x1 + r,
        y1,
        x2 - r,
        y1,
        x2 - r,
        y1,
        x2,
        y1,
        x2,
        y1 + r,
        x2,
        y1 + r,
        x2,
        y2 - r,
        x2,
        y2 - r,
        x2,
        y2,
        x2 - r,
        y2,
        x2 - r,
        y2,
        x1 + r,
        y2,
        x1 + r,
        y2,
        x1,
        y2,
        x1,
        y2 - r,
        x1,
        y2 - r,
        x1,
        y1 + r,
        x1,
        y1 + r,
        x1,
        y1,
    )
    return canvas.create_polygon(points, **kwargs, smooth="True")


def update():
    k = 0
    if k % 2 == 0:
        text["fill"] = "#202020"
    else:
        text["fill"] = "#FFFFFF"
    k = k + 1
    root.after(500, update)  # while temporary


canvas = tk.Canvas(root, width=1920, height=1080)  # Canvasの作成
background = canvas.create_rectangle(
    0, -0, 1920, 1080, fill="#202020", outline="#202020"
)

# Canvas Initialize
f1_rec = round_rectangle(
    280, 60, 680, 180, r=30, fill="#202020", outline="#FFFFFF", width=4
)
f1 = canvas.create_text(
    480, 120, text="1階", fill="#FFFFFF", font=("BIZ UDPGothic", 64), justify="center"
)
f2_rec = round_rectangle(
    1240, 60, 1640, 180, r=30, fill="#202020", outline="#FFFFFF", width=4
)
f2 = canvas.create_text(
    1440, 120, text="2階", fill="#FFFFFF", font=("BIZ UDPGothic", 64), justify="center"
)

# 表作成
# 00A000 = Key: Locked, Light: OFF
# C0C000 = Key: Locked, Light: ON
# 000000 = Key: Unlocked, Light: ON (Letter color: #FFFF00)
postx = [200, 480, 760, 1160, 1440, 1720]
posty = [345, 495, 645, 795, 945]
for i in posty:
    for j in postx:
        if (
            (i <= posty[2])
            or (j != postx[2] and i == posty[3])
            or (j >= postx[3] and i == posty[4])
        ):
            waku = canvas.create_rectangle(
                j - 140,
                i - 75,
                j + 140,
                i + 75,
                fill="#202020",
                outline="#FFFFFF",
                width=4,
            )

text = canvas.create_text(
    postx[0],
    posty[0],
    text="101",
    fill="#FFFFFF",
    font=("Myriad Pro", 64),
    justify="center",
)
update()
# キャンバスバインド
canvas.place(x=0, y=0)  # Canvasの配置

root.mainloop()