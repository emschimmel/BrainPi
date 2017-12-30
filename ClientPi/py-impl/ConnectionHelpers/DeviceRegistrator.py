import random

import sys
sys.path.append('../gen-py')
from ShortMemory import ShortMemoryService
from AutorisationStruct.ttypes import DeviceTokenInput

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from dns import resolver

sys.path.append('../../')
import config

class DeviceRegistrator:

    device_token = None

    def resolve_stm_config(self):
        consul_resolver = resolver.Resolver()
        consul_resolver.port = config.consul_resolver_port
        consul_resolver.nameservers = [config.consul_ip]

        dnsanswer = consul_resolver.query("short-term-memory.service.consul.", 'A')
        ip = str(dnsanswer[0])
        dnsanswer_srv = consul_resolver.query("short-term-memory.service.consul.", 'SRV')
        port = int(str(random.choice(dnsanswer_srv)).split()[2])
        return ip, port

    def register_device(self):
        if not self.device_token:
            ip, port = self.resolve_stm_config()
            transport = TSocket.TSocket(ip, port)  # Make socket
            try:
                transport = TTransport.TBufferedTransport(transport)  # Buffering is critical. Raw sockets are very slow
                protocol = TBinaryProtocol.TBinaryProtocol(transport)  # Wrap in a protocol
                client = ShortMemoryService.Client(protocol)  # Create a client to use the protocol encoder
                transport.open()  # Connect!
                inputDevice = DeviceTokenInput()
                inputDevice.ip = '127.0.0.1'
                inputDevice.devicetype = 'Development'
                self.device_token = client.generateDeviceToken(inputDevice)
                transport.close()
            except Thrift.TException as tx:
                print('%s' % (tx.message))
            except Exception as ex:
                print('whot??? %s' % ex)
            finally:
                transport.close()
        return self.device_token

