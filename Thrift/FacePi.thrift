struct PersonEntry {
	1 : required string person
	2 : required double chance
	3 : optional binary image
}

struct FacePiInput {
	1 : required binary image
}

struct FacePiOutput {
	1 : optional list<PersonEntry> personCollection
}

struct ConfirmInput {
    1 : required binary image
    2 : required string person
}

service FacePiThriftService {

    FacePiOutput handleRequest(1: FacePiInput input)
    oneway void confimFace(1: ConfirmInput input)

}
