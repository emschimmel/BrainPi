import cv2, os, sys
import numpy as np
import pickle
sys.path.append('../')
from FaceDetection.DetectFaces import DetectFaces
import random
sys.path.append('../../')
import config


class TrainNetwork():

    def __init__(self):
        pass

    @classmethod
    def learn(self, image, name, id):
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(config.lbph_trainer_file)
    #    faces, Ids
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faceSamples = []
        faceSamples.append(gray_image)
        Ids = []
        Ids.append(id)
        self.__write_to_disc(image=image, name=name)
        recognizer.update(faceSamples, np.array(Ids))
        # recognizer.save('./Data/trainer.yml')
        recognizer.write(config.lbph_trainer_file)

    @classmethod
    def basicTrain(self):
        self.getImagesAndLabels()

    @staticmethod
    def trainAndWrite(faces, Ids):
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.train(faces, np.array(Ids))
        #recognizer.save('./Data/trainer.yml')
        recognizer.write(config.lbph_trainer_file)

    @classmethod
    def getImagesAndLabels(self):
        path = config.lbph_data_path

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faceSamples = []
        Ids = []
        namedIds = dict()
        label = 0
        for imagePath in imagePaths:
            name = imagePath.split(path+'/')
            print(name)
            name = name[0].replace('_', ' ', -1)
            print(label)
            print(imagePath)
            imageCollection = self.__read_image(path=imagePath)
            print(len(imageCollection))
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
            if len(faceSamples) > 100:
                self.trainAndWrite(faceSamples, Ids)
                faceSamples.clear()
                Ids.clear()
            self.trainAndWrite(faceSamples, Ids)
            with open(config.lbph_name_id_file, 'wb') as namedIdsFile:
                pickle.dump(namedIds, namedIdsFile)

    @staticmethod
    def __write_to_disc(image, name):
        save_name = name.replace(' ', '_', -1)
        file_name = config.lbph_data_path + save_name + '/' + save_name + '_%d' % random.randint(0,9) + '_%d' % random.randint(0,9) + '_%d' % random.randint(0,9) + '.jpg'
        print(file_name)
        cv2.imwrite(file_name, image)

    @staticmethod
    def __read_image(path):
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
