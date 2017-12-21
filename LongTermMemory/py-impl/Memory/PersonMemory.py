
import sys
sys.path.append('../gen-py')
from LongMemory.ttypes import *


class PersonMemory():


    def getPerson(self, uniquename):
        retrievedPerson = self.getPersonFromDatabase()
        outputPerson = self.removeSecrets(retrievedPerson)
        return outputPerson

    def removeSecrets(self, person):
        pass

    def updatePerson(self):
        retrievedPerson = self.getPersonFromDatabase()

    def getPersonFromDatabase(self):
        return Person()
