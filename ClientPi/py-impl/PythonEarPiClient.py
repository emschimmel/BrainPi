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

    __person = None
    __uniquename = 'MockPerson'
    __username = 'admin'
    __password = 'admin'
    __code = '123456ABCD'
    __devicetoken = None
    __token = None
    __autorisations = dict

    def enterFirstPerson(self):
        try:
            input = Person()
            input.uniquename = self.__uniquename

            details = user_detail()
            details.firstname = 'Mock'
            details.lastname = 'Person'
            details.gender = 'Cat'
            details.dob = '03-09-1966'
            input.details = details
            input.username = self.__username
            input.password = self.__password
            input.code = self.__code
            input.enabled = True
            self.__person = input
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

    def getUserList(self):
        try:
            tokenInput = self.createEarPiAuthObject()
            output = ConnectEarPi().getUserList(tokenInput)
            print(output.personList)
            self.__token = output.token
        except Thrift.TException as tx:
            print("%s" % (tx.message))

    def createEarPiAuthObject(self):
        tokenObject = EarPiAuthObject()
        tokenObject.token = self.__token
        tokenObject.deviceToken = self.__devicetoken
        return tokenObject






if __name__ == '__main__':
    classUnderTest = testFlow()
    classUnderTest.enterFirstPerson()
    classUnderTest.loginWithUser()
    classUnderTest.getUserList()

