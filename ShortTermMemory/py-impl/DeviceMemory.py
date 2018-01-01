import random
import string
import consul

import sys
sys.path.append('../../')
import config

sys.path.append('../gen-py')
from ShortMemory.ttypes import DeviceTokenInput
from thrift import TSerialization
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport

class DeviceMemory:

    __consul_instance = consul.Consul(host=config.consul_ip, port=config.consul_port)

    def __init__(self):
        pass

    @classmethod
    def generateDeviceToken(self, input):
        print("generate device token")
        key = self.__generateNewDeviceToken()
        self.__consul_instance.kv.put(key, self.__serializeDeviceToken(input=input))
        print("DeviceToken = %s" % key)
        return key

    @classmethod
    def validateDeviceToken(self, tokenString):
        index, data = self.__consul_instance.kv.get(tokenString)
        if data is not None:
            deviceObject = self.__deserializeDeviceToken(data.get('Value'))
            return deviceObject.enabled
        return False

    @classmethod
    def __generateNewDeviceToken(self):
        newToken = ''.join(random.choice(string.ascii_uppercase) for _ in range(8))
        if self.validateDeviceToken(newToken):
            self.__generateNewDeviceToken()
        else:
            return newToken

    @classmethod
    def getDeviceList(self):
        index, data = self.__consul_instance.kv.get(key='', recurse=True)
        devicedict = {}

        for item in data:
            devicedict[item.get('Key')] = self.__deserializeDeviceToken(item.get('Value'))
        return devicedict

    @classmethod
    def confirmDevice(self, devicetoken, enabled):
        index, data = self.__consul_instance.kv.get(devicetoken)
        if data is not None:
            deviceObject = self.__deserializeDeviceToken(data.get('Value'))
            deviceObject.enabled = enabled
            self.__consul_instance.kv.put(key=devicetoken, value=self.__serializeDeviceToken(deviceObject))

    @staticmethod
    def __serializeDeviceToken(input):
        transportOut = TTransport.TMemoryBuffer()
        protocolOut = TBinaryProtocol.TBinaryProtocol(transportOut)
        input.write(protocolOut)
        return transportOut.getvalue()


    @staticmethod
    def __deserializeDeviceToken(data):
        transportIn = TTransport.TMemoryBuffer(data)
        protocolIn = TBinaryProtocol.TBinaryProtocol(transportIn)
        deviceObject = DeviceTokenInput()
        deviceObject.read(protocolIn)
        return deviceObject
