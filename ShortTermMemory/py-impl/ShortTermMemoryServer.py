import sys

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

class ShortTermMemoryThriftServer:
    def __init__(self):
        self.log = {}

    def getToken(self, tokenObject):
        try:
            return TokenMemory().generateToken(tokenObject)
        except Exception as ex:
            print('invalid request %s' % ex)

    def validateToken(self, stringToken, deviceToken):
        try:
            return TokenMemory().validateToken(stringToken, deviceToken)
        except Exception as ex:
            print('invalid request %s' % ex)

    def writeLog(self, log):
        try:
            LogMemory().storeLog(log)
        except Exception as ex:
            print('invalid request %s' % ex)

    def readLog(self, starttime, endtime, amount):
        try:
            return LogMemory().getLog(starttime, endtime, amount)
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