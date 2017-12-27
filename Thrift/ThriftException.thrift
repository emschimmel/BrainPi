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