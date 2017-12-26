import sys
sys.path.append('../../')
import config
from pymongo import MongoClient



class MongoImplementation():
    def __init__(self):
        self.mongoClient = MongoClient(host=config.mongo_service_ip, port=config.mongo_service_port)
        self.person_db = self.mongoClient.person_database
        self.person_collection = self.person_db.person_collection


    def get(self, uniquename):
        print('mongo get')
        return self.person_collection.find_one({'uniquename': uniquename})

    def get_all(self):
        print('mongo get')
        return self.person_collection.find_many()

    def get_by_query(self, criteria):
        print('mongo get')
        return self.person_collection.find_one(criteria)

    def store_new(self, value):
        print('mongo put')
        self.person_collection.insert_one(value)

    def update(self, uniquename, value, field):
        person = self.get(uniquename)
        person[field] = value
        self.person_collection.update({'_id':person._id}, {'$set': person}, upsert=False)
        print('mongo update')

    def delete(self, uniquename):
        print('mongo delete')
        self.person_collection.delete_one({'uniquename' : uniquename})