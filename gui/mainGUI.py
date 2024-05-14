import tkinter as tk
from PIL import Image,ImageTk
from homePage import homePage
from familyPage import familyPage
from devicePage import devicePage
from chucnangPage import chucnangPage
from setTimePage import setTimePage
# import Python.speak
# with open('E:\\Code\\Python\\Doanreal\\Python\\speak\\speaking.py', 'r') as f:
#     code = f.read()
# exec(code)

class mainGUI(tk.Tk):
    def __init__(self, username):
        print (username)
        super().__init__()
        self.title("Trang chu") 
        screen_width=self.winfo_screenwidth()
        screen_height=self.winfo_screenheight()
        x=(screen_width-1100)//2
        y=(screen_height-600)//2
        width=1100
        height=600
        self.geometry(f"{width}x{height}+{x}+{y}")
        def switch(page):
            
            for child in main_frame.winfo_children():
                child.destroy()
                self.update()
            page()
            
        def home_page():
            home = homePage(main_frame)
            # Python.speak.Assigment()
            
            self.update()
            
        def tool_page():

            tool = chucnangPage (main_frame)
            self.update()

            

        def infor_page():
            toggle_info_fm=tk.Frame(main_frame,highlightbackground="white",highlightthickness=2,bg="#000000")
            toggle_info_fm.place(x=0,y=0,height=550,width=1100)

            lb=tk.Label(toggle_info_fm,text="info page")
            lb.pack()

            self.update()
        def family_page():
            family = familyPage(main_frame)
            self.update()

        def device_page():
                                                   
            device=devicePage(main_frame)
            self.update()

        def setTime_page():
                                                   
            a= setTimePage(main_frame)

            self.update()

        
        def account_page():
                                                   
            toggle_account_fm=tk.Frame(main_frame,highlightbackground="white",highlightthickness=2,bg="#000000")
            toggle_account_fm.place(x=0,y=0,height=550,width=1100)

            lb=tk.Label(toggle_account_fm,text="account page")
            lb.pack()

            self.update()

        

        def toggle_menu():

            def toggle_menu_colapse():
                toggle_menu_fm.destroy()
                toggle_btn.config(text="≡")
                toggle_btn.config(command=toggle_menu)
            def change(indicator):
                for child in toggle_menu_fm.winfo_children():
                    if isinstance(child,tk.Button):
                        child['fg']='white'

                indicator['fg']="#FF0099"
            def logout ():
                self.destroy()
                a=signIn()
            toggle_menu_fm = tk.Frame(self,bg="#FFC1C1", highlightbackground="white",
                                    highlightthickness=2)
            toggle_menu_fm.place(x=0,y=50,height=1050,width=200)
            toggle_btn.config(text="X")
            toggle_btn.config(command=toggle_menu_colapse)

            home_btn =tk.Button(toggle_menu_fm,text="Trang chủ",font=("Bold",25),bd=0,background='#FFC1C1',fg="white",cursor="hand2",
                                activebackground='#FFC1C1',activeforeground="#FF0099",command=lambda: [switch(page=home_page),change(home_btn),toggle_menu_colapse()])
            home_btn.place(x=10,y=20)
            tool_btn =tk.Button(toggle_menu_fm,text="Chức năng",font=("Bold",25),bd=0,background='#FFC1C1',fg="white",cursor="hand2",
                                activebackground='#FFC1C1',activeforeground="#FF0099",command=lambda: [switch(page=tool_page),change(tool_btn),toggle_menu_colapse()])
            tool_btn.place(x=10,y=80)
            in4_btn =tk.Button(toggle_menu_fm,text="Thông tin",font=("Bold",25),bd=0,background='#FFC1C1',fg="white",cursor="hand2",
                                activebackground='#FFC1C1',activeforeground="#FF0099",command=lambda: [switch(page=infor_page),change(in4_btn),toggle_menu_colapse()])
            in4_btn.place(x=10,y=140)
            family_btn =tk.Button(toggle_menu_fm,text="Thành viên",font=("Bold",25),bd=0,background='#FFC1C1',fg="white",cursor="hand2",
                                activebackground='#FFC1C1',activeforeground="#FF0099",command=lambda: [switch(page=family_page),change(family_btn),toggle_menu_colapse()])
            family_btn.place(x=10,y=200)
            device_btn =tk.Button(toggle_menu_fm,text="Thiết bị",font=("Bold",25),bd=0,background='#FFC1C1',fg="white",cursor="hand2",
                                activebackground='#FFC1C1',activeforeground="#FF0099",command=lambda: [switch(page=device_page),change(device_btn),toggle_menu_colapse()])
            device_btn.place(x=10,y=260)
            setTime_btn =tk.Button(toggle_menu_fm,text="Hẹn giờ",font=("Bold",25),bd=0,background='#FFC1C1',fg="white",cursor="hand2",
                                activebackground='#FFC1C1',activeforeground="#FF0099",command=lambda: [switch(page=setTime_page),change(setTime_btn),toggle_menu_colapse()])
            setTime_btn.place(x=10,y=320)
            account_btn =tk.Button(toggle_menu_fm,text="Đăng xuất",font=("Bold",25),bd=0,background='#FFC1C1',fg="white",cursor="hand2",
                                activebackground='#FFC1C1',activeforeground="#FF0099",command=logout)
            account_btn.place(x=10,y=380)


        header_frame = tk.Frame(self,bg="#FFC1C1",
                                highlightbackground="white",
                                highlightthickness=2
                                )

        toggle_btn = tk.Button(header_frame, text="≡", bg="#FFC1C1",fg="white",
                            cursor="hand2",
                            font=("Bold",40),
                            bd=0,activebackground="#FFC1C1",
                            command=toggle_menu,
                            activeforeground="red")

        toggle_btn.pack(side="left")

        title_lb = tk.Label(header_frame,text="Smart Home",bg="#FFC1C1",fg="white",
                            font=("Bold",30))
        title_lb.pack(side="left")


        header_frame.pack(side=tk.TOP,fill=tk.X)
        header_frame.pack_propagate(False)
        header_frame.configure(height="50")

        main_frame=tk.Frame(self,highlightbackground="white",highlightthickness=2)
        main_frame.place(x=0,y=50,height=550,width=1100)


        home_page()


        self.resizable(False,False)
        self.mainloop()

