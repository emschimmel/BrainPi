import sys

sys.path.append('../../')
import config

sys.path.append('../gen-py')
from AutorisationStruct.ttypes import *

import json
from thrift import TSerialization
from thrift.protocol import TJSONProtocol


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
        thrift_json_string = TSerialization.serialize(
            value, TJSONProtocol.TSimpleJSONProtocolFactory()).decode('utf-8')
        result = json.loads(thrift_json_string)
        self.storage.store_new(result)

    def update(self, uniquename, value, field):
        self.storage.update(uniquename, value, field)

    def delete(self, uniquename):
        self.storage.delete(uniquename)

    def translateToJson(self, jsondata):
        # thrift_string = TSerialization.deserialize(
        #     jsondata, None, TBinaryProtocol.TBinaryProtocolFactory())
        # person = thrift_string

        person = Person()
        person.uniquename = '%s' % jsondata['uniquename']
        if 'details' in jsondata:
            user_detail_json = jsondata['details']
            details = user_detail()
            if 'firstname' in user_detail_json:
                details.firstname = '%s' % user_detail_json['firstname']
            if 'lastname' in user_detail_json:
                details.lastname = '%s' % user_detail_json['lastname']
            if 'gender' in user_detail_json:
                details.gender = '%s' % user_detail_json['gender']
            if 'dob' in user_detail_json:
                details.dob = '%s' % user_detail_json['dob']
            person.details = details
        if 'enabled' in jsondata:
            person.enabled = True if jsondata['enabled'] else False
        if 'autorisations' in jsondata:
            autorisation_json = jsondata['autorisations']
            person.autorisations = dict()
            for i in range(len(autorisation_json)):
                if autorisation_json[i]:
                    autorisation = autorisation()
                    autorisation.write = True if autorisation_json[i]['write'] else False
                    autorisation.enabled = True if autorisation_json[i]['enabled'] else False
                    if autorisation_json[i]['module_config']:
                        autorisation.module_config = autorisation_json[i]['module_config']
                    person.autorisations[i] = autorisation
        return person

