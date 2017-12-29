import sys
sys.path.append('../../')
import config
from pymongo import MongoClient



class MongoImplementation():
    def __init__(self):
        self.mongoClient = MongoClient(host=config.mongo_service_ip, port=config.mongo_service_port)
        self.person_db = self.mongoClient.person_database


    def get(self, uniquename):
        print('mongo get')
        return self.person_db.person_collection.find_one({'uniquename': uniquename})

    def get_all(self):
        print('mongo get all')
        documents = []
        cursor = self.person_db.person_collection.find({})
        for document in cursor:
            documents.append(document)
        return cursor

    def drop_collection(self):
        self.person_db.person_collection.drop()

    def get_by_query(self, criteria):
        print('mongo get by query')
        return self.person_db.person_collection.find(criteria)

    def store_new(self, value):
        print('mongo put')
        self.person_db.person_collection.insert_one(value)

    def update(self, uniquename, value, field):
        person = self.get(uniquename)
        person[field] = value
        self.person_db.person_collection.update({'_id':person._id}, {'$set': person}, upsert=False)
        print('mongo update')

    def delete(self, uniquename):
        print('mongo delete')
        self.person_db.person_collection.delete_one({'uniquename' : uniquename})