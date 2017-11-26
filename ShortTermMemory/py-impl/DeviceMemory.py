import random
import string
import consul

class DeviceMemory:

    def __init__(self):
        self.log = {}
        self.consul_instance = consul.Consul(host='localhost')

    def generateDeviceToken(self, input):
        print("generate device token")
        key = self.generateNewDeviceToken()
        print(key)
        self.consul_instance.kv.put(key, str(input))

        return key

    def validateDeviceToken(self, tokenString):
        index, data = self.consul_instance.kv.get(tokenString)
        print(data)
        if data is not None:
            return True
        return False

    def generateNewDeviceToken(self):
        newToken = ''.join(random.choice(string.ascii_uppercase) for _ in range(8))
        if self.validateDeviceToken(newToken):
            self.generateNewDeviceToken()
        else:
            return newToken
