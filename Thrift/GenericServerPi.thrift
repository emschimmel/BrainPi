include "GenericStruct.thrift"
include "ThriftException.thrift"

service GenericPiThriftService {
    binary handleRequest(1: binary input) throws (1: ThriftException.ExternalEndpointUnavailable endPointUnavailiable 2: ThriftException.ThriftServiceException thriftException)
    void ping(1: GenericStruct.PingObject pingObject) throws (1: ThriftException.ExternalEndpointUnavailable endPointUnavailiable 2: ThriftException.ThriftServiceException thriftException)
}

