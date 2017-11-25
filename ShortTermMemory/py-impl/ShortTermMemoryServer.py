import sys

import consul

sys.path.append('../gen-py')
from ShortMemory import ShortMemoryService
from ShortMemory.ttypes import *

from TokenMemory import TokenMemory
from LogMemory import LogMemory

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

class ShortTermMemoryThriftServer:
    def __init__(self):
        self.log = {}

    @stat.timer("generateToken")
    def generateToken(self, tokenObject):
        try:
            return TokenMemory().generateToken(tokenObject)
        except Exception as ex:
            print('invalid request %s' % ex)

    @stat.timer("validateToken")
    def validateToken(self, stringToken, deviceToken):
        try:
            return TokenMemory().validateToken(stringToken, deviceToken)
        except Exception as ex:
            print('invalid request %s' % ex)

    @stat.timer("writeLog")
    def writeLog(self, log):
        try:
            LogMemory().storeLog(log)
        except Exception as ex:
            print('invalid request %s' % ex)

    @stat.timer("readLog")
    def readLog(self, starttime, endtime, amount):
        try:
            return LogMemory().getLog(starttime, endtime, amount)
        except Exception as ex:
            print('invalid request %s' % ex)

def create_server(host=config.short_storage_ip):
    handler = ShortTermMemoryThriftServer()
    return TServer.TSimpleServer(
        ShortMemoryService.Processor(handler),
        TSocket.TServerSocket(host=host, port=port),
        TTransport.TBufferedTransportFactory(),
        TBinaryProtocol.TBinaryProtocolFactory()
    )

def register():
    log.info("register started")
    c = consul.Consul(host='localhost')
    #check = consul.Check.tcp("127.0.0.1", port, "30s")
    check = consul.Check = {'script': 'ps | awk -F" " \'/ShortTermMemoryServer.py/ && !/awk/{print $1}\'',
                                    'id': 'eye_pi', 'name': 'short_term_memory process tree check', 'Interval': '10s',
                                    'timeout': '2s'}
    c.agent.service.register("short-term-memory", "short-term-memory-%d" % port, address=config.short_storage_ip, port=port, check=check)
    log.info("services: " + str(c.agent.services()))

def unregister():
    log.info("unregister started")
    c = consul.Consul(host='localhost')
    c.agent.service.deregister("short-term-memory-%d" % port)
    log.info("services: " + str(c.agent.services()))

if __name__ == '__main__':
    server = create_server()
    register()
    server.serve()
    unregister()