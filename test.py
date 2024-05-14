import cv2
import tkinter as tk
from tkinter_webcam import webcam

faceCascade = cv2.CascadeClassifier (
    cv2.data.haarcascades + "./haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture (0)
 
window =tk.Tk()
window.title("con cho tran nam")
window.geometry("1000x1000")

video = webcam.Box(window,width=500,height=500)

video.show_frames()

while cap.isOpened ():
    success, frame = cap.read ()
    if (not success):
        print ("ok")
        break
    face = faceCascade.detectMultiScale (frame,
                                        minNeighbors=7,
                                        scaleFactor=1.3)
    for (x, y, w, h) in face:
        print (x, y , w, h)
    
tk.mainloop()

