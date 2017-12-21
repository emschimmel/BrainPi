#
# Autogenerated by Thrift Compiler (0.10.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
import sys

from thrift.transport import TTransport


class ActionEnum(object):
    LOGIN = 0
    KAKU = 1
    AGENDA = 2
    MUSIC = 3
    WEATHER = 4
    CONFIG = 5

    _VALUES_TO_NAMES = {
        0: "LOGIN",
        1: "KAKU",
        2: "AGENDA",
        3: "MUSIC",
        4: "WEATHER",
        5: "CONFIG",
    }

    _NAMES_TO_VALUES = {
        "LOGIN": 0,
        "KAKU": 1,
        "AGENDA": 2,
        "MUSIC": 3,
        "WEATHER": 4,
        "CONFIG": 5,
    }


class UiType(object):
    admin = 0
    user = 1

    _VALUES_TO_NAMES = {
        0: "admin",
        1: "user",
    }

    _NAMES_TO_VALUES = {
        "admin": 0,
        "user": 1,
    }


class Action(object):
    """
    Attributes:
     - actionEnum
     - uiType
     - name
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'actionEnum', None, None, ),  # 1
        (2, TType.I32, 'uiType', None, None, ),  # 2
        (3, TType.STRING, 'name', 'UTF8', None, ),  # 3
    )

    def __init__(self, actionEnum=None, uiType=None, name=None,):
        self.actionEnum = actionEnum
        self.uiType = uiType
        self.name = name

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.actionEnum = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.uiType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('Action')
        if self.actionEnum is not None:
            oprot.writeFieldBegin('actionEnum', TType.I32, 1)
            oprot.writeI32(self.actionEnum)
            oprot.writeFieldEnd()
        if self.uiType is not None:
            oprot.writeFieldBegin('uiType', TType.I32, 2)
            oprot.writeI32(self.uiType)
            oprot.writeFieldEnd()
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 3)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class PingObject(object):
    """
    Attributes:
     - action
     - ip
     - port
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'action', None, None, ),  # 1
        (2, TType.STRING, 'ip', 'UTF8', None, ),  # 2
        (3, TType.I16, 'port', None, None, ),  # 3
    )

    def __init__(self, action=None, ip=None, port=None,):
        self.action = action
        self.ip = ip
        self.port = port

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.action = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.ip = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.port = iprot.readI16()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('PingObject')
        if self.action is not None:
            oprot.writeFieldBegin('action', TType.I32, 1)
            oprot.writeI32(self.action)
            oprot.writeFieldEnd()
        if self.ip is not None:
            oprot.writeFieldBegin('ip', TType.STRING, 2)
            oprot.writeString(self.ip.encode('utf-8') if sys.version_info[0] == 2 else self.ip)
            oprot.writeFieldEnd()
        if self.port is not None:
            oprot.writeFieldBegin('port', TType.I16, 3)
            oprot.writeI16(self.port)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
