from collections import defaultdict

from ShortMemory.ttypes import *

class LocalImplementation():

    logMemory = defaultdict(list)

    def storeLog(self, logInput):
        print("local store log")
        self.logMemory[logInput.key] = logInput.value

    def getLog(self, starttime, endtime, amount):
        print("local get log")
        return dict((k, v) for k, v in self.logMemory.items() if k >= starttime and k <=endtime and sum(v) <=amount)