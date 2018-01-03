import sys

sys.path.append('../../')
import config

sys.path.append('../gen-py')
from AutorisationStruct.ttypes import Person
from AutorisationStruct.ttypes import Autorisation
from AutorisationStruct.ttypes import user_detail

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
            storage = State_d(imp=MongoImplementation.MongoImplementation())
        except Exception as ex:
            print("mongodb is a requirement, using LocalMockImplementation")
            from . import LocalMockImplementation
            storage = State_d(imp=LocalMockImplementation.LocalMockImplementation())
    else:
        print("mongodb is a requirement, using LocalMockImplementation")
        from . import LocalMockImplementation
        storage = State_d(imp=LocalMockImplementation.LocalMockImplementation())

    @classmethod
    def check_if_uniquename_exists(self, uniquename):
        return self.storage.check_if_uniquename_exists(uniquename=uniquename)

    @classmethod
    def check_if_username_exists(self, username):
        return self.storage.check_if_username_exists(username=username)


    @classmethod
    def get(self, key):
        return self.__JsonToThrift(jsondata=self.storage.get(uniquename=key))

    @classmethod
    def get_all(self):
        result = []
        for item in self.storage.get_all():
            result.append(self.__JsonToThrift(jsondata=item))
        return result

    @classmethod
    def get_by_query(self, query):
        result = []
        for item in self.storage.get_by_query(criteria=query):
            result.append(self.__JsonToThrift(jsondata=item))
        return result

    @classmethod
    def store_new(self, value):
        self.storage.store_new(self.__ThriftToJson(value))

    @classmethod
    def update(self, uniquename, value, field):
        self.storage.update(uniquename=uniquename, value=self.__ThriftToJson(value), field=field)

    @classmethod
    def updateActionConfig(self, uniquename, action, value):
        autorisation = Autorisation()
        autorisation.module_config = value
        self.storage.updateActionConfig(uniquename=uniquename, action=action, value=self.__ThriftToJson(autorisation))

    @classmethod
    def delete(self, uniquename):
        self.storage.delete(uniquename=uniquename)

    @staticmethod
    def __ThriftToJson(thriftdata):
        thrift_json_string = TSerialization.serialize(thriftdata, TJSONProtocol.TSimpleJSONProtocolFactory()).decode('utf-8')
        json_value = json.loads(thrift_json_string)
        return json_value

    @staticmethod
    def __JsonToThrift(jsondata):
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
            print("can't translate autorisation_json")
            print(autorisation_json)
            autorisations  = dict()
            for key in autorisation_json:
                value = autorisation_json[key]
                autorisation = Autorisation()
                autorisation.write_enabled = True if value['write_enabled'] else False
                autorisation.enabled = True if value['enabled'] else False
                # if value['module_config']:
                #     autorisation.module_config = str.encode(value['module_config'])
                autorisations[int(key)] = autorisation
            person.autorisations = autorisations
        return person

