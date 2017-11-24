#!/usr/bin/env python

# not used in this project.

import sys
sys.path.append('../gen-py')
 
from EyePi import EyePiThriftService
from EyePi.ttypes import *
from EyePi.constants import *
 
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from dns import resolver

def resolve_config():
    consul_resolver = resolver.Resolver()
    consul_resolver.port = 8600
    consul_resolver.nameservers = ["127.0.0.1"]

    dnsanswer = consul_resolver.query("eye-pi.service.consul.", 'A')
    ip = str(dnsanswer[0])
    dnsanswer_srv = consul_resolver.query("eye-pi.service.consul.", 'SRV')
    port = int(str(dnsanswer_srv[0]).split()[2])
    return ip, port

try:
    ip, port = resolve_config()

    # Make socket
    transport = TSocket.TSocket(ip, port)
 
    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)
 
    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
 
    # Create a client to use the protocol encoder
    client = EyePiThriftService.Client(protocol)
 
    # Connect!
    transport.open()

    input = EyePiInput()


    input.deviceToken = 'myLaptop'
    input.action = ActionEnum.LOGIN

    client.writeLog(input)

    transport.close()
 
except Thrift.TException as tx:
    print ("%s" % (tx.message))
