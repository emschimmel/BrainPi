from ConnectionHelpers.DeviceRegistrator import DeviceRegistrator
from ConnectionHelpers.ConnectEyePi import ConnectEyePi

from EyePi.ttypes import EyePiInput
from GenericStruct.ttypes import ActionEnum
from WeatherPi.ttypes import WeatherInput
import cv2
import threading
import time
import pickle

class CameraSimulation:

    def __init__(self):
        self.log = {}

    cap = cv2.VideoCapture(0)
    device_token = DeviceRegistrator().register_device()
    face_connection_thread_running = False
    names = []

    def testWithMacCamera(self):
        while (True):
            # Capture frame-by-frame
            ret, frame = self.cap.read()
            image, faces, eyes = self.detectFaceWithEyes(frame)
            if faces > 0 and eyes > 1:
                if not self.face_connection_thread_running:
                    t1 = threading.Thread(target=self.connectToEyePi, args=(frame,))
                    t1.start()
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()
        # When everything done, release the capture

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

    def connectToEyePi(self, image):

        # try1: cv2.threshold(img,127,255,cv2.THRESH_BINARY)
        # try2:
        print('i see faces')
        try:
            self.face_connection_thread_running = True
            input = EyePiInput()
            # input.image = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
            input.image = pickle.dumps(obj=image, protocol=None, fix_imports=False)

            actions = dict()
            weather_input = WeatherInput()
            weather_input.location = 'Amsterdam,nl'
            actionParameter = pickle.dumps(obj=weather_input, protocol=None, fix_imports=False)
            actions[ActionEnum.WEATHER] = actionParameter
            input.action = actions

            input.deviceToken = self.device_token
            output =  ConnectEyePi().handleRequest(input)
            time.sleep(1)
            if output.ok:
                print('ok, yay, I know you')
                self.names = output.personCollection
            time.sleep(10)
            self.face_connection_thread_running = False
        except Exception as ex:
            print('exception catched %s' % ex)

CameraSimulation().testWithMacCamera()



