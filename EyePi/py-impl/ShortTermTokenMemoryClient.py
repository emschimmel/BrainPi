import random
import sys
sys.path.append('../gen-py')
from ShortMemory import ShortMemoryService
from ShortMemory.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from dns import resolver

import time
import datetime
# ShortTermMemoryClient.py

class ShortTermTokenMemoryClient:
    def __init__(self):
        self.log = {}
    def getToken(self, eyeInput):
        print('short term memory handler')
        inputToken = TokenObject()
        inputToken.deviceToken = eyeInput.deviceToken
        inputToken.token = eyeInput.token
        inputToken.image = eyeInput.image
        ts = time.time()
        inputToken.date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S')
        inputToken.time = ts
        return self.get_token_from_service(inputToken)

    def validateToken(self, inputToken, deviceToken):
        print('short term memory handler')
        try:
            ip, port = self.resolve_config()
            transport = TSocket.TSocket(ip, port)  # Make socket
            transport = TTransport.TBufferedTransport(transport)  # Buffering is critical. Raw sockets are very slow
            protocol = TBinaryProtocol.TBinaryProtocol(transport)  # Wrap in a protocol
            client = ShortMemoryService.Client(protocol)  # Create a client to use the protocol encoder
            transport.open()  # Connect!

            output = client.validateToken(inputToken, deviceToken)
            print(output)
            transport.close()
            return output

        except Thrift.TException as tx:
            print('%s' % (tx.message))
        except Exception as ex:
            print('whot??? %s' % ex)
    def get_token_from_service(self, inputToken):
        outputToken = False
        try:
            ip, port = self.resolve_config()
            transport = TSocket.TSocket(ip, port)  # Make socket
            transport = TTransport.TBufferedTransport(transport)  # Buffering is critical. Raw sockets are very slow
            protocol = TBinaryProtocol.TBinaryProtocol(transport)  # Wrap in a protocol
            client = ShortMemoryService.Client(protocol)  # Create a client to use the protocol encoder
            transport.open()  # Connect!
            outputToken = client.generateToken(inputToken)

            transport.close()

        except Thrift.TException as tx:
            print('%s' % (tx.message))
        except Exception as ex:
            print('whot??? %s' % ex)
        return outputToken

    def resolve_config(self):
        consul_resolver = resolver.Resolver()
        consul_resolver.port = 8600
        consul_resolver.nameservers = ["127.0.0.1"]

        dnsanswer = consul_resolver.query("short-term-memory.service.consul.", 'A')
        ip = str(dnsanswer[0])
        dnsanswer_srv = consul_resolver.query("short-term-memory.service.consul.", 'SRV')
        port = int(str(random.choice(dnsanswer_srv)).split()[2])
        return ip, port