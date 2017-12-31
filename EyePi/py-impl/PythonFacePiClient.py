#!/usr/bin/env python
import random
import sys
sys.path.append('../gen-py')
 
from FacePi import FacePiThriftService
from FacePi.ttypes import FacePiInput

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from ThriftException.ttypes import ThriftServiceException
from ThriftException.ttypes import ExternalEndpointUnavailable

from dns import resolver
sys.path.append('../../')
import config

class FacePiThriftClient:

    def __init__(self):
        self.log = {}

    def handle_request(self, image):
        ip, port = self.__resolve_config()
        transport = TSocket.TSocket(ip, port)  # Make socket
        try:
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
        finally:
            transport.close()

    def confim_face(self, input):
        ip, port = self.__resolve_config()
        transport = TSocket.TSocket(ip, port)  # Make socket
        try:
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
        finally:
            transport.close()

    def __resolve_config(self):
        consul_resolver = resolver.Resolver()
        consul_resolver.port = config.consul_resolver_port
        consul_resolver.nameservers = [config.consul_ip]

        dnsanswer = consul_resolver.query("face-pi.service.consul.", 'A')
        ip = str(dnsanswer[0])
        dnsanswer_srv = consul_resolver.query("face-pi.service.consul.", 'SRV')
        port = int(str(random.choice(dnsanswer_srv)).split()[2])
        return ip, port