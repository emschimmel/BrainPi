import sys
sys.path.append('../gen-py')
from ShortMemory import ShortMemoryService
from ShortMemory.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

sys.path.append('../../')
import config

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
        logObject.actionParameters = input.actionParameters
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
        logObject.actionParameters = input.actionParameters
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
        logObject.actionParameters = input.actionParameters
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
        print('short term memory handler')
        try:
            transport = TSocket.TSocket(config.short_storage_ip, config.short_storage_port)  # Make socket
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

