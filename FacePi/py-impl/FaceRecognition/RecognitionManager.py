
from LBPH.RecognizeFace import RecognizeFace
from LBPH.TrainNetwork import TrainNetwork

class RecognitionManager():

    def __init__(self):
        self.log = {}

    def train(self):
        TrainNetwork().basicTrain()

    def recon_face(self, image):
        return RecognizeFace().reconFaceFromImage(image)

    def recon_cam_face(self):
        return RecognizeFace().reconFaceWithCam()


if __name__ == '__main__':
    RecognitionManager().train()
    RecognitionManager().recon_cam_face()