
import sys
sys.path.append('../gen-py')
from LongMemory.ttypes import *
from . import ConnectionManager

class PersonMemory():

    con = ConnectionManager.ConnectionManager()

    def getPerson(self, uniquename):
        return self.getPersonFromDatabase(uniquename=uniquename)

    def updatePerson(self, person):
        # todo
        self.con.update(uniquename=person, field="", value="")

    def storeNewPerson(self, person):
        # todo
        self.con.store_new(value=person)


    def getPersonFromDatabase(self, uniquename):
        # get from database
        return self.con.get(key=uniquename)
