#!/usr/bin/env python

import sys

sys.path.append('../gen-py')

from GenericStruct.ttypes import *
from GenericStruct.constants import *
from GenericServerPi import GenericPiThriftService
from GenericServerPi.ttypes import *
from GenericServerPi.constants import *
from ThriftException.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from dns import resolver

class GenericThriftClient:
    def __init__(self):
        self.log = {}

    def handle_request(self, action, input):
        print('generic handler %s' % action)
        try:
            ip, port = self.resolve_config(action)
            transport = TSocket.TSocket(ip, port)  # Make socket
            transport = TTransport.TBufferedTransport(transport)  # Buffering is critical. Raw sockets are very slow
            protocol = TBinaryProtocol.TBinaryProtocol(transport)  # Wrap in a protocol
            client = GenericPiThriftService.Client(protocol)  # Create a client to use the protocol encoder
            transport.open()  # Connect!

            output = client.handleRequest(input)
            print(output)
            transport.close()
            return output

        except Thrift.TException as tx:
            print('%s' % (tx.message))
            raise ThriftServiceException('generic', tx.message)
        except ThriftServiceException as tex:
            print('thrift exception request %s' % tex)
            raise tex
        except ExternalEndpointUnavailable as endEx:
            print('endpoint exception request %s' % endEx)
            raise endEx
        except Exception as ex:
            print('whot??? %s' % ex)
            raise ex

    def resolve_config(self, action):

        if action is ActionEnum.MUSIC:
            service_string = 'music'
        elif action is ActionEnum.WEATHER:
            service_string = 'weather'
        elif action is ActionEnum.KAKU:
            service_string = 'home'
        elif action is ActionEnum.AGENDA:
            service_string = 'agenda'
        else:
            service_string = ''
        consul_resolver = resolver.Resolver()
        consul_resolver.port = 8600
        consul_resolver.nameservers = ["127.0.0.1"]

        dnsanswer = consul_resolver.query(service_string+"-pi.service.consul.", 'A')
        ip = str(dnsanswer[0])
        dnsanswer_srv = consul_resolver.query(service_string+"-pi.service.consul.", 'SRV')
        port = int(str(dnsanswer_srv[0]).split()[2])
        return ip, port