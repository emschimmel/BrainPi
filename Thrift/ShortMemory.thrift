namespace java nl.earpi.generated.shortmemory

include "GenericStruct.thrift"

struct DeviceTokenInput {
    1 : required string ip
    2 : required string devicetype
    3 : optional string userAgent
    4 : optional string person
    5 : required bool enabled = false
}

struct TokenObject {
    1 : required string deviceToken
	2 : optional string person
	3 : required string token
	4 : optional binary image
	5 : optional string date
    6 : optional double time
    7 : optional string newToken
}

struct LogObject {
	1 : required map<GenericStruct.ActionEnum, binary> action
    2 : required string serviceName;
    3 : required string message;
    4 : optional string endpoint
    5 : optional string person
    6 : optional string deviceToken
    7 : optional string date
}

struct Log {
    1 : required double key
    2 : optional LogObject value
}

service ShortMemoryService {
    string generateToken(1: TokenObject token)
    list<Log> readLog(1: double starttime, 2: double endtime, 3: i32 amount)
    bool validateToken(1: string token, 2: string deviceToken)
    oneway void writeLog(1: Log log)
    string generateDeviceToken(1: DeviceTokenInput input)
    bool validateDeviceToken(1: string deviceToken)
    map<string, DeviceTokenInput> getDeviceList()
    oneway void confirmDevice(1: string deviceToken, 2: bool enabled)
}
