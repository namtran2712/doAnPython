import tkinter as tk
from tkinter import ttk 
import numpy as np
import ttkthemes
from tkinter import messagebox
from datetime import datetime
import sys
sys.path.append('E:\\Code\\Python\\Doanreal')
from database import userDAO

class familyPage(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.place(x=0,y=0,height=550,width=1100)

        lb=tk.Label(self,text="Danh sách thành viên",font=("bold",30),fg="red",anchor=tk.NW)
        lb.pack()
        style= ttkthemes.ThemedStyle(self)
        style.theme_use("clam")
        style.configure("Treeview",font=("Verdana",12),cellpadding=50)
        style.configure("Treeview.Heading",font=("bold",15),foreground="red",background="#FFC1C1")
        tree = ttk.Treeview(self, columns=("STT","ID", "Tên thành viên","Tài khoản","Mật khẩu","Ngày sinh","Số điện thoại"),height=100)
        tree.column("#0", width=0, stretch=tk.NO)
        tree.heading("STT", text="STT")
        tree.heading("ID", text="ID")
        tree.heading("Tên thành viên", text="Tên thành viên")
        tree.heading("Tài khoản", text="Tài khoản")
        tree.heading("Mật khẩu", text="Mật khẩu")
        tree.heading("Ngày sinh", text="Ngày sinh")
        tree.heading("Số điện thoại", text="Số điện thoại")

        tree.column("STT",width=50,anchor=tk.CENTER)
        tree.column("ID", width=80,anchor=tk.CENTER)
        tree.column("Tên thành viên", width=200,anchor=tk.CENTER)
        tree.column("Tài khoản", width=150,anchor=tk.CENTER)
        tree.column("Mật khẩu", width=130,anchor=tk.CENTER)
        tree.column("Ngày sinh", width=130,anchor=tk.CENTER)
        tree.column("Số điện thoại", width=140,anchor=tk.CENTER)

        tree.columnconfigure("all",pady=10)

        yscrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)

        yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tree.configure(yscrollcommand=yscrollbar.set)

        def showData ():
            nodeChild = tree.get_children ()
            for item in nodeChild:
                tree.delete (item)
            userData = userDAO.selectAll ()
            data = []
            i = 1
            for user in userData:
                l = []
                l.append (i)
                l.append (user[0])
                l.append (user[1])
                l.append (user[4])
                l.append (user[5])
                l.append (user[2])
                l.append (user[3])
                i+=1
                data.append (l)


            for row in data:
                tree.insert("", tk.END, values=row)

            tree.pack()
        
        showData ()

        
        def delete ():
            selected_node = tree.selection ()[0]
            item = int (tree.item (selected_node)["values"][1])
            userDAO.delete (item)
            self.update()
            showData ()

        
        def add():

            def validate_birthdate(text):
                try:
                    datetime.strptime(text, "%Y-%m-%d")
                    return True
                except ValueError:
                    return False

            def validate_phone(text):
                if len(text) != 10 or not text.isdigit():
                    return False
                return True
            def focus_out_birthdate(event):
                if not validate_birthdate(etBirthday.get()):
                    etBirthday.config(highlightbackground="red")

            def focus_out_phone(event):
                if not validate_phone(etPhone.get()):
                    etPhone.config(highlightbackground="red")
            def addCollapse():
                addFrame.destroy()
                self.update()

            addFrame=tk.Frame(self,relief='solid', bd=2,background="white")
            btnClose=tk.Button(addFrame,text="X",font=("bold",15),background="red",bd=0,activebackground="#800000",fg="white",highlightbackground="white", highlightcolor="white", highlightthickness=1,command=addCollapse)
            lbTitleAdd=tk.Label(addFrame,text="Thêm thành viên",font=("bold",30),fg="red",anchor=tk.NW,background="white",bd=0)
            lbName=tk.Label(addFrame,text="Họ và tên :",font=("bold",15),fg="#800000",anchor=tk.NW,background="white")
            lbUsername=tk.Label(addFrame,text="Username :",font=("bold",15),fg="#800000",anchor=tk.NW,background="white")
            lbPass=tk.Label(addFrame,text="Password :",font=("bold",15),fg="#800000",anchor=tk.NW,background="white")
            lbBirthday=tk.Label(addFrame,text="Ngày sinh :",font=("bold",15),fg="#800000",anchor=tk.NW,background="white")
            lbPhone=tk.Label(addFrame,text="Số điện thoại :",font=("bold",15),fg="#800000",anchor=tk.NW,background="white")

            etName=tk.Entry(addFrame, highlightbackground="black", highlightcolor="black", highlightthickness=1,font=("bold",15))
            etUsername=tk.Entry(addFrame, highlightbackground="black", highlightcolor="black", highlightthickness=1,font=("bold",15))
            etPass=tk.Entry(addFrame, highlightbackground="black", highlightcolor="black", highlightthickness=1,font=("bold",15))
            etBirthday=tk.Entry(addFrame,validate="key",validatecommand=(validate_birthdate,"%P"), highlightbackground="black", highlightcolor="black", highlightthickness=1,font=("bold",15))
            etPhone=tk.Entry(addFrame,validate="key",validatecommand=(validate_phone,"%P"), highlightbackground="black", highlightcolor="black", highlightthickness=1,font=("bold",15))

            btnAdd=tk.Button(addFrame,text="Thêm",font=("bold",20),background="red",bd=0,activebackground="#800000",fg="white",highlightbackground="white", highlightcolor="white", highlightthickness=1,bg="red")
            etBirthday.bind("<FocusOut>", focus_out_birthdate)
            etPhone.bind("<FocusOut>", focus_out_phone)

            btnClose.place(x=560,y=1,width=35,height=37)
            lbTitleAdd.place(x=150,y=75,width=300,height=60)
            lbName.place(x=100,y=150,width=150,height=30)
            lbUsername.place(x=100,y=200,width=150,height=30)
            lbPass.place(x=100,y=250,width=150,height=30)
            lbBirthday.place(x=100,y=300,width=150,height=30)
            lbPhone.place(x=100,y=350,width=150,height=30)

            etName.place(x=250,y=150,width=250,height=30)
            etUsername.place(x=250,y=200,width=250,height=30)
            etPass.place(x=250,y=250,width=250,height=30)
            etBirthday.place(x=250,y=300,width=250,height=30)
            etPhone.place(x=250,y=350,width=250,height=30)

            btnAdd.place(x=250,y=420,width=100,height=40)
            addFrame.place(x=250,y=0,width=600,height=500)

        def update():
            selected_node = tree.selection ()[0]
            item = int (tree.item (selected_node)["values"][1])
            user = userDAO.selectByID (item)

            def addCollapse():
                addFrame.destroy()
                self.update()

            def setVal(entry, value):
                entry.delete(0, tk.END)
                entry.insert(0, value)  
               
                showData ()
            def updateValue():
                import validate
                name = etName.get ()
                username = etUsername.get()
                password = etPass.get ()
                birthday = etBirthday.get ()
                phone = etPhone.get ()
                
                if (validate.checkEmpty (name) or
                    validate.checkEmpty (username) or
                    validate.checkEmpty (password) or
                    validate.checkEmpty (birthday) or
                    validate.checkEmpty (phone)):
                    messagebox.showinfo("Thông báo", "Vui lòng không để trống thông tin!")
                else:
                    if (
                        validate.checkName(name) and
                        validate.checkBirthday(birthday) and
                        validate.checkPhone(phone)):
                        if (userDAO.checkMatchPhone (phone,user[0][0])==False):
                            userDAO.update (name, birthday, phone,user[0][0])
                            addCollapse()
                            showData ()
                        else :
                            messagebox.showerror("Error", "Số điện thoại đã tồn tại")
                    else:
                        messagebox.showinfo("Thông báo", "Thông tin nhập không hợp lệ!")

            addFrame=tk.Frame(self,relief='solid', bd=2,background="white")

            etName=tk.Entry(addFrame, highlightbackground="black", highlightcolor="black", highlightthickness=1,font=("bold",15))
            etUsername=tk.Entry(addFrame , highlightbackground="black", highlightcolor="black", highlightthickness=1,font=("bold",15))
            etPass=tk.Entry(addFrame, highlightbackground="black", highlightcolor="black", highlightthickness=1,font=("bold",15))
            etBirthday=tk.Entry(addFrame,validate="key", highlightbackground="black", highlightcolor="black", highlightthickness=1,font=("bold",15))
            etPhone=tk.Entry(addFrame,validate="key", highlightbackground="black", highlightcolor="black", highlightthickness=1,font=("bold",15))



            setVal (etName, user[0][1])
            setVal (etBirthday, user[0][2])
            setVal (etPhone, user[0][3])
            setVal (etUsername, user[0][4])
            setVal (etPass, user[0][5])

            btnClose=tk.Button(addFrame,text="X",font=("bold",15),background="red",bd=0,activebackground="#800000",fg="white",highlightbackground="white", highlightcolor="white", highlightthickness=1,command=addCollapse)
            lbTitleAdd=tk.Label(addFrame,text="Sửa thành viên",font=("bold",30),fg="red",anchor=tk.NW,background="white",bd=0)
            lbName=tk.Label(addFrame,text="Họ và tên :",font=("bold",15),fg="#800000",anchor=tk.NW,background="white")
            lbUsername=tk.Label(addFrame,text="Username :",font=("bold",15),fg="#800000",anchor=tk.NW,background="white")
            lbPass=tk.Label(addFrame,text="Password :",font=("bold",15),fg="#800000",anchor=tk.NW,background="white")
            lbBirthday=tk.Label(addFrame,text="Ngày sinh :",font=("bold",15),fg="#800000",anchor=tk.NW,background="white")
            lbPhone=tk.Label(addFrame,text="Số điện thoại :",font=("bold",15),fg="#800000",anchor=tk.NW,background="white")


            btnAdd=tk.Button(addFrame,text="Sửa",font=("bold",20),bd=0,activebackground="#800000",fg="white",highlightbackground="white", highlightcolor="white", highlightthickness=1,bg="pink"
                             ,command=updateValue)
            # etBirthday.bind("<FocusOut>", focus_out_birthdate)
            # etPhone.bind("<FocusOut>", focus_out_phone)

            btnClose.place(x=560,y=1,width=35,height=37)
            lbTitleAdd.place(x=150,y=75,width=300,height=60)
            lbName.place(x=100,y=150,width=150,height=30)
            lbUsername.place(x=100,y=200,width=150,height=30)
            lbPass.place(x=100,y=250,width=150,height=30)
            lbBirthday.place(x=100,y=300,width=150,height=30)
            lbPhone.place(x=100,y=350,width=150,height=30)

            etName.place(x=250,y=150,width=250,height=30)
            etUsername.place(x=250,y=200,width=250,height=30)
            etPass.place(x=250,y=250,width=250,height=30)
            etBirthday.place(x=250,y=300,width=250,height=30)
            etPhone.place(x=250,y=350,width=250,height=30)

            btnAdd.place(x=250,y=420,width=100,height=40)
            addFrame.place(x=250,y=0,width=600,height=500)


        menu_frame=tk.Frame(self)
        
        add_btn=tk.Button(menu_frame,text="Thêm",bg="#00FF00",fg="white",font=("bold",20),
                          activebackground="green",bd=1,command=add)
        delete_btn=tk.Button(menu_frame,text="Xóa",bg="#FFFF00",fg="white",font=("bold",20),
                          activebackground="#808000",bd=1, command=delete)
        update_btn=tk.Button(menu_frame,text="Sửa",bg="#800000",fg="white",font=("bold",20),
                          activebackground="red",bd=1,command=update)
        # add_btn.place(x=0,y=0,width=80,height=50)
        update_btn.place(x=0,y=60,width=80,height=50)
        delete_btn.place(x=0,y=120,width=80,height=50)

        menu_frame.place(x=990,y=100,width=80,height=180)


    