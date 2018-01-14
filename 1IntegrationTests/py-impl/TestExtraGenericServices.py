
import datetime
import sys
sys.path.append('../gen-py')
import pickle

from thrift import Thrift
from PythonEarPiClient import testFlow

class TestExtraGenericServices:

    __devicetoken = None
    __token = None
    __person = None

    def __init__(self):
        # define preconditions
        precondition_setup = testFlow()
        precondition_setup.enterFirstPerson()
        precondition_setup.loginWithUser()
        precondition_setup.confirmFirstDevice()
        precondition_setup.loginWithUser()
        self.__token, self.__devicetoken, self.__person = precondition_setup.get_class_state()


    def login(self):
        print(self.__devicetoken)
        print(self.__token)
        print(self.__person)
        pass

if __name__ == '__main__':

    starttime = datetime.datetime.utcnow()
    classUnderTest = TestExtraGenericServices()

    print("----> make first call")
    classUnderTest.login()
    print((datetime.datetime.utcnow() - starttime).total_seconds())
    currenttime = datetime.datetime.utcnow()
