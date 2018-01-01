#!/usr/bin/env bash

# Kill PythonFacePiServer if running
FacePiServerPID=$(ps -ef | awk -F" " '/PythonFacePiServer.py/ && !/awk/{print $2}')
[[ !  -z  $FacePiServerPID  ]] && kill -9 $FacePiServerPID

# Kill PythonWeatherPiServer if running
WeatherPiServerPID=$(ps -ef | awk -F" " '/PythonWeatherPiServer.py/ && !/awk/{print $2}')
[[ !  -z  $WeatherPiServerPID  ]] && kill -9 $WeatherPiServerPID

# Kill PythonEyePiServer if running
EyePiServerPID=$(ps -ef | awk -F" " '/PythonEyePiServer.py/ && !/awk/{print $2}')
[[ !  -z  $EyePiServerPID  ]] && kill -9 $EyePiServerPID

# Kill PythonEarPiServer if running
EarPiServerPID=$(ps -ef | awk -F" " '/PythonEarPiServer.py/ && !/awk/{print $2}')
[[ !  -z  $EarPiServerPID  ]] && kill -9 $EarPiServerPID

# Kill ShortTermMemoryServer if running
ShortTermMemoryServerPID=$(ps -ef | awk -F" " '/ShortTermMemoryServer.py/ && !/awk/{print $2}')
[[ !  -z  $ShortTermMemoryServerPID  ]] && kill -9 $ShortTermMemoryServerPID

# Kill LongTermMemoryServer if running
LongTermMemoryServerPID=$(ps -ef | awk -F" " '/LongTermMemoryServer.py/ && !/awk/{print $2}')
[[ !  -z  $LongTermMemoryServerPID  ]] && kill -9 $LongTermMemoryServerPID


#Kill consul
#ConsulPID=$(ps | awk -F" " 'consul agent -dev -enable-script-checks && !/awk/{print $1}')
#[[ !  -z  $ConsulPID  ]] && killall -9 $ConsulPID
