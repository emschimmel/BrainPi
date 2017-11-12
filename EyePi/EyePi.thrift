enum ActionEnum {
	LOGIN
	KAKU
	AGENDA
	MUSIC
}

struct PersonEntry {
	1 : required string person
	2 : required double chance
}

struct EyePiInput {
	1 : required ActionEnum action
	2 : optional list<string> actionParameters
	3 : required string deviceToken
	4 : optional string person
	5 : optional string token
	6 : optional binary image
}

struct EyePiOutput {
	1 : required bool ok
	2 : optional set<PersonEntry> personCollection
}

service EyePiThriftService {

    EyePiOutput handleRequest(1: EyePiInput input)
    oneway void writeLog(1: EyePiInput input)

}
