from PIL import Image
import tkinter as tk

# Đọc ảnh
root=tk.Tk()
root.geometry("1200x700")

image = Image.open("img_home.png")

# Tạo PhotoImage
photo_image = tk.PhotoImage(image)

# Tạo Label với ảnh
home_lb = tk.Label(root,image=photo_image)
home_lb.pack()

root.mainloop()