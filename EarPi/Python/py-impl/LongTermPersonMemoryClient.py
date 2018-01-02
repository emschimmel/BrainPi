import random
import sys
sys.path.append('../gen-py')
from LongMemory import LongMemoryService
from LongMemory.ttypes import LongMemoryLoginInputObject
from AutorisationStruct.ttypes import Person
from ThriftException.ttypes import BadHashException
from ThriftException.ttypes import LoginFailedException
from ThriftException.ttypes import UniqueFailedException

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from dns import resolver
sys.path.append('../../../')
import config

class LongTermPersonMemoryClient:
    def __init__(self):
        pass

    @classmethod
    def createNewPerson(self, person):
        ip, port = self.__resolve_config()
        transport = TSocket.TSocket(ip, port)  # Make socket
        try:
            transport = TTransport.TBufferedTransport(transport)  # Buffering is critical. Raw sockets are very slow
            protocol = TBinaryProtocol.TBinaryProtocol(transport)  # Wrap in a protocol
            client = LongMemoryService.Client(protocol)  # Create a client to use the protocol encoder
            transport.open()  # Connect!
            person = client.storeNewPerson(person=person)
            transport.close()
            return person
        except UniqueFailedException as unique:
            raise unique
        except Thrift.TException as tx:
            print('%s' % (tx.message))
        except Exception as ex:
            print('whot??? %s' % ex)
        finally:
            transport.close()

    @classmethod
    def get_Person(self, input):
        ip, port = self.__resolve_config()
        transport = TSocket.TSocket(ip, port)  # Make socket
        try:
            transport = TTransport.TBufferedTransport(transport)  # Buffering is critical. Raw sockets are very slow
            protocol = TBinaryProtocol.TBinaryProtocol(transport)  # Wrap in a protocol
            client = LongMemoryService.Client(protocol)  # Create a client to use the protocol encoder
            transport.open()  # Connect!
            person = client.getPersonConfig(uniquename=input)
            transport.close()
            return person
        except Thrift.TException as tx:
            print('%s' % (tx.message))
        except Exception as ex:
            print('whot??? %s' % ex)
        finally:
            transport.close()

    @classmethod
    def getUserList(self):
        ip, port = self.__resolve_config()
        transport = TSocket.TSocket(ip, port)  # Make socket
        try:
            transport = TTransport.TBufferedTransport(transport)  # Buffering is critical. Raw sockets are very slow
            protocol = TBinaryProtocol.TBinaryProtocol(transport)  # Wrap in a protocol
            client = LongMemoryService.Client(protocol)  # Create a client to use the protocol encoder
            transport.open()
            personList = client.getAll()
            transport.close()
            return personList
        except Thrift.TException as tx:
            print('%s' % (tx.message))
        except Exception as ex:
            print('whot??? %s' % ex)
        finally:
            transport.close()

    @classmethod
    def changeUser(self, field, person):
        ip, port = self.__resolve_config()
        transport = TSocket.TSocket(ip, port)  # Make socket
        try:
            transport = TTransport.TBufferedTransport(transport)  # Buffering is critical. Raw sockets are very slow
            protocol = TBinaryProtocol.TBinaryProtocol(transport)  # Wrap in a protocol
            client = LongMemoryService.Client(protocol)  # Create a client to use the protocol encoder
            transport.open()
            client.updatePerson(field=field, person=person)
            transport.close()
        except Thrift.TException as tx:
            print('%s' % (tx.message))
        except Exception as ex:
            print('whot??? %s' % ex)
        finally:
            transport.close()

    @classmethod
    def configureUser(self, userlist):
        ip, port = self.__resolve_config()
        transport = TSocket.TSocket(ip, port)  # Make socket
        try:
            transport = TTransport.TBufferedTransport(transport)  # Buffering is critical. Raw sockets are very slow
            protocol = TBinaryProtocol.TBinaryProtocol(transport)  # Wrap in a protocol
            client = LongMemoryService.Client(protocol)  # Create a client to use the protocol encoder
            transport.open()
            for user in userlist:
                client.updatePerson(field='enabled', person=user)
            transport.close()
        except Thrift.TException as tx:
            print('%s' % (tx.message))
        except Exception as ex:
            print('whot??? %s' % ex)
        finally:
            transport.close()

    @classmethod
    def configureUserModule(self, uniquename, autorisations):
        ip, port = self.__resolve_config()
        transport = TSocket.TSocket(ip, port)  # Make socket
        try:
            person = Person()
            person.uniquename = uniquename
            person.autorisations = autorisations

            transport = TTransport.TBufferedTransport(transport)  # Buffering is critical. Raw sockets are very slow
            protocol = TBinaryProtocol.TBinaryProtocol(transport)  # Wrap in a protocol
            client = LongMemoryService.Client(protocol)  # Create a client to use the protocol encoder
            transport.open()
            client.updatePerson(field='autorisations', person=person)
            transport.close()
        except Thrift.TException as tx:
            print('%s' % (tx.message))
        except Exception as ex:
            print('whot??? %s' % ex)
        finally:
            transport.close()

    @classmethod
    def configureModuleSettings(self, uniquename, action, config):
        ip, port = self.__resolve_config()
        transport = TSocket.TSocket(ip, port)  # Make socket
        try:
            person = Person()
            person.uniquename = uniquename

            transport = TTransport.TBufferedTransport(transport)  # Buffering is critical. Raw sockets are very slow
            protocol = TBinaryProtocol.TBinaryProtocol(transport)  # Wrap in a protocol
            client = LongMemoryService.Client(protocol)  # Create a client to use the protocol encoder
            transport.open()
            client.updateActionConfig(uniquename=uniquename, action=action, config=config)
            transport.close()
        except Thrift.TException as tx:
            print('%s' % (tx.message))
        except Exception as ex:
            print('whot??? %s' % ex)
        finally:
            transport.close()

    @classmethod
    def changePassword(self, username, password):
        ip, port = self.__resolve_config()
        transport = TSocket.TSocket(ip, port)  # Make socket
        try:
            transport = TTransport.TBufferedTransport(transport)  # Buffering is critical. Raw sockets are very slow
            protocol = TBinaryProtocol.TBinaryProtocol(transport)  # Wrap in a protocol
            client = LongMemoryService.Client(protocol)  # Create a client to use the protocol encoder
            transport.open()
            # TODO review this!
            client.changePassword(username=username, password=password)
            transport.close()
        except BadHashException as bad:
            raise bad
        except LoginFailedException as fail:
            raise fail
        except Thrift.TException as tx:
            print('%s' % (tx.message))
        except Exception as ex:
            print('whot??? %s' % ex)
        finally:
            transport.close()

    @staticmethod
    def __resolve_config():
        consul_resolver = resolver.Resolver()
        consul_resolver.port = config.consul_resolver_port
        consul_resolver.nameservers = [config.consul_ip]

        dnsanswer = consul_resolver.query("long-term-memory.service.consul.", 'A')
        ip = str(dnsanswer[0])
        dnsanswer_srv = consul_resolver.query("long-term-memory.service.consul.", 'SRV')
        port = int(str(random.choice(dnsanswer_srv)).split()[2])
        return ip, port

