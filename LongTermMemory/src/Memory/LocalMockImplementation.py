import json

class LocalMockImplementation(object):


    def __init__(self):
        self.__data = self.__load_mock()
        self.__mockList = [self.__data]

    def check_if_uniquename_exists(self, uniquename):
        print('LongTermMemory: mongo check if available')
        result = None
        for item in self.__mockList:
            if item['uniquename'] == uniquename:
                result = item
        return True if result is not None else False

    def check_if_username_exists(self, username):
        print('LongTermMemory: mongo check if available')
        result = None
        for item in self.__mockList:
            if item['username'] == username:
                result = item
        return True if result is not None else False

    def get(self, uniquename):
        print('LongTermMemory: local get %s' % self.__data)
        for item in self.__mockList:
            if item['uniquename'] == uniquename:
                return item

    def get_all(self):
        print('LongTermMemory: local get')
        return self.__mockList

    def get_by_query(self, criteria):
        print('LongTermMemory: local get')
        list = []
        for item in self.__mockList:
            valide = True
            for key in criteria:
                value = criteria[key]
                if item[key] != value:
                    valide = False
            if valide:
                list.append(item)
        return list

    def store_new(self, value):
        print('LongTermMemory: local put')
        self.__mockList.append(value)

    def update(self, uniquename, value, field):
        print('LongTermMemory: local update')
        for item in self.__mockList:
            if item['uniquename'] == uniquename:
                item[field] = value

    def updateActionConfig(self, uniquename, action, value):
        print('LongTermMemory: mongo config update')
        print('LongTermMemory: local update')
        for item in self.__mockList:
            if item['uniquename'] == uniquename:
                autorisations = {}
                if 'autorisations' in item:
                    autorisations = item['autorisations']
                autorisations[action] = value
                item['autorisations'] = autorisations

    def delete(self, uniquename):
        print('LongTermMemory: local delete')
        for item in self.__mockList:
            if item['uniquename'] == uniquename:
                self.__mockList.remove(item)

    def __load_mock(self):
        return json.load(open('./Memory/personMock.json'))


