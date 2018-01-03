#!/usr/bin/env python

import sys

import consul

import signal

from multiprocessing.managers import SyncManager

sys.path.append('../gen-py')

from LongTermPersonMemoryClient import LongTermPersonMemoryClient
from ShortTermTokenMemoryClient import ShortTermTokenMemoryClient

from EarPi import EarPiThriftService
from EarPi.ttypes import UserOutput
from EarPi.ttypes import UserListOutput
from EarPi.ttypes import DeviceListOutput
from ThriftException.ttypes import BadHashException
from ThriftException.ttypes import LoginFailedException
from ThriftException.ttypes import ExternalEndpointUnavailable
from ThriftException.ttypes import ThriftServiceException
from ThriftException.ttypes import UniqueFailedException
from GenericStruct.ttypes import ActionEnum

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

sys.path.append('../../../')
import config
import logging
import random
import statsd
stat = statsd.StatsClient(config.statsd_ip, config.statsd_port)

port = random.randint(50000, 59000)

log = logging.getLogger()
log.setLevel(logging.DEBUG)

class EarPiThriftHandler:
    def __init__(self):
        self.log = {}

    @stat.timer("EarPi.createNewPerson")
    def createNewPerson(self, person, tokenInput):
        try:
            if not ShortTermTokenMemoryClient().validateToken(earPiAuthObject=tokenInput):
                raise LoginFailedException
            output = UserOutput()
            output.person = LongTermPersonMemoryClient().createNewPerson(person=person)
            output.token = ShortTermTokenMemoryClient().getToken(earPiAuthObject=tokenInput)
            return output
        except UniqueFailedException as unique:
            raise unique

    @stat.timer("EarPi.getUser")
    def getUser(self, uniquename, tokenInput):
        if not ShortTermTokenMemoryClient().validateToken(earPiAuthObject=tokenInput):
            raise LoginFailedException
        output = UserOutput()
        output.person = LongTermPersonMemoryClient().get_Person(input=uniquename)
        output.token = ShortTermTokenMemoryClient().getToken(earPiAuthObject=tokenInput)
        return output

    @stat.timer("EarPi.getUserList")
    def getUserList(self, tokenInput):
        if not ShortTermTokenMemoryClient().validateToken(earPiAuthObject=tokenInput):
            raise LoginFailedException
        output = UserListOutput()
        output.personList = LongTermPersonMemoryClient().getUserList()
        output.token = ShortTermTokenMemoryClient().getToken(earPiAuthObject=tokenInput)
        return output

    @stat.timer("EarPi.changeUser")
    def changeUser(self, field, person, tokenInput):
        if not ShortTermTokenMemoryClient().validateToken(earPiAuthObject=tokenInput):
            raise LoginFailedException
        LongTermPersonMemoryClient().changeUser(field=field, person=person)
        output = ShortTermTokenMemoryClient().getToken(earPiAuthObject=tokenInput)
        return output

    @stat.timer("EarPi.configureUser")
    def configureUser(self, userlist, tokenInput):
        if not ShortTermTokenMemoryClient().validateToken(earPiAuthObject=tokenInput):
            raise LoginFailedException
        LongTermPersonMemoryClient().configureUser(userlist=userlist)
        output = ShortTermTokenMemoryClient().getToken(earPiAuthObject=tokenInput)
        return output

    @stat.timer("EarPi.configureUserModule")
    def configureUserModule(self, uniquename, autorisations, tokenInput):
        if not ShortTermTokenMemoryClient().validateToken(earPiAuthObject=tokenInput):
            raise LoginFailedException
        LongTermPersonMemoryClient().configureUserModule(uniquename=uniquename, autorisations=autorisations)
        output = ShortTermTokenMemoryClient().getToken(earPiAuthObject=tokenInput)
        return output

    @stat.timer("EarPi.configureModuleSettings")
    def configureModuleSettings(self, uniquename, action, config, tokenInput):
        if not ShortTermTokenMemoryClient().validateToken(earPiAuthObject=tokenInput):
            raise LoginFailedException
        LongTermPersonMemoryClient().configureModuleSettings(uniquename=uniquename, action=action, config=config)
        output = ShortTermTokenMemoryClient().getToken(earPiAuthObject=tokenInput)
        return output

    @stat.timer("EarPi.getDeviceList")
    def getDeviceList(self, tokenInput):
        if not ShortTermTokenMemoryClient().validateToken(earPiAuthObject=tokenInput):
            raise LoginFailedException
        output = DeviceListOutput()
        output.deviceList = ShortTermTokenMemoryClient().getDeviceList()
        output.token = ShortTermTokenMemoryClient().getToken(earPiAuthObject=tokenInput)
        return output

    @stat.timer("EarPi.confirmDevice")
    def confirmDevice(self, deviceToken, active, tokenInput):
        if not ShortTermTokenMemoryClient().validateToken(earPiAuthObject=tokenInput):
            raise LoginFailedException
        ShortTermTokenMemoryClient().confirmDevice(devicetoken=deviceToken, active=active)
        output = ShortTermTokenMemoryClient().getToken(earPiAuthObject=tokenInput)
        return output

    @stat.timer("EarPi.changePassword")
    def changePassword(self, username, password, tokenInput):
        try:
            if not ShortTermTokenMemoryClient().validateToken(earPiAuthObject=tokenInput):
                raise LoginFailedException
            LongTermPersonMemoryClient().changePassword(username=username, password=password)
            output = ShortTermTokenMemoryClient().getToken(earPiAuthObject=tokenInput)
            return output
        except BadHashException as badHash:
            # ShortTermLogMemoryClient().log_thrift_exception(loginObject, badHash)
            raise badHash
        except LoginFailedException as fail:
            # ShortTermLogMemoryClient().log_thrift_exception(loginObject, fail)
            raise fail

    @stat.timer("EarPi.ping")
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
    handler = EarPiThriftHandler()
    return TServer.TSimpleServer(
        EarPiThriftService.Processor(handler),
        TSocket.TServerSocket(port=port),
        TTransport.TBufferedTransportFactory(),
        TBinaryProtocol.TBinaryProtocolFactory()
    )

def register():
    log.info("register started")
    c = consul.Consul(host=config.consul_ip, port=config.consul_port)
    check = consul.Check.tcp(host=get_ip(), port=port, interval=config.consul_interval,
                             timeout=config.consul_timeout, deregister=unregister())
    c.agent.service.register(name="ear-pi", service_id="ear-pi-%d" % port, port=port, check=check)
    log.info("services: " + str(c.agent.services()))

def unregister():
    log.info("unregister started")
    c = consul.Consul(host=config.consul_ip, port=config.consul_port)
    c.agent.service.deregister("ear-pi-%d" % port)
    c.agent.service.deregister("ear-pi")
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
        print('finally EarPi shutting down')
        manager.shutdown()
