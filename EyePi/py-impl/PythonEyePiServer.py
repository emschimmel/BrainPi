#!/usr/bin/env python

import sys

import consul

import signal

from multiprocessing.managers import SyncManager

sys.path.append('../gen-py')

from PythonFacePiClient import FacePiThriftClient
from GenericThriftClient import GenericThriftClient
from LongTermPersonMemoryClient import LongTermPersonMemoryClient
from ShortTermLogMemoryClient import ShortTermLogMemoryClient
from ShortTermTokenMemoryClient import ShortTermTokenMemoryClient

from EyePi import EyePiThriftService
from EyePi.ttypes import LoginOutputObject
from EyePi.ttypes import EyePiInput
from EyePi.ttypes import EyePiOutput
from ThriftException.ttypes import BadHashException
from ThriftException.ttypes import LoginFailedException
from ThriftException.ttypes import ExternalEndpointUnavailable
from ThriftException.ttypes import ThriftServiceException
from GenericStruct.ttypes import ActionEnum

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

sys.path.append('../../')
import pickle
import config
import logging
import random
import threading
import statsd
stat = statsd.StatsClient(config.statsd_ip, config.statsd_port)

port = random.randint(50000, 59000)

log = logging.getLogger()
log.setLevel(logging.DEBUG)

class EyePiThriftHandler:
    def __init__(self):
        self.log = {}

    @stat.timer("login")
    def login(self, loginObject):
        try:
            output = LoginOutputObject()
            if not loginObject.deviceInput and not loginObject.deviceToken:
                return output
            person = LongTermPersonMemoryClient().loginCall(loginObject)
            if person:
                output.uniquename = person.uniquename
                output.details = person.details
                output.autorisations = person.autorisations
            if not person:
                return output

            if loginObject.deviceToken is not None:
                output.deviceToken = loginObject.deviceToken
                if ShortTermTokenMemoryClient().validateDeviceToken(loginObject.deviceToken):
                    output.token = self.__get_request_token(uniquename=person.uniquename, deviceToken=loginObject.deviceToken)

            else:
                deviceToken = ShortTermTokenMemoryClient().register_device(loginObject.deviceInput)
                output.deviceToken = deviceToken
            return output
        except BadHashException as badHash:
            # ShortTermLogMemoryClient().log_thrift_exception(loginObject, badHash)
            raise badHash
        except LoginFailedException as fail:
            # ShortTermLogMemoryClient().log_thrift_exception(loginObject, fail)
            raise fail

    @staticmethod
    def __get_request_token(uniquename, deviceToken):
        eyeInput = EyePiInput()
        actions = dict()
        actions[ActionEnum.LOGIN] = pickle.dumps(obj=uniquename, protocol=None, fix_imports=False)
        eyeInput.action = actions
        eyeInput.person = uniquename
        eyeInput.deviceToken = deviceToken
        return ShortTermTokenMemoryClient().getToken(eyeInput)

    @stat.timer("handleRequest")
    def handleRequest(self, input):
        try:
            ShortTermLogMemoryClient().log_event(input, message='start eyepi')
            eyeOutput = EyePiOutput()
            tokenValide = False
            if input.token:
                tokenValide = ShortTermTokenMemoryClient().validateToken(input.token, input.deviceToken)
            if input.image:
                eyeOutput.ok = False
                eyeOutput.personCollection = []
                facePiOutput = FacePiThriftClient().handle_request(input.image)

                for face in facePiOutput:
                    name = face.person
                    person = LongTermPersonMemoryClient().get_Person(input=name)
                    if person:
                        if person.enabled:
                            eyeOutput.personCollection.append(face)
                # eyeOutput.personCollection = facePiOutput

                if eyeOutput.personCollection:
                    eyeOutput.ok = True
                    eyeOutput.token = ShortTermTokenMemoryClient().getToken(input)

            if tokenValide and not input.image:
                eyeOutput.ok = False
            if eyeOutput.ok:
                eyeOutput.data = self.__make_generic_call(input.action)
            return eyeOutput
        except ThriftServiceException as tex:
            ShortTermLogMemoryClient().log_thrift_exception(input, tex)
            raise tex
        except ExternalEndpointUnavailable as endEx:
            ShortTermLogMemoryClient().log_thrift_endpoint_exception(input, endEx)
            raise endEx
        except Exception as ex:
            ShortTermLogMemoryClient().log_exception(input, ex)
            print('invalid request %s' % ex)
            raise ThriftServiceException('EyePi', 'invalid request %s' % ex)

    @staticmethod
    def __make_generic_call(input):
        threads = [None] * len(ActionEnum._VALUES_TO_NAMES)
        call_result = [{}] * len(ActionEnum._VALUES_TO_NAMES)
        for key, request in input.items():
            try:
                threads[key] = threading.Thread(target=GenericThriftClient().handle_request, args=(key, request, call_result))
                threads[key].start()
            #    return GenericThriftClient().handle_request(key, request.actionParameters)
            except Exception as ex:
                print('test')
                print('%s' % ex)
            except Thrift.TException as tx:
                print('test')
                print('%s' % tx.message)
                raise tx
            except ThriftServiceException as tex:
                raise tex
            except ExternalEndpointUnavailable as endEx:
                raise endEx
                # probably try again
        for key in input:
            threads[key].join()
        output = {}
        for key in range(len(call_result)):
            value = call_result[key]
            if value:
                output[key] = value
              # output = {**output, **i}
        return output

    @stat.timer("confimFace")
    def confimFace(self, input):
        FacePiThriftClient.confim_face(self, input)


    @stat.timer("writeLog")
    def writeLog(self, input):
        ShortTermLogMemoryClient().log_event(input, message='start eyepi')

    @stat.timer("ping")
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
    handler = EyePiThriftHandler()
    return TServer.TSimpleServer(
        EyePiThriftService.Processor(handler),
        TSocket.TServerSocket(port=port),
        TTransport.TBufferedTransportFactory(),
        TBinaryProtocol.TBinaryProtocolFactory()
    )

def register():
    log.info("register started")
    c = consul.Consul(host=config.consul_ip, port=config.consul_port)
    check = consul.Check.tcp(host=get_ip(), port=port, interval=config.consul_interval,
                             timeout=config.consul_timeout, deregister=unregister())
    c.agent.service.register(name="eye-pi", service_id="eye-pi-%d" % port, port=port, check=check)
    log.info("services: " + str(c.agent.services()))

def unregister():
    log.info("unregister started")
    c = consul.Consul(host=config.consul_ip, port=config.consul_port)
    c.agent.service.deregister("eye-pi-%d" % port)
    c.agent.service.deregister("eye-pi")
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
        print('finally EyePi shutting down')
        manager.shutdown()
