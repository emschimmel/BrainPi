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
stat = statsd.StatsClient('localhost', 8125)

log = logging.getLogger()
log.setLevel(logging.DEBUG)

class LongTermMemoryThriftServer:
    def __init__(self):
        self.log = {}

    @stat.timer("loginCall")
    def loginCall(self, loginobject):
        try:
            return AutorisationActions().login(loginobject)
        except Exception as ex:
            raise BadHashException()

    @stat.timer("getPersonConfig")
    def getPersonConfig(self, uniquename):
        try:
            PersonMemory().getPerson(uniquename)
        except Exception as ex:
            print('invalid request %s' % ex)

    @stat.timer("changePassword")
    def changePassword(self, username, password):
        try:
            AutorisationActions().changePassword(username, password)
        except Exception as ex:
            raise BadHashException()


def create_server(host=config.long_storage_ip):
    handler = LongTermMemoryThriftServer()
    return TServer.TSimpleServer(
        LongMemoryService.Processor(handler),
        TSocket.TServerSocket(host=host, port=port),
        TTransport.TBufferedTransportFactory(),
        TBinaryProtocol.TBinaryProtocolFactory()
    )

def register():
    log.info("register started")
    c = consul.Consul(host='localhost')
    check = consul.Check = {'script': 'ps | awk -F" " \'/LongTermMemoryServer.py/ && !/awk/{print $1}\'',
                                    'id': 'long-term-memory-%d' % port, 'name': 'long_term_memory process tree check', 'Interval': config.consul_interval,
                                    'timeout': config.consul_timeout}
    c.agent.service.register(name="long-term-memory", service_id="long-term-memory-%d" % port, address=config.long_storage_ip, port=port, check=check)
    log.info("services: " + str(c.agent.services()))

def unregister():
    log.info("unregister started")
    c = consul.Consul(host='localhost')
    c.agent.service.deregister("long-term-memory-%d" % port)
    c.agent.service.deregister("long-term-memory")
    log.info("services: " + str(c.agent.services()))
    print(str(c.agent.services()))

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