#!/usr/bin/env bash

export home="$PWD"

source kill_all.sh

### ShortTermMemory Server
cd ${home}/ShortTermMemory/py-impl
python3 ShortTermMemoryServer.py &

### LongTermMemory Server
cd ${home}/LongTermMemory/py-impl
python3 LongTermMemoryServer.py &

### EarPi Server
cd ${home}/EarPi/Python/py-impl
python3 PythonEarPiServer.py &

### EyePi Server
cd ${home}/EyePi/py-impl
python3 PythonEyePiServer.py &

### FacePi Server
cd ${home}/FacePi/py-impl
python3 PythonFacePiServer.py &

### WeatherPi Server
cd ${home}/WeatherPi/py-impl
python3 PythonWeatherPiServer.py &

### LightPi Server
cd ${home}/LightPi/py-impl
python3 PythonLightPiServer.py &

### AgendaPi Server
cd ${home}/AgendaPi/py-impl
python3 PythonAgendaPiServer.py &

### PhotoPi Server
cd ${home}/PhotoPi/py-impl
python3 PythonPhotoPiServer.py &

### PhotoPi Server
cd ${home}/MusicPi/py-impl
python3 PythonMusicPiServer.py &

### EyePi Start client
### Execute dummy client
#sleep 30
#cd ${home}/ClientPi/py-impl
#python3 CameraSimulation.py