from . import ConnectionManager
import sys
sys.path.append('../gen-py')
from ThriftException.ttypes import UniqueFailedException

class PersonMemory():

    __con = ConnectionManager.ConnectionManager()

    @classmethod
    def getPerson(self, uniquename):
        return self.getPersonFromDatabase(uniquename=uniquename)

    @classmethod
    def storeNewPerson(self, person):
        # todo
        exception = UniqueFailedException()
        exception.field = []
        fail = False
        if self.__con.check_if_username_exists(username=person.username):
            exception.field.append("username")
        elif person.uniquename is None:
        ## generate uniquename?
            pass
        elif self.__con.check_if_uniquename_exists(uniquename=person.username):
            exception.field.append("uniquename")
        if len(exception.field) > 0:
            raise exception
        else:
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
