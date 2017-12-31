import random
import string
import consul

import sys
sys.path.append('../../')
import config

class DeviceMemory:

    def __init__(self):
        self.log = {}
        self.consul_instance = consul.Consul(host=config.consul_ip, port=config.consul_port)

    def generateDeviceToken(self, input):
        print("generate device token")
        key = self.__generateNewDeviceToken()
        print(key)
        self.consul_instance.kv.put(key, str(input))

        return key

    def validateDeviceToken(self, tokenString):
        index, data = self.consul_instance.kv.get(tokenString)
        print(data)
        if data is not None:
            return True
        return False

    def __generateNewDeviceToken(self):
        newToken = ''.join(random.choice(string.ascii_uppercase) for _ in range(8))
        if self.validateDeviceToken(newToken):
            self.__generateNewDeviceToken()
        else:
            return newToken
