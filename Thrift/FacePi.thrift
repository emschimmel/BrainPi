namespace java nl.earpi.generated.exception

include "ThriftException.thrift"

struct PersonEntry {
	1 : required string person
	2 : required double chance
	3 : optional binary image
	4 : optional string algoritm
}

struct FacePiInput {
	1 : required binary image
}

struct FacePiOutput {
	1 : optional list<PersonEntry> personCollection
}

struct ConfirmInput {
    1 : required binary image
    2 : required string person
}

service FacePiThriftService {
    FacePiOutput handleRequest(1: FacePiInput input) throws (1: ThriftException.ExternalEndpointUnavailable endPointUnavailiable 2: ThriftException.ThriftServiceException thriftException)
    oneway void confimFace(1: ConfirmInput input)

}

