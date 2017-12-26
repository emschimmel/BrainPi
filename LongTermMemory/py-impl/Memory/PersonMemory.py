
import sys
sys.path.append('../gen-py')
from LongMemory.ttypes import *
from . import ConnectionManager

class PersonMemory():

    con = ConnectionManager.ConnectionManager()

    def getPerson(self, uniquename):
        retrievedPerson = self.getPersonFromDatabase(uniquename=uniquename)
        outputPerson = self.removeSecrets(person=retrievedPerson)
        return outputPerson

    def removeSecrets(self, person):
        return self.copyTo(newPerson=Person(), oldPerson=person)

    def copyTo(self, newPerson, oldPerson):
        newPerson.uniquename = oldPerson.uniquename
        newPerson.enabled = oldPerson.enabled
        if oldPerson.details is not None:
            newPerson.details = oldPerson.details
        if oldPerson.autorisations:
            newPerson.autorisations = oldPerson.autorisations
        return newPerson

    def updatePerson(self, person):
        # todo
        self.con.update(uniquename=person, field="", value="")


    def getPersonFromDatabase(self, uniquename):
        # get from database
        return self.con.get(key=uniquename)
