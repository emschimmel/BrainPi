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

class FacePiThriftClient():

    def __init__(self):
        self.log = {}

    def send_request(self, image):
        try:
                # Make socket
            transport = TSocket.TSocket('localhost', 30303)

            # Buffering is critical. Raw sockets are very slow
            transport = TTransport.TBufferedTransport(transport)

            # Wrap in a protocol
            protocol = TBinaryProtocol.TBinaryProtocol(transport)

            # Create a client to use the protocol encoder
            client = FacePiThriftService.Client(protocol)

            # Connect!
            transport.open()

            input = FacePiInput()
            input.image = image
            output = client.handleRequest(input)
            print(output)
            transport.close()
            return output.personCollection

        except Thrift.TException as tx:
            print ("%s" % (tx.message))
