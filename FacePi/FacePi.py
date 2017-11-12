#!/usr/bin/env python3

import numpy as np
import cv2
import os.path
import random # test

import config

##------------------------
##     Config
##------------------------
imageCollection = []
file_path = './img/'
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)


def read_image():
    global imageCollection

    root, dirs, files=next(os.walk(config.file_path))
    imageCollection=list(filter(lambda filename:filename.endswith('.jpg'), files))
    return random.choice(imageCollection)

filename = read_image()
print (filename)
colorimg = cv2.imread(file_path +filename)
gray = cv2.cvtColor(colorimg, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
)


#px = img[100,100]
#print (colorimg)
print("Found {0} faces!".format(len(faces)))

if (len(faces) is not 0):

    for (x, y, w, h) in faces:

        cv2.rectangle(colorimg, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imshow("face", colorimg[y:y + w, x:x + h])

#cv2.imshow("Faces found", colorimg)
cv2.waitKey(0)