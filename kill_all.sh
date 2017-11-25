#!/usr/bin/env bash

# Kill PythonFacePiServer if running
FacePiServerPID=$(ps | awk -F" " '/PythonFacePiServer.py/ && !/awk/{print $1}')
[[ !  -z  $FacePiServerPID  ]] && kill -2 $FacePiServerPID

# Kill PythonFacePiServer if running
WeatherPiServerPID=$(ps | awk -F" " '/PythonWeatherPiServer.py/ && !/awk/{print $1}')
[[ !  -z  $WeatherPiServerPID  ]] && kill -2 $WeatherPiServerPID

# Kill PythonFacePiServer if running
EyePiServerPID=$(ps | awk -F" " '/PythonEyePiServer.py/ && !/awk/{print $1}')
[[ !  -z  $EyePiServerPID  ]] && kill -2 $EyePiServerPID

# Kill PythonFacePiServer if running
ShortTermMemoryServerPID=$(ps | awk -F" " '/ShortTermMemoryServer.py/ && !/awk/{print $1}')
[[ !  -z  $ShortTermMemoryServerPID  ]] && kill -2 $ShortTermMemoryServerPID
