#!/usr/bin/env python

import sys
sys.path.append('../gen-py')

from PythonFacePiClient import FacePiThriftClient
from GenericThriftClient import GenericThriftClient
from ShortTermMemoryClient import ShortTermMemoryClient

from EyePi import EyePiThriftService
from EyePi.ttypes import *
from ThriftException.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

sys.path.append('../../')
import config
 
class EyePiThriftHandler:
    def __init__(self):
        self.log = {}

    ### External ###
    def handleRequest(self, input):
        try:
            ShortTermMemoryClient().log_event(input, message='start eyepi')
            eyeOutput = EyePiOutput()
            if input.image:
                facePiOutput = FacePiThriftClient().handle_request(input.image)
                eyeOutput.personCollection = facePiOutput
                if not facePiOutput:
                    eyeOutput.ok = False
                else:
                    eyeOutput.ok = True
            if not input.token and not input.image:
                eyeOutput.ok = False
            if eyeOutput.ok:
                cases = {
                    ActionEnum.MUSIC: lambda: GenericThriftClient().handle_request(input.actionParameters, config.music_pi_ip, config.music_pi_port),
                    ActionEnum.AGENDA: lambda: GenericThriftClient().handle_request(input.actionParameters, config.agenda_pi_ip, config.agenda_pi_port),
                    ActionEnum.KAKU: lambda: GenericThriftClient().handle_request(input.actionParameters, config.kaku_pi_ip, config.kaku_pi_port),
                    ActionEnum.WEATHER: lambda: GenericThriftClient().handle_request(input.actionParameters, config.weather_pi_ip, config.weather_pi_port)
                }
                cases[input.action]()
            return eyeOutput
        except Exception as ex:
            ShortTermMemoryClient().log_exception(input, ex)
            print('invalid request %s' % ex)
            raise ThriftServiceException('EyePi', 'invalid request %s' % ex)

    ### External ###
    def confimFace(self, input):
        FacePiThriftClient.confim_face(self, input)


    ### External ###
    def writeLog(self, input):
        print ("sayMsg(" + input + ")")



handler = EyePiThriftHandler()
processor = EyePiThriftService.Processor(handler)
transport = TSocket.TServerSocket(port=config.eye_pi_port)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
 
server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
 
print ("Starting python server...")
server.serve()
print ("done!")
