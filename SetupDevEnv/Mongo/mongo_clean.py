import config
from pymongo import MongoClient

class MongoMaintain():
    __mongoClient = MongoClient(host=config.mongo_service_ip, port=config.mongo_service_port)
    __person_db = __mongoClient.person_database


    @classmethod
    def drop_collection(self):
        print("dropping mongo")
        self.__person_db.person_collection.drop()

    @classmethod
    def get_all(self):
        print('mongo get all')
        cursor = self.__person_db.person_collection.find({})
        for document in cursor:
            print(document)

if __name__ == '__main__':
    mongoActions = MongoMaintain()
    mongoActions.get_all()
    mongoActions.drop_collection()
    mongoActions.get_all()
