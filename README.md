# BrainPi

This is a microservice project.
It uses Thrift as a communication protocol.
The services register themself to consul and select a random port.

# Services:

Required services
- EyePi (main entry point)
- FacePi (will perform facerecognition)
- ShortTermMemory (stores application logs and tokens. In the future it will connect to Redis)
- LongTermMemory (not yet available)

Optional services (if a service is unavailable the ActionEnum action can't reach the required service).
- WeatherPi (available. get the actual weather based on a city)
- MusicPi (unavailable, name not fixed. will have playlists and connect to bluetooth speakers)
- AgendaPi (unavailable, name not fixed. will connect to a user apple agenda)
- KakuPi (unavailable, name not fixed. will connect 'Klik aan klik uit'/'LightweaveRF' to control lamps)

External requiries
- Consul

# Authentication:
Authentication is done by device registration wich will generate a DeviceToken.
For every call we need to provide a DeviceToken and eighter an image of a face or a token.

# Install:
Thrift/generate-sources.sh

pip install opencv, thrift, python-consul, dnspython, statsd, pyowm, hvac