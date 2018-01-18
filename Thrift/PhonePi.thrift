# these actions are supported in the handle.
# For the input, it is the first field. Make the rest optional to work
enum Action {
	GET_LOCATION = 0
	GET_STATUS = 1
	PLAY_SOUND = 2
	LOST_MODE = 3
}

struct GetLocation {
    1 : required Action action = Action.GET_LOCATION
    2 : required string email
}

struct GetStatus {
    1 : required Action action = Action.GET_STATUS
    2 : required string email
}

struct PlaySound {
    1 : required Action action = Action.PLAY_SOUND
    2 : required string email
}

struct LostMode {
    1 : required Action action = Action.LOST_MODE
    2 : required string email
    3 : optional string phonenumber
    4 : optional string message
}

struct ConfigItem {
    1 : required string email
}