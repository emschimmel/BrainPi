struct WeatherPiInput {
	1 : required string location
}

struct WeatherPiOutput {
	1 : required string temperature
}

service WeatherPiThriftService {
    WeatherPiOutput handleRequest(1: WeatherPiInput input)
}

