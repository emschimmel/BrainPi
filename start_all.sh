#!/usr/bin/env bash

export home="$PWD"

source kill_all.sh

### FacePi Server
cd ${home}/FacePi/py-impl
python3 PythonFacePiServer.py &

### WeatherPi Server
cd ${home}/WeatherPi/py-impl
python3 PythonWeatherPiServer.py &

### EyePi Server
cd ${home}/EyePi/py-impl
python3 PythonEyePiServer.py &

### ShortTermMemory Server
cd ${home}/ShortTermMemory/py-impl
python3 ShortTermMemoryServer.py &

### EyePi Start client
### Execute dummy client
sleep 15
cd ${home}/ClientPi/py-impl
python3 PythonEyePiClient.py