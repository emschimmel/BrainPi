import sys
sys.path.append('../../')
import config
from pymongo import MongoClient
sys.path.append('../src/gen-py')
from AutorisationStruct.ttypes import Autorisation
import json
from thrift import TSerialization
from thrift.protocol import TJSONProtocol

class MongoImplementation():
    __mongoClient = MongoClient(host=config.mongo_service_ip, port=config.mongo_service_port)
    __person_db = __mongoClient.person_database

    def __init__(self):
        pass

    @classmethod
    def check_if_uniquename_exists(self, uniquename):
        print('LongTermMemory: mongo check if available')
        result = self.__person_db.person_collection.find({'uniquename': uniquename}).limit(1)
        for document in result:
            return True
        return False

    @classmethod
    def check_if_username_exists(self, username):
        print('LongTermMemory: mongo check if available')
        result = self.__person_db.person_collection.find({'username': username}).limit(1)
        for document in result:
            return True
        return False

    @classmethod
    def get(self, uniquename):
        print('LongTermMemory: mongo get')
        return self.__person_db.person_collection.find_one({'uniquename': uniquename})

    @classmethod
    def get_all(self):
        print('LongTermMemory: mongo get all')
        documents = []
        cursor = self.__person_db.person_collection.find({})
        for document in cursor:
            documents.append(document)
        return documents

    @classmethod
    def drop_collection(self):
        self.__person_db.person_collection.drop()

    @classmethod
    def get_by_query(self, criteria):
        print('LongTermMemory: mongo get by query')
        return self.__person_db.person_collection.find(criteria)

    @classmethod
    def store_new(self, value):
        print('LongTermMemory: mongo put')
        self.__person_db.person_collection.insert_one(value)

    @classmethod
    def update(self, uniquename, value, field):
        print('LongTermMemory: mongo update')
        person = self.get(uniquename)
        print(person)
        self.__person_db.person_collection.update_one({
            '_id': person['_id']
        }, {
            '$set': {
                field: value
            }
        }, upsert=False)
        person = self.get(uniquename)
        print(person)


    @classmethod
    def updateActionConfig(self, uniquename, action, value):
        print('LongTermMemory: mongo config update')
        person = self.get(uniquename)
        autorisations = dict()
        if 'autorisations' in person and person['autorisations'] is not None:
            autorisations = person['autorisations']
            autorisations[str(action)]['module_config'] = value['module_config']
        else:
            autorisations[str(action)] = value
        person['autorisations'] = autorisations
        self.__person_db.person_collection.update_one({
            '_id': person['_id']
        }, {
            '$set': {
                'autorisations': autorisations
            }
        }, upsert=False)

    @classmethod
    def delete(self, uniquename):
        print('LongTermMemory: mongo delete')
        self.__person_db.person_collection.delete_one({'uniquename' : uniquename})