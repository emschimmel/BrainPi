import sys
sys.path.append('../gen-py')
from ThriftException.ttypes import BadHashException
from ThriftException.ttypes import LoginFailedException

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
            raise LoginFailedException()
        else:
            raise BadHashException()

    def changePassword(self, username, password):
        if self.checkHash(password):
            pass
        else:
            raise BadHashException()

    def checkHash(self, password):
        return True