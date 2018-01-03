#!/usr/bin/env python
import signal
import sys

import consul
from multiprocessing.managers import SyncManager

import pickle

sys.path.append('../gen-py')
sys.path.append('../')

from GenericServerPi import GenericPiThriftService
from GenericStruct.ttypes import ActionEnum
from ThriftException.ttypes import ThriftServiceException
from WeatherPi.ttypes import WeatherOutput

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

sys.path.append('../../')
import config

from OpenWeather import OpenWeather

import logging
import random

import statsd
stat = statsd.StatsClient(config.statsd_ip, config.statsd_port)
port = random.randint(50000, 59000)

log = logging.getLogger()
log.setLevel(logging.DEBUG)

class WeatherPiThriftHandler:

    @stat.timer("WeatherPi.handleRequest")
    def handleRequest(self, input):
        print("weather pi!")
        try:
            input_object = pickle.loads(input, fix_imports=False, encoding="ASCII", errors="strict")
            wind, humidity, temperature = OpenWeather().getWeather(input=input_object.location)

            output = WeatherOutput()
            output.humidity = "%s" % humidity
            output.wind_speed = "%s" % wind['speed']
            output.wind_deg =  "%s" % wind['deg']
            output.temperature_temp = "%s" % temperature['temp']
            output.temperature_temp_max = "%s" % temperature['temp_max']
            output.temperature_temp_min = "%s" % temperature['temp_min']
            pickle_output = pickle.dumps(obj=output, protocol=None, fix_imports=False)
            return pickle_output

        except Exception as ex:
            print('invalid request %s' % ex)
            raise ThriftServiceException('WeatherPi', 'invalid request %s' % ex)

    @stat.timer("WeatherPi.getDefaultModuleConfig")
    def getDefaultModuleConfig(self):
        default_config = "string location"
        return pickle.dumps(obj=default_config, protocol=None, fix_imports=False)

    @stat.timer("WeatherPi.ping")
    def ping(self, input):
        print(input)

def get_ip():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('255.255.255.255', 1)) # isn't reachable intentionally
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def create_server():
    handler = WeatherPiThriftHandler()
    return TServer.TSimpleServer(
        GenericPiThriftService.Processor(handler),
        TSocket.TServerSocket(port=port),
        TTransport.TBufferedTransportFactory(),
        TBinaryProtocol.TBinaryProtocolFactory()
    )

def register():
    log.info("register started")
    c = consul.Consul(host=config.consul_ip, port=config.consul_port)
    key = '%d' % ActionEnum.WEATHER
    c.kv.put(key, 'weather')
    check = consul.Check.tcp(host=get_ip(), port=port, interval=config.consul_interval,
                             timeout=config.consul_timeout, deregister=unregister())
    c.agent.service.register(name="weather-pi", service_id="weather-pi-%d" % port, port=port, check=check)
    log.info("services: " + str(c.agent.services()))

def unregister():
    log.info("unregister started")
    c = consul.Consul(host=config.consul_ip, port=config.consul_port)
    c.agent.service.deregister("weather-pi-%d" % port)
    c.agent.service.deregister("weather-pi")
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
        print('finally WeatherPi shutting down')
        manager.shutdown()
