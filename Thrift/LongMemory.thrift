namespace java nl.earpi.generated.longmemory

include "GenericStruct.thrift"
include "ThriftException.thrift"

struct user_detail {
    1 : optional string firstname
    2 : optional string lastname
    3 : optional string gender
    4 : optional string dob
}

struct autorisation {
    1 : required bool write
    2 : required bool enabled
    3 : optional binary module_config
}

struct Person {
    1 : required string uniquename
    2 : optional user_detail details
    3 : optional string username
    4 : optional string password
    5 : optional string code
    6 : required bool enabled = true
    7 : optional map<GenericStruct.ActionEnum, autorisation> autorisations
}

#Login input
struct LongMemoryLoginInputObject {
    1 : required string username
    2 : optional string password
    3 : optional string code
}

struct LongMemoryLoginOutputObject {
    1 : optional string person
    2 : optional string token
}

service LongMemoryService {
    LongMemoryLoginOutputObject loginCall(1: LongMemoryLoginInputObject loginobject) throws(1: ThriftException.BadHashException badHashException)
    Person getPersonConfig(1: string uniquename)
    list<Person> getAll()
    void storeNewPerson(1: Person person)
    void changePassword(1: string username, 2: string password) throws(1: ThriftException.BadHashException badHashException)
}