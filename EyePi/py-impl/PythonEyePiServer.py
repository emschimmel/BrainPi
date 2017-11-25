#!/usr/bin/env python

import sys

import consul

sys.path.append('../gen-py')

from PythonFacePiClient import FacePiThriftClient
from GenericThriftClient import GenericThriftClient
from ShortTermLogMemoryClient import ShortTermLogMemoryClient
from ShortTermTokenMemoryClient import ShortTermTokenMemoryClient

from EyePi import EyePiThriftService
from EyePi.ttypes import *
from ThriftException.ttypes import *
from GenericStruct.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

sys.path.append('../../')
import config
import logging
import random

import statsd
stat = statsd.StatsClient('localhost', 8125)

port = random.randint(50000, 59000)

log = logging.getLogger()
log.setLevel(logging.DEBUG)

class EyePiThriftHandler:
    def __init__(self):
        self.log = {}

    @stat.timer("handleRequest")
    def handleRequest(self, input):
        try:
            ShortTermLogMemoryClient().log_event(input, message='start eyepi')
            eyeOutput = EyePiOutput()
            tokenValide = False
            if input.token:
                tokenValide = ShortTermTokenMemoryClient().validateToken(input.token, input.deviceToken)
            if input.image:
                facePiOutput = FacePiThriftClient().handle_request(input.image)
                eyeOutput.personCollection = facePiOutput
                if not facePiOutput:
                    eyeOutput.ok = False
                else:
                    eyeOutput.ok = True
                    eyeOutput.token = ShortTermTokenMemoryClient().getToken(input)
            if tokenValide and not input.image:
                eyeOutput.ok = False
            if eyeOutput.ok:
                eyeOutput.data = self.make_generic_call(input)
            return eyeOutput
        except ThriftServiceException as tex:
            ShortTermLogMemoryClient().log_thrift_exception(input, tex)
            raise tex
        except ExternalEndpointUnavailable as endEx:
            ShortTermLogMemoryClient().log_thrift_exception(input, endEx)
            raise endEx
        except Exception as ex:
            ShortTermLogMemoryClient().log_exception(input, ex)
            print('invalid request %s' % ex)
            raise ThriftServiceException('EyePi', 'invalid request %s' % ex)

    def make_generic_call(self, input):
        try:
            GenericThriftClient().handle_request(input.action, input.actionParameters)
        except Thrift.TException as tx:
            raise tx
        except ThriftServiceException as tex:
            raise tex
        except ExternalEndpointUnavailable as endEx:
            raise endEx
            # probably try again

    @stat.timer("confimFace")
    def confimFace(self, input):
        FacePiThriftClient.confim_face(self, input)


    @stat.timer("writeLog")
    def writeLog(self, input):
        ShortTermLogMemoryClient().log_event(input, message='start eyepi')

    @stat.timer("ping")
    def ping(self, input):
        print(input)

def create_server(host=config.eye_pi_ip):
    handler = EyePiThriftHandler()
    return TServer.TSimpleServer(
        EyePiThriftService.Processor(handler),
        TSocket.TServerSocket(host=host, port=port),
        TTransport.TBufferedTransportFactory(),
        TBinaryProtocol.TBinaryProtocolFactory()
    )

def register():
    log.info("register started")
    c = consul.Consul(host='localhost')
    #check = consul.Check.tcp("127.0.0.1", port, "30s")
    check = consul.Check = {'script': 'ps | awk -F" " \'/PythonEyePiServer.py/ && !/awk/{print $1}\'',
                                    'id': 'eye_pi', 'name': 'eye_pi process tree check', 'Interval': '10s',
                                    'timeout': '2s'}
    c.agent.service.register("eye-pi", "eye-pi-%d" % port, address=config.eye_pi_ip, port=port, check=check)
    log.info("services: " + str(c.agent.services()))

def unregister():
    log.info("unregister started")
    c = consul.Consul(host='localhost')
    c.agent.service.deregister("eye-pi-%d" % port)
    log.info("services: " + str(c.agent.services()))

if __name__ == '__main__':
    server = create_server()
    register()
    server.serve()
    unregister()