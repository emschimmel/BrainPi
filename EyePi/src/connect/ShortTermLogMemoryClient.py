import random
import sys
sys.path.append('../src/gen-py')
from ShortMemory import ShortMemoryService
from ShortMemory.ttypes import LogObject
from ShortMemory.ttypes import Log

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from dns import resolver
sys.path.append('../../')
import config

import time
import datetime
# ShortTermMemoryClient.py

class ShortTermLogMemoryClient:
    def __init__(self):
        self.log = {}

    @classmethod
    def log_exception(self, input, exception):
        log = Log()
        logObject = LogObject()
        logObject.action = input.action
        logObject.serviceName = 'EyePi'
        logObject.message = ('%s' % exception)
        logObject.person = input.person
        logObject.deviceToken = input.deviceToken
        ts = time.time()
        logObject.date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S')
        log.key = ts
        log.value = logObject
        self.__write_log(log)

    @classmethod
    def log_thrift_exception(self, input, exception):
        log = Log()
        logObject = LogObject()
        logObject.action = input.action
        logObject.serviceName = exception.serviceName
        logObject.message = exception.message
        logObject.endpoint = 'EyePi'
        logObject.person = input.person
        logObject.deviceToken = input.deviceToken
        ts = time.time()
        logObject.date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S')
        log.key = ts
        log.value = logObject
        self.__write_log(log)

    @classmethod
    def log_thrift_endpoint_exception(self, input, exception):
        log = Log()
        logObject = LogObject()
        logObject.action = input.action
        logObject.serviceName = exception.serviceName
        logObject.message = exception.message
        logObject.endpoint = exception.endpoint
        logObject.person = input.person
        logObject.deviceToken = input.deviceToken
        ts = time.time()
        logObject.date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S')
        log.key = ts
        log.value = logObject
        self.__write_log(log)

    @classmethod
    def log_event(self, input, message):
        log = Log()
        logObject = LogObject()
        logObject.action = input.action
        logObject.serviceName = 'EyePi'
        logObject.message = message
        logObject.person = input.person
        logObject.deviceToken = input.deviceToken
        ts = time.time()
        logObject.date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S')
        log.key = ts
        log.value = logObject
        print(log)
        self.__write_log(log)

    @classmethod
    def __write_log(self, input):
        print('short term memory handler, write log')
        ip, port = self.__resolve_config()
        transport = TSocket.TSocket(ip, port)  # Make socket
        try:
            transport = TTransport.TBufferedTransport(transport)  # Buffering is critical. Raw sockets are very slow
            protocol = TBinaryProtocol.TBinaryProtocol(transport)  # Wrap in a protocol
            client = ShortMemoryService.Client(protocol)  # Create a client to use the protocol encoder
            transport.open()  # Connect!
            client.writeLog(input)
            transport.close()
        except Thrift.TException as tx:
            print('%s' % (tx.message))
        except Exception as ex:
            print('whot??? %s' % ex)
        finally:
            transport.close()

    @staticmethod
    def __resolve_config():
        consul_resolver = resolver.Resolver()
        consul_resolver.port = config.consul_resolver_port
        consul_resolver.nameservers = [config.consul_ip]

        dnsanswer = consul_resolver.query("short-term-memory.service.consul.", 'A')
        ip = str(dnsanswer[0])
        dnsanswer_srv = consul_resolver.query("short-term-memory.service.consul.", 'SRV')
        port = int(str(random.choice(dnsanswer_srv)).split()[2])
        return ip, port

    @staticmethod
    def __submit_on_que(input):
        import pika

        connection = pika.BlockingConnection(pika.ConnectionParameters(config.rabbit_service_ip))
        channel = connection.channel()
        channel.queue_declare(queue='logging')
        channel.basic_publish(exchange='',
                              routing_key='logging',
                              body=input)
        connection.close()

