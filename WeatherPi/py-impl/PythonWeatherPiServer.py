#!/usr/bin/env python
import signal
import sys

import consul
from multiprocessing.managers import SyncManager

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

import logging
import random

import statsd
stat = statsd.StatsClient('localhost', 8125)
port = random.randint(50000, 59000)

log = logging.getLogger()
log.setLevel(logging.DEBUG)

class WeatherPiThriftHandler:
    def __init__(self):
        self.log = {}

    @stat.timer("handleRequest")
    def handleRequest(self, input):
        print("weather pi!")
        try:
            wind, humidity, temperature = OpenWeather().getWeather(input.stringValue)

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

    @stat.timer("ping")
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
    c = consul.Consul(host='localhost')
    key = '%d' % ActionEnum.WEATHER
    c.kv.put(key, 'weather')
    #check = consul.Check.tcp("127.0.0.1", port, "30s")
    check = consul.Check = {'script': 'ps | awk -F" " \'/PythonWeatherPiServer.py/ && !/awk/{print $1}\'',
             'id': 'eye_pi', 'name': 'weather_pi process tree check', 'Interval': config.consul_interval,
             'timeout': config.consul_timeout}
    c.agent.service.register("weather-pi", "weather-pi-%d" % port, address=config.weather_pi_ip, port=port, check=check)
    log.info("services: " + str(c.agent.services()))

def unregister():
    log.info("unregister started")
    c = consul.Consul(host='localhost')
    c.agent.service.deregister("weather-pi-%d" % port)
    log.info("services: " + str(c.agent.services()))

def interupt_manager():
    signal.signal(signal.SIGINT, signal.SIG_IGN)

if __name__ == '__main__':
    manager = SyncManager()
    manager.start(interupt_manager)
    try:
        server = create_server()
        register()
        server.serve()

    finally:
        unregister()
        print('finally')
        manager.shutdown()
