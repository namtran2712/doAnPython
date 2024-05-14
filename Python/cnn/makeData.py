import cv2
from pathlib import Path
from database import userDAO
faceCascade = cv2.CascadeClassifier (
    cv2.data.haarcascades+"./haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture (0)
Path ("dataset").mkdir (parents=True, exist_ok=True)

filePath = userDAO.getLastId()[0][0]
Path ("dataset/" + str(filePath)).mkdir (parents=True, exist_ok=True)

count = 1

while (cap.isOpened ()):
    success, frame = cap.read ()
    
    frameGray = cv2.cvtColor (frame, cv2.COLOR_BGR2GRAY)
    
    face = faceCascade.detectMultiScale (frame,
                                        minNeighbors=6,
                                        scaleFactor=1.3)
    for (x, y, w, h) in face:
        cv2.rectangle (frame,(x, y),
                       (x + w, y + h),
                       (255,255,255),
                       2)
        faceDetect = frameGray[y+5:y+h+5, x+5:x+w-5]
        faceDetect = cv2.resize (faceDetect,(100,100))
        cv2.imwrite ("dataset/" + str (filePath) + "/{}.png".format (count),
                     faceDetect)
        count += 1
    
    cv2.imshow ("Camera", frame)
    if (cv2.waitKey (1) == ord (" ") or count > 500):
        break

cv2.destroyAllWindows ()
cap.release ()
with open('E:\\Code\\Python\\Doanreal\\Python\\cnn\\trainModel.py', 'r') as f:
    code = f.read()
    exec(code)
