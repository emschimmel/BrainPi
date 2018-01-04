# these actions are supported in the handle.
# For the input, it is the first field. Make the rest optional to work
enum Action {
	GET_PLAYLISTS = 0
	GET_PLAYLIST = 1
	GET_SONG = 2
	PLAY_SONG = 3
	SEARCH = 4
	START_PLAYING = 5
	STOP_PLAYING = 6
}

struct GetPlaylistsInput {
    1 : required Action action = Action.GET_PLAYLISTS
}


struct GetPlaylistInput {
    1 : required Action action = Action.GET_PLAYLIST
    2 : optional string name
}

struct GetSongInput {
    1 : required Action action = Action.GET_SONG
    2 : optional string name
}

struct PlaySongInput {
    1 : required Action action = Action.PLAY_SONG
    2 : optional string name
}

struct SearchInput {
    1 : required Action action = Action.SEARCH
    2 : optional string name
}

struct StartPlayingInput {
    1 : required Action action = Action.START_PLAYING
    2 : optional string name
}

struct StopPlayingInput {
    1 : required Action action = Action.STOP_PLAYING
    2 : optional string name
}

struct GetPlaylistOutput {
    1 : required list<string> playlists
}

struct GetSongsOutput {
    1 : required list<string> songs
    2 : optional string playlistname
}

