import json

class LocalMockImplementation(object):


    def __init__(self):
        self.__data = self.__load_mock()
        self.__mockList = [self.__data]

    def get(self, uniquename):
        print('LongTermMemory: local get %s' % self.__data)
        for item in self.__mockList:
            if item.uniquename == uniquename:
                return item

    def get_all(self):
        print('LongTermMemory: local get')
        return self.__mockList

    def get_by_query(self, criteria):
        print('LongTermMemory: local get')
        return self.__mockList

    def store_new(self, value):
        print('LongTermMemory: local put')
        self.__mockList.append(value)

    def update(self, uniquename, value, field):
        print('LongTermMemory: local update')
        for item in self.__mockList:
            if item['uniquename'] == uniquename:
                item[field] = value

    def delete(self, uniquename):
        print('LongTermMemory: local delete')
        for item in self.__mockList:
            if item.uniquename == uniquename:
                self.__mockList.remove(item)

    def __load_mock(self):
        return json.load(open('./Memory/personMock.json'))


