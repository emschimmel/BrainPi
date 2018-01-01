#!/usr/bin/env python

# not used in this project.

import sys
sys.path.append('../gen-py')

from EyePi.ttypes import LoginInputObject
from EarPi.ttypes import EarPiAuthObject
from GenericStruct.ttypes import ActionEnum
from AutorisationStruct.ttypes import Person
from AutorisationStruct.ttypes import user_detail
from AutorisationStruct.ttypes import Autorisation
from AutorisationStruct.ttypes import DeviceTokenInput

from ConnectionHelpers.ConnectLongMemory import ConnectLongMemory
from ConnectionHelpers.ConnectEarPi import ConnectEarPi
from ConnectionHelpers.ConnectEyePi import ConnectEyePi

from thrift import Thrift
import cv2
import os.path
import random # test
import numpy as np
import pickle

sys.path.append('../../')
import config

class testFlow:

    __uniquename = 'CelyneUniqueString'
    __username = 'uname'
    __password = 'pass'
    __code = '12345'
    __devicetoken = None
    __token = None
    __autorisations = dict

    def enterFirstPerson(self):
        try:
            input = Person()
            input.uniquename = self.__uniquename

            details = user_detail()
            details.firstname = 'Celyne'
            details.lastname = 'van der Pol'
            details.gender = 'undefined'
            details.dob = '5-1-2017'
            input.details = details
            input.username = self.__username
            input.password = self.__password
            input.code = self.__code
            input.enabled = True
            ConnectLongMemory().storeNewPerson(input)
        except Thrift.TException as tx:
            print("%s" % (tx.message))

    def loginWithUser(self):
        try:
            input = LoginInputObject()
            input.username = self.__username
            input.password = self.__password
            input.code = self.__code
            inputDevice = DeviceTokenInput()
            inputDevice.ip = '127.0.0.1'
            inputDevice.devicetype = 'Development'
            input.deviceInput = inputDevice
            output = ConnectEyePi().login(input)
            print(output)
            if not output.uniquename == self.__uniquename:
                print("test fail")
            self.__devicetoken = output.deviceToken
            self.__token = output.token
            self.__autorisations = output.autorisations

        except Thrift.TException as tx:
            print("%s" % (tx.message))

if __name__ == '__main__':
    testFlow().enterFirstPerson()
    testFlow().loginWithUser()

