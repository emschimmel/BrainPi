#!/usr/bin/env python

import sys

sys.path.append('../gen-py')
sys.path.append('../')

from GenericServerPi import GenericPiThriftService
from GenericServerPi.ttypes import *
from GenericStruct.ttypes import *
from ThriftException.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# import cv2
sys.path.append('../../')
import config

from OpenWeather import OpenWeather

class WeatherPiThriftHandler:
    def __init__(self):
        self.log = {}

    def handleRequest(self, input):
        try:

            wind, humidity, temperature = OpenWeather().getWeather('Amsterdam,nl')

            output = GenericObject()
            output.mapValue = {'humidity': self.createStringValue(humidity),
                               'wind-speed': self.createStringValue(wind['speed']),
                               'wind-deg': self.createStringValue(wind['deg']),
                               'temperature-temp': self.createStringValue(temperature['temp']),
                               'temperature-temp_max': self.createStringValue(temperature['temp_max']),
                               'temperature-temp_min': self.createStringValue(temperature['temp_min'])}

            return output

        except Exception as ex:
            print('invalid request %s' % ex)
            raise ThriftServiceException('WeatherPi', 'invalid request %s' % ex)

    def createStringValue(self, input):
        value = GenericSubStruct()
        value.stringValue = "%s" % input
        return value

    ### External ###
    def ping(self, input):
        print(input)

handler = WeatherPiThriftHandler()
processor = GenericPiThriftService.Processor(handler)
transport = TSocket.TServerSocket(port=config.weather_pi_port)

tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print("Starting python weather server...")
server.serve()
print("done!")
