
import sys
sys.path.append('../gen-py')
from LongMemory.ttypes import *


class PersonMemory():


    def getPerson(self, uniquename):
        retrievedPerson = self.getPersonFromDatabase()
        outputPerson = self.removeSecrets(retrievedPerson)
        return outputPerson

    def removeSecrets(self, person):
        return self.copyTo(Person(), person)


    def copyTo(self, newPerson, oldPerson):
        newPerson.uniquename = oldPerson.uniquename
        newPerson.enabled = oldPerson.enabled
        if oldPerson.details:
            newPerson.details = oldPerson.details
        if oldPerson.autorisations:
            newPerson.autorisations = oldPerson.autorisations
        return newPerson

    def updatePerson(self, person):
        retrievedPerson = self.getPersonFromDatabase()
        retrievedPerson = self.copyTo(retrievedPerson, person)
        # store retrievedPerson to database


    def getPersonFromDatabase(self):
        # get from database
        return Person()
