namespace java nl.earpi.generated.earpi

include "GenericStruct.thrift"
include "AutorisationStruct.thrift"

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

struct DeviceTokenItem {
    1 : required AutorisationStruct.DeviceTokenInput device
    2 : required bool active
}

service EarPiService {
    list<AutorisationStruct.Person> getUserList() # user management/account management
    oneway void configureUser(1: list<AutorisationStruct.Person> userList) # user management/account management
    oneway void configureUserModule(1: string person, 2: map<GenericStruct.ActionEnum, AutorisationStruct.Autorisation> autorisations)  # user module enable/disable
    oneway void configureModuleSettings(1: string person, 2: GenericStruct.ActionEnum action, 3: binary module_config) # change the module settings and store in longterm
    list<DeviceTokenItem> getDeviceList()
    oneway void confirmDevice(1: string deviceToken, 2: bool active)

}
