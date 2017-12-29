import random
import sys
sys.path.append('../gen-py')
from LongMemory import LongMemoryService
from LongMemory.ttypes import *
from LongMemory.ttypes import *
from ThriftException.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from dns import resolver
sys.path.append('../../')
import config

class LongTermPersonMemoryClient:
    def __init__(self):
        self.log = {}

    def loginCall(self, loginInput):
        print('Long term memory handler, login %s' % input)
        try:
            lmLoginInput = LongMemoryLoginInputObject()
            lmLoginInput.username = loginInput.username
            lmLoginInput.password = loginInput.password
            lmLoginInput.code = loginInput.code
            ip, port = self.resolve_config()
            transport = TSocket.TSocket(ip, port)  # Make socket
            transport = TTransport.TBufferedTransport(transport)  # Buffering is critical. Raw sockets are very slow
            protocol = TBinaryProtocol.TBinaryProtocol(transport)  # Wrap in a protocol
            client = LongMemoryService.Client(protocol)  # Create a client to use the protocol encoder
            transport.open()  # Connect!
            person = client.loginCall(lmLoginInput)
            transport.close()
            return person
        except Thrift.TException as tx:
            print('%s' % (tx.message))
            raise tx
        except BadHashException as badHash:
            print('Bad hash %s' % badHash)
            raise badHash

    def get_Person(self, input):
        print('Long term memory handler, get Person %s' % input)
        try:
            ip, port = self.resolve_config()
            transport = TSocket.TSocket(ip, port)  # Make socket
            transport = TTransport.TBufferedTransport(transport)  # Buffering is critical. Raw sockets are very slow
            protocol = TBinaryProtocol.TBinaryProtocol(transport)  # Wrap in a protocol
            client = LongMemoryService.Client(protocol)  # Create a client to use the protocol encoder
            transport.open()  # Connect!
            person = client.getPersonConfig(input)
            transport.close()
            return person
        except Thrift.TException as tx:
            print('%s' % (tx.message))
        except Exception as ex:
            print('whot??? %s' % ex)

    def resolve_config(self):
        consul_resolver = resolver.Resolver()
        consul_resolver.port = config.consul_resolver_port
        consul_resolver.nameservers = [config.consul_ip]

        dnsanswer = consul_resolver.query("long-term-memory.service.consul.", 'A')
        ip = str(dnsanswer[0])
        dnsanswer_srv = consul_resolver.query("long-term-memory.service.consul.", 'SRV')
        port = int(str(random.choice(dnsanswer_srv)).split()[2])
        return ip, port

