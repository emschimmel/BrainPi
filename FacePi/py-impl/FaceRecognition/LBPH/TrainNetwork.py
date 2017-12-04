import cv2, os, sys
import numpy as np
import pickle
sys.path.append('../')
from FaceDetection.DetectFaces import DetectFaces
import random


class TrainNetwork():

    def __init__(self):
        self.log = {}

    def learn(self, image, name, id):

        self.log = {}
        # recognizer = cv2.face.FisherFaceRecognizer_create()
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('./Data/trainer.yml')
    #    faces, Ids
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faceSamples = []
        faceSamples.append(gray_image)
        Ids = []
        Ids.append(id)
        self.write_to_disc(image, name)
        recognizer.update(faceSamples, np.array(Ids))
        # recognizer.save('./Data/trainer.yml')
        recognizer.write('./Data/trainer.yml')

    def basicTrain(self):
        # recognizer = cv2.face.FisherFaceRecognizer_create()
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        faces, Ids, namedIds = self.getImagesAndLabels()
        print(len(faces))
        print(len(Ids))
        recognizer.train(faces, np.array(Ids))
        #recognizer.save('./Data/trainer.yml')
        recognizer.write('./Data/trainer.yml')

        with open('./Data/namedIds.yml', 'wb') as namedIdsFile:
            pickle.dump(namedIds, namedIdsFile)

    def getImagesAndLabels(self):
        path = './Data/lfw'

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faceSamples = []
        Ids = []
        namedIds = dict()
        label = 0
        for imagePath in imagePaths:
            name = imagePath.split('./Data/lfw/')
            name = name[1].replace('_', ' ', -1)
            print(name)
            print(label)
            imageCollection = self.read_image(imagePath)
            for filename in imageCollection:
                try:
                    file = open(imagePath+'/'+filename, 'rb')
                    readfile = file.read()
                    imageNp = np.fromstring(readfile, np.uint8)
                    image = cv2.imdecode(imageNp, cv2.IMREAD_COLOR)
                    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    faces = DetectFaces().DetectFromBinaryFromCamera(image)

                    for y, h, x, w in faces:

                        crop_img = gray_image[y:y+h,x:x+w]
                        faceSamples.append(crop_img)
                        Ids.append(label)
                        namedIds[label] = name
                except Exception as ex:
                    print('Ik weet niet wat er is, maar het boeit me ook niet')
                    print('%s' % ex)
            label = label + 1
        return faceSamples, Ids, namedIds

    def write_to_disc(self, image, name):
        save_name = name.replace(' ', '_', -1)
        file_name = './LBPH/Data/lfw/' + save_name + '/' + save_name + '_%d' % random.randint(0,9) + '_%d' % random.randint(0,9) + '_%d' % random.randint(0,9) + '.jpg'
        print(file_name)
        cv2.imwrite(file_name, image)

    def read_image(self, path):
        print(path)
        try:
            root, dirs, files=next(os.walk(path))
            print(files)
            imageCollection=list(filter(lambda filename:(filename.endswith('.jpg')| filename.endswith('.png')), files))

            return imageCollection
        except Exception as ex:
            print('Read_image gooit error onder het tapijt!')
            return []

if __name__ == '__main__':
    TrainNetwork().basicTrain()
