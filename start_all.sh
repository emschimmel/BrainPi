#!/usr/bin/env bash

export home="$PWD"

source kill_all.sh

### ShortTermMemory Server
cd ${home}/ShortTermMemory/src
python3 ShortTermMemoryServer.py &

### LongTermMemory Server
cd ${home}/LongTermMemory/src
python3 LongTermMemoryServer.py &

### EarPi Server
cd ${home}/EarPi/src
python3 PythonEarPiServer.py &

### EyePi Server
cd ${home}/EyePi/src
python3 PythonEyePiServer.py &

### FacePi Server
cd ${home}/FacePi/src
python3 PythonFacePiServer.py &

### WeatherPi Server
cd ${home}/WeatherPi/src
python3 PythonWeatherPiServer.py &

### LightPi Server
cd ${home}/LightPi/src
python3 PythonLightPiServer.py &

### AgendaPi Server
cd ${home}/AgendaPi/
python3 src/PythonAgendaPiServer.py &

### PhotoPi Server
cd ${home}/PhotoPi/src
python3 PythonPhotoPiServer.py &

### PhonePi Server
cd ${home}/PhonePi/src
python3 PythonPhonePiServer.py &

### PhotoPi Server
cd ${home}/MusicPi/src
python3 PythonMusicPiServer.py &

### EyePi Start client
### Execute dummy client
#sleep 30
#cd ${home}/ClientPi/src
#python3 CameraSimulation.py

#cd ${home}/DeviceRegistrationUI/src
#go run main.go