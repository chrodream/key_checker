# 関数を紐づけたボタンを配置
#--------------------------

import tkinter
root = tkinter.Tk()
root.title('demo_Tkinter')
root.geometry("400x400")

# コンソールに"Button is clicked."を出力する関数
def second_floor():
    print("Changing display to 2F...")
    canvas.delete('all')
    button = tkinter.Button(root, text="1F", command=first_floor)
    button.grid()

def first_floor():
    print("Changing display to 1F...")
    canvas.delete('all')
    button = tkinter.Button(root, text="2F", command=second_floor)
    button.grid()

# ボタンの作成（text=ボタンに表示されるテキスト, command=押下時に呼び出す関数）
button = tkinter.Button(root, text="2F", command=second_floor)


# ボタンの表示
button.grid()

root.mainloop()
