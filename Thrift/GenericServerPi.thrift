include "GenericStruct.thrift"
include "ThriftException.thrift"

service GenericPiThriftService {
    GenericStruct.GenericObject handleRequest(1: GenericStruct.GenericObject input) throws (1: ThriftException.ExternalEndpointUnavailable endPointUnavailiable 2: ThriftException.ThriftServiceException thriftException)
}

