#!/usr/bin/env python
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import sys
import re
import consul
import signal

from tensorflow.python.platform import gfile
from multiprocessing.managers import SyncManager

sys.path.append('./gen-py')

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

port = random.randint(58830, 58840)

log = logging.getLogger()
log.setLevel(logging.DEBUG)

class FacePiThriftHandler():
    def __init__(self, tensorSession):
        self.tensorSession = tensorSession

    @stat.timer("FacePi.handleRequest")
    def handleRequest(self, input):
        try:
            inputImage = pickle.loads(input.image, fix_imports=False, encoding="ASCII", errors="strict")
            # inputImage = input.image
            #HaarFaceDetection().detectFaceWithEyes(inputImage)
            print("handling")
            #faces = DetectFaces().DetectFromBinaryFromCamera(inputImage)

            output = FacePiOutput()
            output.personCollection = RecognitionManager().recon_face(self.tensorSession, inputImage)
            print(output)
            return output
        except Exception as ex:
            print('invalid request %s' % ex)
            raise ThriftServiceException('FacePi', 'invalid request %s' % ex)

    @stat.timer("FacePi.confirmFace")
    def confirmFace(self, input):
        print(input)
        # train the network with the found face with name
        print(input.person)

    @stat.timer("FacePi.trainNetwork")
    def trainNetwork(self):
        RecognitionManager().train()

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

def create_server(sess):
    handler = FacePiThriftHandler(sess)
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


def load_model(self):
    model_exp = os.path.expanduser(config.tensor_model_path)
    if (os.path.isfile(model_exp)):
        print('Model filename: %s' % model_exp)
        with gfile.FastGFile(model_exp, 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            tf.import_graph_def(graph_def, name='')
    else:
        print('Model directory: %s' % model_exp)
        meta_file, ckpt_file = self.get_model_filenames()

        print('Metagraph file: %s' % meta_file)
        print('Checkpoint file: %s' % ckpt_file)

        saver = tf.train.import_meta_graph(os.path.join(model_exp, meta_file))
        saver.restore(tf.get_default_session(), os.path.join(model_exp, ckpt_file))

def get_model_filenames():
    model_dir = config.tensor_model_path
    files = os.listdir(model_dir)
    meta_files = [s for s in files if s.endswith('.meta')]
    if len(meta_files) == 0:
        raise ValueError('No meta file found in the model directory (%s)' % model_dir)
    elif len(meta_files) > 1:
        raise ValueError('There should not be more than one meta file in the model directory (%s)' % model_dir)
    meta_file = meta_files[0]
    meta_files = [s for s in files if '.ckpt' in s]
    max_step = -1
    for f in files:
        step_str = re.match(r'(^model-[\w\- ]+.ckpt-(\d+))', f)
        if step_str is not None and len(step_str.groups()) >= 2:
            step = int(step_str.groups()[1])
            if step > max_step:
                max_step = step
                ckpt_file = step_str.groups()[0]
    return meta_file, ckpt_file

def main(args=None):
    with tf.Graph().as_default():
        with tf.Session() as sess:
            manager = SyncManager()
            manager.start(interupt_manager)
            try:
                server = create_server(sess)
                register()
                server.serve()
            finally:
                unregister()
                print('finally FacePi shutting down')
                manager.shutdown()

if __name__ == '__main__':
    main()
