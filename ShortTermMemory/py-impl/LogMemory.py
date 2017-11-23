import sys

from collections import defaultdict

sys.path.append('../gen-py')
from ShortMemory.ttypes import *

class LogMemory:

    logMemory = defaultdict(list)

    def __init__(self):
        self.log = {}

    def storeLog(self, logInput):

        self.logMemory[logInput.key] = logInput.value

    def getLog(self, starttime, endtime, amount):
        print(len(self.logMemory))
        return dict((k, v) for k, v in self.logMemory.items() if k >= starttime and k <=endtime and sum(v) <=amount)