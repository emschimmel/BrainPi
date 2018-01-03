#!/usr/bin/env python
import signal
import sys

import consul
from multiprocessing.managers import SyncManager

import pickle

sys.path.append('../gen-py')

from GenericServerPi import GenericPiThriftService
from GenericStruct.ttypes import ActionEnum
from ThriftException.ttypes import ThriftServiceException
from LightPi.ttypes import Action
from LightPi.ttypes import GenericOkOutput

from Domain.FloorLayout import FloorLayout
from Connect.ControlLightwaveRF import ControlLightwaveRF

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

sys.path.append('../../')
import config

import logging
import random

import statsd
stat = statsd.StatsClient(config.statsd_ip, config.statsd_port)
port = random.randint(50000, 59000)

log = logging.getLogger()
log.setLevel(logging.DEBUG)

class LightPiThriftHandler:
    def __init__(self):
        self.log = {}

    @stat.timer("handleRequest")
    def handleRequest(self, input):
        print("weather pi!")
        try:
            input_object = pickle.loads(input, fix_imports=False, encoding="ASCII", errors="strict")
            output = GenericOkOutput()
            if input_object.action is Action.GET_FLOOR_LAYOUT:
                output = FloorLayout.getLayout()
            elif input_object.action is Action.UPDATE_FLOOR_LAYOUT:
                FloorLayout.storeLayout(input_object)
            elif input_object.action is Action.PERFORM_ACTION:
                ControlLightwaveRF().handleInput(input_object)

            pickle_output = pickle.dumps(obj=output, protocol=None, fix_imports=False)
            return pickle_output

        except Exception as ex:
            print('invalid request %s' % ex)
            raise ThriftServiceException('WeatherPi', 'invalid request %s' % ex)

    @stat.timer("ping")
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
    handler = LightPiThriftHandler()
    return TServer.TSimpleServer(
        GenericPiThriftService.Processor(handler),
        TSocket.TServerSocket(port=port),
        TTransport.TBufferedTransportFactory(),
        TBinaryProtocol.TBinaryProtocolFactory()
    )

def register():
    log.info("register started")
    c = consul.Consul(host=config.consul_ip, port=config.consul_port)
    key = '%d' % ActionEnum.LIGHT
    c.kv.put(key, 'light')
    check = consul.Check.tcp(host=get_ip(), port=port, interval=config.consul_interval,
                             timeout=config.consul_timeout, deregister=unregister())
    c.agent.service.register(name="light-pi", service_id="light-pi-%d" % port, port=port, check=check)
    log.info("services: " + str(c.agent.services()))

def unregister():
    log.info("unregister started")
    c = consul.Consul(host=config.consul_ip, port=config.consul_port)
    c.agent.service.deregister("light-pi-%d" % port)
    c.agent.service.deregister("light-pi")
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
        print('finally LightPi shutting down')
        manager.shutdown()
