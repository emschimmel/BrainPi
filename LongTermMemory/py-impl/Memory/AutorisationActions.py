
from LongMemory.ttypes import *
from . import ConnectionManager

class AutorisationActions():

    con = ConnectionManager.ConnectionManager()

    def login(self, loginobject):
        if self.checkHash(loginobject.password):
            query = dict()
            query['username'] = loginobject.username
            if loginobject.password:
                query['password'] = loginobject.password
            if loginobject.code:
                query['code'] = loginobject.code
            query['enabled'] = 1
            personList = self.con.get_by_query(query)
            if personList:
                return personList[0]
            return None
        else:
            raise Exception

    def changePassword(self, username, password):
        if self.checkHash(password):
            pass
        else:
            raise Exception

    def checkHash(self, password):
        return True