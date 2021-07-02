#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter
import time
import threading

#
# GUI設定
#
flg = 0
root = tkinter.Tk()
root.title("tkinterのCanvasを使ってみる")
root.geometry("1920x1080")

#キャンバスエリア
canvas = tkinter.Canvas(root, width = 1920, height = 1080)#Canvasの作成
background = canvas.create_rectangle(-1, -1, 1920, 1080, fill = '#000000', outline = '#000000')

#表作成
for i in range(7):
    r101_bg = canvas.create_rectangle(i * 50, 100, i * 50 + 40, 200, fill = '#FFFFFF', outline = '#000000')
    r101 = canvas.create_text(70, i * 100, text = "101", fill = '#FFFF00', font = ('', 24), justify = "left")



#キャンバスバインド
canvas.place(x=0, y=0)#Canvasの配置


#
# GUIの末端
#
root.mainloop()