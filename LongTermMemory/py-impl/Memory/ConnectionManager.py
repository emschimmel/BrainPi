import sys

sys.path.append('../../')
import config
from LongMemory.ttypes import *
from thrift_json import thrift2dict

class State_d:
    def __init__(self, imp):
        self.__implementation = imp
    def changeImp(self, newImp):
        self.__implementation = newImp
    # Delegate calls to the implementation:
    def __getattr__(self, name):
        return getattr(self.__implementation, name)

class ConnectionManager():
    try:
        from pymongo import MongoClient
    #    MongoClient = None
    except ImportError:
        MongoClient = None
    if MongoClient:
        try:
            client = MongoClient(host=config.mongo_service_ip, port=config.mongo_service_port)
            from . import MongoImplementation
            storage = State_d(MongoImplementation.MongoImplementation())
        except Exception as ex:
            print("mongodb is a requirement")
            from . import LocalMockImplementation
            storage = State_d(LocalMockImplementation.LocalMockImplementation())
    else:
        print("mongodb is a requirement")
        from . import LocalMockImplementation
        storage = State_d(LocalMockImplementation.LocalMockImplementation())

    def get(self, key):
        return self.translateToJson(self.storage.get(key))

    def get_all(self):
        result = []
        for item in self.storage.get_all():
            result.append(self.translateToJson(item))
        return result

    def get_by_query(self, query):
        result = []
        for item in self.storage.get_by_query(query):
            result.append(self.translateToJson(item))
        return result

    def store_new(self, value):
        result = thrift2dict(value)
        self.storage.store_new(result)

    def update(self, uniquename, value, field):
        self.storage.update(uniquename, value, field)

    def delete(self, uniquename):
        self.storage.delete(uniquename)

    def translateToJson(self, jsondata):
        person = Person()
        person.uniquename = jsondata['uniquename']
        if 'details' in jsondata:
            user_detail_json = jsondata['details']
            details = user_detail()
            if 'firstname' in user_detail_json:
                details.firstname = user_detail_json['firstname']
            if 'lastname' in user_detail_json:
                details.lastname = user_detail_json['lastname']
            if 'gender' in user_detail_json:
                details.gender = user_detail_json['gender']
            if 'dob' in user_detail_json:
                details.dob = user_detail_json['dob']
            person.details = details
        if 'username' in jsondata:
            person.username = jsondata['username']
        if 'password' in jsondata:
            person.password = jsondata['password']
        if 'code' in jsondata:
            person.code = jsondata['code']
        person.enabled = jsondata['enabled']
        if 'autorisations' in jsondata:
            pass
            # person.autorisations = jsondata['autorisations']
            # person.autorisations = dict()
            # person.autorisations[0] = pickle.dumps(None, protocol=None, fix_imports=False)
            # person.autorisations[1] = pickle.dumps(None, protocol=None, fix_imports=False)
            # person.autorisations[2] = pickle.dumps(None, protocol=None, fix_imports=False)
            # person.autorisations[3] = pickle.dumps(None, protocol=None, fix_imports=False)
            # person.autorisations[4] = pickle.dumps(None, protocol=None, fix_imports=False)
            # person.autorisations[5] = pickle.dumps(None, protocol=None, fix_imports=False)
        return person

