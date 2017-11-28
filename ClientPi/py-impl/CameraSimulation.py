from DeviceRegistrator import DeviceRegistrator
from ConnectHandleRequest import ConnectHandleRequest

from EyePi.ttypes import *
from GenericStruct.ttypes import *
import cv2
import threading
import time

class CameraSimulation:

    def __init__(self):
        self.log = {}

    cap = cv2.VideoCapture(0)
    device_token = DeviceRegistrator().register_device()
    face_connection_thread_running = False

    def testWithMacCamera(self):
        while (True):
            # Capture frame-by-frame
            ret, frame = self.cap.read()
            image, faces, eyes = self.detectFaceWithEyes(frame)
            if faces > 0 and eyes > 1:
                print('i see faces')
                if not self.face_connection_thread_running:
                    t1 = threading.Thread(target=self.connectToEyePi(image))
                    t1.start()
            else:
                print('I see no faces')
            cv2.imshow('frame', image)
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
        return img, len(faces), len(eyes)

    def connectToEyePi(self, image):
        self.face_connection_thread_running = True
        input = EyePiInput()
        input.image = image

        parameter = GenericObject()
        parameter.stringValue = "%s" % 'Amsterdam,nl'

        input.deviceToken = self.device_token
        input.action = ActionEnum.WEATHER
        input.actionParameters = parameter
        output =  ConnectHandleRequest().handleRequest(input)
        print(output)
        if output.ok:
            print('ok, yay, I know you')
            time.sleep(10)
            self.cap.release()
            cv2.destroyAllWindows()
            self.face_connection_thread_running = False
        else:
            self.face_connection_thread_running = False

CameraSimulation().testWithMacCamera()



