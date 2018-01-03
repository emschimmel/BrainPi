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

        newToken, key = self.__generateNewToken(tokenObject.deviceToken)
        tokenObject.time = datetime.datetime.utcnow()
        ts = time.time()
        tokenObject.date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S')
        self.__con.put(key, tokenObject)
        if tokenObject.token:
            oldKey = self.__generateKey(tokenObject.token, tokenObject.deviceToken)
            self.__con.update(oldKey, newToken)
        print(newToken)
        return newToken

    @classmethod
    def validateToken(self, tokenString, deviceToken):
        key = self.__generateKey(tokenString, deviceToken)
        tokenObject = self.__con.get(key)
        # time=datetime.datetime(2018, 1, 1, 10, 58, 49, 723580))
        if (tokenObject):
            if (datetime.datetime.utcnow() - tokenObject.time).total_seconds() <= self.max_token_time:
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

