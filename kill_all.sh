#!/usr/bin/env bash

# Kill PythonFacePiServer if running
FacePiServerPID=$(ps | awk -F" " '/PythonFacePiServer.py/ && !/awk/{print $1}')
[[ !  -z  $FacePiServerPID  ]] && kill -9 $FacePiServerPID

# Kill PythonFacePiServer if running
WeatherPiServerPID=$(ps | awk -F" " '/PythonWeatherPiServer.py/ && !/awk/{print $1}')
[[ !  -z  $WeatherPiServerPID  ]] && kill -9 $WeatherPiServerPID

# Kill PythonFacePiServer if running
EyePiServerPID=$(ps | awk -F" " '/PythonEyePiServer.py/ && !/awk/{print $1}')
[[ !  -z  $EyePiServerPID  ]] && kill -9 $EyePiServerPID

# Kill PythonFacePiServer if running
ShortTermMemoryServerPID=$(ps | awk -F" " '/ShortTermMemoryServer.py/ && !/awk/{print $1}')
[[ !  -z  $ShortTermMemoryServerPID  ]] && kill -9 $ShortTermMemoryServerPID

#Kill consul
#ConsulPID=$(ps | awk -F" " 'consul agent -dev -enable-script-checks && !/awk/{print $1}')
#[[ !  -z  $ConsulPID  ]] && killall -9 $ConsulPID
