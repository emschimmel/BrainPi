from . import ConnectionManager

class LogMemory:

    __con = ConnectionManager.ConnectionManager()

    def __init__(self):
        self.log = {}

    @classmethod
    def storeLog(self, logInput):
        self.__con.storeLog(logInput)

    @classmethod
    def getLog(self, starttime, endtime, amount):
        return self.__con.getLog(starttime, endtime, amount)
