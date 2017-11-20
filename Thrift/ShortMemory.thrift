include "GenericStruct.thrift"

typedef string Timestamp

enum ActionEnum {
	LOGIN
	KAKU
	AGENDA
	MUSIC
	WEATHER
}

struct TokenObject {
    1: required string deviceToken
	2: optional string person
	3: required string token
	4: optional binary image
	5: optional Timestamp date
    6: optional i64 time
}

struct LogObject {
    1: required ActionEnum action;
    2: optional GenericStruct.GenericObject actionParameters
    3: required string serviceName;
    4: required string message;
    5: optional string endpoint
    6: optional string person
    7: optional string deviceToken
    8: optional Timestamp date
}

struct Log {
    1: required Timestamp key
    2: optional LogObject value
}

service ShortMemoryService {
    string generateToken(1: TokenObject token)
    list<Log> readLog(1: Timestamp starttime, 2: Timestamp endtime, 3: i32 amount)
    bool validateToken(1: string token, 2: string deviceToken)
    oneway void writeLog(1: Log log)
}
