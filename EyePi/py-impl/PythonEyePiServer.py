#!/usr/bin/env python

import sys
sys.path.append('../gen-py')

from PythonFacePiClient import FacePiThriftClient

from EyePi import EyePiThriftService
from EyePi.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
 
import socket
 
class EyePiThriftHandler():
    def __init__(self):
        self.log = {}



    def handleRequest(self, input):

        facePiOutput = FacePiThriftClient.handle_request(self, input.image)
        eyeOutput = EyePiOutput()
        eyeOutput.personCollection = facePiOutput
        if not facePiOutput:
            eyeOutput.ok = False
        else:
            eyeOutput.ok = True
        return eyeOutput

    def confimFace(self, input):
        FacePiThriftClient.confim_face(self, input)

    def writeLog(self, input):
        print ("sayMsg(" + input + ")")

 
handler = EyePiThriftHandler()
processor = EyePiThriftService.Processor(handler)
transport = TSocket.TServerSocket(port=30302)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
 
server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
 
print ("Starting python server...")
server.serve()
print ("done!")
