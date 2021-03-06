import signal
import sys

import consul
from multiprocessing.managers import SyncManager

sys.path.append('./gen-py')
from ShortMemory import ShortMemoryService
from AuthToken.TokenMemory import TokenMemory
from Logging.LogMemory import LogMemory
from DeviceMemory import DeviceMemory

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

sys.path.append('../../')
import config
import logging
import random
import statsd

port = random.randint(58880, 58890)
stat = statsd.StatsClient(config.statsd_ip, config.statsd_port)

log = logging.getLogger()
log.setLevel(logging.DEBUG)

class ShortTermMemoryThriftServer:
    def __init__(self):
        self.log = {}

    @stat.timer("ShortTermMemory.generateToken")
    def generateToken(self, tokenObject):
        try:
            return TokenMemory().generateToken(tokenObject)
        except Exception as ex:
            print('invalid request %s' % ex)

    @stat.timer("ShortTermMemory.validateToken")
    def validateToken(self, stringToken, deviceToken):
        try:
            if (DeviceMemory.validateDeviceToken(deviceToken)):
                return TokenMemory().validateToken(stringToken, deviceToken)
            return False
        except Exception as ex:
            print('invalid request %s' % ex)

    @stat.timer("ShortTermMemory.writeLog")
    def writeLog(self, log):
        try:
            LogMemory().storeLog(log)
        except Exception as ex:
            print('invalid request %s' % ex)

    @stat.timer("ShortTermMemory.readLog")
    def readLog(self, starttime, endtime, amount):
        try:
            return LogMemory().getLog(starttime, endtime, amount)
        except Exception as ex:
            print('invalid request %s' % ex)

    @stat.timer("ShortTermMemory.generateDeviceToken")
    def generateDeviceToken(self, input):
        try:
            return DeviceMemory().generateDeviceToken(input)
        except Exception as ex:
            print('invalid request %s' % ex)

    @stat.timer("ShortTermMemory.validateDeviceToken")
    def validateDeviceToken(self, input):
        try:
            return DeviceMemory().validateDeviceToken(input)
        except Exception as ex:
            print('invalid request %s' % ex)

    @stat.timer("ShortTermMemory.confirmDevice")
    def confirmDevice(self, devicetoken, enabled):
        try:
            DeviceMemory().confirmDevice(devicetoken=devicetoken, enabled=enabled)
        except Exception as ex:
            print('invalid request %s' % ex)

    @stat.timer("ShortTermMemory.getDeviceList")
    def getDeviceList(self):
        try:
            return DeviceMemory().getDeviceList()
        except Exception as ex:
            print('invalid request %s' % ex)

    def processLog(self, ch, method, properties, body):
        try:
            LogMemory().storeLog(body)
        except Exception as ex:
            print('invalid request %s' % ex)

    def logSubscriber(self):
        import pika
        connection = pika.BlockingConnection(pika.ConnectionParameters(config.rabbit_service_ip))
        channel = connection.channel()
        channel.basic_consume(self.processLog,
                              queue='logging',
                              no_ack=True)
        channel.start_consuming()




def get_ip():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('255.255.255.255', 1)) # isn't reachable intentionally
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def create_server():
    handler = ShortTermMemoryThriftServer()
    return TServer.TSimpleServer(
        ShortMemoryService.Processor(handler),
        TSocket.TServerSocket(port=port),
        TTransport.TBufferedTransportFactory(),
        TBinaryProtocol.TBinaryProtocolFactory()
    )

def register():
    log.info("register started")
    c = consul.Consul(host=config.consul_ip, port=config.consul_port)
    check = consul.Check.tcp(host=get_ip(), port=port, interval=config.consul_interval,
                             timeout=config.consul_timeout, deregister=unregister())
    c.agent.service.register(name="short-term-memory", service_id="short-term-memory-%d" % port, port=port, check=check)
    log.info("services: " + str(c.agent.services()))

def unregister():
    log.info("unregister started")
    c = consul.Consul(host=config.consul_ip, port=config.consul_port)
    c.agent.service.deregister("short-term-memory-%d" % port)
    c.agent.service.deregister("short-term-memory")
    log.info("services: " + str(c.agent.services()))

def interupt_manager():
    signal.signal(signal.SIGINT, signal.SIG_IGN)

def main(args=None):
    manager = SyncManager()
    manager.start(interupt_manager)
    try:
        server = create_server()
        # ShortTermMemoryThriftServer().logSubscriber() # test
        register()
        server.serve()

    finally:
        unregister()
        print('finally Short term memory Shutting down')
        manager.shutdown()

if __name__ == '__main__':
    main()