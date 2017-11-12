struct PersonEntry {
	1 : required string person
	2 : required double chance
}

struct FacePiInput {
	1 : required binary image
}

struct FacePiOutput {
	1 : optional list<PersonEntry> personCollection
}

service FacePiThriftService {

    FacePiOutput handleRequest(1: FacePiInput input)

}

