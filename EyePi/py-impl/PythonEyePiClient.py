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

### test
file_path = '../img/'
def read_image():
    root, dirs, files=next(os.walk(file_path))
    imageCollection=list(filter(lambda filename:filename.endswith('.jpg'), files))
    return random.choice(imageCollection)


### end test

try:
        # Make socket
    transport = TSocket.TSocket('localhost', 30302)
 
    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)
 
    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
 
    # Create a client to use the protocol encoder
    client = EyePiThriftService.Client(protocol)
 
    # Connect!
    transport.open()

    input = EyePiInput()
    filename = file_path +read_image()
    print('image == '+filename)
    file = open(filename, 'rb')
    input.image = file.read()

    input.deviceToken = 'myLaptop'
    input.action = ActionEnum.LOGIN

    output = client.handleRequest(input)
    print(output)
    client.writeLog(input)
 
    transport.close()
 
except Thrift.TException as tx:
    print ("%s" % (tx.message))
