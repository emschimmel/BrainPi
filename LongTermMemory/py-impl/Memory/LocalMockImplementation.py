import json

class LocalMockImplementation(object):


    def __init__(self):
        self.__data = self.__load_mock()
        self.__mockList = [self.__data]

    def get(self, uniquename):
        print('local get %s' % self.__data)
        return self.__data

    def get_all(self):
        print('local get')
        return self.__mockList

    def get_by_query(self, criteria):
        print('local get')
        return self.__mockList

    def store_new(self, value):
        print('local put')

    def update(self, uniquename, value, field):
        print('local update')

    def delete(self, uniquename):
        print('local delete')

    def __load_mock(self):
        return json.load(open('./Memory/personMock.json'))


