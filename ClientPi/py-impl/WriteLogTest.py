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

import os.path
import random # test

sys.path.append('../../')
import config

try:
        # Make socket
    transport = TSocket.TSocket(config.eye_pi_ip, config.eye_pi_port)
 
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
    input.action = ActionEnum.WEATHER

    client.writeLog(input)

    transport.close()
 
except Thrift.TException as tx:
    print ("%s" % (tx.message))
