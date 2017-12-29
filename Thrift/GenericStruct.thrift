namespace java nl.earpi.generated.genericstruct

enum ActionEnum {
	LOGIN = 0
	KAKU = 1
	AGENDA = 2
	MUSIC = 3
	WEATHER = 4
	CONFIG = 5
}

enum UiType {
    admin = 0,
    user = 1
}

struct Action {
    1: ActionEnum actionEnum
    2: UiType uiType
    3: string name
}

const Action loginAction = {
    "actionEnum" : ActionEnum.LOGIN
    "uiType" : UiType.user
    "name": "Login"
}

const Action kaku = {
    "actionEnum" :ActionEnum.KAKU
    "uiType" :UiType.user
    "name":"Klik aan klik uit"
}

const Action agenda = {
    "actionEnum" :ActionEnum.AGENDA
    "uiType" :UiType.user
    "name":"Agenda"
}

const Action music = {
    "actionEnum" :ActionEnum.MUSIC
    "uiType" :UiType.user
    "name":"Music"
}

const Action weather = {
    "actionEnum" :ActionEnum.WEATHER
    "uiType" :UiType.user
    "name":"Weather"
}

const Action config = {
    "actionEnum" :ActionEnum.CONFIG
    "uiType" :UiType.admin
    "name":"Config"
}

const list<Action> available_actions = {0: login, 1: kaku, 2:agenda, 3: music, 4: weather, 5: config}

struct PingObject {
    1 : optional ActionEnum action
    2 : optional string ip
    3 : optional i16 port
}
