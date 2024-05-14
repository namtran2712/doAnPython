import tkinter as tk
from tkinter import ttk
from tkinter import *
import ttkthemes
class chucnangPage(Frame):
    
    def __init__(self,parent):
        super().__init__(parent)
        self.place(x=0, y=0, width=1100, height=550) 
        self.config (bg="white")        
        self.is_on = True  
      
        global current_row
        global current_column
        current_row = 2
        current_column = 0

        title = tk.Label (self, font=("Arial",30),text="Điều khiển thiết bị" ,bg="RED", fg="WHITE",width=50)
        title.pack ()

        table = ttk.Treeview (self)
        table.tag_configure ("odd",background="blue",foreground="white")

        table["columns"]= ("Thiết bị","Trạng thái")
        table.heading ("Thiết bị",text="Thiết bị")
        table.heading ("Trạng thái",text="Trạng thái")

        table.insert("", tk.END, values=("Đèn", "30"),tags=("odd",))

        # buttonStatus = tk.Button (self,text="Đang hoạt động")        
        table.insert("", tk.END, values=("Bob", "35"))

        table.column("Thiết bị", width=100,anchor="center")
        table.column("Trạng thái", width=50,anchor="center")

        table.columnconfigure ("all", pad= 10)

        # style table
        style= ttkthemes.ThemedStyle(self)
        style.theme_use("clam")
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Helvetica", 25),background="#FFC1C1")  
        style.configure("Treeview", font=("Helvetica", 18)) 
        style.configure("Treeview", rowheight=30)
        table.column("#0", width=0, stretch=tk.NO)  
        table.pack(expand=True, fill=tk.BOTH)


   
root=tk.Tk()
root.geometry("1100x550")

a=chucnangPage(root)
root.mainloop()

