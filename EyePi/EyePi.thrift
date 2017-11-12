enum ActionEnum {
	LOGIN
	KAKU
	AGENDA
	MUSIC
}

struct PersonEntry {
	1 : string person
	2 : double chance
}

struct EyePiInput {
	1 : ActionEnum action
	2 : list<string> actionParameters
	3 : string deviceToken
	4 : string person
	5 : string token
	6 : binary image
}

struct EyePiOutput {
	1 : bool ok
	2 : set<PersonEntry> personCollection
}

