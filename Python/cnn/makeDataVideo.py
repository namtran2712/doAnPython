import time
import cv2
from pathlib import Path
import os

faceCascade = cv2.CascadeClassifier (
    cv2.data.haarcascades + "./haarcascade_frontalface_default.xml"
)

Path ("dataset").mkdir (parents=True, exist_ok=True)

for fileChild in os.listdir ("./video"):
    fileChildPath = os.path.join ("./video", fileChild)
    dem = 1
    for filename in os.listdir (fileChildPath):
        filenamePath = os.path.join (fileChildPath, filename)
        # arr = filename.split (".")
        Path ("./dataset/" + fileChild).mkdir (exist_ok=True,parents=True)
        
        cap = cv2.VideoCapture (filenamePath) 
        while cap.isOpened ():
            success, frame = cap.read ()
            if (not success):
                break
            
            frameGray = cv2.cvtColor (frame, cv2.COLOR_BGR2GRAY)
            # time.sleep(0.5)
            
            face = faceCascade.detectMultiScale (frameGray,
                                                scaleFactor=1.3,
                                                minNeighbors=5)
            
            for (x, y, w, h) in face:
                detect = cv2.resize (frameGray[y : y + h, x : x + w], (128,128))
                cv2.imwrite ("./dataset/" + fileChild + "/{}.jpg".format (dem),
                            detect)
                cv2.rectangle (frame, (x, y),
                            (x + w, y + h),
                            (255,255,255),2)
                dem+=1
                
            cv2.imshow (fileChild,frame)
            cv2.waitKey (2)
            if (cv2.waitKey (2) == ord (" ")):
                break
        cv2.destroyAllWindows ()
        cap.release ()