#!/usr/bin/env python3

import numpy as np
import cv2

class DetectFaces():


    def __init__(self):
        self.log = {}

    def DetectFromBinaryFromCamera(self, image):
        face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        return faces

    def DetectFromBinaryFromFile(self, image):
        try:
            # print(image)
            face_cascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")
            nparr = np.fromstring(image, np.uint8)
            colorimg = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
          #  colorimg = cv2.imread(image)
            gray = cv2.cvtColor(colorimg, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(30, 30),
                flags = cv2.CASCADE_SCALE_IMAGE
            )
            return faces
        except Exception as ex:
            print("ex %s" % ex)

        # if (len(faces) is not 0):
        #
        #     for (x, y, w, h) in faces:
        #
        #         cv2.rectangle(colorimg, (x, y), (x+w, y+h), (0, 255, 0), 2)
        #         cv2.imshow("face", colorimg[y:y + w, x:x + h])
        # else:
        #     print("0")
        #cv2.imshow("Faces found", colorimg)
