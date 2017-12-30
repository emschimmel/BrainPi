#!/usr/bin/env python

import pyowm

# Parse configuration
from configparser import ConfigParser

parser = ConfigParser()
parser.read('../config/weather.ini')

class OpenWeather:
    def __init__(self):
        self.log = {}

    def getWeather(self, input):
        owm = pyowm.OWM(parser.get('DEFAULT', 'owmapikey'))
        observation = owm.weather_at_place(input)
        w = observation.get_weather()
        return w.get_wind(), w.get_humidity(), w.get_temperature('celsius')
