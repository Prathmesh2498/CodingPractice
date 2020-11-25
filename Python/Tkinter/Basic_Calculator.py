# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 20:27:24 2020

@author: Admin
"""

from tkinter import *
from style import *
import os
import random
import time

#Note: You cannot use pack and grid together!

root = Tk()

root.geometry('720x480')

numbers_frame = Frame(root, bg='#000000')
numbers_frame.pack(side=LEFT, expand=YES, fill=BOTH)

numbers_frame = Frame(root, bg='#000000')
numbers_frame.pack(side=RIGHT, expand=YES, fill=BOTH)


frame1 = Frame(root)
frame1.pack(side=LEFT, expand=YES, fill=BOTH)

btn = Button(frame1, text='Button')
btn.pack()

root.mainloop()