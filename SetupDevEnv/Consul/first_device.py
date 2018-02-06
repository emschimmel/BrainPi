import sys
sys.path.append('./gen-py')
from ShortMemory.ttypes import DeviceTokenInput
sys.path.append('../../')

from thrift import TSerialization
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport

import config
import consul

class FirstDevice:

    __consul_instance = consul.Consul(host=config.consul_ip, port=config.consul_port)
    __key = "ABCDEFGH"

    def __init__(self):
        pass

    @classmethod
    def enterDummy(self):
        self.__consul_instance.kv.put(self.__key, self.__serializeDeviceToken(input=self.__generateDeviceToken()))
        print("DeviceToken = %s" % self.__key)


    @staticmethod
    def __generateDeviceToken():
        tokenInput = DeviceTokenInput()
        tokenInput.enabled = True
        tokenInput.devicetype = 'Dummy'
        tokenInput.ip = get_ip()
        return tokenInput

    @staticmethod
    def __serializeDeviceToken(input):
        transportOut = TTransport.TMemoryBuffer()
        protocolOut = TBinaryProtocol.TBinaryProtocol(transportOut)
        input.write(protocolOut)
        return transportOut.getvalue()

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

if __name__ == '__main__':
    FirstDevice().enterDummy()