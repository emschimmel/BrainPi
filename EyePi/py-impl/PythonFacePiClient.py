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

sys.path.append('../../')
import config

class FacePiThriftClient():

    def __init__(self):
        self.log = {}

    def handle_request(self, image):
        try:
            transport = TSocket.TSocket(config.face_pi_ip, config.face_pi_port)     # Make socket
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

    def confim_face(self, input):
        try:
            transport = TSocket.TSocket(config.face_pi_ip, config.face_pi_port)     # Make socket
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
        except ThriftServiceException as tex:
            print('thrift exception request %s' % tex)
        except ExternalEndpointUnavailable as endEx:
            print('endpoint exception request %s' % endEx)
        except Exception as ex:
            print('whot??? %s' % ex)