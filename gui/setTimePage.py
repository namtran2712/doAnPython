import tkinter as tk
from tkinter import ttk 
import numpy as np
import ttkthemes


class setTimePage(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.place(x=0,y=0,height=550,width=1100)
        self.config()
        lb_title=tk.Label(self,text="Hẹn giờ thiết bị",fg="red",font=("bold",30))
        lb_device=tk.Label(self,text="Danh sách thiết bị",fg="pink",font=("bold",20))
        lb_time=tk.Label(self,text="Danh sách hẹn giờ",fg="#800000",font=("bold",20))
        device_fm=tk.Frame(self,bd=0,highlightbackground="black", highlightcolor="black", highlightthickness=1,bg="white")
        time_fm=tk.Frame(self,bd=0,highlightbackground="black", highlightcolor="black", highlightthickness=1,bg="white")

        def set_time(id,name):

            def colapse():
                set_time_fm.destroy()
                self.update()

            set_time_fm=tk.Frame(self,relief='solid', bd=2,background="white")
            lbTitle=tk.Label(set_time_fm,text="Hẹn giờ",font=("bold",25),fg="red",bg="white")
            btnClose=tk.Button(set_time_fm,text="X",font=("bold",20),bg="red",activebackground="#800000",fg="white",bd=0,command=colapse,cursor="hand2")
            lbName=tk.Label(set_time_fm,text="Tên thiết bị :",font=("bold",15),bg="white")
            # lbPort=tk.Label(set_time_fm,text="Port :",font=("bold",15),bg="white")
            etName=tk.Entry(set_time_fm,font=("italic",15),highlightbackground="black", highlightcolor="black", highlightthickness=1,bg="white")
            # etPort=tk.Entry(set_time_fm,font=("italic",15),highlightbackground="black", highlightcolor="black", highlightthickness=1,bg="white")
            lbTime=tk.Label(set_time_fm,text="Thời gian",font=("bold",15),bg="white")
            etHour=tk.Entry(set_time_fm,font=("bold",25),highlightbackground="black", highlightcolor="black", highlightthickness=1,bg="white")
            lbMid=tk.Label(set_time_fm,text=":",font=("bold",25),bg="white")
            etMinute=tk.Entry(set_time_fm,font=("bold",25),highlightbackground="black", highlightcolor="black", highlightthickness=1,bg="white")
            btnAdd=tk.Button(set_time_fm,text="Hẹn giờ",font=("bold",15),bd=0,activebackground="#800000",fg="white",highlightbackground="white", highlightcolor="white", highlightthickness=1,bg="pink")
            etHour.insert(0,"00")
            etMinute.insert(0,"00")
            var1 = tk.IntVar()
            varAll = tk.IntVar()
            lbLoop=tk.Label(set_time_fm,text="Lặp lại :",font=("bold",15),bg="white")
            lbCheck1=tk.Label(set_time_fm,text="Chỉ một lần :",font=("",10),bg="white")
            lbCheckAll=tk.Label(set_time_fm,text="Mỗi ngày :",font=("",10),bg="white")
            def checking1():

                if var1.get()==1:
                    if varAll.get()==1:
                        var1.set(0)

            def checkingAll():

                if varAll.get()==1:
                    if var1.get()==1:
                        varAll.set(0)

            check1=tk.Checkbutton(set_time_fm,text="",variable=var1,bg="white",font=("bold",15),activebackground="white",
                                  command=checkingAll)
            checkAll=tk.Checkbutton(set_time_fm,text="",variable=varAll,bg="white",font=("bold",15),activebackground="white",
                                    command=checking1)


            lbTitle.place(x=180,y=20,width=150,height=40)
            lbName.place(x=30,y=80,width=400,height=30)
            etName.place(x=40,y=110,width=400,height=30)
            # lbPort.place(x=250,y=80,width=200,height=30)
            # etPort.place(x=260,y=110,width=200,height=30)
            lbTime.place(x=200,y=140,width=100,height=30)
            etHour.place(x=150,y=180,width=80,height=80)
            lbMid.place(x=240,y=180,width=20,height=80)
            etMinute.place(x=270,y=180,width=80,height=80)
            lbLoop.place(x=30,y=280,width=100,height=30)
            lbCheck1.place(x=140,y=280,width=100,height=30)
            check1.place(x=250,y=285,width=20,height=20)
            lbCheckAll.place(x=280,y=280,width=100,height=30)
            checkAll.place(x=390,y=285,width=20,height=20)
            
            btnClose.place(x=465,y=2,width=30,height=30)
            btnAdd.place(x=200,y=340,width=100,height=30)
            set_time_fm.place(x=300,y=80,width=500,height=400)
        canvas = tk.Canvas(device_fm)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = tk.Scrollbar(device_fm, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)
        frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor=tk.NW)

        from database import deviceDAO
        result = deviceDAO.selectAll ()
        data = []
        for device in result:
            l = []
            l.append (device[0])
            l.append (device[1])
            l.append (device[2])
            l.append (device[3])
            l.append (device[4])
            data.append (l)

        # Tao item
        for dt in data:
            panel = tk.Frame (frame,width=400,height=60)
            lb=tk.Label(panel,text=dt[1] + " " + dt[4],font=("italic",15))
            btn = tk.Button (panel,text="Hẹn giờ",font=("italic",15),fg="white",background="pink",activebackground="red",bd=0,command=set_time (id=dt[0],name=dt[1]),cursor="hand2")
            lb.place(x=50,y=5,width=150,height=50)
            btn.place(x=260,y=10,width=100,height=40)
            panel.pack (side=tk.TOP ,fill=tk.X, padx=5, pady=5)

        frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        canvas2 = tk.Canvas(time_fm)
        canvas2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar2 = tk.Scrollbar(time_fm, orient=tk.VERTICAL, command=canvas2.yview)
        scrollbar2.pack(side=tk.RIGHT, fill=tk.Y)
        canvas2.configure(yscrollcommand=scrollbar2.set)
        frame2 = tk.Frame(canvas2)
        canvas2.create_window((0, 0), window=frame2, anchor=tk.NW)


        from database import listTimeDAO
        result = listTimeDAO.selectAll ()

        # Tao item
        for rs in result:
            print (rs)
            div = tk.Frame (frame2,width=400,height=60)
            lbName=tk.Label(div,text=rs[1],font=("italic",15))
            lbTime=tk.Label(div,text=str(rs[6]) + ":" + str(rs[7]),font=("italic",15))
            btnDelete = tk.Button (div,text="Xóa",font=("italic",10),fg="white",background="pink",activebackground="red",bd=0,cursor="hand2")
            btnUpdate = tk.Button (div,text="Sửa",font=("italic",10),fg="white",background="pink",activebackground="red",bd=0,cursor="hand2")
            lbName.place(x=20,y=5,width=150,height=50)
            lbTime.place(x=185,y=5,width=80,height=50)
            btnUpdate.place(x=300,y=5,width=100,height=20)
            btnDelete.place(x=300,y=35,width=100,height=20)

            div.pack (side=tk.TOP ,fill=tk.X, padx=5, pady=5)
        frame2.update_idletasks()
        canvas2.config(scrollregion=canvas2.bbox("all"))


        lb_title.place(x=400,y=0,width=300,height=50)
        lb_device.place(x=150,y=80,width=250,height=40)
        lb_time.place(x=680,y=80,width=250,height=40)
        device_fm.place(x=70,y=120,width=450,height=340)
        time_fm.place(x=570,y=120,width=450,height=340)
        
