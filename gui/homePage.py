import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk

class homePage(tk.Frame):
    def __init__(self,parent):
        img_home=ImageTk.PhotoImage(Image.open("img2.png"))
        super().__init__(parent)                    
        self.place(x=0,y=0,height=550,width=1100)

        lb=tk.Label(self,image=img_home)
        lb.image=img_home
        lb.pack()
        label =tk.Label(self,text="abcd",anchor=tk.NW)
        label.pack()
    