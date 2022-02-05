# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 21:16:51 2020

@author: HERVE NG
"""

from tkinter import *
from tkinter import filedialog
import os 
import tkinter as tk
from PIL import Image, ImageTk # importing the image library
import tensorflow as tf



def showimage():
    file = filedialog.askopenfilename(initialdir=os.getcwd(),
                                     title="Select Image File",
                                     filetypes=(("JPG File", "*.jpg"),
                                                ("PNG File", "*.png"),
                                                ("All Files", "*.*")))
    img = Image.open(file)
    img.thumbnail((350,350))
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img
    

def exit():
    root.destroy()
root = Tk()

frm = Frame(root)
frm.pack(side=BOTTOM, padx=15, pady=15)

lbl = Label(root)
lbl.pack()

btn = Button(frm, text="Browse Image", command=showimage)
btn.pack(side=tk.LEFT)

btn2 = Button(frm, text="Exit", command=exit)
btn2.pack(side=tk.LEFT, padx=10)

root.title("Classification of Painting styles Using CNN and SVM pipelines")
root.geometry("300x350")
root.mainloop()
