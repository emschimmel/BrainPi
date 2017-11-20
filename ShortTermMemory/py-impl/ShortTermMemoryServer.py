import sys

sys.path.append('../gen-py')
from ShortMemory import ShortMemoryService
from ShortMemory.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

sys.path.append('../../')
import config

class ShortTermMemoryThriftServer:
    def __init__(self):
        self.log = {}

    def getPerson(self, token):
        try:
            print(token)
            return token
        except Exception as ex:
            print('invalid request %s' % ex)

    def getToken(self, token):
        try:
            print(token)
            return token
        except Exception as ex:
            print('invalid request %s' % ex)

    def writeToken(self, token):
        try:
            print(token)
        except Exception as ex:
            print('invalid request %s' % ex)

    def writeLog(self, log):
        try:
            print(log.key)
        except Exception as ex:
            print('invalid request %s' % ex)

    def readLog(self, starttime, endtime, amount):
        try:
            print(starttime)
            print(endtime)
            print(amount)
        except Exception as ex:
            print('invalid request %s' % ex)

handler = ShortTermMemoryThriftServer()
processor = ShortMemoryService.Processor(handler)
transport = TSocket.TServerSocket(port=config.short_storage_port)

tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print("Starting python server...")
server.serve()
print("done!")