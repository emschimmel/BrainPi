typedef list<GenericSubStruct> ListValue
typedef set<GenericSubStruct> SetValue
typedef map<string, GenericSubStruct> MapValue

struct GenericSubStruct {
    1 : optional string stringValue
    2 : optional i64 intValue
    3 : optional double doubleValue
    4 : optional bool boolValue
    5 : optional binary binaryValue
}

struct GenericObject {
    1 : optional string stringValue
    2 : optional i64 intValue
    3 : optional double doubleValue
    4 : optional bool boolValue
    5 : optional binary binaryValue
    6 : optional ListValue listValue
    7 : optional SetValue setValue
    8 : optional MapValue mapvalue
}

