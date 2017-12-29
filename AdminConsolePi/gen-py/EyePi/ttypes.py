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
import GenericStruct.ttypes
import ThriftException.ttypes
import AutorisationStruct.ttypes

from thrift.transport import TTransport


class PersonEntry(object):
    """
    Attributes:
     - person
     - chance
     - image
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'person', 'UTF8', None, ),  # 1
        (2, TType.DOUBLE, 'chance', None, None, ),  # 2
        (3, TType.STRING, 'image', 'BINARY', None, ),  # 3
    )

    def __init__(self, person=None, chance=None, image=None,):
        self.person = person
        self.chance = chance
        self.image = image

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
                if ftype == TType.STRING:
                    self.person = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.DOUBLE:
                    self.chance = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.image = iprot.readBinary()
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
        oprot.writeStructBegin('PersonEntry')
        if self.person is not None:
            oprot.writeFieldBegin('person', TType.STRING, 1)
            oprot.writeString(self.person.encode('utf-8') if sys.version_info[0] == 2 else self.person)
            oprot.writeFieldEnd()
        if self.chance is not None:
            oprot.writeFieldBegin('chance', TType.DOUBLE, 2)
            oprot.writeDouble(self.chance)
            oprot.writeFieldEnd()
        if self.image is not None:
            oprot.writeFieldBegin('image', TType.STRING, 3)
            oprot.writeBinary(self.image)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.person is None:
            raise TProtocolException(message='Required field person is unset!')
        if self.chance is None:
            raise TProtocolException(message='Required field chance is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class EyePiInput(object):
    """
    Attributes:
     - action
     - deviceToken
     - person
     - token
     - image
    """

    thrift_spec = (
        None,  # 0
        (1, TType.MAP, 'action', (TType.I32, None, TType.STRING, 'BINARY', False), None, ),  # 1
        (2, TType.STRING, 'deviceToken', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'person', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'token', 'UTF8', None, ),  # 4
        (5, TType.STRING, 'image', 'BINARY', None, ),  # 5
    )

    def __init__(self, action=None, deviceToken=None, person=None, token=None, image=None,):
        self.action = action
        self.deviceToken = deviceToken
        self.person = person
        self.token = token
        self.image = image

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
                if ftype == TType.MAP:
                    self.action = {}
                    (_ktype1, _vtype2, _size0) = iprot.readMapBegin()
                    for _i4 in range(_size0):
                        _key5 = iprot.readI32()
                        _val6 = iprot.readBinary()
                        self.action[_key5] = _val6
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.deviceToken = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.person = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.token = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.image = iprot.readBinary()
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
        oprot.writeStructBegin('EyePiInput')
        if self.action is not None:
            oprot.writeFieldBegin('action', TType.MAP, 1)
            oprot.writeMapBegin(TType.I32, TType.STRING, len(self.action))
            for kiter7, viter8 in self.action.items():
                oprot.writeI32(kiter7)
                oprot.writeBinary(viter8)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        if self.deviceToken is not None:
            oprot.writeFieldBegin('deviceToken', TType.STRING, 2)
            oprot.writeString(self.deviceToken.encode('utf-8') if sys.version_info[0] == 2 else self.deviceToken)
            oprot.writeFieldEnd()
        if self.person is not None:
            oprot.writeFieldBegin('person', TType.STRING, 3)
            oprot.writeString(self.person.encode('utf-8') if sys.version_info[0] == 2 else self.person)
            oprot.writeFieldEnd()
        if self.token is not None:
            oprot.writeFieldBegin('token', TType.STRING, 4)
            oprot.writeString(self.token.encode('utf-8') if sys.version_info[0] == 2 else self.token)
            oprot.writeFieldEnd()
        if self.image is not None:
            oprot.writeFieldBegin('image', TType.STRING, 5)
            oprot.writeBinary(self.image)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.action is None:
            raise TProtocolException(message='Required field action is unset!')
        if self.deviceToken is None:
            raise TProtocolException(message='Required field deviceToken is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ConfirmInput(object):
    """
    Attributes:
     - image
     - person
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'image', 'BINARY', None, ),  # 1
        (2, TType.STRING, 'person', 'UTF8', None, ),  # 2
    )

    def __init__(self, image=None, person=None,):
        self.image = image
        self.person = person

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
                if ftype == TType.STRING:
                    self.image = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.person = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('ConfirmInput')
        if self.image is not None:
            oprot.writeFieldBegin('image', TType.STRING, 1)
            oprot.writeBinary(self.image)
            oprot.writeFieldEnd()
        if self.person is not None:
            oprot.writeFieldBegin('person', TType.STRING, 2)
            oprot.writeString(self.person.encode('utf-8') if sys.version_info[0] == 2 else self.person)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.image is None:
            raise TProtocolException(message='Required field image is unset!')
        if self.person is None:
            raise TProtocolException(message='Required field person is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class EyePiOutput(object):
    """
    Attributes:
     - ok
     - personCollection
     - token
     - data
    """

    thrift_spec = (
        None,  # 0
        (1, TType.BOOL, 'ok', None, None, ),  # 1
        (2, TType.LIST, 'personCollection', (TType.STRUCT, (PersonEntry, PersonEntry.thrift_spec), False), None, ),  # 2
        (3, TType.STRING, 'token', 'UTF8', None, ),  # 3
        (4, TType.MAP, 'data', (TType.I32, None, TType.STRING, 'BINARY', False), None, ),  # 4
    )

    def __init__(self, ok=None, personCollection=None, token=None, data=None,):
        self.ok = ok
        self.personCollection = personCollection
        self.token = token
        self.data = data

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
                if ftype == TType.BOOL:
                    self.ok = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.personCollection = []
                    (_etype12, _size9) = iprot.readListBegin()
                    for _i13 in range(_size9):
                        _elem14 = PersonEntry()
                        _elem14.read(iprot)
                        self.personCollection.append(_elem14)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.token = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.MAP:
                    self.data = {}
                    (_ktype16, _vtype17, _size15) = iprot.readMapBegin()
                    for _i19 in range(_size15):
                        _key20 = iprot.readI32()
                        _val21 = iprot.readBinary()
                        self.data[_key20] = _val21
                    iprot.readMapEnd()
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
        oprot.writeStructBegin('EyePiOutput')
        if self.ok is not None:
            oprot.writeFieldBegin('ok', TType.BOOL, 1)
            oprot.writeBool(self.ok)
            oprot.writeFieldEnd()
        if self.personCollection is not None:
            oprot.writeFieldBegin('personCollection', TType.LIST, 2)
            oprot.writeListBegin(TType.STRUCT, len(self.personCollection))
            for iter22 in self.personCollection:
                iter22.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.token is not None:
            oprot.writeFieldBegin('token', TType.STRING, 3)
            oprot.writeString(self.token.encode('utf-8') if sys.version_info[0] == 2 else self.token)
            oprot.writeFieldEnd()
        if self.data is not None:
            oprot.writeFieldBegin('data', TType.MAP, 4)
            oprot.writeMapBegin(TType.I32, TType.STRING, len(self.data))
            for kiter23, viter24 in self.data.items():
                oprot.writeI32(kiter23)
                oprot.writeBinary(viter24)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.ok is None:
            raise TProtocolException(message='Required field ok is unset!')
        if self.data is None:
            raise TProtocolException(message='Required field data is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class LoginInputObject(object):
    """
    Attributes:
     - username
     - password
     - code
     - deviceInput
     - deviceToken
     - token
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'username', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'password', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'code', 'UTF8', None, ),  # 3
        (4, TType.STRUCT, 'deviceInput', (AutorisationStruct.ttypes.DeviceTokenInput, AutorisationStruct.ttypes.DeviceTokenInput.thrift_spec), None, ),  # 4
        (5, TType.STRING, 'deviceToken', 'UTF8', None, ),  # 5
        (6, TType.STRING, 'token', 'UTF8', None, ),  # 6
    )

    def __init__(self, username=None, password=None, code=None, deviceInput=None, deviceToken=None, token=None,):
        self.username = username
        self.password = password
        self.code = code
        self.deviceInput = deviceInput
        self.deviceToken = deviceToken
        self.token = token

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
                if ftype == TType.STRING:
                    self.username = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.password = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.code = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRUCT:
                    self.deviceInput = AutorisationStruct.ttypes.DeviceTokenInput()
                    self.deviceInput.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.deviceToken = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.token = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('LoginInputObject')
        if self.username is not None:
            oprot.writeFieldBegin('username', TType.STRING, 1)
            oprot.writeString(self.username.encode('utf-8') if sys.version_info[0] == 2 else self.username)
            oprot.writeFieldEnd()
        if self.password is not None:
            oprot.writeFieldBegin('password', TType.STRING, 2)
            oprot.writeString(self.password.encode('utf-8') if sys.version_info[0] == 2 else self.password)
            oprot.writeFieldEnd()
        if self.code is not None:
            oprot.writeFieldBegin('code', TType.STRING, 3)
            oprot.writeString(self.code.encode('utf-8') if sys.version_info[0] == 2 else self.code)
            oprot.writeFieldEnd()
        if self.deviceInput is not None:
            oprot.writeFieldBegin('deviceInput', TType.STRUCT, 4)
            self.deviceInput.write(oprot)
            oprot.writeFieldEnd()
        if self.deviceToken is not None:
            oprot.writeFieldBegin('deviceToken', TType.STRING, 5)
            oprot.writeString(self.deviceToken.encode('utf-8') if sys.version_info[0] == 2 else self.deviceToken)
            oprot.writeFieldEnd()
        if self.token is not None:
            oprot.writeFieldBegin('token', TType.STRING, 6)
            oprot.writeString(self.token.encode('utf-8') if sys.version_info[0] == 2 else self.token)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.username is None:
            raise TProtocolException(message='Required field username is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class LoginOutputObject(object):
    """
    Attributes:
     - uniquename
     - details
     - deviceToken
     - token
     - autorisations
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'uniquename', 'UTF8', None, ),  # 1
        (2, TType.STRUCT, 'details', (AutorisationStruct.ttypes.user_detail, AutorisationStruct.ttypes.user_detail.thrift_spec), None, ),  # 2
        (3, TType.STRING, 'deviceToken', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'token', 'UTF8', None, ),  # 4
        (5, TType.MAP, 'autorisations', (TType.I32, None, TType.STRUCT, (AutorisationStruct.ttypes.Autorisation, AutorisationStruct.ttypes.Autorisation.thrift_spec), False), None, ),  # 5
    )

    def __init__(self, uniquename=None, details=None, deviceToken=None, token=None, autorisations=None,):
        self.uniquename = uniquename
        self.details = details
        self.deviceToken = deviceToken
        self.token = token
        self.autorisations = autorisations

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
                if ftype == TType.STRING:
                    self.uniquename = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.details = AutorisationStruct.ttypes.user_detail()
                    self.details.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.deviceToken = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.token = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.MAP:
                    self.autorisations = {}
                    (_ktype26, _vtype27, _size25) = iprot.readMapBegin()
                    for _i29 in range(_size25):
                        _key30 = iprot.readI32()
                        _val31 = AutorisationStruct.ttypes.Autorisation()
                        _val31.read(iprot)
                        self.autorisations[_key30] = _val31
                    iprot.readMapEnd()
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
        oprot.writeStructBegin('LoginOutputObject')
        if self.uniquename is not None:
            oprot.writeFieldBegin('uniquename', TType.STRING, 1)
            oprot.writeString(self.uniquename.encode('utf-8') if sys.version_info[0] == 2 else self.uniquename)
            oprot.writeFieldEnd()
        if self.details is not None:
            oprot.writeFieldBegin('details', TType.STRUCT, 2)
            self.details.write(oprot)
            oprot.writeFieldEnd()
        if self.deviceToken is not None:
            oprot.writeFieldBegin('deviceToken', TType.STRING, 3)
            oprot.writeString(self.deviceToken.encode('utf-8') if sys.version_info[0] == 2 else self.deviceToken)
            oprot.writeFieldEnd()
        if self.token is not None:
            oprot.writeFieldBegin('token', TType.STRING, 4)
            oprot.writeString(self.token.encode('utf-8') if sys.version_info[0] == 2 else self.token)
            oprot.writeFieldEnd()
        if self.autorisations is not None:
            oprot.writeFieldBegin('autorisations', TType.MAP, 5)
            oprot.writeMapBegin(TType.I32, TType.STRUCT, len(self.autorisations))
            for kiter32, viter33 in self.autorisations.items():
                oprot.writeI32(kiter32)
                viter33.write(oprot)
            oprot.writeMapEnd()
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
