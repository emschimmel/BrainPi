namespace java nl.earpi.generated.earpi

include "GenericStruct.thrift"
# Configure user management
# Configure module management
# Autorization (write mode)
# Entry point for device registration

# configuration manager input
struct ConfigurationInput {
    1 : required map<string, binary> keyValueMap
    2 : required string deviceToken
	3 : optional string token
}

# configuration manager output
struct ConfigurationOutput {
    1 : bool ok
}

# module management input
struct ModuleAutorizationInput {
    1 : required map<GenericStruct.ActionEnum, bool> moduleMap
    2 : required string person
    3 : required string deviceToken
	4 : optional string token
}

struct DeviceTokenInput {
    1 : required string ip
    2 : required string devicetype
    3 : optional string userAgent
    4 : optional string person
}

# device registration input
struct LoginInputObject {
    1 : required string username
    2 : optional string password
    3 : optional i16 code
    4 : optional DeviceTokenInput deviceInput
    5 : optional string deviceToken
    6 : optional string token
}

# device registration output
struct LoginOutputObject {
    1 : optional string name
    2 : optional string deviceToken
    3 : optional string token
    4 : required list<GenericStruct.ActionEnum> action
}