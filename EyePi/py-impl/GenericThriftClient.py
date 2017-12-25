#!/usr/bin/env python
import random
import sys

sys.path.append('../../')
import config
import consul

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
sys.path.append('../../')
import config

class GenericThriftClient:
    def __init__(self):
        self.log = {}

    def handle_request(self, action, input, output):
        print('generic handler %s' % action)
        try:
            ip, port = self.resolve_config(action)
            transport = TSocket.TSocket(ip, port)  # Make socket
            transport = TTransport.TBufferedTransport(transport)  # Buffering is critical. Raw sockets are very slow
            protocol = TBinaryProtocol.TBinaryProtocol(transport)  # Wrap in a protocol
            client = GenericPiThriftService.Client(protocol)  # Create a client to use the protocol encoder
            transport.open()  # Connect!

            output[action] = client.handleRequest(input)
            transport.close()

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
            print('whot generic thrift??? %s' % ex)
            raise ex

    def resolve_config(self, action):
        c = consul.Consul(host=config.consul_ip, port=config.consul_resolver_port)
        key = '%d' % action
        index, data = c.kv.get(key)
        value = data.get('Value').decode('utf-8')
        consul_resolver = resolver.Resolver()
        consul_resolver.port = config.consul_resolver_port
        consul_resolver.nameservers = [config.consul_ip]

        dnsanswer = consul_resolver.query("%s-pi.service.consul." % value, 'A')
        ip = str(dnsanswer[0])
        dnsanswer_srv = consul_resolver.query("%s-pi.service.consul." % value, 'SRV')
        port = int(str(random.choice(dnsanswer_srv)).split()[2])
        return ip, port