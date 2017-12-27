import sys
sys.path.append('../../')
import config
import elasticsearch

class ElasticsearchImplementation():



    def __init__(self):
        self.esService = elasticsearch.Elasticsearch([{'host': config.es_service_ip, 'port': config.es_service_port}],
                                         verify_certs=True)


        # self.esService = elasticsearch.Elasticsearch([{'host': config.es_service_ip, 'port': config.es_service_port}], verify_certs=True)

    def storeLog(self, logInput):
        print("es store log")
        self.esService.search(index=logInput.key, body=logInput.value)


    def getLog(self, starttime, endtime, amount):
        print("es get log")
        #self.esService.search()
