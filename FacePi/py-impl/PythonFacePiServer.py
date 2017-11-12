#!/usr/bin/env python

import sys

sys.path.append('../gen-py')
sys.path.append('../')

from FacePi import FacePiThriftService
from FacePi.ttypes import *

from DetectFaces import DetectFaces

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import socket


class FacePiThriftHandler:
    def __init__(self):
        self.log = {}

    def handleRequest(self, input):

        inputImage = input.image
        faces = DetectFaces.DetectFromBinary(self, inputImage)
        print("Found {0} faces!".format(len(faces)))
        personList = []
        if (faces is not None):
            for face in faces:
                person = PersonEntry()
                person.person = 'Hans'
                person.chance = 90.0
                personList.append(person)
        output = FacePiOutput()
        output.personCollection = personList
        print(output)
        return output


handler = FacePiThriftHandler()
processor = FacePiThriftService.Processor(handler)
transport = TSocket.TServerSocket(port=30303)

tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print("Starting python server...")
server.serve()
print("done!")
