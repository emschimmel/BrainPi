#!/usr/bin/env python
import signal
import sys

import consul
from multiprocessing.managers import SyncManager

import pickle
sys.path.append('./gen-py')

from GenericServerPi import GenericPiThriftService
from GenericStruct.ttypes import ActionEnum
from ThriftException.ttypes import ThriftServiceException
from ThriftException.ttypes import ExternalEndpointUnavailable
from PhonePi.ttypes import Action

from IPhoneConnect import IPhoneConnect

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
port = random.randint(58800, 58810)

log = logging.getLogger()
log.setLevel(logging.DEBUG)

class PhonePiThriftHandler:
    # GET_LOCATION = 0
    # GET_STATUS = 1
    # PLAY_SOUND = 2
    # LOST_MODE = 3

    @stat.timer("PhonePi.handleRequest")
    def handleRequest(self, input):
        print("phone pi!")
        try:
            input_object = pickle.loads(input, fix_imports=False, encoding="ASCII", errors="strict")
            output = ""
            if input_object.action is Action.GET_LOCATION:
                output = IPhoneConnect().getLocation(input_object)
            elif input_object.action is Action.GET_STATUS:
                output = IPhoneConnect().getStatus(input_object)
            elif input_object.action is Action.PLAY_SOUND:
                output = IPhoneConnect().playSound(input_object)
            elif input_object.action is Action.LOST_MODE:
                if input_object.phonenumber is None:
                    exception = ThriftServiceException()
                    exception.serviceName = 'PhonePi'
                    exception.message = 'Phone number required for lost phone'
                    raise ThriftServiceException()
                output = IPhoneConnect().lostMode(input_object)
            else:
                output = "NOT IMPLEMENTED YET"

            pickle_output = pickle.dumps(obj=output, protocol=None, fix_imports=False)
            return pickle_output
        except ExternalEndpointUnavailable as endPoint:
            raise endPoint
        except Exception as ex:
            print('invalid request %s' % ex)
            raise ThriftServiceException('PhonePi', 'invalid request %s' % ex)

    @stat.timer("PhonePi.getDefaultModuleConfig")
    def getDefaultModuleConfig(self):
        default_config = "email string"
        return pickle.dumps(obj=default_config, protocol=None, fix_imports=False)

    @stat.timer("PhonePi.ping")
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
    handler = PhonePiThriftHandler()
    return TServer.TSimpleServer(
        GenericPiThriftService.Processor(handler),
        TSocket.TServerSocket(port=port),
        TTransport.TBufferedTransportFactory(),
        TBinaryProtocol.TBinaryProtocolFactory()
    )

def register():
    log.info("register started")
    c = consul.Consul(host=config.consul_ip, port=config.consul_port)
    key = '%d' % ActionEnum.PHONE
    c.kv.put(key, 'phone')
    check = consul.Check.tcp(host=get_ip(), port=port, interval=config.consul_interval,
                             timeout=config.consul_timeout, deregister=unregister())
    c.agent.service.register(name="phone-pi", service_id="phone-pi-%d" % port, port=port, check=check)
    log.info("services: " + str(c.agent.services()))

def unregister():
    log.info("unregister started")
    c = consul.Consul(host=config.consul_ip, port=config.consul_port)
    c.agent.service.deregister("phone-pi-%d" % port)
    c.agent.service.deregister("phone-pi")
    log.info("services: " + str(c.agent.services()))

def interupt_manager():
    signal.signal(signal.SIGINT, signal.SIG_IGN)

def main(args=None):
    manager = SyncManager()
    manager.start(interupt_manager)
    try:
        server = create_server()
        register()
        server.serve()

    finally:
        unregister()
        print('finally PhonePi shutting down')
        manager.shutdown()

if __name__ == '__main__':
    main()
