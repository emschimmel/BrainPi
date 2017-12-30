#!/usr/bin/env python

# not used in this project.

import sys
sys.path.append('../gen-py')

from ConnectionHelpers.ConnectEyePi import ConnectEyePi

from EyePi.ttypes import EyePiInput
from GenericStruct.ttypes import ActionEnum
 
from thrift import Thrift
import pickle

try:
    input = EyePiInput()
    input.deviceToken = 'myLaptop'
    action = dict()
    action[ActionEnum.LOGIN] = pickle.dumps("testdata", protocol=None, fix_imports=False)
    input.action = action
    ConnectEyePi().writeLog(input)
 
except Thrift.TException as tx:
    print ("%s" % (tx.message))
