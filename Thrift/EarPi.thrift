namespace java nl.earpi.generated.earpi

include "GenericStruct.thrift"
include "AutorisationStruct.thrift"
include "ThriftException.thrift"

# Configure user management
# Configure module management
# Autorization (write mode)
# Entry point for device registration

struct EarPiAuthObject {
	1 : required string token
	2 : required string deviceToken
}

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

struct DeviceTokenItem {
    1 : required AutorisationStruct.DeviceTokenInput device
    2 : required string key
    3 : required bool active
}

struct UserListOutput {
    1 : list<AutorisationStruct.Person> personList
    2 : optional string token
}

struct DeviceTokenInput {
    1 : required string ip
    2 : required string devicetype
    3 : optional string userAgent
    4 : optional string person
    5 : required bool enabled = false
}

struct DeviceListOutput {
    1 : map<string, DeviceTokenInput> deviceList
    2 : optional string token
}

service EarPiThriftService {
    ### user management/account management get the person list
    UserListOutput getUserList(1: EarPiAuthObject tokenInput) throws (1: ThriftException.LoginFailedException fail)

    ### change a field of a specific user
    string changeUser(1: string field, 2: AutorisationStruct.Person person, 4: EarPiAuthObject tokenInput) throws (1: ThriftException.LoginFailedException fail)

    ### user management/account management enable/disable account access
    string configureUser(1: list<AutorisationStruct.Person> userList, 2: EarPiAuthObject tokenInput) throws (1: ThriftException.LoginFailedException fail)

    ### user module enable/disable
    string configureUserModule(1: string uniquename, 2: map<GenericStruct.ActionEnum, AutorisationStruct.Autorisation> autorisations, 3: EarPiAuthObject tokenInput) throws (1: ThriftException.LoginFailedException fail)

    ### change the module settings for a specific user and store in longterm
    string configureModuleSettings(1: string uniquename, 2: GenericStruct.ActionEnum action, 3: binary module_config, 4: EarPiAuthObject tokenInput) throws (1: ThriftException.LoginFailedException fail)

    ### get a list of registered devices (enabled + disabled
    DeviceListOutput getDeviceList(1: EarPiAuthObject tokenInput) throws (1: ThriftException.LoginFailedException fail)

    ### enable/disabe device access
    string confirmDevice(1: string deviceToken, 2: bool active, 3: EarPiAuthObject tokenInput) throws (1: ThriftException.LoginFailedException fail)

    ### change the password for a specific username
    string changePassword(1: string username, 2: string password, 3: EarPiAuthObject tokenInput) throws (1: ThriftException.BadHashException bad, 2: ThriftException.LoginFailedException fail)
}
