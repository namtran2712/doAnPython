

from mainGUI import mainGUI
from pathlib import Path
import tkinter as tk
# from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import re
import sys
sys.path.append('E:\\Code\\Python\\Doanreal\\gui')
from signUpGUI import signUpGUI
from database import userDAO

class signIn(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Đăng nhập")
        
        screen_width=self.winfo_screenwidth()
        screen_height=self.winfo_screenheight()
        width=600
        height=550
        x=(screen_width-width)//2
        y=(screen_height-height)//2
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.configure(bg = "#370365")

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")
        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        canvas = Canvas(
            self,
            bg = "#370365",
            height = 550,
            width = 600,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            391.0,
            334.0,
            image=entry_image_1
        )
        username = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Arial-BoldMT", int(20.0)),

        )
        username.place(
            x=275.0,
            y=314.0,
            width=232.0,
            height=38.0
        )

        canvas.create_text(
            75.0,
            314.0,
            anchor="nw",
            text="Tài khoản",
            fill="#FFFFFF",
            font=("Inter Bold", 24 * -1)
        )

        canvas.create_text(
            205.0,
            253.0,
            anchor="nw",
            text="Đăng nhập",
            fill="#53D9ED",
            font=("Inter Black", 32 * -1)
        )


        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            391.0,
            395.0,
            image=entry_image_2
        )
        password = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Arial-BoldMT", int(20.0)),
            show="*"
        )
        password.place(
            x=275.0,
            y=375.0,
            width=232.0,
            height=38.0
        )

        canvas.create_text(
            79.0,
            375.0,
            anchor="nw",
            text="Mật khẩu",
            fill="#FFFFFF",
            font=("Inter Regular", 24 * -1)
        )

        def signUp():
            self.destroy()
            a=signUpGUI()

        button_sign_up = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_signUp = Button(
            image=button_sign_up,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#370365",
            command=signUp,
            relief="flat",
            cursor="hand2"
        )
        button_signUp.place(
            x=411.0,
            y=463.0,
            width=123.0,
            height=38.0
        )

        def openCamera ():
            with open('E:\\Code\\Python\\Doanreal\\Python\\cnn\\test.py', 'r') as f:
                self.destroy ()
                code = f.read()
            exec(code)

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_faceId = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#370365",
            command=  openCamera,
            relief="flat",
            cursor="hand2"
        )
        button_faceId.place(
            x=86.0,
            y=463.0,
            width=108.0,
            height=38.0
        )

        def check (user, pw):
            if (user.strip () == "" or pw.strip () == ""):
                return False, "Không được để trống"
            regex = "^[a-zA-Z0-9]+$"
            pattern = re.compile (regex)
            if re.match (pattern, user) != None and len(pw.strip ()) >= 8:
                check = userDAO.selectByUsername (user,pw)
                if (check == 1):
                    return True, "Đăng nhập thành công"
                else:
                    return False, "Kiểm tra thông tin đăng nhập"

            else:
                return False, "Kiểm tra thông tin đăng nhập"


        def signIn():
            user = username.get ()
            pw = password.get ()
            success, mess = check (user, pw)
            if (success == False):
                messagebox.showwarning ("Lỗi đăng nhập",mess)
            else:
                messagebox.showinfo ("Success",mess)
                self.destroy()
                mainpage=mainGUI(user)

        

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        
        button_signIn = Button(
            image=button_image_3,
            borderwidth=0,
            activebackground="#370365",
            highlightthickness=0,
            command=lambda: signIn(),
            relief="flat",
            cursor="hand2"
        )
        button_signIn.place(
            x=244.0,
            y=463.0,
            width=122.0,
            height=38.0
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            300.0,
            145.0,
            image=image_image_1
        )

        canvas.create_rectangle(
            73.99992610899784,
            520.4999389648438,
            534.0011029217276,
            523.0381274093105,
            fill="#FFFFFF",
            outline="")
        self.resizable(False, False)
        self.mainloop()

