import sys

sys.path.append('../../')
import config

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
    except ImportError:
        elasticsearch = None
    if elasticsearch:
        try:
            es = elasticsearch.Elasticsearch(['http://%s:%d/' % config.es_service_ip % config.es_service_port], verify_certs=True)
            es.ping()
            from . import ElasticsearchImplementation
            storage = State_d(ElasticsearchImplementation.ElasticsearchImplementation())
        except Exception as ex:
            from . import LocalImplementation
            storage = State_d(LocalImplementation.LocalImplementation())
            print('%s' % ex.message)
    else:
        from . import LocalImplementation
        storage = State_d(LocalImplementation.LocalImplementation())

    def getLog(self, startdate, enddate, amount):
        self.storage.search(startdate, enddate, amount)

    def storeLog(self, logitem):
        self.storage.storeLog(logitem)



