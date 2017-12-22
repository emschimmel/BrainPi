import sys

sys.path.append('../../')
import config

# import importlib
# spam_spec = importlib.util.find_spec("redis")
# found = spam_spec is not None
# print(found)

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
    except ImportError:
        MongoClient = None
    if MongoClient:
        try:
            client = MongoClient(host=config.mongo_service_ip, port=config.mongo_service_port)
            from . import MongoImplementation
            storage = State_d(MongoImplementation.MongoImplementation())
        except Exception as ex:
            print("mongodb is a requirement")
        #    from . import LocalImplementation
        #    storage = State_d(LocalImplementation.LocalImplementation())
    else:
        print("mongodb is a requirement")
    #    from . import LocalImplementation
    #    storage = State_d(LocalImplementation.LocalImplementation())

    def get(self, key):
        self.storage.get(key)

    def get_all(self):
        self.storage.get_all()

    def get_by_query(self, query):
        self.storage.get_by_query(query)

    def store_new(self, value):
        self.storage.store_new(value)

    def update(self, uniquename, value, field):
        self.storage.update(uniquename, value, field)

    def delete(self, uniquename):
        self.storage.delete(uniquename)


