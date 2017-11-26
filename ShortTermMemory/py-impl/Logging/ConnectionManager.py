import sys

sys.path.append('../../')
import config
from . import ElasticsearchImplementation
from . import LocalImplementation

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
        import elasticsearch
        #es = elasticsearch.Elasticsearch([{'host': config.es_service_ip, 'port': config.es_service_port}])

        es = elasticsearch.Elasticsearch(['http://%s:%d/' % config.es_service_ip % config.es_service_port], verify_certs=True)
        es.ping()
        storage = State_d(ElasticsearchImplementation.ElasticsearchImplementation())
    except Exception:
        storage = State_d(LocalImplementation.LocalImplementation())

    def getLog(self, startdate, enddate, amount):
        self.storage.search(startdate, enddate, amount)

    def storeLog(self, logitem):
        self.storage.storeLog(logitem)



