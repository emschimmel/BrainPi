
import datetime
import sys
sys.path.append('../gen-py')
from thrift import Thrift
from EyePi.ttypes import EyePiInput
from GenericStruct.ttypes import ActionEnum
from WeatherPi.ttypes import WeatherInput
from AgendaPi.ttypes import GetItemsActionInput
from PhotoPi.ttypes import GetRandomPhotoActionInput
from PhonePi.ttypes import GetStatus
from PhonePi.ttypes import PlaySound

import pickle


from PythonEarPiClient import testFlow
from ConnectionHelpers.ConnectEyePi import ConnectEyePi


class TestExtraGenericServices:

    __devicetoken = None
    __token = None
    __person = None

    def __init__(self):
        # define preconditions
        precondition_setup = testFlow()
        precondition_setup.enterFirstPerson()
        precondition_setup.loginWithUser()
        precondition_setup.confirmFirstDevice()
        precondition_setup.loginWithUser()
        self.__token, self.__devicetoken, self.__person = precondition_setup.get_class_state()

    def make_agenda_call(self):
        config = self.__unpickle(self.__person.autorisations[ActionEnum.AGENDA].module_config)
        agenda_input = GetItemsActionInput()
        agenda_input.email = config.email

        input = EyePiInput()
        input.deviceToken = self.__devicetoken
        input.token = self.__token
        actions = dict()
        actions[ActionEnum.AGENDA] = self.__pickle(agenda_input)
        input.action = actions

        output = ConnectEyePi().handleRequest(input)
        print(output)
        print(self.__unpickle_action(output.data, ActionEnum.AGENDA))
        if output.ok:
            print("output = ok")
            self.__token = output.token

    def make_weather_call(self):
        input = EyePiInput()
        input.deviceToken = self.__devicetoken
        input.token = self.__token
        actions = dict()
        actions[ActionEnum.WEATHER] = self.__person.autorisations[ActionEnum.WEATHER].module_config
        input.action = actions

        output = ConnectEyePi().handleRequest(input)
        print(output)
        print(self.__unpickle_action(output.data, ActionEnum.WEATHER))
        if output.ok:
            self.__token = output.token

    def make_photo_call(self):
        config = self.__unpickle(self.__person.autorisations[ActionEnum.PHOTO].module_config)
        photo_input = GetRandomPhotoActionInput()
        photo_input.email = config.email

        input = EyePiInput()
        input.deviceToken = self.__devicetoken
        input.token = self.__token
        actions = dict()
        actions[ActionEnum.PHOTO] = self.__pickle(photo_input)
        input.action = actions

        output = ConnectEyePi().handleRequest(input)
        print(output)
        print(self.__unpickle_action(output.data, ActionEnum.PHOTO))
        if output.ok:
            self.__token = output.token

    def make_phone_call(self):
        config = self.__unpickle(self.__person.autorisations[ActionEnum.PHONE].module_config)
        phone_input = GetStatus()
        phone_input.email = config.email

        input = EyePiInput()
        input.deviceToken = self.__devicetoken
        input.token = self.__token
        actions = dict()
        actions[ActionEnum.PHONE] = self.__pickle(phone_input)
        input.action = actions

        output = ConnectEyePi().handleRequest(input)
        print(output)
        print(self.__unpickle_action(output.data, ActionEnum.PHONE))
        if output.ok:
            self.__token = output.token

    @staticmethod
    def __unpickle(input):
        return pickle.loads(input, fix_imports=False, encoding="ASCII", errors="strict")

    @staticmethod
    def __unpickle_action(input, action):
        if len(input):
            return pickle.loads(input[action], fix_imports=False, encoding="ASCII", errors="strict")
        else:
            return None

    @staticmethod
    def __pickle(input):
        return pickle.dumps(obj=input, protocol=None, fix_imports=False)

if __name__ == '__main__':

    starttime = datetime.datetime.utcnow()
    classUnderTest = TestExtraGenericServices()

    print("----> make agenda call")
    classUnderTest.make_agenda_call()
    print((datetime.datetime.utcnow() - starttime).total_seconds())
    currenttime = datetime.datetime.utcnow()

    print("----> make weather call")
    classUnderTest.make_weather_call()
    print((datetime.datetime.utcnow() - starttime).total_seconds())
    currenttime = datetime.datetime.utcnow()

    print("----> make photo call")
    classUnderTest.make_photo_call()
    print((datetime.datetime.utcnow() - starttime).total_seconds())
    currenttime = datetime.datetime.utcnow()

    print("----> make phone call")
    classUnderTest.make_phone_call()
    print((datetime.datetime.utcnow() - starttime).total_seconds())
    currenttime = datetime.datetime.utcnow()

