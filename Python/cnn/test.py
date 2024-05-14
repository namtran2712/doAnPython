import cv2
import numpy
from keras._tf_keras.keras.models import load_model
import os
from database import userDAO
from gui.mainGUI import mainGUI

faceCascade = cv2.CascadeClassifier (cv2.data.haarcascades + 
                                     "haarcascade_frontalface_default.xml")

model = load_model ("python/cnn/nhanDien.h5")

cap = cv2.VideoCapture (0)

listResult = []

for x in os.listdir ("./dataset"):
    listResult.append (x)

check = True

i = 0

while (check):
    success, frame = cap.read ()
    
    frameGray = cv2.cvtColor (frame,cv2.COLOR_BGR2GRAY)
    
    face = faceCascade.detectMultiScale (frameGray,
                                         minNeighbors=5,
                                         scaleFactor=1.3)
    i += 1
    if (i > 50):
        for (x, y, w, h) in face:
            faceDetect = cv2.resize (frameGray[y : y+h, x : x+w], (100,100))
            result = numpy.argmax (model.predict (faceDetect.reshape (-1, 100, 100, 1)))
            if (model.predict (faceDetect.reshape (-1, 100, 100, 1))[0][result] > 0.95):
                cv2.rectangle (frame, (x, y),
                            (x + w, y + h),
                            (255,255,255), 2)
                print (listResult)
                user = userDAO.selectByID (listResult[result])
                if (len(user)>0):
                    check = False
                    cv2.destroyAllWindows ()
                    cap.release ()
                    print (user)
                    gui= mainGUI (user[0][4])
                    print (user)
                cv2.putText (frame, listResult[result],
                        (x+15, y-15), cv2.FONT_HERSHEY_DUPLEX,
                        0.8, (255,255,255), 3)
            
    cv2.imshow ("Camera", frame)
    if (cv2.waitKey (1) == ord (" ")):
        break
    
cv2.destroyAllWindows ()
cap.release ()