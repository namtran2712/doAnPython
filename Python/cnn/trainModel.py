import os
import numpy as np

from keras.models import Sequential
from keras.layers import Dense, MaxPooling2D, Conv2D, Dropout, BatchNormalization, Flatten
from sklearn.model_selection import train_test_split

filePath = "./dataset"
data = []

def oneHot (filePath):
    listOneHot = []
    for i in range (len(os.listdir (filePath))):
        tmp = np.zeros (len(os.listdir (filePath)))
        tmp[i] = 1
        listOneHot.append (tmp)
    
    i = 0
    for x in os.listdir (filePath):
        dictData[x] = listOneHot[i]
        i+=1
    
    return dictData

dictData = oneHot (filePath)

def getData (file, data):
    for fileChild in os.listdir (file):
        fileChildPath = os.path.join (file, fileChild)
        listData = []
        for filename in os.listdir (fileChildPath):
            from PIL import Image
            filenamePath = os.path.join (fileChildPath, filename)
            img = np.array (Image.open (filenamePath))
            listData.append ((img, dictData[fileChild]))
        data.extend(listData)
    return data

data = getData (filePath, data)

np.random.shuffle (data)
np.random.shuffle (data)

xTrain, xTest = train_test_split (data, test_size=0.2)

model = Sequential ([
    Conv2D (32, (3,3), input_shape=(100,100,1), activation='relu'),
    MaxPooling2D (pool_size = (2,2)),

    Conv2D (64, (3,3), input_shape=(100,100,1), activation='relu'),
    MaxPooling2D (pool_size = (2,2)),

    Conv2D (128, (3,3), activation='relu'),
    MaxPooling2D (pool_size = (2,2)),
    
    Flatten (),
    Dense (512, activation='relu'),
    Dropout (0.5),
    Dense (len (dictData), activation='softmax')
])

imagesTrain = np.array([x[0] for x in xTrain])
labelsTrain = np.array([x[1] for x in xTrain])

imagesTest = np.array([x[0] for x in xTest])
labelsTest = np.array([x[1] for x in xTest])

model.compile (optimizer="adam",
               loss="categorical_crossentropy",
               metrics=["accuracy"])

model.fit(imagesTrain, labelsTrain, epochs=20,
           batch_size=32,
           validation_data=(imagesTest, labelsTest))

model.summary ()

model.save ("./python/cnn/nhandien.h5")
from gui import sigInGUI
a =sigInGUI.signIn()