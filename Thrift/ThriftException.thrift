namespace java nl.earpi.generated.exception

exception ExternalEndpointUnavailable {
    1 : required string serviceName;
    2 : required string message;
    3 : optional string endpoint
}

exception ThriftServiceException {
    1 : required string serviceName;
    2 : required string message;
}

exception BadHashException {
    1 : required string serviceName = "LongMemoryPi";
    2 : required string message = "Unable to change the password";
}

exception LoginFailedException {
    1 : required string serviceName = "LongMemoryPi";
    2 : required string message = "Can't with login given credentials";
}

exception UniqueFailedException {
    1 : required string serviceName = "LongMemoryPi";
    2 : required string message = "Field has to be unique";
    3 : required list<string> fields
}