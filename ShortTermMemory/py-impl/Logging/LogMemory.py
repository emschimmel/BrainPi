import sys

from collections import defaultdict

sys.path.append('../gen-py')
from ShortMemory.ttypes import *
from . import ConnectionManager

class LogMemory:

    con = ConnectionManager.ConnectionManager()

    def __init__(self):
        self.log = {}

    def storeLog(self, logInput):
        self.con.storeLog(logInput)

    def getLog(self, starttime, endtime, amount):
        self.con.getLog(starttime, endtime, amount)
