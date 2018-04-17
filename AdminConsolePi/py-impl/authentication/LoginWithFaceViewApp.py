import sys
import cv2
import threading
import time
import pickle

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.camera import Camera
from kivy.clock import Clock
from kivy.graphics.texture import Texture


sys.path.append('../gen-py')

from EyePi import EyePiThriftService
from EyePi.ttypes import *
from AutorisationStruct.ttypes import *

from ConnectionHelpers.ConnectEyePi import ConnectEyePi
from ConnectionHelpers.PasswordHelper import PasswordHelper

from ThriftException.ttypes import *
from thrift import Thrift

Builder.load_file("authentication/template/LoginWithFaceView.kv")

class MyCamera(Camera):

    names = []

    def __init__(self, **kwargs):
        super(MyCamera, self).__init__(**kwargs)
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0 / 30)

    def update(self, dt):
        ret, frame = self.capture.read()

        image, faces, eyes = self.detectFaceWithEyes(frame)

        # convert it to texture
        buf1 = cv2.flip(frame, 0)
        buf = buf1.tostring()
        image_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        # display image from the texture
        self.texture = image_texture

        if faces > 0 and eyes > 1:
            print('Face found')


    def detectFaceWithEyes(self, img):
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        eyes = []
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            name = self.names[0].person if 0 < len(self.names) else ""
            confidence = "%s%%" % self.names[0].chance if 0 < len(self.names) else ""
            cv2.putText(img, name + ' ' + str(confidence), (x - 150, y - 40), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)
        return img, len(faces), len(eyes)

    def addDetectedFace(self, name):
        MyLabel.text = 'Hallo Hans'


class LoginWithFaceView(Popup):
    def __init__(self, **kwargs):
        super(LoginWithFaceView, self).__init__(**kwargs)

    def translate(self, key):
        app = App.get_running_app()
        return app.i18n.t(key)

    def exit_application(self):
        App.get_running_app().stop()


class LoginWithFaceViewApp(App):

    def build(self):
        return LoginWithFaceView()
