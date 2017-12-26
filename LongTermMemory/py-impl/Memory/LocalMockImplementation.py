from LongMemory.ttypes import *
import pickle

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
        import json
        person = Person()
        jsondata = json.load(open('./Memory/personMock.json'))
        person.uniquename = jsondata['uniquename']

        user_detail_json = jsondata['user_detail']
        details = user_detail()
        details.firstname = user_detail_json['firstname']
        details.lastname = user_detail_json['lastname']
        details.gender = user_detail_json['gender']
        details.dob = user_detail_json['dob']
        person.details = details
        person.username = jsondata['username']
        person.password = jsondata['password']
        person.code = jsondata['code']
        person.enabled = jsondata['enabled']
        # person.autorisations = jsondata['autorisations']
        # person.autorisations = dict()
        # person.autorisations[0] = pickle.dumps(None, protocol=None, fix_imports=False)
        # person.autorisations[1] = pickle.dumps(None, protocol=None, fix_imports=False)
        # person.autorisations[2] = pickle.dumps(None, protocol=None, fix_imports=False)
        # person.autorisations[3] = pickle.dumps(None, protocol=None, fix_imports=False)
        # person.autorisations[4] = pickle.dumps(None, protocol=None, fix_imports=False)
        # person.autorisations[5] = pickle.dumps(None, protocol=None, fix_imports=False)
        return person
