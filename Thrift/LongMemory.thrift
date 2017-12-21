namespace java nl.earpi.generated.longmemory

include "GenericStruct.thrift"

#Login input
struct LoginInputObject {
    1 : required string username
    2 : optional string password
    3 : optional i16 code
}

struct LoginOutputObject {
    1 : required string person
    2 : required list<GenericStruct.ActionEnum> permissions
    3 : required string token
}

service LongMemoryService {
    LoginOutputObject loginCall(1: LoginInputObject loginobject)
}