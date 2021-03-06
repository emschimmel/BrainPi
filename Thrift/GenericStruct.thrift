namespace java nl.earpi.generated.genericstruct
namespace go generated.genericstruct

enum ActionEnum {
	LOGIN = 0
	LIGHT = 1
	AGENDA = 2
	MUSIC = 3
	WEATHER = 4
	CONFIG = 5
	PHOTO = 6
	PHONE = 7
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

const Action light = {
    "actionEnum" :ActionEnum.LIGHT
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

const Action photo = {
    "actionEnum" :ActionEnum.PHOTO
    "uiType" :UiType.user
    "name":"Photo"
}

const Action phone = {
    "actionEnum" :ActionEnum.PHONE
    "uiType" :UiType.user
    "name":"Phone"
}

const list<Action> available_actions = {0: login, 1: light, 2:agenda, 3: music, 4: weather, 5: config, 6: photo, 7: phone}

struct PingObject {
    1 : optional ActionEnum action
    2 : optional string ip
    3 : optional i16 port
}
