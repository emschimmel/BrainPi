namespace java nl.earpi.generated.autorisationstruct

include "GenericStruct.thrift"

struct Autorisation {
    1 : required bool write_enabled = false
    2 : required bool enabled = false
    3 : optional binary module_config
}

struct DeviceTokenInput {
    1 : required string ip
    2 : required string devicetype
    3 : optional string userAgent
    4 : optional string person
}

struct user_detail {
    1 : optional string firstname
    2 : optional string lastname
    3 : optional string gender
    4 : optional string dob
}

struct Person {
    1 : optional string uniquename
    2 : optional user_detail details
    3 : optional string username
    4 : optional binary password
    5 : optional binary code
    6 : required bool enabled = true
    7 : optional map<GenericStruct.ActionEnum, Autorisation> autorisations
}