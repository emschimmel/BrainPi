import random

import sys
sys.path.append('../gen-py')
from LongMemory import LongMemoryService
from LongMemory.ttypes import *
from GenericStruct.ttypes import *
from ThriftException.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from dns import resolver
sys.path.append('../../')
import config

class ConnectLongMemory:

    def resolve_longmemory_config(self):
        consul_resolver = resolver.Resolver()
        consul_resolver.port = config.consul_resolver_port
        consul_resolver.nameservers = [config.consul_ip]
        dnsanswer = consul_resolver.query("long-term-memory.service.consul.", "A")
        ip = str(dnsanswer[0])
        dnsanswer_srv = consul_resolver.query("long-term-memory.service.consul.", "SRV")
        port = int(str(random.choice(dnsanswer_srv)).split()[2])
        return ip, port

    def getPersonConfig(self, input):
        try:
            ip, port = self.resolve_longmemory_config()
            transport = TSocket.TSocket(ip, port)
            transport = TTransport.TBufferedTransport(transport)
            protocol = TBinaryProtocol.TBinaryProtocol(transport)
            client = LongMemoryService.Client(protocol)
            transport.open()
            output = client.getPersonConfig(input)
            print(output)

            transport.close()
            return output

        except Thrift.TException as tx:
            print("%s" % (tx.message))

    def getAll(self):
        try:
            ip, port = self.resolve_longmemory_config()
            transport = TSocket.TSocket(ip, port)
            transport = TTransport.TBufferedTransport(transport)
            protocol = TBinaryProtocol.TBinaryProtocol(transport)
            client = LongMemoryService.Client(protocol)
            transport.open()
            output = client.getAll()
            print(output)

            transport.close()
            return output

        except Thrift.TException as tx:
            print("%s" % (tx.message))

    def storeNewPerson(self, input):
        try:
            ip, port = self.resolve_longmemory_config()
            transport = TSocket.TSocket(ip, port)
            transport = TTransport.TBufferedTransport(transport)
            protocol = TBinaryProtocol.TBinaryProtocol(transport)
            client = LongMemoryService.Client(protocol)
            transport.open()
            client.storeNewPerson(input)

            transport.close()
        except Thrift.TException as tx:
            print("%s" % (tx.message))

    def login(self, input):
        try:
            ip, port = self.resolve_longmemory_config()
            transport = TSocket.TSocket(ip, port)
            transport = TTransport.TBufferedTransport(transport)
            protocol = TBinaryProtocol.TBinaryProtocol(transport)
            client = LongMemoryService.Client(protocol)
            transport.open()
            output = client.loginCall(input)

            transport.close()
            return output
        except Thrift.TException as tx:
            print("%s" % (tx.message))





