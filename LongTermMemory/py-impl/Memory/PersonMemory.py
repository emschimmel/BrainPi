from . import ConnectionManager

class PersonMemory():

    __con = ConnectionManager.ConnectionManager()

    @classmethod
    def getPerson(self, uniquename):
        return self.getPersonFromDatabase(uniquename=uniquename)

    @classmethod
    def storeNewPerson(self, person):
        # todo
        self.__con.store_new(value=person)

    @classmethod
    def getAll(self):
        return self.__con.get_all()

    @classmethod
    def getPersonFromDatabase(self, uniquename):
        # get from database
        return self.__con.get(key=uniquename)

    @classmethod
    def updatePerson(self, uniquename, field, person):
        self.__con.update(uniquename=uniquename, field=field, value=getattr(person, field))
