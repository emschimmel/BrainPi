import signal
import sys

import consul
from multiprocessing.managers import SyncManager

sys.path.append('../gen-py')
from LongMemory import LongMemoryService
from LongMemory.ttypes import *

from Memory.PersonMemory import PersonMemory
from Memory.AutorisationActions import AutorisationActions

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

sys.path.append('../../')
import config
import logging
import random
import statsd

port = random.randint(50000, 59000)
stat = statsd.StatsClient(config.statsd_ip, config.statsd_port)

log = logging.getLogger()
log.setLevel(logging.DEBUG)

class LongTermMemoryThriftServer:
    def __init__(self):
        self.log = {}

    @stat.timer("loginCall")
    def loginCall(self, loginobject):
        try:
            output = LongMemoryLoginOutputObject()
            output.person = AutorisationActions().login(loginobject)
            return output
        except Exception as ex:
            raise BadHashException()

    @stat.timer("getPersonConfig")
    def getPersonConfig(self, uniquename):
        try:
            return PersonMemory().getPerson(uniquename)
        except Exception as ex:
            print('invalid request %s' % ex)

    @stat.timer("storeNewPerson")
    def storeNewPerson(self, person):
        try:
            PersonMemory().storeNewPerson(person=person)
        except Exception as ex:
            print('invalid request %s' % ex)

    @stat.timer("changePassword")
    def changePassword(self, username, password):
        try:
            AutorisationActions().changePassword(username, password)
        except Exception as ex:
            raise BadHashException()

    def getAll(self):
        try:
            return PersonMemory().getAll()
        except Exception as ex:
            print('invalid request %s' % ex)

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
    handler = LongTermMemoryThriftServer()
    return TServer.TSimpleServer(
        LongMemoryService.Processor(handler),
        TSocket.TServerSocket(port=port),
        TTransport.TBufferedTransportFactory(),
        TBinaryProtocol.TBinaryProtocolFactory()
    )

def register():
    log.info("register started")
    c = consul.Consul(host=config.consul_ip, port=config.consul_port)
    check = consul.Check.tcp(host=get_ip(), port=port, interval=config.consul_interval,
                             timeout=config.consul_timeout, deregister=unregister())
    c.agent.service.register(name="long-term-memory", service_id="long-term-memory-%d" % port, port=port, check=check)
    log.info("services: " + str(c.agent.services()))

def unregister():
    log.info("unregister started")
    c = consul.Consul(host=config.consul_ip, port=config.consul_port)
    c.agent.service.deregister("long-term-memory-%d" % port)
    c.agent.service.deregister("long-term-memory")
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
        print('finally Long term memory Shutting down')
        manager.shutdown()