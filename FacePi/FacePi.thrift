struct PersonEntry {
	1 : string person
	2 : double chance
}

struct FacePiInput {
	1 : binary image
}

struct FacePiOutput {
	1 : set<PersonEntry> personCollection	
}

