#!/usr/bin/env python3

import numpy as np
import cv2
import os.path
import random # test


##------------------------
##     Config
##------------------------
#imageCollection = []
#file_path = './img/'

# def read_image():
#     global imageCollection
#
#     root, dirs, files=next(os.walk(file_path))
#     imageCollection=list(filter(lambda filename:filename.endswith('.jpg'), files))
#     return random.choice(imageCollection)
#
# filename = read_image()
# print (filename)

class DetectFaces():


    def __init__(self):
        self.log = {}

    def DetectFromBinary(self, image):
        cascPath = "./haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascPath)
        nparr = np.fromstring(image, np.uint8)
        colorimg = cv2.imdecode(nparr, cv2.IMREAD_COLOR)  # cv2.IMREAD_COLOR in OpenCV 3.1

      #  colorimg = cv2.imread(image)
        gray = cv2.cvtColor(colorimg, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags = cv2.CASCADE_SCALE_IMAGE
        )

        # if (len(faces) is not 0):
        #
        #     for (x, y, w, h) in faces:
        #
        #         cv2.rectangle(colorimg, (x, y), (x+w, y+h), (0, 255, 0), 2)
        #         cv2.imshow("face", colorimg[y:y + w, x:x + h])
        # else:
        #     print("0")
        #cv2.imshow("Faces found", colorimg)
        return faces