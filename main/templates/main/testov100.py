#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter.filedialog import askopenfilename
from tkinter import *
import os, sys

def die(event):
    sys.exit(0)

root = Tk()
w = root.winfo_screenwidth()//2 - 400
h = root.winfo_screenwidth()//2 -300
root.geometry('800x600+{}+{}'.format(w, h))
root.title('Подписать документ')

flName = askopenfilename(title='Что подписываем?')

if flName:
    os.system('gpg -ba ' + flName)
    button = Button(text='ЭЦП создана')
    button.bind('<Button-1>', die)
    button.pack(expand=YES, anchor=CENTER)
else:
    die()

root.mainloop()