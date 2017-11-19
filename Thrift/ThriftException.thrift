exception ExternalEndpointUnavailable {
    1: required string serviceName;
    2: required string message;
    3: optional string endpoint
}

exception ThriftServiceException {
    1: required string serviceName;
    2: required string message;
}