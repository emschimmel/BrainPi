import random
import string
import consul

import sys
sys.path.append('../../')
import config

class DeviceMemory:

    __consul_instance = consul.Consul(host=config.consul_ip, port=config.consul_port)

    def __init__(self):
        pass

    @classmethod
    def generateDeviceToken(self, input):
        print("generate device token")
        key = self.__generateNewDeviceToken()
        print(key)
        self.__consul_instance.kv.put(key, str(input))

        return key

    @classmethod
    def validateDeviceToken(self, tokenString):
        index, data = self.__consul_instance.kv.get(tokenString)
        print(data)
        if data is not None:
            return True
        return False

    @classmethod
    def __generateNewDeviceToken(self):
        newToken = ''.join(random.choice(string.ascii_uppercase) for _ in range(8))
        if self.validateDeviceToken(newToken):
            self.__generateNewDeviceToken()
        else:
            return newToken
