# Знакомство с виджетами. Виджет Button

def say_hello():
    print('hello')
def add_lebel():
    print('Python')

def add_new_lebel():
    print('Python')

import tkinter as tk

win = tk.Tk()
win.geometry(f"400x500+100+200")
win.title('Мое первое графическое приложение')

btn1 = tk.Button(win, text='Hello',
                 command=say_hello
                 )
btn2 = tk.Button(win, text='Python',
                 command=add_lebel
                 )
btn3 = tk.Button(win, text='Super',
                 command=add_lebel
                 )
btn1.pack()
btn2.pack()
win.mainloop()
