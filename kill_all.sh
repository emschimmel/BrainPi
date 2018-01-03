#!/usr/bin/env bash

# Kill PythonFacePiServer if running
FacePiServerPID=$(ps -ef | awk -F" " '/PythonFacePiServer.py/ && !/awk/{print $2}')
[[ !  -z  $FacePiServerPID  ]] && kill -9 $FacePiServerPID

# Kill PythonWeatherPiServer if running
WeatherPiServerPID=$(ps -ef | awk -F" " '/PythonWeatherPiServer.py/ && !/awk/{print $2}')
[[ !  -z  $WeatherPiServerPID  ]] && kill -9 $WeatherPiServerPID

# Kill PythonWeatherPiServer if running
PhotoPiServerPID=$(ps -ef | awk -F" " '/PythonPhotoPiServer.py/ && !/awk/{print $2}')
[[ !  -z  PhotoPiServerPID  ]] && kill -9 $PhotoPiServerPID

# Kill PythonWeatherPiServer if running
LightPiServerPID=$(ps -ef | awk -F" " '/PythonLightPiServer.py/ && !/awk/{print $2}')
[[ !  -z  LightPiServerPID  ]] && kill -9 $LightPiServerPID

# Kill PythonWeatherPiServer if running
AgendaPiServerPID=$(ps -ef | awk -F" " '/PythonAgendaPiServer.py/ && !/awk/{print $2}')
[[ !  -z  AgendaPiServerPID  ]] && kill -9 $AgendaPiServerPID

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
