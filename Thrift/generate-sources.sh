#!/usr/bin/env bash

thrift -gen py EyePi.thrift
thrift -gen py FacePi.thrift
thrift -gen py WeatherPi.thrift

# EyePI
cp -Rf ./gen-py/EyePi ../EyePi/gen-py/

# FacePI
cp -Rf ./gen-py/FacePi ../EyePi/gen-py/
cp -Rf ./gen-py/FacePi ../FacePi/gen-py/

# WeatherPI
cp -Rf ./gen-py/WeatherPi ../EyePi/gen-py/
cp -Rf ./gen-py/WeatherPi ../WeatherPi/gen-py/