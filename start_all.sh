#!/usr/bin/env bash

export home="$PWD"

# Kill PythonFacePiServer if running
FacePiServerPID=$(ps | awk -F" " '/PythonFacePiServer.py/ && !/awk/{print $1}')
[[ !  -z  $FacePiServerPID  ]] && kill -9 $FacePiServerPID

# Kill PythonFacePiServer if running
WeatherPiServerPID=$(ps | awk -F" " '/PythonWeatherPiServer.py/ && !/awk/{print $1}')
[[ !  -z  $WeatherPiServerPID  ]] && kill -9 $WeatherPiServerPID

# Kill PythonFacePiServer if running
EyePiServerPID=$(ps | awk -F" " '/PythonEyePiServer.py/ && !/awk/{print $1}')
[[ !  -z  $EyePiServerPID  ]] && kill -9 $EyePiServerPID

### FacePi Server
cd ${home}/FacePi/py-impl
python3 PythonFacePiServer.py &

### WeatherPi Server
cd ${home}/WeatherPi/py-impl
python3 PythonWeatherPiServer.py &

### EyePi Server
cd ${home}/EyePi/py-impl
python3 PythonEyePiServer.py &

### EyePi Start client
### Execute dummy client
sleep 1
cd ${home}/ClientPi/py-impl
python3 PythonEyePiClient.py