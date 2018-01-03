enum Action {
	GET_FLOOR_LAYOUT = 0
	PERFORM_ACTION = 1
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
    1 : required string name
    2 : required DeviceType type
}

struct Room {
    1 : required i16 number
    2 : required string name
    3 : optional list<Device> deviceCollection
}

struct Floor {
    1 : required string name
    2 : optional list<Room> roomCollection
}

struct LightActionInput {
    1 : required Action action = Action.PERFORM_ACTION
    2 : optional Device device
    3 : optional DeviceState state
}

struct LightActionOutput {
    1 : required bool ok
}

struct GetFloorInput {
    1 : required Action action = Action.GET_FLOOR_LAYOUT
}

struct GetFloorOutput {
    1 : required list<Floor> floor
}
