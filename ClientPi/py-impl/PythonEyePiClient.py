#!/usr/bin/env python

# not used in this project.

import sys
sys.path.append('../gen-py')
 
from EyePi import EyePiThriftService
from EyePi.ttypes import *
from EyePi.constants import *
from GenericStruct.ttypes import *

from DeviceRegistrator import DeviceRegistrator

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from dns import resolver

import os.path
import random # test

sys.path.append('../../')
import config

def resolve_eye_config():
    consul_resolver = resolver.Resolver()
    consul_resolver.port = 8600
    consul_resolver.nameservers = ["127.0.0.1"]

    dnsanswer = consul_resolver.query("eye-pi.service.consul.", 'A')
    ip = str(dnsanswer[0])
    dnsanswer_srv = consul_resolver.query("eye-pi.service.consul.", 'SRV')
    port = int(str(random.choice(dnsanswer_srv)).split()[2])
    return ip, port



### test
def read_image():
    root, dirs, files=next(os.walk(config.file_path))
    imageCollection=list(filter(lambda filename:filename.endswith('.jpg'), files))
    return random.choice(imageCollection)
### end test


try:
    ## mock! ###
    # normally a device would properly register itself and keep the token.
    # But in development case, the cahce is resetted every time. This mock registers the device.
    device_token = DeviceRegistrator().register_device()
    ### end mock ###

    ip, port = resolve_eye_config()
    transport = TSocket.TSocket(ip, port)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = EyePiThriftService.Client(protocol)
    transport.open()

    input = EyePiInput()
    filename = config.file_path +read_image()
    print('image == '+filename)
    file = open(filename, 'rb')
    input.image = file.read()

    parameter = GenericObject()
    parameter.stringValue = "%s" % 'Amsterdam,nl'

    input.deviceToken = device_token
    input.action = ActionEnum.WEATHER
    input.actionParameters = parameter

    output = client.handleRequest(input)
    print(output)
    if output.ok:
        for face in output.personCollection:
            confirm_input = ConfirmInput()
            confirm_input.image = face.image
            confirm_input.person = face.person
            client.confimFace(confirm_input)

    transport.close()
 
except Thrift.TException as tx:
    print ("%s" % (tx.message))

