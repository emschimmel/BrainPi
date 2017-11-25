import random
import string
from collections import defaultdict


class DeviceMemory:
    deviceMemory = defaultdict(list)

    def __init__(self):
        self.log = {}

    def generateDeviceToken(self, input):
        self.deviceMemory[self.generateNewDeviceToken()] = input

    def validateDeviceToken(self, tokenString):
        if self.deviceMemory.get(tokenString):
            return True
        return False

    def generateNewDeviceToken(self):
        newToken = ''.join(random.choice(string.ascii_uppercase) for _ in range(8))
        if self.validateDeviceToken(newToken):
            self.generateNewDeviceToken()
        else:
            return newToken
