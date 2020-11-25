# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 18:49:31 2020

@author: Admin

Tkinter - FCC
"""

from tkinter import *
from style import *
import os
import random
import time

def get_Files():
    files = os.listdir('E:\Music')
    return files

def play_Music():
    music = get_Files()
    shuff_music = random.choice(music)
    shuff_music_path = os.path.join('E:\Music', shuff_music)
    os.startfile(shuff_music_path)
    pass


#Create a basic window
root = Tk()
root.configure(bg=blue)
root.geometry("480x320")


title = Label(root, text="Better Than iTunes", fg=yellow, bg=blue, font=(font_type, 18))
title.pack()

secondary_title = Label(root, text="Click the button to find out why!", fg=yellow, bg=blue, 
                        font=(font_type, 18))
secondary_title.pack()

btn = Button(
        root, text="Play",
        fg=yellow, bg=blue, 
        command = play_Music,
        font=(font_type, 18)
        ) 
btn.pack(side=BOTTOM)


#Opens the main window
root.mainloop()
