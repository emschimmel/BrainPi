#!/usr/bin/env python3

import numpy as np
import cv2

class DetectFaces():

    @staticmethod
    def DetectFromBinaryFromCamera(image):
        face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        return faces

    @staticmethod
    def DetectFromBinaryFromFile(image):
        try:
            face_cascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")
            nparr = np.fromstring(image, np.uint8)
            colorimg = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
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


