#!/usr/bin/env python

import sys

import consul

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
import logging
import random

import statsd
stat = statsd.StatsClient('localhost', 8125)

port = random.randint(50000, 59000)

log = logging.getLogger()
log.setLevel(logging.DEBUG)

class FacePiThriftHandler:
    def __init__(self):
        self.log = {}

    @stat.timer("handleRequest")
    def handleRequest(self, input):
        try:
            inputImage = input.image
            faces = DetectFaces().DetectFromBinary(inputImage)
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

    @stat.timer("confirmFace")
    def confirmFace(self, input):
        print(input)
        # train the network with the found face with name
        print(input.person)

def create_server(host=config.face_pi_ip):
    handler = FacePiThriftHandler()
    return TServer.TSimpleServer(
        FacePiThriftService.Processor(handler),
        TSocket.TServerSocket(host=host, port=port),
        TTransport.TBufferedTransportFactory(),
        TBinaryProtocol.TBinaryProtocolFactory()
    )

def register():
    log.info("register started")
    c = consul.Consul(host='localhost')
    #check = consul.Check.tcp("127.0.0.1", port, "30s")
    check = consul.Check = {'script': 'ps | awk -F" " \'/PythonFacePiServer.py/ && !/awk/{print $1}\'',
                                    'id': 'eye_pi', 'name': 'face_pi process tree check', 'Interval': '10s',
                                    'timeout': '2s'}
    c.agent.service.register("face-pi", "face-pi-%d" % port, address=config.face_pi_ip, port=port, check=check)
    log.info("services: " + str(c.agent.services()))

def unregister():
    log.info("unregister started")
    c = consul.Consul(host='localhost')
    c.agent.service.deregister("face-pi-%d" % port)
    log.info("services: " + str(c.agent.services()))

if __name__ == '__main__':
    server = create_server()
    register()
    server.serve()
    unregister()
