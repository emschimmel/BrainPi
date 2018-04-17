# https://docs.opencv.org/3.3.0/dc/d88/tutorial_traincascade.html
import sys
import cv2
import pickle
from .TrainNetwork import TrainNetwork
sys.path.append('../')
from FaceDetection.DetectFaces import DetectFaces
sys.path.append('../../')
import config

class RecognizeFace():

    def __init__(self):
        pass

    def reconFaceWithCam(self):
        output = dict()
        with open(config.eigen_name_id_file, 'rb') as namedIdsFile:
            self.namedIds = pickle.loads(namedIdsFile.read())
        recon = self.recon_face_with_camera()
        print(recon)
        list_names = []
        for conf in recon:
            if conf[1] < 20:
                if not any(conf[0] in s for s in list_names):
                    list_names.append(conf[0])
                    output[conf[0]] = conf[1]
                    TrainNetwork().learn(conf[2], conf[0], conf[3])
        print(output)

    def reconFaceFromImage(self, image):
        output = dict()
        with open(config.eigen_name_id_file, 'rb') as namedIdsFile:
            self.namedIds = pickle.loads(namedIdsFile.read())
        recon = self.recon_face_with_file(image)
        print(recon)
        list_names = []
        for conf in recon:
            if conf[1] < 20:
                if not any(conf[0] in s for s in list_names):
                    list_names.append(conf[0])
                    output[conf[0]] = conf[1]
                    TrainNetwork().learn(conf[2], conf[0], conf[3])
        print(output)

    def sort_output(self, recon_collection):
        list_names = dict(list)

    def recon_face_with_camera(self):
        # recognizer = cv2.face.FisherFaceRecognizer_create()
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(config.eigen_trainer_file)
        cam = cv2.VideoCapture(0)
        recon = []
        loop = True
        while loop:
            ret, im = cam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = DetectFaces().DetectFromBinaryFromCamera(im)
            stopLoop = False
            for (x, y, w, h) in faces:
                Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
                name = self.namedIds[Id]
                if (conf < 20):
                    crop_img = im[y:y + h, x:x + w]
                    recon.append([name, conf, crop_img, Id])
                    stopLoop = True
                cv2.rectangle(im, (x - 22, y - 90), (x + w + 22, y - 22), (0, 255, 0), -1)
                cv2.putText(im, name+' '+str(conf), (x, y - 40), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)
            if stopLoop:
                loop = False
            cv2.imshow('im', im)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        cam.release()
        return recon

    def recon_face_with_file(self, im):
        # recognizer = cv2.face.FisherFaceRecognizer_create()
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(config.eigen_trainer_file)
        recon = []
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = DetectFaces().DetectFromBinaryFromCamera(im)
        for (x, y, w, h) in faces:
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            name = self.namedIds[Id]
            if (conf < 20):
                crop_img = im[y:y + h, x:x + w]
                recon.append([name, conf, crop_img, Id])

            cv2.rectangle(im, (x - 22, y - 90), (x + w + 22, y - 22), (0, 255, 0), -1)
            cv2.putText(im, name+' '+str(conf), (x, y - 40), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)

        return recon
