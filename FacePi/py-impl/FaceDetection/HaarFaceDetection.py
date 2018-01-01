# https://docs.opencv.org/3.3.0/d7/d8b/tutorial_py_face_detection.html
# https://docs.opencv.org/3.3.0/dc/d88/tutorial_traincascade.html

import numpy as np
import cv2
import time

class HaarFaceDetection:


    def __init__(self):
        self.log = {}

    cap = cv2.VideoCapture(0)

    @classmethod
    def testWithMacCamera(self):
        while (True):
            # Capture frame-by-frame
            ret, frame = self.cap.read()

            # Our operations on the frame come here
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = self.detectFaceWithEyes(frame)
            # Display the resulting frame
            cv2.imshow('frame', gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # When everything done, release the capture
        self.cap.release()
        cv2.destroyAllWindows()

    @staticmethod
    def detectFaceWithEyes(img):
        face_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_default.xml')
        # face_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_alt.xml')
        # face_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_alt2.xml')
        # face_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_alt_tree.xml')
        # face_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalcatface.xml')
        # face_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalcatface_extended.xml')
        # face_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_profileface.xml')

        # eye_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_eye.xml')
        # eye_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_eye_tree_eyeglasses.xml')
        # img = cv2.imread('10-test.jpg')
        # img = cv2.imread('me.jpg')
        # img = cv2.imread('me_2.jpg')
        # img = cv2.imread('cat.jpg')

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # roi_gray = gray[y:y + h, x:x + w]
            # roi_color = img[y:y + h, x:x + w]
            # eyes = eye_cascade.detectMultiScale(roi_gray)
            # for (ex, ey, ew, eh) in eyes:
            #     cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        return img
        # cv2.imshow('img', img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

HaarFaceDetection().testWithMacCamera()
#HaarFaceDetection().detectFaceWithEyes(None)