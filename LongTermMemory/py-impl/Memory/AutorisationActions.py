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
            person_list, login_object_list = self.__con.get_for_login(query)

            if person_list:
                person = person_list[0]
                person_login_object = login_object_list[0]
                checks_passed = False
                if loginobject.password is not None:
                    passed_password = self.__decrypt(fernet_key=person_login_object.password, token=loginobject.password)

                    string_passed_password = passed_password.decode()
                    print(string_passed_password)
                    string_object_password = person_login_object.password
                    string_object_code = string_object_password.decode()
                    print(string_object_code)

                    if string_passed_password != string_object_code:
                        print('password fail')
                        print(passed_password)
                        print(person_login_object.password)
                        raise LoginFailedException()
                    else:
                        checks_passed = True

                if loginobject.code is not None:
                    passed_password = self.__decrypt(fernet_key=person_login_object.code, token=loginobject.code)

                    string_passed_password = passed_password.decode()
                    print(string_passed_password)
                    string_object_code = person_login_object.code
                    string_object_code = string_object_code.decode()
                    print(string_object_code)

                    if string_passed_password != string_object_code:
                        print('code fail')
                        print(passed_password)
                        print(person_login_object.code)
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
            person_list, login_object_list = self.__con.get_for_login(query)
            if person_list:
                person = person_list[0]
                person_login_object = login_object_list[0]
                if password is not None:
                    passed_password = self.__decrypt(token=password, fernet_key=person_login_object.password)
                    if passed_password is not password:
                        raise BadHashException()
                    else:
                        self.__con.update(uniquename=person.uniquename, value=passed_password.decode(), field='password')

            pass
        else:
            raise BadHashException()

    def __checkHash(self, password):
        return True

    @staticmethod
    def __decrypt(token, fernet_key):
        try:
            f = Fernet(fernet_key)
            return f.decrypt(token)
        except Exception as ex:
            print('catching ex')
            print(ex)
            raise BadHashException()