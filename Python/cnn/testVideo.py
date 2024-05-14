import cv2
import numpy as np
from keras.models import load_model
import os

faceCascade = cv2.CascadeClassifier (cv2.data.haarcascades + 
                                     "haarcascade_frontalface_default.xml")

model = load_model ("python/cnn/nhanDien.h5")

listResult = []

for x in os.listdir ("./dataset"):
    listResult.append (x)
    
for fileTest in os.listdir ("./test"):
    fileTestPath = os.path.join ("./test",fileTest)
    cap = cv2.VideoCapture (fileTestPath)
    while (cap.isOpened ()):
        success, frame = cap.read ()
        if (not success):
            break
        gray = cv2.cvtColor (frame, cv2.COLOR_BGR2GRAY)
        face = faceCascade.detectMultiScale (gray, scaleFactor=1.3,
                                             minNeighbors=5)
        for (x, y, w, h) in face:
            faceDetect = cv2.resize (gray[y : y+h, x : x+w], (128,128))
            result = np.argmax (model.predict (faceDetect.reshape (-1, 128, 128, 1)))
            if (model.predict (faceDetect.reshape (-1, 128, 128, 1))[0][result] > 0.95):
                cv2.rectangle (frame, (x, y),
                            (x + w, y + h),
                            (255,255,255), 2)
                cv2.putText (frame, listResult[result],
                        (x+15, y-15), cv2.FONT_HERSHEY_DUPLEX,
                        0.8, (255,255,255), 3)
        
        cv2.imshow ("camera",frame)
                
        if (cv2.waitKey (1) == ord (" ")):
            break
    
    cv2.destroyAllWindows ()
    cap.release ()