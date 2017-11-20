import sys

sys.path.append('../gen-py')
from ShortMemory.ttypes import *
import random, string
import time
import datetime

class TokenMemory:
    tokenMemory = dict()
    personMemory = dict()

    max_token_time = 1000

    def __init__(self):
        self.log = {}

    def generateToken(self, tokenObject):
        global tokenMemory
        newToken = self.generateNewToken()
        key = self.generateKey(newToken, tokenObject.deviceToken)
        tokenObject.time = datetime.datetime.utcnow()
        ts = time.time()
        tokenObject.date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S')
        tokenMemory.update({key, tokenObject})
        return newToken

    def validateToken(self, tokenString, deviceToken):
        global tokenMemory
        global max_token_time
        key = self.generateKey(tokenString, deviceToken)
        tokenObject = tokenMemory.get(key)
        if (tokenObject):
            if tokenObject.time - datetime.datetime.utcnow() <= max_token_time:
                return True
        return False

    def getToken(self, tokenInput):
        global tokenMemory
        key = tokenInput.value.token.join(':').join(tokenInput.value.deviceToken)
        return tokenMemory.get(key)


    def generateKey(self, token, deviceToken):
        return token.join(':').join(deviceToken)

    def generateNewToken(self):
        return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))

