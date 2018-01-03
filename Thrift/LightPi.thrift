# these actions are supported in the handle.
# For the input, it is the first field. Make the rest optional to work
enum Action {
	GET_FLOOR_LAYOUT = 0
	UPDATE_FLOOR_LAYOUT = 1
	PERFORM_ACTION = 2
}

enum DeviceType {
	LAMP = 0
	DIM_LAMP = 1
	ON_OFF = 2
}

enum DeviceState {
    STATE_ON = 0
    STATE_OFF = 1
    STATE_DIM = 2
    STATE_LOW = 8
    STATE_MED = 16
    STATE_HIGH = 24
}

struct Device {
    1 : required i16 number
    2 : required string name
    3 : required bool enabled = true
    4 : required DeviceType type
}

struct Room {
    1 : required i16 number
    2 : required string name
    3 : required bool enabled = true
    4 : optional list<Device> deviceCollection
}

struct Floor {
    1 : required i16 number
    2 : required string name
    3 : required bool enabled = true
    4 : optional list<Room> roomCollection
}

struct LightActionInput {
    1 : required Action action = Action.PERFORM_ACTION
    2 : optional i16 roomNumber
    3 : optional i16 deviceNumber
    4 : optional DeviceState state
    5 : optional i16 optionalValue
//    6 : optional string msg1
//    7 : optional string msg2
}

struct GetFloorInput {
    1 : required Action action = Action.GET_FLOOR_LAYOUT
}

struct UpdateFLoorLayoutInput {
    1 : required Action action = Action.UPDATE_FLOOR_LAYOUT
    2 : optional binary floorjson
}

struct GetFloorOutput {
    1 : required list<Floor> floorCollection
}

struct GenericOkOutput {
    1 : required bool ok = true
}
