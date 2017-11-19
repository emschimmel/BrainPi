#!/usr/bin/env python

import sys

sys.path.append('../gen-py')
sys.path.append('./FaceDetection')
sys.path.append('./FaceRecognition')


from FacePi import FacePiThriftService
from FacePi.ttypes import *
from ThriftException.ttypes import *

from DetectFaces import DetectFaces

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# import cv2
sys.path.append('../../')
import config


class FacePiThriftHandler:
    def __init__(self):
        self.log = {}

    def handleRequest(self, input):
        try:
            inputImage = input.image
            faces = DetectFaces.DetectFromBinary(self, inputImage)
            print("Found {0} faces!".format(len(faces)))
            personList = []
            if (faces is not None):
                for face in faces:
                    person = PersonEntry()
                    person.person = '== Hans =='
                    person.chance = 90.0
                #    person.image = cv2.threshold(face,127,255,cv2.THRESH_BINARY)
                    personList.append(person)
            output = FacePiOutput()
            output.personCollection = personList
            print(output)
            return output
        except Exception as ex:
            print('invalid request %s' % ex)
            raise ThriftServiceException('FacePi', 'invalid request %s' % ex)

    def confirmFace(self, input):
        print(input)
        # train the network with the found face with name
        print(input.person)


handler = FacePiThriftHandler()
processor = FacePiThriftService.Processor(handler)
transport = TSocket.TServerSocket(port=config.face_pi_port)

tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print("Starting python server...")
server.serve()
print("done!")
