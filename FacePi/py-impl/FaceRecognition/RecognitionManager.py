
from LBPH.RecognizeFace import RecognizeFace as LbphFace
from LBPH.TrainNetwork import TrainNetwork as LbphTrain
from Eigen.RecognizeFace import RecognizeFace as EigenFace
from Eigen.TrainNetwork import TrainNetwork as EigenTrain
from Fisher.RecognizeFace import RecognizeFace as FisherFace
from Fisher.TrainNetwork import TrainNetwork as FisherTrain

class RecognitionManager():

    def __init__(self):
        self.log = {}

    def train(self):
        LbphTrain().basicTrain()
        # EigenTrain().basicTrain()
        # FisherTrain().basicTrain()
        pass

    def recon_face(self, image):
        output = dict()
        # output['LBPH'] = LbphFace().reconFaceFromImage(image)
        # output['Eigen'] = EigenFace().reconFaceFromImage(image)
        # output['Fisher'] = FisherFace().reconFaceFromImage(image)
        return output

    def recon_cam_face(self):
        output = dict()
        # output['LBPH'] = LbphFace().reconFaceWithCam()
        # output['Eigen'] = EigenFace().reconFaceWithCam()
        # output['Fisher'] = FisherFace().reconFaceWithCam()
        return output


if __name__ == '__main__':

    RecognitionManager().train()
#    RecognitionManager().recon_cam_face()
#    pass