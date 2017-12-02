enum ActionEnum {
	LOGIN
	KAKU
	AGENDA
	MUSIC
	WEATHER
}

struct PingObject {
    1 : optional ActionEnum action
    2 : optional string ip
    3 : optional i16 port
}
