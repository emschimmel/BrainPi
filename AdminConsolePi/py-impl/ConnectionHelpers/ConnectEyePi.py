import random

import sys
sys.path.append('../gen-py')
from EyePi import EyePiThriftService
from EyePi.ttypes import *
from GenericStruct.ttypes import *
from ThriftException.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from dns import resolver
sys.path.append('../../')
import config

class ConnectEyePi:

    def resolve_eye_config(self):
        consul_resolver = resolver.Resolver()
        consul_resolver.port = config.consul_resolver_port
        consul_resolver.nameservers = [config.consul_ip]
        dnsanswer = consul_resolver.query("eye-pi.service.consul.", "A")
        ip = str(dnsanswer[0])
        dnsanswer_srv = consul_resolver.query("eye-pi.service.consul.", "SRV")
        port = int(str(random.choice(dnsanswer_srv)).split()[2])
        return ip, port

    def login(self, input):
        try:
            ip, port = self.resolve_eye_config()
            transport = TSocket.TSocket(ip, port)
            transport = TTransport.TBufferedTransport(transport)
            protocol = TBinaryProtocol.TBinaryProtocol(transport)
            client = EyePiThriftService.Client(protocol)
            transport.open()
            output = client.login(input)
            print(output)

            transport.close()
            return output

        except Thrift.TException as tx:
            print("%s" % (tx.message))


    def handleRequest(self, input):
        try:
            ip, port = self.resolve_eye_config()
            transport = TSocket.TSocket(ip, port)
            transport = TTransport.TBufferedTransport(transport)
            protocol = TBinaryProtocol.TBinaryProtocol(transport)
            client = EyePiThriftService.Client(protocol)
            transport.open()
            output = client.handleRequest(input)
            print(output)
            if output.ok:
                print("YAY!")

            transport.close()
            return output

        except Thrift.TException as tx:
            print("%s" % (tx.message))

    def confimFace(self, input):
        try:
            ip, port = self.resolve_eye_config()
            transport = TSocket.TSocket(ip, port)
            transport = TTransport.TBufferedTransport(transport)
            protocol = TBinaryProtocol.TBinaryProtocol(transport)
            client = EyePiThriftService.Client(protocol)
            transport.open()
            client.confimFace(input)

            transport.close()

        except Thrift.TException as tx:
            print("%s" % (tx.message))

    def writeLog(self, input):
        try:
            ip, port = self.resolve_eye_config()
            transport = TSocket.TSocket(ip, port)
            transport = TTransport.TBufferedTransport(transport)
            protocol = TBinaryProtocol.TBinaryProtocol(transport)
            client = EyePiThriftService.Client(protocol)
            transport.open()
            client.writeLog(input)

            transport.close()

        except Thrift.TException as tx:
            print("%s" % (tx.message))



