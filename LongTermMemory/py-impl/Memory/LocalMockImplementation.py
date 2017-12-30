import json

class LocalMockImplementation():

    def __init__(self):
        self.data = self.load_mock()
        self.mockList = [self.data]
        pass

    def get(self, uniquename):
        print('local get %s' % self.data)
        return self.data

    def get_all(self):
        print('local get')
        return self.mockList

    def get_by_query(self, criteria):
        print('local get')
        return self.mockList

    def store_new(self, value):
        print('local put')

    def update(self, uniquename, value, field):
        print('local update')

    def delete(self, uniquename):
        print('local delete')

    def load_mock(self):
        return json.load(open('./Memory/personMock.json'))

