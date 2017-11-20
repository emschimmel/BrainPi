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
	3: optional string token
	4: optional binary image
}

struct Token {
    1: required string key // person + device
    2: optional TokenObject value
}

struct Person {
    1: required string person
    2: required string deviceToken
}

struct LogObject {

    1: required ActionEnum action;
    2: optional GenericStruct.GenericObject actionParameters
    3: required string serviceName;
    4: required string message;
    5: optional string endpoint
    6: optional string person
    7: optional string deviceToken
}

struct Log {
    1: required Timestamp key
    2: optional LogObject value
}

service ShortMemoryService {
    Person getPerson(1: Token token)
    Token getToken(1: Token token)
    oneway void writeToken(1: Token token)
    oneway void writeLog(1: Log log)
    list<Log> readLog(1: Timestamp starttime, 2: Timestamp endtime, 3: i32 amount)
}
