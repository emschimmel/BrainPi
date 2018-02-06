struct WeatherInput {
    1 : required string location
}

struct WeatherOutput {
    1 : required string humidity
    2 : required string wind_speed
    3 : required string wind_deg
    4 : required string temperature_temp
    5 : required string temperature_temp_max
    6 : required string temperature_temp_min
}