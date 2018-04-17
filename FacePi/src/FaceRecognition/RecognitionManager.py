import sys
sys.path.append('./LBPH')
from .LBPH.RecognizeFace import RecognizeFace as LbphFace
from .LBPH.TrainNetwork import TrainNetwork as LbphTrain
from .Eigen.RecognizeFace import RecognizeFace as EigenFace
from .Eigen.TrainNetwork import TrainNetwork as EigenTrain
from .Fisher.RecognizeFace import RecognizeFace as FisherFace
from .Fisher.TrainNetwork import TrainNetwork as FisherTrain
from .TensorFlow.startTensor import StartTensor as Tensor

class RecognitionManager():

    def __init__(self):
        pass

    @staticmethod
    def train(tensorSession):
        LbphTrain().basicTrain()
        Tensor().train(tensorSession)
        # EigenTrain().basicTrain()
        # FisherTrain().basicTrain()
        pass

    @staticmethod
    def recon_face(tensorSession, image):
        print('manager')
        personList = []
        # for name, conf in LbphFace().reconFaceFromImage(image):
        #     person = PersonEntry()
        #     person.person = name
        #     person.chance = conf
        #     person.algoritm = 'LBPH'
        #     personList.append(person)
        #     print(person)
        print("asking tensor")
        personList += Tensor().loadWithoutTrainFromFrame(tensorSession, image)
        print(personList)
        # output['Eigen'] = EigenFace().reconFaceFromImage(image)
        # print(output)
        # output['Fisher'] = FisherFace().reconFaceFromImage(image)
        # print(output)
        return personList

    @staticmethod
    def recon_cam_face():
        output = dict()
        output['LBPH'] = LbphFace().reconFaceWithCam()
        # output['Eigen'] = EigenFace().reconFaceWithCam()
        # output['Fisher'] = FisherFace().reconFaceWithCam()
        return output


if __name__ == '__main__':
    pass
#   RecognitionManager().train()
#    RecognitionManager().recon_cam_face()
#    pass