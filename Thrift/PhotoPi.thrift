# these actions are supported in the handle.
# For the input, it is the first field. Make the rest optional to work
enum Action {
	GET_PHOTOS = 0
	GET_RANDOM_PHOTO = 1
}

struct GetPhotosActionInput {
    1 : required Action action = Action.GET_PHOTOS
    2 : required string email
    3 : required i16 limit = 1
}

struct GetRandomPhotoActionInput {
    1 : required Action action = Action.GET_RANDOM_PHOTO
    2 : required string email
    3 : required i16 limit = 1
}

struct ConfigItem {
    1 : required string email
}