import random, string
import time
import datetime
from . import ConnectionManager

class TokenMemory:

    max_token_time = 1000
    __con = ConnectionManager.ConnectionManager()

    def __init__(self):
        pass

    @classmethod
    def generateToken(self, tokenObject):
        if tokenObject.token:
            oldKey = self.__generateKey(tokenObject.token, tokenObject.deviceToken)
            if self.__con.get(oldKey):
                self.__con.delete(oldKey)
        newToken, key = self.__generateNewToken(tokenObject.deviceToken)
        tokenObject.time = datetime.datetime.utcnow()
        ts = time.time()
        tokenObject.date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S')
        self.__con.put(key, tokenObject)
        print(newToken)
        return newToken

    @classmethod
    def validateToken(self, tokenString, deviceToken):
        key = self.__generateKey(tokenString, deviceToken)
        tokenObject = self.__con.get(key)
        if (tokenObject):
            if tokenObject.time - datetime.datetime.utcnow() <= self.max_token_time:
                return True
        return False

    @staticmethod
    def __generateKey(token, deviceToken):
        return ''.join([token, ':', deviceToken])

    @classmethod
    def __generateNewToken(self, deviceToken):
        newToken = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
        key = self.__generateKey(newToken, deviceToken)
        if self.__con.get(key):
            self.__generateNewToken(deviceToken)
        else:
            return newToken, key
if __name__ == '__main__':
    TokenMemory()

