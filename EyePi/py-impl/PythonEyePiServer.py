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

sys.path.append('../../')
import config
 
class EyePiThriftHandler():
    def __init__(self):
        self.log = {}

    def handleRequest(self, input):
        eyeOutput = EyePiOutput()
        if input.image:
            facePiOutput = FacePiThriftClient.handle_request(self, input.image)
            eyeOutput.personCollection = facePiOutput
            if not facePiOutput:
                eyeOutput.ok = False
            else:
                eyeOutput.ok = True
        if not input.token and not input.image:
            eyeOutput.ok = False
        if eyeOutput.ok:
            cases = {
                ActionEnum.MUSIC: lambda: self.make_music(input.actionParameters),
                ActionEnum.AGENDA: lambda: self.make_agenda(input.actionParameters),
                ActionEnum.KAKU: lambda: self.make_kaku(input.actionParameters),
                ActionEnum.WEATHER: lambda: self.make_weather(input.actionParameters)
            }
            cases[input.action]()
        return eyeOutput

    def confimFace(self, input):
        FacePiThriftClient.confim_face(self, input)

    def writeLog(self, input):
        print ("sayMsg(" + input + ")")

    def make_music(self, parameters):
        print('MUSIC')

    def make_agenda(self, parameters):
        print('AGENDA')

    def make_kaku(self, parameters):
        print('KAKU')

    def make_weather(self, parameters):
        print('WEATHER')

handler = EyePiThriftHandler()
processor = EyePiThriftService.Processor(handler)
transport = TSocket.TServerSocket(port=config.eye_pi_port)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
 
server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
 
print ("Starting python server...")
server.serve()
print ("done!")
