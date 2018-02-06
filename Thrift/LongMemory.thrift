namespace java nl.earpi.generated.longmemory

include "AutorisationStruct.thrift"
include "ThriftException.thrift"
include "GenericStruct.thrift"


#Login input
struct LongMemoryLoginInputObject {
    1 : required string username
    2 : optional binary password
    3 : optional binary code
}

service LongMemoryService {
    AutorisationStruct.Person loginCall(1: LongMemoryLoginInputObject loginobject) throws(1: ThriftException.BadHashException bad, 2: ThriftException.LoginFailedException fail)
    AutorisationStruct.Person getPersonConfig(1: string uniquename)
    list<AutorisationStruct.Person> getAll()
    void updateActionConfig(1: string uniquename, 2: GenericStruct.ActionEnum action, 3: binary config)
    void storeNewPerson(1: AutorisationStruct.Person person) throws(1: ThriftException.UniqueFailedException unique)
    void updatePerson(1: string field 2: AutorisationStruct.Person person)
    void changePassword(1: string username, 2: binary password) throws(1: ThriftException.BadHashException bad)
}