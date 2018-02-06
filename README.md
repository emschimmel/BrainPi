# BrainPi

This is a microservice project.
It uses Thrift as a communication protocol.
The services register themself to consul and select a random port.

# Services:

Required services
- EyePi (main entry point for read authentication actions)
- FacePi (will perform facerecognition)
- ShortTermMemory (stores application logs and tokens. Can connect to Redis and Elasticsearch, but has local mock storages if unavailable)
- LongTermMemory (stores account data. Can connect to Mongo, but has a local mock if mongo is unavailable)

- Earpi (main entry point for write authentication +autorisation actions).
* My resume needed Spring boot, that is why it is in Java. But will rewrite this service to Python soon

Optional services (if a service is unavailable the ActionEnum action can't reach the required service).
- WeatherPi (available. get the actual weather based on a city)
- MusicPi (unavailable, name not fixed. will have playlists and connect to bluetooth speakers)
- AgendaPi (available, connects to a user apple agenda. Needs to have device registered)
- LightPi (available, connects to 'Klik aan klik uit'/'LightweaveRF' to control lamps)
- PhotoPi (available, connects to a user apple photos. Needs to have device registered)

External requiries
- Consul (can eighter run in a docker container together with Registrator and the databases, or as local consul)

SetupDevEnv
- Docker environment with Registrator. This is complete optional and can be used instead of normal local development. We will implement no Docker specific things, because the environment will not use Docker on a Raspberri.

# Authentication:
Authentication is done by device registration wich will generate a DeviceToken.
For every call we need to provide a DeviceToken and eighter an image of a face or a token.

# Install:
1. pip install opencv, thrift, python-consul, dnspython, statsd, pyowm, hvac
2. Thrift/generate-sources.sh

# Start
1. if docker: ./SetupDevEnv/run_docker.sh
else: consul agent -dev
2. ./start_all.sh

# Stop
1. if docker: ./SetupDevEnv/stop_docker.sh
2. ./kill_all.sh


