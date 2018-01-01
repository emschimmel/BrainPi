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

from ConnectionHelpers.ConnectShortMemory import ConnectShortMemory
from ConnectionHelpers.ConnectLongMemory import ConnectLongMemory
from ConnectionHelpers.ConnectEarPi import ConnectEarPi
from ConnectionHelpers.ConnectEyePi import ConnectEyePi
from ConnectionHelpers.DeviceRegistrator import DeviceRegistrator

from thrift import Thrift

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
            input.deviceToken = self.__devicetoken
            input.token = self.__token
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

    def changeUser(self):
        try:
            # create person
            person = Person()
            person.uniquename = self.__uniquename
            person.code='123456789'
            details = user_detail()
            details.firstname = 'Changed'
            details.lastname = 'Person'
            details.gender = 'Cat'
            details.dob = '03-09-1966'
            person.details = details
            tokenInput = self.createEarPiAuthObject()
            print(person)
            token = ConnectEarPi().changeUser("code", person, tokenInput)
            self.__token = token
        except Thrift.TException as tx:
            print("%s" % (tx.message))

    ### Somehow we have to trust the first device
    def confirmFirstDevice(self):
        try:
            ConnectShortMemory().confirmDevice(input=self.__devicetoken)
        except Thrift.TException as tx:
            print("%s" % (tx.message))

    ### Make a new device and register it
    def confirmDevice(self):
        try:
            device_token = DeviceRegistrator().register_device()
            tokenInput = self.createEarPiAuthObject()
            output = ConnectEarPi().confirmDevice(device_token, True, tokenInput)
            self.__token = output
        except Thrift.TException as tx:
            print("%s" % (tx.message))

    def getDeviceList(self):
        try:
            tokenInput = self.createEarPiAuthObject()
            output = ConnectEarPi().getDeviceList(tokenInput)
            self.__token = output.token
            print(output.deviceList)
        except Thrift.TException as tx:
            print("%s" % (tx.message))

    def createEarPiAuthObject(self):
        tokenObject = EarPiAuthObject()
        tokenObject.token = self.__token
        tokenObject.deviceToken = self.__devicetoken
        return tokenObject

if __name__ == '__main__':
    classUnderTest = testFlow()
    print("----> enterFirstPerson")
    classUnderTest.enterFirstPerson()
    print("----> loginWithUser failed, no registered device")
    classUnderTest.loginWithUser()
    print("----> trust that first device")
    classUnderTest.confirmFirstDevice()
    print("----> loginWithUser succes, device registered")
    classUnderTest.loginWithUser()
    print("----> getUserList")
    classUnderTest.getUserList()
    print("----> changeUser")
    classUnderTest.changeUser()
    print("----> getUserList")
    classUnderTest.getUserList()
    print("----> register and confirm a second device")
    classUnderTest.confirmDevice()
    print("----> get deviceList")
    classUnderTest.getDeviceList()
