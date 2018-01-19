from . import ConnectionManager
import sys
sys.path.append('../src/gen-py')
from ThriftException.ttypes import UniqueFailedException

class PersonMemory():

    __con = ConnectionManager.ConnectionManager()

    @classmethod
    def getPerson(self, uniquename):
        return self.getPersonFromDatabase(uniquename=uniquename)

    @classmethod
    def storeNewPerson(self, person):
        fields = []
        if person.username is not None and self.__con.check_if_username_exists(username=person.username):
            fields.append("username")
        if person.uniquename is None:
        ## generate uniquename?
            pass
        elif person.uniquename is not None and self.__con.check_if_uniquename_exists(uniquename=person.uniquename):
            fields.append("uniquename")
        if len(fields) > 0:
            raise UniqueFailedException(fields=fields)
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

    @classmethod
    def updateActionConfig(self, uniquename, action, user_config):
        self.__con.updateActionConfig(uniquename=uniquename, action=action, value=user_config)
