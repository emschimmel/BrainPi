#!/usr/bin/env python

import sys

import consul

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

import logging
import random

port = random.randint(50000, 59000)

log = logging.getLogger()
log.setLevel(logging.DEBUG)


class WeatherPiThriftHandler:
    def __init__(self):
        self.log = {}

    def handleRequest(self, input):
        try:
            print(input)
            output = GenericObject()

            ### if map structure ###
            value = GenericSubStruct()
            value.intValue = 12
            print(value)
            output.mapValue = {'temperature': value}

            ### if int structure ###
            output.intValue = 12
            print(output)
            return output

        except Exception as ex:
            print('invalid request %s' % ex)
            raise ThriftServiceException('WeatherPi', 'invalid request %s' % ex)

    ### External ###
    def ping(self, input):
        print(input)

def create_server(host=config.weather_pi_ip):
    handler = WeatherPiThriftHandler()
    return TServer.TSimpleServer(
        GenericPiThriftService.Processor(handler),
        TSocket.TServerSocket(host=host, port=port),
        TTransport.TBufferedTransportFactory(),
        TBinaryProtocol.TBinaryProtocolFactory()
    )

def register():
    log.info("register started")
    c = consul.Consul()
    #check = consul.Check.tcp("127.0.0.1", port, "30s")
    check = consul.Check = {'script': 'ps | awk -F" " \'/PythonWeatherPiServer.py/ && !/awk/{print $1}\'',
             'id': 'eye_pi', 'name': 'weather_pi process tree check', 'Interval': '10s',
             'timeout': '2s'}
    c.agent.service.register("weather-pi", "weather-pi-%d" % port, address=config.weather_pi_ip, port=port, check=check)
    log.info("services: " + str(c.agent.services()))

def unregister():
    log.info("unregister started")
    c = consul.Consul()
    c.agent.service.deregister("weather-pi-%d" % port)
    log.info("services: " + str(c.agent.services()))

if __name__ == '__main__':
    server = create_server()
    register()
    server.serve()
    unregister()
