from collections import defaultdict

class LocalImplementation():

    __logMemory = defaultdict(list)

    @classmethod
    def storeLog(self, logInput):
        print("local store log")
        self.__logMemory[logInput.key] = logInput.value

    @classmethod
    def getLog(self, starttime, endtime, amount):
        print("local get log")
        return dict((k, v) for k, v in self.__logMemory.items() if k >= starttime and k <=endtime and sum(v) <=amount)