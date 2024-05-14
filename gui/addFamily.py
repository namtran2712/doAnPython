
from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
from tkinter import simpledialog


class addFamily(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Thêm thànhh viên")
        screen_width=self.winfo_screenwidth()
        screen_height=self.winfo_screenheight()
        width=600
        height=550
        x=(screen_width-width)//2
        y=(screen_height-height)//2
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.configure(bg = "#FFFFFF")

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r".\\assets3\\frame0")
        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 500,
            width = 600,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_text(
            150.0,
            29.0,
            anchor="nw",
            text="Thêm thànhh viên",
            fill="red",
            font=("Inter Bold", 32 * -1)
        )

        entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))

        entry_bg_1 = canvas.create_image(
            364.0,
            119.5,
            image=entry_image_1
        )
        
        entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
            x=265.0,
            y=96.0,
            width=198.0,
            height=45.0
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            364.0,
            383.5,
            image=entry_image_2
        )
        entry_2 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_2.place(
            x=265.0,
            y=360.0,
            width=198.0,
            height=45.0
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = canvas.create_image(
            364.0,
            317.5,
            image=entry_image_3
        )
        entry_3 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_3.place(
            x=265.0,
            y=294.0,
            width=198.0,
            height=45.0
        )

        entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        entry_bg_4 = canvas.create_image(
            364.0,
            185.5,
            image=entry_image_4
        )
        entry_4 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_4.place(
            x=265.0,
            y=162.0,
            width=198.0,
            height=45.0
        )

        entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_5.png"))
        entry_bg_5 = canvas.create_image(
            364.0,
            251.5,
            image=entry_image_5
        )
        entry_5 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_5.place(
            x=265.0,
            y=228.0,
            width=198.0,
            height=45.0
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=241.0,
            y=443.0,
            width=135.0,
            height=39.0
        )

        canvas.create_text(
            35.0,
            105.0,
            anchor="nw",
            text="Tên thành viên",
            fill="#000000",
            font=("Inter Bold", 24 * -1)
        )

        canvas.create_text(
            35.0,
            370.0,
            anchor="nw",
            text="Ngày sinh",
            fill="#000000",
            font=("Inter Bold", 24 * -1)
        )

        canvas.create_text(
            35.0,
            300.0,
            anchor="nw",
            text="Số điện thoại",
            fill="#000000",
            font=("Inter Bold", 24 * -1)
        )

        canvas.create_text(
            35.0,
            235.0,
            anchor="nw",
            text="Password",
            fill="#000000",
            font=("Inter Bold", 24 * -1)
        )

        canvas.create_text(
            35.0,
            170.0,
            anchor="nw",
            text="UserName",
            fill="#000000",
            font=("Inter Bold", 24 * -1)
        )
        self.resizable(False, False)
        self.mainloop()


# a=addFamily()

# def showAddFamily (root):
#     dialog = tk.Toplevel (root)
#     dialog.title ("Thêm thành viên")
#     dialog.transient (root)
#     dialog.geometry ("400x400")

#     title = tk.Label (dialog, text="Thêm thành viên",foreground="RED", font=("Arial", 14))
#     title.place (relx=0.5, rely=0.5, anchor="center")
#     title.grid (row=0, column=0, padx=10, pady=10 ,sticky="nsew")

# root = tk.Tk ()
# showAddFamily (root)

# root.mainloop ()