import sys
sys.path.append('../../')
import config
import elasticsearch

class ElasticsearchImplementation():

    __esService = elasticsearch.Elasticsearch(hosts=[{'host': config.es_service_ip, 'port': config.es_service_port}], verify_certs=True)

    def __init__(self):
        pass

    @classmethod
    def storeLog(self, logInput):
        print("es store log")
        self.__esService.search(index=logInput.key, body=logInput.value)

    @classmethod
    def getLog(self, starttime, endtime, amount):
        # todo: es get log implementation
        print("es get log")
        #self.__esService.search()
