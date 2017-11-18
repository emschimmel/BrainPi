include "GenericStruct.thrift"

service GenericPiThriftService {
    GenericStruct.GenericObject handleRequest(1: GenericStruct.GenericObject input)
}

