#!/usr/bin/env python
import signal
import sys

import consul
from multiprocessing.managers import SyncManager

sys.path.append('../gen-py')
sys.path.append('./FaceDetection')
sys.path.append('./FaceRecognition')


from FacePi import FacePiThriftService
from FacePi.ttypes import FacePiOutput
from FacePi.ttypes import PersonEntry
from ThriftException.ttypes import ThriftServiceException

from FaceDetection.DetectFaces import DetectFaces
from FaceRecognition.RecognitionManager import RecognitionManager


from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

sys.path.append('../../')
import config
import logging
import random
import pickle

import statsd
stat = statsd.StatsClient(config.statsd_ip, config.statsd_port)

port = random.randint(50000, 59000)

log = logging.getLogger()
log.setLevel(logging.DEBUG)

class FacePiThriftHandler:
    def __init__(self):
        self.log = {}

    @stat.timer("handleRequest")
    def handleRequest(self, input):
        try:
            inputImage = pickle.loads(input.image, fix_imports=False, encoding="ASCII", errors="strict")
            # inputImage = input.image
            #HaarFaceDetection().detectFaceWithEyes(inputImage)
            #faces = RecognitionManager().recon_face(inputImage)
            faces = DetectFaces().DetectFromBinaryFromCamera(inputImage)

            personList = []
            if (faces is not None):
                print("Found {0} faces!".format(len(faces)))
                for face in faces:
                    person = PersonEntry()
                    person.person = '== Hans =='
                    person.chance = 90.0
                #    person.image = cv2.threshold(face,127,255,cv2.THRESH_BINARY)
                    person.image = pickle.dumps(obj=face, protocol=None, fix_imports=False)
                    personList.append(person)
            output = FacePiOutput()
            output.personCollection = personList
            print(output)
            return output
        except Exception as ex:
            print('invalid request %s' % ex)
            raise ThriftServiceException('FacePi', 'invalid request %s' % ex)

    @stat.timer("confirmFace")
    def confirmFace(self, input):
        print(input)
        # train the network with the found face with name
        print(input.person)

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
    handler = FacePiThriftHandler()
    return TServer.TSimpleServer(
        FacePiThriftService.Processor(handler),
        TSocket.TServerSocket(port=port),
        TTransport.TBufferedTransportFactory(),
        TBinaryProtocol.TBinaryProtocolFactory()
    )

def register():
    log.info("register started")
    c = consul.Consul(host=config.consul_ip, port=config.consul_port)
    check = consul.Check.tcp(host=get_ip(), port=port, interval=config.consul_interval, timeout=config.consul_timeout, deregister=unregister())
    c.agent.service.register(name="face-pi", service_id="face-pi-%d" % port, port=port, check=check)
    log.info("services: " + str(c.agent.services()))

def unregister():
    log.info("unregister started")
    c = consul.Consul(host=config.consul_ip, port=config.consul_port)
    c.agent.service.deregister("face-pi-%d" % port)
    c.agent.service.deregister("face-pi")
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
        print('finally FacePi shutting down')
        manager.shutdown()
