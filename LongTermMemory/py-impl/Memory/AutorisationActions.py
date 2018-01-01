import sys
sys.path.append('../gen-py')
from ThriftException.ttypes import BadHashException
from ThriftException.ttypes import LoginFailedException

from . import ConnectionManager

class AutorisationActions():

    __con = ConnectionManager.ConnectionManager()

    def login(self, loginobject):
        if self.__checkHash(loginobject.password):
            query = dict()
            query['username'] = loginobject.username
            if loginobject.password:
                query['password'] = loginobject.password
            if loginobject.code:
                query['code'] = loginobject.code
            query['enabled'] = 1
            personList = self.__con.get_by_query(query)
            if personList:
                return personList[0]
            raise LoginFailedException()
        else:
            raise BadHashException()

    def changePassword(self, username, password):
        if self.__checkHash(password):
            pass
        else:
            raise BadHashException()

    def __checkHash(self, password):
        return True