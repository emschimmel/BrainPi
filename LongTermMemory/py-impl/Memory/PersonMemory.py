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

    def getAll(self):
        return self.con.get_all()

    def getPersonFromDatabase(self, uniquename):
        # get from database
        return self.con.get(key=uniquename)
