import random
import sys
sys.path.append('../gen-py')
from ShortMemory import ShortMemoryService
from ShortMemory.ttypes import *
from ThriftException.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from dns import resolver

import time
import datetime
# ShortTermMemoryClient.py

class ShortTermLogMemoryClient:
    def __init__(self):
        self.log = {}

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
        self.write_log(log)

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
        self.write_log(log)

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
        self.write_log(log)

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
        self.write_log(log)

    def write_log(self, input):
        print('short term memory handler, write log')
        try:
            ip, port = self.resolve_config()
            transport = TSocket.TSocket(ip, port)  # Make socket
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

    def resolve_config(self):
        consul_resolver = resolver.Resolver()
        consul_resolver.port = 8600
        consul_resolver.nameservers = ["127.0.0.1"]

        dnsanswer = consul_resolver.query("short-term-memory.service.consul.", 'A')
        ip = str(dnsanswer[0])
        dnsanswer_srv = consul_resolver.query("short-term-memory.service.consul.", 'SRV')
        port = int(str(random.choice(dnsanswer_srv)).split()[2])
        return ip, port

