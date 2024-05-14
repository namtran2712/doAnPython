import tkinter as tk
from tkinter import END, ttk
import numpy as np
import ttkthemes
from database import deviceDAO
from database import userDAO
from database import portDao
from database import *
from tkinter import messagebox

class devicePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, y=0, height=550, width=1100)

        lb = tk.Label(
            self,
            text="Danh sách thiết bị",
            font=("bold", 30),
            fg="orange",
            anchor=tk.NW,
        )
        lb.pack()
        style = ttkthemes.ThemedStyle(self)
        style.theme_use("clam")
        style.configure("Treeview", font=("Verdana", 12), cellpadding=50)
        style.configure(
            "Treeview.Heading",
            font=("bold", 20),
            foreground="red",
            background="#FFC1C1",
        )
        tree = ttk.Treeview(
            self,
            columns=(
                "STT",
                "ID",
                "Tên thiết bị",
                "Loại",
                "Trạng thái",
                "Vị trí",
                "Cổng",
            ),
            height=100,
        )
        tree.column("#0", width=0, stretch=tk.NO)
        tree.heading("STT", text="STT")
        tree.heading("ID", text="ID")
        tree.heading("Tên thiết bị", text="Tên thiết bị")
        tree.heading("Loại", text="Loại")
        tree.heading("Trạng thái", text="Status")
        tree.heading("Vị trí", text="Vị trí")
        tree.heading("Cổng", text="Cổng")

        tree.column("STT", width=80, anchor=tk.CENTER)
        tree.column("ID", width=80, anchor=tk.CENTER)
        tree.column("Tên thiết bị", width=250, anchor=tk.CENTER)
        tree.column("Loại", width=160, anchor=tk.CENTER)
        tree.column("Trạng thái", width=120, anchor=tk.CENTER)
        tree.column("Vị trí", width=100, anchor=tk.CENTER)
        tree.column("Cổng", width=80, anchor=tk.CENTER)

        tree.columnconfigure("all", pady=10)

        yscrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)

        yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tree.configure(yscrollcommand=yscrollbar.set)

        def showData():
            nodeChild = tree.get_children()
            for item in nodeChild:
                tree.delete(item)
            listDevice = deviceDAO.selectAll()

            data = []
            i = 1   

            for device in listDevice:
                l = []
                l.append(i)
                l.append(device[0])
                l.append(device[1])
                l.append(device[2])
                l.append(device[3])
                l.append(device[4])
                listport = portDao.selectByDevice(device[0])
                print (listport)
                s = []
                for port in listport:
                    s.append(port[0])

                i += 1
                l.append(s)
                data.append(l)
            
            for row in data:
                tree.insert("", tk.END, values=row)

            tree.pack()

        showData()

        def delete():
            selected_node = tree.selection()[0]
            item = int(tree.item(selected_node)["values"][1])
            deviceDAO.deleteDevice (item)
            self.update()
            showData()

        def add():

            # def validate_birthdate(text):
            #     try:
            #         datetime.strptime(text, "%Y-%m-%d")
            #         return True
            #     except ValueError:
            #         return False

            # def validate_phone(text):
            #     if len(text) != 10 or not text.isdigit():
            #         return False
            #     return True
            # def focus_out_birthdate(event):
            #     if not validate_birthdate(etBirthday.get()):
            #         etBirthday.config(highlightbackground="red")

            # def focus_out_phone(event):
            def addCollapse():
                addFrame.destroy()
                self.update()

            def insertDevice():
                import validate  
                nameDevice = etName.get()
                location = etLocation.get()
                typeDevice = etType.get()
                port = etPort.get()
                if (validate.checkEmpty (nameDevice) or
                    validate.checkEmpty (location) or
                    validate.checkEmpty (typeDevice) or
                    validate.checkEmpty (port) ):
                    messagebox.showwarning ("error","Vui lòng nhập đầy đủ thông tin")
                else:
                    if validate.checkPort (port):
                        listPort =port.split (" ")
                        deviceDAO.insertDevice (nameDevice,location,typeDevice,listPort)
                        showData()
                    else :
                        messagebox.showwarning ("error", "Lỗi port")
                   
            addFrame = tk.Frame(self, relief="solid", bd=2, background="white")
            btnClose = tk.Button(
                addFrame,
                text="X",
                font=("bold", 15),
                background="red",
                bd=0,
                activebackground="#800000",
                fg="white",
                highlightbackground="white",
                highlightcolor="white",
                highlightthickness=1,
                command=addCollapse,
            )
            lbTitleAdd = tk.Label(
                addFrame,
                text="Thêm thiết bị",
                font=("bold", 30),
                fg="red",
                anchor=tk.NW,
                background="white",
                bd=0,
            )
            lbName = tk.Label(
                addFrame,
                text="Tên thiết bị :",
                font=("bold", 15),
                fg="#800000",
                anchor=tk.NW,
                background="white",
            )
            lbType = tk.Label(
                addFrame,
                text="Loại :",
                font=("bold", 15),
                fg="#800000",
                anchor=tk.NW,
                background="white",
            )
            lbStatus = tk.Label(
                addFrame,
                text="Vị trí :",
                font=("bold", 15),
                fg="#800000",
                anchor=tk.NW,
                background="white",
            )
            lbPort = tk.Label(
                addFrame,
                text="Cổng :",
                font=("bold", 15),
                fg="#800000",
                anchor=tk.NW,
                background="white",
            )

            etName = tk.Entry(
                addFrame,
                highlightbackground="black",
                highlightcolor="black",
                highlightthickness=1,
                font=("bold", 15),
            )
            etType = tk.Entry(
                addFrame,
                highlightbackground="black",
                highlightcolor="black",
                highlightthickness=1,
                font=("bold", 15),
            )
            etLocation = tk.Entry(
                addFrame,
                highlightbackground="black",
                highlightcolor="black",
                highlightthickness=1,
                font=("bold", 15),
            )
            etPort = tk.Entry(
                addFrame,
                validate="key",
                highlightbackground="black",
                highlightcolor="black",
                highlightthickness=1,
                font=("bold", 15),
            )

            btnAdd = tk.Button(
                addFrame,
                text="Thêm",
                font=("bold", 20),
                background="red",
                bd=0,
                activebackground="#800000",
                fg="white",
                highlightbackground="white",
                highlightcolor="white",
                highlightthickness=1,
                bg="red",
                command=insertDevice,
            )
            # etBirthday.bind("<FocusOut>", focus_out_birthdate)

            btnClose.place(x=560, y=1, width=35, height=37)
            lbTitleAdd.place(x=170, y=75, width=300, height=60)
            lbName.place(x=100, y=150, width=150, height=30)
            lbType.place(x=100, y=200, width=150, height=30)
            lbStatus.place(x=100, y=250, width=150, height=30)
            lbPort.place(x=100, y=300, width=150, height=30)

            etName.place(x=250, y=150, width=250, height=30)
            etType.place(x=250, y=200, width=250, height=30)
            etLocation.place(x=250, y=250, width=250, height=30)
            etPort.place(x=250, y=300, width=250, height=30)

            btnAdd.place(x=250, y=380, width=100, height=40)
            addFrame.place(x=250, y=0, width=600, height=500)
        def setValue (entry ,value):
            entry.delete (0,END)
            entry.insert (0,value)
        def update():
           
            def addCollapse():
                addFrame.destroy()
                self.update()

            addFrame = tk.Frame(self, relief="solid", bd=2, background="white")
            btnClose = tk.Button(
                addFrame,
                text="X",
                font=("bold", 15),
                background="red",
                bd=0,
                activebackground="#800000",
                fg="white",
                highlightbackground="white",
                highlightcolor="white",
                highlightthickness=1,
                command=addCollapse,
            )
            lbTitleAdd = tk.Label(
                addFrame,
                text="Sửa thiết bị",
                font=("bold", 30),
                fg="red",
                anchor=tk.NW,
                background="white",
                bd=0,
            )
            lbName = tk.Label(
                addFrame,
                text="Tên thiết bị :",
                font=("bold", 15),
                fg="#800000",
                anchor=tk.NW,
                background="white",
            )
            lbType = tk.Label(
                addFrame,
                text="Loại :",
                font=("bold", 15),
                fg="#800000",
                anchor=tk.NW,
                background="white",
            )
            lbPosition = tk.Label(
                addFrame,
                text="Vị trí :",
                font=("bold", 15),
                fg="#800000",
                anchor=tk.NW,
                background="white",
            )
            lbPort = tk.Label(
                addFrame,
                text="Cổng :",
                font=("bold", 15),
                fg="#800000",
                anchor=tk.NW,
                background="white",
            )

            etName = tk.Entry(
                addFrame,
                highlightbackground="black",
                highlightcolor="black",
                highlightthickness=1,
                font=("bold", 15),
                
            )
            etType = tk.Entry(
                addFrame,
                highlightbackground="black",
                highlightcolor="black",
                highlightthickness=1,
                font=("bold", 15),
            )
            etPosition = tk.Entry(
                addFrame,
                highlightbackground="black",
                highlightcolor="black",
                highlightthickness=1,
                font=("bold", 15),
            )
            etPort = tk.Entry(
                addFrame,
                validate="key",
                highlightbackground="black",
                highlightcolor="black",
                highlightthickness=1,
                font=("bold", 15),
            )

            def updateDevice ():
                import validate  
                nameDevice = etName.get()
                location = etPosition.get()
                typeDevice = etType.get()
                port = etPort.get()
                if (validate.checkEmpty (nameDevice) or
                    validate.checkEmpty (location) or
                    validate.checkEmpty (typeDevice) or
                    validate.checkEmpty (port) ):
                    messagebox.showwarning ("error","Vui lòng nhập đầy đủ thông tin")
                else:
                    if validate.checkPort (port):
                        listPort =port.split (" ")
                        deviceDAO.update (item,nameDevice,location,typeDevice,listPort)
                        showData()
                    else :
                        messagebox.showwarning ("error", "Lỗi port")


            btnAdd = tk.Button(
                addFrame,
                text="Sửa",
                font=("bold", 20),
                bd=0,
                activebackground="#800000",
                fg="white",
                highlightbackground="white",
                highlightcolor="white",
                highlightthickness=1,
                bg="pink",
                command= updateDevice 
            )
            # etBirthday.bind("<FocusOut>", focus_out_birthdate)

            btnClose.place(x=560, y=1, width=35, height=37)
            lbTitleAdd.place(x=175, y=50, width=300, height=60)
            lbName.place(x=100, y=150, width=150, height=30)
            lbType.place(x=100, y=200, width=150, height=30)
            lbPosition.place(x=100, y=250, width=150, height=30)
            lbPort.place(x=100, y=300, width=150, height=30)

            etName.place(x=250, y=150, width=250, height=30)
            etType.place(x=250, y=200, width=250, height=30)
            etPosition.place(x=250, y=250, width=250, height=30)
            etPort.place(x=250, y=300, width=250, height=30)

            btnAdd.place(x=225, y=380, width=150, height=40)
            addFrame.place(x=250, y=0, width=600, height=500)

            selected_node = tree.selection()[0]
            item = int(tree.item(selected_node)["values"][1])
            result =deviceDAO.selectDeviceById (item)
            print (result)
            setValue (etName,result[0][1])  
            setValue (etType,result[0][2])
            setValue (etPosition,result[0][4])
            ports = ""
            for port in result :
                ports+=  str (port[6]) +" "
            setValue (etPort,ports.strip())

        menu_frame = tk.Frame(self)

        add_btn = tk.Button(
            menu_frame,
            text="Thêm",
            bg="#00FF00",
            fg="white",
            font=("bold", 20),
            activebackground="green",
            bd=1,
            command=add,
        )
        delete_btn = tk.Button(
            menu_frame,
            text="Xóa",
            bg="#FFFF00",
            fg="white",
            font=("bold", 20),
            activebackground="#808000",
            bd=1,
            command=delete,
        )
        update_btn = tk.Button(
            menu_frame,
            text="Sửa",
            bg="#800000",
            fg="white",
            font=("bold", 20),
            activebackground="red",
            bd=1,
            command=update,
        )

        add_btn.place(x=0, y=0, width=80, height=50)
        update_btn.place(x=0, y=60, width=80, height=50)
        delete_btn.place(x=0, y=120, width=80, height=50)

        menu_frame.place(x=990, y=100, width=80, height=180)
