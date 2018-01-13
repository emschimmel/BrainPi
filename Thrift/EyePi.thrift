include "GenericStruct.thrift"
include "ThriftException.thrift"
include "AutorisationStruct.thrift"

struct PersonEntry {
	1 : required string person
	2 : required double chance
	3 : optional binary image
}

struct EyePiInput {
	1 : required map<GenericStruct.ActionEnum, binary> action
	2 : required string deviceToken
	3 : optional string person
	4 : optional string token
	5 : optional binary image
}

struct ConfirmInput {
    1 : required binary image
    2 : required string person
}

struct EyePiOutput {
	1 : required bool ok
	2 : optional list<PersonEntry> personCollection
	3 : optional string token
	4 : required map<GenericStruct.ActionEnum, binary> data
}

# device registration input
struct LoginInputObject {
    1 : required string username
    2 : optional binary password
    3 : optional binary code
    4 : optional AutorisationStruct.DeviceTokenInput deviceInput
    5 : optional string deviceToken
    6 : optional string token
}

# device registration output
struct LoginOutputObject {
    1 : optional string uniquename
    2 : optional AutorisationStruct.user_detail details
    3 : optional string deviceToken
    4 : optional string token
    5 : optional map<GenericStruct.ActionEnum, AutorisationStruct.Autorisation> autorisations
}

service EyePiThriftService {
    EyePiOutput handleRequest(1: EyePiInput input) throws (1: ThriftException.ExternalEndpointUnavailable endPointUnavailiable 2: ThriftException.ThriftServiceException thriftException)
    oneway void confimFace(1: ConfirmInput input)
    oneway void writeLog(1: EyePiInput input)
    void ping(1: GenericStruct.PingObject pingObject) throws (1: ThriftException.ExternalEndpointUnavailable endPointUnavailiable 2: ThriftException.ThriftServiceException thriftException)
    LoginOutputObject login(1: LoginInputObject loginObject) throws (1: ThriftException.BadHashException bad, 2: ThriftException.LoginFailedException fail)
}
