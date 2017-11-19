#!/usr/bin/env python

import sys

sys.path.append('../gen-py')
sys.path.append('../')

from WeatherPi import WeatherPiThriftService
from WeatherPi.ttypes import *
from ThriftException.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# import cv2
sys.path.append('../../')
import config


class WeatherPiThriftHandler:
    def __init__(self):
        self.log = {}

    def handleRequest(self, input):
        try:
            print(input)
            output = WeatherPiOutput()
            output.temperature = 12
            print(output)
            return output

        except Exception as ex:
            print('invalid request %s' % ex)
            raise ThriftServiceException('WeatherPi', 'invalid request %s' % ex)


handler = WeatherPiThriftHandler()
processor = WeatherPiThriftService.Processor(handler)
transport = TSocket.TServerSocket(port=config.weather_pi_port)

tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print("Starting python weather server...")
server.serve()
print("done!")
