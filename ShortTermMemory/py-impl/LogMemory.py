import sys

sys.path.append('../gen-py')
from ShortMemory.ttypes import *

class LogMemory:

    logMemory = dict()

    def __init__(self):
        self.log = {}

    def storeLog(self, logInput):
        global logMemory
        print(logInput)
        logMemory.update({logInput.key, logInput.value})

    def getLog(self, starttime, endtime, amount):
        global logMemory
        print(len(logMemory))
        return dict((k, v) for k, v in logMemory.items() if k >= starttime and k <=endtime and sum(v) <=amount)