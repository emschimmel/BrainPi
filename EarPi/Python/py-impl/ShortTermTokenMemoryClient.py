import random
import sys
sys.path.append('../gen-py')
from ShortMemory import ShortMemoryService
from ShortMemory.ttypes import TokenObject

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from dns import resolver
sys.path.append('../../../')
import config

import time
import datetime
# ShortTermMemoryClient.py

class ShortTermTokenMemoryClient:
    def __init__(self):
        self.log = {}

    @classmethod
    def getToken(self, earPiAuthObject):
        print('short term memory handler')
        inputToken = TokenObject()
        inputToken.deviceToken = earPiAuthObject.deviceToken
        inputToken.token = earPiAuthObject.token
        ts = time.time()
        inputToken.date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S')
        inputToken.time = ts
        return self.__get_token_from_service(inputToken=inputToken)

    @classmethod
    def getDeviceList(self):
        print('short term memory handler')
        ip, port = self.__resolve_config()
        transport = TSocket.TSocket(ip, port)  # Make socket
        try:
            transport = TTransport.TBufferedTransport(transport)  # Buffering is critical. Raw sockets are very slow
            protocol = TBinaryProtocol.TBinaryProtocol(transport)  # Wrap in a protocol
            client = ShortMemoryService.Client(protocol)  # Create a client to use the protocol encoder
            transport.open()
            output = client.getDeviceList()
            transport.close()
            return output
        except Thrift.TException as tx:
            print('%s' % (tx.message))
        except Exception as ex:
            print('whot??? %s' % ex)
        finally:
            transport.close()

    @classmethod
    def confirmDevice(self, devicetoken, active):
        print('short term memory handler')
        ip, port = self.__resolve_config()
        transport = TSocket.TSocket(ip, port)  # Make socket
        try:
            transport = TTransport.TBufferedTransport(transport)  # Buffering is critical. Raw sockets are very slow
            protocol = TBinaryProtocol.TBinaryProtocol(transport)  # Wrap in a protocol
            client = ShortMemoryService.Client(protocol)  # Create a client to use the protocol encoder
            transport.open()
            client.confirmDevice(deviceToken=devicetoken, enabled=active)
            transport.close()
        except Thrift.TException as tx:
            print('%s' % (tx.message))
        except Exception as ex:
            print('whot??? %s' % ex)
        finally:
            transport.close()

    @classmethod
    def validateToken(self, earPiAuthObject):
        print('short term memory handler')
        ip, port = self.__resolve_config()
        transport = TSocket.TSocket(ip, port)  # Make socket
        try:
            transport = TTransport.TBufferedTransport(transport)  # Buffering is critical. Raw sockets are very slow
            protocol = TBinaryProtocol.TBinaryProtocol(transport)  # Wrap in a protocol
            client = ShortMemoryService.Client(protocol)  # Create a client to use the protocol encoder
            transport.open()  # Connect!

            output = client.validateToken(token=earPiAuthObject.token, deviceToken=earPiAuthObject.deviceToken)
            transport.close()
            return output
        except Thrift.TException as tx:
            print('%s' % (tx.message))
        except Exception as ex:
            print('whot??? %s' % ex)
        finally:
            transport.close()

    @classmethod
    def __get_token_from_service(self, inputToken):
        ip, port = self.__resolve_config()
        transport = TSocket.TSocket(ip, port)  # Make socket
        try:
            transport = TTransport.TBufferedTransport(transport)  # Buffering is critical. Raw sockets are very slow
            protocol = TBinaryProtocol.TBinaryProtocol(transport)  # Wrap in a protocol
            client = ShortMemoryService.Client(protocol)  # Create a client to use the protocol encoder
            transport.open()  # Connect!
            output = client.generateToken(token=inputToken)
            transport.close()
            return output
        except Thrift.TException as tx:
            print('%s' % (tx.message))
        except Exception as ex:
            print('whot??? %s' % ex)
        finally:
            transport.close()

    @staticmethod
    def __resolve_config():
        consul_resolver = resolver.Resolver()
        consul_resolver.port = config.consul_resolver_port
        consul_resolver.nameservers = [config.consul_ip]

        dnsanswer = consul_resolver.query("short-term-memory.service.consul.", 'A')
        ip = str(dnsanswer[0])
        dnsanswer_srv = consul_resolver.query("short-term-memory.service.consul.", 'SRV')
        port = int(str(random.choice(dnsanswer_srv)).split()[2])
        return ip, port