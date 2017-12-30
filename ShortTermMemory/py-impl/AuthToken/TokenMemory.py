import random, string
import time
import datetime
from . import ConnectionManager

class TokenMemory:

    max_token_time = 1000
    con = ConnectionManager.ConnectionManager()

    def __init__(self):
        self.log = {}

    def generateToken(self, tokenObject):
        if tokenObject.token:
            oldKey = self.generateKey(tokenObject.token, tokenObject.deviceToken)
            if self.con.get(oldKey):
                self.con.delete(oldKey)
        newToken, key = self.generateNewToken(tokenObject.deviceToken)
        tokenObject.time = datetime.datetime.utcnow()
        ts = time.time()
        tokenObject.date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S')
        self.con.put(key, tokenObject)
        print(newToken)
        return newToken

    def validateToken(self, tokenString, deviceToken):
        key = self.generateKey(tokenString, deviceToken)
        tokenObject = self.con.get(key)
        if (tokenObject):
            if tokenObject.time - datetime.datetime.utcnow() <= self.max_token_time:
                return True
        return False

    def generateKey(self, token, deviceToken):
        return ''.join([token, ':', deviceToken])

    def generateNewToken(self, deviceToken):
        newToken = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
        key = self.generateKey(newToken, deviceToken)
        if self.con.get(key):
            self.generateNewToken(deviceToken)
        else:
            return newToken, key
if __name__ == '__main__':
    TokenMemory()

