import random

import sys
sys.path.append('../gen-py')
from EyePi import EyePiThriftService

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from dns import resolver
sys.path.append('../../')
import config

class ConnectEarPi:

    def getUserList(self, tokenInput):
        ip, port = self.__resolve_eye_config()
        transport = TSocket.TSocket(ip, port)
        try:
            transport = TTransport.TBufferedTransport(transport)
            protocol = TBinaryProtocol.TBinaryProtocol(transport)
            client = EyePiThriftService.Client(protocol)
            transport.open()
            output = client.getUserList(tokenInput=tokenInput)
            transport.close()
            return output
        except Thrift.TException as tx:
            print("%s" % (tx.message))
        finally:
            transport.close()

    def changeUser(self, field, person, tokenInput):
        ip, port = self.__resolve_eye_config()
        transport = TSocket.TSocket(ip, port)
        try:
            transport = TTransport.TBufferedTransport(transport)
            protocol = TBinaryProtocol.TBinaryProtocol(transport)
            client = EyePiThriftService.Client(protocol)
            transport.open()
            output = client.changeUser(field=field, person=person, tokenInput=tokenInput)
            transport.close()
            return output
        except Thrift.TException as tx:
            print("%s" % (tx.message))
        finally:
            transport.close()

    def configureUser(self, userlist, tokenInput):
        ip, port = self.__resolve_eye_config()
        transport = TSocket.TSocket(ip, port)
        try:
            transport = TTransport.TBufferedTransport(transport)
            protocol = TBinaryProtocol.TBinaryProtocol(transport)
            client = EyePiThriftService.Client(protocol)
            transport.open()
            output = client.configureUser(userlist=userlist, tokenInput=tokenInput)
            transport.close()
            return output
        except Thrift.TException as tx:
            print("%s" % (tx.message))
        finally:
            transport.close()

    def configureUserModule(self, uniquename, autorisations, tokenInput):
        ip, port = self.__resolve_eye_config()
        transport = TSocket.TSocket(ip, port)
        try:
            transport = TTransport.TBufferedTransport(transport)
            protocol = TBinaryProtocol.TBinaryProtocol(transport)
            client = EyePiThriftService.Client(protocol)
            transport.open()
            output = client.configureUserModule(uniquename=uniquename, autorisations=autorisations, tokenInput=tokenInput)
            transport.close()
            return output
        except Thrift.TException as tx:
            print("%s" % (tx.message))
        finally:
            transport.close()

    def configureModuleSettings(self, uniquename, action, config, tokenInput):
        ip, port = self.__resolve_eye_config()
        transport = TSocket.TSocket(ip, port)
        try:
            transport = TTransport.TBufferedTransport(transport)
            protocol = TBinaryProtocol.TBinaryProtocol(transport)
            client = EyePiThriftService.Client(protocol)
            transport.open()
            output = client.configureModuleSettings(uniquename=uniquename, action=action, config=config, tokenInput=tokenInput)
            transport.close()
            return output
        except Thrift.TException as tx:
            print("%s" % (tx.message))
        finally:
            transport.close()

    def getDeviceList(self, tokenInput):
        ip, port = self.__resolve_eye_config()
        transport = TSocket.TSocket(ip, port)
        try:
            transport = TTransport.TBufferedTransport(transport)
            protocol = TBinaryProtocol.TBinaryProtocol(transport)
            client = EyePiThriftService.Client(protocol)
            transport.open()
            output = client.getDeviceList(tokenInput=tokenInput)
            transport.close()
            return output
        except Thrift.TException as tx:
            print("%s" % (tx.message))
        finally:
            transport.close()

    def confirmDevice(self, deviceToken, active, tokenInput):
        ip, port = self.__resolve_eye_config()
        transport = TSocket.TSocket(ip, port)
        try:
            transport = TTransport.TBufferedTransport(transport)
            protocol = TBinaryProtocol.TBinaryProtocol(transport)
            client = EyePiThriftService.Client(protocol)
            transport.open()
            output = client.confirmDevice(deviceToken=deviceToken, active=active, tokenInput=tokenInput)
            transport.close()
            return output
        except Thrift.TException as tx:
            print("%s" % (tx.message))
        finally:
            transport.close()

    def changePassword(self, username, password, tokenInput):
        ip, port = self.__resolve_eye_config()
        transport = TSocket.TSocket(ip, port)
        try:
            transport = TTransport.TBufferedTransport(transport)
            protocol = TBinaryProtocol.TBinaryProtocol(transport)
            client = EyePiThriftService.Client(protocol)
            transport.open()
            output = client.changePassword(username=username, password=password, tokenInput=tokenInput)
            transport.close()
            return output
        except Thrift.TException as tx:
            print("%s" % (tx.message))
        finally:
            transport.close()

    def __resolve_eye_config(self):
        consul_resolver = resolver.Resolver()
        consul_resolver.port = config.consul_resolver_port
        consul_resolver.nameservers = [config.consul_ip]
        dnsanswer = consul_resolver.query("eye-pi.service.consul.", "A")
        ip = str(dnsanswer[0])
        dnsanswer_srv = consul_resolver.query("eye-pi.service.consul.", "SRV")
        port = int(str(random.choice(dnsanswer_srv)).split()[2])
        return ip, port



