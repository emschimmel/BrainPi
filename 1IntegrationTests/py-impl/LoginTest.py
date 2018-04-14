#!/usr/bin/env python

# not used in this project.

import sys
sys.path.append('../gen-py')
from EyePi.ttypes import LoginInputObject
from AutorisationStruct.ttypes import DeviceTokenInput
import sys

sys.path.append('../gen-py')

from ConnectionHelpers.ConnectEyePi import ConnectEyePi
from ConnectionHelpers.PasswordHelper import PasswordHelper

from thrift import Thrift


def test1():
    try:
        input = LoginInputObject()
        input.username = 'AnyRandomString'
        input.password = None
        input.code = PasswordHelper.encryptPassword(PasswordHelper.hashPassword('12345'))
        inputDevice = DeviceTokenInput()
        inputDevice.ip = '127.0.0.1'
        inputDevice.devicetype = 'Development'
        input.deviceInput = inputDevice
        output = ConnectEyePi().login(input)
        print(output)
    except Thrift.TException as tx:
        print("%s" % (tx.message))

def test2():
    try:
        input = LoginInputObject()
        input.username = 'sesy'
        input.password = None
        input.code = PasswordHelper.encryptPassword(PasswordHelper.hashPassword('12345'))
        inputDevice = DeviceTokenInput()
        inputDevice.ip = '127.0.0.1'
        inputDevice.devicetype = 'Development'
        input.deviceInput = inputDevice
        output = ConnectEyePi().login(input)
        print(output)
    except Thrift.TException as tx:
        print("%s" % (tx.message))

def test3():
    try:
        input = LoginInputObject()
        input.username = 'sesy'
        input.password = None
        input.code = PasswordHelper.encryptPassword(PasswordHelper.hashPassword('12345'))
        inputDevice = DeviceTokenInput()
        inputDevice.ip = '127.0.0.1'
        inputDevice.devicetype = 'Development'
        input.deviceInput = inputDevice
        output = ConnectEyePi().login(input)
        print(output)

    except Thrift.TException as tx:
        print("%s" % (tx.message))

test1()
test2()
test3()