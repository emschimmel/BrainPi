import sys

from collections import defaultdict

sys.path.append('../gen-py')
from ShortMemory.ttypes import *
import random, string
import time
import datetime

class TokenMemory:
    tokenMemory = defaultdict(list)

    max_token_time = 1000

    def __init__(self):
        self.log = {}

    def generateToken(self, tokenObject):
        newToken = self.generateNewToken()
        key = self.generateKey(newToken, tokenObject.deviceToken)
        tokenObject.time = datetime.datetime.utcnow()
        ts = time.time()
        tokenObject.date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S')
        self.tokenMemory[key] = tokenObject
        return newToken

    def validateToken(self, tokenString, deviceToken):
        key = self.generateKey(tokenString, deviceToken)
        tokenObject = self.tokenMemory.get(key)
        if (tokenObject):
            if tokenObject.time - datetime.datetime.utcnow() <= self.max_token_time:
                return True
        return False

    def getToken(self, tokenInput):
        key = tokenInput.value.token.join(':').join(tokenInput.value.deviceToken)
        return self.tokenMemory.get(key)


    def generateKey(self, token, deviceToken):
        return token.join(':').join(deviceToken)

    def generateNewToken(self):
        return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))

