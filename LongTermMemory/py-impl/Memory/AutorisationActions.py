import sys
sys.path.append('../gen-py')
from ThriftException.ttypes import BadHashException
from ThriftException.ttypes import LoginFailedException
from cryptography.fernet import Fernet

from . import ConnectionManager

class AutorisationActions():

    __con = ConnectionManager.ConnectionManager()

    def login(self, loginobject):
        if self.__checkHash(loginobject.password):
            query = dict()
            query['username'] = loginobject.username
            query['enabled'] = 1
            personList = self.__con.get_by_query(query)

            if personList:
                person = personList[0]
                checks_passed = False
                if loginobject.password is not None:
                    passed_password = self.__decrypt(person.password, loginobject.password)
                    if passed_password is not loginobject.password:
                        raise LoginFailedException()
                    else:
                        checks_passed = True

                if loginobject.code is not None:
                    passed_password = self.__decrypt(person.code, loginobject.code)
                    if passed_password is not loginobject.code:
                        raise LoginFailedException()
                    else:
                        checks_passed = True
                if checks_passed:
                    return person
            raise LoginFailedException()
        else:
            raise BadHashException()

    def changePassword(self, username, password):
        if self.__checkHash(password):
            query = dict()
            query['username'] = username
            query['enabled'] = 1
            personList = self.__con.get_by_query(query)
            if personList:
                person = personList[0]
                if password is not None:
                    passed_password = self.__decrypt(person.password, password)
                    if passed_password is not password:
                        raise BadHashException()
                    else:
                        self.__con.update(uniquename=person.uniquename, value=passed_password, field='password')

            pass
        else:
            raise BadHashException()

    def __checkHash(self, password):
        return True

    @staticmethod
    def __decrypt(token, key):
        f = Fernet(key)
        return f.decrypt(token)