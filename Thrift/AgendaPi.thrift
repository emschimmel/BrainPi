# these actions are supported in the handle.
# For the input, it is the first field. Make the rest optional to work
enum Action {
	GET_ITEMS = 0
	MAKE_ITEM = 1
}

struct GetItemsActionInput {
    1 : required Action action = Action.GET_ITEMS
    2 : required string email
    3 : optional i16 startDay
    4 : optional i16 startMonth
    5 : optional i16 startYear
    6 : optional i16 endDay
    7 : optional i16 endMonth
    8 : optional i16 endYear
}

struct MakeItemActionInput {
    1 : required Action action = Action.MAKE_ITEM
    2 : required string email
}