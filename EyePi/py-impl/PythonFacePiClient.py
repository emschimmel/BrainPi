#!/usr/bin/env python
 
import sys
sys.path.append('../gen-py')
 
from FacePi import FacePiThriftService
from FacePi.ttypes import *
from FacePi.constants import *
 
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from dns import resolver

class FacePiThriftClient:

    def __init__(self):
        self.log = {}

    def handle_request(self, image):
        try:
            ip, port = self.resolve_config()
            transport = TSocket.TSocket(ip, port)     # Make socket
            transport = TTransport.TBufferedTransport(transport) # Buffering is critical. Raw sockets are very slow
            protocol = TBinaryProtocol.TBinaryProtocol(transport) # Wrap in a protocol
            client = FacePiThriftService.Client(protocol) # Create a client to use the protocol encoder
            transport.open()        # Connect!

            input = FacePiInput()
            input.image = image
            output = client.handleRequest(input)
            print(output)
            transport.close()
            return output.personCollection

        except Thrift.TException as tx:
            print ('%s' % (tx.message))
            raise tx

    def confim_face(self, input):
        try:
            ip, port = self.resolve_config()
            transport = TSocket.TSocket(ip, port)     # Make socket
            transport = TTransport.TBufferedTransport(transport) # Buffering is critical. Raw sockets are very slow
            protocol = TBinaryProtocol.TBinaryProtocol(transport) # Wrap in a protocol
            client = FacePiThriftService.Client(protocol) # Create a client to use the protocol encoder
            transport.open()        # Connect!

            # input = ConfirmInput()
            # input.image = image
            # input.person = person
            client.confimFace(input)
            transport.close()
        except Thrift.TException as tx:
            print('%s' % (tx.message))
            raise ThriftServiceException('FacePi', tx.message)
        except ThriftServiceException as tex:
            print('thrift exception request %s' % tex)
            raise tex
        except ExternalEndpointUnavailable as endEx:
            print('endpoint exception request %s' % endEx)
            raise endEx
        except Exception as ex:
            print('whot??? %s' % ex)
            raise ex

    def resolve_config(self):
        consul_resolver = resolver.Resolver()
        consul_resolver.port = 8600
        consul_resolver.nameservers = ["127.0.0.1"]

        dnsanswer = consul_resolver.query("face-pi.service.consul.", 'A')
        ip = str(dnsanswer[0])
        dnsanswer_srv = consul_resolver.query("face-pi.service.consul.", 'SRV')
        port = int(str(dnsanswer_srv[0]).split()[2])
        return ip, port