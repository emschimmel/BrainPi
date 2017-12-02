#!/usr/bin/env python

# not used in this project.

import sys
sys.path.append('../gen-py')

from EyePi.ttypes import *
from GenericStruct.ttypes import *
from WeatherPi.ttypes import *

from ConnectionHelpers.DeviceRegistrator import DeviceRegistrator
from ConnectionHelpers.ConnectEyePi import ConnectEyePi

from thrift import Thrift
import cv2
import os.path
import random # test
import numpy as np
import pickle

sys.path.append('../../')
import config

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

    input = EyePiInput()
    filename = config.file_path +read_image()
    print('image == '+filename)
    file = open(filename, 'rb')
    file = open(filename, 'rb')
    readfile = file.read()

    nparr = np.fromstring(readfile, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    input.image = pickle.dumps(image, protocol=None, fix_imports=False)
    actions = dict()
    weather_input = WeatherInput()
    weather_input.location = 'Amsterdam,nl'
    actionParameter = pickle.dumps(weather_input, protocol=None, fix_imports=False)
    actions[ActionEnum.WEATHER] = actionParameter
    input.action = actions
    #parameter = GenericObject()
    #parameter.stringValue = "%s" % 'Amsterdam,nl'

    input.deviceToken = device_token
    #input.action = ActionEnum.WEATHER
    #input.actionParameters = parameter

    output = ConnectEyePi().handleRequest(input)
    print(output)
    if output.ok:
        for face in output.personCollection:
            confirm_input = ConfirmInput()
            confirm_input.image = face.image
            confirm_input.person = face.person
            ConnectEyePi().confimFace(confirm_input)
except Thrift.TException as tx:
    print("%s" % (tx.message))
