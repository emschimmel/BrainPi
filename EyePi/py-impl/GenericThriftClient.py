#!/usr/bin/env python

import sys

sys.path.append('../gen-py')

from GenericStruct.ttypes import *
from GenericStruct.constants import *
from GenericServerPi import GenericPiThriftService
from GenericServerPi.ttypes import *
from GenericServerPi.constants import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol



class GenericThriftClient():
    def __init__(self):
        self.log = {}

    def handle_request(self, input, ip, port):
        print('generic handler')
        try:
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

