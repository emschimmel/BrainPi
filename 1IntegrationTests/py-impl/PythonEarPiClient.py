#!/usr/bin/env python

# not used in this project.
import datetime
import sys
sys.path.append('../gen-py')

from EyePi.ttypes import LoginInputObject
from EarPi.ttypes import EarPiAuthObject
from GenericStruct.ttypes import ActionEnum
from AutorisationStruct.ttypes import Person
from AutorisationStruct.ttypes import user_detail
from AutorisationStruct.ttypes import Autorisation
from AutorisationStruct.ttypes import DeviceTokenInput
from ThriftException.ttypes import UniqueFailedException

from ConnectionHelpers.ConnectShortMemory import ConnectShortMemory
from ConnectionHelpers.ConnectLongMemory import ConnectLongMemory
from ConnectionHelpers.ConnectEarPi import ConnectEarPi
from ConnectionHelpers.ConnectEyePi import ConnectEyePi
from ConnectionHelpers.DeviceRegistrator import DeviceRegistrator
from ConnectionHelpers.PasswordHelper import PasswordHelper
from ConnectionHelpers.AutorisationsStructProvider import AutorisationsStructProvider
import pickle

from thrift import Thrift

class testFlow:

    __displayLists = False
    __person = None
    __uniquename = 'MockPerson'
    __username = 'admin'
    __password = PasswordHelper.hashPassword('admin')
    __code = PasswordHelper.hashPassword('123456ABCD')
    __devicetoken = None
    __token = None
    __autorisations = dict()

    __secondUniquename = 'Test'
    __secondUsername = 'Test'
    __secondPassword = PasswordHelper.hashPassword('Test')
    __secondPerson = None
    __secondCode = PasswordHelper.hashPassword('123456')

    def get_class_state(self):
        return self.__token, self.__devicetoken, self.__person

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
            input.autorisations = AutorisationsStructProvider().generate_full_autorisations()
            self.__person = input
            ConnectLongMemory().storeNewPerson(input)

        except UniqueFailedException as unique:
            print('catching unique failed Exception')
            for field in unique.fields:
                print('unique field %s already in database with value' % field)
        except Thrift.TException as tx:
            print("%s" % (tx.message))

    def loginWithUser(self):
        try:
            input = LoginInputObject()
            input.username = self.__username
            print(self.__password)
            encrypted_password = PasswordHelper.encryptPassword(self.__password)
            input.password = encrypted_password
            encrypted_code = PasswordHelper.encryptPassword(self.__code)
            input.code = encrypted_code
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

    def enterNewPerson(self):
        try:
            input = Person()
            input.uniquename = self.__secondUniquename
            details = user_detail()
            details.firstname = 'Celyne'
            details.lastname = 'Van der Pol'
            details.gender = 'Cat'
            details.dob = '03-09-1966'
            input.details = details
            input.username = self.__secondUsername
            encrypted_password = PasswordHelper.encryptPassword(self.__password)
            input.password = encrypted_password
            encrypted_code = PasswordHelper.encryptPassword(self.__secondCode)
            input.code = encrypted_code
            input.enabled = True
            tokenInput = self.createEarPiAuthObject()
            self.__token = ConnectEarPi().storeNewPerson(person=input, tokenInput=tokenInput)
            print(self.__token)

        except UniqueFailedException as unique:
            print('catching unique failed Exception')
            for field in unique.fields:
                print('unique field %s already in database with value' % field)
        except Thrift.TException as tx:
            print("%s" % (tx.message))
        except Exception as ex:
            print(ex)

    def getUser(self):
        try:
            tokenInput = self.createEarPiAuthObject()
            output = ConnectEarPi().getUser(uniquename=self.__secondUniquename, tokenInput=tokenInput)
            print(output)
            if not output.person.uniquename:
                print('test failed')
            else:
                self.__secondPerson = output.person
            self.__token = output.token
        except Thrift.TException as tx:
            print("%s" % (tx.message))

    def getUserList(self):
        try:
            tokenInput = self.createEarPiAuthObject()
            output = ConnectEarPi().getUserList(tokenInput)
            self.__token = output.token
            if output.personList:
                print("%d items" % len(output.personList))
            else:
                print("test fail 0 items")
            if self.__displayLists:
                for item in output.personList:
                    print(item)
        except Thrift.TException as tx:
            print("%s" % (tx.message))

    def changeUser(self):
        try:
            # create person
            person = Person()
            person.uniquename = self.__uniquename
            person.code=PasswordHelper.hashPassword('123456789')
            details = user_detail()
            details.firstname = 'Changed'
            details.lastname = 'Person'
            details.gender = 'Cat'
            details.dob = '03-09-1966'
            person.details = details
            tokenInput = self.createEarPiAuthObject()
            print(person)
            token = ConnectEarPi().changeUser("details", person, tokenInput)
            self.__token = token
        except Thrift.TException as tx:
            print("%s" % (tx.message))

    def changeAllModuleSettings(self):
        try:
            if self.__secondPerson is not None:
                tokenInput = self.createEarPiAuthObject()
                print(self.__secondPerson)
                autorisations = self.__secondPerson.autorisations
                if autorisations is None:
                    print('test failed, autorisations where none')
                    autorisations = dict()
                    autorisation = Autorisation()
                    autorisation.write_enabled = True
                    autorisation.enabled = True
                    autorisation.module_config = pickle.dumps(obj='hallo nieuwe config', protocol=None, fix_imports=False)
                    autorisations[ActionEnum.LOGIN] = autorisation
                else:
                    for auto in autorisations:
                        autorisations[auto].enabled = True
                token = ConnectEarPi().configureUserModule(self.__secondUniquename, autorisations, tokenInput)
                self.__token = token
            else:
                print("failed, test not executed")
        except Thrift.TException as tx:
            print("%s" % (tx.message))

    def changeModuleSettings(self):
        try:
            tokenInput = self.createEarPiAuthObject()
            newBinary = pickle.dumps(obj='hallo nieuwe config', protocol=None, fix_imports=False)
            token = ConnectEarPi().configureModuleSettings(self.__secondUniquename, ActionEnum.LOGIN, newBinary, tokenInput)
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
            if output.deviceList:
                print("%d items" % len(output.deviceList))
            else:
                print("test fail 0 items")
            if self.__displayLists:
                for key in output.deviceList:
                    print(key+" - %s" % output.deviceList[key])
        except Thrift.TException as tx:
            print("%s" % (tx.message))

    def createEarPiAuthObject(self):
        tokenObject = EarPiAuthObject()
        tokenObject.token = self.__token
        tokenObject.deviceToken = self.__devicetoken
        return tokenObject

if __name__ == '__main__':
    starttime = datetime.datetime.utcnow()
    testFlow = testFlow()

    print("----> enterFirstPerson")
    testFlow.enterFirstPerson()
    print((datetime.datetime.utcnow() - starttime).total_seconds())
    currenttime = datetime.datetime.utcnow()

    print("----> loginWithUser failed, no registered device")
    testFlow.loginWithUser()
    print((datetime.datetime.utcnow() - currenttime).total_seconds())
    currenttime = datetime.datetime.utcnow()

    print("----> trust that first device")
    testFlow.confirmFirstDevice()
    print((datetime.datetime.utcnow() - currenttime).total_seconds())
    currenttime = datetime.datetime.utcnow()

    print("----> loginWithUser succes, device registered")
    testFlow.loginWithUser()
    print((datetime.datetime.utcnow() - currenttime).total_seconds())
    currenttime = datetime.datetime.utcnow()

    print("----> enterNewPerson")
    testFlow.enterNewPerson()
    print((datetime.datetime.utcnow() - currenttime).total_seconds())
    currenttime = datetime.datetime.utcnow()

    print("----> getUser")
    testFlow.getUser()
    print((datetime.datetime.utcnow() - currenttime).total_seconds())
    currenttime = datetime.datetime.utcnow()

    print("----> getUserList")
    testFlow.getUserList()
    print((datetime.datetime.utcnow() - currenttime).total_seconds())
    currenttime = datetime.datetime.utcnow()

    print("----> changeUser")
    testFlow.changeUser()
    print((datetime.datetime.utcnow() - currenttime).total_seconds())
    currenttime = datetime.datetime.utcnow()

    print("----> changeModuleSettings")
    testFlow.changeModuleSettings()
    print((datetime.datetime.utcnow() - currenttime).total_seconds())
    currenttime = datetime.datetime.utcnow()

    print("----> getUser to get the newly set autorisations")
    testFlow.getUser()
    print((datetime.datetime.utcnow() - currenttime).total_seconds())
    currenttime = datetime.datetime.utcnow()

    print("----> changeAllModuleSettings")
    testFlow.changeAllModuleSettings()
    print((datetime.datetime.utcnow() - currenttime).total_seconds())
    currenttime = datetime.datetime.utcnow()

    print("----> getUserList")
    testFlow.getUserList()
    print((datetime.datetime.utcnow() - currenttime).total_seconds())
    currenttime = datetime.datetime.utcnow()

    print("----> register and confirm a second device")
    testFlow.confirmDevice()
    print((datetime.datetime.utcnow() - currenttime).total_seconds())
    currenttime = datetime.datetime.utcnow()

    print("----> get deviceList")
    testFlow.getDeviceList()
    endtime = datetime.datetime.utcnow()
    print((datetime.datetime.utcnow() - currenttime).total_seconds())
    print((endtime - starttime).total_seconds())
