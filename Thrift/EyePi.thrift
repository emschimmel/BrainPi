include "GenericStruct.thrift"
include "ThriftException.thrift"

struct PersonEntry {
	1 : required string person
	2 : required double chance
	3 : optional binary image
}

struct EyePiInput {
	1 : required GenericStruct.ActionEnum action
	2 : optional GenericStruct.GenericObject actionParameters
	3 : required string deviceToken
	4 : optional string person
	5 : optional string token
	6 : optional binary image
}

struct ConfirmInput {
    1 : required binary image
    2 : required string person
}

struct EyePiOutput {
	1 : required bool ok
	2 : optional list<PersonEntry> personCollection
	3 : optional string token
	4 : optional GenericStruct.GenericObject data
}

service EyePiThriftService {
    EyePiOutput handleRequest(1: EyePiInput input) throws (1: ThriftException.ExternalEndpointUnavailable endPointUnavailiable 2: ThriftException.ThriftServiceException thriftException)
    oneway void confimFace(1: ConfirmInput input)
    oneway void writeLog(1: EyePiInput input)
    void ping(1: GenericStruct.PingObject pingObject) throws (1: ThriftException.ExternalEndpointUnavailable endPointUnavailiable 2: ThriftException.ThriftServiceException thriftException)
}
