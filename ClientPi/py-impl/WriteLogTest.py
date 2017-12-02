#!/usr/bin/env python

# not used in this project.

import sys
sys.path.append('../gen-py')

from ConnectionHelpers.ConnectEyePi import ConnectEyePi

from EyePi.ttypes import *
from EyePi.constants import *
from GenericStruct.ttypes import *
 
from thrift import Thrift

try:
    input = EyePiInput()
    input.deviceToken = 'myLaptop'
    input.action = ActionEnum.LOGIN
    ConnectEyePi().writeLog(input)
 
except Thrift.TException as tx:
    print ("%s" % (tx.message))
