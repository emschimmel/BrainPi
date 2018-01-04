#!/usr/bin/env python
import signal
import sys

import consul
from multiprocessing.managers import SyncManager

import pickle

sys.path.append('../gen-py')

from GenericServerPi import GenericPiThriftService
from GenericStruct.ttypes import ActionEnum
from ThriftException.ttypes import ThriftServiceException
from MusicPi.ttypes import Action


from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

sys.path.append('../../')
import config

import logging
import random

import statsd
stat = statsd.StatsClient(config.statsd_ip, config.statsd_port)
port = random.randint(58860, 58870)

log = logging.getLogger()
log.setLevel(logging.DEBUG)

class MusicPiThriftHandler:

    @stat.timer("MusicPi.handleRequest")
    def handleRequest(self, input):
        print("music pi!")
        try:
            input_object = pickle.loads(input, fix_imports=False, encoding="ASCII", errors="strict")
            output = ""
            if input_object.action is Action.GET_PLAYLISTS:
                pass
            elif input_object.action is Action.GET_PLAYLIST:
                pass
            elif input_object.action is Action.GET_SONG:
                pass
            elif input_object.action is Action.PLAY_SONG:
                pass
            elif input_object.action is Action.SEARCH:
                pass
            elif input_object.action is Action.START_PLAYING:
                pass
            elif input_object.action is Action.STOP_PLAYING:
                pass

            pickle_output = pickle.dumps(obj=output, protocol=None, fix_imports=False)
            return pickle_output

        except Exception as ex:
            print('invalid request %s' % ex)
            raise ThriftServiceException('MusicPi', 'invalid request %s' % ex)

    @stat.timer("MusicPi.getDefaultModuleConfig")
    def getDefaultModuleConfig(self):
        default_config = FloorLayout.getLayout()
        return pickle.dumps(obj=default_config, protocol=None, fix_imports=False)

    @stat.timer("MusicPi.ping")
    def ping(self, input):
        print(input)

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
    handler = MusicPiThriftHandler()
    return TServer.TSimpleServer(
        GenericPiThriftService.Processor(handler),
        TSocket.TServerSocket(port=port),
        TTransport.TBufferedTransportFactory(),
        TBinaryProtocol.TBinaryProtocolFactory()
    )

def register():
    log.info("register started")
    c = consul.Consul(host=config.consul_ip, port=config.consul_port)
    key = '%d' % ActionEnum.MUSIC
    c.kv.put(key, 'music')
    check = consul.Check.tcp(host=get_ip(), port=port, interval=config.consul_interval,
                             timeout=config.consul_timeout, deregister=unregister())
    c.agent.service.register(name="music-pi", service_id="music-pi-%d" % port, port=port, check=check)
    log.info("services: " + str(c.agent.services()))

def unregister():
    log.info("unregister started")
    c = consul.Consul(host=config.consul_ip, port=config.consul_port)
    c.agent.service.deregister("music-pi-%d" % port)
    c.agent.service.deregister("music-pi")
    log.info("services: " + str(c.agent.services()))

def interupt_manager():
    signal.signal(signal.SIGINT, signal.SIG_IGN)

if __name__ == '__main__':
    manager = SyncManager()
    manager.start(interupt_manager)
    try:
        server = create_server()
        register()
        server.serve()

    finally:
        unregister()
        print('finally MusicPi shutting down')
        manager.shutdown()
