from tkinter import *
from tkinter.ttk import *

from time import strftime

root  = Tk()
root.title(" DIGI Clock")

def time():
    string = strftime("%H:%M:%S %p")
    lable.config(text= string)
    lable.after(10000, time)

lable = Label(root, font= ("Arial", 80), foreground= "yellow", background= "black")
lable.pack(anchor= 'center')
time()

mainloop()
