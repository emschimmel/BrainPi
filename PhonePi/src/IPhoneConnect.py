#https://github.com/picklepete/pyicloud

from datetime import datetime
from pyicloud import PyiCloudService
import sys
sys.path.append('./gen-py')
from PhonePi.ttypes import LostMode
from ThriftException.ttypes import ExternalEndpointUnavailable

class IPhoneConnect:

    @staticmethod
    def getLocation(input):
        try:
            api = PyiCloudService(input.email)
            output = api.iphone.location()
            return output
        except Exception as ex:
            print(ex)
            raise ExternalEndpointUnavailable("PhonePi", "Device needs to be registered", "icloud")

    @staticmethod
    def getStatus(input):
        try:
            api = PyiCloudService(input.email)
            output = api.iphone.status()
            return output
        except Exception as ex:
            print(ex)
            raise ExternalEndpointUnavailable("PhonePi", "Device needs to be registered", "icloud")

    @staticmethod
    def playSound(input):
        try:
            api = PyiCloudService(input.email)
            output = api.iphone.play_sound()
            return output
        except Exception as ex:
            print(ex)
            raise ExternalEndpointUnavailable("PhonePi", "Device needs to be registered", "icloud")

    @classmethod
    def lostMode(self, input):
        input_object = self.__fillLostModeOptional(input)
        try:
            api = PyiCloudService(input_object.email)
            output = api.iphone.lost_device(input_object.phonenumber, input_object.message)
            return output
        except Exception as ex:
            print(ex)
            raise ExternalEndpointUnavailable("PhonePi", "Device needs to be registered", "icloud")

    @staticmethod
    def __fillLostModeOptional(input):
        input_object = LostMode()
        input_object.action = input.action
        input_object.email = input.email
        input_object.phonenumber = input.phonenumber if input.phonenumber is not None else '11111'
        input_object.message = input.message if input.message is not None else 'Thief! Return my phone immediately.'
