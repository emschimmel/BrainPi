namespace java nl.earpi.generated.longmemory

include "AutorisationStruct.thrift"
include "ThriftException.thrift"



#Login input
struct LongMemoryLoginInputObject {
    1 : required string username
    2 : optional string password
    3 : optional string code
}



service LongMemoryService {
    AutorisationStruct.Person loginCall(1: LongMemoryLoginInputObject loginobject) throws(1: ThriftException.BadHashException bad, 2: ThriftException.LoginFailedException fail)
    AutorisationStruct.Person getPersonConfig(1: string uniquename)
    list<AutorisationStruct.Person> getAll()
    void storeNewPerson(1: AutorisationStruct.Person person)
    void changePassword(1: string username, 2: string password) throws(1: ThriftException.BadHashException badHashException)
}